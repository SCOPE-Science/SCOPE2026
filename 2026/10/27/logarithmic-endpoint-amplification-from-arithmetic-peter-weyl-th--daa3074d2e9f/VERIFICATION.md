---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The full-block central kernel is the dimension-weighted sum of characters, not the projection kernel on the span of the characters alone. Convolution has both strong endpoint norms equal to the Haar L1 mass (phase test and approximate identity), so the Weyl-weighted integral is (2/pi) times the integral of |T| sin(theta). Differentiating the finite geometric sum gives the stated cosine numerator with frequency qM+r−q/2 and first-order poles at qth roots of unity. The removed intervals of radius 1/M cost O_q(M) by |T|=O_q(M²); outside them the second-order remainder integrates to O_q(M). At each interior pole the weighted residue is M sin(2 pi h/q); bounded-primitive averaging of |cos| contributes (2/pi) log M+O_q(1) on each side, uniformly in phase. The Weyl factor gives exactly (8/pi²) sin(2 pi h/q) per interior pole, including C_3=4 sqrt(3)/pi². At 0 and pi the vanishing weight costs only O_q(M); for q=1,2 these are the only possible poles. Constants are for fixed q and uniform over its finitely many r. The analytic argument establishes the asymptotic; the recorded 8,288 finite checks were inspected in source, not rerun.

## originality

PASS

The supported distinction is the exact fixed-modulus logarithmic amplification at interior Weyl angles, with residue-independent leading coefficient and an O_q(M) remainder. Single blocks and standard consecutive kernels do not give this result. The q=1,2 comparison is background rather than a separate claim of novelty. The result is distinct to the best of the inspected evidence, not a historical-priority certification.

## value

PASS

Selecting a full residue class is a natural periodic spectral filter. The theorem shows that regular thinning can increase worst-case endpoint amplification by a logarithm, locates the first modulus where this occurs, and gives the sharp coefficient through the interior Weyl-angle weights. This quantifies a genuine distinction between central parity selection and higher moduli, not merely an alternative expression for the consecutive norm.

The dated certificate retains the supplied scientific assessment, sources and limitations.
