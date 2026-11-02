---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

PASS: Summing internal spins on each path yields endpoint weights P_±=prod_i(1±s_i t^{ell_i}), with correlation (P_+-P_-)/(P_++P_-), denominator positive for 0<t<1. Base numerator factorization -2t²(1-t²)²(1+t²+t⁴)Q(t) was recomputed exactly, as were all 19 coefficients of transformed (1+z)^18 Q(z/(1+z)). There are exactly two Descartes sign changes. Direct exact signs of the numerator at t=7/10,3/4,4/5 are -,+,-, proving exactly two simple roots with no extra tangency. The signed inverse-tanh sum is negative as t->0 and t->1 and positive at 3/4; increasing either negative long path length preserves positivity there, giving >=2 roots for every 9<=d<e. For <=3 paths, two positive and one negative reduction gives a polynomial with two positive sign variations, including the simple t=1 root, thus at most one interior root. Independent direct spin enumeration on a small three-branch graph checked path elimination. The finite d,e grid in the package is not used to infer the infinite family.

## originality

PASS

The signed-terminal-correlation law of a series-parallel theta network is standard. The checked potential new theorem is an equal-absolute-coupling *five*-path Ising network with exactly two finite-temperature sign changes, an infinite family with at least two, and a three-path impossibility boundary. Primary decorated-bond work has known nonmonotonicity and a single-crossing example but no inspected result implying the two-root 25-vertex example. Priority is best-of-knowledge, not exhaustive.

## value

PASS

PASS: Reentrant sign of two-terminal thermal correlation under frustration is a natural observable; exactly two reversals with *identical absolute couplings* and no magnetic field identify a nontrivial topological entropy-competition mechanism. The rigorous Descartes root-count certificate and at-most-three-branch comparison give meaningful structural boundaries; a single approximate 25-vertex witness alone would not suffice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
