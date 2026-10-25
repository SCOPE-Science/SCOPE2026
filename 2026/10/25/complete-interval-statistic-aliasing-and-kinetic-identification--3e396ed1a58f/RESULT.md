# Complete interval-statistic aliasing and kinetic identification in reset coagulation

## Finding

An infinite one-dimensional nearest-neighbour coagulation--diffusion process, independently reset at rate \(r>0\) to a fresh Bernoulli configuration of occupation probability \(p\in(0,1)\), has the following exact inverse-data structure when the per-neighbour particle hopping rate \(D>0\) is known.

Write \(q=1-p\), and let \(\lambda\in(0,1)\) be the unique root of
\[
\lambda+\lambda^{-1}-2=\frac{r}{2D}.
\]
For every integer \(n\ge0\), the stationary probability \(E_n\) that a specified block of \(n\) consecutive sites is empty is invariant under exchanging \(\lambda\) and \(q\). More explicitly, for \(\lambda\ne q\),
\[
E_n=\frac{\lambda^{n+1}(1-q)^2-q^{n+1}(1-\lambda)^2}{(\lambda-q)(1-\lambda q)},
\]
and for \(\lambda=q=s\),
\[
E_n=\frac{s^n[(n+1)(1-s)+2s]}{1+s}.
\]
Thus even *all* stationary contiguous-empty-block probabilities, and the nearest-neighbour interparticle-gap distribution they determine, cannot distinguish the two parameter pairs \((\lambda,q)\) and \((q,\lambda)\).

Let \(u=\mathbb E\eta_0\) denote the stationary occupation density and \(v=\mathbb E(\eta_0\eta_1)\) the adjacent occupied-pair probability. Their exact realizability region is
\[
0<u<1,\qquad \frac{4u^3}{(1+u)^2}\le v<u^2.
\]
Every interior data pair corresponds to *exactly two* physically different parameter pairs, interchanged as above. Equality at the lower boundary gives *exactly one* pair, with \(\lambda=q\).

Now let \(C(t)=\mathbb E[\eta_0(0)\eta_0(t)]\) in the stationary process and define the normalized initial decorrelation rate
\[
m=-\frac{C'(0+)}{u}.
\]
It satisfies \(m=2D+r(1-p)\). The observable pair \((u,m)\) identifies \((p,r)\) **uniquely**, with the complete sharp realizability region
\[
0<u<1,\qquad m>2D.
\]
No nontrivial interchangeable pair has the same initial decorrelation rate. Consequently one kinetic slope removes an ambiguity that arbitrarily many stationary contiguous-interval measurements cannot remove.

## Assumptions and scope

The sites are indexed by \(\mathbb Z\). Each site is either empty or contains one particle; each occupied site attempts to hop to each nearest neighbour at rate \(D>0\). It vacates its starting site upon a hop, and the hopping particle disappears if the destination was occupied. Independently, at the epochs of a rate-\(r\) Poisson process, the *entire* configuration is replaced by a new independent product-Bernoulli configuration with site occupation probability \(p\in(0,1)\). A fresh independent draw at each reset is essential for the stated two-time formula. Observations refer to the unique spatially translation-invariant stationary law. No particle injection between resets, hard-core branching or asymmetric hopping is assumed.

## Proof

**Existence and stationary empty intervals.** Coupling by the first common global reset yields a unique stationary process. Equivalently, with \(\mu_p\) the Bernoulli product law and \(S_t\) the unreset coagulation--diffusion semigroup, its law is \(r\int_0^\infty e^{-rt}\mu_p S_t\,dt\). The empty-interval equation of Durang--Henkel--Park gives, with \(t=r/(2D)\),
\[
E_{n+1}-(2+t)E_n+E_{n-1}=-t q^n,\quad n\ge1,\quad E_0=1,\quad\lim_{n\to\infty}E_n=0.
\]
The bounded homogeneous solution is a multiple of \(\lambda^n\), where \(\lambda+\lambda^{-1}-2=t\); a particular solution is a multiple of \(q^n\). Imposing \(E_0=1\) yields the displayed closed expression; the coincident-root formula follows by taking its ordinary continuous limit. The expression is unchanged by interchanging \(\lambda\) and \(q\), including at equality. The probability that two consecutive particles are exactly \(n\) bonds apart, with empty intermediate sites, is \(E_{n-1}-2E_n+E_{n+1}\). Thus the normalized nearest-gap distribution is likewise invariant.

**Exact static inverse and feasibility.** Inclusion--exclusion at one and two sites gives
\[
u=1-E_1=\frac{(1-\lambda)(1-q)}{1-\lambda q},\qquad
v=1-2E_1+E_2=u^2(1-\lambda q).
\]
Write \(z=v/u^2\). Necessarily \(0<z<1\) and \(\lambda q=1-z\). Moreover \((1-\lambda)(1-q)=u z\), so \(\lambda,q\) are exactly the two roots, with multiplicity, of
\[
\xi^2-[2-z(1+u)]\xi+(1-z)=0.
\]
Its discriminant is \(z[z(1+u)^2-4u]\). Hence the above static inequalities are necessary. Conversely, assume those inequalities. Then \(0<z<1\), the discriminant is nonnegative, the root product \(1-z\) and sum \(2-z(1+u)\) are positive, and the polynomial is positive at \(1\), where its value is \(uz>0\). Both roots therefore lie strictly between \(0\) and \(1\). Setting either root to \(\lambda\), the other to \(q\), then \(p=1-q\) and \(r=2D(1-\lambda)^2/\lambda\) gives every and only the stated preimages. At the lower boundary the two roots meet, with \(\lambda=q=(1-u)/(1+u)\). No other static preimages exist because \(E_1,E_2\) already fix the unordered root pair.

**Dynamic slope and global reconstruction.** For \(\eta_0=1\), hops originating at site \(0\) remove its occupation at total rate \(2D\); hops arriving at an already occupied site do not remove the original particle; a fresh reset leaves the site occupied with probability \(p\). Therefore the generator obeys
\[
\eta_0\,L\eta_0=-[2D+r(1-p)]\eta_0,
\]
which, upon stationary expectation, proves \(m=2D+r q\). For the two static preimages the difference of their normalized slopes is
\[
\frac{m(\lambda,q)-m(q,\lambda)}{2D}
=\frac{(q-\lambda)(\lambda+q-2\lambda q)}{\lambda q}.
\]
The second factor is strictly positive, so the slopes are unequal whenever the parameters are distinct.

In fact \((u,m)\) alone is globally identifying. For a fixed \(u\in(0,1)\), solving the density equation for \(q\) gives
\[
q(\lambda)=\frac{1-u-\lambda}{1-(1+u)\lambda},\qquad 0<\lambda<1-u.
\]
Its derivative is \(-u^2/[1-(1+u)\lambda]^2<0\). Both positive factors in
\[
\frac{m}{2D}-1=\frac{(1-\lambda)^2}{\lambda}\,q(\lambda)
\]
are strictly decreasing on that interval; their product runs continuously from \(+\infty\) to \(0\). Thus every \(m>2D\) gives one and only one \(\lambda\), hence one \(q,p,r\), and no value \(m\le2D\) is possible for strictly positive parameters. This proves all claims.

## Verification

Run `python check.py` using Python's standard library. The program checks 300 parameter pairs and their exact inverse roots, seven empty-block sizes per pair, the recurrence residual, exchange invariance, the kinetic-slope split, seven independently solved finite-truncation recurrences, four exact collision cases and five fixed-density monotonic scans. The mathematical proof establishes the infinite-lattice results; numerical checks do not substitute for that proof. The direct finite-truncation systems use a zero boundary at a large block length to check local values and are not claimed to be exact finite-ring dynamics.

## Relationship to prior work

Durang, Henkel and Park (arXiv:1309.2107, 2013) derive the empty-interval evolution with stochastic resetting and its stationary density, and discuss spatial interval and nearest-gap statistics. Their continuum exponential-reset formulas already imply an analogous exchange symmetry algebraically; neither the standard empty-interval recurrence nor that continuum forward model is claimed as new. The contribution here is the **complete discrete-lattice observation-fiber classification, sharp feasibility bounds, and a kinetic measurement that resolves the twofold aliasing globally**. Durang, Fortin and Henkel (arXiv:1012.4724, 2010) derive two-time functions for unreset coagulation, not this fresh-reset inverse problem. Shapoval and collaborators (arXiv:1801.09216, 2018) study reaction/diffusion crossover, chiefly on Bethe lattices, not the stated observation fiber.

## Limitations

The conclusion concerns a known hopping rate, fresh independent Bernoulli resets, and exact infinite-lattice stationary expectations and right derivatives. A reset repeatedly to one fixed quenched configuration need not have the stated two-time slope. Equal empty-block probabilities do not establish equality of all spatial multi-point functions. Finite observation windows, noisy finite-difference estimates of \(C'(0+)\), and unknown \(D\) introduce statistical or structural questions not settled here. The discrete-lattice symmetry is strongly suggested by known continuum formulas; an equivalent inverse classification elsewhere cannot be ruled out merely from a targeted literature search. Independent review has not been performed.

## References

1. X. Durang, M. Henkel, H. Park, *Statistical mechanics of the coagulation-diffusion process with a stochastic reset*, arXiv:1309.2107 (first submitted 2013-09-09), https://arxiv.org/abs/1309.2107.
2. X. Durang, J.-Y. Fortin, M. Henkel, *Exact two-time correlation and response functions in the one-dimensional coagulation-diffusion process by the empty-interval-particle method*, arXiv:1012.4724 (first submitted 2010-12-21), https://arxiv.org/abs/1012.4724.
3. D. Shapoval, M. Dudka, X. Durang, M. Henkel, *Crossover between diffusion-limited and reaction-limited regimes in the coagulation-diffusion process*, arXiv:1801.09216 (first submitted 2018-01-28), https://arxiv.org/abs/1801.09216.
