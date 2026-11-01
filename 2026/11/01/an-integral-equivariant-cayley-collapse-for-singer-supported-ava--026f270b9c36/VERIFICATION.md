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
# Verification and boundaries

The supplied Python 3 script `verify_singer_avalanche.py` uses only the standard library. Run:

```bash
python3 verify_singer_avalanche.py
```

Its last line is `VERIFY_OK` after four complete finite tests, with prime-power orders \(q=2,3,4,5\) and cycle lengths \(n=7,13,21,31\). The tests verify all ordered differences, all pairwise facet intersections, every complete firing orbit, and exact elementary collapses (respectively 7, 52, 231, and 806 free-face pairs). The surviving one-complexes have reduced first Betti numbers 8, 27, 64, and 125. Twenty randomized exact **integer** one-cycle reconstructions per test also verify boundary vanishing, uniqueness of coefficients in the Hamiltonian-plus-chord basis and covariance under every cyclic rotation. A negative test on a non-perfect consecutive support confirms that shared edges invalidate the relative-collapse premise.

The finite calculations do not establish the infinite prime-power theorem or exclude torsion by sampling: the full integral proof lies in `RESULT.md`. Specifically, each positive-dimensional old face has a unique block owner, every proposed free face has its stipulated single surviving coface when removed, and every integral graph cycle has a unique decomposition into one globally invariant unit cycle and translated chord-minus-arc cycles. Singer's independent finite-field theorem supplies perfect difference sets for all prime powers. There is no claim of filtration persistence, uniqueness among all possible supports, external certification or independent auditing.
