#!/usr/bin/env python3
"""Exact finite checks for a homogeneous edge-transmission path model.
Run with Python 3 standard library only; prints deterministic JSON certificate.
"""
import json
from fractions import Fraction
from itertools import product


def gap_tail(length, threshold, p):
    if length < threshold:
        return Fraction(0)
    return p ** (threshold - 1) * ((threshold - (threshold - 1) * p) * length - threshold * (threshold - 1) * (1 - p))


def gap_mean(length, p):
    return Fraction(length) + 2 * sum((length - distance) * p ** distance for distance in range(1, length))


def enumerate_edges(length, threshold, p):
    e = t = Fraction(0)
    for bits in product((0, 1), repeat=max(0, length-1)):
        prob = Fraction(1)
        for bit in bits:
            prob *= p if bit else (1-p)
        for v in range(length):
            left = right = v
            while left and bits[left-1]:
                left -= 1
            while right < length-1 and bits[right]:
                right += 1
            size = right-left+1
            e += prob*size
            t += prob*(size >= threshold)
    return e,t


def compositions(total, count):
    if count == 1:
        yield (total,)
    else:
        for first in range(total+1):
            for rest in compositions(total-first,count-1):
                yield (first,)+rest


def run():
    direct_cases=0
    for p in (Fraction(1,3),Fraction(1,2),Fraction(2,3)):
        for length in range(8):
            for threshold in range(2,9):
                assert enumerate_edges(length,threshold,p)==(gap_mean(length,p),gap_tail(length,threshold,p))
                direct_cases+=1
    profiles=cases=0
    for k in range(2,5):
        b=k+1
        for N in range(3,10):
            for threshold in range(3,N+1):
                for p in (Fraction(1,3), Fraction(2,3)):
                    z=list(compositions(N,b))
                    scores=[(sum((gap_tail(x,threshold,p) for x in a),Fraction(0)),sum((gap_mean(x,p) for x in a),Fraction(0))) for a in z]
                    mt=min(v[0] for v in scores)
                    me=min(v[1] for v in scores)
                    q,r=divmod(N,b)
                    for a,(tv,ev) in zip(z,scores):
                        if N<=b*(threshold-1):
                            optimal_tail=max(a)<=threshold-1
                        else:
                            optimal_tail=sorted(a)==[threshold-1]*(b-1)+[N-(b-1)*(threshold-1)]
                        optimal_mean=sorted(a)==[q]*(b-r)+[q+1]*r
                        assert (tv==mt)==optimal_tail,('tail',k,N,threshold,p,a)
                        assert (ev==me)==optimal_mean,('mean',k,N,threshold,p,a)
                    cases+=1
                    profiles+=len(z)
    p=Fraction(1,2)
    example={}
    for name,gaps in (('mean_opt',[4,3,3]),('tail_opt',[6,2,2])):
        avg=sum((gap_mean(z,p) for z in gaps),Fraction(0))/10
        tail=sum((gap_tail(z,3,p) for z in gaps),Fraction(0))/10
        example[name]={'gaps':gaps,'mean':str(avg),'tail_at_3':str(tail)}
    return {'schema_version':1,'arithmetic':'exact rational','direct_edge_enumeration_cases':direct_cases,'global_parameter_configurations':cases,'optimality_profile_evaluations':profiles,'example':example,'limitation':'Finite checks support but do not prove statements for unrestricted parameters.'}

if __name__=='__main__':
    print(json.dumps(run(),sort_keys=True,separators=(',',':')))
