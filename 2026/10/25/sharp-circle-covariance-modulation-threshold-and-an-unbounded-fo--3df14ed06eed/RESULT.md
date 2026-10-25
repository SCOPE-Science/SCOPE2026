# Sharp circle-covariance modulation threshold and an unbounded Fourier-mode staircase

## Finding

Let \(\mathbb S^1=\{e^{it}:t\in\mathbb R/(2\pi\mathbb Z)\}\), with intrinsic distance \(\theta(z,w)\in[0,\pi]\). For every \(a>0\) and \(b\in\mathbb R\), consider the continuous, rotation-invariant kernel
\[
K_{a,b}(z,w)=e^{-a\theta(z,w)}\bigl(1+b\cos\theta(z,w)\bigr).
\]
Put \(A=a^2\), \(h=\tanh(\pi a/2)\), and, for \(t\ge0\),
\[
F_A(t)=\frac{(A+(t-1)^2)(A+(t+1)^2)}{(A+t^2)(A+t^2+1)},\qquad
s_A=\sqrt{\frac{A+1+2\sqrt{4A^2+5A+1}}3}.
\]
For positive integers \(n\), define \(R_n=hF_A(n)\) when \(n\) is even and \(R_n=h^{-1}F_A(n)\) when \(n\) is odd. In each of the two parity classes, take the largest positive integer in that class not exceeding \(s_A\) and the smallest one not less than \(s_A\), counting an index at equality once; if the lower index does not exist, retain the least positive member and its successor. Denote their union by \(\mathcal N_A\); it has at most four elements. Then the explicitly finite minimum
\[
B(a)=\min_{n\in\mathcal N_A}R_n
\]
satisfies \(0<B(a)<h<1\), and the following equivalence is exact:
\[
K_{a,b}\text{ is positive definite on }\mathbb S^1
\quad\Longleftrightarrow\quad b\ge-B(a).
\]
Every admissible kernel, **including the boundary** \(b=-B(a)\), is strictly positive definite on any finite set of distinct points. At the boundary the Fourier coefficients that vanish are precisely the finitely many modes attaining \(B(a)\), together with their negatives.

The critical coefficient has the two distinct regimes
\[
B(a)=\frac{9\pi}{40}a+O(a^3)\quad(a\downarrow0),\qquad
B(a)=1-\frac9{16a^2}+O(a^{-4})\quad(a\to\infty).
\]
Any minimizing positive Fourier frequency satisfies \(n=\sqrt{5/3}\,a+O(1)\) as \(a\to\infty\). Moreover, every sufficiently large integer \(n\) is the **unique** minimizing positive frequency for at least one value of \(a\): one may choose
\[
a=a_n,\qquad a_n^2=\frac{-(n^2+3)+2\sqrt{4n^4-n^2+1}}5.
\]
Thus the active Fourier frequency along the sharp boundary is unbounded and undergoes infinitely many changes as the correlation length changes.

## Assumptions and scope

Only the unit circle with shortest-arc distance is considered; the formulas are not claims for Euclidean space or higher-dimensional spheres. Positive definiteness means that every finite kernel Gram matrix is positive semidefinite; strict positive definiteness means positive definite on distinct points. No normalization to unit diagonal is assumed. For admissible \(b\), the positive number \(1+b\) allows the usual correlation normalization \(K_{a,b}/(1+b)\). The parameter \(a\) is strictly positive, and \(b\) can be any real number.

## Proof

**1. Exact Fourier spectrum.** On the representative angular interval \([-\pi,\pi]\), the kernel profile is \(g(t)=e^{-a|t|}(1+b\cos t)\). Its unmodulated normalized complex Fourier coefficients are, for \(n\in\mathbb Z\),
\[
c_n=\frac1{2\pi}\int_{-\pi}^{\pi}e^{-a|t|}e^{-int}\,dt
=\frac{a\,[1-(-1)^n e^{-\pi a}]}{\pi(A+n^2)}>0.
\]
Multiplication by \(\cos t\) gives coefficients
\[
d_n=c_n+\frac b2(c_{n-1}+c_{n+1}).
\]
The Herglotz criterion on the compact abelian group \(\mathbb S^1\) says that \(K_{a,b}\) is positive definite exactly when \(d_n\ge0\) for every integer \(n\). If \(b\ge0\), all coefficients are positive. If \(b<0\), the criterion becomes \(b\ge-\inf_{n\ge0}2c_n/(c_{n-1}+c_{n+1})\). Direct substitution gives \(2c_n/(c_{n-1}+c_{n+1})=R_n\) for every \(n\ge1\), and the frequency-zero value is
\[
R_0=\frac{c_0}{c_1}=h\frac{A+1}{A}.
\]
Frequency zero cannot be the minimum, since
\[
R_0-R_2=h\frac{20(A+1)}{A(A+4)(A+5)}>0.
\]

**2. Reduction from infinitely many inequalities to four.** Set \(y=t^2\). An exact simplification and differentiation give
\[
F_A(\sqrt y)=1+\frac{A+1-3y}{(A+y)(A+y+1)},
\]
\[
\frac{d}{dy}F_A(\sqrt y)=
\frac{3y^2-(2A+2)y-(5A^2+6A+1)}{(A+y)^2(A+y+1)^2}.
\]
The numerator has one positive and one negative root. Its positive root is precisely \(s_A^2\). Thus \(F_A(t)\) strictly decreases for \(0<t<s_A\) and strictly increases for \(t>s_A\). Within each parity class, the positive integer minimum therefore occurs among the two integers that bracket \(s_A\), with the stated endpoint convention. The factors \(h\) and \(h^{-1}\) are constant within each parity class. This proves the finite formula for \(B(a)\). Also \(F_A(n)<1\) for all sufficiently large even \(n\), because \(A+1-3n^2<0\). Consequently \(0<B(a)<h<1\); in particular the infimum is a genuine finite minimum, and the equivalence follows.

**3. Boundary strictness.** At \(b=-B(a)\), one has \(d_n\ge0\), with \(d_n=0\) exactly when \(R_{|n|}=B(a)\) for \(n\ne0\). The preceding unimodality and \(B(a)<h\) show that only finitely many modes can vanish and \(d_n>0\) for every sufficiently large \(|n|\). At \(b>-B(a)\), all coefficients are positive. In either case, if the quadratic form for distinct \(z_j=e^{it_j}\) and weights \(u_j\) vanished, absolute convergence of the Fourier series and positivity would imply \(\sum_j u_jz_j^m=0\) for all sufficiently large consecutive integers \(m\). The corresponding square Vandermonde matrix is invertible, so every \(u_j=0\). This proves strict positive definiteness even at the sharp boundary.

**4. Two asymptotic regimes.** As \(a\downarrow0\), \(h=\pi a/2+O(a^3)\) and \(F_0(2)=9/20\). Since \(F_0(t)\) strictly increases for \(t>1\), mode \(2\) is the unique minimizing even index for all sufficiently small \(a\). The odd mode \(1\) has \(R_1=4a/\pi+O(a^3)\), while odd modes \(n\ge3\) have values bounded below by a positive constant times \(a^{-1}\), uniformly in \(n\). Since \(9\pi/40<4/\pi\), mode \(2\) is the global minimizer near zero, giving the first expansion.

As \(A\to\infty\), one has \(s_A^2=5A/3+O(1)\). Substitution into the rational formula yields \(F_A(s_A)=1-9/(16A)+O(A^{-2})\). The closest integer of either parity differs from \(s_A\) by at most two, and Taylor's theorem gives a corresponding discrepancy \(O(A^{-2})\), since the second derivative in \(t\) is \(O(A^{-2})\) for \(t\asymp\sqrt A\). Also \(h^{\pm1}=1+O(e^{-\pi a})\). Consequently \(B(a)=1-9/(16a^2)+O(a^{-4})\). The finite-candidate reduction gives \(n=s_A+O(1)=\sqrt{5/3}\,a+O(1)\) for every minimizing frequency.

**5. Every large Fourier frequency becomes uniquely active.** The function \(s_A\) increases continuously from \(1\) to infinity. Solving \(s_A=n\) for \(A\) gives the positive expression \(A=a_n^2\) stated above, for each integer \(n\ge2\). At that parameter, \(F_A(t)\) has its unique real minimum at \(t=n\). Taylor expansion of the explicit rational function near \(n\asymp\sqrt A\) shows the gap between \(F_A(n)\) and each neighboring integer value is bounded below by \(cA^{-2}\) for some fixed \(c>0\) and all sufficiently large \(n\). Unimodality bounds all other integer gaps below by the same order. The parity multipliers differ from \(1\) by only \(O(e^{-\pi\sqrt A})=o(A^{-2})\), uniformly because \(F_A(k)\) is bounded on positive integers. Thus the unique minimizer of \(R_k\) is \(k=n\) for sufficiently large \(n\). Continuity of the coefficients makes the minimizing index locally constant whenever unique. Since arbitrarily large different indices are attained, infinitely many switches must occur.

## Verification

The accompanying standalone `CHECK.py` verifies the exact coefficient formula against direct numerical integration, the derivative and minimizer formulas against centered finite differences, the finite-candidate reduction against long initial Fourier ranges at multiple parameter values, and the asymptotic and large-index mode claims on sample parameters. All infinite and uniform claims are proved analytically above; numerical checks are illustrative and not substitutes for the proof. The checker uses only the Python standard library.

## Relationship to prior work

Gneiting's 2011 preprint (2013 journal version) gives the spherical Schoenberg criterion, its circle Fourier-coefficient specialization, and the completely monotone geodesic exponential class; these are premises, not new discoveries. Feragen–Lauze–Hauberg (2014) establishes positive definiteness of geodesic Laplacian kernels on spaces with conditionally negative definite distance. Porcu–Bevilacqua–Genton (2015 public preprint, 2016 journal) constructs sphere-based spatial, temporal and multivariate covariance models, including exponential baselines. The contribution here is the exact **signed first-harmonic modulation** parameter boundary, its finite Fourier test and its unbounded active-mode staircase; the cited results do not state that parameter boundary or the staircase. Earlier circle-covariance tests of Gneiting (1998) were also considered, but their full text was not accessible in this review; their abstract describes general sufficient and necessary tests rather than this complete signed two-parameter classification. This is a bounded priority assessment, not a claim of exhaustive bibliographic uniqueness.

## Limitations

The result applies to \(\mathbb S^1\) only, not to \(\mathbb S^d\) for \(d\ge2\). At isolated parameter values two or more distinct positive Fourier indices may tie at the boundary, and no exhaustive algebraic classification of those tie values is claimed. The result does not characterize generic higher harmonic multipliers or a full two-dimensional parameter cone. The bounded literature review could miss an equivalent derivation, especially in inaccessible pre-1999 sources. No independent mathematical audit has been performed.

## References

1. T. Gneiting, *Strictly and non-strictly positive definite functions on spheres*, arXiv:1111.7077, first posted 2011-11-30; Bernoulli 19 (2013), 1327–1349. In particular, the circle specialization of Schoenberg coefficients (Theorem 1 and formulas (13)–(14)) and powered exponential example.
2. A. Feragen, F. Lauze, and S. Hauberg, *Geodesic Exponential Kernels: When Curvature and Linearity Conflict*, arXiv:1411.0296, first posted 2014-11-02, especially Theorem 4.
3. E. Porcu, M. Bevilacqua, and M. G. Genton, *Spatio-Temporal Covariance and Cross-Covariance Functions of the Great Circle Distance on a Sphere*, preprint publicly available by 2015-08-05, J. Amer. Statist. Assoc. 111 (2016), 888–898, DOI: 10.1080/01621459.2015.1072541.
4. T. Gneiting, *Simple tests for the validity of correlation function models on the circle*, Statist. Probab. Lett. 39 (1998), 119–122, DOI: 10.1016/S0167-7152(98)00042-X. Abstract-level comparison only; full text unavailable in this review.
