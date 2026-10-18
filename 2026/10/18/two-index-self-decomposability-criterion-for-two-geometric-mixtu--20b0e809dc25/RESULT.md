# Two-index self-decomposability criterion for two-geometric mixtures

## Finding

Consider a positive mixture of two nonidentical, zero-based geometric distributions. The mixture is always compound-Poisson, as is known more generally for geometric mixtures. The specific finding is a **complete finite test** for its stronger Bernoulli-thinning self-decomposability: for all parameters it suffices to evaluate two explicitly computable neighboring jump-measure defects. The failure indices, if any, form one consecutive interval; no parameter-independent cutoff on which defects suffice is possible.

Specifically, let \(0<q<r<1\) and \(0<w<1\), and put
\[
\Pr(X=k)=w(1-q)q^k+(1-w)(1-r)r^k\qquad(k=0,1,2,\ldots).
\]
Define
\[
t=\frac{w(1-q)r+(1-w)(1-r)q}{w(1-q)+(1-w)(1-r)},\qquad q<t<r,
\]
and for integers \(k\ge1\), define
\[
d_k=(1-q)q^k+(1-r)r^k-(1-t)t^k.
\]
Set
\[
x_* =\frac{\log\!\left(\frac{(1-q)\log(t/q)}{(1-r)\log(r/t)}\right)}{\log(r/q)},\quad
K=\{\max(1,\lfloor x_*\rfloor),\max(1,\lceil x_*\rceil)\}.
\]
Then \(X\) is discrete self-decomposable under **every** independent Bernoulli thinning if and only if \(d_k\ge0\) for both indices \(k\in K\). A duplicated index is tested only once. If the condition fails, all positive integer indices at which \(d_k<0\) are consecutive. In addition, for every integer \(B\ge1\), there are such mixtures with \(d_1,\ldots,d_B>0\) but \(d_k<0\) for some \(k>B\).

## Assumptions and scope

A zero-based geometric law with parameter \(s\in(0,1)\) assigns mass \((1-s)s^k\) at each integer \(k\ge0\). The mixture parameter \(w\) is strictly between zero and one. Interchanging the two geometric components allows the ordering \(q<r\) without loss. The pure-component limits are ordinary geometric laws and are self-decomposable, but they are not needed for the finite-index formula (whose logarithmic minimizer requires \(q<t<r\)).

For \(\alpha\in(0,1)\), Bernoulli thinning of an integer-valued variable \(Y\) means \(\alpha\circ Y=\sum_{j=1}^{Y}B_j\), where the \(B_j\) are independent Bernoulli variables of success probability \(\alpha\), independent of \(Y\). A law with generating function \(G\) is *discrete self-decomposable* here if for every \(\alpha\in(0,1)\) there exists a nonnegative integer-valued \(R_\alpha\), independent of a fresh copy of \(X\), such that \(X\stackrel d=\alpha\circ X+R_\alpha\). Equivalently, the analytic quotient \(G(z)/G(1-\alpha+\alpha z)\) must be a probability-generating function for every \(\alpha\in(0,1)\). This is ordinary independent thinning, not dependent counting or geometric infinite divisibility.

## Proof

**Generating function and jump measure.** Direct summation of both geometric components gives
\[
G(z)=\frac{(1-q)(1-r)}{1-t}\cdot\frac{1-tz}{(1-qz)(1-rz)}.
\]
The scalar is the required normalizer since \(G(1)=1\). Expanding the logarithms for \(|z|<1/r\),
\[
\log G(z)=\log G(0)+\sum_{k\ge1}\frac{q^k+r^k-t^k}{k}z^k.
\]
Set \(A_k=q^k+r^k-t^k\) and \(\nu_k=A_k/k\). Because \(r>t>q>0\), each \(A_k>0\), \(\sum_{k\ge1}\nu_k<\infty\), and normalization yields
\[
G(z)=\exp\!\left(\sum_{k\ge1}\nu_k(z^k-1)\right).
\]
This recovers compound-Poisson infinite divisibility, but that broader property is not asserted as new.

**Thinning criterion, proved directly.** We have \(A_k-A_{k+1}=d_k\), and \(A_k\to0\). Define \(g(z)=-(1-z)G'(z)/G(z)\). Then
\[
g(z)=-A_1+\sum_{k\ge1}d_kz^k.
\]
If every \(d_k\ge0\), telescoping gives \(\sum_{k\ge1}d_k=A_1\), so
\[
g(z)=\sum_{k\ge1}d_k(z^k-1).
\]
Fix \(0<\alpha<1\). Differentiating \(\log G(1-\beta+\beta z)\) with respect to \(\beta\) and integrating proves
\[
\log\frac{G(z)}{G(1-\alpha+\alpha z)}
=\int_\alpha^1\sum_{k\ge1}\frac{d_k}{\beta}
\left[(1-\beta+\beta z)^k-1\right]\,d\beta.
\]
For each \(\beta\), \((1-\beta+\beta z)^k\) is a binomial generating polynomial. The right side is an absolutely convergent compound-Poisson exponent with nonnegative jump masses, since \(\int_\alpha^1d\beta/\beta<\infty\) and \(\sum d_k=A_1<\infty\). Hence the quotient is a probability-generating function for every \(\alpha\), proving self-decomposability.

Conversely, suppose \(d_j<0\) for some \(j\ge1\). Writing \(\alpha=1-h\), analyticity near \(h=0\) gives
\[
\frac{G(z)}{G(h+(1-h)z)}=1+h\,g(z)+O(h^2).
\]
The coefficient of \(z^j\) is \(h\,d_j+O(h^2)<0\) for sufficiently small \(h>0\). Such a quotient cannot be a probability-generating function. Therefore self-decomposability is **equivalent** to \(d_k\ge0\) for every integer \(k\ge1\).

**Reduction to two indices.** Divide \(d_k\) by the positive quantity \((1-t)t^k\). Then \(d_k\ge0\) is equivalent to \(\Phi(k)\ge1\), where
\[
\Phi(x)=\frac{1-q}{1-t}\left(\frac qt\right)^x
+\frac{1-r}{1-t}\left(\frac rt\right)^x,\qquad x\in\mathbb R.
\]
The first base lies strictly below one and the second above one, so \(\Phi\) is strictly convex, tends to infinity at both ends of the real axis, and has a unique global minimizer. Solving \(\Phi'(x_*)=0\) yields exactly the displayed expression for \(x_*\). The minimum on the positive integers occurs at one of \(\max(1,\lfloor x_*\rfloor)\) or \(\max(1,\lceil x_*\rceil)\). This proves the two-index criterion. Strict convexity also makes \(\{x:\Phi(x)<1\}\) an interval, so its intersection with the positive integers is a consecutive (possibly empty) block.

**No universal initial-index cutoff.** For each integer \(N>10\), set
\[
q_N=1-\frac{10}{N},\quad r_N=1-\frac1{10N},\quad t_N=1-\frac3N,
\]
which satisfy \(0<q_N<t_N<r_N<1\). These parameters are realized by the unique positive mixture weight
\[
\lambda_N=\frac{t_N-q_N}{r_N-q_N},\qquad
w_N=\frac{\lambda_N(1-r_N)}{\lambda_N(1-r_N)+(1-\lambda_N)(1-q_N)}.
\]
For each fixed positive integer \(k\), direct limits give
\[
\lim_{N\to\infty}N\,d_k(q_N,r_N,t_N)=10+\tfrac1{10}-3=\tfrac{71}{10}>0.
\]
But with \(k_N=\lfloor N/3\rfloor\),
\[
\lim_{N\to\infty}N\,d_{k_N}(q_N,r_N,t_N)
=10e^{-10/3}+\tfrac1{10}e^{-1/30}-3e^{-1}<0.
\]
Indeed \(e^{10/3}>\sum_{j=0}^{4}(10/3)^j/j!=5153/243>20\) and \(e<3\), so the last limit is less than \(1/2+1/10-1=-2/5\). For any prescribed \(B\), choose sufficiently large \(N\) so all defects through \(B\) are strictly positive while \(d_{k_N}<0\). This completes the theorem.

## Verification

The supplementary `checker.py` uses exact rational arithmetic for all probability, logarithmic-jump, defect, and generating-function coefficient identities; its minimizer search is supplementary floating-point guidance only. It tested \(375\) rational parameter triples with \(99\) positive jump-intensity checks and \(180\) successive defect checks per triple, along with \(16\) exact generating-function coefficient comparisons each. Four further rational examples with \(N=90,180,360,720\) exhibited first defective indices \(16,32,64,129\), respectively. No finite computation is used to justify the universal conclusions; those follow from the analytical proof above.

A small exact witness is \(q=1/10\), \(r=99/100\), \(t=19/20\), and \(w=17/89\). It has \(d_1=131/2500>0\) but \(d_2=-6581/250000<0\), illustrating why a first-jump test is insufficient.

## Relationship to prior work

Steutel and van Harn (1979) introduced the discrete self-decomposability concept. Pakes (2022), Definition 2, describes the decreasing canonical-sequence criterion and explains that **general geometric mixtures are compound-Poisson**, so the unconditional infinite-divisibility portion is established prior literature. Bouzar (2021) studies quasi-geometric infinite divisibility, a different algebraic property. Nastić, Ristić and Miletić Ilić (2016) study a time-series model with two-geometric innovations under *dependent* Bernoulli counting, which differs from ordinary independent thinning. The present result is the explicit two-index reduction, contiguous-failure structure, and the absence of a universal low-order cutoff for the full, ordinary-thinning self-decomposability problem.

## Limitations

The result does not classify arbitrary mixtures of three or more geometric components, nor does it give a closed algebraic inequality involving only bounded-degree polynomials in the mixture parameters. Evaluating \(x_*\) uses real logarithms; its two neighboring integer indices provide a mathematically exact decision rule, while numerical implementations must control rounding near integers. The finite checker is not an independent proof of the all-parameter theorem. Earlier treatments of general geometric mixtures could contain an equivalent specialized finite test under different terminology; the 2025 article by Waza and Ahmad with an exactly matching object title was not available in full for comparison. No independent external audit has been performed.

## References

1. F. W. Steutel and K. van Harn, *Discrete analogues of self-decomposability and stability*, Annals of Probability **7** (1979), 893–899. DOI: 10.1214/aop/1176994950.
2. N. Bouzar, *Quasi-geometric infinite divisibility*, first public arXiv:2112.04105v1, 2021-12-08; primary MSC 60E07.
3. A. G. Pakes, *Mutant Number Laws and Infinite Divisibility*, Axioms **11** (2022), 584, especially Definitions 2 and 6 and Fact 9. DOI: 10.3390/axioms11110584.
4. A. S. Nastić, M. M. Ristić and A. V. Miletić Ilić, *A geometric time-series model with an alternative dependent Bernoulli counting series*, Communications in Statistics—Theory and Methods, DOI: 10.1080/03610926.2015.1005100.
5. O. A. Waza and A. Ahmad, *A New Distribution Based on a Mixture of Two Geometric Distributions*, Journal of Statistical Theory and Practice **19** (2025), article 98. DOI: 10.1007/s42519-025-00513-8. Publisher abstract/metadata only; full text not compared.
