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

# Verification and reproduction

Run `python3 verify.py` with Python 3 and its standard library. The script has no network requests, third-party packages, or data dependencies.

The first independent method enumerates each of the \(3^{2n}\) functions on \(H_n\) for \(2\le n\le7\) and tests the original two conditions directly for every vertex. Its exact \(5,380,830\) assignments yielded valid-function totals \(25,209,1825,16265,145969,1312697\) for \(n=2,3,4,5,6,7\), respectively. The second method uses a nine-state prefix/suffix transfer with capped neighbor-label sums. It agrees coefficient-by-coefficient with the finite-sum formula for every \(2\le n\le18\). Separately asserted equalities include the closed total count and the predicted minimum coefficient. The captured output is bundled in `verification_output.txt`.

The general combinatorial bijection and geometric-series proof, not the finite experiments, establish the formula for every permitted graph order. No independent audit or formal proof certificate is claimed.
