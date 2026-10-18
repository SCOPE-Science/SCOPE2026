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

# Reproducibility and verification

The complete statement, normalization, assumptions, proof, and exact counting argument are in `RESULT.md`. Run `python checker.py` in the same folder using Python 3 with `sympy` and `mpmath` installed; no downloaded data or network connection is needed.

The checker conducts exact cyclotomic polynomial greatest-common-divisor tests for all 80 primitive root pairs at conductors \(2\cdot3^h\), \(1\le h\le4\). For eight isolated Fourier zeros with predicted orders \(2,4,6\), it tests the vanishing mask factors, nonvanishing of the next factors, convergence of the normalized local product, and phase winding zero on a small real circle, at 90-digit working precision. It also verifies the exact nested order-shell counting identities at radii \(20,100,300\) by direct integer enumeration. At radius \(300\), isolated zeros occur with order multiplicities \(27{,}948,3{,}088,348,40,4\) for orders \(2,4,6,8,10\).

**Analytic versus finite verification:** None of those finite checks proves the theorem for arbitrary frequency or order. The unrestricted statements rest on the cyclotomic separation lemma, analytic nonvanishing of the infinite-product tail, local Taylor expansion, and nested-lattice counting proved in `RESULT.md`. The software checks representative identities and the polynomial obstruction in small conductors. No independent audit has been performed.
