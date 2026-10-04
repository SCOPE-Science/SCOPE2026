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

The proof uses two exact identities. With \(c_n=1\) for even \(n\) and \(c_n=\cos(\pi/n)\) for odd \(n\), the dual remainder satisfies
\[
\widehat\tau(k)=4(1-x_k)(x_k+c_n),
\qquad
x_k=\cos(2\pi k/n).
\]
The cyclic cosine grid obeys \(-c_n\le x_k\le1\), so this is nonnegative for every character.

The proposed extremizer
\[
f_*(j)=\frac{c_n+\cos(2\pi\lfloor n/2\rfloor j/n)}{1+c_n}
\]
has nonnegative Fourier coefficients and is pointwise nonnegative. It has values \(f_*(0)=1\), \(f_*(\pm1)=0\), and \(f_*(\pm2)=2c_n-1\), giving ratio \(4c_n-1\).

The accompanying `verify.py` replays these identities numerically for every \(5\le n\le400\), including all character frequencies and all points of each cycle, and prints `VERIFY_OK`.

The finite replay is a consistency check only. The theorem for arbitrary \(n\ge5\) follows from the analytic factorization and explicit witness.
