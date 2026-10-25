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
# Reproduction and boundaries

Execute `python3 check_g2.py` using Python 3, SymPy and NumPy. The script constructs the exact seven- and fourteen-dimensional fundamental characters as Laurent polynomials, constructs the Weyl density over the full six positive-root pairs, and calculates all mixed moments of total degree two, four, and six by integer coefficient convolution and division by the Weyl order 12. It also verifies exact symbolic derivatives of both sharp-ratio polynomials, verifies one positive-root sign change per derivative polynomial, and checks exact rational intervals for their unique positive roots.

The additional 48-by-48 torus-grid calculation checks the same moments numerically. For total moment degree at most six, every Laurent exponent coordinate of the weighted integrand has absolute value less than 24; thus discrete averaging over the grid would be exact in infinite precision. Floating-error tolerance is below \(10^{-7}\) in the numerical implementation; this is an auxiliary cross-check, not proof by finite sampling.

The proof of universality is the analytic common-phase reduction and Descartes-based global optimization in `RESULT.md`; the finite checker verifies its explicit coefficient inputs. The six-moment theorem says nothing about higher-weight representations, other complex dimensions, or unclaimed exponents. No external independent scientific audit has been performed.
