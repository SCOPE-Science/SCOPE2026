# Sharp two-round stochastic consensus on odd cycles

## Finding

**Theorem.** Let \(n\ge5\) be odd. On the undirected unit cycle \(C_n\), let \(L=2I-S-S^{-1}\), where \(S\) is the cyclic shift. Consider two successive, spatially homogeneous, symmetric, nearest-neighbor Markov steps
\[
P(p)=I-pL=(1-2p)I+p(S+S^{-1}),\qquad 0\le p\le\tfrac12.
\]
Both factors are individually entrywise nonnegative and stochastic. Among all ordered pairs \((p,q)\in[0,1/2]^2\), minimize the two-round second-largest eigenvalue modulus on the orthogonal complement of the constants:
\[
R_n(p,q)=\max_{1\le k<n}|(1-p\lambda_k)(1-q\lambda_k)|,
\qquad \lambda_k=2-2\cos\frac{2\pi k}{n}.
\]
Set
\[
a=2-2\cos(2\pi/n),\qquad b=2+2\cos(\pi/n).
\]
Then the **unique optimal unordered pair** and optimal two-round contraction are
\[
\boxed{\{p,q\}=\left\{\tfrac12,\frac1{a+b-2}\right\}},
\qquad
\boxed{R_n^*=\frac{(2-a)(b-2)}{2(a+b-2)}}.
\]
The best **repeated single-step** choice has \(p=q=2/(a+b)\), with two-round factor \(R_n^{\mathrm{stat}}=(b-a)^2/(a+b)^2\). The strict finite-size improvement is exactly
\[
\boxed{R_n^{\mathrm{stat}}-R_n^*=
\frac{ab(a+b-4)^2}{2(a+b)^2(a+b-2)}>0}.
\]
For \(n=5\), the optimum is \((p,q)=(1/2,1/3)\), up to order, and \(P(1/2)P(1/3)=(I+J)/6\), where \(J\) is the five-by-five all-ones matrix; its nonconstant eigenvalues all equal \(1/6\). The best repeated-step factor is \(1/5\). As \(n\) tends to infinity through odd integers,
\[
R_n^*=1-\frac{4\pi^2}{n^2}+O(n^{-4}),\qquad
R_n^{\mathrm{stat}}-R_n^*=\frac{9\pi^6}{4n^6}+O(n^{-8}).
\]

## Assumptions and scope

The objective is the operator norm on mean-zero states **after precisely two rounds**. Each individual factor must be a nonnegative symmetric nearest-neighbor stochastic matrix with a **single common edge probability** over the entire cycle; self-loops are permitted. The theorem makes no claim of global optimality when probabilities can depend on vertex, when transitions may jump farther than one edge in a single round, when intermediate factors may have negative entries, or for a different number of rounds. The odd-order assumption is substantive; the even-order case is not claimed.

Since \(n\) is odd, the smallest and largest positive Laplacian eigenvalues are \(a\) and \(b\) as above. They satisfy \(0<a<2<b<4\), \(4<a+b\le5\), and \(1/3\le 1/(a+b-2)<1/2\). For odd \(n\ge7\), \(a\le1\).

## Proof

**1. Fourier reduction.** The cyclic shift diagonalizes both factors simultaneously. On the nonconstant Fourier mode \(k\), the product multiplier is \(f(\lambda_k)=(1-p\lambda_k)(1-q\lambda_k)\), so the proposed objective and the endpoint lower bound
\[
R_n(p,q)\ge \max\{(1-ap)(1-aq),\, |(1-bp)(1-bq)|\}
\]
are exact and valid for all feasible \(p,q\). The first endpoint product is strictly positive.

**2. Exact optimization of the two endpoint modes.** Suppose \(p<1/b\). Since \(q\le1/2\), the first endpoint alone satisfies
\[
(1-ap)(1-aq)>(1-a/b)(1-a/2)>R_n^*.
\]
The second strict inequality reduces, after a positive denominator is cleared, to \(a(2-a)>0\). The same holds with \(p,q\) interchanged. Therefore any endpoint-optimal pair must lie in \([1/b,1/2]^2\).

Put \(B=b/2-1>0\), \(x=bp-1\), \(y=bq-1\), \(\alpha=1-a/b\), and \(\beta=a/b\). Then \(0\le x,y\le B\), and the endpoint products become
\[
F_a=(\alpha-\beta x)(\alpha-\beta y),\qquad F_b=xy.
\]
For fixed \(c=xy\), the elementary inequality \((B-x)(B-y)\ge0\) implies \(x+y\le B+c/B\); consequently,
\[
F_a\ge(\alpha-\beta B)(\alpha-\beta c/B),
\]
with equality exactly when \(x=B\) or \(y=B\). This lower bound decreases strictly with \(c\in[0,B^2]\), whereas \(F_b=c\) increases strictly. At \(c=0\) the former is positive; at \(c=B^2\) the former is \((1-a/2)^2<B^2\) because \(a+b>4\). Thus their maximum has a unique minimizing intersection. Equality forces one of \(p,q\) to be \(1/2\). Balancing the endpoint values,
\[
(1-a/2)(1-aq)=(b/2-1)(bq-1),
\]
gives uniquely \(q=1/(a+b-2)\), with common endpoint value \(R_n^*\). In particular **every** feasible pair has endpoint objective at least \(R_n^*\), and equality forces the stated unordered pair.

**3. All intermediate Fourier modes.** For the proposed pair define
\[
f(\lambda)=(1-\lambda/2)(1-q\lambda),\qquad q=1/(a+b-2).
\]
Its two roots are \(2\) and \(1/q\in[2,3]\). The function is positive and decreasing on \([a,2]\), positive and increasing on \([1/q,b]\), so its positive maximum throughout \([a,b]\) is the balanced endpoint value \(R_n^*\). Between its roots, its negative minimum has magnitude
\[
\frac{(1/2-q)^2}{2q}\le\frac1{24},
\]
since \(1/3\le q<1/2\). At \(n=5\), \(R_n^*=1/6\). At every odd \(n\ge7\), the bound \(a\le1\) gives \(R_n^*=(1-a/2)(1-aq)\ge1/4\). Thus the negative trough is always below the endpoint modulus. Every Fourier multiplier satisfies \(|f(\lambda_k)|\le R_n^*\), completing attainment and the uniqueness proof.

**4. Repeating one kernel and the strict gain.** For a fixed feasible \(p\), the worst one-step modulus is \(\max\{1-ap,|1-bp|\}\), because the absolute value of an affine function is maximized at a spectral endpoint. The unique minimizer balances them at \(p=2/(a+b)\), feasible since \(a+b>4\). Its squared two-round factor is \((b-a)^2/(a+b)^2\). Direct common-denominator algebra gives the displayed positive improvement identity. Finally, Taylor expansion of the two cosine endpoints gives the asymptotic expansions. This completes the proof.

## Verification

The accompanying `verify.py` uses only Python's standard library, and can be run by `python verify.py`. It checked 22,455 finite assertions: exact rational five-vertex transition products, a distinct even-vertex boundary example, rational endpoint-balance and gain identities, Fourier spectra for every odd order from 5 through 301, sampled admissible competitors, and directly multiplied stochastic matrices through order 27. A separate differential-evolution numerical search on selected dimensions also returned the claimed pair. These finite checks are supplementary; the argument above proves the result for every admissible odd order.

## Relationship to prior work

Boyd, Diaconis, Parrilo and Xiao analyze stationary fastest mixing on symmetric graphs, including cycles: their one-step optimization yields the stationary comparator, but a theorem about a **product of two independently chosen, individually stochastic factors** does not follow from that one-step optimum. Apers and Sarlette analyze accelerated consensus with quadratic polynomial filters and explicitly allow factors outside the Markov nonnegativity constraint; their unconstrained spectral polynomial optimization does not imply the present boundary-constrained pair. A published result on stagewise-nonexpansive Richardson factors optimizes over the broader numerical range \(0\le p\le2/b\) and a whole spectral interval; because \(b<4\) on odd cycles, that range includes nonstochastic matrices with negative holding probabilities. Its formulas apply to a different feasible set, and even-cycle consequences are excluded from this theorem. The combination of **discrete odd-cycle modes** and the per-round **Markov positivity bound** is the specific question solved here.

## Limitations

The formula proves a sharp finite-size two-round contraction, **not** an asymptotic Chebyshev-order acceleration. The advantage over repeating the best fixed kernel is positive but of order \(n^{-6}\) in the contraction value. The claimed originality is relative to the inspected primary and available research literature; unindexed treatments of two-period stochastic consensus may contain an equivalent formula. No independent mathematical audit is claimed.

## References

1. S. Apers and A. Sarlette, *Accelerating Consensus by Spectral Clustering and Polynomial Filters*, arXiv:1503.01269, initial public submission 2015-03-04. https://arxiv.org/abs/1503.01269
2. S. Boyd, P. Diaconis, P. Parrilo and L. Xiao, *Fastest mixing Markov chain on graphs with symmetries*, arXiv:0709.0955, initial submission 2007-09-06. https://arxiv.org/abs/0709.0955
3. S. Boyd, P. Diaconis and L. Xiao, *Fastest mixing Markov chain on a graph*, SIAM Review 46 (2004), 667–689. https://web.stanford.edu/~boyd/papers/fmmc.html
4. *Sharp stagewise-safe Richardson frontier and a no-acceleration barrier*, publicly available research record. https://github.com/Resultary/2026/tree/main/2026/9/20/SCOPE-stagewise-safe-two-step-richardson-frontier--31fff666d705
