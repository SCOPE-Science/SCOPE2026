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

Run `python verify.py` with Python 3 and NumPy from the same directory. Expected output begins `VERIFY_OK` and reports 1,875 counted assertion units. The code independently builds integer Hamming-distance Gram matrices for 49 pairs \(3\le q,d\le9\), checks exact invariant blocks and trace identities, compares with direct finite Fourier matrices on six cyclic examples, and confirms a noncyclic \((\mathbb Z/2\mathbb Z)^2\) example. `VERIFY_OUTPUT.txt` records the actual run outcome.

The exact all-group assertion instead follows from orthogonality of finite abelian characters and from the exhaustive invariant-space decomposition given in `RESULT.md`. Tests at finitely many \(q,d\) do not establish universal spectral formulas; numerical eigenvalues are checked within stated floating-point tolerances, whereas all internal block checks use integer identities.

Scientific review of correctness, originality and value has been performed for this finding; independent audit and independently obtained mathematical certification have not been performed.
