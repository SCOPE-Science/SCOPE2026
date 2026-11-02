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

The n-th power splits orthogonally into n irreducible unilateral shifts, one for each residue r mod n, with weights a_(r,k)=prod_{j=0}^{n-1}w_(r+nk+j). Irreducibility follows from ker(V*)=span{e0} and cyclic orbit V^k e0; a single shift attains norm exactly when sup weights is reached. In a finite direct sum, intertwiners commuting with both shift and adjoint identify only unitarily equivalent irreducibles, so every reducing subspace is a direct sum of their copies and attains its norm if and only if all residue shifts do. Exact rational telescoping for w0=3/2,w_j=j/(j+1) gives norm-attaining S but all n>=2 products <1 with supremum 1; a second constructed sequence with initial weights 0.9 and later small odd weights yields S not in beta but S^2 in beta. Hyponormality is monotonicity of positive weights, and attaining supremum means an eventual constant tail. Exact finite arithmetic independently verified both examples; no finite shift truncation is used for the all-reducing-subspace theorem.

## originality

PASS

Su–Zhang 2026 study stability under finite-rank and compact perturbations; Golla–Osaka–Sequeira 2026 study quasinormal/hyponormal beta-class structure. Their available primary abstracts do not assert a full arbitrary-exponent residue-maxima criterion or both opposite power membership transitions. Full text arXiv and alternative OA failed; authorized Oxford access reported VPN disconnected, so these are named material priority risks rather than automatic originality failure.

## value

PASS

Power stability is a natural structural question for beta(H); a complete if-and-only-if arithmetic criterion, two opposite failure modes, and a hyponormal sharp stability boundary answer more than finite examples or a routine norm maximum calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
