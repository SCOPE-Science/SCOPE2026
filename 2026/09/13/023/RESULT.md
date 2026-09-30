# First-order flat-state rigid-unfolding parity criterion for the equiangular degree-8 vertex (A8)

## Context

For equal-angle single-vertex crease patterns, Ouchi and Uehara record two facts that fix the flat-folding/forcing baseline: an equal-angle MV assignment is flat-foldable if and only if |#M-#V|=2, and for n>=4 every equal-angle flat-foldable SVCP has minimum forcing-set size n/2+1. Thus at n=8 the 112 Maekawa assignments are the complete flat-foldable MV family and their forcing number 5 is prior theory, not a new finding. The retained result here is the exact tangent-space classification of rigid unfolding from the fully flat-folded state.

## Definitions

Let A8 have eight equal sectors alpha=pi/4 and creases indexed 0,...,7 cyclically. Encode an MV assignment by s in {+1,-1}^8. Let P={s: sum_i s_i=+2 or -2}; by the equal-angle flat-foldability criterion, P is exactly the flat-foldable MV family. Let F be the subfamily for which both parity classes {0,2,4,6} and {1,3,5,7} contain both signs, and let G=P\F.

At the fully flat-folded state set rho_k=s_k*pi. A first-order rigid-unfolding direction with the prescribed signs is represented by strictly positive speeds v_k>0 satisfying J D_s v=0, where J is the closure Jacobian and D_s=diag(s_0,...,s_7).

## Result

1. |P|=112. Under the dihedral action on crease labels, P has exactly 10 orbits with size multiset [8,8,8,8,8,8,16,16,16,16].
2. The flat-state first-order system admits a strictly positive solution if and only if s is mixed on the even creases and mixed on the odd creases. Consequently |F|=96 and |G|=16.
3. The accompanying exhaustive forcing computation reproduces minimum forcing number 5 for every member of P, in agreement with the published equal-angle theorem. This item is a verification cross-check and is not claimed as original. The same brute-force definition, restricted to F, also returns 5 for all 96 members.

## Proof / evidence

The 112-count is 2*C(8,3). Exact dihedral canonicalization gives the stated ten orbit sizes.

For the tangent calculation, write D=diag(1,-1,-1), Rz=Rz(pi/4), and Fmat=Rz D. Exactly Fmat^2=I. Differentiating the eight-factor closure at rho_k=±pi gives columns alternating between (sqrt(2)/2,sqrt(2)/2,0) on even indices and (1,0,0) on odd indices. Therefore J D_s v=0 is equivalent to

sum_{i even} s_i v_i=0,  sum_{i odd} s_i v_i=0.

For a finite set of positive weights, a signed weighted sum can vanish exactly when both signs occur. Applying this independently to the four even and four odd indices proves the criterion and the 96/16 split.

## Originality boundary

The forcing-number-5 statement is prior Ouchi–Uehara theory and has been removed from the novelty claim. A targeted comparison with that forcing-set paper, its equal-angle flat-foldability lemma, and the standard rigid-origami vertex literature did not locate the specific A8 flat-folded Jacobian parity criterion or its 96/16 classification. The retained contribution is therefore only that exact first-order classification.

## Limitations

This is a tangent-space result at a singular fully flat-folded configuration. A positive first-order direction is necessary but is not shown to integrate to a finite rigid branch, and no claim of finite-amplitude rigid foldability follows from the 96/16 split.

## Reproducibility

Run `python3 artifacts/enumerate_forcing.py` for the exact integer census/orbits/forcing cross-check and `python3 artifacts/jacobian_parity.py` for the exact symbolic Jacobian calculation.

## References

- K. Ouchi and R. Uehara, Minimum Forcing Sets for Single-vertex Crease Pattern, Journal of Information Processing 28 (2020), 800-805, DOI 10.2197/ipsjjip.28.800.
- Z. Abel et al., Rigid origami vertices: conditions and forcing sets, Journal of Computational Geometry 7 (2016), arXiv:1507.01644.
- K. Ouchi and R. Uehara, Efficient Enumeration of Flat-Foldable Single Vertex Crease Patterns, IEICE Trans. Inf. & Syst. E102.D (2019), DOI 10.1587/transinf.2018FCP0004.
