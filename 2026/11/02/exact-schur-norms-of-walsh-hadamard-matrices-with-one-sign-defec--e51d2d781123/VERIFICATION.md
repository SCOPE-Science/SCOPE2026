---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

PASS: For complex operator-norm Schur multiplication, operator/nuclear duality gives ||S_M||=max_{p,q in simplex} ||diag(sqrt p) M diag(sqrt q)||_1. This is quantum fidelity between A=diag p and B=M diag q M^T and is jointly concave by the positive-matrix variational formula, allowing averaging over simultaneous GL(d,2) actions and transpose to p=q with two orbits {0} and nonzero characters. The reduced symmetric C has N−2 singular values sqrt N; its remaining 2D Gram eigenvalue sum simplifies to sqrt(t²+(4N−6)t+1). Thus F(t)=((N−2)sqrt N+sqrt(t²+(4N−6)t+1))/(t+N−1), whose unique t≥0 maximizer t_N=2sqrt(N(N+2))−(2N+1) gives boxed formula for N=2^d>=8. Expanding yields deficit N^-3/2+O(N^-7/2); row/column Walsh translations preserve norm of an arbitrary one-entry flip. Fresh independent numpy nuclear-SVD checks for N=8,16,32 recovered formula and optimizer to numerical precision, but global proof uses joint concavity and exact spectrum. Arbitrary asymmetric optimizers are not claimed to be unique.

## originality

PASS

PASS (qualified): Holbrook–Johnston–Schoch show the general √N bound with equality precisely at genuine Hadamard matrices, and tabulate the order-four single-defect value, which is expressly not new. Davidson–Donsig transitive-symmetry norm formulas and Christensen's general self-adjoint variational representation describe broader frameworks but do not explicitly evaluate the nontransitive two-orbit one-flip Walsh family. The new contribution is the complete all-dyadic closed form, explicit optimizing weights and exact N^-3/2 loss. An earlier factorization or near-Hadamard perturbation formula remains possible.

## value

PASS

PASS: This gives a sharp quantitative stability law for an extremal family of Schur multipliers under the smallest combinatorial sign perturbation. The exact norm deficit and explicit probability-weight optimizer answer a natural condition-number/norm robustness problem beyond the known strict inequality, for every dyadic order rather than a single numerical example. Neither a generic SDP restatement nor a small-order lookup suffices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
