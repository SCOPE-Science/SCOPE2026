---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Bordering the 3×3 Hankel B gives det H=(det B)a6−vᵀadj(B)v. Invertible B contributes q^6−q^5 to every t. For det B=0 and top-left δ=a0a2−a1²≠0, adj(B)=δnnᵀ yields a squared linear form; direct summation of ρ2(−t/δ) using m_q(δ)=q²+q(ρ2(−δ)−1) gives q^4(q−1)+q³(q−1)(ρ2(t)−1). In the remaining rank-2 δ=0 cases, A=a0≠0 gives det H=−Ah³ and q³(q−1) solutions for t≠0, whereas a0=0,a3≠0 gives det H=a3^4 and q³ρ4(t). Rank≤1 gives the zero-fiber remainder q⁴. All terms sum to stated formula including t=0, no forbidden division at zero. Independent direct permutation-determinant enumeration over q=2,3,5 agrees with every fiber (q=2:64,64; q=3:729,810,648; q=5:15625,16500,15000,15000,16000); finite counts corroborate but do not prove all prime powers.

## originality

PASS

Classical Daykin and García-Armas–Ghorpade–Ram work enumerates Hankel ranks/zero determinant; Dwivedi–Grinberg prescribes initial coefficients and Hankel rank. The result refines these by nonzero determinant values and quadratic/fourth-power residue types, which cannot be reconstructed from rank counts.

## value

PASS

A complete exact polynomial-fiber distribution for a canonical seven-parameter determinantal family over all finite fields, including arithmetic residue splitting, is a naturally reusable invariant distinct from the existing singularity census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
