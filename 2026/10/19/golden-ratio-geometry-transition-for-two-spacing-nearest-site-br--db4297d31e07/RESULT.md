# Golden-ratio geometry transition for two-spacing nearest-site Brownian resetting

## Finding

A Brownian particle reset at rate \(r\) to the nearest point of a lattice with alternating positive spacings \(a,b\) has the exact centered diffusivity

\[\mathcal D(a,b)=\frac{r(a+b)^2\cosh(ka/2)\cosh(kb/2)}{4[\sinh(ka/2)+\sinh(kb/2)]\sinh(k(a+b)/2)},\qquad k=\sqrt{r/D}.\]

At fixed period \(L=a+b\) and fixed positive \(D,r\), its optimal geometry has a sharp golden-ratio transition. Write \(\varphi=(1+\sqrt5)/2\) and \(q=kL/4\). If \(\cosh q<\varphi\), no positive-gap geometry attains the supremum: clustering two sites arbitrarily close approaches it. If \(\cosh q\ge\varphi\), equal gaps uniquely maximize \(\mathcal D\). Exactly at \(\cosh q=\varphi\), the equal-gap value and clustered-site limit tie, while all strictly unequal positive gaps are worse. In every regime the macroscopic drift is zero.

## Assumptions and scope

Let \(D,r,L>0\), \(a\in(0,L)\), and \(b=L-a\). Between rate-\(r\) independent Poisson alarms, the real-valued position evolves as standard Brownian motion with generator \(D\partial_{xx}\). At every alarm, its position is instantaneously mapped to a nearest site of \(\Lambda=\{nL,nL+a:n\in\mathbb Z\}\); midpoint ties have probability zero. There is no waiting time at a reset site. The initial position is at a site (an arbitrary fixed initial displacement has no effect on the limit). Define \(\mathcal D=\lim_{t\to\infty}\operatorname{Var}(X_t)/(2t)\). All statements are for \(a,b>0\); the clustered configuration is understood only as a one-sided limiting geometry.

## Proof

**1. Exact one-step renewal statistics.** Starting at a site with its left neighbor at \(-b\) and right neighbor at \(+a\), record the first arrival at either neighboring site by Brownian hitting or by an alarm mapping the current position there. An alarm in the central interval \((-b/2,a/2)\) restarts the trial at zero. Let \(H\) be Brownian first exit from \((-b,a)\), and \(E\) an independent exponential clock of rate \(r\). Set \(k=\sqrt{r/D}\) and \(L=a+b\).

The killed resolvent density from zero is

\[G(y)=\begin{cases}\dfrac{\sinh(k(b+y))\sinh(ka)}{Dk\sinh(kL)},&-b<y<0,\\[5pt]\dfrac{\sinh(kb)\sinh(k(a-y))}{Dk\sinh(kL)},&0<y<a.\end{cases}\]

The right success probability in one trial consists of a Brownian exit at \(+a\), with probability \(\sinh(kb)/\sinh(kL)\), and the alarm contribution \(r\int_{a/2}^aG(y)\,dy\). Their sum is \(R/\sinh(kL)\), where

\[R=\sinh(kb)\cosh(ka/2),\qquad Q=\sinh(ka)\cosh(kb/2).\]

The analogous left success probability is \(Q/\sinh(kL)\). Summing the geometric number of failed central resets gives eventual right/left probabilities

\[p=\frac{R}{R+Q},\qquad 1-p=\frac{Q}{R+Q}.\]

The expected duration of one trial is \(\mathbb E\min(H,E)=[1-\mathbb E e^{-rH}]/r\). Since \(\mathbb E e^{-rH}=[\sinh(ka)+\sinh(kb)]/\sinh(kL)\), division by its success probability gives the mean time to move from the current site to an adjacent site:

\[\tau=\frac{\sinh(kL)-\sinh(ka)-\sinh(kb)}{r(R+Q)}>0.\]

All stopping times here have finite moments; this follows from positive trial-success probability and exponential killing of individual trials. Brownian strong Markov and Poisson memorylessness make successive completed site-to-site trials independent after conditioning on site type.

**2. Two-site centering and the effective variance.** The lattice alternates types \(A\) and \(B\). At \(A\), the next step is \(+a\) with probability \(p\) or \(-b\) with probability \(1-p\). The geometry at \(B\) is the reflection: it steps right by \(b\) with probability \(1-p\), or left by \(a\) with probability \(p\). Both types have the same mean completion time \(\tau\). Thus every consecutive \(A\)-to-\(B\)-to-\(A\) cycle has mean displacement zero and mean elapsed time \(2\tau\). Its total displacement equals \(+L\) or \(-L\), each with probability \(p(1-p)\), and otherwise vanishes. Its second moment is exactly \(2L^2p(1-p)\). Different complete two-step cycles are independent and identically distributed, even though each displacement can correlate with its own duration.

The renewal-reward variance theorem for cycles with zero mean reward yields

\[\lim_{t\to\infty}\frac{\operatorname{Var}(X_t)}{2t}=\frac{2L^2p(1-p)}{2(2\tau)}=\frac{L^2p(1-p)}{2\tau}.\]

Indeed, the particle is always within one neighboring gap of the most recently completed site passage, so the residual displacement is uniformly bounded by \(L\) and does not change the diffusive limit. Since the mean cycle reward is zero, no displacement-duration covariance correction is required at the cycle level. Substitution gives

\[\mathcal D=\frac{rL^2RQ}{2(R+Q)[\sinh(kL)-\sinh(ka)-\sinh(kb)]}.\]

Putting \(u=ka/2\), \(v=kb/2\) and using \(\sinh(2u+2v)-\sinh(2u)-\sinh(2v)=4\sinh(u+v)\sinh u\sinh v\), this simplifies to the expression in the finding. Macroscopic drift vanishes by the zero-mean cycle reward and finite mean cycle time.

**3. Exact geometric optimization.** Keep \(s=kL/2=u+v\) fixed and put \(w=\cosh((u-v)/2)\), \(c=\cosh(s/2)\). The positive-gap domain maps onto \(1\le w<c\), with \(w=1\) only for \(a=b\). The diffusivity is a positive constant independent of \(w\) times

\[f_s(w)=2w+\frac{\cosh s-1}{w},\qquad \frac{\mathcal D}{D}=\frac{(kL)^2}{16\sinh(s/2)\sinh s}f_s(w).\]

Here \(f_s''(w)=2(\cosh s-1)/w^3>0\), so its maximum over the closed extension \([1,c]\) is at an endpoint, strictly beating all interior points. Because \(\cosh s-1=2(c^2-1)\),

\[f_s(c)-f_s(1)=-\frac{2(c-1)(c^2-c-1)}{c}.\]

For \(c>1\), its sign is positive precisely for \(c<\varphi\), zero precisely for \(c=\varphi\), and negative precisely for \(c>\varphi\). The endpoint \(w=c\) is a degenerate dimer \(a\to0\) or \(b\to0\), hence not attained among distinct positive gaps. The endpoint \(w=1\) is the uniform spacing \(a=b\). This proves all equality and attainment statements. Equivalently, the threshold is \(kL=4\operatorname{arcosh}\varphi\), or \(rL^2/D=16(\operatorname{arcosh}\varphi)^2\).

## Verification

The supplied standalone `checker.py` evaluates the stopped-Brownian killed resolvent independently by numerical integration and compares exit probabilities, mean passage time, and both exact diffusivity formulas. It checks the regular-lattice limit, the clustered-lattice limit, the golden-ratio phase boundary, strict convexity endpoint bounds, and the positive adjacent-step anticorrelation contribution. It completed 2177 assertions with no failures using SciPy and NumPy. These tests support implementation and normalization; the proof of the all-parameter classification is the analytic argument above.

## Relationship to prior work

Alston and Bertrand (2024 preprint; 2025 journal publication) introduce the nearest-site Poisson resetting model, derive interval first-passage statistics, and establish the homogeneous-array diffusivity \(\mathcal D/D=z^2\csch z\coth z\) for the gap parameter \(z=kL/2\). Their article also studies irregular arrays through a site-averaged local mean-square approach and establishes an optimum when the reset rate and array geometry can both be tuned. The present result instead fixes \(r,D,L\), explicitly retains the alternating directions in a two-site renewal cycle, and classifies the geometry optimizer via an exact golden-ratio threshold. Its nonuniform two-spacing dispersion and fixed-period phase transition are not asserted as already present in the source paper. The source's general irregular-array treatment creates a residual risk that similar formulas or implications have appeared elsewhere.

Roberts, Sezik, and Lardet (2024) study a different ratchet-mediated resetting mechanism and its currents; a spatially asymmetric capture rule on an otherwise uniform lattice does not reduce to the present alternating-gap nearest-site model. Standard Markov-renewal and regeneration theorems are used, not asserted as new.

## Limitations

The result assumes a strictly two-periodic arrangement, one-dimensional free Brownian excursions, instantaneous nearest-site resetting, and Poisson alarms. A near-merger of two distinct sites is a limit of geometries rather than an attained maximizer. The theorem fixes the total two-gap period \(L\), not the average nearest-site spacing across differently sized unit cells, and does not optimize \(r\). No statement is made about arbitrary disordered arrays, interacting particles, finite-speed capture, or independent mathematical-priority verification.

## References

- H. Alston and T. Bertrand, *Boosting macroscopic diffusion with local resetting*, arXiv:2401.12772v1 (first public 2024-01-23); Phys. Rev. E **111**, 034114 (2025), doi:10.1103/PhysRevE.111.034114. Sections III–VI and Appendices B–C.
- C. Roberts, R. Sezik, and M. Lardet, *Ratchet-mediated resetting: Current, efficiency, and exact solution*, arXiv:2405.10698v1 (2024).
- Standard strong Markov, killed Brownian Green-function, and renewal-reward principles, used in the proof without novelty claim.
