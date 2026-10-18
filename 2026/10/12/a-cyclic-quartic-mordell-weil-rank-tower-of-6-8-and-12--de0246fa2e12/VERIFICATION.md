---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

The curve coefficients lie in C(v⁴,t), with s=v² and Gal(C(v,t)/C(w,t))=C4. Burek Theorem 1.1/Proposition 5.6 establishes generic rank 12; Appendix A.10–A.12 establishes 12 independent specialized sections (height Gram determinant 4096/9). An independently written exact SymPy reconstruction from the source formulas evaluated all 12 section Weierstrass identities at v=5, reconstructed 12x12 H, computed 144 transformed pairwise local/gcd heights for v=5i and the order-two counterpart at v=-5, found T=H^{-1}G with T^4=I, T^TH T=H and traces (12,4,4,4), and verified the independent order-two matrix T². Separate exact arithmetic on the full printed 12x12 integral T confirmed characteristic polynomial (λ−1)^6(λ+1)^2(λ²+1)^2 and invariant dimensions 6 and 8. Injectivity of the twelve-dimensional specialization and ordinary Galois descent, not mere sampling, provide the global rank conclusion. Does not establish integral MW saturation or arithmetic ranks.

## originality

PASS

The exact fixed-field rank profile and rational cyclic-character refine the known rank-twelve family. Neither Burek's rank-12 theorem/height table nor Kumar–Kuwata's explicit geometric lattice/field-of-definition statements alone supply the specific C4 fixed-subspace multiplicities without the mixed-height computation.

## value

PASS

Nontrivial explicit arithmetic-geometric descent of a natural new rank-twelve elliptic surface family: gives three exact ranks and its rational cyclic action. These are missing precise invariants for the natural quartic coefficient quotient, not an arbitrary computational slice. No claim of integral MW generators or saturation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
