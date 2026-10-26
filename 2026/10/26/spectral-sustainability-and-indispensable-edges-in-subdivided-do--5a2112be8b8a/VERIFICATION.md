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

# Verification

With `numpy>=1.24`, run `python verify.py` in the extracted directory. The program constructs each \(B(\ell,a,b)\), enumerates every edge, removes it, computes the two resulting vertex components, and evaluates the top adjacency eigenvalue after every different legal reconnection. The observed failing edges are compared with the exact theorem classification for all 75 cases \(2\le\ell\le6\), \(2\le b\le a\le6\). Execution output: `VERIFY_OK: 75 cases (all legal swaps of every edge; 2<=ell<=6, 2<=b<=a<=6)`.

Separately, the derivation uses the path continuant recursion, pendant-vertex characteristic-polynomial expansion, and a positive resolvent monotonicity argument. Strict sign inequalities are uniform in the path length and leaf counts; finite numerical samples do not certify those inequalities for all parameters. Dependency, input ranges, assumptions, and limitations are stated explicitly.
