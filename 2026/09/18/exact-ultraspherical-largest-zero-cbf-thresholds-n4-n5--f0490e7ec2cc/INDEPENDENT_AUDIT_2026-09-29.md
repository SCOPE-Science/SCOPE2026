# Independent audit — 2026-09-29

**Record:** `2026/09/18/exact-ultraspherical-largest-zero-cbf-thresholds-n4-n5--f0490e7ec2cc`  
**Audited source tree:** `101f6392668ff1d00d0e95cfd84cd2a31725da58`  
**Repository snapshot:** `SCOPE-Science/SCOPE2026@253a0fe5d0217455660a277f9adb940030e567ad`  
**Disposition:** **PASSED**

## Correctness — PASS

PASS. I re-derived the quadratic equations in y=x^2 for C_4^lambda and C_5^lambda and obtained exactly the filed largest-zero branches. With the upper-half-plane continuation normalized from lambda>-1/2, the radical is negative real to the left of both of its real branch points. Hence Y_4 remains positive on (-3,-2) and Y_5 remains positive on (-4,-3), extending the nonnegative largest-sheet boundary needed by the Pick argument. At the next degree-loss points the continued branches satisfy Y_4(lambda)=3/(lambda+3)+O(1) and Y_5(lambda)=5/(lambda+4)+O(1); upper continuation therefore gives z_4~sqrt(3)(lambda+3)^(-1/2) and z_5~sqrt(5)(lambda+4)^(-1/2), with negative imaginary boundary value immediately to the left. This proves failure of the Pick property for d>3 and d>4 respectively. For 1/2<=d<=3 or <=4, combining the explicit extended real-boundary sign with Castillo's right-half-plane property and sublinear-singularity boundary minimum principle gives the Pick property. Independent complex evaluations using the correctly continued factorwise square roots found no upper-half-plane sign violation at d=3 or 4 and immediate violations above those thresholds. The endpoint functions have finite Hermite limits at infinity and are nonconstant, so the representing measure is nonzero and the stated strict derivative inequalities follow.

## Originality — PASS

PASS, qualified. I inspected the complete 46-page arXiv:2609.19186v1 text through authorized institutional access. Its Theorem A.3 gives an exact threshold only for nonlargest zeros k>=2; Proposition A.4 gives the largest zero only the sufficient range d<=ceil(n/2) and explicitly says its upper endpoint is not claimed optimal; Remark A.5 gives exact largest-zero classifications only for n=2,3. Thus the exact n=4 threshold d=3 and n=5 threshold d=4 are not in the accessible v1. A third-party version index reports a September 18 update, but targeted web searches found no v2 and an authorized request for the explicit v2 PDF returned HTTP 404/no verified PDF. I therefore retain a version-indexing priority caveat rather than claiming an absolute priority guarantee.

## Scientific value — PASS

PASS. The result sharply resolves the first two largest-zero degrees left open by the source's general sufficient bound and identifies the next pole—not the first degree-loss point—as the exact obstruction. Although low-degree, it supplies a concrete mechanism that can guide the still-open all-degree largest-zero threshold problem and cleanly separates complete-Bernstein failure from the weaker ordinary Bernstein question.

## Independent checks

- Re-derived both largest-zero formulas directly from C_4^lambda and C_5^lambda as quadratics in x^2.
- Checked the upper-half-plane branch convention factorwise and numerically sampled the Pick sign at the sharp endpoints and immediately beyond them.
- Verified the pole residues 3 and 5 and the consequent half-order boundary rotation.

## Sources checked

- https://arxiv.org/abs/2609.19186 — K. Castillo (2026), Complete Bernstein functions and scaled ultraspherical zeros. Full v1 text inspected; Appendix A.3/A.4/A.5 are the direct comparison points.
- https://doi.org/10.1515/9783110269338 — Schilling, Song and Vondraček, Bernstein Functions, for the Pick/complete-Bernstein characterization used by both source and record.

## Limitations

- The exact classification is only for the largest zero in degrees 4 and 5; it does not establish the all-degree optimal threshold.
- The negative side proves failure of the complete-Bernstein/Pick property, not failure of the weaker Bernstein property.
- A metadata index reports a September 18 update of arXiv:2609.19186, while the accessible full text was v1 and an explicit v2 retrieval returned 404/no PDF; originality is therefore qualified by that version-indexing discrepancy.

## Audit conclusion

All three audit axes pass. No substantive research-file correction is required. This audit updates only the independent-audit verification channel; the Lean and expert-attestation channels are preserved exactly. GitHub was used only as read-only evidence during this audit.
