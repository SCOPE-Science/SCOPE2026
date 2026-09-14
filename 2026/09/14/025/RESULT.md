# Realizability of the genus-0 degree-12 Belyi passport (4-2-1^6, 5-4-3, 7-3-2)

## Context
The admitted target asks whether the genus-zero degree-12 passport
P4 = ([4,2,1,1,1,1,1,1], [5,4,3], [7,3,2]) over {0,1,infinity} is realized by a
connected cover f: P^1_C -> P^1_C branched only over three points. The partition
lengths are 8+3+3=14, so Riemann-Hurwitz gives 2g-2 = -24+(4+9+9) = -2, i.e.
g=0, which is necessary but not sufficient. Realizability requires an explicit
transitive triple in S12 with the stated cycle types and product one, or a
rigorous obstruction. No field-of-definition statement is required for the
complex realizability question.

## Definitions
Permutations are 0-indexed image arrays on sheets {0,...,11} with composition
compose(a,b)[i] = b[a[i]] (apply a first). A triple (v0,v1,vinf) satisfies
v0*v1*vinf = id. Its passport is the triple of cycle types. It is transitive if
<v0,v1> acts transitively; the monodromy group is L = <v0,v1> and the cover
automorphism group is the centralizer of L in S12. The Nielsen census fixes one
coordinate and counts pairs (x,y) with xyz=1 modulo simultaneous conjugation;
pure-braid and full-braid orbits act by standard Hurwitz moves.

## Result
The passport is realizable over C. With
v0 = [1,2,3,0,5,4,6,7,8,9,10,11],
v1 = [11,10,4,5,7,9,3,2,6,8,0,1],
vinf = [10,11,7,6,1,2,8,5,9,4,0,3],
the 1-indexed cycles are [[1,2,3,4],[5,6]], [[1,12,2,11],[3,5,8],[4,6,10,9,7]],
[[1,11],[2,12,4,7,9,10,5],[3,8,6]], of exact types (4,2,1^6), (5,4,3),
(7,3,2). They satisfy v0*v1*vinf = id and generate a transitive subgroup.
The monodromy group is L = S12 of order 479001600, and Aut = 1. Census data:
Frobenius count N = 4088 pairs for fixed z of type (7,3,2); 142 simultaneous
conjugacy classes of which 66 are transitive; pure-braid orbit of the reported
class has length 1; full-braid orbit has length 6 with one class in each ordered
slice.

## Proof / evidence
Direct machine verification (01_triple.py): cycle types, product identity,
transitivity, and Riemann-Hurwitz counts check exactly. Group identification
(02_group_id.py) proceeds two independent ways: (i) vinf^6 is a verified
7-cycle, so with primitivity Jordan's theorem (p=7 <= 12-3) forces L >= A12 and
the odd generators v1, vinf lift to S12; (ii) sympy computes |<v0,v1>| = 12!
with transitivity and primitivity confirmed. The centralizer of S12 is trivial.
The structure constant N = 4088 is proved both by a Murnaghan-Nakayama
character sum (validated against the S4 table and column orthogonality) and by
independent brute-force enumeration of all 83160 elements of class (4,2,1^6)
(census.py, re-executed in audit). Nielsen classification (nielsen_correct.py)
and braid computations (braid_correct.py, fullbraid.py) were re-executed and
confirm 142/66 and orbit lengths 1 and 6. All scripts need only Python plus
sympy.

## Limitations
Realizability over C only. Field of moduli, field of definition, explicit
rational or number-field model coefficients, and the Galois partition of the 66
transitive Nielsen classes are not established. Numerical model-solving
attempts were attracted to an extraneous degenerate locus and are reported as
negative evidence only. The census numbers are exact for the stated slices but
do not by themselves identify fields of definition.

## Reproducibility
From output/artifacts run 01_triple.py, 02_group_id.py, census.py,
nielsen_correct.py, and sc.py. Expected outputs: types
(4,2,1,1,1,1,1,1)/(5,4,3)/(7,3,2), product identity true, transitive true,
vinf^6 type [7,1^5], order 479001600, N=4088, 142 classes with 66 transitive.

## References
Musty-Schiavone-Sijsling-Voight, A database of Belyi maps (2019);
LMFDB Belyi maps section (degree <= 9); Wang et al., Hurwitz existence problem
and prime-degree conjecture (2025); Riemann-Hurwitz and Jordan theorems as
cited in the verification scripts.
