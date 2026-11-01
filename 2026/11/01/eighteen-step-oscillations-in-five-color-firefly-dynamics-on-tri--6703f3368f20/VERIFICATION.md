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

Run `python verify_fca5_tripartite.py` with Python 3 standard library and `python verify_fca5_micro.py` with NumPy. Both were run using their actual embedded code; the combined stdout is in `verify_output.txt`. The first examines every one of the 29,791 nonempty support triples, asserts the support census and checks six exact orbit-count instances. The second exhaustively simulates all 390,625 microstates on the labelled K(1,3,4) graph through 18 steps and confirms 48 primitive period-18 orbits. No probabilistic tests or infinite-parameter computations are represented as exhaustive microstate verification.

The finite quotient is valid for arbitrary shore multiplicities because the transition at any vertex depends only on the colors present in *other* shores; lift of a periodic support orbit to each labelled microstate follows from local bijectivity on occupied classes.
