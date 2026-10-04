---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The theorem is analytic. The critical steps are:

1. Translation places the four-point support inside its difference span \(H\), and the restriction map on characters has constant fiber size \(2^{d-r}\). Thus ambient Fourier-support size is exactly that factor times the local support size.
2. If \(r=2\), the support is the full affine two-plane. The local Walsh matrix is invertible, and finite-hyperplane avoidance realizes every nonempty local Fourier support.
3. If \(r=3\), normalization gives \(\{0,e_1,e_2,e_3\}\) and local Fourier values \(L(\varepsilon)=a+b\varepsilon_1+c\varepsilon_2+d\varepsilon_3\). Adjacent zero vertices would force one of \(b,c,d\) to vanish; antipodal zero vertices would force \(a=0\); four remaining pairwise distance-two zeros form a parity tetrahedron and their summed equations also force \(a=0\). Hence there are at most three zeros.
4. Explicit coefficient quadruples realize zero counts \(0,1,2,3\), and cube symmetries realize every allowed exact pattern.

`artifacts/verify.py` uses exact rational arithmetic to exhaust all \(256\) candidate zero subsets of the cube. It confirms counts \(1,8,12,8\) for zero-set sizes \(0,1,2,3\), confirms that the size-two patterns are exactly distance-two pairs and the size-three patterns are exactly parity-tetrahedron triples, verifies all affine-plane Fourier-support subsets, checks the two affine support types in dimensions \(3\) and \(4\), and prints `VERIFY_OK`.

Replay command:

`python3 artifacts/verify.py`

The finite local enumeration is exact and complete, but the all-dimensional statement still uses the analytic character-restriction argument above rather than extrapolation from finite data.
