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

# Verification of the exact rank-one operator count

The included standalone `checker.py` needs Python 3 and NumPy. From the directory containing the file, execute `python checker.py` and compare stdout with `CHECK_OUTPUT.txt`. The last line must equal `ELLIPTIC_ROTA_BAXTER_RANK_ONE_OK`.

The checker constructs the multiplication from two bilinear polarizations rather than substituting the theorem's operator count into the identity. It uses all \(36\) ordered pairs of basis vectors to test weight-zero Rota–Baxter validity, including the central cases. Over \(\mathbb F_3\) with \(y^2=x^3+x\), it considers every ordered pair of nonzero six-coordinate vectors \((a,f)\), namely \((3^6-1)^2=529984\) presentations. Dividing by the scalar-rescaling multiplicity \(2\) yields exactly \(5792\) distinct solutions, split into \(2912\) central-image and \(2880\) noncentral-image solutions.

For eight configurations over \(\mathbb F_3,\mathbb F_5,\mathbb F_7,\mathbb F_{11}\), it directly counts projective intersections of the defining quadrics, compares them with independently evaluated Weierstrass point counts, and verifies Jacobian rank at every rational point. In each configuration, it uses \(400\) sampled nonzero presentations to compare the original identity and the structural criterion. It also computes the point count of \(y^2=x^3+x\) over the genuine degree-two extension \(\mathbb F_9=\mathbb F_3[t]/(t^2+1)\) using pair arithmetic; the count is \(16\), as predicted by the Frobenius recurrence.

The finite calculations do **not** verify smoothness over every algebraic extension, the universal Weierstrass realization, or the infinite family of finite-field formulas. Those are mathematical assertions proved in `RESULT.md`; the finite computations are consistency checks. Nothing in this package constitutes independent mathematical auditing.
