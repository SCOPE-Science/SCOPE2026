---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

A rank-r square-zero map is exactly a flag I⊆K of dimensions r,n−r and an isomorphism V/K→I. Its count has q-exponent 2r(n−r), so after division by q^(2m(m+epsilon)) the residual exponent is −2k(k+epsilon), with the product ratio p_n/p_(m−k) bounded by one and tending to one. The two flag factors count respectively U=W∩K with prescribed intersection with I and extensions from U to W: in each, after choosing intersection and projected subspace, lifts are graphs of linear maps into a quotient, giving the stated q-power. The finite intersection probability has net q-exponent −b(r−(m−b))=−j(j+k). The Gaussian product factors give beta_k and a uniform summable bound by a q-dependent multiple of q^(−j(j+k)); the defect weights similarly dominate the finite defect law. Uniformity of U means conditional on its DIMENSION b (not on its identity, as the opening wording of Proof's homology paragraph could suggest); it follows from the constant extension count. Generating U with b independent uniform vectors conditioned to be linearly independent incurs error tending to zero. Their unconditioned quotient images are uniform independent entries of an h-by-b matrix; the rank census and tightness normalize the joint law. The FO sentence is equivalent to T_m>0; the zero matrix contributes q^(−hb), including the h=0 or b=0 cases. Independent rational replay `python3 /workspace/audit_replay/parity_bounds.py` bounds both limits to width below 4.34e−19: approximately 0.337415921239570 and 0.436153157721005, inside the advertised disjoint intervals. The verified nonconvergence example uses q=2; convergence of all sentences even within a single parity is not asserted. Inspected the original checker and verification notes; the mathematical limit does not rely on their finite experiment.

## originality

PASS

Credit the known homology-defect marginal and standard counting identities. The supported distinct claim is the joint law with an independent half-dimensional subspace, and specifically its nontrivial parity-paired probabilities for a sentence requiring that subspace to detect homology. Generic parity nonconvergence by itself is not an originality claim: a sentence in D alone can already detect nonzero homology, always present in odd dimensions but absent with positive limiting probability in even dimensions by the known marginal.

## value

PASS

The half-dimensional cut is the natural scale where the kernel intersection has finite random excess and can see a finite random homology space without certain detection. The joint law resolves that critical sampling regime and gives quantitative first-order probabilities strictly between zero and one for a genuinely probe-dependent sentence, not just a restatement of unavoidable parity of the defect.

The dated certificate retains the supplied scientific assessment, sources and limitations.
