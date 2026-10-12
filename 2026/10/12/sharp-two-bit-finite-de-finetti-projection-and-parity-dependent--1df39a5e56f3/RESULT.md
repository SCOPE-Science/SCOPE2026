# Sharp two-bit finite de Finetti projection and parity-dependent approximation radius

## Finding

Let \(P\) be any exchangeable probability law on \(\{0,1\}^2\). Write \(a=P(1,1)\), \(c=P(0,0)\), and \(P(1,0)=P(0,1)=(1-a-c)/2\). Let \(\mathcal E_\infty\) be the set of laws on two bits that are marginals of infinitely exchangeable binary sequences. Normalize total variation by \(d_{\mathrm{TV}}(P,Q)=\sup_E|P(E)-Q(E)|\), one half of the sum of absolute cellwise differences.

**Exact projection.** Suppose \(\operatorname{Cov}_P(B_1,B_2)<0\). Equivalently, \(\sqrt a+\sqrt c<1\). Put
\[
I=[\sqrt a,1-\sqrt c],\qquad q_*=\operatorname{proj}_I(1/2).
\]
Then
\[
\min_{Q\in\mathcal E_\infty} d_{\mathrm{TV}}(P,Q)
=q_*^2+(1-q_*)^2-a-c,
\]
and the **unique** minimizing two-bit law is \(Q=\operatorname{Bernoulli}(q_*)^{\otimes2}\). The representing mixing probability measure is uniquely the point mass at \(q_*\). Concretely, \(q_*=1-\sqrt c\) for \(c\ge1/4\), \(q_*=\sqrt a\) for \(a\ge1/4\), and \(q_*=1/2\) otherwise (the two endpoint conditions cannot both hold under the stated negative-covariance assumption). For a nonnegatively correlated exchangeable pair, the minimum is zero, since the law itself has an infinite exchangeable extension.

**Sharp finite-extension radius.** Let \(\mathcal E_N\) be the set of exchangeable two-bit laws extendible to an exchangeable \(N\)-bit law, for integers \(N\ge2\). Then
\[
\sup_{P\in\mathcal E_N}\min_{Q\in\mathcal E_\infty}d_{\mathrm{TV}}(P,Q)
=\begin{cases}
1/[2(N-1)],&N\text{ even},\\
1+1/N-\sqrt{1+1/N},&N\text{ odd}.
\end{cases}
\]
The maximum is attained by drawing two bits without replacement from an urn of \(N\) bits containing exactly \(\lfloor N/2\rfloor\) ones or, symmetrically, exactly \(\lceil N/2\rceil\) ones. This is the exact worst-case approximation radius for binary two-marginals in the stated total-variation normalization, not merely its asymptotic order. Its product-mixture minimizer has the above explicit parameter.

## Assumptions and scope

Every exchangeable binary pair admits the coordinates \((a,c)\) above with \(a,c\ge0\) and \(a+c\le1\). The marginal success probability is \(p=(1+a-c)/2\); hence the covariance equals \(a-p^2\). Negative covariance is equivalent to the strict inequality \(\sqrt a+\sqrt c<1\): if covariance is negative, then \(\sqrt a<p\) and \(\sqrt c<1-p\); conversely covariance nonnegative forces both reversed inequalities. Infinite extendibility of a pair means the existence of an infinite exchangeable sequence with exactly that two-coordinate law. It is equivalent, by the binary de Finetti representation, to the existence of a probability measure \(\mu\) on \([0,1]\) such that
\[
Q=\int\operatorname{Bernoulli}(\theta)^{\otimes2}\,d\mu(\theta).
\]
There is no requirement to preserve the original pair's one-coordinate marginal when approximating it; the optimization is over *all* infinite-exchangeable two-bit laws. The uniqueness statement concerns both the resulting law and its mixing measure in the negative-covariance regime.

## Proof

**1. Exact total variation on exchangeable pairs.** For a second exchangeable pair law \(Q\), write \(A=Q(1,1)\), \(C=Q(0,0)\). Evaluating all four atoms gives
\[
d_{\mathrm{TV}}(P,Q)=\frac{|A-a|+|C-c|+|(A+C)-(a+c)|}{2}.
\]
For \(Q\in\mathcal E_\infty\), let \(\Theta\) be distributed according to its mixing measure. Then \(A=\mathbb E\Theta^2\) and \(C=\mathbb E(1-\Theta)^2\). The triangle inequality in \(L^2\) yields
\[
\sqrt A+\sqrt C=\|\Theta\|_2+\|1-\Theta\|_2\ge\|1\|_2=1.
\]
Equality forces \(\Theta\) to be almost surely constant: for nonnegative \(\Theta\) and \(1-\Theta\), equality in the Hilbert-space triangle inequality entails proportionality, and their sum equals one.

**2. Eliminate opposite-sign endpoint errors.** Assume \(\sqrt a+\sqrt c<1\). The product law at parameter \(q=\sqrt a\) has first endpoint mass exactly \(a\), other endpoint mass \((1-\sqrt a)^2>c\), and distance \((1-\sqrt a)^2-c\). If an infinite-exchangeable competitor had \(A<a\), the previous inequality would force
\[
C\ge(1-\sqrt A)^2>(1-\sqrt a)^2,
\]
so its total variation distance would be at least \(C-c\), strictly larger than that admissible product law's distance. Symmetrically, any competitor with \(C<c\) is strictly worse than the product law at parameter \(q=1-\sqrt c\). Thus every minimizer has \(A\ge a\) and \(C\ge c\). In this quadrant the total variation formula becomes \(A+C-a-c\).

**3. Minimize the endpoint sum and prove uniqueness.** Write \(u=\sqrt A\), \(v=\sqrt C\). The necessary constraints are \(u\ge\sqrt a\), \(v\ge\sqrt c\), and \(u+v\ge1\). Every feasible point with \(u+v>1\) can lower at least one coordinate until \(u+v=1\) without violating its lower bounds; both lower bounds cannot simultaneously bind at a sum greater than one because \(\sqrt a+\sqrt c<1\). Hence the unique minimal endpoint-sum pair satisfies \(u+v=1\). Writing \(u=q\), the remaining minimization is
\[
\min_{\sqrt a\le q\le1-\sqrt c}\bigl(q^2+(1-q)^2\bigr).
\]
This strictly convex quadratic is uniquely minimized at \(q_*=\operatorname{proj}_{[\sqrt a,1-\sqrt c]}(1/2)\). The corresponding independent product law realizes these endpoints. Equality \(\sqrt A+\sqrt C=1\) for an optimizing mixture makes its mixing parameter almost surely constant, so no nontrivial mixture is a second optimizer. When covariance is nonnegative, \(a\ge p^2\) and \(c\ge(1-p)^2\); taking a mixing variable with mean \(p\) and variance \(a-p^2\) in the admissible Bernoulli moment interval produces \(P\) itself. An explicit construction is the mixture at \(0,p,1\), or equivalently the order-two truncated Hausdorff moment characterization.

**4. Reduce finite extendibility to fixed-count urns.** Any exchangeable \(N\)-bit vector is a mixture, indexed by its total number \(m\) of ones, of uniform permutations of exactly \(m\) ones and \(N-m\) zeros. Thus its two-bit marginal is a convex combination of laws \(P_{N,m}\) with
\[
a_m=\frac{m(m-1)}{N(N-1)},\qquad
c_m=\frac{(N-m)(N-m-1)}{N(N-1)}.
\]
Distance from a point to a convex set in a norm is a convex function of the point. Therefore its supremum over \(\mathcal E_N\) equals the largest of the finitely many distances for \(P_{N,m}\). The endpoint urns are already product laws, giving zero distance. All interior fixed-count urns have negative covariance
\[
\operatorname{Cov}(B_1,B_2)=-\frac{m(N-m)}{N^2(N-1)}<0.
\]

**5. The balanced urns are extremal.** By symmetry it suffices to examine \(0\le m\le N/2\). Here \(c_m\ge a_m\). If \(c_m\ge1/4\), the exact projection formula becomes, with \(z=(N-m)/N\),
\[
T_N(m)=2z-2\sqrt{\frac{z(Nz-1)}{N-1}}.
\]
As \(m\) increases, \(z\) decreases. The derivative with respect to \(z\) is
\[
2-\frac{2Nz-1}{\sqrt{(N-1)z(Nz-1)}}<0,
\]
where strict negativity follows by squaring the positive terms and using
\[
(2Nz-1)^2-4(N-1)z(Nz-1)=4z(Nz-1)+1>0.
\]
If \(c_m\le1/4\), then also \(a_m\le1/4\), the optimal parameter is \(1/2\), and
\[
T_N(m)=\frac{2m(N-m)}{N(N-1)}-\frac12,
\]
which is nondecreasing for \(m\le N/2\). The displayed expressions agree at \(c_m=1/4\); viewed as functions of a continuous interpolating \(m\) they are nondecreasing across the transition, hence also on the integer urns. This proves that \(m=\lfloor N/2\rfloor\) maximizes the distance, as does its reflected urn.

For even \(N\), the balanced urn has \(a=c=(N-2)/[4(N-1)]\), so \(q_*=1/2\) and \(T_N=1/[2(N-1)]\). For odd \(N\), the urn with \(m=(N-1)/2\) has \(a=(N-3)/(4N)\), \(c=(N+1)/(4N)\), so \(q_*=1-\sqrt{(N+1)/(4N)}\), yielding \(T_N=1+1/N-\sqrt{1+1/N}\). This proves the stated sharp radius for every integer \(N\ge2\).

## Verification

The included standalone `verification.py` uses rational arithmetic for the finite-urn masses and 65-digit decimal arithmetic for square roots and distances. Running `python verification.py` reproduced `VERIFY_OK urns=1323 cases=9240 parity=49 phases=3`. It compared the proposed projection against independent product and nontrivial two-point-mixture competitors on finite rational grids, verified the analytic even/odd radius formulas for every integer \(2\le N\le50\), and checked the three parameter regimes. These finite tests are regression evidence; the preceding proof establishes the universal assertions.

## Relationship to prior work

Carlier, Friesecke, and Vögler establish the extremal fixed-population representations for finitely exchangeable laws (Theorems 4.1–4.2 and the binary specialization of formula (4.7), arXiv:2106.09101v1). This is the finite-urn premise used in Step 4; their correlated-correction formulas and order bounds do not give the total-variation projection of a negatively correlated binary pair onto the full class of infinitely extendible pairs, nor the optimal parity-dependent finite-extension radius in that metric.

Diaconis and Freedman's classical finite de Finetti theorem provides uniform bounds using the sampling-with-versus-without-replacement coupling. The later full-text treatments by Volfovsky and Airoldi, and by Gavalakis, Johnson, and Kontoyiannis, present those statements as generic bounds (and, in the latter case, relative-entropy bounds), rather than the exact binary two-coordinate minimax radius and unique closest mixing measure. Some of these works adopt a total variation convention twice the present one, and their bounds must be rescaled before comparisons. The optimized parameter here generally differs from the empirical urn frequency: for the one-success three-ball urn it is \(1-1/\sqrt3\) rather than \(1/3\).

## Limitations

This result addresses two-coordinate binary marginals only, with approximation permitted to change the one-coordinate mean. It does not establish a corresponding projection for three or more coordinates, arbitrary finite alphabets, relative entropy, or the mean-preserving projection problem. The proof is analytic and does not infer an infinite statement from finite experiments. The complete 1980 Diaconis–Freedman paper was not accessible for full-text comparison; its theorems as reproduced in later full-text papers concern universal bounds rather than this sharp binary projection, but that limited direct access remains a bibliographic uncertainty.

## References

1. G. Carlier, G. Friesecke, D. Vögler, *Convex geometry of finite exchangeable laws and de Finetti style representation with universal correlated corrections*, arXiv:2106.09101v1 (first posted 2021-06-16), Theorems 4.1–4.2 and formula (4.7). https://arxiv.org/abs/2106.09101
2. L. Gavalakis, O. Johnson, I. Kontoyiannis, *Finite de Finetti bounds in relative entropy*, arXiv:2407.12921v1 (2024-07-17), Sections 3–4 and 6–7. https://arxiv.org/abs/2407.12921
3. A. Volfovsky, E. M. Airoldi, *Sharp Total Variation Bounds for Finitely Exchangeable Arrays*, arXiv:1407.6092 (2014), Sections 1–2. https://arxiv.org/abs/1407.6092
4. L. Gavalakis and I. Kontoyiannis, *An Information-Theoretic Proof of a Finite de Finetti Theorem*, arXiv:2104.03882 (2021). https://arxiv.org/abs/2104.03882
5. P. Diaconis and D. Freedman, *Finite Exchangeable Sequences*, Annals of Probability 8 (1980), 745–764. DOI:10.1214/aop/1176994663.
