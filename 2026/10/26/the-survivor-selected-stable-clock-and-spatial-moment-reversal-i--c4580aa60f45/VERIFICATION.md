---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Reconstructed the clock and killed-kernel argument. The refresh-epoch transform is (1+u^alpha/n)^(-n), equivalently the independent product S_alpha (G_n/n)^(1/alpha). Mellin integration gives the stated negative moments and bounded moments of any fixed negative order for large n, as well as the uniform positive orders p<alpha. For the kernel estimates, write p_s(k) for the rate-one free transition probability and telescope the reflected difference into h terms p_s(k-1)-p_s(k+1)=2k p_s(k)/s at k=j-h+1,j-h+3,...,j+h-1. Applying the ordinary free lattice local CLT to these terms proves the derivative-scale kernel limit without subtracting two uncontrolled CLT errors. Survival telescopes exactly to sum_{k=1-h}^h p_s(k), giving the stated constant and uniform bound. For the endpoint tails, a global pointwise Gaussian bound is neither required nor valid at arbitrarily distant Poissonized sites: for s>=1 the free walk W_s satisfies E exp(±W_s/sqrt(s))=exp(s[cosh(1/sqrt(s))-1])<=C. The telescoping identity then controls every rescaled killed polynomial tail, and sup_k p_s(k)<=C/sqrt(s) controls the small endpoint range. This justifies the local-limit Riemann sums and the asymptotic M_q(s) with the stated Rayleigh coefficient. Negative moments control clock mass near zero, and the survival bound controls large clocks. The resulting inverse-square-root tilt is normalized by the stated A_alpha. At any t>0 the finite positive weighted sum of rates has 1-Laplace(u) asymptotic to a positive constant times u^alpha; the fractional-moment integral proves finiteness precisely below alpha, including divergence at equality. For q>1 use M_q(s) of order s^((q-1)/2); for q<=1 use the stopped first moment h. A larger still-subcritical moment gives uniform integrability; q=1 follows directly from conservation. This also checks all Gamma constants and the alpha=1/2 boundary. Replay: RESULT.md §§1–4 with the Bessel recurrence and exponential tail argument above. Inspected VERIFICATION.md and VERIFY.py; their numerical checks are only finite corroboration and were not executed.

## originality

PASS

Supported distinct contribution: the refresh-epoch survivor-conditioned joint endpoint/clock limit and actual normalized conditional-moment convergence. Do not credit the rate law, killed propagator, survival exponent or mean-absorption transition as new. The fixed-time cutoff and reversal also occur in a distinct later-dated record; no priority/order beyond the displayed dates is inferred, and the later result does not give the joint limit.

## value

PASS

The law of the operational time among survivors differs substantially from the population clock, even at the limiting scale. The joint limit makes the selection effect quantitative and explains which survivor spatial moments can be used; the exact finite-time moment boundary prevents an inference about spatial dispersion from the mean absorption time alone. These are meaningful consequences for this specified model without asserting a conditioned path-space theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
