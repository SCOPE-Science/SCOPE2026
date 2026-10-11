---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The restriction-class structure reduces every basis partner to the displayed canonical Fourier block with one repeated column. On the \(m-2\) dimensional zero-sum subspace the Gram eigenvalue is exactly \(m\), and direct expansion of the complementary \(3\times3\) block gives the stated cubic. Its signs at \(0,m,2m\), positivity of the Gram matrix, and the sign of the derivative at the extreme simple roots prove the root locations and monotonic optimization. At \(t=4\) the cubic factors as \((\lambda-1)(\lambda-2m)^2\); for odd \(m\) the maximal root-of-unity chord gives the stated \(t_m\), and the perturbation equation yields the asymptotic. Independent direct Fourier-Gram determinant checks through \(m=12\) reproduced the factorization and even-modulus spectrum.

## originality

PASS

The full Ferguson--Mayeli--Sothanaphan primary text was inspected at Example 4.19. It studies exactly \(E_m\), proves exactly one restriction class is doubled, and derives only \(L(E_m)\le2\) and \(\rho(E_m)\ge(m+1)/2\). It does not diagonalize the Gram matrix, optimize the chord parameter, or state the exact even/odd Riesz constants and sharp asymptotic. Resultary surfaced a determinant-tightness record for the same family and a two-point tightness profile, but neither determines the three extreme eigenvalues or this condition number.

## value

PASS

The source introduced this family precisely as quantitative evidence through a diverging Riesz ratio. Replacing its coarse divergence bound with the exact optimizing spectrum, parity split, and first asymptotic correction resolves the natural quantitative question for the exemplar family and distinguishes determinant tightness from conditioning.

The dated certificate retains the supplied scientific assessment, sources and limitations.
