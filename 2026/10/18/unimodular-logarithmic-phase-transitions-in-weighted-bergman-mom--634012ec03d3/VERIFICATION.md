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

Angular orthogonality diagonalizes the stated bounded radial symbol, and the weighted squared monomial norms are a B(n+1,a), giving the normalized beta integral. At x=n(1−t), replacing the beta density by the gamma density on [0,sqrt(n)] has absolute error O_a(n^−1) plus an exponentially small tail; this is uniform for a phase of modulus one on the real interval. Dominated convergence after removing exp(iL^τ) gives the subcritical result. At τ=1 the exact beta quotient has gamma ratio Γ(a−i)Γ(n+a+1)/(Γ(a)Γ(n+a+1−i)); the limiting radius is positive and strictly less than one by strict triangle inequality for the gamma law. In both cases the leading angle tends to infinity with increments tending to zero, so every point of the relevant circle occurs as a cluster point. For 1<τ<2 a real-axis pointwise linearization would not justify an exponentially small relative asymptotic. The clockwise rotation θ=arctan(κ/a) is valid up to R=exp(L/2): L−log x stays in the right half-plane on the sector, its τ-power has nonnegative imaginary part, and the outer arc is polynomial in R times exp(−R cos θ), negligible even relative to the gamma factor. After scaling x=κu exp(−iθ) and removing exp(−κθ), the small-u tail up to κ^−M is o(κ^−1/2): at |x|<1, Im(A+iθ)^τ≥τA^(τ−1)θ≥κθ for A=L−log|x|, using monotonicity of Re(A+iv)^(τ−1) in v≥0. Above u=κ² the exponential amplitude dominates even exp(κθ). In the middle the Taylor remainder is O(L^(τ−2)log² κ)=o(1); its u derivative is O(L^(τ−2)(1+|log(κu)|)/u), and its first two derivatives tend to zero near the saddle. Thus on the nonstationary left the derivative after division by the phase slope has an integrable O(u^(a−1)) bound, and on the right it has an exponential majorant. Integration by parts is O(κ^−1). The nondegenerate saddle u=1/sin θ gives the complex Gaussian factor, including exp(iπ/4); κ cot θ=a and κ(π/2−θ)→a cancel the remaining real amplitude factors exactly to leading order. Stirling at a−iκ supplies the same phase and modulus, and κ=o(L) makes the absolute beta error negligible relative to that modulus. The diagonal therefore vanishes at infinity without being summable to any positive power, and two-sided logarithmic bounds squeeze N_τ(s) without monotonicity of the diagonal. The proof is for fixed a>0 and fixed τ<2; no endpoint or parameter-uniform claim. The frozen verifier was inspected, not executed; its four rotated gamma-law tests are not independent checks of a relative all-parameter beta asymptotic.

## originality

PASS

The supported distinct contribution is the relative complex moving-frequency Mellin/Gamma comparison for the exact radial logarithmic chirp, for fixed 1<τ<2. Radial diagonalization, bounded radial compactness criteria and fixed-frequency beta/gamma moments are background. The examined primary and indexed results do not state or imply the required comparison to exponential relative accuracy for this symbol; no exhaustive priority claim is made.

## value

PASS

This natural fixed-modulus family separates boundary oscillation from decay of the symbol itself and has a sharp compactness transition. In the compact regime the complex formula determines not just convergence but the cancellation scale, phase, and logarithmic spectral-counting constant. Compactness outside every finite Schatten class is a substantive contrast with faster boundary chirps. The relative estimate is needed for the quantitative spectral description, not just a routine application of a compactness criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
