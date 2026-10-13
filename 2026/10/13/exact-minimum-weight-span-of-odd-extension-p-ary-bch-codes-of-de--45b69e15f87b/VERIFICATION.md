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
# Verification

The symbolic verification checks the following chain.

1. A cyclic shift and scalar normalize every weight-three word to \(1+a x^i+b x^j\).
2. Eliminating one locator from the two BCH equations gives a polynomial of degree at most two over \(\mathbb F_p\) for the other locator. Odd \(m\) forces that locator into \(\mathbb F_p\); symmetry gives the same conclusion for both.
3. Therefore \(h\mid i,j\), and the two BCH equations become zeros at \(\beta\) and \(\beta^2\) of a polynomial in \(x^h\).
4. Hence every weight-three word is divisible by \((x^h-\beta)(x^h-\beta^2)\).
5. That divisor itself has exactly three nonzero coefficients and satisfies both BCH checks, so its shifts are weight-three words and span the entire cyclic ideal.
6. Its degree is \(2h\), giving dimension \(n-2h\). Since \(\dim C=n-2m\), the component exponent is \(2(h-m)\).

The bundled `verify.py` additionally performs a direct computation for \(p=5,m=3\) in \(\mathbb F_{125}\). It enumerates all normalized weight-three solutions of the two parity checks, confirms the support differences are multiples of \(31\), verifies the explicit generator, and row-reduces all cyclic shifts. Expected terminal output includes:

`cyclic_shift_rank 62`

`C_dimension 118 component_exponent 56`

`VERIFY_OK`

This finite calculation is a reproducibility anchor only; it is not used to extrapolate the all-parameter theorem.
