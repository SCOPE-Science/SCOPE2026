---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

On Gr(3,9), E=(Sym² U*)⊕² has rank 12, is globally generated, and its sections induced by pairs of ambient forms generate the fibers. A general section is transverse; the nonzero degree calculation also proves nonemptiness. Its zero locus has dimension 6 and class c12(E), with tangent K-class [TG]−[E]. In ordinary K-theory [TG]=9[U*]−[U*⊗U], giving c1(TG)=9H, c1(E)=8H, and adjunction −K_F=H as a divisor class. Independently of torus localization, used roots x,y,z of U*, the ordinary total Chern series product ∏(1+x_i t)^9 divided by ∏(1+(x_i−x_j)t)∏_{i≤j}(1+(x_i+x_j)t)^2, and integer polynomial arithmetic through t^6. For every partition of six, multiplied the resulting monomial by ∏_{i≤j}(x_i+x_j)^2 and (x−y)(x−z)(y−z), then extracted [x^8 y^7 z^6]. All eleven values in source order are 3904, 3072, 1664, 896, 384, 256, 2880, 1728, 5248, 1792, 1088. The Grassmannian coefficient functional picks the rectangular Schur coefficient. This computation requires no smooth special example or finite-sample extrapolation. Top Chern integration gives the topological Euler characteristic.

## originality

PASS

Credit the exact Euler value 256 to prior cohomology, and the anticanonical identification and Grassmannian integration machinery to standard methods. The result assessed positively is the complete table, in particular the explicit mixed tangent-Chern pairings. The best inspected same-variety results compute Hodge/cohomological invariants, not that full table; other exact tables apply to different parameter spaces. The precise primary reference for the even ambient cohomology is Chen–Vilonen–Xue arXiv:1510.05986 rather than arXiv:1602.03052, which treats odd ambient dimension. Belmans et al. already provide the even-ambient refinement cited in the frozen record.

## value

PASS

The Fano parameter space of planes is a natural sixfold and the chosen invariants are the full top Chern-number list in its intrinsic anticanonical polarization, not a selective sample of integers. The table allows evaluation of degree-six characteristic polynomials, for example in Riemann–Roch or comparisons with other sixfolds, without repeating the ambient computation. This value rests on the explicit mixed pairings beyond the known Euler entry, not on novelty of the characteristic-class method or on the degree alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
