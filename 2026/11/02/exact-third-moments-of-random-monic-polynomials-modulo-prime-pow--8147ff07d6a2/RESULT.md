# Exact third moments of random monic polynomials modulo prime powers

## Finding

Let \(p\) be any prime, \(k\geq1\) and \(d\geq3\). Choose a monic polynomial
\[
F(X)=X^d+a_{d-1}X^{d-1}+\cdots+a_1X+a_0
\]
uniformly from \((\mathbb Z/p^k\mathbb Z)^d\), independently in its lower coefficients, and put
\[
R=\#\{x\bmod p^k:F(x)\equiv0\pmod{p^k}\}.
\]
Then \(\mathbb ER=1\), \(\operatorname{Var}(R)=k(1-p^{-1})\), and the **exact third raw moment**, independent of \(d\), is
\[
\boxed{\mathbb ER^3=\begin{cases}
\dfrac{p^m(p^2+8p+1)-(6m+8)p+6m-1}{p^2},&k=2m,\quad m\geq1,\\[2mm]
\dfrac{5(p+1)p^{m+1}-(6m+11)p+6m+2}{p^2},&k=2m+1,\quad m\geq0.
\end{cases}}
\]
Thus, as \(k\to\infty\) along even and odd integers respectively,
\[
\frac{\mathbb ER^3}{p^{k/2}}\longrightarrow
\begin{cases}
(p^2+8p+1)/p^2,&k\ \text{even},\\
5(p+1)/p^{3/2},&k\ \text{odd}.
\end{cases}
\]
In particular, the third moment grows on the exponential square-root scale \(p^{k/2}\), although the variance grows only linearly in \(k\). The statement concerns *congruence roots modulo each finite prime power*, not the number of genuine roots in \(\mathbb Q_p\).

## Assumptions and scope

The prime \(p\) may equal \(2\). Every positive exponent \(k\) is included. The degree condition \(d\geq3\) is essential to the proof because the constant, linear and quadratic coefficients must be independent and uniform modulo \(p^k\). Repeated roots and all coincidences of sampled points are counted without restriction. The monic leading term can be replaced by any fixed higher-degree polynomial without changing the conclusion, provided those three coefficients remain independent uniform; the displayed theorem fixes the monic model.

## Proof

Put \(q=p^k\). Write \(\nu(w)=\min(k,v_p(w))\), with \(\nu(0)=k\).

**First and second moments.** For each \(x\bmod q\), the random value \(F(x)\) is uniform because \(a_0\) is uniform, hence \(\mathbb ER=1\). For an ordered pair \(x,y\), the two evaluation constraints have probability \(p^{-2k+\nu(x-y)}\): subtraction reduces the second constraint to \((x-y)a_1\) plus a fixed term, and the constant coefficient enforces the first. Summing over \(x,y\) gives
\[
\mathbb ER^2=\sum_{h\bmod q}p^{-k+\nu(h)}
=1+k(1-p^{-1}).
\]
Therefore \(\operatorname{Var}(R)=\mathbb ER^2-1=k(1-p^{-1})\).

**Three evaluations.** For any ordered triple \((x,y,z)\), the matrix of the three coefficients \(a_0,a_1,a_2\) is
\[
V(x,y,z)=\begin{pmatrix}1&x&x^2\\1&y&y^2\\1&z&z^2\end{pmatrix}.
\]
All coefficients of higher powers merely translate the target of this linear system. The first Smith invariant of \(V\) is a unit. Let
\[
t=\min\{\nu(x-y),\nu(x-z),\nu(y-z)\}.
\]
If \(t<k\), the second Smith exponent is \(t\), since the greatest common divisor of all \(2\times2\) minors has valuation \(t\). The Vandermonde determinant is \((y-x)(z-x)(z-y)\), so its third exponent, truncated at \(k\), is
\[
s=\min\bigl(k,\nu(x-y)+\nu(x-z)+\nu(y-z)-t\bigr).
\]
(The formula is valid when a difference vanishes modulo \(q\), because all exponents are truncated at \(k\).) Consequently the probability of the three zeros is \(p^{-3k+t+s}\). When \(x=y=z\), the probability is \(p^{-k}\). Summing the ordered triples, translating by \(x\), and setting \(u=y-x\), \(v=z-x\) therefore yields
\[
\mathbb ER^3=p^{-2k}\sum_{u,v\bmod q}p^{t(u,v)+s(u,v)}.
\tag{1}
\]
The identical triple \(u=v=0\) contributes exactly \(1\).

**Exact valuation partition.** Fix \(0\leq t<k\), and divide \(u,v\) by \(p^t\). Put \(L=k-t\). The reduced ordered triple \((0,u',v')\) has at least two distinct residues modulo \(p\). With normalized measure on the two reduced coordinates, the possibilities are:
\[
\begin{array}{c|c}
\text{valuation pattern}&\text{probability}\ 
\hline
\text{all three distinct modulo }p\ (j=0)&w_0=(p-1)(p-2)/p^2\\
\text{one pair agrees to exact depth }j,\ 1\leq j<L&w_j=3(p-1)^2/p^{j+2}\\
\text{one pair agrees modulo }p^L\ (j=L)&w_L=3(p-1)/p^{L+1}.
\end{array}
\]
These weights sum to \(1-p^{-2}\). In each case, \(s=\min(k,2t+j)\); the total contribution of the fixed \(t\) to (1) is \(p^{-t}B_t\), where
\[
B_t=\sum_{j=0}^{L}w_jp^{\min(k,2t+j)}.
\]
If \(2t\geq k\), all terms are saturated, giving \(B_t=(1-p^{-2})p^k\). If \(2t<k\), set \(h=k-2t\). Terms \(1\leq j<h\) each contribute \(3(p-1)^2p^{2t-2}\), while the total tail probability for \(j\geq h\) is \(3(p-1)p^{-h-1}\). Combining this with \(j=0\) gives
\[
B_t=(p-1)p^{2t-2}\bigl[p+1+3(p-1)(k-2t)\bigr].
\]
Therefore, for \(m=\lceil k/2\rceil\), the exact finite sum is
\[
\mathbb ER^3=1+
\frac{p-1}{p^2}\sum_{t=0}^{m-1}p^t\bigl[p+1+3(p-1)(k-2t)\bigr]
+\left(1-p^{-2}\right)\sum_{t=m}^{k-1}p^{k-t}.
\tag{2}
\]
Both sums are elementary. Substitute
\[
\sum_{t=0}^{m-1}p^t=\frac{p^m-1}{p-1},\qquad
\sum_{t=0}^{m-1}tp^t=\frac{p-mp^m+(m-1)p^{m+1}}{(p-1)^2},
\]
and \(\sum_{t=m}^{k-1}p^{k-t}=p(p^{k-m}-1)/(p-1)\). Simplifying separately for \(k=2m\) and \(k=2m+1\) produces the displayed closed forms. Finally, the terms linear in \(k\) are negligible relative to \(p^{k/2}\), and the parity-dependent limits follow immediately. Every step is finite and exact.

## Verification

The accompanying standalone `verify.py` uses exact rational arithmetic. It compares three separately implemented forms: direct enumeration of coefficient tuples for monic cubics, direct enumeration of all ordered triples via their Vandermonde valuation weights, and the closed formula. It additionally enumerates monic quartics in three cases and compares the reduced valuation sum with the closed formula for five primes and the first twenty exponents. The observed result is:

`VERIFY_OK cubic_full_enumerations=11 quartic_full_enumerations=3 smith_triple_checks=11 symbolic_group_checks=100 exact_arithmetic=yes`

Run using `python3 verify.py`. The finite computations corroborate, but do not replace, the proof for all primes, degrees and exponents.

## Relationship to prior work

Simhi's 2026 paper on squarefree values of random polynomials studies local root counts modulo \(p^2\), uses pairwise coefficient congruences and proves bounds for arbitrary fixed moments in that square-modulus model. Equation (2) here gives an exact *third* moment for **every** prime-power exponent, including the explicit parity transition and large-exponent scale. Bhargava–Cremona–Fisher–Gajović and Caruso study the number and correlations of actual \(p\)-adic roots; those are not the same statistic as roots modulo \(p^k\), which can include large singular clusters not lifting to genuine roots. Related finite-modulus root laws at exponents two and three do not alone imply the unrestricted formula.

## Limitations

The result makes no claim about fourth or higher moments, the full finite-modulus root-count distribution, or degrees below three. The formula is for uniform independent coefficients, not conditioned primitive or squarefree polynomials. The novelty assessment is based on inspected relevant literature and searches, not an exhaustive priority certificate; an earlier equivalent formula in the literature on congruence roots remains possible. No independent external mathematical audit has been performed.

## References

1. O. Simhi, *Squarefree values of random polynomials are Gaussian mixtures*, arXiv:2610.29911v1, first submitted 21 October 2026; especially §§2, 3.1, 5 (https://arxiv.org/html/2610.29911v1).
2. M. Bhargava, J. Cremona, T. Fisher and S. Gajović, *The density of polynomials of degree n over \(\mathbb Z_p\) having exactly r roots in \(\mathbb Q_p\)*, Proceedings of the London Mathematical Society, 2022, DOI:10.1112/plms.12438 (https://doi.org/10.1112/plms.12438).
3. X. Caruso, *Where are the zeroes of a random p-adic polynomial?*, Forum of Mathematics, Sigma 10 (2022), e55, DOI:10.1017/fms.2022.27 (https://doi.org/10.1017/fms.2022.27).
