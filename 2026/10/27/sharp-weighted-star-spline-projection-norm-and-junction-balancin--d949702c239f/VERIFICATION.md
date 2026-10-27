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

# Verification and proof-to-evidence correspondence

The theorem covers all integers \(m\ge3\), all strictly positive arm lengths and positive edgewise constant densities, and real or complex bounded data. A separate exact-arithmetic checker, `check_star.py`, constructs the Gram matrix directly from hat-function integrals, inverts it without floating-point arithmetic, and integrates affine kernels by exact root splitting. Running `python check_star.py` must print a PASS message after 225 nontrivial rational input cases, plus balanced and degenerating cases. These are reproducibility checks and are not a finite proof of the stated real-parameter theorem.

The analytic verification has five independent points: the Gram entries integrate to \(M/3\), \(\mu_i/6\), and \(\mu_i/3\); its leaf Schur complement is \(M/4\); vertex kernels are the displayed affine formulas; their signed-root integrals equal the central value \(5/3\) and leaf values \(7/3-4\mu_i/[3(M+\mu_i)]\); and the strictly decreasing dependence on each normalized arm mass gives all extremal cases. Strict convexity of integrated absolute kernels along an arm follows from oppositely signed central/terminal kernel rows on other arms.

An extremizing bounded input exists by taking the sign of a minimizing-leaf kernel almost everywhere. If input continuity is imposed, its sign jumps may be approximated in the weighted \(L^1\) norm by continuous bounded inputs, yielding the same *operator norm* as a supremum; no continuous sign-extremizer is asserted.

Scientific limitations include restriction to exactly one linear element per arm and inability of semantic literature searches to prove historical uniqueness. No independent audit was conducted.
