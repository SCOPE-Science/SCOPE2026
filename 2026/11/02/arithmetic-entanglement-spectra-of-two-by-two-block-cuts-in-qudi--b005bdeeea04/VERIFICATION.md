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

The pure prime-qudit graph-state phase across a cut is omega^(x^T Gamma y); tracing B produces kernel coset blocks and exactly p^R equal eigenvalues p^-R where R=rank_Fp Gamma. For diagonal rectangle blocks A, all crossing adjacency outputs depend solely on row/column margins, whose only two compatibility constraints leave m+n-2 dimensions. Kernel of the margin-to-output map has constants alpha,beta obeying [[a,c],[d,b]](alpha,beta)=0, dimension 2-r_p. Therefore rank Gamma=m+n-4+r_p and all Rényi spectra follow. Direct independent finite-field Gaussian elimination of the literal rook cross-cut matrices confirmed formula for 243 cases a,b,c,d=1..3, p=2,3,5. All prime p and positive block sizes covered algebraically; arbitrary cuts not claimed.

## originality

PASS

General graph-state Schmidt rank=cut adjacency rank is old, as is qubit rook graph topological code construction. Liao-Sanders-Feder full arXiv HTML §IV.2.5 and Appendix F analyzes balanced L(K_m,m) graph codes and Hamming weights, not this qudit two-by-two block-cut spectrum. The computed four-block modular trichotomy is a distinct exact specialization.

## value

PASS

A natural symmetric graph-state family has a surprisingly low-entropy macroscopic diagonal checkerboard cut and prime-dependent jumps. The formula supplies precise Schmidt spectra usable to assess structured cuts and code-state entanglement, rather than merely restating a universal rank identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
