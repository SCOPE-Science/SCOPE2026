# Independent audit — 2026-09-29

Record: `2026/09/13/048`  
Audited source tree: `04ac2a833fa05ff42ed3279001b5ac4ed35008c8`  
Disposition: **passed**

## Correctness

The two-sided discrepancy claim survives independent checking. The cubic-character indicator gives normalized Fourier coefficients of size O(p^{-1/2}), so Erdos-Turan yields E_p=O(log p/sqrt(p)). For p=7 mod 12, chi(-1)=1, so the three cubic Gaussian periods are real. When 2 is a cubic non-residue, S_1 and S_2 correspond to two distinct period values; the elementary three-cosine identity forces one of them to have size at least a constant times p^{-1/2}. Koksma then gives E_p>=c/sqrt(p). In Q(zeta_12,cuberoot(2)), primes p=7 mod 12 for which the S3 Frobenius is a 3-cycle form a positive-density Chebotarev set and are exactly the relevant 2-nonresidue cases. A fresh computation for the 44 primes p=7 mod 12 below 1000 reproduced the Fourier dichotomy with no failures and gave E_p*sqrt(p) in [0.617,1.190].

## Originality

The upper bound is a standard Gauss-sum plus Erdos-Turan consequence, and prior papers already study distribution/counting identities for cubic residues using third-order characters and Gauss sums. The specific infinitely-often lower bound obtained by coupling the first two Fourier modes with a Chebotarev family was not located in the focused search, but search non-detection is not a priority proof. The record should therefore be read as a concise explicit specialization rather than as an established new general discrepancy theorem.

## Scientific value

The record gives a clean matching square-root scale, up to the logarithm in the upper bound, and strengthens the requested lower bound by removing its logarithmic loss on an infinite arithmetic subfamily. The value is primarily in the explicit low-frequency/Chebotarev mechanism.

## Limitations

- The search found related cubic-residue distribution literature, so no priority claim is warranted.
- The exact constants in the discrepancy inequalities are not optimized.
- The repository text names output/artifacts/verify_numerics.py, while the audited tree stores the script at artifacts/verify_numerics.py; the audit used the actual archived artifact and treats this as a packaging-path defect, not a mathematical defect.
- The independent numerical check was supporting evidence only; the proof is analytic.

## Sources checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/13/048
- https://doi.org/10.3934/math.2020388
- https://encyclopediaofmath.org/wiki/Cubic_residue
- https://doi.org/10.1073/pnas.34.5.204
