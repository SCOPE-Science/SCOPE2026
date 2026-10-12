# Exact uniform comonotonicity defect of the EPD Bernstein copula
## Finding
For an integer \(m\ge1\), consider the bivariate EPD Bernstein copula in the incomplete-beta representation
\[
C_m(u,v)=\frac{1}{m+1}\sum_{k=0}^{m}
I_u(k+1,m+1-k)\,I_v(k+1,m+1-k),
\qquad 0\le u,v\le1,
\]
where \(I_x(a,b)\) is the regularized incomplete beta function. Let
\[
M(u,v)=\min(u,v)
\]
be the comonotonic copula. Then
\[
\|M-C_m\|_\infty
=
\frac{\binom{2m+2}{m+1}}{2\,4^{m+1}},
\]
and this value is attained at
\[
(u,v)=\left(\frac12,\frac12\right).
\]
Hence
\[
\|M-C_m\|_\infty
\sim
\frac{1}{2\sqrt{\pi(m+1)}}.
\]

Thus this smooth finite-degree positive-dependence construction approaches perfect comonotonicity at the exact uniform rate \(1/(2\sqrt{\pi(m+1)})\), with a closed-form finite-\(m\) defect.

## Assumptions and scope
The statement concerns the bivariate EPD Bernstein copula defined by the displayed incomplete-beta formula. The integer parameter satisfies \(m\ge1\). No assertion is made about arbitrary Bernstein copulas, other extremal points, dimensions above two, or other metrics.

The norm is the ordinary supremum norm on \([0,1]^2\). Since every copula is bounded above by the Fréchet–Hoeffding upper copula \(M\), the absolute difference equals \(M-C_m\).

## Proof
Put
\[
n=m+1.
\]
For \(J_u\sim\operatorname{Bin}(n,u)\),
\[
\Pr\{J_u\ge r\}=I_u(r,n-r+1).
\]
Therefore, if \(J_u\) and \(J_v\) are independent binomial variables with respective success probabilities \(u\) and \(v\),
\[
C_m(u,v)
=
\frac1n\sum_{r=1}^{n}\Pr\{J_u\ge r\}\Pr\{J_v\ge r\}
=
\frac1n\,\mathbb E\!\left[\min(J_u,J_v)\right].
\tag{1}
\]
This is exactly the order-\(n\) copula written by Baker.

Assume first that \(u\le v\). Since \(M(u,v)=u=\mathbb E[J_u]/n\), equation (1) gives
\[
M(u,v)-C_m(u,v)
=
\frac1n\,\mathbb E\!\left[(J_u-J_v)_+\right].
\tag{2}
\]
For fixed \(u\), the binomial variable \(J_v\) is stochastically increasing in \(v\). Hence the right-hand side of (2) is nonincreasing in \(v\) on \(v\ge u\), so it is maximized there at \(v=u\). By symmetry, the global supremum is attained on the diagonal.

Write \(J,K\) for independent \(\operatorname{Bin}(n,p)\) variables. On the diagonal,
\[
M(p,p)-C_m(p,p)
=
\frac{\mathbb E|J-K|}{2n}.
\tag{3}
\]
Pair the Bernoulli summands of \(J\) and \(K\). Each difference summand equals \(1\) or \(-1\) with probability \(p(1-p)\) each and equals \(0\) otherwise. If
\[
R=2p(1-p),
\]
then the number \(N\) of nonzero difference summands is \(\operatorname{Bin}(n,R)\); conditional on \(N=j\), the difference has the law of a \(j\)-step simple symmetric random walk \(S_j\).

Let
\[
a_j=\mathbb E|S_j|.
\]
For every integer \(s\),
\[
\frac{|s+1|+|s-1|}{2}-|s|
=
\mathbf 1_{\{s=0\}},
\]
so
\[
a_{j+1}-a_j=\Pr\{S_j=0\}\ge0.
\]
Thus \(a_j\) is nondecreasing. Since \(\operatorname{Bin}(n,R)\) is stochastically increasing in \(R\), the expectation in (3) is nondecreasing in \(R\). The quantity
\[
R=2p(1-p)
\]
is maximized at \(p=1/2\). Hence a global maximizer is \((u,v)=(1/2,1/2)\).

At \(p=1/2\),
\[
J-K\stackrel d=B_{2n}-n,
\qquad
B_{2n}\sim\operatorname{Bin}(2n,1/2),
\]
because \(J+(n-K)\sim\operatorname{Bin}(2n,1/2)\). By symmetry,
\[
\mathbb E|B_{2n}-n|
=
\frac{2}{4^n}
\sum_{k=0}^{n-1}(n-k)\binom{2n}{k}.
\]
Using
\[
(n-k)\binom{2n}{k}
=
n\left[\binom{2n-1}{k}-\binom{2n-1}{k-1}\right],
\]
the sum telescopes to
\[
\frac{n}{2}\binom{2n}{n}.
\]
Therefore
\[
\mathbb E|B_{2n}-n|
=
n\frac{\binom{2n}{n}}{4^n},
\]
and (3) yields
\[
\|M-C_m\|_\infty
=
\frac{\binom{2n}{n}}{2\,4^n}
=
\frac{\binom{2m+2}{m+1}}{2\,4^{m+1}}.
\]
Finally, the central-binomial asymptotic
\[
\binom{2n}{n}\sim\frac{4^n}{\sqrt{\pi n}}
\]
gives the stated rate.

## Verification
The bundled `verify.py` checks, in exact rational arithmetic, the center identity and the telescoping binomial identity for many values of \(n\). It also evaluates the copula on deterministic grids for small \(n\) and verifies that no grid point exceeds the proved center defect.

A successful run ends with
`VERIFY_OK exact_n=120 grid_n=8 asymptotic_ratio=0.999987500078`.

The finite checks are not used to prove the global supremum; the proof above is analytic for every integer \(m\ge1\).

## Relationship to prior work
Blier-Wong, Cossette, and Marceau identify an EPD extremal point for exchangeable Bernstein copulas and give the incomplete-beta representation used here. Their paper explains that exchangeable FGM copulas are the simplest exchangeable Bernstein copulas and defers the broader Bernstein analysis to future work. The inspected source does not quantify the uniform distance of the EPD Bernstein construction from the comonotonic copula.

Baker's order-statistics copula of order \(n\) is
\[
C_n(u,v)=\frac1n\sum_{r=1}^{n}Q_{r,n}(u)Q_{r,n}(v),
\]
which is the same bivariate family after \(n=m+1\). Baker gives the Spearman correlation \((n-1)/(n+1)\), studies dependence ordering, and states that the Fréchet upper bound is attained as \(n\to\infty\). The inspected full text does not state an exact supremum-norm error or a convergence constant.

General Bernstein-copula literature establishes approximation and uniform convergence, but targeted searches did not locate the finite-\(m\) identity above or the exact \(1/(2\sqrt{\pi n})\) leading constant for this extremal family.

## Limitations
This is a bivariate exact approximation result. It does not determine a multivariate supremum defect, other norms, or approximation rates for arbitrary exchangeable Bernstein copulas.

The bibliographic comparison includes the direct construction source, Baker's full order-statistics treatment, and targeted searches for equivalent Bernstein-approximation formulations. An equivalent identity could still exist in older approximation-theory literature under terminology unrelated to copulas.

## References
1. C. Blier-Wong, H. Cossette, and E. Marceau, “Exchangeable FGM copulas,” arXiv:2205.11302v1, 23 May 2022; *Advances in Applied Probability* 56 (2024), 205–234, DOI: 10.1017/apr.2023.19.
2. R. Baker, “Copulas from Order Statistics,” arXiv:1412.0948, 2 December 2014.
3. A. Sancetta and S. Satchell, “The Bernstein copula and its applications to modeling and approximations of multivariate distributions,” *Econometric Theory* 20 (2004), 535–562.
