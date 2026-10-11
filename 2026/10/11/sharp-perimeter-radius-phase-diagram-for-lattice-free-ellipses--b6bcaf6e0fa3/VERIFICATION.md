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

The theorem is established by the complete analytic proof in `RESULT.md`. Its critical steps are: an exact ellipse-perimeter integral; the strict inequality \(\partial_aP<4\) at fixed minor semiaxis; the covering-radius constraint \(b\le\rho(\Lambda)\); existence of deepest-hole disks; and a lattice-free strip construction for every full-rank planar lattice. These prove all coefficient regimes, boundary coefficients, and equality conditions without finite enumeration.

## Reproducible diagnostic checks

From the directory containing the embedded files, run:

```sh
python3 verify.py
```

The command was run and printed:

```text
VERIFY_OK: 28 axis pairs, five parameters, attained square-lattice sharp disk and free-strip ellipses.
```

The script uses Python's standard library and a composite Simpson quadrature. It tests twenty-eight axis pairs and five coefficient values, compares perimeter and derivative inequalities, verifies the permitted square-lattice extremal disk, and checks some elongated ellipses in the open unit lattice strip. Computed inequalities allow numerical tolerance; they support, but do not prove, statements quantified over real coefficients, all ellipses, or all lattices.

## Boundaries and historical verification

The admissibility condition forbids lattice points in the **interior** but permits boundary contact. The square-lattice equality disk touches four lattice sites on its boundary. The disk equality conditions differ between \(4\le\lambda<2\pi\) and \(\lambda=2\pi\); the supremum is unattained for \(\lambda>2\pi\). Comparisons with the cited literature are limited to the inspected published texts and available search records; independent audit is not performed.
