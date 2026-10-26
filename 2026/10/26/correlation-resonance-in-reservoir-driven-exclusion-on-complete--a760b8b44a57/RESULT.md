# Correlation resonance in reservoir-driven exclusion on complete bipartite networks

## Finding

For integers \(m,n\ge2\), let \(K_{m,n}\) have parts \(A\) and \(B\). Each undirected edge exchanges its endpoint occupations at rate one (an exchange has no effect when occupations agree). Vacant \(A\)-vertices receive particles at rate \(\alpha>0\), and occupied \(B\)-vertices lose particles at rate \(\beta>0\); there are no other changes. In the unique stationary state, write \(x=\mathbb E\eta_i\) for \(i\in A\), \(y=\mathbb E\eta_j\) for \(j\in B\), and \(d=x-y\). Then

\[
d=\left(1+\frac{n}{\alpha}+\frac{m}{\beta}\right)^{-1},\qquad
x=1-\frac{nd}{\alpha},\qquad y=\frac{md}{\beta}.
\]

The total directed stationary particle current from \(A\) to \(B\) is exactly \(J=mn d\). Set

\[
D=\alpha+\beta+\frac{(n-1)\beta}{m+\beta}+\frac{(m-1)\alpha}{n+\alpha}.
\]

For two **distinct** vertices, the complete stationary pair-covariance formula is

\[
\begin{aligned}
w&=\operatorname{Cov}(\eta_i,\eta_j)=-\frac{d^2}{D},&&i\in A,\ j\in B,\\
u&=\operatorname{Cov}(\eta_i,\eta_{i'})=\frac{n}{n+\alpha}w,&&i\ne i'\in A,\\
v&=\operatorname{Cov}(\eta_j,\eta_{j'})=\frac{m}{m+\beta}w,&&j\ne j'\in B.
\end{aligned}
\]

In particular, all off-diagonal occupations are strictly negatively correlated.

**Unique reservoir-speed optimum.** Keep the positive source-to-sink rate ratio fixed by setting \(\alpha=at\), \(\beta=bt\) with \(a,b>0\). Then the magnitude of the cross-part covariance \(|w(t)|\) tends to zero at both ends \(t\downarrow0\) and \(t\to\infty\), and has **exactly one** global maximum \(t_*\). Write

\[
C=\frac{n}{a}+\frac{m}{b},\qquad p=\frac{m}{b},\qquad q=\frac{n}{a},
\qquad
G(t)=a+b+\frac{n-1}{t+p}+\frac{m-1}{t+q}.
\]

Then \(|w(t)|=t/[(t+C)^2G(t)]\). Its unique maximizing rate is the unique positive zero of

\[
H(t)=(C-t)(a+b)
+(n-1)\frac{t(2C-p)+Cp}{(t+p)^2}
+(m-1)\frac{t(2C-q)+Cq}{(t+q)^2},
\]

and satisfies the strict threshold \(t_*>C\).

**Universal balanced scaling.** If \(m=n=k\) and \(a=b=1\), so \(\alpha=\beta=t\), then

\[
w(t)=-\frac{t(t+k)}{2(t+2k)^2(t+2k-1)}.
\]

Writing \(N=2k\), the unique maximizing rate and its peak covariance satisfy

\[
\boxed{\frac{t_*}{N}\longrightarrow\frac{1+\sqrt3}{2}},\qquad
\boxed{N\max_{t>0}|w(t)|\longrightarrow\frac{\sqrt3}{18}}.
\]

Thus the strongest nonequilibrium occupation anticorrelation occurs when the reservoir rate per site is proportional to network size, not when it is infinitely fast or infinitely slow.

For general balanced-density growing parts, the same crossover has an explicit exponent. Let \(N=m+n\), \(m/N\to s\in(0,1)\), and \(\alpha=aN^\gamma\), \(\beta=bN^\gamma\) for \(a,b>0\) and \(\gamma\ge0\). Define \(L=(1-s)/a+s/b\), \(K=a/(1-s)+b/s\). Then

\[
w\sim
\begin{cases}
-\dfrac{1}{L^2 K}\,N^{\gamma-2},&0\le\gamma<1,\\[2mm]
-\dfrac{1}{[1+L]^2}\left[a+b+\dfrac{(1-s)b}{s+b}+\dfrac{sa}{1-s+a}\right]^{-1}\!N^{-1},&\gamma=1,\\[2mm]
-\dfrac{1}{a+b}\,N^{-\gamma},&\gamma>1.
\end{cases}
\]

## Assumptions and scope

The model is a continuous-time Markov chain on \(\{0,1\}^{m+n}\). Each edge has its own unit-rate Poisson interchange clock. Each \(A\) site has an independent rate-\(\alpha\) addition clock, active only while vacant; each \(B\) site has an independent rate-\(\beta\) removal clock, active only while occupied. All rates are strictly positive; no thermodynamic assumptions are needed for the exact finite formulas. The covariance definition uses different vertices even when they belong to the same part. The graph sizes satisfy \(m,n\ge2\). The common-rate optimization varies \(t\) while keeping \(m,n,a,b\) fixed.

## Proof

**Stationarity and first moments.** Removal at \(B\), interchange along edges, and addition at \(A\) communicate with every occupation configuration, so the finite chain is irreducible and has a unique stationary law. Permutations within either graph part preserve its generator, making the expectations constant within a part. Applying its generator to \(\eta_i\) and \(\eta_j\) gives

\[
0=n(y-x)+\alpha(1-x),\qquad
0=m(x-y)-\beta y.
\]

Solving yields the expressions for \(d,x,y\). On one edge the net mean flux is \(\mathbb E[\eta_i(1-\eta_j)-\eta_j(1-\eta_i)]=x-y\), giving \(J=mn d\), which also equals total mean injection and removal.

**Second moments and closure.** Exchange dynamics cancel cubic terms in pair observables. For two different vertices of \(A\), stationarity of their covariance gives

\[
0=2n(w-u)-2\alpha u.
\]

For two different vertices of \(B\), it gives \(0=2m(w-v)-2\beta v\). For adjacent unlike vertices, the exchange on their shared edge contributes the drift-gradient term \(-d^2\), because exchanging two equal occupations is inert and exchanging unequal ones anticorrelates the increments. The exact equation is

\[
0=(m-1)(u-w)+(n-1)(v-w)-(\alpha+\beta)w-d^2.
\]

Consequently \(u=nw/(n+\alpha)\), \(v=mw/(m+\beta)\), and substitution into the third equation gives \(Dw=-d^2\). All denominators are positive, establishing strict negativity.

**The unique resonance.** Put \(\alpha=at\), \(\beta=bt\), and \(C=p+q\) as above. Algebra gives \(d=t/(t+C)\), \(D=tG(t)\), and hence \(|w|=t/((t+C)^2G(t))\). Its derivative has the sign of \(H(t)=(C-t)G(t)-t(t+C)G'(t)\), which simplifies to the displayed expression. Since \(0<p,q<C\), differentiating gives

\[
H'(t)=-(a+b)
-(n-1)\frac{(2C-p)t+p^2}{(t+p)^3}
-(m-1)\frac{(2C-q)t+q^2}{(t+q)^3}<0.
\]

Moreover \(H(C)>0\) and \(H(t)\to-\infty\). Thus there is one and only one critical point \(t_*>C\). As \(|w|\) vanishes at \(0\) and \(+\infty\), this point is the strict global maximum.

**Balanced constants and scaling.** Inserting \(m=n=k\) and \(\alpha=\beta=t\) gives the stated rational expression. With \(t=N\tau\) and \(N=2k\), uniformly on positive compact \(\tau\)-intervals,

\[
N|w(N\tau)|\longrightarrow F(\tau)=\frac{\tau(1+2\tau)}{4(1+\tau)^3},\qquad
F'(\tau)=\frac{1+2\tau-2\tau^2}{4(1+\tau)^4}.
\]

The unique positive root is \(\tau_*=(1+\sqrt3)/2\), and substitution gives \(F(\tau_*)=\sqrt3/18\). Derivative-sign convergence at any fixed points immediately below and above \(\tau_*\), together with unique finite-size critical points, forces \(t_*/N\to\tau_*\); uniform convergence then gives the peak limit. Finally the three general-rate regimes follow by inserting \(m/N\to s\) and the specified rates into the exact \(d\) and \(D\); at \(\gamma=1\) all leading contributions to \(D\) are order \(N\), whereas for \(\gamma<1\) and \(\gamma>1\) the displayed terms dominate.

## Verification

Run `python verify_reservoir_bipartite.py` using Python 3 and the standard library. The checker builds the **independent** bivariate occupation-count Markov generator on \((m+1)(n+1)\) states, solves its stationary equations with exact rational arithmetic, and compares the five analytical one- and two-point observables for 27 combinations of dimensions and rates. It additionally tests the strict optimizer against perturbed rates and the balanced scaling constants. Its recorded execution passed 168 checks. Analytical arguments, not these finite tests, establish the statements for arbitrary positive rates and graph sizes.

## Relationship to prior work

Mendonça (arXiv:1207.4106, first posted 2012-07-17) analyzes the SSEP spectrum on complete and complete bipartite graphs in **fixed-particle-number sectors**; that is the graph and interacting-particle background, not this open-system stationary observable. Landim, Milanés, and Olla (arXiv:math/0608165, first posted 2006-08-07) rigorously study stationary fluctuations in a **one-dimensional** reservoir-driven exclusion chain, using a Laplacian Green-function covariance. General exclusion-duality methods and related nonequilibrium correlation theory are established. The present result evaluates a different distributed-reservoir graph geometry and proves the all-rate unique cross-covariance maximum and balanced constant. No absolute historical priority or general-network uniqueness is claimed.

## Limitations

The result concerns equal unit edge-exchange rates and homogeneous within-part source and sink rates; noncomplete or weighted graphs, spatially heterogeneous reservoirs, current-counting noise, higher stationary cumulants, and dynamical mixing times are not determined. The nonmonotone optimization is for a fixed source-to-sink rate **ratio** and the magnitude of an unlike-part **stationary occupation covariance**, not for stationary transport current. Numerical checks verify examples only. Exhaustive priority verification is not claimed; broader general-graph results may subsume the evaluated covariance formula even if they do not print it explicitly.

## References

- J. Ricardo G. Mendonça, *Exact eigenspectrum of the symmetric simple exclusion process on the complete, complete bipartite, and related graphs*, arXiv:1207.4106 (2012), https://arxiv.org/abs/1207.4106.
- C. Landim, A. Milanés, S. Olla, *Stationary and Nonequilibrium Fluctuations in Boundary Driven Exclusion Processes*, arXiv:math/0608165 (2006), https://arxiv.org/abs/math/0608165.
