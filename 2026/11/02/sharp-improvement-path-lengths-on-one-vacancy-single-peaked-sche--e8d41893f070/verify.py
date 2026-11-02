"""Exact finite checks for one-vacancy single-peaked jump games on cycles.

Uses only the Python standard library. This is a finite consistency check,
not a substitute for the general combinatorial proof.
"""
from fractions import Fraction as F
from itertools import combinations
from functools import lru_cache


def utility(q, peak):
    return q / peak if q <= peak else (1-q)/(1-peak)


def same_fraction(state, i):
    n = len(state)
    assert state[i] in 'RB'
    vals = [state[j] for j in ((i-1)%n,i,(i+1)%n) if state[j] != '.']
    return F(sum(c == state[i] for c in vals), len(vals))


def apply(state, i):
    z=state.index('.')
    out=list(state)
    out[z],out[i]=out[i],out[z]
    return ''.join(out)


def improving(state, i, peak):
    z=state.index('.')
    if i==z: return False
    new=apply(state,i)
    return utility(same_fraction(new,z),peak)>utility(same_fraction(state,i),peak)


def mono(state):
    n=len(state)
    return sum(state[i] in 'RB' and state[i]==state[(i+1)%n] for i in range(n))


def homogeneous_hole(state):
    i=state.index('.')
    return state[(i-1)%len(state)]==state[(i+1)%len(state)]


def iter_states(n,b):
    for z in range(n):
        available=[i for i in range(n) if i!=z]
        for bs in combinations(available,b):
            s=['R']*n;s[z]='.'
            for i in bs:s[i]='B'
            yield ''.join(s)


def longrun_second(state, color):
    runs=[]
    j=0
    while j<len(state):
        if state[j]!=color:j+=1;continue
        k=j
        while k<len(state) and state[k]==color:k+=1
        runs.append((k-j,j))
        j=k
    length,start=max(runs)
    assert length>=3,(state,color,runs)
    return start+1


def move_assert(state,i,peak):
    assert improving(state,i,peak),(state,i,peak)
    return apply(state,i)


def lower_path(n,peak):
    """Witness for n-3 strict improvements when 0<peak<1/2."""
    assert n>=3 and peak<F(1,2)
    m=n//2
    a=m-1;c=m if n%2 else m-1
    s='R'*a+'.'+'B'*c+'R'
    path=[s]
    for j in range((m-1) if n%2 else (m-2)):
        # The penultimate B in the long B block moves to the vacancy.
        pos=a+1+c-2
        s=move_assert(s,pos,peak);path.append(s)
        # The last R of the initial run moves into a B-flanked vacancy.
        pos=a-1
        s=move_assert(s,pos,peak);path.append(s)
        a-=1;c-=1
        assert s=='R'*a+'.'+'B'*c+'RB'*(j+1)+'R'
    if n%2==0:
        # Last adjacent R leaves the final monochromatic bond.
        s=move_assert(s,0,peak);path.append(s)
    assert len(path)-1==n-3
    return path


def upper_path(n,peak):
    """Witness for floor((n-2)/2) strict improvements, peak>=1/2."""
    assert n>=3 and peak>=F(1,2)
    r=n//2;b=n-1-r
    s='.'+'R'*r+'B'*b
    path=[s]
    bound=(n-2)//2
    if not bound:return path
    if n%4!=2:
        s=move_assert(s,1,peak);path.append(s)
        for t in range(2,bound+1):
            if t%2==0:
                # Last contiguous B-run, of length at least three.
                j=len(s)-1
                while s[j]!='B':j-=1
                k=j
                while k>=0 and s[k]=='B':k-=1
                assert j-k>=3
                i=k+2
            else:
                i=longrun_second(s,'R')
            s=move_assert(s,i,peak);path.append(s)
    else:
        # First jump is the second B of the original B block.
        s=move_assert(s,r+2,peak);path.append(s)
        for t in range(2,bound+1):
            if t%2==0:
                i=longrun_second(s,'R')
            else:
                # This is a B flanked by B, in the remaining B run.
                candidates=[i for i,c in enumerate(s)
                            if c=='B' and s[(i-1)%n]=='B' and s[(i+1)%n]=='B']
                assert candidates
                i=candidates[-1]
            s=move_assert(s,i,peak);path.append(s)
    assert len(path)-1==bound
    return path


def check():
    nstates=nedges=0
    for peak in (F(1,4),F(1,2),F(3,4)):
        for n in range(3,11):
            best=0
            for b in range(1,(n-1)//2+1):
                states=list(iter_states(n,b))
                @lru_cache(None)
                def length(s):
                    return max((1+length(apply(s,i)) for i in range(n)
                                if improving(s,i,peak)),default=0)
                for s in states:
                    nstates+=1
                    h=homogeneous_hole(s);m=mono(s)
                    for i in range(n):
                        if improving(s,i,peak):
                            nedges+=1
                            t=apply(s,i);hh=homogeneous_hole(t);mm=mono(t)
                            if peak<=F(1,2): assert mm<m
                            if peak>=F(1,2):
                                if h:assert hh and mm==m-2
                                else:assert hh
                    d=length(s)
                    best=max(best,d)
                    assert d<= (n-3 if peak<F(1,2) else (n-2)//2)
            assert best==(n-3 if peak<F(1,2) else (n-2)//2),(n,peak,best)
    constructions=0
    for n in range(3,101):
        for peak in (F(1,100),F(2,5),F(1,2),F(3,5),F(99,100)):
            path=lower_path(n,peak) if peak<F(1,2) else upper_path(n,peak)
            assert all(improving(s,next(i for i in range(n) if s[i]!='.' and t[i]=='.'),peak)
                       for s,t in zip(path,path[1:]))
            constructions+=1
    print('PASS states',nstates,'improving moves',nedges,'constructive families',constructions)

if __name__=='__main__':check()
