# High-inversion Mallows bias reverses fixed-point covariance at every odd size

## Finding
Let \(n\ge2\) be an integer and \(q>0\). Sample a permutation \(\Pi\in S_n\) with probability
\[
\mathbb P_q(\Pi=\pi)=\frac{q^{J(\pi)}}{Z_n(q)},\qquad
J(\pi)=\#\{(a,b):a<b,\ \pi(a)>\pi(b)\},\qquad
Z_n(q)=\sum_{\pi\in S_n}q^{J(\pi)}.
\]
Write \(F(\pi)=\#\{i:\pi(i)=i\}\) for the fixed-point count and \(J=J(\Pi)\) for the inversion count.

**Finite-size covariance sign theorem.** For every \(n\ge2\),
\[
\operatorname{Cov}_{q=1}(F,J)=-\frac{n+1}{6},\qquad
0<q\le\frac{1}{100n^2}\implies\operatorname{Cov}_{q}(F,J)<0.
\]
At the opposite end of the inversion tilt,
\[
q\ge100n^2\implies
\operatorname{sgn}\operatorname{Cov}_{q}(F,J)
=\begin{cases}+1,&n\text{ odd},\\-1,&n\text{ even}.\end{cases}
\]
Consequently, **for every odd size \(n\ge3\)**, the expected number of fixed points has a strict local minimum at some bias in \((1,100n^2)\), and there is at least one covariance zero there. Increasing the expected inversion count can therefore **increase** the expected number of fixed points. This contradicts the unrestricted Mallows-based monotonicity conjecture discussed in the cited 2024 question on fixed points versus inversions.

The endpoint expansions, for each fixed \(n\), are
\[
\operatorname{Cov}_q(F,J)=-2(n-1)q+O_n(q^2)\quad(q\downarrow0),
\]
\[
\operatorname{Cov}_q(F,J)=
\begin{cases}2/q+O_n(q^{-2}),&n\text{ odd},\\
-2/q+O_n(q^{-2}),&n\text{ even}
\end{cases}\quad(q\to\infty).
\]
For \(n=3\), the complete formula is
\[
\operatorname{Cov}_q(F,J)
=\frac{2q(q^2-2q-2)}{(q^2+q+1)^2},
\]
so the exact and unique sign switch in that size occurs at \(q=1+\sqrt3\).

## Assumptions and scope
The law is the **finite**, one-parameter Mallows distribution weighted by the ordinary inversion statistic, with no conditioning or asymptotic scaling of sample size. The quantities \(n\) and \(q\) range exactly as specified; the global sign for the intermediate range of \(q\) is **not** asserted for even sizes, and the number or uniqueness of crossings for odd sizes beyond \(n=3\) is **not** asserted. All endpoint \(O_n\)-constants may depend on fixed \(n\).

## Proof
**1. Exponential tilt.** Differentiation of the finite partition function gives the identity
\[
q\frac{d}{dq}\mathbb E_q F=\operatorname{Cov}_q(F,J).
\tag{1}
\]
Also, \(q\,d\mathbb E_q J/dq=\operatorname{Var}_q(J)>0\) for all \(n\ge2\); hence the covariance sign determines the derivative of the fixed-point expectation with respect to the expected inversion count.

**2. The unbiased point.** Write \(I_i=\mathbf1\{\Pi(i)=i\}\) and \(X_{ab}=\mathbf1\{\Pi(a)>\Pi(b)\}\) for \(a<b\). Under the uniform law, conditional on \(I_i=1\), the other values remain uniformly permuted. Only \(i=a\) and \(i=b\) contribute to \(\operatorname{Cov}(F,X_{ab})\); explicitly,
\[
\operatorname{Cov}(I_a,X_{ab})=\frac{2a-n-1}{2n(n-1)},\quad
\operatorname{Cov}(I_b,X_{ab})=\frac{n+1-2b}{2n(n-1)}.
\]
Thus \(\operatorname{Cov}(F,X_{ab})=(a-b)/(n(n-1))\), and summing over all \(a<b\) yields
\[
\operatorname{Cov}_{q=1}(F,J)
=-\frac{1}{n(n-1)}\sum_{a<b}(b-a)
=-\frac{n+1}{6}.
\]

**3. Adjacent inversions at the two extrema.** An adjacent transposition changes \(F\) by at most two. Starting at the identity and introducing one inversion by swapping adjacent entries removes exactly two fixed points, at each of \(n-1\) locations.

Starting at the reversing permutation \(r(i)=n+1-i\), there is one fixed point when \(n\) is odd and no fixed points when \(n\) is even. A single adjacent swap decreases the inversion count by one. For odd \(n\), precisely the two swaps adjacent to the central fixed point each destroy one fixed point; all other swaps leave the fixed-point count unchanged. For even \(n\), precisely the central adjacent swap creates two fixed points. Accordingly, the summed first-level fixed-point changes are \(-2(n-1)\) at the identity, \(-2\) at odd reversal, and \(+2\) at even reversal.

**4. A uniform quantitative perturbation lemma.** Work from either extremal permutation and let \(x\) be its small bias parameter: \(x=q\) near the identity, and \(x=1/q\) near reversal. Let \(k\) be the minimal adjacent-swap distance from the extremal permutation. Set \(a_k\) to the number of permutations at distance \(k\), and \(b_k\) to the sum of their \(F-F_0\) values, where \(F_0\) is the extremal fixed-point count. Write
\[
Z(x)=\sum_{k\ge0}a_kx^k,\qquad B(x)=\sum_{k\ge0}b_kx^k,\qquad
\mathbb E_x F=F_0+\frac{B(x)}{Z(x)}.
\]
The inversion-sequence generating product \(Z(x)=\prod_{j=1}^n(1+x+\cdots+x^{j-1})\) implies \(a_k\le n^k\) (the coefficient counts weak compositions into \(n-1\) bounded parts). The adjacent-swap Lipschitz bound gives \(|b_k|\le2ka_k\). In particular, \(a_0=1\), \(b_0=0\), and the first coefficient \(c=b_1\) is one of the three explicit nonzero values in Step 3.

Put \(B(x)=cx+R_B(x)\) and \(s=nx\). For \(0<x\le1/(100n^2)\) one has \(0<s\le1/100\), and the elementary geometric-series bounds are
\[
Z<2,\qquad Z'<2n,\qquad
\left|Z-xZ'-1\right|<2s^2,\qquad
|R_B|<5s^2,\qquad |R_B'|<10ns.
\tag{2}
\]
For example, \(|R_B'|\le2n\sum_{k\ge2}k^2s^{k-1}=2n((1+s)/(1-s)^3-1)<10ns\); the remaining bounds follow from the same series. Hence the derivative numerator satisfies
\[
\left|Z^2\frac{d}{dx}\mathbb E_xF-c\right|
=\left|c(Z-xZ'-1)+R_B'Z-R_BZ'\right|
<4ns^2+20ns+10ns^2\le\frac15+\frac{14}{10000}<1.
\tag{3}
\]
Here \(|c|\le2(n-1)<2n\) and \(ns\le1/100\). Since \(|c|\ge2\) in all three cases, the derivative \(d\mathbb E_xF/dx\) has exactly the sign of \(c\). For \(x=q\), (1) gives negative covariance near zero. For \(x=1/q\), the chain rule gives \(\operatorname{Cov}_q(F,J)=-x(d\mathbb E_xF/dx)\), so the high-bias sign is opposite to \(c\): positive for odd \(n\) and negative for even \(n\). This proves the uniform numerical cutoffs.

**5. Endpoint expansions and crossing.** Since \(Z(0)=1\) and \(B(x)=cx+O_n(x^2)\), (1) and the reverse-bias chain rule give the stated asymptotics. For odd \(n\ge3\), the covariance is negative at \(q=1\) and positive at \(q=100n^2\). Analyticity of finite partition functions for \(q>0\) ensures at least one zero and a strict interior local minimum of \(\mathbb E_qF\). For the first odd case, direct enumeration yields \(Z_3(q)=(1+q)(1+q+q^2)\) and \(\sum_\pi F(\pi)q^{J(\pi)}=3+2q+q^3\). Equation (1) simplifies to the displayed exact rational formula, whose numerator changes sign precisely at \(q=1+\sqrt3\). This completes the proof.

## Verification
Run the included standard-library checker with `python mallows_fixedpoint_checker.py`. It independently enumerates every permutation for \(2\le n\le8\), checks the \(q\)-factorial counts, endpoint-level coefficients, the adjacent-swap Lipschitz inequalities, covariance identities for several positive rational biases, the uniform covariance formula, both quantitative cutoff signs, and the \(n=3\) exact rational identity. The delivered checker returned `PASS: 393 exact checks`. These finite calculations are diagnostic; the proof for every \(n\) is the geometric-series argument of Step 4.

## Relationship to prior work
He (2021) and He–Müller–Verstraaten (2022) study Mallows cycle counts, including strong odd/even differences for odd cycles when the bias is fixed and the permutation size tends to infinity. The latter paper's Theorem 1.6 gives limiting fixed-point expectations along even and odd size subsequences. These asymptotic distributional statements are not the finite-size derivative in (1), its all-size quantitative cutoff, or the explicit finite covariance reversal. The Mallows reversal identity and the inversion-sequence product are established background.

A February 2024 MathOverflow discussion explicitly asks about monotonic dependence of fixed-point expectation on expected inversions under a Mallows model. Its published comments and answers analyze uniform-permutation inversion classes and suggest monotonic behavior but do not give the present finite odd-size reversal. The all-odd-size counterfamily and the exact \(n=3\) threshold directly delimit that question. The statement does not claim uniqueness of the crossing for general odd sizes or monotonicity at every intermediate bias.

## Limitations
This is a finite-size result about covariance and mean response, not stochastic ordering of whole fixed-point distributions. The bound \(100n^2\) is sufficient but not optimized. No uniqueness of an odd-size sign change is claimed beyond \(n=3\), and no all-parameter negative covariance theorem is claimed for even sizes. Full historical priority cannot be guaranteed from accessible sources alone; independent mathematical review remains outstanding.

## References
1. J. He, *A central limit theorem for cycles of Mallows permutations*, initial preprint December 17, 2021, arXiv:2112.09789, https://arxiv.org/abs/2112.09789.
2. J. He, T. Müller, and T. Verstraaten, *Cycles in Mallows random permutations*, initial preprint January 27, 2022, arXiv:2201.11610, https://arxiv.org/abs/2201.11610.
3. *Relationship between fixed points and inversions in permutations*, MathOverflow question (February 7, 2024), with answers and discussion February 8–14, 2024, https://mathoverflow.net/questions/463675/relationship-between-fixed-points-and-inversions-in-permutations.
