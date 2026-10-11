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

# Reproduction and scientific limits

Execute `python3 verify.py` using a standard Python 3 installation. This is a standalone artifact without external dependencies. The verifier forms the exact eight-by-eight signed matching transfer over the integers and evaluates its two boundary vectors for half-turns. It checks the two rational generating functions through coefficients thirteen and the order-eight Cayley--Hamilton argument, independently enumerates compatible half-turn edge orbits for every width \(2\le n\le17\), and checks the displayed width-seventeen full-quotient Euler characteristic. Expected output begins with `VERIFY_OK 16` and reports the quotient value \(-51\).

The symbolic argument for all widths is: if \(s_m=e_0^\mathsf T T^m u\), then the coefficient of \(z^{m+6}\) in \(D(z)\sum_{j\ge0}s_jz^j\) equals \(e_0^\mathsf T T^m p(T)u\). Checking this for \(m=0,\ldots,7\) gives eight zero terms of a scalar sequence satisfying the characteristic recurrence of the eight-dimensional matrix \(T\); Cayley--Hamilton then forces all later terms to vanish. Initial coefficients supply the exact numerators, without extrapolating from finite grids. Independent orbit enumeration checks folding and orientation signs only in its finite range.

The topological quotient calculation uses the standard rational average of equivariant Lefschetz numbers for a finite simplicial group action, after equivariant barycentric subdivision. This proves Euler characteristics, not individual Betti groups or quotient homotopy types. The computation does not independently establish the absence of all earlier mathematical equivalents, nor is an independent audit claimed.
