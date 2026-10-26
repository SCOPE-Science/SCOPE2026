---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducible verification

Run `python3 verify.py` using only the Python standard library. The program has two separately specified paths: it enumerates labelled spanning trees as connected acyclic edge subsets and calculates the overlap histogram of every ordered pair, while its rational polynomial arithmetic independently evaluates the formula for \(\mathbb E[t^{X_{3,n}}]\).

The program enumerates all \(432\) trees of \(K_{3,4}\) and their \(186{,}624\) ordered pairs, and all \(2025\) trees of \(K_{3,5}\) and their \(4{,}100{,}625\) ordered pairs; every coefficient agrees exactly. It confirms the edge-disjoint pair count and performs 37 additional exact-rational polynomial checks for \(4\le n\le40\), including nonnegative coefficients, coefficient sum one, the mean, variance, and zero-overlap identity. Observed final marker: `VERIFY_OK exhaustive_pairs= 4287249 additional_rational_laws= 37`.

The all-parameter independent convolution theorem is a symbolic consequence of the bounded-degree-core construction in `RESULT.md`. The finite checks do not certify the theorem for all orders; they test two full exact histograms and additional formula specializations. Literature-priority assessment is also separate from computational correctness.
