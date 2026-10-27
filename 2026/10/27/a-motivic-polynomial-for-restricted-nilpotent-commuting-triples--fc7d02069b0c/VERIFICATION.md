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

# Reproducibility of the mathematical checks

Run `OPENBLAS_NUM_THREADS=1 python witt_triples_check.py` with Python 3 and NumPy installed. The program uses exact integer arithmetic modulo the relevant prime to generate restricted powers, and integer coefficient matrices modulo that prime to test brackets. Float-based matrix multiplication is used **only** to sum a finite boolean adjacency matrix with entries and intermediate values small enough for exact representation in binary floating point; the resulting integer triple count is therefore exact in the tested case. A complete general proof appears in `RESULT.md`.

For \(p=q=5\), all \(5^5=3125\) derivations are generated, the 625 nilpotent ones selected by computing the fifth iterate of each derivation on the generator, and the full pairwise-commutation graph tested. The exact results are 6,625 commuting ordered pairs and 108,625 commuting ordered triples. All commuting pairs in the indicated positive-valuation coefficient spaces are enumerated at \(p=5\) for \(m=2,3\) and \(p=7\) for \(m=3,4\). Additionally, 150 deterministic random centralizer-rank checks are performed for each of \(p=5\) and \(p=7\). The expected final marker is `WITT_TRIPLES_OK`.

The numerical checks are finite and do not establish the formula for arbitrary \(p\), arbitrary extension degrees, or Grothendieck classes; those assertions rest on the valuation-stratified proof. No independent mathematical audit or proof-assistant certification has been performed.
