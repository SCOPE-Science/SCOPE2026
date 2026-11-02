---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

On the real Hilbert space of Hermitian matrices, normalized circular complex off-diagonal variance1 makes standard GUE covariance the identity, so T=I+D*(Sigma-I)D even when Sigma is singular. A unitary preserves the centered Gaussian law exactly when Ad_U commutes with S=D*A D. Differentiating at skew-Hermitian K and testing E_ii forces K_ab(A_bi−A_ai)=0; therefore its Lie algebra is block diagonal for identical-row classes of A. Block-trace representation S(X)=sum a_ab Tr(P_b X)P_a proves every U(C_a) symmetry. Normalizers of this identity component permute the primitive central block projectors; their coordinate permutations preserve the law iff P Sigma P^T=Sigma. This establishes G=(prod U(C_a)) Aut_perm(Sigma), the component quotient and dimension, and full U(M) iff Sigma=I+b11^T with b>=−1/M. I independently tested general complex Haar block rotations, non-symmetry of cross-block rotations, and an example with eigenvalue1 but distinct rows. Tests are finite corroboration; the compact Lie normalizer proof is unrestricted.

## originality

PASS

The exact same-model primary paper Houdré–Kidonakis 2026 introduces the correlated-diagonal Hermitian ensemble and, according to its cited Proposition2.2/Remark2.3(ii), identifies monomial stabilizers subject to 1 not in the diagonal covariance spectrum; exceptional unit eigenvalues were left outside those hypotheses. This theorem completes their exceptional cases with an *exact row-equivalence* criterion, all continuous connected block groups and disconnected permutations, including singular covariance. Its novelty is qualified: the original primary full text was inaccessible through arXiv/other lawful OA; authorized institutional download returned vpn_disconnected, so source comparison used the available abstract, source package’s exact quoted proposition hypotheses and independent mathematical derivation. A general covariance-stabilizer theorem could already imply the specialization without naming this model.

## value

PASS

The symmetry classification resolves a sharp natural exception of a current correlated-diagonal random matrix ensemble. Eigenvalue1 alone does not enlarge symmetry, whereas identical rows of Sigma−I generate continuous unitary blocks; explicit dimensions, components and singular boundaries enable symmetry reduction for probabilistic and spectral questions. It is a complete classification for all PSD covariance matrices and M>=2, not a routine low-dimensional example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
