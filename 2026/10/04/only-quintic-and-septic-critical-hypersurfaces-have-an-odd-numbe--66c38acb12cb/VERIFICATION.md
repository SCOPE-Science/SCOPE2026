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
The exact checker reconstructs the coefficient
\[
[x^n y^{n-1}z^{n-2}](x-y)(x-z)(y-z)\prod_{i+j+k=d}(ix+jy+kz)
\]
with integer arithmetic for several critical degrees. It reproduces the displayed quintic and septic counts and verifies sample even cases without using the parity theorem as an input.

A separate exact path checks the reduced hook-number formula
\[
K_q=\frac{2(3q)!}{q!(q+1)!(q+2)!}
\]
and its \(2\)-adic valuation. It verifies the predicted parity for every admissible odd degree through \(d=299\) and the valuation classification for \(1\le q\le5000\).

Those bounded replays are regression evidence. The infinite result is proved in RESULT.md by the symbolic reduction of the full top-Chern product modulo \(2\), followed by a uniform floor-sum argument showing \(\nu_2(K_q)>0\) for all \(q\ge3\).

The real consequence uses only conjugation on a zero-dimensional scheme over \(\mathbb R\): non-real closed points contribute even total degree, so odd length forces a real point.
