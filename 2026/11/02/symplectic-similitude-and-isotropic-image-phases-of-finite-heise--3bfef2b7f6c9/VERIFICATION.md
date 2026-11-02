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

# Verification of the stated finite Heisenberg Rota–Baxter family

Run the self-contained Python standard-library script `verify.py` with `python3 verify.py` in the same directory. On success, its final line reads `VERIFY_OK`.

The checker builds the group law on \(V\times\mathbb F_p\) and evaluates both sides of the Rota–Baxter equation directly. Its exhaustive \(p=3,n=1\) test considers all \(81\) matrices \(T\), each \(\mu\in\mathbb F_3\), and all \(27^2\) ordered group pairs for the prescribed quadratic function with zero linear shift, checking equivalence with the symplectic criterion. The exhaustive \(p=5,n=1\) test checks all \(625\) matrices against the criterion and the predicted coset/isotropic counts. It also verifies admissible matrices and rejects sampled inadmissible matrices in dimension four at \(p=3\) by directly testing group identities, with random linear central shifts for positive samples.

Observed matrix counts per scalar are \((33,24,33)\) for \(p=3\), and \((145,120,120,120,145)\) for \(p=5\), before multiplying by the number \(p^{2n}\) of central linear forms. Independently, the argument in `RESULT.md` proves the general finite-field count. No tested finite sample provides an infinite proof; no external formal certification or independent mathematical audit has been performed.
