---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Sign reversal of a (t,t,1−2t) law reverses p_t(z), leaving four candidates up to global reflection. Log-concavity of each support convolution localizes modes, and the source exact ordered-simplex barycentric substitution gives eight homogeneous cubic modal comparisons with 20 coefficients apiece, all nonnegative. I independently reconstructed all 160 integer coefficients using separate JS polynomial convolution of the actual ordered vertices; all exactly matched COEFFICIENTS.tsv with minimum 0. Five coefficient factorizations dominate two mixed patterns, leaving A=ab+ac+bc−3abc and B=7abc−4ab−ac−bc+a+b, with A−B=(1−2c)(5ab−a−b). Strictly ordered interior cases have unique optimal sign up to global reversal, ties at equality, and endpoints follow weak inequalities; rational examples corroborate but do not prove continuum theorem.

## originality

PASS

Best-of-knowledge: no inspected preceding concentration result computes the complete ordered heterogeneous three-variable sign optimum for the three-atom canonical extremal laws or the phase 5ab=a+b. Kurauskas gives an asymptotic concentration bound and states exact conjectural sign-selection, Madiman--Wang--Woo give gap-closing majorization, and Singhal treats Bernoulli laws; none directly implies the stated fixed-three-variable reflection optimization.

## value

PASS

The signed optimal ordering of the standard three-atom concentration extremizers is an explicit finite case of Kurauskas’s natural conjectural extremal formalism. It supplies a complete heterogeneous chamber classification with an unexpected two-smaller-parameter boundary independent of the largest, a precise fact unavailable from the asymptotic bound and potentially useful in understanding higher-summand signed convolutions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
