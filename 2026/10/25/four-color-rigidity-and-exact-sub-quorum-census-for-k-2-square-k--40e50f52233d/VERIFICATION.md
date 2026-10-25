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
# Reproducibility
Run `python3 verify.py` using Python 3.9 or newer; no third-party packages or network connection are required. The program enumerates all partial colorings modulo color-label permutations for \(n=2,3,4,5\), checking local majority conditions directly on the reconstructed graph. It reports \(52,877,21147,678570\) candidate support-and-partition assignments, respectively. The maximum number of colors is \(2,3,4,4\), with exactly \(6\) and \(30\) four-color optima for \(n=4,5\); every counted optimum passes the structural characterization. It separately evaluates the coefficient formula for \(4\le n\le12\). A successful run ends in `VERIFY_OK`.

These are finite computational tests only. Correctness for all \(n\) is established by the preceding closed-neighborhood proof. No independent audit or exhaustive historical-priority certificate is represented.
