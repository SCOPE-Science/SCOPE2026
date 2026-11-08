---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

For the uniform 8-digit ternary carpet, the Fourier digit mask is exactly M(x,y)=exp(-2 pi i(x+y))[(1+2cos2pi x)(1+2cos2pi y)-1]/8. Removing all common powers of 3 reduces each nonzero integer frequency to a primitive pair, with first mask modulus 1/8. Checked the two pointwise sharp bounds for subsequent masks: for one coordinate primitive, c_j=(3s(3^-j)-1)/8, for both primitive b_j=(s(3^-j)^2-1)/8; all equality congruences force ±axis-unit or ±diagonal-unit residues at every power of 3. At the first incompatible ternary digit, one-coordinate-primitive nonextremizers have a mask <=1/2, hence coefficient <=1/16. The explicit infinite-product bound B>515/7776>1/16 separates the second family from all others; c_j>b_j yields A>B. Independently evaluated mask and convergent products: A≈0.1007268724734242, B≈0.08075493227479424; (2,0) is below 1/16; (3,0) reproduces A. Cyclotomic reduction ζ→1 mod(3,ζ-1) sends each numerator to 8≡-1 mod3, ensuring nonzero factors, with summable tail guaranteeing a nonzero product. Thus all integer Fourier multipliers are nonzero, giving the sharp first and second L² convolution norm levels and injectivity; finite artifact checks alone do not establish the unbounded frequency assertion.

## originality

PASS

The 1986 Lakhtakia–Varadan–Varadan conference abstract discusses fractal diffraction and the Sierpiński carpet without an exact 8-digit lattice Fourier extremum classification. Barral–Mensi (2007) treats Gibbs measures and multifractal spectra; Murugan–Shimizu (2023/2025) uses the same canonical carpet measure for Sobolev/energy theory, not shown to imply these multiplier levels. Resultary results on discrete Fourier cubes/finite apertures concern distinct measures and invariants. The combination of exact top-two infinite lattice multiplier levels, equality classes, and all-mode nonvanishing was not found covered in directly read statements, but unavailable 2007 text/older diffraction can contain priority overlap.

## value

PASS

The first two integer Fourier magnitudes and precise extremizers are natural spectral invariants of the canonical singular uniform Sierpiński carpet measure. Their strict separation gives sharp mean-zero convolution contraction rates and explicit subspace filtration for powers, and nonvanishing proves a substantive injectivity fact. The infinite lattice optimization and digit-rigidity argument cannot be replaced by testing finitely many frequencies; this is a motivated harmonic-analytic computation, not a recomputation of a familiar table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
