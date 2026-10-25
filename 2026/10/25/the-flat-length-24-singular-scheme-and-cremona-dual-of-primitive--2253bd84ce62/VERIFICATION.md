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

# Verification protocol and limits

Run `python3 verify.py` using Python 3 and no third-party libraries. A successful run prints `VERIFY_OK`.

The program performs exact arithmetic in \(\mathbf F_4=\mathbf F_2[t]/(t^2+t+1)\) and exhaustively tests the \(85\) points of \(\mathbf P^3(\mathbf F_4)\). For the four representative zero-coefficient patterns \(r=0,1,2,3\) with \(a=e=1\), it verifies every projective singular point, the exact gradient support, the predicted point counts \(12,10,8,6\), and the six edge-divisor support and multiplicity totals. It separately checks all distinct degree-\(12\) Cremona pullback monomial exponent vectors, the absence of coordinate divisibility, and the cubic involution identity on every nonzero four-tuple over \(\mathbf F_4\).

The universal theorem for algebraically closed coefficient fields does **not** follow from the finite-field enumeration. The proof is the characteristic-two differentiation, squarefree coordinate-edge ideal, monic degree-four edge equations, formal transverse splitting, normality, and Laurent-torus birational argument in `RESULT.md`. The program does not establish independent proof certification, general Picard lattices, or novelty in unsearched works.
