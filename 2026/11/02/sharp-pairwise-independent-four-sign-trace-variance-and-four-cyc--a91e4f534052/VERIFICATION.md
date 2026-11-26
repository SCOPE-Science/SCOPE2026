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

Pairwise products give the trace mean. In the centered square, diagonal edge-pair terms contribute four times the sum of squared edge weights, intersecting distinct edges reduce to pairwise sign moments of zero, and disjoint edges give the three cross terms with coefficient eight times the common fourth moment. Both fourth-moment endpoints are realized by fair uniform parity laws. At a forced endpoint the first and second moments vanish and each triple moment equals the parity times the complementary singleton moment, so Walsh inversion uniquely determines the entire law. At S=0 all laws are optimal; completing squares proves the zero-variance criterion. For the nonnegative weighted cycle S=ac+bd; the odd parity formula follows, including weight-zero cases. For spectral functions of the unweighted cycle, cyclic symmetry pairs the opposite entries and gives exactness for an exact matrix-function action; independent block choices retain isotropy. The eigenvalues of I+A/4 lie in [1/2,3/2] and the iid variance is 1. Below four coordinates there are no disjoint edge pairs. The finite rational checks in verify.py complement the proof; the supplied script was inspected, not executed, and does not enumerate all feasible laws.

## originality

PASS

The supported distinct claim is the exact matrix-dependent optimum and complete equality-law classification over the entire fair pairwise-independent four-sign class, together with its weight-uniform cycle defect law. Fourth-moment methods, independent-sign variance and fixed structured probes are not new. The strongest inspected exact formulas cover specific probe designs or different couplings, rather than all feasible laws and their uniqueness in this problem.

## value

PASS

This identifies when dependence is useful without changing any pairwise sign statistics, in the smallest dimension where it can make a difference. It distinguishes a matrix-dependent optimal law from a single law that works for all nonnegative four-cycle weights, and gives the exact degradation from imbalance of opposite weights. The full equality-law result is useful as a benchmark for small correlated-probe designs; neither the standard fourth-moment identity nor fixed-design evaluations alone answer that design question. It is not a general trace-oracle optimality claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
