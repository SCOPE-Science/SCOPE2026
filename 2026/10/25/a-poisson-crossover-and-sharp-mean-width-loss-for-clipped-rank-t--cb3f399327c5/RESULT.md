# A Poisson crossover and sharp mean-width loss for clipped rank-two matroid polytopes

## Finding

Let integers \(p\ge1\), \(q\ge2\), and \(n=p+q\) be given. Partition the standard coordinate set into \(A\) with \(p\) elements and \(B\) with \(q\) elements, and define the rank-two matroid base polytope
\[
P_{p,q}=\operatorname{conv}\{e_i+e_j:i<j,\ \{i,j\}\not\subseteq A\}\subset\mathbb R^n.
\]
It is a lattice-path (Schubert) matroid polytope, obtained from the hypersimplex \(\Delta(2,n)\) by forbidding pairs entirely inside one initial parallel class. Both polytopes have intrinsic dimension \(d=n-1\). Let \(U\) be uniform on the Euclidean unit sphere of the zero-sum direction space, and set \(W_{p,q}(U)=\max_{x\in P_{p,q}}\langle U,x\rangle-\min_{x\in P_{p,q}}\langle U,x\rangle\).

For \(q\to\infty\) and any integer sequence \(p=p(q)\ge1\) with \(p/q\to c\in[0,\infty)\), put
\[
 b_q=\sqrt{2\log q}-\frac{\log\log q+\log(4\pi)}{2\sqrt{2\log q}},\qquad
 a_q=(2\log q)^{-1/2}.
\]
Let \(E_1,E_2,E_3\) be independent exponential random variables of mean one. Define
\[
H_c=-\log E_1-\log\min\{E_1+E_2,E_3/c\},
\]
where \(E_3/0=+\infty\); let \(H_c'\) be an independent copy. Then the following assertions hold.

**(i) Full directional-width crossover.**
\[
\frac{\sqrt d\,W_{p,q}(U)-4b_q}{a_q}\ \Longrightarrow\ H_c+H_c'.
\]
In particular, the fixed-class endpoint \(c=0\) is the sum of two independent copies of the *sum of the first two points* of a unit Gumbel Poisson process, while every finite \(c>0\) incorporates a competing extreme from the parallel class. The distribution of \(H_c\) has an explicit integral CDF: with \(v=e^{-x}\),
\[
\Pr(H_c\le x)=\int_0^{\sqrt v}\exp\!\left(-\frac{(1+c)v}{t}\right)dt
 +\int_{\sqrt v}^{\infty}\exp\!\left(-t-\frac{cv}{t}\right)dt.
\]

**(ii) Sharp mean-width expansion.** With \(\gamma_{\rm E}\) denoting Euler's constant,
\[
\mathbb E[\sqrt d\,W_{p,q}(U)]
=4b_q+a_q\left(4\gamma_{\rm E}+2\log(1+c)-\frac2{1+c}\right)+o(a_q).
\]
Consequently the sharp Euclidean mean-width penalty relative to the full hypersimplex in the *same* dimension is
\[
\boxed{\lim_{q\to\infty}\frac{\sqrt d}{a_q}
\left(\mathbb E W_{\Delta(2,n)}(U)-\mathbb E W_{p,q}(U)\right)
=2\left(\log(1+c)-\frac{c}{1+c}\right).}
\]
This limit is strictly positive for every \(c>0\), though the two polytopes have the same leading-order mean width.

**(iii) Exact normal-cone class mass.** For every finite \(p\ge1,q\ge2\), the probability that the almost surely unique vertex exposed by \(U\) uses a coordinate from \(A\) is exactly
\[
\boxed{1-\frac{q(q-1)}{(p+q)(p+q-1)}}.
\]
When \(p/q\to c\), it tends to \(1-(1+c)^{-2}\). This last finite identity holds for any exchangeable continuous coordinate score distribution, not just Gaussian scores, provided its ranking is uniform.

## Assumptions and scope

All coordinates use the unscaled standard Euclidean metric, and all widths refer to the intrinsic \((n-1)\)-dimensional Euclidean sphere. The affine span is \(\sum_i x_i=2\); its direction space is \(\{u:\sum_i u_i=0\}\). The asymptotics require \(q\to\infty\) and a *finite* limit \(c=p/q\); the theorem does not assert the same normalization when \(p/q\to\infty\). The quantity \(\gamma_{\rm E}\) is Euler's constant, not a shape parameter.

The given vertex set is precisely the set of bases of the rank-two lattice-path matroid whose upper bounding path has north-step positions \((1,p+1)\) and whose lower bounding path has north-step positions \((n-1,n)\). In particular it includes the rank-two Schubert matroids with one nontrivial parallel class. The affine dimension is \(n-1\): differences between allowed pair indicators span all coordinate differences, using any two distinct \(B\) coordinates and one \(A\) coordinate.

## Proof

**1. An exact finite support identity.** Given real scores \(g=(g_1,\ldots,g_n)\), write \(B_{(1)}\ge B_{(2)}\) for the two largest among the \(B\)-scores and \(A_{(1)}\) for the largest among the \(A\)-scores. Every allowed pair contains at least one \(B\) coordinate, hence
\[
h_{P_{p,q}}(g)=B_{(1)}+\max\{B_{(2)},A_{(1)}\}.
\]
Likewise, the minimum score is the sum of the least \(B\)-score and the minimum of the next \(B\)-score and the least \(A\)-score. Both statements follow by taking the best pair from the disjoint possibilities \(B\)-\(B\) and \(A\)-\(B\); no pair type is omitted. For Gaussian \(g\), the raw width is \(h_{P_{p,q}}(g)+h_{P_{p,q}}(-g)\).

**2. The exact exposed-class probability.** The highest two scores overall are both in \(B\) if and only if the maximizing allowed pair uses no \(A\) coordinate. Any other ordering forces its maximizing allowed pair to contain the highest \(A\)-score. Every ordering is equally likely under iid continuous scores. Therefore the probability of avoiding \(A\) is \(q(q-1)/(n(n-1))\). Subtracting gives assertion (iii). The radial projection used below subtracts a common coordinate mean, so this ranking event is unchanged when scores are replaced by intrinsic sphere directions.

**3. Gaussian extreme-point process.** Take iid \(g_i\sim N(0,1)\). The normal tail estimate yields, for each fixed real \(x\),
\[
q\Pr\{g_i>b_q+a_qx\}\longrightarrow e^{-x}.
\]
The positive standardized exceedance process of the \(q\) coordinates in \(B\) therefore converges to a Poisson process with intensity \(e^{-x}dx\). Its two greatest points have the joint representation
\[
X_1=-\log E_1,\qquad X_2=-\log(E_1+E_2).
\]
The positive process from \(A\) converges independently to intensity \(c e^{-x}dx\) for \(c>0\), with maximum \(Y_c=\log c-\log E_3\). At \(c=0\) the \(A\) process is empty on every bounded-above window; formally \(Y_0=-\infty\). Hence by the exact support identity,
\[
\frac{h_{P_{p,q}}(g)-2b_q}{a_q}\Longrightarrow X_1+\max\{X_2,Y_c\}=H_c.
\]
For negative exceedances the same argument applies to \(-g\). Upper and lower Gaussian exceedance point processes converge jointly to independent limits: for any bounded threshold windows an individual coordinate cannot satisfy both a positive and a negative extreme event, and the multinomial rare-event generating function factors in the limit. Independence across the disjoint \(A\) and \(B\) coordinate sets is exact. Consequently
\[
\frac{h_{P_{p,q}}(g)+h_{P_{p,q}}(-g)-4b_q}{a_q}
\Longrightarrow H_c+H_c',
\]
with independent copies as asserted.

**4. The explicit CDF.** Put \(v=e^{-x}\). The event \(H_c\le x\) is
\(E_1\min\{E_1+E_2,E_3/c\}\ge v\). Conditioning on \(E_1=t\), the probability is \(\exp[-\max\{v/t-t,0\}-cv/t]\). Multiplying by the \(e^{-t}\) density and splitting at \(t=\sqrt v\) gives the two integrals in (i). This calculation is valid at \(c=0\) by taking the displayed convention.

**5. From Gaussian to intrinsic Euclidean directions.** Let \(\Pi\) project orthogonally onto the zero-sum subspace and set \(R=\|\Pi g\|_2\). Then \(R\) has the \(\chi_d\) distribution and \(U=\Pi g/R\) is uniform on its unit sphere. Because every point of \(P_{p,q}\) has coordinate sum \(2\), widths are unchanged by subtracting the scalar mean of \(g\). Thus \(W_{p,q}(U)=\bigl(h_{P_{p,q}}(g)+h_{P_{p,q}}(-g)\bigr)/R\). Now \(R/\sqrt d=1+O_{\Pr}(d^{-1/2})\), the Gaussian raw width is \(O_{\Pr}(\sqrt{\log q})\), and \(d\ge q\). The replacement error after dividing by \(a_q\) is \(O_{\Pr}((\log q)/\sqrt q)=o_{\Pr}(1)\). This proves (i).

**6. First moments and the strict deficit.** The random variable \(e^{-\max\{X_2,Y_c\}}\) equals \(T_c=\min\{E_1+E_2,E_3/c\}\), with survival function \(e^{-(1+c)t}(1+t)\). Its density \(e^{-(1+c)t}\bigl(c+(1+c)t\bigr)\) is a mixture of an exponential and a shape-two Gamma distribution, both of rate \(1+c\), with weights \(c/(1+c)\) and \(1/(1+c)\), respectively. Therefore
\[
\mathbb E[-\log T_c]=\gamma_{\rm E}+\log(1+c)-\frac1{1+c},
\qquad \mathbb E[-\log E_1]=\gamma_{\rm E},
\]
so \(\mathbb E H_c=2\gamma_{\rm E}+\log(1+c)-1/(1+c)\). Uniform integrability follows by sandwiching each raw support score between the sums of the top two of the \(q\) \(B\)-Gaussians and of all \(n\) Gaussians: because \(n/q\to1+c<\infty\), both bounding standardized top-two sums have uniformly bounded fixed absolute moments. This last bound follows directly from Gaussian Mills inequalities, giving exponentially decaying positive tails and superexponentially decaying negative tails for the second maximum. The same holds for the negative-score support, so expectations converge at the claimed \(a_q\) scale.

The identity \(\mathbb E R\,\mathbb E W_{p,q}(U)=\mathbb E[h(g)+h(-g)]\) holds exactly, since radial length and angular direction are independent. Moreover \(\mathbb E R=\sqrt d(1+O(d^{-1}))\), and \(\sqrt{\log q}/d=o(a_q)\), yielding (ii)'s first expansion.

For \(\Delta(2,n)\), the raw Gaussian support is simply the sum of the largest two out of all \(n\) scores. Their standardized limiting mean is \(2\gamma_{\rm E}-1\); hence \(\mathbb E[\sqrt d W_{\Delta(2,n)}(U)]=4b_n+a_n(4\gamma_{\rm E}-2)+o(a_n)\). With \(\lambda=1+c\), \(b_n=b_q+a_q\log\lambda+o(a_q)\) and \(a_n=a_q+o(a_q)\). Subtraction gives \(2(\log\lambda-1+1/\lambda)\) and hence the boxed formula. Its derivative in \(c\) is \(2c/(1+c)^2>0\) for \(c>0\), establishing strict positivity.

## Verification

The accompanying standalone `CHECK.py` reconstructs all allowed pair-indicator vertices, compares direct support and width evaluations against the exact formula, exhausts finite label rankings for the class-contact probability, and tests the independent exponential limit representation against its analytic CDF and mean. Running `python CHECK.py` with NumPy passed 840 direct support/width tests, 15 exhaustive rank-probability identities, and 15 Poisson-process CDF checks. The Poisson limits and mean-width expansion are proved analytically above; seeded finite diagnostics alone do not certify infinite asymptotics.

## Relationship to prior work

The lattice-path matroid and base-polytope construction, including facet and integral structure, is established by An–Jung–Kim (2017), Knauer–Martínez-Sandoval–Ramírez Alfonsín (2017), and Benedetti–Knauer–Valencia-Porras (2023). The last paper treats rank-two lattice-path matroid \(h^*\)-vectors and decompositions but not Euclidean random-direction widths. Standard Gaussian Poisson extreme-value convergence supplies the probabilistic input here. The new evaluated quantities are the *shape-dependent continuous crossover law*, its exact class-contact mass, and the sharp second-order mean-width loss when a Schubert matroid polytope clips a hypersimplex. The known rank-two inradius, Minkowski-asymmetry, and basis-exchange graph spectral results concern different invariants and do not imply these width fluctuation statements. The previously considered complete-bipartite symmetric-edge polytope is centrally symmetric and its Gaussian support optimizes different signed edge pairs; its limiting distribution does not cover this clipped hypersimplex's correlated first/second-order-statistic competition.

## Limitations

The claim is for one nontrivial parallel class and the finite aspect-ratio window \(p/q\to c<\infty\); it does not treat arbitrary parallel-class profiles or the regime \(p/q\to\infty\). The Gaussian representation is a proof device; the spherical width statement is Euclidean. Numerical tests validate finite identities and limit diagnostics but not asymptotic quantifiers. Equivalent prior formulations in general Gaussian order-statistics or matroid-greedy literature remain a residual bibliographic risk; the novelty assertion is restricted to the geometric specialization and its evaluated sharp constants. No independent mathematical audit is asserted.

## References

1. S. An, J. Jung, S. Kim, *Facial structures of lattice path matroid polytopes*, arXiv:1701.00362, first public 2017-01-02.
2. K. Knauer, L. Martínez-Sandoval, J. L. Ramírez Alfonsín, *On lattice path matroid polytopes: integer points and Ehrhart polynomial*, arXiv:1701.05529, first public 2017-01-19.
3. C. Benedetti, K. Knauer, J. Valencia-Porras, *On lattice path matroid polytopes: alcoved triangulations and snake decompositions*, arXiv:2303.10458, first public 2023-03-18.
4. Classical Gaussian maximum point-process convergence: standard extreme-value theory for iid normal samples, here reconstructed directly from the Gaussian tail and multinomial rare-event limits.
