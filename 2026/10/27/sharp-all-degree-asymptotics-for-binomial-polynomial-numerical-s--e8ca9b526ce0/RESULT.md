# Sharp Frobenius and genus asymptotics for binomial-polynomial semigroups of fixed degree at least three

## Finding

Fix an integer \(d\ge3\). For coprime integers \(a\ge2\) and \(b\ge1\), define
\[
S_d(a,b)=\left\langle ai+b\binom{i}{d}:i=1,2,\ldots\right\rangle,
\qquad c_d=(d!)^{1/d},\qquad \eta_d=(d-1)/d^2.
\]
The Frobenius number and genus satisfy
\[
\begin{aligned}
F_d(a,b)&=(a-1)b+c_d a^{1+1/d}+O_d(a^{1+\eta_d}),\\
g_d(a,b)&=\frac{(a-1)(b-1)}2+\frac{d}{d+1}c_d a^{1+1/d}+O_d(a^{1+\eta_d}).
\end{aligned}
\]
The constants in the errors depend on \(d\) alone, so the leading asymptotic after subtracting the displayed elementary \(b\)-term is uniform even when \(b\) varies with \(a\). The contribution concerns degrees \(d\ge3\). The same two degree-two expansions, including their power-saving errors, follow from earlier results [1] and are not claimed as new.

## Assumptions and scope

We set \(\binom{i}{d}=0\) for \(i<d\). The semigroup contains zero and has finite complement among the nonnegative integers, since it contains the coprime pair \(a,da+b\). Its smallest positive element is \(a\). The Frobenius number is the largest missing integer and the genus the number of missing nonnegative integers.

## Proof

**1. Binomial index cost.** For \(n\ge0\), let \(\mu_d(n)\) be the least total index cost \(\sum_{i\ge d} i x_i\) of a representation \(n=\sum_{i\ge d}\binom{i}{d}x_i\) with nonnegative integer multiplicities. The unit coin \(\binom{d}{d}=1\) ensures feasibility, and \(\mu_d(0)=0\). Vandermonde's identity gives \(\binom{u+v}{d}\ge\binom{u}{d}+\binom{v}{d}\). Thus any representation with cost \(M\) has \(n\le\binom{M}{d}\le M^d/d!\), and \(\mu_d(n)\ge c_d n^{1/d}\).

For \(n>0\), choose the largest \(k\ge d\) with \(\binom{k}{d}\le n\). Comparing the defining product for the binomial with \((k-d+1)^d/d!\) and \(k^d/d!\) gives \(k=c_d n^{1/d}+O_d(1)\). The remainder \(r=n-\binom{k}{d}\) is nonnegative, strictly less than \(n\), and less than \(\binom{k}{d-1}\), hence \(r=O_d((n+1)^{(d-1)/d})\). In particular, for all sufficiently large \(n\), depending only on \(d\), \((r+1)^{1/d}\le (n+1)^{1/d}/2\). Choose a constant \(A_d\) large enough to bound \(\mu_d(n)/(n+1)^{1/d}\) on the finite range before this inequality holds and large enough that \(k\le (A_d/2)(n+1)^{1/d}\) for all \(n>0\). By strong induction, adding the greedy coin to an optimal representation of \(r\) gives \(\mu_d(n)\le A_d(n+1)^{1/d}\). Applying this coarse bound only to the remainder of the first coin gives
\[
c_d n^{1/d}\le \mu_d(n)\le c_d n^{1/d}+C_d(n+1)^{\eta_d},
\qquad n\ge0,
\]
because \(\eta_d=(d-1)/d^2\).

**2. Residue minima.** Write \(w_r\) for the least semigroup element congruent to \(br\pmod a\), \(0\le r<a\). A representation of such an element has value \(aM+bK\), where \(K=r+ja\) with an integer \(j\ge0\); for that \(K\) the minimum possible cost \(M\) is \(\mu_d(K)\). Generators of index less than \(d\) add positive multiples of \(a\) and cannot decrease this minimum. Consequently
\[
w_r=br+a\lambda_r,\qquad \lambda_r=\min_{j\ge0}\{\mu_d(r+ja)+bj\}.
\]
For every \(j\) the expression inside the minimum is at least \(c_d r^{1/d}\), and the term \(j=0\) gives the upper estimate \(c_d r^{1/d}+C_d(r+1)^{\eta_d}\). No assertion that the minimizing \(j\) is always zero is required. This estimate is independent of \(b\).

**3. Frobenius and genus.** As \(b\) is invertible modulo \(a\), the \(w_r\) constitute the Apéry set for \(a\). The largest possible gap in a residue is its least semigroup element minus \(a\), and the number of gaps in that residue is the least element minus its least nonnegative representative, divided by \(a\). Hence
\[
F_d=\max_r w_r-a,\qquad
g_d=\frac{1}{a}\sum_r w_r-\frac{a-1}{2}
=\frac{(a-1)(b-1)}2+\sum_r\lambda_r .
\]
In the maximum, using \(r=a-1\) for the lower bound and monotonicity of the envelope's upper bound gives
\[
(a-1)b+ac_d(a-1)^{1/d}-a\le F_d\le
(a-1)b+ac_d(a-1)^{1/d}-a+C_d a^{1+\eta_d}.
\]
The change from \(a(a-1)^{1/d}\) to \(a^{1+1/d}\) is \(O_d(a^{1/d})\), and \(-a\) is also absorbed by the claimed error. For the genus, integral comparison gives \(\sum_{r=0}^{a-1} r^{1/d}=\tfrac{d}{d+1}a^{1+1/d}+O_d(a^{1/d})\), while the sum of the envelope errors is \(O_d(a^{1+\eta_d})\). This proves both formulas uniformly in \(b\).

## Relationship to earlier work

In degree two, Hashuga, Herbine and Jensen [1] study the identical family and the identical cost \(\mu_2\). Their Theorems 6.3 and 6.6 bound it between \(f(n)\) and \(f(n)+3f((f(n)-2)/3)\) for positive \(n\), where \(f(t)=(1+\sqrt{8t+1})/2\). In particular \(\mu_2(n)=\sqrt{2n}+O((n+1)^{1/4})\). Their Corollary 7.6 and Theorem 8.1 express the two invariants by the maximum and sum of their Apéry parametrization outside eight fixed pairs. Inserting this cost estimate in the maximum and sum gives the two expansions with constants \(\sqrt2\) and \(2\sqrt2/3\), both with error \(O(a^{5/4})\) independent of \(b\); enlarging the constant covers the fixed exceptions. Those expansions thus follow from [1], even though its displayed order-of-growth corollaries use weaker bounds.

The higher-degree result uses the cost for \(d\)-th binomial coins and a residue envelope that need not identify its optimizer. Robles-Pérez and Rosales [2] study finite tuples of consecutive triangular or tetrahedral numbers, not mixed generators with the independent parameters \(a,b\). Liu, Xin, Ye and Yin [3] use Apéry methods for generalized repunit systems. Hwang and Song [4] study finite sets of binomial coefficients with a fixed upper index. Those statements do not supply the index-cost estimate and uniform envelope for this mixed family.

## Reproducibility and limitations

The accompanying `verify.py` independently compares the exact residue envelope with shortest paths in the residue graph on a finite grid for degrees 2 through 5. The generator cutoff follows because every residue has a representative using at most \(a-1\) copies of \(da+b\). These checks corroborate the residue description on the tested grid; the proof above establishes the asymptotic bounds. There is no claim of an optimal error exponent, an exact finite-parameter formula, or uniformity when \(d\) grows with \(a\). The literature comparison is limited to the material inspected.

1. M. Hashuga, H. Herbine and A. Jensen, *Numerical Semigroups Generated by Quadratic Sequences*, <https://arxiv.org/abs/2009.01981>, Theorems 6.3, 6.6 and 8.1 and Corollary 7.6.
2. A. M. Robles-Pérez and J. C. Rosales, *The Frobenius number for sequences of triangular and tetrahedral numbers*, <https://arxiv.org/abs/1706.04378>, J. Number Theory 186 (2018), 473–492.
3. F. Liu, G. Xin, S. Ye and J. Yin, *On the Frobenius Number and Genus of a Collection of Semigroups Generalizing Repunit Numerical Semigroups*, <https://arxiv.org/abs/2306.03459>.
4. W. Hwang and K. Song, *The Frobenius Problem for Numerical Semigroups Generated by Binomial Coefficients*, <https://arxiv.org/abs/2412.17882>.
