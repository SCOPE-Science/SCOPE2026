---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Exact finite verification

Invoke `python3 verify_homotopy.py` and `python3 verify_homology.py` from the directory containing the accompanying two code files. Only the Python standard library is required.

The first program checks the graph definition, the full face vector, 9,951 ordinary matched face pairs and one critical vertex, one critical three-face and two critical four-faces. It orients every face incidence and proves the matching is acyclic by processing every node in a topological sort. Its signed integer incidence projection gives exactly zero for the two four-cell attaching degrees. A successful execution prints `VERIFY_HOMOTOPY_OK` with the verified counts.

The second program constructs faces by a different recursion and reduces every mod-two boundary matrix, independently finding ordinary Betti numbers \((\beta_0,\beta_3,\beta_4)=(1,1,2)\) with other values zero. It prints `VERIFY_HOMOLOGY_OK`. The mod-two calculation does not prove the attaching degrees zero; the exact integer recursion in the first verifier is needed for that conclusion. The homotopy identification also uses the standard theorem \(\pi_3(S^3)\cong\mathbb Z\).

This is exhaustive for the single stated finite complex, but not a proof of an infinite-parameter assertion. Literature noncoverage is qualified by the residual risk of later or unindexed equivalent results. No external independent audit is asserted.
