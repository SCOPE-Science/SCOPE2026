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

# Reproduction and evidentiary limits

Run `python3 verify.py` in the directory containing this file and `verify.py`. The script needs only the Python standard library. It constructs crown-graph adjacency directly and enumerates every proper colour partition using a restricted-growth representation; each candidate is rejected if any explicitly constructed four-vertex graph path is bichromatic. It separately evaluates the Stirling-number formula and compares all cardinality coefficients for orders two through seven, including the stated range three through seven.

The reproduced output in `verify_output.txt` includes the final line:

`VERIFICATION_OK star_crown exhaustive_n=2..7 direct_checks=1189120 identity_n=3..50`

The direct exhaustive part counts 1,189,120 proper colour partitions for six graph orders, not 1,189,120 arbitrary vertex labelings. The arithmetic part checks the algebraic closed form for orders three through fifty. Neither calculation proves the theorem for unbounded order; the structural obstruction lemma and case enumeration in `RESULT.md` provide that proof. No independent scientific audit has been performed.
