# Falsification of the claimed d >= 9 certificate for the named 3x5 array symmetric lifted-product code at lift 7

## Context

Finite-length certified distances for quantum LDPC codes strictly above the
stabilizer/counting bound m+n, and explicit degenerate witnesses for named
lifted-product (LP) instances, are open after Panteleev-Kalachev asymptotics
and Raveendran-Declercq-Vasic row-and-column partition constraints (RCPC).
The admitted target claimed, for a named 238-qubit symmetric quasi-cyclic LP
CSS code Q* (3x5 all-ones protograph, lift L=7, Fossorier array exponents),
max stabilizer weight w0=8 and distance d(Q*)>=9 via Tanner expansion
|N(S)|>=2|S| for |S|<=4 plus a bounded-weight ILP trace. This record
rigorously falsifies both operative clauses for the exact instance.

## Definitions

Let L=7 and E=[[0,0,0,0,0],[0,1,2,3,4],[0,2,4,6,1]] mod 7.
Let B be the binary 21x35 quasi-cyclic base matrix of the 3x5 all-ones
protograph: row (i,a), column (j,b) has entry 1 iff b-a=E[i][j] mod 7.
Let Q*=LP(B,B) be the symmetric lifted-product CSS code with the standard
ring-level block formulas over R=F2[C7], A=B, B*=conjugate transpose:

  H_X = [A (x) I_5 | I_3 (x) B*],  H_Z = [I_5 (x) B | A* (x) I_3],

realised as binary 105x238 matrices with index maps:
block-1 columns (j1,q,b)->(j1*5+q)*7+b (0..174);
block-2 columns (s,l,b)->175+(s*3+l)*7+b (175..237);
H_X rows (i1,p,a)->(i1*5+p)*7+a; H_Z rows (p',q',a)->(p'*3+q')*7+a.
So N=7*(25+9)=238. All arithmetic is exact over F2.

## Result

For the instance above:

1. H_X H_Z^T=0 (valid CSS pair); every row of H_X and H_Z has weight 8,
   so w0=8.
2. rank(H_X)=rank(H_Z)=97, hence k=238-97-97=44>0.
3. The classical base code ker(B) has exact minimum distance d(B)=6
   (full 2^16 kernel census; distribution {6:21,8:98,10:658,12:2947,
   14:9306,16:15449,18:17108,20:12362,22:5593,24:1764,26:210,28:19}).
4. The vector l with support {0,4,10,18,21,24} (weight 6) satisfies
   H_Z l=0 and l not in rowspace(H_X) (rank augmentation 97->98).
   Hence l is a non-trivial X-logical of weight 6 and d(Q*)<=6,
   refuting the claimed d(Q*)>=9.
5. The Tanner-expansion clause |N(S)|>=2|S| for all |S|<=4 is false:
   it holds for |S|=1,2,3 but fails on 84 four-sets
   (e.g. {0,1,21,29} with |N|=7<8).

## Proof / Evidence

Exact F2 integer-bit computation, stdlib only:
- CSS orthogonality by direct even-overlap check (0 violations);
  row weights 5+3=8 by construction; ranks by reduced bit-echelon (97/97).
- Classical census: rank(B)=19, dim ker(B)=16; enumerating all 65535
  nonzero kernel vectors (nullspace verified B v=0) gives min weight 6
  attained by 21 words.
- Lift: writing H_Z=[I tensor B | A* tensor I], for c in ker(B) and
  basis e_j in F2^5, v_{j,c}=[e_j tensor c;0] satisfies H_Z v=0.
  Census over all 21*5=105 weight-6 lifts and 98*5=490 weight-8 lifts
  shows every one has zero H_Z-syndrome and nonzero remainder modulo
  rowspace(H_X): all are genuine logicals, none stabilizers.
- Explicit witness: classical word c with (var,shift) support
  {(0,0),(0,4),(1,3),(2,4),(3,0),(3,3)} lies in ker(B) (each of 21 checks
  even; machine-verified). Its lift at block j=0,
  l=[e_0 tensor c;0] with support {0,4,10,18,21,24}, has H_Z l=0
  (105 checks, all even) and rank(H_X+l)=98 != 97. So d(Q*)<=6<9.
- Expansion: neighbourhoods from B, variable (j,b) sees checks
  {(i,(b-E[i][j]) mod 7)}. Exhaustive enumeration of all
  35+595+6545+52360=59535 subsets of sizes 1-4 gives 0 failures for
  sizes 1-3 and 84 failures at size 4.
Auditor independently re-ran all scripts byte-identical and cross-checked
ranks/distance/orthogonality with a separate bytearray Gauss-Jordan
implementation (same results).

## Limitations

- Shown: d(Q*)<=6; both operative target clauses (distance bound and
  expansion certificate) are false for the named instance.
- Not shown: exact distance (could be <6 via mixed-block or Z-logicals);
  only the upper bound <=6, sufficient to falsify d>=9.
- Uses the canonical symmetric-LP block formula; any equivalent
  row/column permutation preserves weights, ranks, and distance.

## Reproducibility

```
python3 output/artifacts/build.py     # matrices, ranks, kernel census, expansion log
python3 output/artifacts/disprove.py  # lift census + witness + disproof.json
python3 output/artifacts/verify.py    # re-derivation from (E,L)+witness -> VERIFY_OK
```

Dependencies: Python 3 stdlib only. Runtime seconds.

## References

- N. Raveendran, D. Declercq, B. Vasic, On the Minimum Distances of
  Finite-Length Lifted Product Quantum LDPC Codes, arXiv:2503.07567.
  (RCPC necessary conditions; conditional bound min(d_C,m+n); no 3x5 L=7
  array instance, no ranks/witness/expansion log.)
- P. Panteleev, G. Kalachev, Quantum LDPC Codes With Almost Linear
  Minimum Distance, IEEE Trans. Inf. Theory 68 (2022).
- P. Panteleev, G. Kalachev, Degenerate Quantum LDPC Codes With Good
  Finite Length Performance, Quantum 5, 585 (2021).
- Lifted-product (LP) code, Error Correction Zoo.
- Quasi-cyclic LDPC (QC-LDPC) code, Error Correction Zoo.
