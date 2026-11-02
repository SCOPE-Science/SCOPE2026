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

Reconstructed from actual RESULT.md the quantifiers N>=3, cyclic group Z/N, orientation T f(x)=f(x+1), Laplacian 2I-T-T^-1, zero-mean spectral inverse, normalized convolution, and sign conventions for H_(2N) including the vanishing 0/Nyquist modes. On nonzero character k, L eigenvalue 4 sin²(pi k/N), (T-I) eigenvalue 2i e^(pi i k/N) sin(pi k/N), hence R multiplier i e^(pi i k/N). Its inverse DFT is i Σ_{k=1}^{N-1} e^(2pi i k(r+1/2)/N)=-cot(pi(r+1/2)/N) using q^N=-1 and the finite geometric sum. Squaring yields -exp(2pi i k/N), zero at k=0, proving R²=-T(I-P0). For H_(2N), direct Fourier sine pairing gives zero even-offset kernel and 2cot(pi s/(2N)) on odd offsets. Its even-to-odd and odd-to-even restrictions, with the factor N/(2N)=1/2 from normalized convolutions, give exactly -R and -S_-R. Circulant convolution ℓ1/ℓ∞ norms equal the normalized absolute row sum, attained by a point mass/sign pattern; the same parity blocks imply ||H_(2N)||=||R_N|| and the displayed half-grid cotangent sum. Singular-term subtraction g(x)=cot(pi x)-1/(pi x), harmonic-number asymptotics and midpoint Euler–Maclaurin produce the common logarithmic constant and the even pi/18 versus odd -7pi/36 coefficients, with paritywise O(N^-4); for even N the N^-2 coefficient follows explicitly by combining harmonic +1/(3pi) and smooth -1/(3pi)+pi/18 contributions. Independently evaluated inverse kernels and BOTH parity blocks for N=3,4,5,6,9,12,17, matching to 1e-13, and high-precision C_N for N=100,101,1000,1001 with N² residual approaching predicted coefficients. These finite checks corroborate, never replace, the all-N algebra and asymptotic analysis. No claim about sharp interior ℓp operator norms or higher-dimensional cycles.

## originality

PASS

Qualified best-of-knowledge: the exact cyclic-Hilbert endpoint norm and the full parity-residue N^-2 asymptotics are ALREADY determined for H_(2N) by a separate published exact-Hilbert record; the 1969 finite DFT Hilbert paper already gives its odd cotangent impulse-response kernel. The surviving distinct content is a concrete identification of the forward graph-cycle difference-Laplacian Riesz transform as the even-to-odd half of the doubled cyclic Hilbert operator, its complementary shifted parity block, and the algebraic R_N^2=-T(I-P0) law. These operator-level statements are not stated in the inspected general cyclic-Riesz Lp bounds nor in the full exact-Hilbert source; their proof uses explicit Fourier phase comparison and parity-decimation, not a theorem claiming a universal block identification. Their algebra is short and based on classical symbols, so the historical priority judgment is necessarily qualified and does NOT credit the norm/asymptotic as independently new.

## value

PASS

PASS because the object is canonical: the difference–Laplacian Riesz transform of a finite graph cycle and the finite DFT Hilbert transform are separately important natural singular operators. The exact even/odd block equivalence (with a nontrivial shift/sign convention), and the square-root-of-translated-negative-identity algebra give a compact structural dictionary between graph spectral calculus and cyclic Fourier singular filters. This structural relation could reasonably be reused for transfer of kernel and spectral calculations; it is motivated prior to computing any finite constant. The sharp endpoint numeric values and paritywise asymptotics are NOT independently valuable discoveries here because the separate exact-Hilbert paper already determines them, but they are useful explicit corollaries illustrating the operator bridge. The argument is elementary rather than a deep new Lp theorem; no generalization to other graphs or interior p is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
