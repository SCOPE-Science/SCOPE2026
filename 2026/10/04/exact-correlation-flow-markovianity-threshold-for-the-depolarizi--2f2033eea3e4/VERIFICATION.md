---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-11.md",
      "INDEPENDENT_AUDIT_2026-10-11.json"
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

For isotropic depolarizing plus one-spin Ising memory, write q=e^{-gamma*u}, r=sqrt(1-(1-z^2)*sin(u)^2), and correlation-state eigenvalues a,a,b,c with a=(1-q)/4, b=(1+q+2qr)/4,c=(1+q-2qr)/4. Their mutual information has I_q>0 by strict convexity of relative entropy in q, and I_r>=0. The key ratio I_r/(qI_q)<=2r/(1+2r^2) is EXACTLY the weighted AM-GM statement C^(1+r)>=B^(1-r) A^(2r) for A=1-q,B=1+q+2qr,C=1+q-2qr. Its bound is sharp as q->0 by quadratic expansion. On rising r branches, the rate is controlled by F_z(y)=2(1-z^2)*sqrt(y(1-y))/(3-2(1-z^2)y); differentiation yields unique maximum y*=3/(2(2+z^2)) and threshold (1-z^2)/sqrt(3(1+2z^2)). Above it all rates are nonpositive; below it repeated late rising branches with q->0 make them positive, including gamma=0 by periodicity. z=1 has r constant and threshold zero. Verified boundary z=0 gives 1/sqrt(3) and ratio to the published LPP threshold <=1. Independently evaluated a grid of the ratio and geometric maxima; the all-time iff statement follows from the AM-GM proof, not sampling.

## originality

PASS

The same-model primary Apollaro et al paper derived analytic thresholds for other witnesses but explicitly handled the Luo–Fu–Song (LFS) correlation-flow threshold numerically and reported a universal value near 0.6. It did not give the radical threshold (1-z^2)/sqrt(3(1+2z^2)), its exact uniform max 1/sqrt(3), nor the global all-time sharpness proof. Nearby LFS references define the measure or compare different reservoir models. This is an exact solution of the source’s left-numerical threshold, original to the best of inspected evidence.

## value

PASS

Replacing an explicitly numerical and approximate Markovianity boundary in a standard open-system channel competition model with a sharp analytic iff threshold across all initial memory polarizations is a motivated mathematical gap. The weighted-AM-GM estimate and sharp late-time asymptotics provide a usable exact phase diagram and settle the strongest noise rate 1/sqrt3 rather than merely improving a decimal fit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
