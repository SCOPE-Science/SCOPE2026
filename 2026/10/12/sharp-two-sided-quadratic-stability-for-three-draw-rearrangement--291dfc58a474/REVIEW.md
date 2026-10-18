# Independent mathematical audit

## correctness

PASS

Recomputed F_q(p)=6-9s_2+4s_3 from three disjoint occupancy types (all identical, one pair, all distinct); the centered cubic deficit has exactly the two sum-of-squares certificates printed in RESULT.md. Independent SymPy elimination of one simplex coordinate verifies BOTH polynomial certificates identically for q=3 and q=4 (symbolic residual 0), with separate simple q=2 identity. All factors are nonnegative on the simplex: pairs use 1-p_i-p_j>=0; Schur triples use a sorted-variable decomposition. Vanishing conditions give precisely vertices for the lower nonuniform extremizers and uniform-on-q-1 support for upper, with uniform always equality. The algebraic certificate plus sign/equality argument proves all q>=2; numeric finite grids are not infinite proof.

## originality

PASS

The two optimal global q-dependent coefficients with complete, different boundary equality classes are new relative to the compared exact published mathematical statements: Biswas et al. prove qualitative uniform maximality for all draw lengths; Resultary e3a60ec2aa94 gives a nonsharp d(d-1)/2 lower bound (3 at d=3); Resultary 49b4f93ca348 gives local Hessian only. The full Gonçalves permutation-match manuscript and older Rinott treatment were not accessible, so stronger implications remain a substantial, explicit priority risk. Best-of-knowledge PASS restricted to this precise sharpened three-draw quantitative theorem, not a claim of novel qualitative rearrangement extremality.

## value

PASS

The sharp global two-sided quadratic stability of a canonical sampling functional is a motivated quantitative refinement of the classical extremal inequality; computing BOTH best constants and boundary equality classes controls loss in terms of a natural distance even at sparse/extreme probability vectors, unlike local Hessian or a nonsharp general bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
