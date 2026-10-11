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

For nonempty rows \(R_i\) and \(R_j\) with \(i<j\), forward confluence is equivalent to \(\max R_i<\max R_j\): the later maximum witnesses every earlier element, while failure at the earlier maximum is decisive. Backward confluence is equivalently \(\min R_i<\min R_j\). Hence total expansiveness is exactly strict increase of both endpoint sequences. The existence condition \(m\le n\), the minimum-size functional relations counted by \(\binom{n}{m}\), and the maximum \(m(n-m+1)\) with interval rows follow from the available slack in the two strict endpoint sequences. A fresh exhaustive replay for all relations with \(m,n\le3\) reproduced the endpoint criterion, zero counts for \(m>n\), and all size extrema.

## originality

PASS

Fernández-Duque introduces expansive relations as the forward-and-backward-confluent morphism notion and develops their closure and selection machinery, but complete inspection of the primary paper found no finite-chain normal form, size extremals, or exact relation count. Rowwise expansiveness on chains is a strict analogue of the classical Egli-Milner subset relation, so the endpoint proof is order-theoretically natural; nevertheless, the inspected powerdomain literature does not state the all-relation census or extremal formulas between chains. Current Resultary and web searches found no prior exact classification.

## value

PASS

Expansive relations are a central morphism notion in the current finite-model construction, and strict chains are the canonical test objects. A complete all-relation normal form, exact count, existence threshold, and sharp cardinality extrema provide a natural finite invariant and usable search-space description even though the proof is elementary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
