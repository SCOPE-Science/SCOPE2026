---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
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

Denisi–Höring Section 3 constructs 0→O(C+)→F→O→0 and identifies the nontrivial Atiyah F2 extension on C_-. Because f_*O(C+)=O_E⊕N, R1=0 and the defining section spans O_E, its class is the pushout from E. On any ruling F|P1=O(1)⊕O, hence R1 f_*Sym^m F=0. The fiberwise monomials z^j a^i b^{m-j-i} form a basis, and their transition b↦b+c a fixes j and acts as the single unipotent Jordan block of rank m-j+1; this yields the stated direct-sum decomposition. Atiyah bundles contribute h0(F_r)=1 at j=0; positive-degree N^j⊗F_r has h0=rjd, h1=0. Summing j(m-j+1)=binom(m+2,3), and Denisi–Höring equation (10) identifies graded section rings R(T_M) and R(F). Independent binomial checks m=0..30 and the nilpotent single-Jordan-block condition dimensions 2..8 corroborated, but all-degree proof is geometric.

## originality

PASS

Denisi–Höring prove non-finite generation and the elementary-transform graded-ring isomorphism but do not state this complete direct-image splitting or closed Hilbert series in their inspected Section 3. Atiyah 1957 gives indecomposable unipotent elliptic bundles; assembling their symmetric powers and the ruled pushout gives the new numerical and sheaf-level refinement, not a new proof of nonfinite generation.

## value

PASS

A simple rational Hilbert series for a provably non-finitely-generated natural symmetric-tensor section algebra is a nontrivial structural invariant. The stronger direct-image splitting identifies all graded dimensions for an entire d,m-family and explains the elliptic-unipotent contribution; these facts can be reused without an algorithm for ring multiplication.

The dated certificate retains the supplied scientific assessment, sources and limitations.
