---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

For a two-colouring of \(K_n\), every edge has \(2n-4\) adjacent edges, so both colour counts must equal \(n-2\). If \(d(v)\) is the red degree, this gives \(d(u)+d(v)=n\) on red edges and \(n-2\) on blue edges. For odd \(n\), three pairwise degree sums cannot all be odd. For even \(n\), all degrees have the same parity, differ by at most two, and exactly two values occur; one degree class must be a singleton. The red graph is therefore a star or a clique plus an isolated vertex, and the degree gap forces \(n=4\). The submitted three-colour constructions for \(n=3,5,7\), and the equitable three-part construction for \(n=6\) and \(n\ge8\), meet the threshold. An independent exhaustive replay of every two-colouring for \(K_3,K_4,K_5\) confirmed that only \(K_4\) admits two colours.

## originality

PASS

The defining 2026 strong-majority paper gives the complete-graph upper bound \(\operatorname{Maj}'(K_n)\le3\) and easy small constructions, but not the exact two-colour obstruction. It also states a general observation that index two can occur only when all vertex degrees are even; the explicit \(K_4\) star/triangle colouring satisfies the paper's definition and directly contradicts that observation. The later minimum-degree theorem also supplies only a three-colour upper bound for large complete graphs. No Resultary hit or primary source inspected states the exact family formula with the unique \(K_4\) exception.

## value

PASS

Complete graphs are the canonical dense test family for the newly introduced invariant. The theorem gives the exact index at every order, identifies the unique exceptional two-colour case, and exposes a counterexample to an erroneous general parity observation in the defining paper. That is a natural exact family classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
