# Sharp conductance design for Lipschitz-harmonic extension on metric stars

## Finding
Let \(m\ge3\), and let a metric star have positive arm lengths \(\ell_1,\ldots,\ell_m\). On the leaves take the induced shortest-path distance \(d(v_i,v_j)=\ell_i+\ell_j\). For any positive effective edge conductances \(c_i\), harmonic extension takes the center value \(\sum_i w_i f(v_i)\), where \(w_i=c_i/\sum_j c_j\), and interpolates affinely along the arms. Its exact Lipschitz-seminorm operator norm is
\[
\boxed{\|E_w\|_{\mathrm{Lip}\to\mathrm{Lip}}=\max_{1\le i\le m}\frac{\sum_{j\ne i}w_j(\ell_i+\ell_j)}{\ell_i}.}
\]
Sort the lengths so that \(\ell_1\le\cdots\le\ell_m\). Define \(z_*\) as the unique positive solution to
\[
\sum_{i=1}^m(1-z_*\ell_i)_+=2,
\qquad (s)_+=\max\{s,0\}.
\]
For \(z\ge z_*\) put
\[
b_i(z)=\frac{(1-z\ell_i)_+}{2},\qquad
 e(z)=1-\sum_{i=1}^m b_i(z),\qquad
 D(z)=\sum_{i=1}^m\frac{b_i(z)}{\ell_i}+\frac{e(z)}{\ell_1}.
\]
Then **the sharp infimum over strictly positive conductances** is the following finite exact minimization:
\[
\boxed{\inf_{c_1,\ldots,c_m>0}\|E_c\|_{\mathrm{Lip}\to\mathrm{Lip}}
=1+\min_{z\in\mathcal Z}\frac{z}{D(z)},\qquad
\mathcal Z=\{z_*\}\cup\left\{\frac1{\ell_i}:\frac1{\ell_i}\ge z_*,\ 1\le i\le m\right\}.}
\]
For a minimizing \(z\), define \(a_1=b_1(z)+e(z)\), \(a_i=b_i(z)\) for \(i>1\), and \(w_i=(a_i/\ell_i)/D(z)\). These nonnegative weights realize the same sharp minimum in the closure of the positive-conductance class; they are approached by strictly positive conductances. In particular, not every positive-length star admits a minimizing strictly positive conductance vector.

A sharp phase law occurs when one arm has length \(r\in(0,1]\) and the other \(k=m-1\ge2\) arms have length one:
\[
\boxed{\inf_{c_i>0}\|E_c\|_{\mathrm{Lip}\to\mathrm{Lip}}
=1+\min\left\{r,\frac{2(k-1)r}{k+2r+kr^2}\right\}.}
\]
For \(k\ge3\), the transition is at \(r=(k-2)/k\). Below that threshold, the optimum exists only as all normalized conductance concentrates on the short arm; above it, a unique strictly positive conductance vector attains the optimum. At equality, both boundary and strictly positive optimal choices exist. For \(k=2\), a strictly positive minimizer exists for every \(r>0\). In the equilateral case the familiar sharp factor \(2-2/m\) is recovered. Every fixed star with at least three leaves has optimal norm strictly greater than one.

## Assumptions and scope
A compact metric star consists of the center \(o\) and \(m\) geometric edges identified with intervals \([0,\ell_i]\), joined at their zero endpoints. The metric is arclength shortest-path distance. The boundary data are real functions on the terminal vertices, with Lipschitz seminorm \(\max_{i\ne j}|f(v_i)-f(v_j)|/(\ell_i+\ell_j)\). The effective edge conductance \(c_i>0\) enters the Kirchhoff condition at the center as \(\sum_i c_i(f(v_i)-u(o))=0\). Thus \(w_i=c_i/\sum_jc_j\); this is an **effective conductance**, not an independent physical conductivity per unit arclength. The extension is constant-slope on each arm. Its norm uses all pairs of points of the full metric star. The formula optimizes the particular family of positive linear harmonic extensions, not arbitrary nonlinear extensions or arbitrary signed linear operators. Scaling all arm lengths equally has no effect on the stated norm.

## Proof
**1. Exact norm at fixed conductances.** A continuous function that is affine on each arm has Lipschitz seminorm equal to the largest absolute arm slope. Indeed every path is a concatenation of arm segments, giving the upper bound, and pairs of nearby points on a maximally sloped arm give equality. Consequently
\[
\|E_w f\|_{\mathrm{Lip}}=\max_i\frac{|f(v_i)-\sum_jw_jf(v_j)|}{\ell_i}.
\]
For a boundary datum of Lipschitz seminorm at most one, the \(i\)-th numerator is at most \(\sum_{j\ne i}w_j(\ell_i+\ell_j)\). This bound is sharp: set \(f(v_i)=\ell_i\) and \(f(v_j)=-\ell_j\) for all \(j\ne i\). These values are one-Lipschitz on the boundary because the difference of two negative values is bounded by the sum of the corresponding arm lengths. Taking the maximum gives the first formula without any unproved duality assumption.

**2. Finite-dimensional reparameterization.** Put \(L=\sum_i\ell_iw_i>0\). The exact norm becomes
\[
1+\max_i\frac{L-2\ell_iw_i}{\ell_i}.
\]
Define \(a_i=\ell_iw_i/L\). Then \(a_i>0\), \(\sum_i a_i=1\), \(L=1/\sum_i a_i/\ell_i\), and the excess above one is
\[
T(a)=\frac{\max_i(1-2a_i)/\ell_i}{\sum_i a_i/\ell_i}.
\]
Its numerator is positive for all \(m\ge3\), because \(\sum_i(1-2a_i)=m-2>0\). Allowing \(a_i\ge0\) takes the closure of all conductance choices, and continuity on the compact simplex (the denominator remains strictly positive) ensures a minimum there; strictly positive choices approximate every boundary point.

**3. Water-filling reduction.** For any nonnegative \(a\) summing to one, write \(z=\max_i(1-2a_i)/\ell_i\). The inequalities \(z\ge(1-2a_i)/\ell_i\) are equivalent to \(a_i\ge b_i(z)\). Feasibility requires and is equivalent to \(\sum_i b_i(z)\le1\), or \(z\ge z_*\). The function \(\sum_i(1-z\ell_i)_+\) decreases continuously from \(m>2\) to zero, and is strictly decreasing wherever positive, so its level two has exactly one positive root.

For each fixed feasible \(z\), the quantity \(\sum_i a_i/\ell_i\) is maximized by assigning all surplus mass \(e(z)\) to the shortest arm. Its maximum is \(D(z)\). Thus every \(a\) satisfies \(T(a)\ge z/D(z)\). Conversely, the explicit choice \(a_1=b_1+e\), \(a_i=b_i\) for \(i>1\) has denominator \(D(z)\) and maximum numerator at most \(z\), hence \(T(a)\le z/D(z)\). Taking infima in both directions proves
\[
\min_{a_i\ge0,\ \sum a_i=1}T(a)=\min_{z\ge z_*}\frac{z}{D(z)}.
\]
For \(z\ge1/\ell_1\), all lower bounds vanish, \(D(z)=1/\ell_1\), and the quotient increases strictly to infinity. On each interval of the remaining domain where the active set \(\{i:z<1/\ell_i\}\) is constant, \(D(z)\) is a positive affine function, so the derivative of \(z/D(z)\) has constant sign (or vanishes identically). Therefore its minimum occurs at \(z_*\) or a breakpoint \(1/\ell_i\). This proves the finite formula and constructs every asserted minimizing weight vector.

**4. One-short-arm phase transition.** Let \(\ell_1=r\le1\) and \(\ell_2=\cdots=\ell_{k+1}=1\). Directly solving the level-two equation gives \(z_*=(k-1)/(k+r)\). The only potentially optimal endpoints are \(z_*\) and \(1\): for \(z\ge1\) the surplus allocates entirely to the short arm, giving \(D(z)=1/r\), and the quotient is \(rz\), increasing. At \(z_*\) one obtains
\[
\frac{z_*}{D(z_*)}=\frac{2(k-1)r}{k+2r+kr^2},
\]
whereas at \(z=1\) it equals \(r\). Comparing these two expressions reduces to the sign of \(k(r-(k-2)/k)(r+1)\). For \(k\ge3\), the strict sign determines a unique endpoint; when \(r=(k-2)/k\), the quotient is constant on the entire interval between the endpoints. At \(z_*\), all \(b_i\) are positive, yielding a positive-conductance optimizer; at \(z=1\) all weight is on the short arm. Thus the attainability and equality statements follow. For \(k=2\), the positive branch is always strictly better at \(r>0\). For \(r=1\), the optimal weights are uniform and the norm is \(2-2/m\).

## Verification
The standalone `checker.py` uses only standard Python and exact rational arithmetic. Its independent formulation is the original linear program in variables \(w_1,\ldots,w_m\) and the norm bound, rather than the water-filling transformation. It enumerates all basic feasible vertices for representative stars with three to five arms, comparing optimal rational values and explicit construction; it checks the one-short-arm threshold and equal-arm law. On execution it reports 42 exact-rational minimax comparisons, eight equal-arm checks, and 35 phase-law checks. The finite computations stress-test the formulas but do not replace the all-parameter analytic proof.

## Relationship to prior work
Ambrosio and Puglisi [1] establish broad existence/correspondence theorems between linear Lipschitz extension operators and random projections, using Kantorovich–Rubinstein transport. Such general machinery motivates the class of positive barycentric extensions but does not yield the present exact optimal conductance formula or one-short-arm phase boundary. Sheffield and Smart [2] study nonlinear optimal extensions on finite graphs, a distinct minimization (over each particular datum) rather than a fixed positive linear extension operator; their norm-one scalar existence results therefore do not imply the positive linear optimum. Abrams and Kenyon [3] address harmonic functions and conductance constraints of a different kind. Basso [4] provides general one-point Lipschitz extension bounds, not the explicit metric-star unequal-arm conductance design established here.

Two published mathematical results on equal-arm stars [5,6] already determine the Banach-endpoint extension factor \(2-2/m\), which is **not claimed as novel here**. The novel scope is varying arm lengths, optimizing strictly positive harmonic conductances, the finite water-filling solution and the sharp degeneration-versus-attainment threshold. Another published result [7] concerns a *bounded*-Lipschitz dual norm on equal-arm stars rather than the unbounded Lipschitz-seminorm extension operator. These results provide no identified statement implying the full weighted-star phase diagram. The present exact formula is a special explicit solution of a finite linear-operator design problem; no novelty is attributed to the general existence of finite-dimensional linear programming.

## Limitations
The result concerns finite real scalar metric stars, strictly positive effective conductances and their linear harmonic extensions. The infimum may require a limit of vanishing conductances; it need not be attained within the positive class. No theorem is asserted for infinite stars, nonlinear infinity-harmonic extensions, fixed physical conductivity with nontrivial length normalization, or unrestricted signed extension operators. The equilateral formula is known; equivalence to an unindexed earlier unequal-arm calculation remains a bibliographic risk. Numerical enumeration is not a universal proof.

## References
[1] L. Ambrosio and D. Puglisi, *Linear extension operators between spaces of Lipschitz maps and optimal transport*, preprint deposited 2016-09-02, https://cvgmt.sns.it/paper/3155/ ; arXiv:1609.01450v1 (2016-09-06), https://arxiv.org/abs/1609.01450.

[2] S. Sheffield and C. K. Smart, *Vector-valued optimal Lipschitz extensions*, arXiv:1006.1741v1 (2010-06-09), https://arxiv.org/abs/1006.1741.

[3] A. Abrams and R. Kenyon, *Fixed-energy harmonic functions*, arXiv:1505.05785v1 (2015-05-21), https://arxiv.org/abs/1505.05785.

[4] G. Basso, *Lipschitz extensions to finitely many points*, arXiv:1707.06593v1 (2017-07-20), https://arxiv.org/abs/1707.06593.

[5] *Sharp leaf-count transitions in one-point \(p\)-Banach Lipschitz extensions*, published result (2026), https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-sharp-leaf-count-transitions-in-one-point-p-banach-lipschitz-ext--b03e5cc2b3f1.

[6] *Sharp three-leaf star extension constants for real \(p\)-Banach targets*, published result (2026), https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-sharp-three-leaf-star-extension-constants-for-real-p-banach-targ--e0e2d2aa7094.

[7] *Exact Dudley norms and mass-imbalance thresholds on equiradial stars*, published result (2026), https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-dudley-norms-and-mass-imbalance-thresholds-on-equiradial-s--ecc3b6450a54.
