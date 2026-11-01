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

Execute `python3 wheel6_certificate.py` with a standard Python 3 installation. No external packages, datasets, network access, or adjacent artifacts are required. It constructs every closed graph-distance ball of \(K_1\vee C_5\), forms every admissible selected-row matrix for both maximal operators, and checks positive definiteness by exact integer Bareiss elimination and Sylvester's criterion. It verifies the exceptional selections, their rotational equivalence, the explicit exceptional Gram matrix, the cubic root bracket and polynomial eigenvector identities, and strict averaging comparisons by rational interval bounds.

Expected exact output:

```text
CERTIFICATE_OK centered_selections=486 centered_exceptions=1 uncentered_selections=21875 uncentered_exceptions=5
CERTIFICATE_OK thresholds_centered=3/2 uncentered=81/50 cubic=64z^3-120z^2+27z-1 interval=(81/50,1621/1000)
```

The finite enumeration exhausts all row-choice matrices on this six-vertex graph. It does not prove any assertion about larger or weighted wheels. The displayed cubic is checked using exact eigenvector identities and a rational isolating interval. The proof of uniqueness of the norm-attaining ray for each exceptional matrix also uses positivity and strict ball-selection comparisons, as given in RESULT.md.
