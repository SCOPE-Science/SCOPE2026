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

# Reproducibility and scope

Run `python verify.py` using Python 3 and SymPy. The file is self-contained and uses no network resources or external data. It checks four symbolic rational-function differences, 420 exact direct grounded-matrix inverses across weighted split graphs, and 17 exact boundary sign checks. Successful execution prints:

`VERIFY_OK 4 symbolic comparison identities; 420 exact direct grounded inverse comparisons; 17 exact threshold checks`

Finite matrix tests corroborate, but cannot establish, the unbounded graph-size and continuous-conductance claims. Those statements follow from the analytic block decomposition and sign analysis in RESULT.md. In particular, the threshold root is proved unique beyond its lower comparison boundary, rather than inferred from sampled roots. Independent audit has not been performed.
