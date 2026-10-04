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

# Verification

The proof has two logically separate parts.

First, the infinite convergence statement uses Bernshteyn's published results: the Borel fractional chromatic number of the free-part Bernoulli Schreier graph is the reciprocal of its measurable independence number, and measurable independent sets can be approximated from below in measure by clopen independent sets. Since clopen subsets of \(2^\Gamma\) depend on finitely many coordinates, the best independent cylinder density over an increasing finite exhaustion converges monotonically to the measurable independence number.

Second, the effectiveness statement is finite. For fixed \(D\), \(\Phi\), and \(\sigma\), independence is decided by testing whether two finite cylinder assignments are compatible on the overlap of \(D\) and \(D\sigma^{-1}\). A presentation with decidable equality makes those overlap tests decidable. Exhaustive search over \(\Phi\subseteq2^D\) therefore computes \(\rho(D)\) exactly.

`artifacts/verify.py` checks the finite construction on \(\Gamma=\mathbb Z\) with \(F=\{1\}\). For supports of lengths \(1,\ldots,6\), it obtains maximum pattern-family sizes \(0,1,2,6,12,27\), verifies direct shift-independence of every returned witness, and checks monotonicity of the corresponding densities.

The finite replay does not verify the infinite clopen-approximation theorem; that theorem is taken from the cited primary source. No claim is made about the computational complexity of the finite optimization.
