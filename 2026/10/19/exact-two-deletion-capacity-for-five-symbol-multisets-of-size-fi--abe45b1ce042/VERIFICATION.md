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

# Verification record

The independent-audit channel has not been performed. The following are reproducibility checks supporting the mathematical proof, not an external certification.

Run `python3 verify.py` in a directory containing the included source file; it uses Python's standard library only. A successful run prints exactly `VERIFY_OK profiles=126 cliques=45 patterns=7 bound=10 witness=10`.

The program enumerates all \(\binom94=126\) integer compositions of five into five coordinates. It builds all five cliques \(A_i\), twenty indexed cliques \(B_{ij}\), and twenty indexed cliques \(C_{ij}\); checks all pairwise conflict inequalities; verifies all 126 vector-incidence triples against the seven-type table; evaluates every fractional-cover inequality and total weight using exact rational arithmetic; and checks the ten-word construction exhaustively. In particular, a successful run checks every pair within every finite clique, not a random sample.

The proof that fractional clique covers bound independent-set cardinality, and the equivalence between two-deletion correction and coordinatewise overlap at most two, are supplied in `RESULT.md`. The checker verifies the enumerated finite premises; it does not validate originality, extrapolate to other parameters, or constitute independent audit.
