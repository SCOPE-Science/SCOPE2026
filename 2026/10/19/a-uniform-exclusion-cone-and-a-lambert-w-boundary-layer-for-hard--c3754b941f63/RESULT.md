# A uniform exclusion cone and a Lambert-W boundary layer for Hardy least-squares inverses

## Finding

Let \(H^2\) be the Hardy Hilbert space on the unit disk, with \(\|\sum_{j\ge0}a_jz^j\|_{H^2}^2=\sum_{j\ge0}|a_j|^2\). For every integer \(n\ge1\), let \(q_n\) minimize \(\|1-(1-z)q\|_{H^2}\) over all complex polynomials \(q\) of degree at most \(n\). Then every zero \(z\) of \(q_n\) satisfies

\[
\operatorname{Re}(z-1)<|\operatorname{Im}(z-1)|.
\]

Thus the *entire* closed sector \(\{1+w:w\ne0,\ |\arg w|\le\pi/4\}\) is zero-free simultaneously for all degrees. The boundary point \(z=1\) is also never a zero.

There is a complementary complete local description near this singular boundary point. Set \(m=n+2\) and

\[
F_m(w)=\frac{q_n(1+w/m)}{m},\qquad
F(w)=\begin{cases}\dfrac{e^w-1-w}{w^2},&w\ne0,\\[4pt]1/2,&w=0.\end{cases}
\]

Then \(F_m\to F\) locally uniformly on \(\mathbb C\). If \(\Omega\) is any bounded Jordan domain on whose boundary \(F\) has no zeros, then \(F_m\) and \(F\) have, for every sufficiently large \(m\), exactly the same number of zeros in \(\Omega\), counted with multiplicity. Each nonzero root \(w_0\) of \(e^{w_0}=1+w_0\) is simple and has a unique nearby branch of zeros of \(q_n\) given by

\[
z_n=1+\frac{w_0}{m}+\frac{w_0(1+w_0)}{2m^2}+O_{w_0}(m^{-3}).
\]

Conversely, every bounded sequence of scaled zeros has accumulation points among these nonzero roots. In particular, one such root is \(w_0=2.088843015613\ldots+7.461489285654\ldots i\); its argument is \(74.360416574\ldots\) degrees. The half-angle \(\pi/4\) is **not claimed sharp**; this explicit branch rules out any universally zero-free outward sector with half-angle exceeding \(\arg w_0\).

## Assumptions and scope

The norm is the standard coefficient norm in \(H^2\), the target is the reciprocal of \(f(z)=1-z\), the polynomial degree is arbitrary but finite, and coefficients may be complex. The global exclusion statement includes every degree \(n\ge1\) and the boundary rays of the sector. The local zero-count statement concerns bounded planar domains with zero-free boundary for \(F\); it does not describe roots whose scaled distance from \(1\) tends to infinity. No assertion is made about optimal approximants for other functions or Hardy exponents.

## Proof

**1. Exact least-squares inverse.** Put \(m=n+2\). Every degree-at-most-\(n+1\) polynomial \(h\) with \(h(1)=1\) can be written uniquely as \(h=1-(1-z)q\) with \(\deg q\le n\). If \(h(z)=\sum_{j=0}^{m-1}b_jz^j\), the constraint is \(\sum b_j=1\). Cauchy--Schwarz yields \(\sum|b_j|^2\ge 1/m\), with equality uniquely at \(b_j=1/m\). Therefore

\[
1-(1-z)q_n(z)=\frac1m\sum_{j=0}^{m-1}z^j,
\qquad q_n(z)=\frac1m\sum_{j=0}^{m-2}(m-1-j)z^j.
\]

In particular \(q_n(1)=(m-1)/2>0\). Multiplying out gives the identity

\[
m(1-z)^2q_n(z)=z^m-mz+(m-1).
\tag{1}
\]

For \(z\ne1\), being a root is equivalent to \(z^m-mz+(m-1)=0\), or, writing \(w=z-1\), to

\[
(1+w)^m=1+mw.\tag{2}
\]

**2. Global exclusion by a strict binomial modulus estimate.** Suppose \(w=a+ib\ne0\) lies in the outward sector: \(a\ge|b|\). Write \(r^2=a^2+b^2\), so \(a>0\) and \(2a^2\ge r^2\). Since \(m\ge3\) and \(2a+r^2>0\), the binomial theorem gives the strict inequality

\[
\begin{aligned}
|1+w|^{2m}&=(1+2a+r^2)^m\\
&>1+m(2a+r^2)+\binom m2(2a+r^2)^2\\
&\ge 1+2ma+mr^2+2m(m-1)a^2\\
&\ge 1+2ma+m^2r^2=|1+mw|^2.
\end{aligned}
\]

Here the last step uses \(2a^2\ge r^2\), and the first strict inequality follows from the positive terms of degree at least three in the binomial expansion. Equation (2) is impossible. Along with \(q_n(1)>0\), this proves the global sector theorem.

**3. Exact boundary rescaling.** Substitution \(z=1+w/m\) in (1) gives the polynomial identity, extended through \(w=0\),

\[
F_m(w)=\frac{q_n(1+w/m)}m
=\frac{(1+w/m)^m-1-w}{w^2}.
\tag{3}
\]

Uniform convergence of \((1+w/m)^m\to e^w\) on compact subsets, including its power series after the first two coefficients are removed, proves \(F_m\to F\) locally uniformly. Rouché's theorem applied on \(\partial\Omega\) proves the stated eventual equality of zero counts; tiny disjoint disks around the distinct zeros give individual convergence. The function \(F\) has no zero at the origin, because \(F(0)=1/2\).

If \(w_0\ne0\) and \(e^{w_0}=1+w_0\), then \((e^w-1-w)'_{w=w_0}=e^{w_0}-1=w_0\ne0\), so \(w_0\) is a simple zero of \(F\). Uniformly on each fixed compact subset,

\[
(1+w/m)^m=e^w\left(1-\frac{w^2}{2m}+O(m^{-2})\right).
\]

The simple-root implicit expansion therefore gives a unique zero of \(F_m\) near \(w_0\), with

\[
w_m=w_0+\frac{w_0(1+w_0)}{2m}+O_{w_0}(m^{-2}),
\qquad z_n=1+\frac{w_m}{m}.
\]

This proves the displayed two-term expansion of \(z_n\). Any bounded sequence \(w_m\) with \(F_m(w_m)=0\) has a convergent subsequence whose limit is a zero of \(F\), by uniform convergence; this also establishes the converse local statement.

**4. Location of all boundary-layer limits.** For every \(w\ne0\),

\[
\frac{e^w-1}{w}=\int_0^1 e^{tw}\,dt.
\]

When \(\operatorname{Re}w<0\), the absolute value of this integral is strictly below one. When \(\operatorname{Re}w=0\) and \(w\ne0\), the strict triangle inequality again gives an absolute value below one. Thus \(e^w=1+w\) forces \(\operatorname{Re}w>0\). Its nonzero roots are given by the nonprincipal branches of \(w=-1-W_k(-e^{-1})\), where \(W_k\) is a branch of the Lambert \(W\) function. These roots are simple, and the displayed numerical root supplies one explicit limiting direction outside the exclusion sector. No minimality of its argument among all roots is asserted.

## Verification

A standalone checker, `opa_sector_verifier.py`, runs 38 exact symbolic polynomial-identity checks (degrees \(1\) through \(38\)), numerical root-angle comparisons for degrees \(1\) through \(16\), and high-precision simple-root tracking for \(m=30,60,120,240,480\). Its output appears in `opa_sector_checks.txt`. The numerical scaled-root remainder multiplied by \(m^2\) stays bounded and approaches a finite constant, corroborating the proved first correction. None of those finite checks is treated as proof for all degrees. The all-degree statements follow from the coefficient minimization, strict binomial inequality, analytic convergence, and Rouché/implicit-root arguments above.

## Relationship to prior work

The exact formula for \(q_n\) is classical and is stated in Bénéteau--Centner (2021, Example 2.2). Their Open Question 2 asks for sectors based at points of the unit circle avoiding optimal-approximant zeros. The present theorem gives one explicit global sector for the canonical boundary-zero example and a complete bounded-scale zero-limit description, not a solution for arbitrary cyclic functions. Bénéteau et al. (2016) prove broad zero-localization and Jentzsch-type accumulation results, which do not give this outward sector or its scaling correction. Orive--Sánchez-Lara--Seco (2025, Section 3.1) give an electrostatic model for the same one-boundary-zero polynomial family and discuss a qualitative zero gap. Their stated results provide neither the displayed uniform \(45\)-degree exclusion nor the specific Lambert-\(W\) boundary-layer correction. The main algebraic ingredient here is elementary and all earlier formulas and qualitative facts are acknowledged.

## Limitations

The half-angle \(\pi/4\) is proved safe, not globally optimal. The quoted numerical root and angle are high-precision computations and not a claim of a certified smallest-angle zero. The local zero description does not quantify global zero distributions along the remaining arcs of the unit circle, and it does not apply to general cyclic functions, higher-order boundary zeros, or other Hardy/Dirichlet weights. A fuller historical search of Cesàro polynomial zero geometry could reveal an equivalent older sector or local-zero formulation; independent literature validation is still needed.

## References

1. C. Bénéteau and R. Centner, *A Survey of optimal polynomial approximants, applications to digital filter design, and related open problems*, arXiv:2102.01725v1, 2021-02-02, Example 2.2 and Open Question 2, https://arxiv.org/html/2102.01725v1 .
2. C. Bénéteau, D. Khavinson, C. Liaw, D. Seco, and B. Simanek, *Zeros of optimal polynomial approximants: Jacobi matrices and Jentzsch-type theorems*, arXiv:1606.08615v1, 2016-06-28, Sections 6--7, https://arxiv.org/pdf/1606.08615 .
3. R. Orive, J. Sánchez-Lara, and D. Seco, *Optimal polynomial approximants and orthogonal polynomials on the unit circle: An electrostatic approach*, arXiv:2507.15488v1, 2025-07-21, Section 3.1, https://arxiv.org/pdf/2507.15488 .
4. R. M. Corless et al., *On the Lambert W Function*, Advances in Computational Mathematics 5 (1996), 329--359, https://www.uwo.ca/apmaths/faculty/jeffrey/pdfs/W-adv-cm.pdf .
