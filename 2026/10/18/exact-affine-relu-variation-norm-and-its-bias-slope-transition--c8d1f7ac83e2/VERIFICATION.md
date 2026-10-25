---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

For scalar real affine f(x)=<a,x>+b on an entire real separable Hilbert space and signed ReLU parameter measures in the *joint* Euclidean unit ball, line restriction along a/||a|| contracts TV. In one dimension decompose w=0 mass as constant c and push the w>0,w<0 parts to signed kink measures alpha±(t) weighted by |w|; the parameter-ball condition bounds their first absolute moments by TV. Vanishing distributional second derivative of the affine target enforces alpha_-=-alpha_+, and first moments fix slope s=||a|| and intercept b-c. The Euclidean vector-measure triangle inequality gives TV>=|c|+2 sqrt(s^2+(b-c)^2) for arbitrary signed Borel measures, not just atomic networks. Convex minimization in c produces exact branches 2 sqrt(s^2+|b|^2) for |b|<=s/sqrt(3) and |b|+sqrt(3)s above; explicit antipodal ReLU kink atoms of mass ±s sqrt(1+t^2), with an optional flat c atom, attain both. Kink cancellation proves two atoms minimally below/equal threshold and three strictly above; constant and zero exceptions checked. Independent six-parameter SciPy scalar minimizations and direct pointwise ReLU representation checks agree to numerical tolerance, but do not replace the distributional proof.

## originality

PASS

The homogeneous zero-bias linear variation norm is covered by Yang and Shi; this claim determines the sharp *biased* affine value and the support-size threshold under that identical joint Euclidean parameter unit ball. Other Barron BV seminorm identities and finite-width regularizers use only equivalent rather than exact norms or allow a free intercept; neither is shown to yield the precise sharp two-branch equality. Available source comparison supports best-of-knowledge originality with substantial normalizations caveat.

## value

PASS

This exact affine subspace norm is a natural quantitative building block in bias-penalized infinite-width neural variation spaces. The nontrivial threshold |b|=||a||/sqrt(3) and accompanying two-versus-three minimum neuron support describe a real sparsity transition, not arbitrary parameter tabulation; the result is dimension independent and gives exact variation budget for affine functions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
