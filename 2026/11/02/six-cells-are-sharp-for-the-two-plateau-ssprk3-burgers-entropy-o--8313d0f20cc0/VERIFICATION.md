---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

The independent checker reconstructed modal DG flux and L_m=F_{i−1}−F_i, L_b=3m_i²+b_i²−3(F_{i−1}+F_i), then all SSPRK3 stages symbolically using exact rationals for N=2,4,6,8,10,12. It matched the explicit six/eight/large-N overshoot polynomials coefficientwise, conservation, stage characteristic-speed bounds via Bernstein conversion, and all final mean-in-[0,1] bounds at N=2,4. Analytically δ_N>s²/4 implies physical overshoot Aδ_N>2; one changed cell dominates exponential entropy loss on N=6,8,10, while radius-three locality bounds at most six perturbed high cells for larger N. At N=2,4 mass conservation plus convex chord inequality proves no global growth. Stencil locality, not grid sampling, extends the finite polynomial cases to every even N. Correctness restricted to stated initial data, fixed alpha and global cell-mean criterion.

## originality

PASS

Liu–Jiang–Zhang (arxiv:2610.30535v1) supply the large even-N≥12 two-plateau entropy obstruction, whereas examined derived finite-grid calculations sharpen to N=6. The closest preprint could not be read in full via arXiv/OA, and an authorized institutional retrieval returned vpn_disconnected. Thus no whole-document NOT_COVERING assertion is made. Best-of-knowledge distinct threshold; substantial explicit primary-source access risk remains, which alone does not fail originality.

## value

PASS

The minimum mesh of a canonical published SSPRK3-DG entropy counterexample is a natural sharp finite cutoff, not an arbitrary tiny instance. The two/four-cell universal-convex nonincrease explains a genuine boundary and distinguishes a global mean-entropy obstruction from a universal method stability theorem. Resolving six vs twelve has intrinsic numerical-analysis benchmark value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
