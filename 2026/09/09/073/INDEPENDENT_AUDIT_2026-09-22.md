# Independent audit — 2026/09/09/073

Date: 2026-09-26. Disposition: retain accepted.

## Correctness — PASS

The morphism (x,y)↦(y,x²) satisfies x⁴=y³+1, hence lands on E: V²=U³+1. An independent modulo-7 enumeration found 11 affine points plus one point at infinity, matching #C(F₇)=12. The partial derivatives of Y³Z−X⁴+Z⁴ have no common projective zero in characteristic zero or seven, giving smooth genus three and good reduction at seven. The 2-isogeny descent supplied in RESULT.md reduces E to rank zero; its real exclusions and mod-3 primitive exclusions support quotient sizes two on both sides, while the six torsion points O,(−1,0),(0,±1),(2,±3) are closed under the group law. For their U-coordinates −1,0,2, the curve's x⁴ values are 0,1,9; only x=0,±1 lift rationally. With infinity these are precisely four points. The claimed lack of sharpness at p=7 follows from 12>4. The earlier three-point target is explicitly corrected rather than carried forward.

## Originality — PASS

The rank-zero quotient strategy and elliptic descent are established techniques (Ezome et al., arXiv:2302.03986). The specific exact four-point census and correction of the record's admitted target are a concrete application; I found no matching explicit census in the consulted open prior work, although this is not a comprehensive priority proof.

## Scientific value — PASS

A complete rational-point census for this natural genus-three curve is a useful bounded arithmetic result. Its quotient argument avoids a Jacobian rank claim and clearly identifies why a proposed Stoll-sharp example fails. It does not determine the Prym rank or provide new Coleman integration.

Sources: https://arxiv.org/abs/2302.03986 ; https://arxiv.org/abs/0906.1934 . Open matching preprints were available.
