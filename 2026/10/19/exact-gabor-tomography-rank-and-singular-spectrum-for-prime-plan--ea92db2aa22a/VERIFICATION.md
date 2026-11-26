---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The normalized Weyl basis is W_(h,omega)/p; its output column is p^(-2) times A_g(h,omega) times the character psi(omega·a-b·h). Summing over p^4 output coordinates gives the claimed moduli with no extra factor of p. The conic has m points (split product fibers or nonsplit norm fibers). At nonzero h the intersection lies on h/2+h^perp. If Q(h)=0, h^perp is isotropic and there are no points; otherwise the perpendicular generator (d h_2,h_1) has norm -dQ(h), giving the stated character condition and one point exactly when Q(h)=4. Alternatively the involution (z,w) -> (-w,-z) pairs the ordered non-antipodal distinct differences while antipodes give m singletons; since intersections have size at most two this gives K=m(m-2)/2 and the exact rank. Cyclotomic irreducibility rules out cancellations when the size is 1, 2 or p±1. The nonzero relative displacement is a surjective frequency functional, giving p copies at each residue and the folded cosine multiplicities. For h=0 and nonzero omega, two completed Gauss squares give the multiplier chi(d) and argument -Q*(omega)/4 in the Kloosterman row, with m frequencies at each nonzero dual norm and (p-1)(1+chi(d)) nonzero isotropics. Rows add at coincidences. This is a statement about all matrices, not nonlinear phase retrieval. The checks/ scripts and outputs described at RESULT.md:90 are absent from the supplied package and were not replayed; the independent analytic reconstruction does not require them.

## originality

PASS

The supported distinct claim is the explicit complete spectrum, grouped by dual norm, for both form types at each prime, with the complementary nonsplit geometry. The split rank, nullity and ambiguity support are known and receive no separate novelty credit. A separate indexed diagonal-circle result has the same calibrated geometric bands and a frequency-indexed zero-shift list for d=-1, but does not give the dual-norm resolution or the other isometry type at a fixed prime. This assessment does not adjudicate publication priority.

## value

PASS

The full orbit and indicator conic are natural objects. Rank identifies which operator directions are lost, but not their surviving gains. The complete multiplicity law supplies those gains, distinguishing geometric bands from arithmetic frequency terms and allowing exact conditioning computations for a fixed prime without building a dense lift.

The dated certificate retains the supplied scientific assessment, sources and limitations.
