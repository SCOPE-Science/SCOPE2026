---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For n>=2, d=n-1, 0<=t<=1 and full-dimensional compact convex B, the horizontal section of F_t(B) at height a is (1-(1-t)a)B even if the dilation center lies outside B. For F_t(B)+s(-F_t(B)) at height z, decomposition sections are (1-qa)B+(s+q(z-a))(-B), with q=1-t and max(0,z)<=a<=min(1,z+s). Increasing a reduces BOTH nonnegative coefficients by qh, so the earlier section is the later section plus qh(B-B), and B-B contains 0. Thus the union of sections is exactly the earliest section, not a mere inclusion. On z>=0 the section is (1-qz)B+s(-B); on z<=0 it is B+(s+qz)(-B). Fubini and the normalized degree-d Minkowski polynomial give the s^j coefficient as binom(d,j) M_j Psi_(n-j)/(n-j) + binom(d,j-1) M_(j-1) Psi_j/j = binom(n,j)[M_j Psi_(n-j)+M_(j-1)Psi_j]/n, for 1<=j<=n-1. The endpoint coefficients are Psi_n vol_d(B)/n, and the frustum volume is the same. Alexandrov--Fenchel log concavity of M_0..M_d and equal endpoint volumes force M_j>=vol(B); for d>=2, equality M_1=vol(B) in Minkowski first inequality means B and -B are translates, hence B centrally symmetric. If B is nonsymmetric, M_1>vol(B), so log concavity forces every interior M_j>vol(B); each reflected interior coefficient contains at least one such term with a positive Psi factor. This proves sharpness and rigidity at EVERY interior index, including boundary j=1,n-1, with n=2 automatic interval symmetry. Algebra gives sharp R_(n,j)(t)=1+(1-t^j)(1-t^(n-j))/(1-t^n) for 0<=t<1 and continuous value 1 at t=1; it decreases from 2 to 1, maximizing at central j. Summing the symmetric-base Minkowski polynomial at s=1 gives difference-body lower ratio [2^(n+1)-2(1+t)^n]/(1-t^n), endpoint 2^(n+1)-2 at t=0 and 2^n at t=1. Independent code (not merely the package verifier) performed 840 exact rational symbolic coefficient identities for dimensions 2..15 at 4 t-values and both symmetric/simplex abstract coefficient patterns; 48 further exact rational planar Minkowski-section integrations for 4 concrete convex polygons at four t-values and three s-values all agreed with the formula. The unrestricted statement follows from the symbolic section and classical mixed-volume proof, not from finite checks. The source verified code was inspected rather than executed blindly.

## originality

PASS

Best-of-knowledge mathematical contribution is the exact arbitrary-base dimension-raising reflected mixed-volume recursion, its coefficientwise sharp LOWER envelope and equality iff centrally symmetric base, not the already published simplex-base specialization or classical Minkowski/AF tools. The complete published simplex-truncation proof is contained as the special case M_j=binom(n-1,j)vol(B), yielding exactly its known formula, so no novelty is claimed for that subfamily. The complete published homothetic-frustum Santaló study concerns polar-volume/centroid/Mahler products of the same objects but does not determine their reflected Minkowski-polynomial coefficients. The materially inspected Fryš--Kotrbatý--Mouamine--Wang arXiv v2 PDF proves global upper Godbersen/higher-order inequalities and simplex rigidity, not this restricted-class exact polynomial or sharp lower envelope; Kotrbatý 2025 OA article likewise treats higher-order upper inequalities. Remaining closely related 2026 articles were checked via their original abstracts only because full arXiv/OA access failed and Oxford fallback reported a download-storage limit. Older unindexed cone/Cayley/pyramid mixed-volume identities could express the same result, a material residual priority risk; absence of search hits is not evidence of absolute novelty.

## value

PASS

The natural homothetic-frustum family bridges pyramids and prisms for arbitrary nonsymmetric, nonsmooth and nonpolyhedral convex bases. The exact two-neighbor recurrence calculates EVERY reflected mixed coefficient from dimension n-1 data; this is a usable structural reduction rather than a finite numerical slice. It yields a simultaneous sharp coefficientwise lower envelope with a complete symmetry equality classification, an explicit monotone central-index profile, and a sharp interpolation of difference-body ratios from 2^(n+1)-2 at pyramids to 2^n at prisms. The theorem genuinely extends the published simplex-truncation computation to arbitrary base mixed-volume sequences and produces extremal rigidity not implied by classical general upper bounds. Its possible future mathematical use is exact computation and testing of reflected mixed-volume inequalities on general Cayley/homothetic-frustum families, including sharp obstruction examples. The short derivation uses classical tools, but its full all-dimensional quantitative classification is natural and independently meaningful, not a renaming, an arbitrary computation or a trivial tiny gain. It does not give new universal Godbersen upper bounds or cover skew/nonhomothetic frusta.

The dated certificate retains the supplied scientific assessment, sources and limitations.
