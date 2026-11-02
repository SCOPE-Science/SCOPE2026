---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

For chi<1 the four-state generator is irreducible; conditional second moments solve a linear Markov-modulated OU system (2diag(2k+phi)-M)g=D_x 1. Perron-Frobenius positivity for the shifted Metzler generator ensures finiteness iff its spectral bound is negative; exact determinant and principal-block analysis give the stated D(delta)>0 threshold, with positive stationary stochastic convolution even if its variance diverges. A fresh independent SymPy construction of the entire generator verified det=64(2k+lambda)D(delta), the inverse conditioned moment h=g_2=g_4, Mpsi=-2lambda psi, diag(2k+phi)psi=2k psi and the derivative d h/d delta =D_x lambda c²[k(2k+lambda)-2c²]/[4D(delta)^2]. This backward eigenmode yields the velocity covariance e^{-2(k+lambda)t}; integrating Green–Kubo gives the full MSD and long-time diffusion. A stable k=1,lambda=2,c=3/2 example has critical delta=1/7. The finite symbolic/numerical checks corroborate these identities; irreducibility and positivity arguments justify parameter-wide statements.

## originality

PASS

Cocconi–Alston–Bertrand (2023) gives the same M(chi)=lambda[(1-chi)Mmono+chi Mbi] switching model, but its main text and supplement explicitly restrict exact discrete-state transport to chi=1. Alston–Cocconi–Bertrand (2022) derive 2-state fluctuating-OU conditional variances and entropy rates. Lindskog–Majumder (2019) give general switching-OU stationary behavior. None of those inspected exact statements supplies the irreducible 4-state chi<1 moment determinant, its diffusion-response switch or the persistence independence of chi. Novelty is model-specific and subject to possible deductions from general switching matrices.

## value

PASS

This resolves a physically motivated parameter interpolation omitted in the primary model. Sharp second-moment divergence, asynchrony-driven stabilization, sign-reversing effect on diffusivity, and fixed velocity-memory rate separate fluctuation amplitude from persistence. Such a complete transport phase diagram is more than a routine positivity calculation or marginal parameter perturbation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
