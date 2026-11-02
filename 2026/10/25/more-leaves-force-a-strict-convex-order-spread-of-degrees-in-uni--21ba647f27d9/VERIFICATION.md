---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

PASS: Prüfer coding makes the leaf count n-j equivalent to exactly j occupied labels in an N=n-2 word. Conditioning gives P(X_j=c)=binom(N,c) S(N-c,j-1)/(n S(N,j)) (c>=1), and P(X_j=0)=(n-j)/n, with fixed EX_j=N/n. Size-bias gives q_j(c)=binom(N-1,c-1)S(N-c,j-1)/S(N,j). Real-rooted Bell polynomials imply log-concave Stirling coefficients; the Stirling recurrence proves strictly decreasing S(t,r-1)/S(t,r) in t. Therefore q_{j-1}/q_j increases in c (with endpoint support), yielding strict stochastic order of size biases. The increasing secant-slope representation transfers it into strict convex order of degrees and the covariance consequences. Independently enumerated all Prüfer words for n=4..7 (16,125,1296,16807), checking every adjacent conditional convex-hinge comparison. The universal conclusion rests on the recurrence proof.

## originality

PASS

PASS (qualified): Tagged degree conditional on leaves is classical uniform-ball occupancy conditional on occupied-bin count, so general occupancy stochastic-order theorems are serious possible dominators. The accessible O’Neill 2023 complete article treats occupancy count and spillage, not the strict convex order of one specified bin load across fixed occupied-count classes. Remmel–Williamson ranks fixed-leaf trees; this does not itself establish the strict cross-class likelihood-ratio comparison. Historical general Stirling-TP or urn/occupancy order coverage remains a real risk.

## value

PASS

PASS: Exact leaf count is a natural degree constraint for Cayley trees; all strictly convex local degree costs increase while the conditional mean stays fixed. This stronger finite-n comparison clarifies how hub concentration responds to leaf conditioning and is not simply a variance calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
