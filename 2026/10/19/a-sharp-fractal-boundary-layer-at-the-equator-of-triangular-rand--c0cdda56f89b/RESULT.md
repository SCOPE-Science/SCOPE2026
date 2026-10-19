# A sharp fractal boundary layer at the equator of triangular random matrix products

## Finding

For real \(\lambda>\mu>0\) with \(\rho=\mu/\lambda<1/2\), let \((\xi_j)_{j\geq1}\) be independent fair signs and put
\[
 A_\xi=\begin{pmatrix}\lambda&0\\\xi&\mu\end{pmatrix},\qquad
 P_n=A_{\xi_n}\cdots A_{\xi_1},\qquad v_n=(c\rho^{tn},1),
\]
where \(0<c<\lambda(1-\rho)\) and \(t>0\). The invariant equator is \(E=\mathbb R(0,1)\); the two Lyapunov exponents are \(\log\lambda\) and \(\log\mu\). Define the separated Bernoulli Cantor set
\[
 C_\rho=\left\{\sum_{j=0}^\infty\epsilon_j\rho^j:\epsilon_j\in\{-1,1\}\right\},\qquad
 d_\rho=\frac{\log2}{\log(1/\rho)},
\]
and let \(S\) have the probability law of the same series with independent fair signs. Set
\[
 F_c(s)=\sqrt{c^2+(1+cs/\lambda)^2},\qquad
 H(s)=\sqrt{1+(s/\lambda)^2}.
\]
There is a **sharp three-regime crossover** for the Euclidean norm of products on exponentially approaching initial directions:

1. If \(t>1\), then \(\mu^{-n}\|P_nv_n\|\to1\) for every sign sequence, uniformly over all sign sequences.
2. If \(t=1\), the random variables \(\mu^{-n}\|P_nv_n\|\) converge in law to \(F_c(S)\), while almost surely their complete set of subsequential limits is \(F_c(C_\rho)\). This is a nondegenerate Cantor set of Hausdorff dimension \(d_\rho\).
3. If \(0<t<1\), the variables \(\|P_nv_n\|/(\lambda^n c\rho^{tn})\) converge in law to \(H(S)\), while almost surely their complete set of subsequential limits is \(H(C_\rho)\), again a nondegenerate Cantor set of Hausdorff dimension \(d_\rho\).

Both nonconstant limiting laws are singular, non-atomic, and supported on the indicated Cantor sets. More precisely, with \(W_1\) denoting Wasserstein distance of order one,
\[
 W_1\bigl(\mathcal L(\mu^{-n}\|P_nv_n\|),\mathcal L(F_c(S))\bigr)
 \leq\frac{c\rho^n}{\lambda(1-\rho)}\quad(t=1),
\]
and, writing \(r_n=c\rho^{(t-1)n}\),
\[
 W_1\bigl(\mathcal L(\|P_nv_n\|/(\lambda^nc\rho^{tn})),\mathcal L(H(S))\bigr)
 \leq r_n^{-1}+\frac{\rho^n}{\lambda(1-\rho)}\quad(0<t<1).
\]
For every \(t>0\), almost surely (in fact for every sign sequence),
\[
 \lim_{n\to\infty}\frac1n\log\|P_nv_n\|=
 \begin{cases}(1-t)\log\lambda+t\log\mu,&0<t<1,\\
 \log\mu,&t\geq1.
 \end{cases}
\]
Thus the crossover scale is exactly the exponential Lyapunov-gap scale \(\rho^n\). At \(\lambda=2\), \(\mu=1/2\), the two critical Cantor sets have dimension \(1/2\).

## Assumptions and scope

The norm is the standard Euclidean norm on \(\mathbb R^2\). The matrices are multiplied in the displayed chronological order, with newest increment on the left. The initial vector is deliberately time-dependent; no fixed-initial-vector theorem is asserted to fail. The law assumes independent signs with probability \(1/2\) each. The restriction \(\rho<1/2\) guarantees separated Cantor cylinders, and \(c<\lambda(1-\rho)\) ensures the critical normalization map is strictly increasing on the entire Cantor set. The conclusions concern the normalization, limiting distribution, almost-sure cluster sets, and exponential growth rate, not a central limit theorem for a fixed direction.

## Proof

**Exact cocycle identity.** Direct multiplication gives, for every integer \(n\geq1\),
\[
 P_n=\begin{pmatrix}\lambda^n&0\\ \lambda^{n-1}S_n&\mu^n\end{pmatrix},\qquad
 S_n=\sum_{j=1}^n\xi_j\rho^{n-j}.
\]
The bound \(|S_n|\leq(1-\rho)^{-1}\) holds for every sequence. With \(r_n=c\rho^{(t-1)n}\), it follows *without approximation* that
\[
 \mu^{-n}P_nv_n=\bigl(r_n,1+(r_n/\lambda)S_n\bigr),\qquad
 \mu^{-n}\|P_nv_n\|=\sqrt{r_n^2+(1+r_nS_n/\lambda)^2}.\tag{1}
\]
The diagonal entries and bounded \(S_n\) also imply that \(\|P_n\|\) is bounded above and below by positive constants times \(\lambda^n\), and \(\det P_n=(\lambda\mu)^n\). Therefore the two Lyapunov exponents are \(\log\lambda>\log\mu\); the invariant slow line is precisely \(E\).

**Accumulation of the backward-sign series.** On a probability-one event, every finite sign word occurs infinitely often among disjoint blocks of the independent sign sequence. This follows for each word from independent repeated block trials and the second Borel–Cantelli lemma, then from countable intersection. A word of length \(k\) occurring as the *last* \(k\) signs of \((\xi_1,\ldots,\xi_n)\) forces \(S_n\) within \(\rho^k/(1-\rho)\) of the corresponding length-\(k\) prefix of any prescribed element of \(C_\rho\). Each element of \(C_\rho\) is consequently a subsequential limit of \(S_n\), by successively prescribing longer terminal words. Conversely, every \(S_n\) is within \(\rho^n/(1-\rho)\) of \(C_\rho\), by extending its finite sign expansion arbitrarily. Compactness shows that the almost-sure cluster set of \((S_n)\) is exactly \(C_\rho\). Reversal of independent signs also gives \(S_n\overset{\mathrm d}=\sum_{j=0}^{n-1}\xi_{j+1}\rho^j\). Coupling this finite forward series with \(S\) bounds their absolute difference by \(\rho^n/(1-\rho)\).

**Fractal geometry.** The compact set \(C_\rho\) satisfies \(C_\rho=(-1+\rho C_\rho)\cup(1+\rho C_\rho)\), with the first component lying in \([-1/(1-\rho),-(1-2\rho)/(1-\rho)]\) and the second in \([(1-2\rho)/(1-\rho),1/(1-\rho)]\). These two pieces are disjoint since \(\rho<1/2\). At level \(k\), there are \(2^k\) disjoint cylinders with scale \(\rho^k\), so standard covers give Hausdorff dimension at most \(d_\rho\). The fair cylinder measure assigns each cylinder mass \(2^{-k}\); strong separation gives a constant \(K_\rho\) such that any ball of radius comparable to \(\rho^k\) intersects at most \(K_\rho\) such cylinders. Therefore the measure obeys \(\nu(B(s,r))\leq K'_{\rho}r^{d_\rho}\). The mass-distribution bound proves the reverse inequality. The cylinder measure is nonatomic; since \(d_\rho<1\), it is singular with respect to Lebesgue measure.

For \(c<\lambda(1-\rho)\), the expression \(1+cs/\lambda\) is positive throughout \(C_\rho\) (indeed on its convex hull). Thus \(F_c\) is continuously differentiable there, with derivative
\[
 F_c'(s)=\frac{(c/\lambda)(1+cs/\lambda)}{F_c(s)}>0.
\]
Its derivative is bounded above and away from zero on the compact convex hull, so \(F_c\) is bi-Lipschitz on \(C_\rho\), preserving dimension and nonatomicity. The even map \(H\) sends the negative and positive Cantor pieces to the same image; it is bi-Lipschitz on the entire positive first-level piece, which is itself a similarity image of \(C_\rho\). Therefore \(H(C_\rho)\) likewise has Hausdorff dimension \(d_\rho\), is a Cantor set, and carries a nonatomic singular pushforward of the fair sign measure (at most two inverse points occur).

**Three normalizations and quantitative errors.** If \(t>1\), then \(r_n\to0\). Formula (1) and the reverse triangle inequality give, uniformly in all sign sequences,
\[
 \left|\mu^{-n}\|P_nv_n\|-1\right|
 \leq r_n\sqrt{1+\frac1{\lambda^2(1-\rho)^2}}\longrightarrow0.
\]
If \(t=1\), then \(r_n=c\), so the normalized norm equals \(F_c(S_n)\) exactly. The bound \(|F_c'(s)|\leq c/\lambda\) and the coupling above prove the stated \(W_1\) estimate; continuity transports the complete cluster set to \(F_c(C_\rho)\).

For \(0<t<1\), \(r_n\to\infty\) and (1), divided by \(r_n\), reads
\[
 \frac{\|P_nv_n\|}{\lambda^nc\rho^{tn}}
 =\sqrt{1+\left(S_n/\lambda+r_n^{-1}\right)^2}.
\]
The right side differs uniformly from \(H(S_n)\) by at most \(r_n^{-1}\). Since \(|H'(s)|\leq1/\lambda\), the earlier coupling yields the second \(W_1\) estimate, and uniform convergence of the maps yields cluster set \(H(C_\rho)\). These normalized quantities stay bounded above and away from zero for sufficiently large \(n\); taking logarithms and dividing by \(n\) proves the displayed growth-rate formula for every sign sequence. This completes all assertions.

## Verification

The accompanying `checker.py` uses only Python's standard library. It multiplies the matrices with exact rational arithmetic for every sign word through length eight, for three separated choices of \((\lambda,\mu)\), and verifies the full product identity and norm-square identity for three integer boundary exponents. It also checks separation of the first-level Cantor cylinders for several rational contraction ratios. The expected output is `EXACT_PRODUCTS_AND_SEPARATION_OK 4590`. These finite checks test conventions and calculations; the all-length claims follow from the proof above, not from enumeration.

## Relationship to prior work

Barrientos and Malicet, *Limit theorems for random matrix products with a simple top Lyapunov exponent* (arXiv:2610.12678v1, October 8, 2026), establish limit laws for operator norms and **fixed** directions outside an exceptional equator under a simple-top-exponent hypothesis. Aoun and Guivarc'h, *Random matrix products when the top Lyapunov exponent is simple* (arXiv:1705.09593v4, journal 2020), establish stationary projective measures and the associated affine skew-product and limit-set framework; in particular, contracting affine recursions and Bernoulli convolutions are classical in that framework. Those results motivate but do not state the present **time-dependent input** crossover, its three exact normalizations, or the corresponding pathwise fractal cluster sets of normalized vector norms. The separated Bernoulli convolution and its dimension are elementary, previously known ingredients, not asserted as independently new.

## Limitations

The matrices form a special reducible two-dimensional Bernoulli family. The separation assumption \(\rho<1/2\) is essential to the stated exact dimension by this argument; no formula is claimed when the Cantor pieces overlap. No uniform theorem over all random products with a simple top exponent, no central limit theorem, and no unqualified novelty or independence claim is made. The mathematical conclusions have been checked against selected pertinent passages of the two primary research papers, not against every possible earlier formulation in the wider affine-recursion literature.

## References

- P. G. Barrientos and D. Malicet, *Limit theorems for random matrix products with a simple top Lyapunov exponent*, arXiv:2610.12678v1 (first posted 2026-10-08), https://arxiv.org/pdf/2610.12678.
- R. Aoun and Y. Guivarc'h, *Random matrix products when the top Lyapunov exponent is simple*, J. Eur. Math. Soc. **22** (2020), 2135–2182; open preprint arXiv:1705.09593v4, https://arxiv.org/pdf/1705.09593.
