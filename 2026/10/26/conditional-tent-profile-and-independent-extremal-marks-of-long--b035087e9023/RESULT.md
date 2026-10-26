# Conditional tent profile and independent extremal marks of long root gaps

## Finding

Let \(T_j\), \(j=-1,0,\ldots,n+2\), be independent rate-one exponential first-arrival clocks, and set \(U_j=1-e^{-T_j}\). For \(n\ge1\), let \(E_n\) be the event that sites \(0\) and \(n+1\) are strict local minima among their two immediate neighbors, and that none of \(1,\ldots,n\) is a strict local minimum. On \(E_n\), the interior has a unique maximum at \(K_n\in\{1,\ldots,n\}\). Let \(H_n:[0,1]\to[0,1]\) interpolate linearly through the points \((j/(n+1),U_j)\), \(j=0,\ldots,n+1\).

**Joint conditional shape-and-mark theorem.** As \(n\to\infty\), under the conditional law given \(E_n\),

\[
\|H_n-h\|_\infty\longrightarrow0\quad\text{in probability},\qquad h(x)=2\min\{x,1-x\},
\]

and, jointly,

\[
\left(nT_0,\ nT_{n+1},\ \frac{K_n-(n+1)/2}{\sqrt n},\ T_{K_n}-\log n\right)
\ \Longrightarrow\ (E_L,E_R,Z,G),
\]

where \(E_L,E_R\) are independent exponential variables of rate \(1/2\), \(Z\) is centered normal with variance \(1/4\), \(G\) has standard Gumbel distribution \(\Pr(G\le x)=\exp(-e^{-x})\), and **all four limits are mutually independent**. In particular, the two endpoint first-arrival times have scale \(2/n\), while the interior peak first-arrival time has scale \(\log n\), and the peak location has fluctuations of order \(\sqrt n\).

There is also an exact finite-length mark law. Write \(m\in\{0,\ldots,n-1\}\), \(q=n-1-m\), and define

\[
F_n(m)=\frac{n}{(m+1)(q+1)}\left[
\frac1{n+2}-\frac1{n+3}\left(\frac1{m+2}+\frac1{q+2}\right)
+\frac1{(n+4)(m+2)(q+2)}\right].
\]

Then

\[
\Pr(K_n=m+1\mid E_n)=
\frac{\binom{n-1}{m}F_n(m)}{\displaystyle\sum_{j=0}^{n-1}\binom{n-1}{j}F_n(j)},
\qquad
\sum_{m=0}^{n-1}\binom{n-1}{m}F_n(m)
=\frac{n2^{n+1}}{(n+1)(n+2)(n+4)}.
\]

The denominator identity agrees with the previously published probability of a gap of length \(n+1\); the *marked* conditional law and four-way joint limit are the assertions evaluated here.

## Assumptions and scope

The first-arrival clocks are independent and identically distributed, continuous, with rate one; the monotone probability-integral transform makes the \(U_j\) independent uniforms on \((0,1)\). The local event uses at least five sites indexed \(-1,0,1,\ldots,n,n+1,n+2\); a finite cyclic deposition strip may be used whenever these indices are distinct modulo its size (for example, circumference at least \(n+4\)). There is no requirement to let the circumference and gap length vary at a prescribed joint rate. The marks are conditional on a **specified oriented consecutive-root gap**, not on a randomly size-biased gap picked from the collection of all gaps. The time statements refer to independent Poissonized site clocks; the combinatorial root event depends only on their order.

A root is a site with an arrival earlier than both neighbors, equivalently a strict local minimum of the first-arrival clock field. The event \(E_n\) is precisely that sites \(0\) and \(n+1\) are consecutive roots in the oriented arc between them.

## Proof

**1. Unimodal disintegration.** The deterministic valley criterion of Matijasevick (Lemma 4.1) says that, when the endpoints are valleys and the interior contains no valley, the sequence \(U_1,\ldots,U_n\) increases strictly to its maximum and then decreases strictly. Write \(A_n\) for this interior unimodality event. Relative interior ranks are uniform, hence \(\Pr(A_n)=2^{n-1}/n!\). Conditional on \(A_n\), the maximum \(M=\max_{1\le j\le n}U_j\) has density \(nt^{n-1}\), independent of the left/right assignment of the other \(n-1\) values. Each of those values chooses the left side with probability \(1/2\), independently; values are sorted increasingly on the left and decreasingly on the right. Thus the number \(B=K_n-1\) on the left has law \(\operatorname{Bin}(n-1,1/2)\), independent of \(M\). Conditional on \(B=m\), the \(m\) left and \(q=n-1-m\) right relative values are independent uniforms on \((0,M)\).

Let \(S_L=U_1\), \(S_R=U_n\). Given \(M,B=m\), they are \(M V_m\) and \(M V_q'\), where the \(V\)'s are independent minima of the indicated numbers of independent uniforms on \((0,1)\), with the convention \(V_0=1\). Their moments are

\[
\mathbb E V_m^k=\frac{k!\,m!}{(m+k)!},\quad
\mathbb E M^k=\frac n{n+k}\qquad(k\ge0).
\]

These formulas also hold for the zero-count convention.

**2. Exact tilt and finite apex law.** Conditional on the interior sequence, the root inequalities at the left end require \(U_0<S_L\) and \(U_{-1}>U_0\). Since all these variables are uniform, integrating over \(U_0\) gives

\[
g(S_L)=\int_0^{S_L}(1-u)\,du=S_L-\tfrac12 S_L^2.
\]

The right-end conditions independently contribute \(g(S_R)\). Therefore the conditional law of the interior, given \(E_n\), is exactly the conditional law given \(A_n\) tilted by \(g(S_L)g(S_R)\). Taking the first and second moments in step 1 gives

\[
\mathbb E[g(S_L)g(S_R)\mid A_n,B=m]=F_n(m)
\]

with \(F_n\) as displayed in the finding. Bayes' formula gives the marked apex law. Summing the conditional weights, or integrating the excursion kernel in the cited primary paper, yields

\[
\mathbb E[g(S_L)g(S_R)\mid A_n]
=\frac{4n}{(n+1)(n+2)(n+4)}.
\]

This proves the exact denominator sum and \(\Pr(E_n)=n2^{n+1}/[(n+1)(n+2)(n+4)n!]\).

**3. Untilted joint limit and tent.** Under the conditional law given \(A_n\), binomial central limit theory gives

\[
\frac{B-(n-1)/2}{\sqrt n}\Longrightarrow N(0,1/4).
\]

Uniformly whenever \(m/n\to1/2\), the minimum-of-uniform survival identity \(\Pr(nV_m>x)=(1-x/n)^m\) implies \(nV_m\Rightarrow\operatorname{Exp}(1/2)\); likewise, independently, for \(q\). Because \(M\) is independent of \(B\) and of the normalized relative values, \(n(1-M)\Rightarrow\operatorname{Exp}(1)\) is independent of these three limits. Conditioning on central \(m\) values and using the uniformity of these convergence bounds gives their joint independence. Binomial large-deviation bounds dispose of \(m/n\) away from \(1/2\).

For the interpolated profile, conditional on \(B=m,M\), each slope's array consists of sorted independent uniforms, so the uniform empirical-distribution law shows that the left slope is uniformly close to \(Mj/m\) and the right slope uniformly close to its reversed counterpart. Since \(B/n\to1/2\) and \(M\to1\), \(\|H_n-h\|_\infty\to0\) in probability under \(A_n\), with endpoint values here temporarily set to zero.

**4. Transfer through the rare-gap tilt.** Under \(A_n\), define \(X_{n,L}=n S_L\) and \(X_{n,R}=n S_R\). The previous step yields jointly

\[
(X_{n,L},X_{n,R},\ (B-(n-1)/2)/\sqrt n,\ n(1-M))
\Longrightarrow (X_L,X_R,Z,W),
\]

where \(X_L,X_R\) are independent rate-\(1/2\) exponentials, \(Z\sim N(0,1/4)\), \(W\sim\operatorname{Exp}(1)\), and all are independent. Moreover

\[
n^2 g(S_L)g(S_R)\Longrightarrow X_LX_R,
\qquad
\mathbb E[n^2g(S_L)g(S_R)]\longrightarrow4.
\]

The exact expectation from step 2 proves the second limit. Since the weights are nonnegative, convergence in distribution together with convergence of their expectations to \(\mathbb E[X_LX_R]=4\) ensures uniform integrability of the weights. Thus conditional expectation of any bounded continuous function of the four variables and of the profile equals its \(A_n\)-expectation tilted by these weights and tends to expectation tilted by \(X_LX_R/4\). The tilt acts solely on \(X_L,X_R\): it makes those variables independent \(\operatorname{Gamma}(2,\text{rate }1/2)\), leaving \(Z,W\) independent and unchanged. It also transfers the tent law, as the total weight is uniformly integrable.

**5. Boundary times and the peak time.** Given the interior and \(E_n\), the endpoint \(U_0\) has density \((1-u)/g(S_L)\) for \(0<u<S_L\); the right endpoint has the analogous conditional density, independent of the left endpoint. Because \(S_L,S_R\to0\) under \(E_n\), the normalized ratios \(U_0/S_L,U_{n+1}/S_R\) converge jointly to independent \(\operatorname{Unif}(0,1)\) variables, independent of the limiting interior marks. If \(V\) is uniform and \(X\) is independent \(\operatorname{Gamma}(2,\text{rate }1/2)\), then \(VX\) is \(\operatorname{Exp}(1/2)\) (integrate the gamma density over \(x>t\)). Hence \(nU_0,nU_{n+1}\) converge jointly to independent rate-\(1/2\) exponentials, independent of \(Z,W\). Since \(-\log(1-u)=u+O(u^2)\) at zero, the same limit holds for \(nT_0,nT_{n+1}\).

Finally \(T_{K_n}=-\log(1-M)\), so

\[
T_{K_n}-\log n=-\log[n(1-M)]\Longrightarrow -\log W.
\]

For \(W\sim\operatorname{Exp}(1)\), the last quantity has standard Gumbel law. The independence of all four limiting marks and the full conditional profile convergence now follow.

## Verification

The standalone standard-library script `gap_shape_verifier.py` reconstructs the conditional weighting formula using exact rational moments, verifies the published gap probability identity independently for \(n=1,\ldots,100\), checks symmetry and strict positivity for all \(5{,}050\) apex weights in those lengths, and evaluates the exact conditional variance and first endpoint moment at six lengths. In particular, \(\operatorname{Var}(K_n)/n\) approaches \(1/4\) and \(n\mathbb E[U_0\mid E_n]\) approaches \(2\), the moments predicted by the limiting normal and exponential distributions. The infinite limits above are proved analytically, not inferred from these finite checks. The run output is in `gap_shape_verifier_output.txt`.

## Relationship to prior work

Matijasevick (arXiv:2610.21094v1, 15 October 2026) proves the identification of deposition roots with local minima, an excursion kernel, the unmarked gap probabilities and Gaussian/Poisson limits for **counts** of gaps. Lemma 4.1 and Lemma 4.2 of that paper are directly used. Neither its statements on counts nor its excursion probability formula give the conditional four-dimensional marked limit, endpoint times or a tent profile; the disintegration, size-biased endpoint tilt and joint asymptotic independence are the substantive additions here. Mansour, Rastegar and Roitershtein (2019) establish earlier root-count formulas. Billey, Burdzy and Sagan (2013) enumerate permutations with specified peak sets; the relative-order enumeration accounts for the unmarked gap probability but not for the distribution of actual continuous first-arrival values. Existing results on uniform order statistics and binomial central limits are standard inputs and are not claimed as original.

## Limitations

The result conditions on a specific long oriented gap, not on the globally longest gap or on a typical gap chosen from a random collection; these sampling operations can reweight marks. It treats independent, identically distributed continuous first arrivals (or independent rate-one exponential clocks before uniformization). It does not give finite-\(n\) error rates for the joint convergence or a full process-level fluctuation theorem around the deterministic tent. The source's general interval-count limit theorems are not new claims here. Potential historical overlap with conditional permutation-mountain profiles under other terminology remains an open priority check for independent review.

## References

1. M. Matijasevick, *Gaps between roots in ballistic deposition on a strip: linear variance, Gaussian limits and a Poisson regime*, arXiv:2610.21094v1 (first public 2026-10-15), https://arxiv.org/html/2610.21094 . Sections 2, 4 (especially Lemmas 4.1–4.2, Theorem 4.3), and 6 were inspected.
2. T. Mansour, R. Rastegar, and V. Roitershtein, *On ballistic deposition process on a strip*, Journal of Statistical Physics 177 (2019), pp. 626–650, open text https://pmc.ncbi.nlm.nih.gov/articles/PMC6913540/ . Preprint arXiv:1903.12548.
3. S. Billey, K. Burdzy, and B. E. Sagan, *Permutations with Given Peak Set*, Journal of Integer Sequences 16 (2013), Article 13.6.1, https://www.maths.tcd.ie/EMIS/journals/JIS/VOL16/Billey/billey2.pdf .
