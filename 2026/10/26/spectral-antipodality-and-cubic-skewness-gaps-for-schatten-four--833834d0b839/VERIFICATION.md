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

PASS: For A=XY,B=YX, cyclic trace equality tr(A^3)=tr(B^3) and A=(Q+T)/2,B=(Q-T)/2 yield tr T^3=-3 tr Q^2T; S4 Holder makes the products Hilbert-Schmidt and cubic traces legitimate. HS parallelogram and trace Holder give 4||X||_4²||Y||_4² >= ||T||_2²+||Q||_2² >= ||T||_2²+|tr T^3|/(3||T||op). Every finite trace-zero normal T has a same-size commutator: Fourier-conjugate to a zero-diagonal matrix then solve [D,Z]. Balanced factors prove compact attainment. Equality forces Q=0; Sylvester AB/BA spectral identity gives eigenvalue pairing lambda↔-lambda. For paired normal T a self-adjoint unitary J anticommuting with its polar phase and commuting with |T| gives X=J|T|^1/2,Y=(1/2)JU|T|^1/2, attaining ||T||_2/2. Independent exact rational-matrix identities checked 23 cases including paired examples and skewed cubic obstruction. No exact cost asserted for nonsymmetric target.

## originality

PASS

PASS, best of knowledge: directly read the closely related public rank-free normal commutator theorem. Its assumption 1/p+1/q<1/2 excludes the critical S4-S4 case (p=q=4), and it gives only two-sided comparison constants, not a same-size equality criterion. General Liu compact-factor existence and Liu-Yang target exponents >2 do not prove the critical spectral criterion. Classic trace-ideal equalities or older matrix commutator papers could contain equivalent statements; residual priority risk.

## value

PASS

PASS: The product of two S4 costs for a prescribed normal trace-zero commutator is a canonical quantitative operator-ideal invariant. The theorem identifies all exact lower-bound saturation spectra and gives a strictly improved lower bound from cubic spectral asymmetry, supplying a clear geometric equality obstruction unavailable from qualitative existence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
