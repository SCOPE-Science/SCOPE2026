---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

The block operator has norm \(2\) and a nonzero kernel; the orbit identity \(T\Theta_k=\Theta_{k+1}\) holds for every integer index. The negative and positive geometric-series contributions are \(4/3\) and \(1/3\), giving tight bound \(5/3\). Orthogonal negative-index ranges force infinite-dimensional operator span, while \(\Theta_2=\Theta_1/2\) is an explicit dependence. For the repair, any finite dependence gives a finite forward-invariant span; injectivity on the algebraic range span allows the relation to be propagated backward, forcing the whole bi-infinite orbit into a finite-dimensional space and contradicting the hypothesis.

## originality

PASS

The primary preprint was read at the disputed statements: Proposition 4.1 asserts linear independence from an infinite-dimensional operator span under forward representation, but its proof uses negative powers of the representing operator without assuming invertibility; Theorem 4.3(ii) invokes that proposition. The explicit noninjective example therefore contradicts the source as stated. The later journal record is described in accessible preview material as a reedited copy, but its full theorem body was not available in this run, so the accepted claim is intentionally scoped to arXiv v1. No prior equivalent counterexample or the same injectivity repair was located.

## value

PASS

The result identifies a genuine missing hypothesis in a structural lemma used downstream and supplies a clean sufficient repair inside the intended tight g-fusion-frame setting, rather than a type or normalization defect.

The dated certificate retains the supplied scientific assessment, sources and limitations.
