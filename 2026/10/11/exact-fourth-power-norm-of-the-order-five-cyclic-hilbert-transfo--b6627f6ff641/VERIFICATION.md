---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

Reconstructed normalized Fourier inversion and real-conjugate pairing on C5. Independently computed the five Fourier coefficients of f² by cyclic convolution and confirmed ∥f∥4^4=6r^4+24r²s²+6s^4+8r³s cos(3α+β)+8rs³ cos(α−3β), with the latter rs³ term changing sign for Hf. The phase map (α,β)↦(3α+β,α−3β) has determinant −10 and is surjective on the two-torus, so both cosine variables can attain −1 independently; direct quotient partial derivatives then prove the global phase maximum. For t=s/r, exact symbolic differentiation independently yields R′(t)=−8t²(3t⁴−12t²+8t−9)/D(t)²; g is strictly negative on (0,1] and strictly convex on [1,∞), with g(1)<0 and g→∞, giving one positive stationary root t*=1.853258098625306… and global maximum X*=2.089689004569992… (∥H∥4≈1.202320949439024). Independently confirmed exact polynomial elimination 3185X⁴−17948X³+42750X²−47500X+15625, factor divisible by g(t)², and all ten phase solutions modulo 2π; the ten are one orbit under sign and five translations, so all real extremizers as stated. Cases r=0 or s=0 give quotient 1, below X*. The special C3 zero-mean fourth-moment identity also follows algebraically. This is an analytic proof, not an extrapolation from finite tests.

## originality

PASS

Best-of-knowledge originality. Multiple semantic and exact-fingerprint searches of published Resultary findings, direct full-text comparisons of the closest cyclic Hilbert endpoint/parity and finite Fourier/L4 findings, and materially read original discrete Hilbert/finite-DFT sources found no prior claim that implies the exact real C5 L4→L4 norm and unique equality orbit. The finite-cyclic p=1,∞ theorem covers the same operator but a different exponent; the sharp infinite-lattice ℓp result is not a finite-C5 quotient; and the same-group co-singleton Λ(4) theorem optimizes another ratio. This remains bibliographic best-of-knowledge, not a novelty certificate.

## value

PASS

The real cyclic Hilbert sign-multiplier p4 operator norm is a natural finite version of a classical harmonic-analysis sharp-constant problem, not an arbitrary polynomial slice. The three-point zero-mean case is L4-isometric, making order five the first nontrivial odd cycle; the exact order-five algebraic constant and exhaustive extremizer orbit establish a sharp benchmark and a two-phase reduction potentially reusable for studying larger odd cycles, including the independently documented order-31 open problem. This is a worthwhile self-contained exact natural invariant without claiming general-N resolution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
