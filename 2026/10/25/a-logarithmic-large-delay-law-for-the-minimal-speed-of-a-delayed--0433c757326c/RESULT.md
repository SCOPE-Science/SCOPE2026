# A logarithmic large-delay law for the minimal speed of a delayed Fisher–KPP lattice front

## Finding

For fixed diffusion coefficient \(d>0\), consider the nearest-neighbor delayed Fisher–KPP lattice equation

\[
\dot u_n(t)=d\bigl(u_{n+1}(t)-2u_n(t)+u_{n-1}(t)\bigr)+u_n(t-\tau)\bigl(1-u_n(t)\bigr),\qquad n\in\mathbb Z.
\]

Let \(c_\tau>0\) denote its minimal admissible positive speed for a monotone front \(u_n(t)=\phi(n+c_\tau t)\) connecting \(0\) to \(1\). With the delayed growth coefficient normalized to one, the speed satisfies the additive-constant asymptotic law

\[
\boxed{\frac{\tau c_\tau^2}{d}=\log\tau+1+o(1)\qquad(\tau\to\infty).}
\]

In particular, \(c_\tau\to0\) and \(c_\tau\sim\sqrt{d\log\tau/\tau}\). The constant \(+1\) is part of the claim; the proof below derives it from the double-root equations rather than from numerical fitting.

## Assumptions and scope

The diffusion coefficient \(d\) is fixed and strictly positive. The only reaction term is delayed logistic growth, \(u_n(t-\tau)(1-u_n(t))\); there is no instantaneous mortality term. The spatial operator is the nearest-neighbor lattice Laplacian, and the growth coefficient is one, so \(\tau\) is expressed in the corresponding dimensionless time units. The claim concerns the minimal speed selected by the linearized leading edge. It does not assert the same law for continuous diffusion, nonlocal spatial kernels, an added instantaneous death term, or a general delayed nonlinearity.

## Proof

For this model the leading-edge dispersion function is

\[
\Delta_\tau(c,\lambda)=c\lambda-dL(\lambda)-e^{-c\lambda\tau},\qquad L(\lambda)=e^\lambda+e^{-\lambda}-2=2(\cosh\lambda-1).
\]

Linear speed selection gives a positive double root \((c_\tau,\lambda_\tau)\), so

\[
\Delta_\tau(c_\tau,\lambda_\tau)=0,\qquad
\partial_\lambda\Delta_\tau(c_\tau,\lambda_\tau)=0.
\]

Write \(c=c_\tau\), \(\lambda=\lambda_\tau\), and \(E=e^{-c\lambda\tau}\). The two equations are

\[
c\lambda=dL(\lambda)+E,\qquad c=dL'(\lambda)-c\tau E.
\]

We first show \(\lambda\to0\). The equations imply \(dL(\lambda)<c\lambda\) and \(c<dL'(\lambda)\). If \(\lambda\ge\varepsilon>0\) along a sequence \(\tau\to\infty\), then \(c\lambda\ge dL(\varepsilon)\), hence \(E=e^{-c\lambda\tau}\) is exponentially small. Also \(c\tau E\le d\tau L'(\lambda)e^{-d\tau L(\lambda)}\to0\), uniformly for \(\lambda\ge\varepsilon\), because \(L'(\lambda)/L(\lambda)\) is bounded there and \(L(\lambda)\ge L(\varepsilon)>0\). The two double-root equations would then force both \(c/d\to L'(\lambda)\) and \(c/d\to L(\lambda)/\lambda\), contradicting \(\lambda L'(\lambda)>L(\lambda)\) for every \(\lambda>0\). Thus \(\lambda\to0\), and \(c<dL'(\lambda)\) gives \(c\to0\) and \(E\to0\).

Introduce

\[
p=\frac{c}{d\lambda},\qquad y=d\lambda^2\tau,\qquad z=c\lambda\tau=py,
\qquad \ell=\frac{L(\lambda)}{\lambda^2},\qquad m=\frac{L'(\lambda)}{\lambda}.
\]

The double-root equations give the exact identities

\[
E=d\lambda^2(p-\ell),\qquad \tau E=\frac{m}{p}-1,
\]
so

\[
y(p-\ell)=\frac{m}{p}-1. \tag{1}
\]

Taylor expansion at zero yields \(\ell=1+O(\lambda^2)\) and \(m=2+O(\lambda^2)\). Also \(\ell<p<m\), hence \(p\) is bounded and \(p\ge1+o(1)\). We must have \(y\to\infty\): otherwise \(z=py\) would stay bounded along a subsequence, making \(E=e^{-z}\) bounded away from zero, contrary to \(E\to0\). Equation (1) then implies \(p-\ell=O(1/y)\), and therefore \(p\to1\). It follows from (1) that \(\tau E=m/p-1\to1\), whence

\[
z=-\log E=\log\tau+o(1),\qquad y\sim\log\tau.
\]

Since \(\lambda^2=y/(d\tau)\), we have \(y(\ell-1)=O(y\lambda^2)=O((\log\tau)^2/\tau)=o(1)\). Equation (1) now gives \(y(p-1)=y(p-\ell)+y(\ell-1)\to1\). Consequently \(z-y=y(p-1)\to1\), so

\[
y=\log\tau-1+o(1).
\]

Finally, \(\tau c^2/d=p^2y\), and \(p\to1\), \(y(p-1)\to1\) imply

\[
\frac{\tau c^2}{d}=y+2y(p-1)+y(p-1)^2=\log\tau+1+o(1),
\]
which proves the claim.

## Verification

The proof uses only the double-root characterization of the linearly selected speed and the exact identities displayed above. The sign conventions follow from the front orientation \(u_n(t)=\phi(n+ct)\), \(\phi(-\infty)=0\), \(\phi(+\infty)=1\). The Taylor coefficients used are \(L(\lambda)=\lambda^2+\lambda^4/12+O(\lambda^6)\) and \(L'(\lambda)=2\lambda+\lambda^3/3+O(\lambda^5)\); only the leading terms are needed for the additive constant. No finite numerical experiment is used as proof of the infinite-delay limit. The conclusion is for fixed \(d>0\); no uniformity in \(d\) is asserted.

## Relationship to prior work

The 2014 preprint on stability of traveling fronts for discrete reaction–diffusion equations with nonlocal delay gives this model's traveling-wave dispersion relation and the double-root characterization of its minimal speed. The present claim is a further asymptotic analysis of that implicit system as \(\tau\to\infty\); the large-delay law with additive constant \(+1\) is not stated in the relevant model, dispersion-relation, or main-result sections inspected. A 2006 paper on a broader nonlocal delayed lattice equation establishes existence and minimal-speed results, but its full text was not available in the bounded access attempts; that is a residual originality risk, not evidence that it contains this asymptotic. A 2008 result proves large-delay bounds of order \(1/\tau\) for a different continuous-diffusion equation with an instantaneous death term and a nonlocal delayed birth term. Its dispersion relation and model differ, so it does not imply the lattice law proved here. A 2015 paper on nonlocal delayed lattice dynamics treats nonlocal diffusion and interaction, rather than this nearest-neighbor/local-delayed-growth specialization.

## Limitations

The result determines the leading scale and its additive constant only. It does not give a next-order correction, prove uniformity over families of diffusion coefficients, or transfer to other kernels or reaction laws. A related 2006 lattice paper's full text remained inaccessible during the bounded search, so originality is supported by the actual searches and the inspected literature but is not certified by exhaustive literature coverage.

## References

1. S. Guo and J. Zimmer, “Stability of traveling wavefronts in discrete reaction-diffusion equations with nonlocal delay effects,” *Nonlinearity* 28 (2015), 463–492. Preprint first posted 2014-12-16, arXiv:1412.5164v1. https://arxiv.org/abs/1412.5164. DOI: 10.1088/0951-7715/28/2/463.
2. S. Ma, P. Weng, and X. Zou, “Asymptotic speed of propagation and traveling wavefronts in a non-local delayed lattice differential equation,” *Nonlinear Analysis* 65 (2006), 1858–1890. DOI: 10.1016/j.na.2005.10.042.
3. Z. Xu and J. Ma, “Monotonicity, asymptotics and uniqueness of travelling wave solution of a non-local delayed lattice dynamical system,” *Discrete and Continuous Dynamical Systems* 35 (2015), 5107–5131. DOI: 10.3934/dcds.2015.35.5107.
4. M. Aguerrea and G. Valenzuela, “On the minimal speed of traveling waves for a non-local delayed reaction-diffusion equation,” arXiv:0807.2441 (2008). https://arxiv.org/abs/0807.2441.
