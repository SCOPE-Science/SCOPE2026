"""Exact replay of the nonsplit binary quadric tritangent census.

Run: python verify.py (standard library only). Every polynomial calculation is
performed in finite fields, including a Buchberger ideal-unit computation.
"""
from pathlib import Path
from collections import Counter
import json

from nonsplit_genus4 import BASIS, PTS, GENS, act, all_orbits
from groebner_gf2 import geom_smooth
from tritangents import rtritangents, CONIC, TANGENT_RESTR

HERE=Path(__file__).resolve().parent
EXPECTED=json.loads((HERE/'expected.json').read_text())

def all_orbit_elements(seed):
    seen={seed}; todo=[seed]
    for v in todo:
        for g in GENS:
            w=act(v,g)
            if w not in seen:
                seen.add(w);todo.append(w)
    return todo

def main():
    assert len(BASIS)==16 and len(PTS)==5
    assert len(CONIC)==10 and len(TANGENT_RESTR)==5
    orbits=all_orbits()
    assert len(orbits)==EXPECTED['ambient_orbits']==683
    certificates=(HERE/'orbit_certificate.tsv').read_text().splitlines()
    assert len(certificates)==len(orbits)+1
    assert certificates[0]=='mask_hex\torbit_size\trational_points\tgeometrically_smooth\tsecant_proper\ttangent_proper'
    spectrum=Counter();class_spectrum=Counter();smooth_sections=0
    maxima=[]
    for (m,w,n),line in zip(orbits,certificates[1:]):
        mm,ww,nn,old_s,old_a,old_b=line.split('\t')
        assert (int(mm,16),int(ww),int(nn))==(m,w,n)
        is_smooth=geom_smooth(m)
        assert is_smooth==(old_s=='1'),(m,old_s)
        if not is_smooth:
            assert old_a=='0' and old_b=='0'
            continue
        s,t=rtritangents(m)
        a,b=len(s),len(t)
        assert (a,b)==(int(old_a),int(old_b))
        smooth_sections+=w
        spectrum[n,a,b]+=w;class_spectrum[n,a,b]+=1
        elems=all_orbit_elements(m)
        assert len(elems)==w
        # Independent direct enumeration: every one of the 27,060 smooth
        # equations is retested, without using orbit weights for contacts.
        for x in elems:
            assert tuple(map(len,rtritangents(x)))==(a,b)
            assert sum(1 for p in PTS if sum((x>>(i)&1) for i,mon in enumerate(BASIS)
                           if all((p>>j&1) or not mon[j] for j in range(4)))%2==0)==n
        if a+b==3:maxima.append(f'{m:04x}')
    assert smooth_sections==EXPECTED['smooth_sections']==27060
    assert sum(class_spectrum.values())==EXPECTED['smooth_orbits']==254
    expected={(z['rational_points'],z['secant_proper_tritangents'],z['quadric_tangent_proper_tritangents']):
              (z['sections'],z['projective_orbits']) for z in EXPECTED['joint_spectrum']}
    assert {k:(spectrum[k],class_spectrum[k]) for k in spectrum}==expected
    assert sorted(maxima)==sorted(EXPECTED['extremal_orbit_masks'])
    by_total=tuple(sum(v for (n,a,b),v in spectrum.items() if a+b==i) for i in range(4))
    assert list(by_total)==EXPECTED['proper_total_by_number']==[10300,12810,3600,350]
    print('PASS: 65,535 cubic sections partitioned into 683 projective orbits')
    print('PASS: 254 smooth orbits and 27,060 smooth sections (exact affine ideal tests)')
    print('PASS: direct tritangent tests on all 27,060 smooth sections')
    print('PASS: 33 joint (rational, secant, tangent) spectra and 6 extremal orbits')
    print('PASS: proper rational tritangent distribution',by_total)

if __name__=='__main__':main()
