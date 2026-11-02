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

The theorem has a self-contained analytical proof in RESULT.md using two exact centered-Hilbert inequalities, three lower certificates, and explicit two-simplex embeddings. The standalone `check_deformed_crown.py` uses only Python's standard library and exact rational arithmetic. It verified 1,756 phase/Gram instances across the range of orders 3 through 100, including transition points, and independently enumerated feasible vertices of the reduced linear program for 104 exact test instances:

`CHECK_OK exact_rational_phase_cases= 1756 independent_exact_LP_cases= 104 orders=3..100 phases=3`

The program checks finite cases only. It is not an exhaustive search over real parameters or infinitely many orders; the general proof is given by the displayed inequalities and constructions. Independent mathematical audit has not been performed.
