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

# Reproducibility of exact endpoint calculations

The standalone file `verify.py` runs with Python 3 and no third-party dependencies. Executing `python3 verify.py` in the extracted artifact directory evaluates every possible allowed-edge mask for orders \(2,3,4\), tests it for total support against every permutation matrix, reduces by independent row and column relabelings, and inverts the relevant Gram matrices using exact rational arithmetic. Its expected support/orbit counts are \((3,2)\), \((49,6)\), and \((7443,42)\). The resulting exact maxima are \(1,16/9,9/4\).

The same verifier constructs the support \(j-i\in\{0,2,3,6,8,9\}\pmod {12}\), computes the selected projection row at \((0,2)\), validates all nine exact row-entry multiplicities, checks the projector-row identity \(\sum_fR_{ef}^2=R_{ee}\), and certifies \(41/12-121/36=1/18\). It also verifies the optimal row-sign pairing. Because the row is computed from the full exact Gram inverse, no floating-point tolerance, external dataset, probabilistic search or unlisted dependency enters these certificates.

The code verifies the finite algebraic facts, while the main proof supplies the necessary complete-face and piecewise-affine reduction to all possible real inputs. The twelve-order certificate is not an exhaustive classification of all faces. Independent scientific validation is not performed.
