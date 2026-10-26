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

Execute `python3 verify.py` from this package. It explicitly constructs the covering inequalities and checks inclusionwise minimality by removing each selected element in turn, then compares complete size-frequency tables to the formula for seven graph sizes, including the theorem boundary \(K_{2,2}\) and \(K_{3,4}\). The anticipated last line is `VERIFY_OK 7 complete_bipartite_cases`.

Actual execution of the embedded program gave this last line; the seven exact polynomial-versus-direct comparisons agreed, including \(\mathcal M_{3,3}(z)=33z^5+94z^6+6z^7+z^9\). The computations are finite consistency checks. The proof in RESULT.md establishes the universal statement; no external certification or independent audit has occurred.
