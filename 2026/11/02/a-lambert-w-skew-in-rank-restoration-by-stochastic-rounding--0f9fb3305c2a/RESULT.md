# A Lambert-W skew in rank restoration by stochastic rounding

## Finding

Let \(d\ge 2\) be fixed and \(n\ge d\). Consider the rank-one constant matrix \(A(p)=p\mathbf 1_{n\times d}\), where \(0<p<1\), and independently round every entry to \(1\) with probability \(p\) and to \(0\) otherwise. Write \(B_{n,d}(p)\) for the resulting binary matrix and
\[
\Phi_{n,d}(p)=\Pr\bigl(\operatorname{rank}_{\mathbb R}B_{n,d}(p)<d\bigr),\qquad C_d=\binom d2.
\]

**Fixed-width optimizer.** For every fixed \(d\ge2\), and all sufficiently large integers \(n\) (depending on \(d\)), \(\Phi_{n,d}\) has a unique global minimizer \(p_{n,d}\in(0,1)\). With \(W\) the positive real Lambert function, characterized by \(W(t)e^{W(t)}=t\),
\[
\boxed{p_{n,d}=\frac12+\frac{W(n/(d-1))}{2n}+O_d\!\left(\frac{(\log n)^2}{n^2}\right).}
\]
The optimal rank-deficiency probability and the midpoint probability obey
\[
\boxed{\begin{aligned}
\Phi_{n,d}(p_{n,d})&=C_d2^{-n}\left(1+O_d\!\left(\frac{(\log n)^2}{n}\right)\right),\\
\Phi_{n,d}(1/2)&=(d+C_d)2^{-n}+O_d(c_d^n),\qquad 0<c_d<1/2,\\
\lim_{n\to\infty}\frac{\Phi_{n,d}(p_{n,d})}{\Phi_{n,d}(1/2)}&=\frac{d-1}{d+1}.
\end{aligned}}
\]
Thus variance-maximizing midpoint rounding is not optimal for full-column-rank restoration: a positive, vanishing offset cuts the rare rank-deficiency probability by a nonvanishing proportion. The claim concerns comparison across different input fractions \(p\), not a biased change of the rounding rule for one fixed input.

**Exact two-column law.** For every integer \(n\ge2\) and \(0\le p\le1\), put \(q=1-p\) and \(s=p^2+q^2\). Then
\[
\boxed{\Phi_{n,2}(p)=s^n+2q^n-2q^{2n}.}
\]
For all \(n\ge2\) this polynomial has exactly one global minimum in \((1/2,1)\). Its value for \(n=2\) is exactly \(1/2\), attained at \(p=1/\sqrt2\). In particular, at \(n=2\), midpoint rounding has failure probability \(5/8\), compared with the optimum \(1/2\).

## Assumptions and scope

The base rounding grid consists of \(0\) and \(1\); independently rounded entries use unbiased stochastic nearness. The unrounded input is \(A(p)=p\mathbf1_{n\times d}\) and has rank one for \(p>0\). Rank is taken over \(\mathbb R\), not a finite field. Each fixed \(d\ge2\) is held constant while \(n\to\infty\); the constants implicit in \(O_d\) need not be uniform as \(d\) grows. The statements do not assert anything about nonconstant matrices, dependent rounding, smallest positive singular values, or equality of full matrix distributions.

## Proof

**1. Exact two-column law.** Write the two independent binary columns as \(X,Y\). Two nonzero vectors with entries in \(\{0,1\}\) can be proportional over \(\mathbb R\) only if they are equal. Hence the rank-deficiency event is exactly \(\{X=0\}\cup\{Y=0\}\cup\{X=Y\}\). Its probability is \(2q^n-q^{2n}+s^n-q^{2n}\), as claimed. The subtraction accounts for the all-zero pair in both unions.

For \(p<1/2\), the difference between the failure laws at reflected arguments is
\[
\Phi_{n,2}(p)-\Phi_{n,2}(1-p)
=2\bigl(q^n-p^n\bigr)\bigl(1-q^n-p^n\bigr)>0,
\]
because \(n\ge2\), \(q>p>0\), and \(q^n+p^n<1\). Any optimizer therefore lies in \([1/2,1)\). For \(1/2<p<1\), differentiating gives
\[
\frac{\Phi'_{n,2}(p)}{2n}=(2p-1)s^{n-1}-q^{n-1}(1-2q^n).
\]
For \(n\ge3\), the stationary equation is \(R_n(q)=1\) where
\[
R_n(q)=\frac{(1-2q)s^{n-1}}{q^{n-1}(1-2q^n)},\qquad 0<q<1/2.
\]
Its logarithmic derivative equals
\[
-\frac{2}{1-2q}+(n-1)\frac{4q-2}{s}-\frac{n-1}{q}+\frac{2nq^{n-1}}{1-2q^n}<0.
\]
Indeed the first two terms are negative, and the last two have nonpositive sum since \(2(2n-1)q^n\le 2(2n-1)2^{-n}\le n-1\) for \(n\ge3\). Since \(R_n(0+)=+\infty\) and \(R_n(1/2-)=0\), the stationary point is unique and is the global minimum. For \(n=2\), direct factorization of the derivative in \(q\) gives \(4(q-1)(2q^2-4q+1)\), whose sole interior minimum lies at \(q=1-1/\sqrt2\), hence \(p=1/\sqrt2\) and \(\Phi_{2,2}=1/2\).

**2. Finite-hyperplane principle.** For fixed \(d\), let \(V=\{0,1\}^d\). Because \(V\) spans \(\mathbb R^d\), whenever a collection of rows from \(V\) has rank below \(d\), its span can be extended to a hyperplane spanned by \(d-1\) independent elements of \(V\). There are finitely many such hyperplanes, and rank deficiency is the union of the events that every row lies in one of them.

Every linear hyperplane \(H=\{x:a\cdot x=0\}\) with \(a\ne0\) meets \(V\) in at most \(2^{d-1}\) vertices. Select a nonzero coefficient \(a_j\), and pair vertices by toggling coordinate \(j\); at most one member of each pair belongs to \(H\). Equality forces each other coefficient \(a_i\) to be either \(0\) or \(-a_j\), by considering the vertex supported at \(i\). Two coefficients equal to \(-a_j\) are impossible, by considering the vertex supported at both corresponding coordinates. Consequently equality occurs **only** for the \(d\) hyperplanes \(x_j=0\) and the \(C_d\) hyperplanes \(x_i=x_j\). Conversely every one of those has exactly \(2^{d-1}\) vertices. Intersections of two distinct such hyperplanes contain at most \(2^{d-2}\) vertices: two independent linear equations permit at most one choice of two pivot coordinates for each assignment of the others.

**3. Uniform rare-event expansion.** A random row belongs to \(x_j=0\) with probability \(q\), and to \(x_i=x_j\) with probability \(s=p^2+q^2\). Each of the finitely many other hyperplanes contains at most \(2^{d-1}-1\) vertices at \(p=1/2\), and each intersection of two distinct dominant hyperplanes contains at most \(2^{d-2}\). By continuity of the finite row-probability polynomials, there exist \(\varepsilon_d>0\), \(c_d<1/2\) and constants \(K_{d,r}\) such that, uniformly for \(|p-1/2|\le\varepsilon_d\),
\[
\Phi_{n,d}(p)=dq^n+C_ds^n+E_{n,d}(p),\qquad
\left|\frac{d^r}{dp^r}E_{n,d}(p)\right|\le K_{d,r}n^r c_d^{n-r}\quad (r=0,1,2).
\]
This follows from finite inclusion–exclusion over row-containment events; every error term is a signed power of a polynomial with base at most \(c_d\). The same argument gives the lower bound \(\Phi_{n,d}(p)\ge C_ds^n-O_d(c_d^n)\) in this neighborhood. Evaluating the expansion at \(p=1/2\) gives the stated midpoint expression.

**4. Localization and uniqueness of the optimizer.** Since \(n\ge d\), some binary matrices have full column rank, so \(\Phi_{n,d}(p)<1\) for every interior \(p\); at \(p=0,1\), it equals one. Thus a global minimizer exists in \((0,1)\). Choose the trial argument
\[
p^\circ_n=\frac12+\frac{W(n/(d-1))}{2n}.
\]
Since \(W(t)=O(\log t)\), the expansion in Step 3 yields
\[
\Phi_{n,d}(p^\circ_n)\le C_d2^{-n}\left(1+O_d\!\left(\frac{(\log n)^2}{n}\right)\right).
\]
For any global minimizer \(p_{n,d}\), the event that two specified columns are equal gives \(\Phi_{n,d}(p_{n,d})\ge s(p_{n,d})^n\). This and the trial upper bound imply \(p_{n,d}\to1/2\). Once the minimizer is inside the neighborhood of Step 3, applying the stronger lower bound from that step yields
\[
\bigl(1+4(p_{n,d}-1/2)^2\bigr)^n
\le1+O_d\!\left(\frac{(\log n)^2}{n}\right),
\]
so \(|p_{n,d}-1/2|=O_d((\log n)/n)\).

Let \(G_n(p)=dq^n+C_ds^n\). For \(p\le1/2\), \(G'_n(p)<0\); in the localized region the error derivative is exponentially smaller in magnitude, so any global optimizer is eventually to the right of \(1/2\). Moreover \(G''_n(p)\ge4C_dn s^{n-1}\ge 4C_dn2^{-(n-1)}\) everywhere. The error second derivative is \(O_d(n^2c_d^{n-2})\), exponentially smaller. Thus \(\Phi_{n,d}\) is strictly convex on a fixed neighborhood of \(1/2\) for large \(n\). Every global minimizer lies in that neighborhood, proving eventual **global uniqueness**.

**5. Sharp Lambert-W location.** Put \(\delta_n=p_{n,d}-1/2>0\), \(x_n=2n\delta_n=O_d(\log n)\). The derivative condition and Step 3 give
\[
4C_d\delta_n\left(\frac{s}{q}\right)^{n-1}=d+O_d(e^{-a_dn})
\]
for some \(a_d>0\). Since
\[
(n-1)\log\frac{s}{q}=x_n+O_d\!\left(\frac{(\log n)^2}{n}\right),
\]
it follows that
\[
x_ne^{x_n}=\frac{nd}{2C_d}\left(1+O_d\!\left(\frac{(\log n)^2}{n}\right)\right)
=\frac n{d-1}\left(1+O_d\!\left(\frac{(\log n)^2}{n}\right)\right).
\]
The positive Lambert function is Lipschitz with constant at most one as a function of its argument's logarithm. Consequently \(x_n=W(n/(d-1))+O_d((\log n)^2/n)\), proving the optimizer expansion. Finally, \(s^n=2^{-n}(1+O_d((\log n)^2/n))\), while \(q^n=2^{-n}O_d((\log n)/n)\), proving the optimal probability and ratio.

## Verification

The accompanying standard-library script `verify.py` enumerates all binary matrices in specified small cases and evaluates their real ranks by exact rational elimination. It independently compares the full \(d=2\) probability law against exhaustive enumeration for \(2\le n\le6\) and five rational rounding probabilities; checks exact finite \(d=3\) rank-deficiency polynomials at \(n=3,4\); tests the discrete-hyperplane equality classification over a bounded coefficient grid for \(2\le d\le5\); and checks the two-column optimizer and Lambert asymptotic numerically. No finite enumeration is used to infer the theorem for arbitrarily large \(n\) or \(d\); that conclusion follows from the proof above.

Run with Python 3: `python verify.py`. No third-party packages are needed.

## Relationship to prior work

Dexter, Boutsikas, Ma, Ipsen and Drineas (2024) prove a broad smallest-singular-value regularization effect of stochastic nearness rounding. Their Section 4.1 specifically considers the all-\(1/2\), two-column rank-one example, and Appendix A obtains a high-probability singular-value bound. Neither is an exact probability optimizer as the input fractional placement varies or a fixed-column, large-row Lambert-W law. The present proof supplies that different distributional question, including the contribution of zero columns.

Jain, Sah and Sawhney (2020) establish sharp singularity terms for *square* discrete random matrices at fixed nonuniform entry distributions. The already-known zero-column and equal-column mechanisms are ingredients rather than new phenomena claimed here. Their square growing-width theorem does not imply the uniform, dimension-fixed, bias-varying optimization. Kahn, Komlós and Szemerédi (1995) treat the distinct \(\{\pm1\}\) matrix model; a later discussion attributes to them a fixed-width, fair-sign full-rank asymptotic. That does not supply the zero-atom asymmetry or optimized near-midpoint Bernoulli parameter studied here. The 1995 technical full text could not be fully compared; priority remains qualified.

## Limitations

The optimizer compares the rank-restoration probabilities for *different constant input matrices* \(A(p)\), not different biased rounding distributions for a single fixed matrix. It is not an optimal numerical strategy for arbitrary data. Full rank is weaker than a quantitative lower bound on the smallest singular value. The fixed-width asymptotics are not uniform in growing \(d\), and the exact finite-\(n\) uniqueness result is proved only for two columns. Independent literature confirmation and publication-priority verification have not been performed.

## References

1. G. Dexter, C. Boutsikas, L. Ma, I. C. F. Ipsen, P. Drineas, *Stochastic Rounding Implicitly Regularizes Tall-and-Thin Matrices*, arXiv:2403.12278, first posted 2024-03-18. https://arxiv.org/abs/2403.12278
2. V. Jain, A. Sah, M. Sawhney, *Singularity of Discrete Random Matrices*, arXiv:2010.06554, first posted 2020-10-13. https://arxiv.org/abs/2010.06554
3. J. Kahn, J. Komlós, E. Szemerédi, *On the probability that a random \(\pm1\)-matrix is singular*, Journal of the American Mathematical Society 8 (1995), 223–240. https://doi.org/10.1090/S0894-0347-1995-1260107-2
