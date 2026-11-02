# Exact four-agent mixing law for circle-distance facility mechanisms

## Finding

For four agents located anywhere on a continuous circle, the exact approximation factor of every fixed mixture of Random Dictator (RD) and Even Proportional Circle Distance (EPCD) is

\[
\sup_{\mathbf{x}:\operatorname{OPT}(\mathbf{x})>0}
\frac{\mathbb{E}\operatorname{SC}(M_{\lambda}(\mathbf{x}))}
{\operatorname{OPT}(\mathbf{x})}
=\frac{5+\lambda}{4},\qquad 0\le\lambda\le1,
\]

where \(M_{\lambda}=\lambda\operatorname{RD}+(1-\lambda)\operatorname{EPCD}\). In particular EPCD alone has sharp factor \(5/4\), the published equal-weight mixture MRP has sharp four-agent factor \(11/8\), and RD has sharp factor \(3/2\). All factors are attained by two coincident reports at the middle of a semicircle and one report at each quarter-circle endpoint. When \(0\le\lambda<1\), this is the only extremal profile up to rotation, reflection and agent permutation (for nonzero optimal cost).

This is an exact finite-population theorem about these specified mechanisms, not a lower bound on all truthful mechanisms or on populations other than four.

## Assumptions and scope

Fix the circle \(\mathbb{R}/\mathbb{Z}\) of circumference \(1\) with geodesic distance \(d(x,y)=\min\{|x-y|,1-|x-y|\}\), using representatives whose absolute difference is at most \(1\). A profile \(\mathbf{x}=(x_1,x_2,x_3,x_4)\) is a multiset of four reports; coincident reports are allowed. For a possible facility \(y\), define \(\operatorname{SC}(\mathbf{x},y)=\sum_{i=1}^{4}d(x_i,y)\) and \(\operatorname{OPT}(\mathbf{x})=\min_y\operatorname{SC}(\mathbf{x},y)\). Ratios are considered only when \(\operatorname{OPT}>0\), as all mechanisms below are cost-zero on the collocated case.

RD selects one of the four reported copies uniformly. For any ordered three-report circular profile, PCD selects a report with probability equal to the clockwise gap between the other two ordered reports that does not contain the selected report; if several copies coincide, their probabilities are added. EPCD first deletes one of four report copies uniformly and then runs three-report PCD on the remaining copies, while social cost is always evaluated on *all four* original agents. The published equivalent probability formula (Chan, Lin and Wang, Eq. (2.1)) is: for clockwise ordered copies \(z_1,z_2,z_3,z_4\) with gaps \(g_i\) from \(z_i\) to \(z_{i+1}\), indexed cyclically,

\[
\Pr(\operatorname{EPCD}=z_i)=\tfrac12(g_{i+1}+g_{i+2}).
\]

The mixture weight \(\lambda\) is fixed independently of the reports and belongs to \([0,1]\). The benchmark is the unconstrained optimal single facility on the same circle. No assumptions of distinct locations or generic position are made.

## Proof

**1. An optimal report and a four-point normal form.** As the facility moves around the circle, its total-distance function is continuous and piecewise linear. At a report the directional slope jumps upward, and at its antipode it jumps downward. A global minimum is therefore attained at some report: an isolated minimum requires an upward slope jump, while any flat minimizing interval can be followed to an endpoint with an upward jump. Translate such an optimal report to \(0\).

Let \(P\) be the number of strictly clockwise reports in \((0,1/2)\), \(N\) the number in \((-1/2,0)\), \(H\) the number at the antipode and \(Z\) the number at \(0\), counting the distinguished optimal report. The left and right derivatives at \(0\) are \(N+H-P-Z\) and \(N+Z-P-H\). Since the left derivative is nonpositive and the right derivative is nonnegative, \(P+H\le2\) and \(N+H\le2\). Reflection if needed, and distributing zero and antipodal copies consistently among the two sides, now gives a cyclic representative

\[
(-a,\ 0,\ b,\ c),\qquad 0\le a\le\tfrac12,\quad 0\le b\le c\le\tfrac12,
\]

in which \(0\) is optimal. The cost at that location is \(D_0=a+b+c=\operatorname{OPT}\). This representation includes zero gaps and antipodal coincidences; no genericity limit is used.

**2. Exact mechanism probabilities and costs.** Write \(f(t)=\min\{t,1-t\}\) for \(0\le t\le1\). The social costs at the four ordered copies, in the above order, are

\[
\begin{aligned}
D_{-a}&=a+f(a+b)+f(a+c),\\
D_0&=a+b+c,\\
D_b&=c+f(a+b),\\
D_c&=2c-b+f(a+c).
\end{aligned}
\]

The clockwise gaps are \(a,b,c-b,1-a-c\). Substituting them into the EPCD formula yields the respective probabilities

\[
\bigl(c/2,\ (1-a-b)/2,\ (1-c)/2,\ (a+b)/2\bigr).
\]

Thus the exact expected EPCD cost is

\[
C_E=\tfrac c2D_{-a}+\tfrac{1-a-b}{2}D_0
+\tfrac{1-c}{2}D_b+\tfrac{a+b}{2}D_c.
\]

**3. The sharp \(5/4\) inequality.** Let \(F=5D_0-4C_E\). There are exactly three regimes because \(b\le c\). The displayed formulas below follow by expanding the previous expressions and substituting the appropriate branches of \(f\).

If \(a+c\le1/2\), writing \(u=a+c\) gives

\[
F=u(1-2u)+2(c-a-b)^2+2b^2+b\ge0.
\]

If \(a+b\le1/2\le a+c\), writing \(s=a+b\) and \(t=s+c\) gives

\[
F=t(2t-1)+2(s-c)^2\ge0,
\]

because \(t\ge1/2\). If \(a+b\ge1/2\), writing \(s=a+b\) gives

\[
F=4s^2+3s+4c^2-c-2
\ge \tfrac12-\tfrac1{16}=\tfrac7{16}>0.
\]

The cases overlap consistently at their boundaries. Hence \(C_E\le5\operatorname{OPT}/4\) for every four-report circular profile. Equality with \(\operatorname{OPT}>0\) in the first regime requires \(u=1/2\), \(c=a+b\) and \(b=0\), giving \(a=c=1/4\). Equality in the second regime requires \(t=1/2\), \(s=c=1/4\), and the regime condition \(a+c\ge1/2\) forces \(b=0\), again giving \(a=c=1/4\). Equality in the third regime is impossible. This establishes the asserted rigidity of EPCD extremizers.

**4. RD and mixtures.** For any four points in any metric space and any optimal facility \(y^*\), the triangle inequality gives

\[
C_R=\tfrac14\sum_{i,j}d(x_i,x_j)
\le\tfrac{2(4-1)}4\sum_i d(x_i,y^*)
=\tfrac32\operatorname{OPT}.
\]

Therefore, for every \(\lambda\in[0,1]\),

\[
C_{\lambda}=\lambda C_R+(1-\lambda)C_E
\le\left(\tfrac{3\lambda}{2}+\tfrac{5(1-\lambda)}4\right)\operatorname{OPT}
=\tfrac{5+\lambda}{4}\operatorname{OPT}.
\]

For the concrete profile \((-1/4,0,0,1/4)\), direct evaluation gives \(\operatorname{OPT}=1/2\), \(C_R=3/4\) and \(C_E=5/8\). The ratio therefore equals \((5+\lambda)/4\) for *every* \(\lambda\), proving sharpness. If \(\lambda<1\), equality in the mixture requires equality in the EPCD bound; its preceding equality classification proves rigidity. (No uniqueness claim is made for RD alone, \(\lambda=1\).) \(\square\)

## Verification

The standalone standard-library Python program `check_circle4.py` independently calculates EPCD both by random deletion followed by PCD and by the direct four-gap formula. With exact rational arithmetic it checked all \(30{,}636\) four-report circular profiles with one report fixed at zero on grids of denominators \(24\), \(36\) and \(48\), plus \(6{,}500\) seeded additional rational profiles: \(37{,}136\) profiles overall. It checks the separate RD, EPCD and equal-mixture inequalities as well as a seeded random mixture weight, and verifies all three symbolic case identities on \(4{,}851\) rational parameter triples. A separate symbolic-polynomial expansion confirms that each algebraic identity holds formally; the paper proof, not the finite sampling, establishes the universal result. Reproduce with `python check_circle4.py` (Python 3.10 or later, standard library only); the program prints `PASS exact rational checks` on completion.

## Relationship to prior work

Chan, Lin and Wang (first public September 11, 2026) introduce EPCD through random deletion and prove a population-uniform \(3/2\) bound for the equal-weight MRP mixture. Their Theorem 1 and asymptotic Proposition 1 do not identify the exact four-agent bound, and their four-agent general-mechanism lower bound concerns a different optimization (all strategyproof mechanisms). In fact their asymptotic construction uses the even-population parameter \(k\ge3\), not the exceptional four-agent case \(k=2\). The present theorem gives the exact four-agent EPCD bound, exact four-agent MRP bound and the entire fixed-weight mixture law.

Rogowski and Dziubiński (2025) study RD–PCD mixtures for odd populations, so do not cover four-agent EPCD. Meir (2019) studies three-agent PCD; its \(5/4\) bound does not immediately extend through random deletion because a deleted voter still contributes to four-voter social cost. The proof above addresses this issue explicitly.

## Limitations

The conclusion is for *four* reports on the continuous shortest-arc metric circle and for the *specified* fixed-weight RD–EPCD mixtures. It neither determines the best possible strategyproof four-agent rule nor asserts a finite-population formula at larger sizes. Exhaustive checks are over finite grids only, while the theorem relies on the analytic proof. Priority cannot be ruled out against unindexed equivalent work; independent scientific review remains unperformed.

## References

- H. Chan, J. Lin and C. Wang, *A Randomized \(3/2\)-Approximation for Strategic Facility Location on a Circle*, arXiv:2609.12792, first public September 11, 2026. https://arxiv.org/abs/2609.12792
- K. Rogowski and M. Dziubiński, *Improved Approximation Ratio for Strategyproof Facility Location on a Cycle*, arXiv:2505.12943, first public May 19, 2025. https://arxiv.org/abs/2505.12943
- R. Meir, *Strategyproof Facility Location for Three Agents on a Circle*, arXiv:1902.08070, first public February 21, 2019. https://arxiv.org/abs/1902.08070
