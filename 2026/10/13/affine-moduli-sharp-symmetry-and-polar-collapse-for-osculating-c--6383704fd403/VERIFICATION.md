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
# Reproduction and limits

Run `python3 verify.py` with the standard Python library. It checks exact affine substitutions; full projective stabilizer over \(\mathbb F_3\) via exhaustive \(5616\)-matrix enumeration; finite-field Burnside orbit counts by an independent exhaustive orbit method for all permitted \(m\) over the specified small fields, including \(\mathbb F_4\); and exact polynomial Frobenius identities and gradients for \(p=3,5,7\). The expected output begins with `VERIFY_OK:`.

The general proof is in `RESULT.md`: its key unbounded steps are the projective matrix normal form, closure of a finite parameter set under addition and multiplication at the symmetry bound, the function-field identity \(u^2=s\), and the exhaustive affine conjugacy-cycle classification behind Burnside's formula. The finite tests cannot establish the universal theorem on their own, and no independent audit has been performed.
