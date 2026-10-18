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

# Reproducibility of the square-zero count checks

Run `python3 verify.py` with Python 3 using only the standard library. The code constructs the multiplication coefficient of each alternating word of lengths \(2\) through \(m\) directly from concatenation, identifies the two longest alternating words only at length \(m\), and checks \(x^2=0\). It enumerates all \(2(m-1)\) coefficients below longest degree, multiplying the resulting count by \(q\) for the independently free longest-word coefficient. The finite-field arithmetic includes prime fields \(\mathbb F_2\), \(\mathbb F_3\), \(\mathbb F_5\), together with \(\mathbb F_4=\mathbb F_2[h]/(h^2+h+1)\) and \(\mathbb F_9=\mathbb F_3[h]/(h^2+1)\). It computes the predicted expression separately from the word equations.

The saved checker was executed successfully: `VERIFY_OK` after fifteen exhaustive parameter configurations. Examples: \((m,q)=(3,2):16\), \((4,3):135\), \((4,4):1792\), \((5,3):567\), \((6,3):2187\), \((8,2):1280\), \((9,2):1536\). The checks establish exactly the tested finite cases, not arbitrary-field irreducibility, component counts, or all lengths. Those statements are proved by symbolic triangular elimination and the final degeneration in `RESULT.md`. No independent audit has been performed.
