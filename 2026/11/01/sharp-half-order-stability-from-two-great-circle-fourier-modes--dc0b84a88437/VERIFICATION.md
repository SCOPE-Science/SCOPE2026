---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The rotated equatorial Fourier coefficient defines a bounded L2(S2)->L2(SO3) operator by Jensen/Fubini. Peter-Weyl/Schur orthogonality diagonalizes it on H_ell; parity leaves order2 for even ell and order3 for odd ell. Exact associated-Legendre values at zero yield lambda_even and lambda_odd. Independently evaluated symbolic associated Legendre with factorial prefactors for every ell=2..16 and m=2,3: all exact eigenvalues agree, including parity zeros. With a_k=binom(2k,k)/4^k, W_k=(2k+1)a_k^2 decreases strictly to 2/pi, and (ell+1)lambda_ell>W_k. Therefore sum observations >= (2/pi) sum_{ell>=2} ||f_ell||^2/(ell+1); equality only low degrees, and pure high-harmonic test functions yield sharp constant. Smooth convex support perturbations 1+epsilon Y_ell show no stronger H^s estimate for s>-1/2, with epsilon allowed ell-dependent. Finite exact checks do not replace infinite Schur orthogonality/Wallis asymptotics.

## originality

PASS

Myroshnychenko et al. Theorem 1.4 proves exactly the zero-kernel assertion for continuous functions; that is acknowledged prior work. Hielscher et al. provide general arc-transform Wigner SVD and n^{-1/2} decay, but their integrated arc transform differs from the two selected Fourier moments, and the inspected Theorems 3.3/4.3/4.4 do not state the best 2/pi constant for the joint two-order observable. A specialization of their machinery plus new Wallis optimization is required; originality best of knowledge.

## value

PASS

This gives an exact stable quantitative version of an existing all-circle ball-rigidity test, with optimal inversion exponent and nonattained sharp constant; the inverse problem and two-mode observable are naturally motivated.

The dated certificate retains the supplied scientific assessment, sources and limitations.
