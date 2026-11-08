---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

The restriction kernel U_ell(<x,y>) is the SU(2) Sym^ell character evaluated at xy^{-1}. The 600-cell vertex set is the 120-element binary icosahedral group, so character orthogonality diagonalizes this central convolution in each irreducible regular isotypic summand, yielding eigenvalues 120*m_{ell,i}/d_i with multiplicities d_i² for the nine affine E8 McKay dimensions d=(1,2,3,4,5,6,4,2,3). Clebsch–Gordan yields m_{ell+1}=A m_ell-m_{ell-1}; I independently recomputed 241 exact integer vectors, checked sum d_i m_ell,i=ell+1 and representation parity. Noncentral group element orders divide 60, while central ±I contribute ±60 to the character difference, proving the exact K_(ell+60)=K_ell+60(I+(-1)^ell J). Vanishing of character at all noncentral orders 4,6,10 forces 30|(ell+1), and is sufficient, proving exact tightness iff ell=29 mod 30. A degree-12 invariant and injective multiplication give m_{ell+12,i}>=m_{ell,i}; six odd base degrees 29..39 and six even 60..70 establish eventual rank 60, with exact recurrence ranks 27=56 and 58=59 proving sharp thresholds. Tests include rank13=60, rank15=52. Numerical 120x120 checker was read as claimed corroboration, not substituted for character proof.

## originality

PASS

Character orthogonality, binary icosahedral realization, and the affine E8 McKay graph are classical; the reported new result is the combined full sampling eigenvalue law, exact +60 shift/tightness classification and sharp eventual interpolation thresholds. Searches did not locate a dominating published theorem; best-of-knowledge PASS remains qualified by specialized icosahedral harmonic tables not fully inspected.

## value

PASS

Provides a full exact-degree sampling spectrum, exceptional exact-tight degrees and sharp eventual surjectivity thresholds on a canonical highly symmetric 4-polytope. Antipodal parity imposes a natural 60-dimensional target and the discrete 60-step shift gives concrete harmonic-interpolation and conditioning information. This is more than a numerical rank table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
