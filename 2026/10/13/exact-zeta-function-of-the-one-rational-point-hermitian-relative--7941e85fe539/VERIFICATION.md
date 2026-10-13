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

# Reproducibility and scope of verification

Run `python3 check_zeta.py` with a standard Python 3 interpreter. The script uses only its standard library. It exhaustively counts normalized projective points for the one-point Hermitian-relative model in the four finite fields \(\mathbb F_4\), \(\mathbb F_{16}\), \(\mathbb F_9\), and \(\mathbb F_{81}\), constructing a parameter \(\eta\in\mathbb F_{s^2}\setminus\mathbb F_s\) for each. The output confirms respectively \(1,9,1,109\) points. It also checks that the representation multiplicities sum to \(s(s-1)\) and produce the asserted traces for six prime powers and finitely many extension degrees.

The infinite theorem requires the paper proof, not these tests. The essential exact identities, verified algebraically in the proof, are \(c^{s^2}-c=\eta-\eta^s\), the order-\(p\) translation \(Z\mapsto Z+\delta Y\), conjugation by \((X,Y,Z)\mapsto(X,aY,a^{-s}Z)\), Hermitian maximality, and Fourier inversion of the constant nontrivial-character trace \(-s\). The proof applies to every prime power and every extension degree. Tests of finitely many fields or coefficients cannot establish universal originality or correctness.

The source comparison covers the one-point model in the 2026 WCC preprint and the general zeta argument in arXiv:2402.14192; a separate 2026 projective-equivalence classification chapter was not available in full. An independent audit has not been performed.
