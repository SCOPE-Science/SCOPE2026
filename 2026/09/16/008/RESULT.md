# Saturated closure of the braided-admitting S-Witt equivalence

## Context
Work over C. Let Fus be the commutative monoid of monoidal-equivalence classes of fusion categories under Deligne product, NBFC that of nondegenerate braided fusion categories, and Z1 the Drinfeld-center construction. For a submonoid S of Fus, A,B in NBFC are S-Witt equivalent when A x Z1(P) is braided-equivalent to B x Z1(Q) for some P,Q in S. S is saturated when Z1(X) S-Witt trivial implies X in S. The braided-admitting submonoid bfcFus consists of classes monoidally equivalent to some braided fusion category. Kong-Wang-Zheng arXiv:2511.02624 defines this S-Witt/saturation/saturated-closure framework generally and explicitly poses the saturated closure of bfcFus as open Problem 4.9(1).

## Definitions
S = bfcFus subset Fus. barS = {X in Fus | Z1(X) approx_S Vec}, the saturated closure construction. Vec_G is the pointed category of G-graded vector spaces; Rep(G) carries its usual symmetric braiding. Morita equivalence of fusion categories is equivalence of Drinfeld centers as braided categories (ENO).

## Result
S is a submonoid of Fus. Its saturation barS is a saturated submonoid with S strictly contained in barS; hence S is not saturated. Precisely: (a) barS = {X | exists P,Q in S with X x P Morita equivalent to Q}; (b) X0 = Vec_{S3} lies in barS but not in S; (c) every Vec_G and Rep(G) for finite G lies in barS; (d) bar-barS = barS.

## Proof / Evidence
S contains Vec and is closed under Deligne product via product braidings. For X in S with X monoidally B braided, Z1(X) = Z1(B) = B x B^rev by Mueger, so Z1(X) x Z1(Vec) = Z1(B) witnesses S subset barS. barS is a submonoid by Z1 multiplicativity and closure of S; stability under monoidal equivalence follows since Z1 preserves equivalences. Saturation bar-barS = barS follows by tensoring witnesses: Z1(Y) x Z1(R1) = Z1(R2) with Ri in barS expands via Pi,Qi in S to a witness over S. Part (a) follows from Z1(X x P) = Z1(X) x Z1(P) plus ENO. Pointed-braided lemma: a pointed braided category has abelian group of simples, since braiding c_{g,h}: g x h -> h x g is a nonzero map between simples forcing gh = hg. S3 is nonabelian, so Vec_{S3} is not in S. But Vec_{S3} is Morita equivalent to symmetric Rep(S3), so Z1(Vec_{S3}) = Z1(Rep(S3)) with Rep(S3) in S and Vec in S, giving Vec_{S3} in barS. Same argument gives (c). Numerics: FPdim(Vec_{S3}) = 6, FPdim(Z1) = 36, Z1 = D(S3)-mod of rank 8 (centralizer irrep counts 3+2+3 over class sizes 1,2,3), Rep(S3) degrees 1,1,2 with 1+1+4 = 6, recomputed from scratch by output/artifacts/verify_s3_witness.py (passes).

## Limitations
Proof uses standard cited toolkit (Deligne product, center multiplicativity, ENO, Mueger, Vec_G-Rep(G) Morita equivalence) without re-proving them. The Python artifact checks group/double numerics only, not categorical theorems. The description of barS is the structural Morita characterization plus containment of all group-theoretical Vec_G/Rep(G), not a complete enumeration of barS.

## Reproducibility
Run `python3 output/artifacts/verify_s3_witness.py`; expect noncommuting pair, class sizes [1,2,3], rank 8, FPdims 6/36, degree check, ALL CHECKS PASSED.

## References
Kong-Wang-Zheng, Generalized Witt and Morita equivalences, arXiv:2511.02624; Davydov-Mueger-Nikshych-Ostrik, Witt group of non-degenerate braided fusion categories, arXiv:1009.2117; Drinfeld-Gelaki-Nikshych-Ostrik, On braided fusion categories I.
