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
# Reproducibility and limits

Execute `python check_linecube.py` in an environment with a standard Python 3 interpreter; there are no third-party dependencies. `verification_output.txt` records the checks from the same included program. The script builds every line-graph edge relation directly and compares the result with its alternative row-based construction, computes \(\mathbb F_2\) ranks of the first two update powers, and tests vanishing of the third. The printed cases are dimensions 2–7. All \(2^4=16\) and \(2^{12}=4096\) initial binary states in dimensions 2 and 3 were checked; larger cases use deterministic random samples, explicitly not exhaustive. The proof in RESULT.md establishes the general finite-field statement independently of these tests. No independent scientific audit has been performed.
