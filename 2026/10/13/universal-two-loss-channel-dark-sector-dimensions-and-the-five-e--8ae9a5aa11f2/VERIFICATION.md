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
# Verification details

The analytic proof uses the exact two-excitation basis for \(n\) qubits, an invertible coefficient rescaling, and a complete algebraic classification of the left kernel of the two-channel incidence map. The decisive step is a three-column symmetric-form row-span calculation; no numerical evidence is used in that proof.

The included `verify.py` is a Python 3 standard-library checker. It computes exact rational ranks of the original physical jump matrices, covering every equality-multiplicity partition for \(2\le n\le10\), independently randomized rational coefficients for \(4\le n\le9\), and two explicit dark-vector annihilation tests. Running `python3 verify.py` produced `VERIFY_OK 379 exact rational rank and vector checks`.

These finite computations check implementations and small cases only; they neither certify all complex parameters nor establish publication novelty. The proof covers all nonzero complex couplings analytically. No independent audit has been performed.
