# Pareto boundary layer at the intermittent limit of a reversible cusp map

## Finding
For the anti-symmetric cusp family of Basios, Forti and Gilbert, the canonical stationary conditional law of the contracting coordinate, conditioned at the zero endpoint of the expanding coordinate, has a nondegenerate **Pareto-type boundary-layer limit** at intermittency. Specifically, write \(a=1-\delta\), \(0<\delta<1\), and let \(Y_a\in[0,1]\) have the boundary conditional law defined below. Then
\[
\lim_{\delta\downarrow0}\Pr\{Y_{1-\delta}\le\delta z\}=\frac{z}{1+z},\qquad z\ge0.
\]
The convergence is uniform for \(z\) in compact subsets of \([0,\infty)\). Equivalently, \(Y_{1-\delta}/\delta\) converges in distribution to a nonnegative random variable with density \(1/(1+z)^2\). The limiting law has an infinite first moment. This is a statement about a **conditional measure**, not an absolutely continuous invariant density on the square.

An exact finite-parameter identity underlies the limit. Put
\[
\lambda=\frac{1+a}{2},\qquad G_a(u)=\lambda u-\frac a2u^2,\qquad y_n=G_a^{\circ n}(1).
\]
If \(R_a(y)=\Pr\{Y_a\le y\}\), then for every integer \(n\ge0\),
\[
R_a(y_n)=\lambda^n.
\]
Moreover, for every fixed \(t>0\), as \(\delta\downarrow0\),
\[
\frac{y_{\lfloor t/\delta\rfloor}}{\delta}\longrightarrow\frac{1}{e^{t/2}-1},\qquad
\lambda^{\lfloor t/\delta\rfloor}\longrightarrow e^{-t/2}.
\]
The latter formulas identify the crossover scale and prove the distributional assertion.

## Assumptions and scope
For \(0<a<1\), define monotone inverse branches \(g_{a,0},g_{a,1}:[0,1]\to[0,1]\) by
\[
 g_{a,0}(u)=\frac{1+a}{2}u-\frac a2u^2,\qquad
 g_{a,1}(u)=\frac12+\frac{1-a}{2}u+\frac a2u^2.
\]
Their images are respectively \([0,1/2]\) and \([1/2,1]\). The associated expanding two-branch map \(f_a\) has branches \(g_{a,0}^{-1}\) and \(g_{a,1}^{-1}\). Its reversible triangular extension is \(F_a(x,y)=(f_a(x),g_{a,j}(y))\), where \(j=0\) on \(x<1/2\) and \(j=1\) on \(x>1/2\). Arbitrary choices at partition endpoints do not affect the natural probability measure.

The expanding map preserves Lebesgue probability because \(g_{a,0}'(x)+g_{a,1}'(x)=1\). The **canonical conditional law at the null point \(X=0\)** is defined directly, without ambiguities of almost-everywhere disintegration: start a backward branch chain from \(X_0=0\). Given \(X_{k-1}=x\), draw \(B_k=j\) with probability \(g_{a,j}'(x)\), then set \(X_k=g_{a,j}(x)\). Let
\[
Y_a=\lim_{m\to\infty}g_{a,B_1}\circ g_{a,B_2}\circ\cdots\circ g_{a,B_m}(0).
\]
Both branches have Lipschitz constant at most \(\lambda<1\), so the limit exists for every branch sequence. The chain is the continuous-at-zero backward disintegration of the Lebesgue-stationary expanding map; its stable-coordinate law is the canonical boundary conditional of the natural triangular extension. No assertion is made that conditioning on an ordinary event of probability zero is unique without this construction.

## Proof
**1. Valid backward probabilities and boundary conditional.** We have
\[
 g_{a,0}'(x)=\lambda-ax,\qquad g_{a,1}'(x)=\frac{1-a}{2}+ax,
\]
so both derivatives lie in \([(1-a)/2,\lambda]\) and sum to one. Since the base invariant density is one, these are exactly the reverse-transition probabilities. The chain determines a unique nested stable-coordinate limit. Because the transition probabilities and branches are continuous and the stable maps contract uniformly, this construction is the canonical continuous version of the conditional distribution at \(X=0\).

**2. Exact cylinder masses.** The leftmost stable-coordinate cylinder of length \(n\) is \(g_{a,0}^{\circ n}([0,1])=[0,y_n]\). Except for partition endpoints, it is selected exactly when \(B_1=\cdots=B_n=0\). An individual infinite branch sequence has probability at most \(\lambda^m\) through its first \(m\) symbols, hence the endpoints have zero conditional mass. Along an all-zero backward history starting at \(X_0=0\), every earlier base point remains zero because \(g_{a,0}(0)=0\), and each left-branch probability equals \(g_{a,0}'(0)=\lambda\). Consequently \(R_a(y_n)=\lambda^n\) exactly.

**3. Reciprocal near-parabolic dynamics.** Put \(\delta=1-a\), \(\lambda=1-\delta/2\), \(b=a/2\), and \(v_n=\delta/y_n\). The exact recurrence \(y_{n+1}=\lambda y_n-b y_n^2\) becomes
\[
 v_{n+1}=\lambda^{-1}v_n+
 \frac{\delta b}{\lambda^2}\frac{1}{1-(b/\lambda)y_n}.
\]
For \(a\ge1/2\), \(y_n\le4/(n+4)\): indeed \(1/y_{n+1}-1/y_n\ge b\ge1/4\). Since \(0\le(b/\lambda)y_n\le1/2\), replacing the last factor in the recurrence by one incurs an accumulated error bounded by \(C_T\delta\sum_{j\le T/\delta}y_j\le C_T'\delta\log(1/\delta)\), uniformly for \(n\delta\le T\), after accounting for the bounded geometric weights \(\lambda^{-n}\).

The resulting linear recurrence has the exact solution
\[
 v_n^{\mathrm{lin}}=\delta\lambda^{-n}+\frac{a}{\lambda}(\lambda^{-n}-1).
\]
For each fixed \(t>0\), \(n=\lfloor t/\delta\rfloor\) therefore satisfies
\[
 v_n\to e^{t/2}-1,\qquad
 y_n/\delta\to(e^{t/2}-1)^{-1}.
\]
These convergences are uniform when \(t\) ranges over a compact subset of \((0,\infty)\).

**4. CDF limit.** For \(z>0\), choose \(t(z)=2\log(1+1/z)\). For any fixed \(0<\eta<t(z)\), the indices \(n_\pm=\lfloor(t(z)\pm\eta)/\delta\rfloor\) satisfy \(y_{n_+}<\delta z<y_{n_-}\) for all sufficiently small \(\delta\). Hence \(\lambda^{n_+}\le R_a(\delta z)\le\lambda^{n_-}\). First let \(\delta\downarrow0\), then \(\eta\downarrow0\); both bounds approach \(e^{-t(z)/2}=z/(1+z)\). At \(z=0\), the conditional measure has no atom at zero because \(\Pr\{B_1=\cdots=B_n=0\}=\lambda^n\to0\) for each fixed \(a<1\). Since the limit CDF is continuous, monotonicity upgrades convergence to uniform convergence on every compact \(z\)-interval. The limit distribution has density \((1+z)^{-2}\), completing the proof.

## Verification
`verify.py` checks exact rational branch identities and the reciprocal update, and tests finite-parameter cylinder-mass brackets at several shrinking \(\delta\) values against the theoretical limit. Running `python verify.py` on the embedded source returns `VERIFY_OK`. The convergence for all \(z\) and all \(a\uparrow1\) is proved analytically above; the numerical tests are supplementary.

## Relationship to prior work
Basios, Forti and Gilbert introduced the anti-symmetric cusp triangular map, its inverse branches, and the sequence of leftmost cylinders. Their 2008 preprint and 2009 journal article identify the intermittent endpoint and provide the identity corresponding to \(R_a(g_{a,0}^{\circ n}(1))=\lambda^n\), but do not obtain the scaled boundary conditional law \(z/(1+z)\). Their 2014 corrigendum shows that the natural planar invariant measure is generally **not** absolutely continuous; the present proof uses the canonical conditional distribution and does not rely on the superseded planar-density assertion. General parabolic-iteration arguments explain the reciprocal scaling mechanism, but the present assertion additionally uses the exact symbolic cylinder probabilities of this particular reversible extension.

## Limitations
This concerns a canonical boundary conditional distribution, not the distribution for an arbitrary point \(x>0\), the whole invariant planar measure, or a planar density. No local derivative of the conditional CDF at the endpoint is asserted for fixed \(a<1\); singularity and possible fine-scale oscillations at fixed parameter are not excluded. The law is weak convergence on the parameter-dependent \(y\sim1-a\) scale and does not establish convergence of unbounded moments. Absolute historical priority cannot be certified from indexed sources alone.

## References
1. V. Basios, G. L. Forti, and T. Gilbert, *Statistical properties of time-reversible triangular maps of the square*, first public arXiv posting 2008-12-09, arXiv:0812.1648; *J. Phys. A: Math. Theor.* **42** (2009), 035102, DOI:10.1088/1751-8113/42/3/035102.
2. V. Basios, G. L. Forti, and T. Gilbert, *Corrigendum: Statistical properties of time-reversible triangular maps of the square*, *J. Phys. A: Math. Theor.* **47** (2014), 489501, published 2014-11-06, DOI:10.1088/1751-8113/47/48/489501.
