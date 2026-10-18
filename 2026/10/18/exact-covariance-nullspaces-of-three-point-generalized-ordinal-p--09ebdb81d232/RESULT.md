# Exact covariance nullspaces of three-point generalized ordinal patterns

## Finding
Let \(X_1,X_2,\ldots\) be independent and identically distributed on a **finite, totally ordered alphabet** \(\mathcal A\), with all \(q=|\mathcal A|\) symbol probabilities strictly positive. The length-three generalized ordinal pattern \(\Pi_i\) records every strict comparison and tie among \((X_i,X_{i+1},X_{i+2})\). Write \(\mathcal P_3\) for the thirteen weak-order patterns (rank vectors whose distinct entries are consecutive integers starting at zero), and put
\[
\widehat p_{n,\pi}=\frac1{n-2}\sum_{i=1}^{n-2}{\bf1}\{\Pi_i=\pi\},\qquad p_\pi=\Pr(\Pi_1=\pi),\quad n\ge3.
\]
Let \(\Sigma=\lim_{n\to\infty}n\operatorname{Cov}(\widehat p_n)\), with coordinates in \(\mathcal P_3\). The limit exists, and its rank is **exactly**
\[
\boxed{\operatorname{rank}\Sigma=\begin{cases}0,&q=1,\\3,&q=2,\\10,&q\ge3.\end{cases}}
\]
The rank depends only on the number of positively supported ordered symbols, **not** on their probabilities. More precisely, define the thirteen-component vectors
\[
{\bf1}(\pi)=1,\quad U(\pi)={\bf1}\{\pi_1<\pi_2\}-{\bf1}\{\pi_2<\pi_3\},\quad D(\pi)={\bf1}\{\pi_1>\pi_2\}-{\bf1}\{\pi_2>\pi_3\}.
\]
If \(q\ge3\), then
\[
\boxed{\ker\Sigma=\operatorname{span}\{{\bf1},U,D\}.}
\]
If \(q=2\), six strict three-distinct-value patterns are impossible and produce six independent zero-coordinate vectors; among the seven possible patterns, the nullspace has basis consisting of the restrictions of \({\bf1},U,D\) and the additional vector
\[
W(\pi)={\bf1}\{\pi=(1,1,0)\}-{\bf1}\{\pi=(0,1,1)\}.
\]
If \(q=1\), the empirical pattern vector is deterministic. For \(q\ge2\), the multivariate two-dependent central limit theorem holds:
\[
\sqrt n(\widehat p_n-p)\ \Longrightarrow\ N_{13}(0,\Sigma).
\]
For a *specified* null alphabet law, a quadratic statistic using \(\Sigma^+\) (Moore--Penrose inverse) consequently has asymptotic \(\chi^2_3\) calibration for two symbols and \(\chi^2_{10}\) for at least three. This statement does not assume unknown symbol probabilities can be replaced without adjusting the limit.

## Assumptions and scope
All samples are iid, all \(q\) alphabet masses are strictly positive, and the ordering of the alphabet is fixed. The pattern associated with a triple \((a,b,c)\) is its relative-rank vector: for example \((a,a,b)\) with \(a<b\) gives \((0,0,1)\), and \((a,b,c)\) with \(a<b<c\) gives \((0,1,2)\). All thirteen possible pattern coordinates are included even when some are deterministically zero. The limit is taken with fixed \(q\) and fixed symbol probabilities as \(n\to\infty\).

## Proof
**Step 1: A zero-asymptotic-variance criterion.** For an arbitrary real function \(f:\mathcal A^3\to\mathbb R\), write \(\mu=\mathbb Ef(X_1,X_2,X_3)\) and its orthogonal iid Hoeffding expansion as
\[
f(a,b,c)-\mu=f_1(a)+f_2(b)+f_3(c)+f_{12}(a,b)+f_{13}(a,c)+f_{23}(b,c)+f_{123}(a,b,c).
\]
Each nonempty-coordinate term is conditionally centered in each of its arguments. When summing over successive length-three windows, the bulk one-coordinate term is \(f_1+f_2+f_3\), the adjacent-coordinate term is \(f_{12}+f_{23}\), the lag-two term is \(f_{13}\), and the three-coordinate term is \(f_{123}\). Distinct nonempty coordinate sets carry orthogonal Hoeffding components; boundary contributions are of bounded second moment. Consequently, exactly,
\[
\lim_{n\to\infty}\frac1n\operatorname{Var}\Big(\sum_{i=1}^{n}f(X_i,X_{i+1},X_{i+2})\Big)
=\|f_1+f_2+f_3\|_2^2+\|f_{12}+f_{23}\|_2^2+\|f_{13}\|_2^2+\|f_{123}\|_2^2.
\]
Thus this asymptotic variance vanishes if and only if the four displayed functions vanish. In that case, setting \(h(a,b)=f_1(a)-f_3(b)+f_{12}(a,b)\) yields
\[
\boxed{f(a,b,c)=\mu+h(a,b)-h(b,c)}
\]
for every triple in the full support. The converse follows by telescoping: its sum differs from \(n\mu\) by \(h(X_1,X_2)-h(X_{n+1},X_{n+2})\), whose variance is bounded. Positivity of all alphabet masses makes the identities pointwise, not merely almost sure.

**Step 2: Characterize pattern-constant coboundaries for at least three symbols.** Fix a vector \(v\) of pattern scores and let \(f(a,b,c)=v(\operatorname{pat}(a,b,c))\). By Step 1, \(v\in\ker\Sigma\) precisely when \(f=\mu+h(a,b)-h(b,c)\). For equal triples, \(\mu=v(0,0,0)\). Subtract this common value from every score. Write \(A=v(0,0,1)-\mu\), \(B=v(1,1,0)-\mu\), and \(H_a=h(a,a)\). For each \(a<b\), the words \(aab\) and \(abb\) give
\[
h(a,b)=H_a-A,\qquad H_a-H_b=A+\bigl(v(0,1,1)-\mu\bigr).
\]
The right side of the second equation is the *same* for every ordered pair. With any three symbols \(a<b<c\), add the equations for \((a,b)\) and \((b,c)\) and compare with \((a,c)\): their common value must be zero. Hence \(H_a=H_b\) for all symbols. The words \(bba\) similarly give \(h(b,a)=H-B\). Therefore
\[
h(a,b)=H-A{\bf1}\{a<b\}-B{\bf1}\{a>b\}.
\]
Its edge difference is a linear combination of the two telescoping comparison contrasts \(U,D\). Together with the constant contrast, they are linearly independent on three distinct alphabet symbols; hence \(\ker\Sigma\) has dimension three and \(\operatorname{rank}\Sigma=13-3=10\), with no restriction on positive symbol masses.

**Step 3: Two or one symbol.** When \(\mathcal A=\{0,1\}\), only seven weak-order patterns occur. A coboundary is determined by four values \(h(0,0),h(0,1),h(1,0),h(1,1)\) modulo one additive constant, together with \(\mu\). This four-dimensional family of pattern scores is spanned by \({\bf1},U,D,W\): the extra direction \(W\) is the edge difference of \(h(a,b)={\bf1}\{a=b=1\}\). Thus the seven supported coordinates have covariance rank \(7-4=3\); the six forbidden coordinates contribute six additional null directions in the complete thirteen-dimensional space. For \(q=1\), every triple has pattern \((0,0,0)\), so \(\Sigma=0\).

**Step 4: Existence and limiting normality.** The centered pattern indicator vectors form a bounded stationary two-dependent process. The covariance limit is the sum of the lag-zero covariance and both directions of lags one and two. The classical finite-dependence central limit theorem, applied by Cramér--Wold, gives the stated possibly degenerate multivariate Gaussian limit. The rank and kernel characterization from Steps 1--3 applies to precisely that covariance.

## Verification
Run `python verify.py` using the Python standard library. The checker enumerates all length-three, four and five words with rational product probabilities, constructs the exact thirteen-by-thirteen long-run covariance by lags zero, one and two, performs exact fraction-preserving Gaussian elimination, and checks its null vectors. It tests one one-point, three two-point, three three-point and two four-point positive probability vectors. All nine cases returned the stated ranks (zero, three or ten), and every claimed null vector was annihilated exactly. These finite checks independently corroborate the identities but are not used as an infinite-parameter proof.

## Relationship to prior work
Weiß and Schnurr (2023) introduced bootstrap tests based on weak-order patterns of discrete time series and calculated pattern probabilities and asymptotic covariance information, including explicit two-point-pattern formulas (Proposition 3.1). Those results motivate identifying the effective dimension of the *thirteen* overlapping three-point-pattern frequencies, but do not state the probability-independent full nullspace classification given here. Schnurr and Fischer (2024) develop tie-aware generalized patterns and limit theorems, without an analogous support-cardinality covariance-rank classification. Bandt (2022) analyzes covariance eigenstructure of the **six tie-free** length-three permutations under continuous iid data: its four nonzero modes differ from the present discrete/tied thirteen-coordinate setting. The overlap between these bodies of work is the use of ordinal patterns and finite-dependent Gaussian limits; the full discrete-alphabet rank jump and the additional binary telescoping relation are the present claim.

## Limitations
This theorem concerns fixed finite alphabets with positive masses, length-three overlapping windows, and the iid null. It makes no claim for infinite alphabets, varying alphabets, dependent alternatives, parameter-estimation-adjusted quadratic tests, or higher-length patterns. The numerical checker samples finitely many rational laws and cannot establish historical priority; that assessment requires separate literature review. The closest primary article appeared online on July 10, 2023, before its 2024 print issue.

## References
1. C. H. Weiß and A. Schnurr, *Generalized ordinal patterns in discrete-valued time series: nonparametric testing for serial dependence*, Journal of Nonparametric Statistics 36 (2024), 573--599, online July 10, 2023. DOI: 10.1080/10485252.2023.2231565.
2. A. Schnurr and S. Fischer, *Generalized Ordinal Patterns Allowing for Ties and Their Applications in Hydrology*, arXiv:2401.12268, initial submission January 22, 2024.
3. C. Bandt, *Statistics and modelling of order patterns in univariate time series*, arXiv:2212.14386, initial submission December 29, 2022; see Section IV on six strict patterns and their covariance contrasts.
