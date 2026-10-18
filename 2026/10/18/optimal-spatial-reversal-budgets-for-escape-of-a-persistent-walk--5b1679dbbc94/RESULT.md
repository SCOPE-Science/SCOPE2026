# Optimal spatial reversal budgets for escape of a persistent walker

## Finding
A particle travels at speed \(v>0\) in the open interval \((0,L)\), with velocity \(+v\) or \(-v\), reversing direction at a position-dependent rate \(\lambda(x)\geq0\). Both endpoints absorb at first contact, and the initial velocity is equally likely to have either sign. Fix a starting point \(0<x<L\) and the *total spatial reversal budget* \(\Lambda=\int_0^L\lambda(y)\,dy\). Define \(s=x/L\) and \(\eta=\Lambda/v\). Among **all** nonnegative integrable profiles with this budget, the attainable mean exit times \(\tau_\lambda(x)\), for \(\eta>0\), are exactly the open interval
\[
\boxed{\ \frac{L}{v}\left(\frac12-\frac{\eta}{1+\eta}\left|s-\frac12\right|\right)
<\tau_\lambda(x)<\frac{L}{2v}(1+\eta)\ .\ }
\]
The bounds are sharp but are not attained by an integrable profile. The lower value is approached by concentrating all rate immediately *to the right of the source* if \(s<1/2\), or *to its left* if \(s>1/2\); either side works at the midpoint. The upper value is approached by dividing the spatial rate budget equally into narrow layers at the two absorbing endpoints. If \(\Lambda=0\), the unique value is \(L/(2v)\).

In contrast, **every reflection-symmetric rate profile** \(\lambda(y)=\lambda(L-y)\) has \(\tau_\lambda(x)\ge L/(2v)\) at every starting position. Thus an asymmetric spatial reversal layer can reduce the mean below the direction-averaged ballistic exit time for any off-center source, although a symmetric reversal profile cannot.

## Assumptions and scope
The motion is a piecewise-deterministic velocity-jump Markov process with velocities \(\pm v\), instantaneous reversals at local Poisson intensity \(\lambda(x)\in L^1((0,L))\), and no sticking, force, diffusion, or reflections. Both endpoints are fully absorbing on contact. For the theorem, fix \(L,v>0\), \(s\in(0,1)\), and \(\Lambda\ge0\); all admissible rate profiles are nonnegative measurable integrable functions with \(\int_0^L\lambda=\Lambda\). Boundary values on null sets have no effect. The escape time is averaged over the two equiprobable initial velocity signs, not over initial positions. The optimization concerns the *spatial integral* of the reversal rate, not the mean number of actual reversals.

## Proof
**Existence and backward equations.** During a straight excursion of length at most \(L\), the integrated hazard of a velocity reversal is at most \(\Lambda/v\). Conditional on any current position and velocity, with probability at least \(e^{-\Lambda/v}>0\) the walker exits without another reversal within \(L/v\). Iterating this bound proves almost-sure finite exit and finite expected exit time, even for unbounded integrable rates. Writing \(T_+(y)\) and \(T_-(y)\) for the velocity-conditioned means, the generator equations hold almost everywhere:
\[
 vT_+'+\lambda(T_--T_+)=-1,\qquad
 -vT_-'+\lambda(T_+-T_-)=-1,
\]
with outgoing absorption conditions \(T_-(0)=0\) and \(T_+(L)=0\). Their bounded absolutely continuous solution is the mean exit time by the stopped-process Dynkin formula; the positivity argument above also guarantees uniqueness.

**Exact mean for an arbitrary integrable profile.** Let \(U=(T_++T_-)/2\), \(D=(T_+-T_-)/2\). Adding/subtracting the equations gives
\[
D'=-1/v,\qquad U'=(2\lambda/v)D.
\]
Thus \(D(y)=(cL-y)/v\) for a constant \(c\). The absorbing conditions imply \(U(0)=D(0)\), \(U(L)=-D(L)\). Define the dimensionless finite measure \(d\mu(t)=(L/v)\lambda(Lt)\,dt\) on \([0,1]\). Its total mass is \(\eta\). Write
\[
m=\int_0^1t\,d\mu(t),\qquad a=\mu([0,s]),\qquad b=\int_0^st\,d\mu(t).
\]
Integrating \(U'\) and imposing the boundary conditions gives
\[
c=\frac{1/2+m}{1+\eta},\qquad
\boxed{\ \frac vL\tau_\lambda(Ls)=\frac{(1+2a)(1/2+m)}{1+\eta}-2b\ .\ }
\]
This identity is exact for every allowed profile. The normalization is **reversal rate**, not the rate of randomized tumbles that select a new direction with probability one half.

**Sharp lower bound.** Let \(b_r=m-b\) be the right-side first moment. Rearranging the exact identity gives
\[
(1+\eta)\frac vL\tau_\lambda(Ls)
=(1+2a)(1/2+b_r)-(1+2\eta-2a)b.
\]
For fixed \(a\in[0,\eta]\), \(0\le b\le sa\) and \(s(\eta-a)\le b_r\le\eta-a\). Therefore
\[
(1+\eta)\frac vL\tau_\lambda(Ls)
\ge\frac12+s\eta+a(1-2s).
\]
The minimum over \(a\in[0,\eta]\) is \(1/2+\eta\min\{s,1-s\}\), yielding the claimed lower endpoint. Equality for \(\eta>0\) would require the positive mass of \(\mu\) to be concentrated at the single interior location \(s\), impossible for absolutely continuous \(\mu\). A constant-height narrow rectangular reversal layer on the appropriate side of \(s\), whose total mass is exactly \(\eta\), approaches equality. For \(s=1/2\), either side works.

**Sharp upper bound.** For fixed \(a\), \(b\ge0\) and \(b_r\le\eta-a\) give
\[
(1+\eta)\frac vL\tau_\lambda(Ls)
\le(1+2a)(1/2+\eta-a)
=\frac{(1+\eta)^2}{2}-2\left(a-\frac\eta2\right)^2.
\]
The last term vanishes at \(a=\eta/2\), giving the upper endpoint. For \(\eta>0\) equality would require positive mass exactly at the endpoints \(0\) and \(1\), which no integrable profile has. Two shrinking rectangular boundary layers, each bearing half the mass, approach equality.

**Every interior value is attainable.** The class of fixed-mass nonnegative integrable profiles is convex and hence path-connected. The exact displayed mean depends continuously on the profile in the \(L^1\) norm for fixed \(s\). Given any desired value strictly between the two sharp endpoints, choose one admissible profile with a smaller mean and another with a larger mean using the described concentrating sequences; interpolating these profiles and applying the intermediate value theorem yields that value. This establishes the complete *open* range, not merely the bounds.

**Symmetry obstruction.** For reflection-symmetric \(\lambda\), the dimensionless first moment is \(m=\eta/2\), hence \(c=1/2\). The mean-profile derivative is
\[
\frac{d}{ds}\left(\frac vL\tau_\lambda(Ls)\right)
=2\frac{d\mu}{ds}\left(\frac12-s\right),
\]
which is nonnegative to the left of the midpoint and nonpositive to its right. The dimensionless mean equals \(1/2\) at both endpoints by the exact formula, so it is at least \(1/2\) everywhere. An off-center source with \(\eta>0\) admits a strictly lower nonsymmetric design by the lower sharp bound.

## Verification
A standalone script `verification.py` computes the exact integral formula for piecewise-constant profiles and independently approximates the stopped velocity-jump process by a finite-state Markov chain on increasingly fine spatial grids. It checks three profiles (uniform, a localized source-adjacent layer, and symmetric endpoint layers), verifies the strict theoretical bounds, and records decreasing discrepancies between the full Markov generator and the analytic formula. The proof of the continuum theorem is the backward-equation and sharp-moment argument above; finite-grid agreement is a corroborating calculation, not an infinite-dimensional certificate. Run with `python verification.py` (requires NumPy and SciPy).

## Relationship to prior work
Leydolt (1993) studies telegrapher first-passage distributions, including two absorbing boundaries. Angelani, Di Leonardo and Paoluzzi (2014, openly available as a 2015 preprint) derive spatially dependent tumble-rate first-passage equations for a reflecting/absorbing configuration; they do not optimize the freely located rate profile under a fixed integral with two absorbing endpoints. Newby and Keener (2011) study spatially inhomogeneous velocity-jump dynamics and metastable escape near turning points, a related but physically different first-exit question. Angelani (2023) develops generic boundary conditions with homogeneous bulk switching, and Angelani (2024) optimizes homogeneous tumbling in other boundary arrangements. Guéneau, Majumdar and Schehr (2023/2024) optimize a constant reversal rate under confining potentials. The contribution here is the exact *function-space, fixed-budget* attainable interval with sharp spatial concentrating designs and the symmetric-profile obstruction. The general backward-equation method itself is standard and is not presented as novel.

## Limitations
The optima are infima and suprema not achieved within \(L^1\): their approximating rates diverge on shrinking intervals. Imposing pointwise bounds, smoothness, or a minimum spatial width changes the optimization. This result concerns only the initial-velocity-averaged mean first-exit time, not its variance, the conditioned exit-side distribution, empirical reversal count, or interacting particle systems. The sharp variational conclusion is supported by the cited comparisons but unindexed equivalent formulations cannot be ruled out. Full texts of some older closely related papers were unavailable, including the Newby–Keener paper; its publisher abstract, not its full derivation, was examined.

## References
- H. J. Leydolt, *First-passage times and solutions of the telegrapher equation with boundaries*, Physical Review E **47** (1993), 3988. DOI: 10.1103/PhysRevE.47.3988.
- J. M. Newby and J. P. Keener, *An asymptotic analysis of the spatially inhomogeneous velocity-jump process*, Multiscale Modeling & Simulation **9** (2011). DOI: 10.1137/10080676X.
- L. Angelani, R. Di Leonardo and M. Paoluzzi, *First-passage time of run-and-tumble particles*, European Physical Journal E **37** (2014), article 59. DOI: 10.1140/epje/i2014-14059-4; https://arxiv.org/abs/1506.08046.
- L. Angelani, *One-dimensional run-and-tumble motions with generic boundary conditions*, 2023. https://iris.cnr.it/handle/20.500.14243/450937.
- L. Angelani, *Optimal escapes in active matter*, 2024. DOI: 10.1140/epje/s10189-023-00402-7.
- M. Guéneau, S. N. Majumdar and G. Schehr, *Optimal mean first-passage time of a run-and-tumble particle in a class of one-dimensional confining potentials*, https://arxiv.org/abs/2311.06923.
