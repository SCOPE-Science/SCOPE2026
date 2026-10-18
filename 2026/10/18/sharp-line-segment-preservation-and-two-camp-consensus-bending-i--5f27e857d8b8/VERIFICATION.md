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

# Mathematical verification

The proof, rather than a finite computation, provides the infinite-time claim. Its essential identities are the two characteristic velocities, the weighted-mean derivative, and the positive quadrature for the normalized consensus difference. The proof treats the four equality cases separately, establishes strictly positive quadrature in all complementary cases, and evaluates the weak-locality coefficient as a convergent explicitly integrated expression.

Run `python3 check_two_camp_geometry.py` using Python 3 and no third-party dependencies. The checker passed \(81\) independent exact rational algebra configurations and finite numerical tests of a strict example, topic-importance order reversal, both topic-gap orders, and the two degenerate locality endpoints. It also checked the first-order onset via \(\beta=0.001\) and \(\beta=0.003\): computed difference quotients were approximately \(0.06024163\) and \(0.06020172\), compared with the analytic coefficient \(0.06026154\). The finite-time integration reaches a common-camp discrepancy below \(10^{-9}\); it is not an exhaustive parameter sweep or an infinity certificate.

Limitations: The argument uses strictly ordered initial coordinates and positive affine influence. The general published model includes a broader family of influences, importance distributions and initial probability measures; those are outside the mathematical claim. Historical novelty remains subject to independent scrutiny.
