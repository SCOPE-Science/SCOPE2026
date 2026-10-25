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

# Exact reproducibility and limits

Run `python VERIFY.py` using Python 3 and SymPy. The script produces exact rational Sturm root counts for every integer \(2\le n\le21\), checks the analytic derivative identities, and confirms strictly alternating signs at the decisive rational evaluation points for \(n=21\). Observed final status: `PASS exact finite root counts and derivative identities`.

The finite Sturm counts support only the listed finite cases. The extension to all \(n\ge21\) is an analytic argument in `RESULT.md`; the code is not claimed to be a computational proof over infinitely many sizes. Literature priority and correctness have not been independently audited.
