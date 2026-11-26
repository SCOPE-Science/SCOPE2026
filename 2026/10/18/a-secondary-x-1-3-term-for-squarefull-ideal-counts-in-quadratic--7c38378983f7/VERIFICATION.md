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

For a fixed quadratic K, the all-ideal norm coefficients are 1*chi_D. Splitting the corresponding pair sum at sqrt(y), bounded partial sums of chi_D give O_K(sqrt(y)) on the large-character-index portion and on the tail replacing the partial L(1,chi_D); flooring on the remaining part has the same error. This verifies the stated all-ideal estimate for real as well as imaginary quadratic K. The squarefree count follows by ideal Möbius inversion: the omitted N(J)^-2 tail is O_K(y^-1/2) and the accumulated errors are bounded by sqrt(y) times a harmonic norm sum. Abel summation of the all-ideal main term plus residual gives the claimed constant at sigma=2/3, since the integral of the residual continues zeta_K(s)-rho_K s/(s-1) into Re(s)>1/2; the analogous squarefree tail calculation gives 2 kappa_K Y^-1/2. Splitting exponents at each prime ideal by parity makes I=A²B³ unique with B squarefree and no coprimality condition. For T=x^1/5 all pairs lie in the union of the two strip counts, with a full overlap rectangle. The leading terms of size x^2/5 have coefficients -2,+3,-1 times rho_K*kappa_K and cancel. The remaining error sizes are x^1/2 T^-1 log(2T), x^1/4 T^1/4, x^1/3 T^-1/6, x^1/6 T^2/3 log(2x), and T^3/2 log(2T), all O_K(x^3/10 log(2x)). The Gaussian coefficient sign follows from positive alternating beta and eta at 2/3 and the negative factor 1-2^(1-2/3) converting eta to zeta. The unit ideal is included, real noninteger cutoffs use weak inequalities, and no claim of nonvanishing for general K is needed. The frozen checker was inspected, not executed; its finite Gaussian counts do not prove the asymptotic.

## originality

PASS

The leading coefficient is already in Horikx–Pieropan's general m-full ideal theorem. The distinct supported claim resolves the secondary contribution at exactly the scale of that theorem's quadratic remainder, with an explicit smaller error. No broader prior result resolving that coefficient was identified in the sources checked.

## value

PASS

The previous leading estimate leaves an entire natural secondary scale unresolved. The explicit second term and power-saving remainder distinguish a real arithmetic effect, including a definite negative secondary correction for the Gaussian field, rather than just shortening a remainder at an arbitrary exponent. The proof explains the cancellation that makes this second term measurable, across both real and imaginary quadratic fields.

The dated certificate retains the supplied scientific assessment, sources and limitations.
