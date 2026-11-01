---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-01.md",
      "INDEPENDENT_AUDIT_2026-11-01.json"
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

Independent same-arm arclength distance density is 2(a-t)_+ per arm; for two distinct arms it is the triangular-convolution hinge t_+-(t-a)_+-(t-b)_++(t-a-b)_+ per orientation. Summing proves (L²/2)f(t)=L + n(n-3)t/2 -(n-2)Σ(t-a_i)_++Σ_{i<j}(t-a_i-a_j)_+. Thus f(0)=2/L, L²f′(0+)=n(n-3), and the latter strictly determines n≥3. Distributional curvature ν=−(n−2)Σδ_ai+Σ_{i<j}δ_{ai+aj}. If two sorted multisets first differ at smallest positive s, pair sums at s involve only smaller positive lengths already equal, so coefficient difference is −(n−2) times multiplicity difference, impossible. The signed-atom peeling algorithm repeatedly subtracts contributions from already recovered arms and recovers all multiplicities. Independently reconstructed exact-rational curvature/peeling for 1,2,3 (the invisible third arm), equal arms, ties and longer examples; examined actual verify.py (exact rational hinge vs conditioning and simulations). These finite examples supplement, not replace, the strict-smallest-difference proof.

## originality

PASS

Prior metric-measure-space distance histogram work states a local-injectivity result for metric graphs; that alone is not global all-positive-length rigidity with invisible knot collisions. The relevant complete Mémoli–Needham paper was not lawfully accessible in this run; an attempted institutional retrieval reported a disconnected VPN. This is a material priority risk, not evidence of prior coverage and not a correctness defect. Aldous–Blanc–Curien construct realizable distance laws with freely specified measures, whereas the asserted inverse theorem fixes normalized arclength measure and star topology.

## value

PASS

A two-point unlabeled distance distribution is a canonical metric-measure observable; exact recovery of topology degree, scale and all positive arm lengths is an inverse rigidity theorem for a natural nontrivial graph class. Resolving exact cancellations makes reconstruction genuinely global rather than a generic-position local statement; the small example (1,2,3) shows why direct kink reading fails.

The dated certificate retains the supplied scientific assessment, sources and limitations.
