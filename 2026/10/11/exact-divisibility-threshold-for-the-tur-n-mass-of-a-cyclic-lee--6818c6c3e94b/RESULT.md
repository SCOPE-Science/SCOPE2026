# Exact divisibility threshold for the Turán mass of a cyclic Lee two-ball

## Finding
For each integer \(n\ge5\), let \(G_n=(\mathbb Z/n\mathbb Z)^2\), equipped with counting measure. Let \(e_1,e_2\) be its coordinate generators and put
\[
B_1=\{0,\pm e_1,\pm e_2\},\qquad B_2=B_1-B_1
 =\{(u,v):d_n(u,0)+d_n(v,0)\le2\},
\]
where \(d_n\) is cyclic distance. In particular, \(|B_2|=13\). Define the normalized positive-definite Turán mass
\[
\mathcal T_n=\max\left\{\sum_{g\in G_n}f(g):
 f:G_n\to\mathbb C\text{ is positive definite},\ f(0)=1,
 \operatorname{supp}f\subseteq B_2\right\}.
\]
Then the **exact arithmetic equality criterion** is
\[
\boxed{\mathcal T_n=5\quad\Longleftrightarrow\quad 5\mid n\text{ or }12\mid n.}
\]
For every other \(n\ge5\), one has \(\mathcal T_n>5\). The theorem does not determine the exact value of \(\mathcal T_n\) in those strict cases. The baseline \(5\) is naturally attained for every \(n\) by the normalized autocorrelation of the five-point cross \(B_1\). Thus the result characterizes exactly when that canonical positive-definite witness remains globally optimal.

## Assumptions and scope
A function \(f\) is positive definite when, for arbitrary points \(g_j\in G_n\) and coefficients \(z_j\in\mathbb C\),
\[
\sum_{j,k}f(g_j-g_k)z_j\overline{z_k}\ge0.
\]
Equivalently, the Fourier coefficients \(\widehat f(k,\ell)=\sum_{g\in G_n}f(g)\exp(-2\pi i(k g_1+\ell g_2)/n)\) are all real and nonnegative. The mass in the finding is \(\widehat f(0,0)\), with no division by \(|G_n|\); consequently the normalization is **counting**, not probability, measure. Complex coefficients and nonradial functions are allowed. Taking the real part and averaging over the coordinate swaps and sign changes preserves admissibility and the mass, so the maximum is attained by a real, symmetry-invariant function. The admissible set is compact: \(|f(g)|\le f(0)=1\) follows from positive definiteness.

For such an averaged function set
\[
\begin{aligned}
a&=f(\pm e_1)=f(\pm e_2),\\
b&=f(\pm2e_1)=f(\pm2e_2),\\
c&=f(\pm e_1\pm e_2).
\end{aligned}
\]
Its mass is \(1+4(a+b+c)\). If \(x=\cos(2\pi k/n)\) and \(y=\cos(2\pi\ell/n)\), Fourier positivity is exactly
\[
P_{a,b,c}(x,y)=1+2a(x+y)+2b(2x^2+2y^2-2)+4cxy\ge0
\]
for every \(k,\ell\in\mathbb Z/n\mathbb Z\). Both this formula and the averaging reduction are exact.

## Proof
**1. Canonical lower bound.** Write \(u=\mathbf1_{B_1}\) and \(\widetilde u(g)=u(-g)\). The function
\[
f_0=\frac15(u*\widetilde u)
\]
is positive definite because its Fourier transform is nonnegative. It has \(f_0(0)=1\), support \(B_2\), and total mass \((\sum u)^2/5=5\). Direct difference counting gives
\[
(a_0,b_0,c_0)=(2/5,1/5,2/5).
\]
Writing \(K(x,y)=1+2x+2y\), its Fourier polynomial is exactly
\[
P_{a_0,b_0,c_0}(x,y)=K(x,y)^2/5.
\]
Thus \(\mathcal T_n\ge5\) always.

**2. Universal upper bounds at the two arithmetic resonances.** If \(5\mid n\), sample the Fourier inequality at
\[
x=\cos(2\pi/5)=\frac{\sqrt5-1}{4},\qquad
 y=\cos(4\pi/5)=-\frac{\sqrt5+1}{4}.
\]
These satisfy \(x+y=-1/2\), \(x^2+y^2=3/4\), and \(xy=-1/4\). Consequently
\[
0\le P_{a,b,c}(x,y)=1-a-b-c.
\]
Every admissible function has mass at most \(1+4=5\).

If \(12\mid n\), both sampled pairs \((x,y)=(-1,1/2)\) and \((x,y)=(-1/2,0)\) occur. Their Fourier inequalities respectively read
\[
1-a+b-2c\ge0,\qquad1-a-3b\ge0.
\]
Taking their average yields \(1-a-b-c\ge0\), again giving mass at most \(5\). Along with the baseline, these prove \(\mathcal T_n=5\) whenever \(5\mid n\) or \(12\mid n\).

**3. All zeros of the baseline Fourier polynomial.** The equality \(K(x,y)=0\) is equivalent to
\[
1+z+z^{-1}+w+w^{-1}=0,
\qquad z=e^{2\pi i k/n},\quad w=e^{2\pi i\ell/n}.
\]
We apply the classification of vanishing sums of at most five roots of unity. Lam and Leung prove that with at most two distinct prime divisors, minimal vanishing sums are rotated prime cycles (Theorem 3.3 and Corollary 3.4); for three or more distinct prime divisors, their Lower Bound Theorem 4.8 forces every asymmetric minimal vanishing sum to have weight at least
\[
(p_1-1)(p_2-1)+(p_3-1)\ge(2-1)(3-1)+(5-1)=6.
\]
Hence a vanishing five-term multiset is either a regular five-cycle or the disjoint union of an antipodal pair and an equilateral triple. (A decomposition into smaller minimal pieces can only have sizes \(2+3\); a minimal five-term piece must be a regular five-cycle.)

In the regular five-cycle case \(5\mid n\). Otherwise, the conjugate pairs \(\{z,z^{-1}\}\) and \(\{w,w^{-1}\}\), together with the term \(1\), restrict the possible antipodal pair. A pair across the two conjugate pairs would force its conjugate to be another antipodal pair, leaving the term \(1\) uncancelled, so cannot occur. If \(1\) is paired with \(z\) or \(w\), the corresponding root is \(-1\) and the other conjugate pair sums to \(1\); the sampled cosine pair is \((-1,1/2)\) up to coordinate swap, requiring \(6\mid n\). If an inverse pair is itself antipodal, that pair's cosine is \(0\) and the remaining conjugate pair sums to \(-1\); the cosine pair is \((0,-1/2)\) up to swap, requiring \(12\mid n\). These are all possibilities and each occurs at the stated divisibility threshold.

It follows that if \(5\nmid n\) and \(12\nmid n\), then the grid zeros of \(K\) are either absent (when \(6\nmid n\)) or **exactly** the points \((-1,1/2)\) and \((1/2,-1)\) (when \(6\mid n\)). This is the key finite-cyclotomic rigidity statement; no inference from a bounded numerical search is used.

**4. Strict improvement when the baseline has no zeros.** Suppose \(5\nmid n\) and \(6\nmid n\). The finitely many grid values \(P_0=K^2/5\) have a positive minimum \(m_n\). For any \(0<\varepsilon<m_n/2\), put
\[
f_\varepsilon=(1+\varepsilon)f_0-\varepsilon\delta_0.
\]
It has the same support restriction, \(f_\varepsilon(0)=1\), and Fourier values \((1+\varepsilon)P_0-\varepsilon\ge P_0-\varepsilon>0\), so is positive definite. Its total mass is \(5+4\varepsilon>5\).

**5. Strict improvement when just the sixfold contacts remain.** Suppose \(6\mid n\), \(5\nmid n\), and \(12\nmid n\). Set
\[
(a_\varepsilon,b_\varepsilon,c_\varepsilon)
=(2/5+\varepsilon,\ 1/5+3\varepsilon,\ 2/5+\varepsilon).
\]
The Fourier polynomial is \(P_\varepsilon=P_0+\varepsilon R\), where
\[
R(x,y)=2(x+y)+6(2x^2+2y^2-2)+4xy.
\]
At the *only* zeros of \(P_0\), namely \((-1,1/2)\) and its swap, the exact value is \(R=-1+3-2=0\). At every other grid point \(P_0>0\). Since the grid is finite, some \(\varepsilon>0\) makes \(P_\varepsilon\ge0\) everywhere. The resulting positive-definite function has mass \(5+20\varepsilon>5\). This completes all cases and proves the equivalence.

## Verification
A self-contained standard-library script `checker.py` enumerates the exact integer differences of \(B_1\) on cyclic tori of orders \(5\) through \(40\), verifies the three radial autocorrelation coefficients, and gives a **rational** strict witness for \(n=6\):
\[
(a,b,c)=(3/7,2/7,3/7),\qquad
\sum_{g\in G_6}f(g)=39/7>5.
\]
For this witness every Fourier value is a nonnegative rational, because the sampled cosines are among \(\{1,1/2,-1/2,-1\}\); all sixteen ordered cosine pairs are checked exactly. The script additionally tests the complete baseline-zero contact classification and both perturbation mechanisms numerically for \(5\le n\le240\). It prints `CHECKER_PASS` on success. These tests are supplementary only. The all-order theorem is established by the analytic Fourier inequalities plus the cited structural theorem on vanishing root sums.

## Relationship to prior work
Kolountzakis and Révész give the general positive-definite Turán formulation on locally compact abelian groups and establish packing and spectral upper bounds for finite groups (Theorems 2 and 4). Berdysheva and Révész study the generalized Turán/Delsarte problem and packing-type upper estimates, including finite-group settings (Theorem 1.1). These furnish the natural framework and explain the five-point autocorrelation baseline, but the inspected statements do not give the exact criterion on the thirteen-point Lee ball of a square finite torus. In particular, the two-contact upper certificate at the twelvefold resonance and the strict perturbation when only sixfold zeros occur are additional assertions needing proof.

Lam and Leung's structural results on short vanishing root-of-unity sums yield the exact list of possible baseline Fourier zeros; they do not themselves optimize the positive-definite mass. Other published finite-grid calculations for a five-point subset of a *one-dimensional* cyclic group and for a Boolean weight-two Hamming shell concern different groups/support geometries and neither statement implies this square-torus criterion. Exact implication comparisons, not merely differing terminology, distinguish these settings.

## Limitations
This theorem determines **when the value is exactly five**, and proves strict excess otherwise. It does not give closed forms for the optimal excesses, all optimizer faces, nonsquare rectangular tori, or higher-dimensional Lee balls. The prime-cycle classification is an invoked published theorem, with its hypotheses and specialized consequences stated explicitly. A differently indexed older calculation of this particular finite-grid Turán mass remains a literature risk; unsuccessful searches alone are not a proof of novelty. Numerical grid testing is not offered as an infinite certificate. Counting-measure normalization must be retained when comparing constants.

## References
1. E. E. Berdysheva and S. Gy. Révész, *Delsarte's extremal problem and packing on locally compact abelian groups*, arXiv:1904.03614, first public 7 April 2019; primary MSC 43A35, 05B40. Definitions and Theorem 1.1.
2. M. N. Kolountzakis and S. Gy. Révész, *Turán's extremal problem for positive definite functions on groups*, arXiv:math/0312218, first public 10 December 2003; Theorems 2 and 4.
3. T. Y. Lam and K. H. Leung, *On vanishing sums of roots of unity*, arXiv:math/9511209, first public 13 November 1995, *Journal of Algebra* 224 (2000), 91–109; Theorem 3.3, Corollary 3.4, and Lower Bound Theorem 4.8.
