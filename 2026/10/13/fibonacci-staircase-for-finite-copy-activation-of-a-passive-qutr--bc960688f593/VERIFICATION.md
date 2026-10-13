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

Execute `python3 verify_passivity.py` using Python 3's standard library. The program uses exact integer comparisons to classify the signs of rational expressions in the golden ratio and to test all smaller candidate fractions for thirteen selected rational departures. For the eight test values with feasible small first-copy counts, it also enumerates distinct qutrit occupancy triples and compares the energy ordering with the logarithmic-probability ordering, rather than relying only on the rational-window calculation. It separately checks eight adjacent-convergent determinant and mediant identities, plus the next activating fraction at six exact irrational equality breakpoints.

A successful replay produces the `VERIFY_OK` summary and sample \(N_{\rm act}\) values. The two printed floating-point constants are illustrations of the exact algebraic liminf and limsup, not numerical certificates. Only the accompanying proof of the general inversion criterion, Farey lower bound, and Binet asymptotics establishes the result for every \(\delta>0\).

The exact endpoint convention is essential: a rational at \(\delta=\varepsilon_k\) is excluded because no *strict* population inversion arises from that pair. Degenerate-energy equalities likewise cannot extract work. The result does not quantify achievable work, physical gate depth, or catalytic variants.
