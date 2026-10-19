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
# Verification of the three-block nilradical commuting-tuple formulas

The accompanying `verify.py` was independently extracted and run with Python 3. It constructs all \(q^{r+s}\) pairs \((u,v)\) per tuple index, computes pairwise matrix commutators by exact finite-field arithmetic, and enumerates every commuting tuple for the nine small input configurations in the main result. The finite fields comprise \(\mathbb F_2\), \(\mathbb F_3\), \(\mathbb F_5\), and an explicit four-element field \(\mathbb F_4\).

All nine configurations passed both tests: (i) each commuting tuple lies in the union of the two pure components or the rank-one determinantal component; (ii) the count agrees with the closed formula. Output was `VERIFY_OK_THREE_BLOCK_COMMUTING_TUPLES`. The largest explicit tuple search has \(3^{12}=531{,}441\) tuples at parameters \((q,r,s,t)=(3,2,2,3)\); other instances probe tuple length four. The central \(Z_i\) matrices contribute an independent exact factor \(q^{rst}\), not an enumerated materialization.

The complete proof separately verifies the tensor-rigidity lemma, component maximality, irreducibility, dimensions, the equidimensionality boundary, and finite-field counts for all parameters. The calculations are corroboration only; they do not establish infinitely many parameters. No computer algebra system was used to claim scheme-theoretic reducedness or independent proof certification.
