# Second-order locality breaking in many-walker cover times

## Finding

Let \(Q=(q(x,y))_{x,y\in V}\) be the generator of an irreducible continuous-time Markov chain on a **finite** state space \(V\), with rates \(q(x,y)\geq0\) for distinct states and exit rates \(\lambda(x)=-q(x,x)=\sum_{y\ne x}q(x,y)\). Fix an initial distribution \(\rho\), a nonempty target set \(U\subseteq V\), and \(N\) independent chains with initial law \(\rho\). Their union cover time is \(\sigma_N=\inf\{t\geq0:\text{every }u\in U\text{ has been visited by at least one chain by }t\}\).

Write \(d=\max_{u\in U}\operatorname{dist}(\operatorname{supp}\rho,u)\) for the maximum number of positive-rate jumps needed to reach a target, **assuming \(d\geq2\)**, and \(F=\{u\in U:\operatorname{dist}(\operatorname{supp}\rho,u)=d\}\). For any nonempty \(J\subseteq F\), define the first-hit path collections \(\mathcal P_k(J)\) as in the next section, and put

\[
\begin{aligned}
W_k(J)&=\sum_{(x_0,\ldots,x_k)\in\mathcal P_k(J)}\rho(x_0)\prod_{i=0}^{k-1}q(x_i,x_{i+1}),\\
L_d(J)&=\sum_{\pi=(x_0,\ldots,x_d)\in\mathcal P_d(J)}\rho(x_0)\prod_{i=0}^{d-1}q(x_i,x_{i+1})\sum_{i=0}^{d-1}\lambda(x_i),\\
A_J&=\frac{W_d(J)}{d!}>0,\qquad B_J=\frac{W_{d+1}(J)-L_d(J)}{(d+1)!}.
\end{aligned}
\]

For every **fixed real** \(m>0\), as the integer \(N\to\infty\),

\[
\boxed{\mathbb E[\sigma_N^m]=N^{-m/d}\bigl(K_m^{(0)}+N^{-1/d}K_m^{(1)}+o(N^{-1/d})\bigr),}
\]

where the two fully explicit finite sums are

\[
\begin{aligned}
K_m^{(0)}&=\Gamma(1+m/d)\sum_{\varnothing\ne J\subseteq F}(-1)^{|J|+1}A_J^{-m/d},\\
K_m^{(1)}&=-\frac{m}{d}\Gamma\!\left(\frac{m+d+1}{d}\right)\sum_{\varnothing\ne J\subseteq F}(-1)^{|J|+1}B_J A_J^{-(m+d+1)/d}.
\end{aligned}
\]

There is also a pointwise distributional correction: for each fixed \(x>0\),

\[
\begin{aligned}
\Pr\bigl(N^{1/d}\sigma_N>x\bigr)
={}&\sum_{\varnothing\ne J\subseteq F}(-1)^{|J|+1}e^{-A_Jx^d}\\
&-N^{-1/d}x^{d+1}\sum_{\varnothing\ne J\subseteq F}(-1)^{|J|+1}B_Je^{-A_Jx^d}+o(N^{-1/d}).
\end{aligned}
\]

**Locality-breaking corollary.** Suppose \(F=\{z\}\), and a new dead-end vertex \(w\) is connected bidirectionally to an existing vertex \(v\ne z\) by new rates \(q(v,w)=r>0\) and \(q(w,v)>0\), while all preexisting off-diagonal rates and the initial distribution are unchanged; \(w\notin U\) and has no initial mass. If \(v\) lies on a shortest positive-rate path of length \(d\) from \(\operatorname{supp}\rho\) to \(z\), then \(K_m^{(0)}\) is unchanged, whereas the second coefficient increases **strictly** by

\[
\boxed{\Delta K_m^{(1)}=\frac{mr}{d(d+1)!}\Gamma\!\left(\frac{m+d+1}{d}\right)A_{\{z\}}^{-(m+d+1)/d}W_v>0,}
\]

with \(W_v\) the total \(\rho\)-weighted product of rates over length-\(d\) paths to \(z\) that pass through \(v\). Thus the leading many-searcher universality cannot extend unchanged to the next order: a branch outside every shortest path can change the next coefficient.

For a completely explicit example, start all searchers at \(s\) on the unit-edge-rate tree with edges \(s-a\), \(s-b\), \(a-z\), and target \(U=\{b,z\}\). Without and with one additional non-target leaf \(w\) attached to \(a\), respectively,

\[
\boxed{\begin{aligned}
\mathbb E\sigma_N^{\mathrm{base}}&=\sqrt{\pi/2}\,N^{-1/2}+\frac43N^{-1}+o(N^{-1}),\\
\mathbb E\sigma_N^{\mathrm{leaf}}&=\sqrt{\pi/2}\,N^{-1/2}+\frac53N^{-1}+o(N^{-1}).
\end{aligned}}
\]

Both cover problems have two target vertices, and the additional leaf is not a target.

## Assumptions and scope

Here \(\operatorname{dist}(S,u)\) means the minimum length of a directed path from some \(s\in S\) to \(u\) along strictly positive rates. The finite irreducible chain makes every such distance finite. A \(k\)-jump first-hit path \(\pi=(x_0,\ldots,x_k)\in\mathcal P_k(J)\) has \(\rho(x_0)>0\), positive rates between consecutive distinct states, \(x_i\notin J\) for \(0\leq i<k\), and \(x_k\in J\). Such paths may revisit states outside \(J\). All sums are finite for each \(k\); no simple-path assumption is imposed at length \(d+1\). A shortest path of length \(d\) is necessarily simple. For \(J\subseteq F\), every state in \(J\) has distance \(d\), so \(\mathcal P_k(J)\) is empty for \(k<d\) and \(W_d(J)>0\).

The generator, initial distribution, target and real moment \(m>0\) remain fixed as \(N\to\infty\). Finite-state irreducibility supplies exponential tails for single-searcher hitting times; this condition is used to justify integration of the expansions.

## Proof

**1. Two-term small-time first hitting expansion.** Let \(\tau(J)\) be the first hit of \(J\) by one chain, and let \(F_J(t)=\Pr(\tau(J)\leq t)\). Since \(J\) is not charged by \(\rho\), killing the generator on \(J\) gives

\[
1-F_J(t)=\rho_{J^c}\exp(tQ_{J^c,J^c})\mathbf 1.
\]

This is analytic at zero. More concretely, condition on the successive states before the first visit to \(J\). A first-hit path of length \(k\) contributes the path-rate product times an integral over the \(k\) pre-jump holding intervals. The leading simplex volume is \(t^k/k!\). For a length-\(d\) path, expanding the exponential holding factors to first order contributes

\[
\frac{t^d}{d!}-\frac{t^{d+1}}{(d+1)!}\sum_{i=0}^{d-1}\lambda(x_i)+O(t^{d+2});
\]

length-\(d+1\) first-hit paths contribute \(t^{d+1}/(d+1)!+O(t^{d+2})\), and paths with at least \(d+2\) jumps contribute \(O(t^{d+2})\). The final holding interval after reaching \(J\) is not included, because the event is first hitting by time \(t\), not occupying \(J\) at time \(t\). Bounded finite-state jump rates control the remainder. Summing yields

\[
F_J(t)=A_Jt^d+B_Jt^{d+1}+O(t^{d+2}).
\]

**2. The farthest-target expansion.** Let \(\sigma_{N,F}\) be the time to cover \(F\) by the \(N\) searchers. Inclusion-exclusion and independence give the exact survival identity

\[
\Pr(\sigma_{N,F}>t)=\sum_{\varnothing\ne J\subseteq F}(-1)^{|J|+1}\bigl(1-F_J(t)\bigr)^N.
\]

Set \(\delta=N^{-1/d}\). Because \(d\geq2\), the term \(N F_J(\delta x)^2\) is \(O(N^{-1})=o(\delta)\) for fixed \(x\). Therefore

\[
\bigl(1-F_J(\delta x)\bigr)^N=e^{-A_Jx^d}\bigl(1-\delta B_Jx^{d+1}+o(\delta)\bigr)
\]

at each fixed \(x\geq0\), which proves the stated pointwise correction for \(\sigma_{N,F}\).

For moments, use \(\mathbb E Y^m=m\int_0^\infty t^{m-1}\Pr(Y>t)\,dt\). The small-time lower bound \(F_J(t)\geq c_Jt^d\) supplies a uniform integrable envelope on the rescaled range, while finite-state exponential hitting tails control the range away from zero. Splitting at a slowly growing rescaled cutoff, Taylor expansion under the integral gives

\[
\begin{aligned}
\mathbb E\bigl[\min_{1\leq i\leq N}\tau_i(J)\bigr]^m
={}&N^{-m/d}\bigg[\Gamma(1+m/d)A_J^{-m/d}\\
&-N^{-1/d}\frac{mB_J}{d}\Gamma\!\left(\frac{m+d+1}{d}\right)A_J^{-(m+d+1)/d}+o(N^{-1/d})\bigg],
\end{aligned}
\]

since \(\int_0^\infty x^{m+d}e^{-Ax^d}\,dx=\Gamma((m+d+1)/d)/(dA^{(m+d+1)/d})\). The finite inclusion-exclusion sum now gives both stated coefficients for \(\sigma_{N,F}\).

**3. Near targets are invisible through this order.** For \(u\in U\setminus F\), let \(r_u=\operatorname{dist}(\operatorname{supp}\rho,u)<d\), and choose any \(z\in F\). On the event that all far targets have been visited but \(u\) has not, at least one walker has visited \(z\) while all other walkers avoided \(u\). A union bound over that walker gives

\[
0\leq\Pr(\sigma_N>t)-\Pr(\sigma_{N,F}>t)
\leq\sum_{u\in U\setminus F}N F_{\{z\}}(t)\bigl(1-F_{\{u\}}(t)\bigr)^{N-1}.
\]

For \(r_u\geq1\), at small time \(F_{\{z\}}(t)\leq Ct^d\) and \(F_{\{u\}}(t)\geq c_ut^{r_u}\); hence the difference of \(m\)-th moments contributed over a fixed small interval is bounded by a constant times

\[
N\int_0^{t_0}t^{m+d-1}e^{-c(N-1)t^{r_u}}\,dt
=O\bigl(N^{-(m+d-r_u)/r_u}\bigr)
=o\bigl(N^{-(m+1)/d}\bigr).
\]

The last comparison follows from \(r_u\leq d-1\). If \(r_u=0\), then \(F_{\{u\}}(t)\geq\rho(u)>0\), making the small-time contribution exponentially small in \(N\). For \(t\geq t_0\), finite-state irreducibility yields an exponentially decaying single-walker avoidance tail, so its \(N\)-th power has exponentially small integrated moment. Thus \(\mathbb E\sigma_N^m-\mathbb E\sigma_{N,F}^m=o(N^{-(m+1)/d})\), and, at fixed rescaled time \(x>0\), the survival difference is exponentially small. This completes the main theorem.

**4. Pendant-branch effect.** When \(F=\{z\}\), the new pendant leaf creates no new first-hit paths of length \(d\) or \(d+1\) to \(z\): an excursion into and out of the leaf costs two additional jumps. It leaves all old path products unchanged but increases \(\lambda(v)\) by \(r\). Therefore \(A_{\{z\}}\) is unchanged and \(\Delta B_{\{z\}}=-rW_v/(d+1)!<0\). Substitution into \(K_m^{(1)}\) gives the strictly positive displayed change.

For the small tree example, the unique two-jump path is \(s,a,z\), so \(A_{\{z\}}=1/2\). Its pre-hit exit-rate sum is \(4\) in the baseline graph and \(5\) with the pendant leaf; there are no three-jump first-hit paths by bipartiteness. Thus \(B_{\{z\}}=-2/3\) or \(-5/6\). With \(m=1,d=2\), the formulas reduce to \(K_1^{(0)}=\sqrt{\pi/2}\) and \(K_1^{(1)}=-2B_{\{z\}}\), producing \(4/3\) and \(5/3\).

## Verification

Run \(\texttt{python3 checker.py}\) for exhaustive exact rational comparisons of first-hit path and killed-generator coefficients on connected small graphs, plus weighted asymmetric graphs and the explicit pendant example. The recorded result is **6,807 exact rational assertions passed**. Run \(\texttt{python3 numeric_example.py}\) for a separate, standard-library finite-\(N\) integration diagnostic. At \(N=10000\), the estimated \(N(\mathbb E\sigma_N-\sqrt{\pi/2}\,N^{-1/2})\) values are approximately \(1.34879037\) without the leaf and \(1.69337030\) with the leaf, approaching \(4/3\) and \(5/3\), respectively. These finite checks do not establish any of the infinite asymptotic assertions; their proofs are the four analytic steps above.

## Relationship to prior work

Kim and Lawley, *Cover times of many random walkers on a discrete network*, first publicly posted 2023-10-11 (arXiv:2310.07905), prove a leading \(N^{-m/d}\) moment law, with coefficient determined by shortest paths to the farthest targets. Their Section II derives inclusion-exclusion and first-order extreme-hitting asymptotics; their Sections III–V investigate that leading-scale geodesic locality. The present result retains the same basic model but supplies the next coefficient, a length-\(d+1\) first-hit/holding-rate formula, proof that nearer targets do not contribute at this order, and a strictly positive response to a new non-target pendant edge. It therefore isolates a precise limit to the leading geodesic-locality principle rather than claiming to rediscover the first-order theorem.

Lawley, *Extreme first-passage times for random walks on networks*, first publicly posted 2020-08-11 (arXiv:2008.04496), proves the leading fastest-hitting laws, including the limiting Weibull distribution and moments. The second-order expansion uses standard Taylor/Laplace asymptotics, but the general multivertex cover coefficient and pendant-edge locality-breaking comparison do not follow from a displayed second-order statement in those inspected sources. A complete historical-priority survey beyond the cited primary works has not been established.

## Limitations

The network is finite and irreducible, the initial and target sets are fixed, and the maximum target distance satisfies \(d\geq2\). The \(d=1\) case requires an additional order-\(N^{-1}\) binomial-logarithm correction and is not asserted. Countably infinite networks, diffusion limits, growing targets, dependent searchers, and nonexponential waiting laws are not covered. The displayed pendant response requires a unique farthest target, no initial mass at the new leaf, and a genuinely new dead-end vertex. The argument does not claim every possible off-geodesic perturbation increases the second coefficient, nor does it assert an optimal uniform-in-\(N\) error constant. Priority against all uncatalogued older extreme-value and phase-type asymptotic results remains a scientific risk.

## References

1. H. Kim and S. D. Lawley, *Cover times of many random walkers on a discrete network*, arXiv:2310.07905 (first posted 2023-10-11), later *Physical Review E* **109**, 014121 (2024). https://arxiv.org/abs/2310.07905
2. S. D. Lawley, *Extreme first-passage times for random walks on networks*, arXiv:2008.04496 (first posted 2020-08-11), later *Physical Review E* **102**, 062118 (2020). https://arxiv.org/abs/2008.04496
