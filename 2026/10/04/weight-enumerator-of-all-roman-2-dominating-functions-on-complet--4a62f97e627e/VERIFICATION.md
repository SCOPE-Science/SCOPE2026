---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

Writing \(A\) and \(B\) for the total numbers of labels \(1\) and \(2\), a zero in part \(i\) is defended exactly when \(B-b_i\ge1\) or \(A-a_i\ge2\). The package's three regimes are exhaustive and disjoint. If label \(2\) occurs in at least two parts, every zero sees a \(2\) outside its own part. If it occurs in exactly one part, zeros in that same part require at least two outside labels \(1\), while zeros outside automatically see the unique \(2\)-supporting part. If no label \(2\) occurs, a selected \(t\)-set of ones is invalid precisely when some nonfull part contains \(t\) or \(t-1\) selected vertices; for \(t\ge3\) these failures are disjoint across parts, while \(t=2\) gives exactly a whole size-two part or two singleton parts. Those cases reproduce the displayed \(c_2\) and \(q_t\) coefficients. A fresh independent replay on every complete multipartite profile through order six matched the literal vertex definition and the local criterion.

## originality

PASS

Roman \(\{2\}\)-domination is also called Italian domination. Padamutham and Palagiri's open primary article computes minimum values and algorithms on complete bipartite, chain, and threshold graphs, while the 2024 survey catalogues the broader Roman \(\{2\}\) literature. Neither inspected source states an all-function weight enumerator for complete multipartite graphs. The September 2026 paper on Italian domination polynomials counts weights on paths, trees, and cycles, confirming that the enumerator is a recognized invariant while leaving this graph class uncovered. Current Resultary searches returned the assigned multipartite enumerator as the exact hit and no stronger prior theorem implying its three-regime coefficient formula.

## value

PASS

The all-weight Italian/Roman-\(\{2\}\) polynomial is now explicitly studied as an enumerative invariant in the literature, and complete multipartite graphs are a canonical dense graph class. The three-regime formula gives every coefficient and exposes structural transitions that the known minimum parameter cannot see. It is therefore a motivated exact invariant, not an arbitrary finite slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
