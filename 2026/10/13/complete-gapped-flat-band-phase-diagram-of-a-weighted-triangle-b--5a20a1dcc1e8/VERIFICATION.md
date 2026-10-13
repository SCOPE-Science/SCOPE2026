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

# Verification and reproducibility

Run `python3 verify_triangle_bridge.py` from the directory containing the file, with Python 3 and SymPy available. Its expected output is:

```
VERIFY_OK exact_Laurent=1 flat_locus=1 CLS_kernel=1 simple_isolation=1 branch_samples=4
```

The script directly reconstructs the \(3\times3\) Bloch matrix from the four hoppings and three onsite energies and uses exact symbolic rational-function simplification. It checks the coefficient decomposition of \(\det(H(z)-EI)\), the replacement \(E=Q_C-qr/p\), the identity \(\det(H(z)-\lambda I)=g(\alpha\beta-s^2)\), the nullvector under the exact constraint, and the principal minor \(g\alpha\). Four small unweighted cases at two phases give supplementary band-order and rank tests.

The proof in `RESULT.md` establishes the needed universal quantifiers analytically: the Laurent coefficient forces the energy, Schur complement gives the precise necessary and sufficient locus, matrix inertia gives band placement, and compactness plus rank two gives the gap. Numerical testing is not used to infer universal claims, and no independent audit or external certification has been performed.
