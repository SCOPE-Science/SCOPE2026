---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

For normalized Bergman e_n=sqrt(n+1)z^n and monomial-normalized W_r, B_a sends e_n to sqrt((n+1)/(m+1))e_m if m=(n+a)/r is an integer. Its two compositions telescope to basis outputs m_i=(n+d_i)/r^2, d_1=b+ra and d_2=a+rb, with signs +/-. The square of every nonzero weight is r^2-(d_i+r^2-1)/(m_i+1)<r^2 and tends to r^2. Since d_1-d_2=(r-1)(a-b) and gcd(r-1,r^2)=1, for r^2 not dividing a-b the two input residue supports are disjoint and CC* is diagonal with all diagonal entries <2r^2 approaching 2r^2, so ordinary/essential norms are r sqrt2, essential spectrum of CC* singleton {2r^2}, and no maximizer exists. Otherwise CC* is a compact perturbation of r^2(2I-S^q-S*^q), q=abs(d_1-d_2)/r^2>=1, giving [0,4r^2] and sharp norm 2r. Strict weight inequalities on each composition exclude norm attainment. Independently constructed six sparse finite-section commutators (size 2200), confirming singular norms approaching predicted sharp 2.82843/4/4.24264/6/5.65685/8 from below. Finite truncations do not establish the Calkin spectrum.

## originality

PASS

Best-of-knowledge original sharp quantitative two-level norm/positive-essential-spectrum classification of commutators for distinct analytic monomials under the actual Bergman downsampling normalization. Cui–Li–Lu 2026 Theorem 2.5 and Corollary 2.6 prove commutativity and finite-rank rigidity but do not compute sharp Calkin spectra. Liu–Lu 2013 gives product and commutation conditions. The directly relevant Lu–Liu–Yang 2010 primary text was inaccessible after arXiv/open-access search and authorized institutional retrieval; its abstract reports essentially qualitative results. This remains a material priority risk, not an automatic originality failure.

## value

PASS

The class is a canonical test family for slant Toeplitz operator theory and its Calkin algebra. The arithmetic residue threshold r^2|(a-b) separates asymptotically scalar and discrete-Laplacian positive squares, giving distinct exact norms and essential spectral shapes; this is structurally more informative than merely noncommutativity or a finite numerical example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
