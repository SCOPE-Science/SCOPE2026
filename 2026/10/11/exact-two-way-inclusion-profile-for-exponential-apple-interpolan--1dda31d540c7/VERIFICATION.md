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

# Verification of the two-way inclusion profile

The proof of the infinite real-parameter theorem is analytic. Its critical checkpoints are: (i) the strictly positive real part of \(h_q'\); (ii) the strict imaginary-strip bound on \(h_q\), giving injectivity of the exponential and positivity of the generator; (iii) the Möbius lower bound on \(\operatorname{Re}(1/(1+tz))\); (iv) the Rouché disk-containment argument and the real supporting boundary point; and (v) the positive-coefficient exact maximum and canonical extremizer outside the critical radius.

The reproducibility program `verify_radius.py` uses only the Python standard library. Invoke `python verify_radius.py` to recompute the high-precision roots for three rational choices of \(q\), check \(R_q-q\log(1-R_q)=1\), and perform a noncertifying diagnostic mesh check of \(|\operatorname{Im}h_q|<3/2\). The program must not be interpreted as proving the continuous angular maximum or the quantifiers over all \(q\) and all analytic functions.

At \(q=1/2\), the exact answer is \(1-W(2)/2\), approximately \(0.5736972489931372543\); the inradius is \(1+(\log2)/2\), approximately \(1.3465735902799726547\). No external or independent validation is asserted.
