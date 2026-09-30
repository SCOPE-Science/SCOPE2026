# Independent audit — 2026-09-30

**Record:** `2026/09/21/lorenz96-critical-global-stability-closure--2ec1ac76b299`  
**Audited source tree:** `0f8e72e152b10a0836b9df0f3788e5edb732f2a0`  
**Disposition:** passed

## Correctness — PASS

PASS. Cyclic equivariance makes G(e) a scalar multiple of e and energy preservation forces that scalar to vanish; homogeneity then yields Ae=0. Translating by Fe gives w'=G(w)+(FA-I)w and V'=w^T(FS-I)w. In the strict region this is negative definite. At a finite endpoint F=1/p*, the zero-dissipation set is E*=ker(S-p*I), which is orthogonal to e. Polarizing (e+sw)^TG(e+sw)=0 gives e^TG(w)=-w^TAw. Thus along any w in E*, d(e^Tw)/dt=-p*||w||^2, nonzero for w!=0, while a trajectory contained in E* would have e^Tw identically zero; hence the largest invariant subset is {0}. Boundedness plus LaSalle gives global asymptotic stability even at equality. If an inequality fails, normality of the circulant A supplies a linear eigenvalue with positive real part. The Lorenz-96 Fourier eigenvalues and the stated positive/negative endpoints follow directly.

## Originality — PASS

PASS. The accessible full arXiv manuscript of Kerin--Engler (arXiv:2005.07767) gives small-forcing/global convergence results for energy-preserving quadratic Lorenz-96 generalizations and spectral/bifurcation information, but the inspected text does not state the exact closed endpoint theorem or the transversality identity closing the semidefinite case. van Kekem--Sterk locate and classify first linear bifurcations, not global nonlinear stability at the nonhyperbolic boundary. Schlegel--Noack explains why semidefinite energy estimates are not generically sufficient. The filed endpoint argument therefore supplies a distinct closure of the known strict-energy region.

## Scientific value — PASS

PASS. Closing a sufficient open stability region exactly at the first linear-instability thresholds is a meaningful nonlinear stability result, especially because the endpoints are nonhyperbolic and ordinary negative-definite Lyapunov theory stops there. The proof isolates a reusable polarization/transversality mechanism for cyclic energy-preserving quadratic systems, and the classical Lorenz-96 corollary gives explicit dimension-dependent endpoints.

## Independent checks

- Re-derived G(e)=0, Ae=0, and the translated quadratic dynamics.
- Expanded the energy-preservation polynomial in e+sw to verify e^TG(w)=-w^TAw.
- Checked the LaSalle transversality argument at both positive and negative finite endpoints.
- Inspected the accessible Kerin--Engler manuscript and compared the classical Lorenz-96 bifurcation thresholds.

## Literature evidence

- https://arxiv.org/abs/2005.07767 — Kerin and Engler, accessible full manuscript on Lorenz-96 and energy-preserving generalizations; inspected for prior stability statements.
- https://doi.org/10.5194/npg-25-301-2018 — van Kekem and Sterk (2018), first-bifurcation and wave-propagation analysis of Lorenz-96.
- https://arxiv.org/abs/1310.0053 — Schlegel and Noack, energy-preserving quadratic systems and limitations of semidefinite trapping arguments.

## Limitations

- The theorem assumes homogeneous quadratic energy preservation, cyclic equivariance, uniform linear damping, and uniform forcing.
- It proves asymptotic stability at the endpoints but not a general sharp critical decay rate.
- It does not characterize post-bifurcation attractors outside the closed window.

No GitHub write was performed by the audit chat. The guarded publication plan stages only this audit evidence and the independent-audit verification channel.
