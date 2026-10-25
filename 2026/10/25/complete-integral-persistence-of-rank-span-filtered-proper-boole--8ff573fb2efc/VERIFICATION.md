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

# Reproduction and limits

Run `python3 verify.py` using Python 3. The program constructs nonempty proper subsets, enumerates every allowed inclusion chain for \(3\le n\le6\), builds the simplicial boundary matrices over \(\mathbb F_2\), and derives every reduced Betti rank independently of the closed-form recurrence. It also checks face counts and Euler sums for \(3\le n\le40\). A successful run ends in `VERIFY_OK`.

Observed checks: \(n=3\): \((5,1)\); \(n=4\): \((13,11,1)\); \(n=5\): \((29,41,19,1)\); \(n=6\): \((61,119,91,29,1)\). Fourteen exact finite boundary-rank instances were checked. The entire filtration's integral barcode is proved separately in `RESULT.md` from known wedge concentration, an all-dimensional face count, Euler evaluation and vanishing of degree-preserving inclusion maps. Finite mod-two homology alone would not imply torsion-freeness or the infinite theorem. No outside audit or independent validation has been performed.
