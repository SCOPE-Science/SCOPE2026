# Finite-monodromy seeds cannot yield the Boalch–Klein 7-branch Painlevé VI solution

## Context
The Boalch–Klein solution is the seven-branch algebraic Painlevé VI solution with exponent data `(2,2,2,4)/7`. The statement below is correct, but it is not a new structural theorem: it is an immediate RS-pullback corollary of Boalch’s published Lemma 7, which proves that the explicit `SL_2(C)` monodromy triple for the Klein solution generates an infinite subgroup of `SU_2`.

## Result
No RS-pullback realization of the Boalch–Klein solution can start from a hypergeometric equation with finite projective monodromy, in any pullback degree.

## Proof
For a rational pullback of a linear differential equation, the pulled-back monodromy representation is the seed representation composed with the induced map on the punctured fundamental group. Its image is therefore a subgroup of the seed monodromy image. Schlesinger transformations preserve the monodromy representation up to the usual conjugacy/integer-exponent changes and do not turn a finite monodromy image into an infinite one.

Boalch gives explicit matrices `M1,M2,M3` for the Klein solution and proves in Lemma 7 of `math/0308221` that the group they generate is an infinite subgroup of `SU_2`. Hence a finite-monodromy hypergeometric seed cannot produce this target by any rational pullback followed by Schlesinger transformations.

An elementary alternative check is also available from the displayed matrices: `M1` and `M2` give noncommuting projective elements of order 7. The Platonic finite groups `A4,S4,A5` have no elements of order 7; a cyclic seed is abelian; and in a (binary) dihedral group all odd-order elements lie in the cyclic rotation subgroup and commute. This excludes every Schwarz finite-monodromy type directly.

## Originality and value
The no-finite-seed conclusion should be cited as a corollary of Boalch’s infinite-monodromy lemma plus standard pullback functoriality, not as an independent new theorem. The elementary order-7 argument is still a useful compact RS-specific proof and clarifies that any search for an RS realization of this solution may restrict attention to infinite-monodromy hypergeometric seeds.

## Limitations
This result says nothing about the minimal degree of an RS realization with an infinite-monodromy seed. In particular it does not prove a universal degree lower bound of 11, nor does it rule out an infinite-seed realization in degree at most 10.

## References
- P. Boalch, *From Klein to Painlevé via Fourier, Laplace and Jimbo*, arXiv:math/0308221, especially Remark 6 and Lemma 7.
- R. Vidunas and A. Kitaev, *Computation of RS-pullback transformations for algebraic Painlevé VI solutions*, arXiv:0705.2963.
