---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The monitored-to-unmonitored adjacency block B is the Boolean inclusion matrix, so B*B=kI+A_U and H equals −k on the unmonitored ker B. The up/down commutator at level l is (n−1−2l)I, giving injectivity of the up map below the middle level; complementing sets supplies the other side. This covers the central square matrix and endpoint levels, giving d=max(0,u−v). The real part of the Hilbert–Schmidt generator form is −1/2 times the positively weighted sum of squared monitored commutators. Every imaginary-axis eigenoperator is therefore block diagonal with diagonal monitored block. At zero frequency the adjacency of the monitored Johnson graph makes that block scalar; the two cross-block equations then make the remainder supported on ker B on both sides. At nonzero imaginary frequency the monitored diagonal instead vanishes, and the same cross-block equations leave only ker B, on which the Hamiltonian commutator vanishes. Contractivity rules out Jordan blocks at zero or elsewhere on the imaginary axis. The dark compression remains constant and trace preservation fixes the scalar on its complement, proving ordinary convergence. Permutation transitivity gives local dark weight d/u, and evaluating the limiting diagonal gives the two return formulas. At n=2k there is no dark component; at n=2k+1 the central binomial difference equals C_k and the bright dimension is 2k C_k, giving the exact return and k²R→1. Independent numerical incidence and small unequal-rate generator tests, including coherent initial states, and exact finite Catalan identities agree with the proof.

## originality

PASS

Bounded pass for the exact stationary algebra, actual Lindblad limit and local-return comparison for this monitor geometry. The Johnson harmonic multiplicity and general Lindblad asymptotic framework are prior ingredients. The closest indexed overlap has the same dark projector and Catalan rank for absorbers but is later and has a capture law, not the dephasing limit stated here.

## value

PASS

A natural site selection on a standard graph family gives an exact memory algebra for arbitrary positive rates, and the comparison across adjacent central ranks changes an experimentally meaningful model observable, local return, from exponential to quadratic inverse decay. The statement explains why and when coherences are preserved, rather than just supplying a single dimension or a numerical asymptote.

The dated certificate retains the supplied scientific assessment, sources and limitations.
