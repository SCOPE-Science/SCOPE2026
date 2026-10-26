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

The standalone `verify.py` needs Python 3 and no additional packages. Execute `python3 verify.py`; it reconstructs the normalized six-point branch configurations in \(\mathbb F_9\) and \(\mathbb F_{27}\), checks the harmonic cross-ratio identities over each exact field, and computes the genus-two Cartier–Manin matrix and its entrywise-cubed Frobenius iterate, following Howe (2006, Section 2). Six example profiles are asserted. Exhaustive local checks cover \(35\) normalized triples over \(\mathbb F_9\) and \(2300\) normalized triples over \(\mathbb F_{27}\).

These finite checks alone do not prove the statement for every algebraically closed characteristic-three field. That step is mathematical: prime-to-three Galois character decomposition, uniqueness of harmonic completion, and the explicitly nonzero determinant \(-(u-v)^2\) establish the global obstruction; the examples establish all possibilities.

The reviewed formulas concern \(3\)-rank, \(a\)-number and Newton polygon. No independent validation or external certification has been performed.
