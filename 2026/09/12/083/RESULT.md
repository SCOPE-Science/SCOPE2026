# Computational simple-module table for the parafermion VOA K(G2,2)

## Background
For G2 at level 2, the integrable affine highest weights are 0, w1, w2, 2w2. Since P=Q for G2 and Q/2Q_L has order 12, the standard parafermion module classification gives 48 simple-module labels. The computation here evaluates their lowest coset weights and top multiplicities from affine weight multiplicities/string functions.

## Computed table
Using Delta(0)=0, Delta(w1)=2/3, Delta(w2)=1/3, Delta(2w2)=7/9 and classes (i,j) modulo 2Z alpha1 + 6Z alpha2, the archived computation gives:

- L=0: (0,0) h=0,t=1; (0,1),(0,5),(1,1),(1,2),(1,4),(1,5) h=5/6,t=1; (0,2),(0,4) h=4/3,t=3; (0,3),(1,0),(1,3) h=1/2,t=1.
- L=w1: (0,0) h=2/3,t=2; the six classes above h=1/2,t=1; (0,2),(0,4) h=1,t=3; (0,3),(1,0),(1,3) h=1/6,t=1.
- L=w2: (0,0) h=1/3,t=1; the six classes above h=1/6,t=1; (0,2),(0,4) h=2/3,t=3; (0,3),(1,0),(1,3) h=5/6,t=3.
- L=2w2: (0,0) h=7/9,t=3; the six classes above h=11/18,t=2; (0,2),(0,4) h=1/9,t=1; (0,3),(1,0),(1,3) h=5/18,t=1.

Because the VOA is rational, its Zhu algebra is semisimple and the table gives dim A = sum t^2 = 149. The vacuum string coefficients beginning 1,2,11,35,114,317,847, when multiplied by the eta^2 product, give vacuum-character coefficients 1,0,6,13,38,80,182 through grade 6.

## Clarification of the top multiplicity
Several theta-translated affine weights in the same class can attain the same value of F=36n-9|w|^2. They are representatives of the same string-function sector, not independent top-space copies. The top multiplicity t is the common string-function coefficient at the minimum. It is **not** the sum over all theta-translated minimizers. The previous wording suggesting such a sum was incorrect.

## Independent stability check
The filed scripts used finite affine-weight boxes. The independent audit repeated the Freudenthal-Kac recursion for all four level-2 modules with a larger box B=20 and grades through 7; all 48 minimizing (F,t) pairs agree with the filed B=14/grade-5 table. This is strong computational stabilization evidence, while not a formal proof of a universal truncation bound.

## Reproducibility
Use `artifacts/sectors.py`, `artifacts/stringql.py`, `artifacts/kac2.py`, `artifacts/sectors.json`, and `artifacts/stringQL.json`. The earlier `output/artifacts/...` paths were repository-path errors.

## Scope
This is a computational table built on the published classification/rationality theory. It does not establish a priority claim for the numerical table, nor does it settle the generator-relation or classically-free questions for K(G2,2).

## References
- Dong and Ren, representation theory/rationality for parafermion VOAs.
- Ai, Dong, Jiang and Lin, irreducible modules, quantum dimensions and fusion rules for parafermion VOAs.
- Arakawa, Lam and Yamada, Zhu/C2 results for parafermion VOAs, arXiv:1207.3909.
