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

On this perfect-detection Markov life cycle with constant immigration, the local one-year bank is Y from the previous census, so successive visible pairs are the states. With u=1−d and w=u(1−c), independence gives q_yz=u−w(1−g0)^y(1−g1)^z. In coordinates (q00,a,b,r) this is (u−w,wg0,wg1,wg0g1), yielding w=ab/r. Positivity of q00, the strict inequalities on r and the upper bound on q00+w are exactly what is needed for 0<w<u<1 and 0<g0,g1<1. Substitution recovers every table entry. The determinant in the listed order is −u w² g0 g1, agreeing with the frozen formula; at g1=0 the lag contrast and determinant vanish. Every pair is reached with positive probability in two steps and the chain has self-loops, so stationary conditional denominators are positive. In the pair law, stationarity imposes pi01=pi10, and flow into 00 and 11 fixes pi01/pi00=q00/(1−q01) and pi11/pi01=q10/(1−q11). Conversely those two ratios and normalization give every pair frequency. Fixing the ratios gives two independent affine constraints in the open table domain, so each interior parameter has a local two-dimensional fiber even though the triple gives all four conditionals. The stationary linear solve and 256 exact rational round trips were independently replayed, including the frozen witness and a distinct witness with the same pair law.

## originality

PASS

PASS for the exact global interior inverse, its strict feasible-table characterization and the sharp stationary law horizon with two-dimensional pair-law fibers. Do not credit the observable-state reduction itself, or the idea of using three-year histories, as new: the 2017 follow-up makes both explicit. The accessible likelihood and simulation sections do not establish the surviving exact law-level theorem.

## value

PASS

For the constant-immigration ecological model used in real survey methodology, the exact short-horizon distinction matters: the pair law leaves continuous parameter ambiguity, whereas replicated three-census histories can in principle recover the full interior model. The feasible-table inequalities are a concrete diagnostic of compatibility with the assumed life cycle. The result isolates structural limitations and does not assert reliable estimation or that three realized observations suffice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
