---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

In the multigroup adaptive SIS dynamics with n=2, B=[[4,1],[1,1/2]], all epidemiological and link rates 1, breaking functions 1 and creation 1 except cr_21(y1)=max(1-2y1,0)^3 (C^2 nonincreasing), the disease-free next-generation radius equals (9+sqrt65)/8>1. Stationarity of y1 forces y1>1/2 if both groups infected; then z21=0 and stationary y2 equation is -y2(3+y2)/4<0. Thus only DFE and y1=1/2,y2=0 partial state exist. Full 6x6 Jacobian eigenvalues {-2 multiplicity3,-1 multiplicity2,-3/4}, independently reconstructed in exact SymPy. For strictly positive creation and positive Q on infection-carrying edges, positive Metzler Perron bound at R0>1, a compact truncated cube, and inward-pointing Brouwer projection ensure nonzero reduced equilibrium; irreducibility plus positive Z propagates any zero coordinate to all, so equilibrium is fully endemic.

## originality

PASS

Original Achterberg–Sensi–Sottile 2024/2025 primary work states Conjecture 6 that R0>1 implies fully endemic equilibrium without an all-group link-creation condition; its Theorem 5 proves stronger row-sum sufficient criterion. Read primary arXiv HTML and checked hypotheses: counterexample has minimum row sum 3/4 and is not refuted by Theorem 5. This is a substantive counterexample to the conjectured implication in its allowed smooth monotone function class plus a meaningful repaired sufficient hypothesis. Resultary papers on static multigroup R0 or other adaptive diseases do not cover the exact mechanism.

## value

PASS

Settles an explicit natural conjecture about infectious pathway extinction with a smooth exact two-group example, while proving a structural positivity condition under which the expected supercritical implication is restored. The distinction is mathematically useful beyond mere numerical mismatch.

The dated certificate retains the supplied scientific assessment, sources and limitations.
