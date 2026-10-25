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

# Exact verification

Execute `python3 verify_gd_scroll.py` from the extracted package directory with Python 3 standard library; there are no third-party dependencies.

The script builds the two norm polynomials \(s_1,s_2\), the rank-one block data polynomials \(p_1,p_2\), the common denominator \(L=s_1s_2\), the numerator \(G\), and the critical numerator \(H=G'L-GL'\), all over exact rational coefficients. It checks \(\deg L=10\) and \(\deg H=18\); it reproduces all \(19\) coefficients of \(105H\) and checks the monic polynomial greatest common divisors \(\gcd(G,L)=\gcd(H,L)=\gcd(H,H')=\gcd(H,p_1p_2)=1\). The last identity certifies that the critical roots avoid the algebraic cut locus of the explicit projection data.

Successful output is `VERIFY_OK GD=18; 18 simple finite critical points, no poles/infinity`. The code is a certificate for the exact polynomial subclaims, not a randomized sample or an independent mathematical review. The geometric proof that this witness implies the generic GD degree is in `RESULT.md`.

The result does not determine generic real critical-point counts or other scroll types. No independent audit has been performed.
