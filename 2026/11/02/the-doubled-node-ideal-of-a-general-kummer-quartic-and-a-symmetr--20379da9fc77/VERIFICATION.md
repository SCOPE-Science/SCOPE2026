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

# Reproducible mathematical checks

Execute \(\texttt{python3 kummer_node_square_verifier.py}\) with Python 3, SymPy and NumPy. It checks all sixteen explicit rational nodes and their nondegenerate Hessians, a degree-sixteen reduced affine gradient scheme and no critical points at infinity. The lexicographic initial monomials of that affine gradient scheme are \(X,Y^4,Y^2Z^2,Z^6\), giving length \(16\).

It then constructs evaluation and three-direction first-jet matrices, four cubic gradients and three extra quartic node generators. Exact rational kernels and rank calculations, together with modular ranks at \(1009\) and \(1013\), yield the following verified sequence: first-jet ranks \((20,34,52,64,64,64)\) in degrees \(3\) through \(8\); ranks \(20\) and \(56\) for the candidate symbolic-square generators in degrees \(6,7\); rank \(52\) for the ordinary square in degree \(7\), and rank \(101\) for the ordinary square in degree \(8\).

The proof in RESULT.md explains why these exact finite-dimensional linear-algebra certificates imply an all-degree ideal equality, and separately why openness extends the rational witness to the general characteristic-zero Kummer quartic. A check of finitely many primes alone does not establish the characteristic-zero statement; instead their ranks provide lower bounds for explicit rational matrices, while ideal containment gives complementary upper bounds.

The included \(\texttt{verification_output.txt}\) records the reproducible stdout ending with \(\texttt{VERIFY_OK}\). No independent audit has been conducted. Historical novelty beyond inspected sources is not certified.
