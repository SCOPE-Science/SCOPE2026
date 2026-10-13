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

# Verification and reproducibility

The universal theorem is analytical. Its critical identities and checks are these:

1. Each of the \(q+1\) finite-field lines is self-symplectic-orthogonal. Its character sum over the nonzero labels is \(q-1\) for a label in that line and \(-1\) otherwise. These identities fix all normalization factors in the canonical rates.
2. Every nontrivial channel eigenvalue is \(x_j+(1-x_j)e^{-ct}>0\) at finite time, so no singular time-local generator is assumed. Weyl Fourier inversion gives \(\gamma_k=q^{-2}(\sum_{j\ne k}g_j-(q-1)g_k)\), where \(g_j=c(1-x_j)e^{-ct}/[x_j+(1-x_j)e^{-ct}]\).
3. The first-order Choi test shows negativity of any individual coefficient is an obstruction to complete positivity, while the nonnegative coefficients form a GKLS generator.
4. In the simplex interior, \(a_j=(1-x_j)/x_j\), \(m=\max_j a_j\), and monotonicity of \(a/(1+ay)\) give CP-divisibility if and only if \(\sum_j a_j\ge qm\). Otherwise the one-dimensional function \(F(y)\) in the proof increases strictly, starting negative and ending positive, establishing precisely one onset of a negative rate.
5. Zero-weight faces are checked directly at every positive time; a vertex reduces to its original semigroup. The equality-case expansion is a Taylor expansion with a strictly positive coefficient.

The packaged `verify.py` uses only Python 3.9+ standard-library modules. Run `python3 verify.py` in the directory containing this document. It directly evaluates all nonidentity Weyl Fourier characters (not only the derived formula) for prime fields of sizes 3, 5, 7 and the proper degree-two field of size 4. It uses a reproducible seed, 240 mixing vectors for each dimension, eight times, and direct character sums over \(q^2-1\) labels. All 182400 direct Fourier-to-formula comparisons passed, together with sign, onset-root and face classification tests. This finite computation cannot establish the claim for all prime powers or exclude unexamined prior work.

A diagnostic exact example is \(q=3\), \(x=(1/10,3/10,3/10,3/10)\): the onset occurs at \(e^{-ct_*}=11/21\). The numerical tests do not certify numerical precision outside their tested samples, nor provide an independent external audit.
