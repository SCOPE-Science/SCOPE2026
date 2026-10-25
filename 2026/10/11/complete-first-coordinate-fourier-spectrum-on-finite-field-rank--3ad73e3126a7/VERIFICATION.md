---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

For every prime power q and m,n>=2, independently counted the rank-one shell via uv^T with q-1 factorizations to recover Delsarte’s formula S_r=(q^(m+n-r)-q^m-q^n+1)/(q-1). Frequency differences from the zero-plus-one-coordinate band have rank 0,1,2, giving D=qt I+t(R⊗J_z)+c2 J. Diagonalization of the rook matrix yields label-contrast qt [mn(q-2)], row (1+zn)t [m-1], column (1+zm)t [n-1], and interaction t [(m-1)(n-1)]. Constant and zero-frequency modes form the exact 2×2 block [[1,c1√T],[c1√T,B]] with roots λ±, so dimensions total 1+mn(q−1). Its determinant Var_X(T−q support(u)support(v))/T>0, since support products vary when m,n≥2; all eigenvalues positive. Parseval and Rayleigh give sharp energy concentration and squared condition number; exact trace/determinant expansion at fixed q and m=n=d gives λ+~(q−1)d²/q², λ−~2(q−1)/d, κ²~d³/(2q²). Independent direct character enumeration of 8 (q,m,n) cases including GF(4) matched full eigenspectra (maximum error 2.22e−15); finite tests corroborate and do not establish the unrestricted proof.

## originality

PASS

Best-of-knowledge PASS for the complete selected rank-one-shell coordinate Fourier restriction spectrum. Delsarte 1978 A7 supplies exactly the known rank-one Fourier character kernel and is fully credited. The additional sparse-coordinate rook-block diagonalization, sharp eigenvalue/equality spaces, injectivity, norm concentration and cubic conditioning are not stated in the complete primary Delsarte paper or other inspected mathematical sources. Four fresh semantic mathematical-record searches identified only the same claim for exact matching (excluded), and related results on different matrix varieties; unpublished, unindexed or implicit specializations remain risks.

## value

PASS

The rank-one (Segre) variety is a canonical finite-field matrix variety and the complete constant-plus-one-entry additive Fourier band is a natural first-order harmonic model. The theorem gives a genuine full exact spectral classification, every equality subspace, uniform injectivity and the sharp concentration operator norm, while quantifying significant cubic squared-conditioning deterioration. The Fourier kernel alone is known; a coordinate-specific compressed Gram spectrum and its stability were not a textbook rank-character lookup or unmotivated arbitrary slice. The precise spectral data may be used in finite-field Fourier interpolation, structured sensing or stability analysis without claiming optimal frequency design or higher-degree results.

The dated certificate retains the supplied scientific assessment, sources and limitations.
