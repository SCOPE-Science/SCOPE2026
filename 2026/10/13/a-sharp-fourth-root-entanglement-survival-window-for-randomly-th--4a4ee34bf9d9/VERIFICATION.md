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

## Analytic chain

For a graph-state generator \(K_i=Z_{i-1}X_iZ_{i+1}\), every surviving stabilizer is indexed by a retained-only binary vector satisfying \(u_{j-1}+u_{j+1}=0\) at all erased sites \(j\). Two consecutive erased sites separate the constraint system; at cluster endpoints its indexed bits must vanish. Every component of at most three retained sites, or four without four consecutive sites, has at most one independent remaining generator and thus yields a fully separable marginal. The complement of this separability event is included in the union of four-consecutive-survivor windows and five-survivor gap patterns; there are at most \(16n\) patterns of the latter. The known four-site NPT certificate supplies the lower inclusion.

Four-run factorial moments give a Poisson limit when \(nr^4\) converges and \(r\to0\); overlapping windows require extra retained sites and vanish at that scale. The disjoint-block bound proves the supercritical assertion. The claimed convergence is analytic, not an inference from finite tests.

## Standalone computations

Run `python3 verify.py` from the extracted document directory. Python 3 standard library only. The direct binary-linear-algebra checker enumerates every retained subset for \(n=10,11,12,13,14,15\), giving 64,512 masks, and tests 22,297 masks within the separability side of the sandwich. It verifies cluster-wise stabilizer rank at most one and checks that the sum of component ranks equals the full surviving stabilizer rank (53,569 local component certificates). The program additionally checks the \(-1/8\) sign of the four-site partial-transpose eigenvalue. The resulting output is `VERIFY_OK`.

## Scope and remaining limits

These are finite linear-algebra computations; they do not establish the asymptotic theorem. The proof itself requires the graph-state formula, a finite-dimensional tensor-product separability argument, and the standard Poisson factorial-moment method. The statistics concern non-full-separability only, not distillable entanglement, violation of Bell inequalities, or quantum error-correction success. Independent audit has not been performed.
