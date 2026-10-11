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

The standard \(\ell\)-step derivative is a bijection from a source word to its length-\(\ell\) prefix and derivative tail, and one length-\(\ell\) tandem duplication inserts \(0^\ell\) into that tail. For a fixed nonzero skeleton, distinct source tails are described by zero-run vectors. Two distinct tails share a one-duplication output exactly when one is obtained from the other by transferring \(\ell\) zeros from one zero run to a distinct zero run; the two changed coordinates uniquely determine the common output, proving multiplicity one. For skeleton length \(s\), oriented transfers are counted by \(s(s+1)\binom{n-2\ell}{s}\), so unordered edges contribute half that. Summing over \((q-1)^s\) skeletons and \(q^\ell\) prefixes, then differentiating the binomial theorem twice, gives the closed formula and boundary \(n\le2\ell\). The inspected verifier reconstructs the channel directly over many finite \((q,\ell,n)\) values and matches the formula, but the general proof is combinatorial.

## originality

PASS

The primary tandem-duplication literature supplies the same derivative transform, zero-run/signature representation, sphere bounds, and descendant-cone intersection machinery, but no inspected source aggregates the exact-one confusability relation over all length-\(n\) sources to obtain this all-parameter edge formula or states that every conflict has exactly one common one-error descendant. Targeted Resultary and web searches found no implication-equivalent published SCOPE record or exact table.

## value

PASS

The confusability graph is the natural graph whose independent sets are one-error-correcting codes. An exact edge count for every alphabet size, block length, and source length, together with the exact common-descendant multiplicity, gives structural density information that is reusable for probabilistic, spectral, and extremal studies of these codes. This is an all-parameter invariant, not an arbitrary finite census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
