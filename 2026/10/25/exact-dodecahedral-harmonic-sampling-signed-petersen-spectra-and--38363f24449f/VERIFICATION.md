---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

Reconstructed probability-L² normalized degree-l addition formula giving G_l(x,y)=P_l(x·y), and antipodal pairing giving 10 forced zeros and active eigenvalues twice the representative matrix spectrum. Independently generated all 20 Q(sqrt5) dodecahedral points, confirmed 10 antipodal pairs and the three 10x10 identities A²=2I−A+J, B²=3I+C, B³=5B entrywise (300 identities), valency 3, and trace multiplicities A:3(1),1(5),−2(4); B:+sqrt5(3),−sqrt5(3),0(4). Thus parity branches hold for every l. A new independent exact-Fraction Legendre recurrence checked all 561 degree/branch values for 0<=l<=186: all nonnegative, zeros precisely l=0,1,2,3,4,5,8,14 with listed sectors, ranks 1,3,5,7,9,6,10,10,9,10,10,10,10,10,9 for l<=14 and 10 for 15<=l<=186; unique strictly-positive representative eigenvalue minimum 3094/1594323 at l=13 in a 3-dimensional odd sector. Analytically from the Laplace Legendre integral, |P_l(t)|<=sqrt(pi/(2l(1−t²))) for |t|<1, hence offdiagonal Gershgorin row sums <=sqrt(186/l) via exact rational pi and sqrt2 bounds; for all l>=187, 1−sqrt(186/l)>3094/1594323. The independent rational checks confirm (1−3094/1594323)²>186/187 and the <186 constant. This proves no later rank defect or smaller eigenvalue: global Gram minimum 6188/1594323, equality only l=13. Moore–Penrose bound applies only to y in range E_l, not unattainable parity data. No extrapolation from finite enumeration.

## originality

PASS

PASS with priority qualification. Exact equivalence was tested under signed Petersen/Seidel association schemes, spherical harmonic Gram/zonal kernels, icosahedral character tables, and interpolation condition numbers. Dai–Xu Theorems 2.6 and 3.3 establish the general reproducing kernel and generic fundamental systems, but not fixed 20-dodecahedron eigenvalues or all-degree minimum. Bannai–Okuda–Tagami explicitly precedes the icosahedral harmonic-index 8 and 14 cancellations; those mechanisms and base group representation theory are prior. Bates–Khalid–Kennedy handles multi-degree antipodal iso-latitude grids; Li–Xu handles trigonometric Fourier analysis on lattice dodecahedral domains, not spherical sampling at twenty vertices. Famoriji et al. discusses 20-vertex configurations numerically, without the three-sector exact-degree spectrum or global rational lower bound in inspected sections. Published Resultary geometric-dodecahedral/icosahedral records address distinct homology or spectral invariants. The closest historical risk is Cohan 1958, all-irreducible icosahedral harmonics through degree 14 (with trivial degree 15): full text inaccessible after arXiv/OA searches and authorized retrieval reported vpn_disconnected; no whole-document NOT_COVERING conclusion. No identified decisive prior implication covers the all-degree spectral law or unique 13th-degree optimum, so best-of-knowledge PASS with this material priority risk.

## value

PASS

The 20-vertex dodecahedron is a canonical, naturally motivated spherical sampling orbit. An all-degree parity-sector Gram decomposition reveals nonmonotone rank obstructions at l=5,8,14 and a sharp permanent full-compatible-rank threshold l=15, together with a globally optimal, degree-independent inverse stability factor sqrt(1594323/6188) uniquely controlled by l=13. These are exact nontrivial invariants for interpolation and representation-aware signal reconstruction, not arbitrary parameter slices, mere known first-moment harmonic design cancellation or routine numerics. Value remains self-contained without a broader polyhedral theorem. Risk: historical spectral tables may have covered pieces; no unconditional novelty certification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
