# The unique side-uniform invariant law for randomized Kaczmarz on acute triangles

## Finding
Let \(V_1,V_2,V_3\) be the vertices of any nondegenerate acute Euclidean triangle. Denote by \(S_i\) its closed side opposite \(V_i\), by \(L_i\) the complete line containing that side, by \(\ell_i>0\) the side length, and by \(A_i\in(0,\pi/2)\) the angle at \(V_i\). Let \(U_i\) be normalized uniform arclength on \(S_i\), and let \(P_i\) denote orthogonal projection onto \(L_i\).

For each strictly positive probability vector \(p=(p_1,p_2,p_3)\), independent draws \(I_n\) with \(\Pr(I_n=i)=p_i\) define the ordinary, unrelaxed randomized Kaczmarz chain
\[
 X_{n+1}=P_{I_{n+1}}X_n.
\]
It possesses a **unique invariant probability law** \(\mu_p\) on \(\mathbb R^2\). The invariant law is conditionally uniform in arclength on each side if and only if the sampling probabilities equal the unique vector
\[
 p_i^*=\frac{\ell_i/\cos A_i}{\sum_{h=1}^3\ell_h/\cos A_h}
 =\frac{1/d_i}{\sum_{h=1}^3 1/d_h},
 \qquad d_i=(V_j-V_i)\cdot(V_k-V_i)>0,
\]
where \(\{i,j,k\}=\{1,2,3\}\). At that sampling law,
\[
 \boxed{\mu_{p^*}=\sum_{i=1}^3p_i^*U_i.}
\]
The unique invariant law is uniform on the entire triangle perimeter (with respect to total arclength) if and only if the triangle is equilateral; then \(p_i^*=1/3\). For an equilateral triangle of side length \(s\), the invariant mean is its centroid \(G\) and \(\mathbb E_{\mu_{p^*}}\|X-G\|^2=s^2/6\).

For every positive \(p\), convergence toward its unique invariant law is exponentially fast in quadratic Wasserstein distance. Define
\[
 q_2(p)=\sum_{i=1}^3p_i^2+\sum_{i\ne j}p_ip_j\cos^2(A_{k(i,j)})<1,
\]
where \(V_{k(i,j)}=L_i\cap L_j\). For every initial probability \(\nu\) with finite second moment, and every integer \(n\ge0\),
\[
 W_2^2(\nu P^n,\mu_p)\le q_2(p)^{\lfloor n/2\rfloor}
 W_2^2(\nu,\mu_p).
\]
Here \(P\) is the Markov kernel induced by the three projections; the displayed constant is an explicit sufficient contraction factor, not asserted to be optimal.

## Assumptions and scope
The three affine line equations are the side-supporting lines of a strictly acute, noncollinear triangle; they have no common solution. The projections are the full affine-line projections (not projection onto a segment), and indices are sampled independently with fixed strictly positive probabilities. No relaxation, acceleration, adaptive stepsizes, or row-dependent noise is present. A random initial point can be any law on \(\mathbb R^2\) with finite second moment for the quantitative bound. Statements of invariant uniqueness do not require any moment assumption on a competing invariant probability law.

## Proof
**1. Exact conditional balance.** Fix side \(S_c=[V_1,V_2]\) of length \(c=\ell_3\), opposite \(V_3\). The perpendicular foot \(F\) of \(V_3\) lies in the interior of \(S_c\) because the triangle is acute. Set \(a=\ell_1=|V_2V_3|\), \(b=\ell_2=|V_3V_1|\), and angles \(A=A_1,B=A_2\). The orthogonal projection of uniform arclength on \(S_b=[V_3,V_1]\) is uniform on \([V_1,F]\), an interval of length \(b\cos A\); that of \(S_a=[V_2,V_3]\) is uniform on \([F,V_2]\), length \(a\cos B\). These intervals are disjoint except at one endpoint and their lengths sum to \(c\).

Suppose an invariant law has sidewise uniform conditional measures. At stationarity the mass on line \(L_i\) equals \(p_i\): the latest projection selects that line, and the law under discussion has no atoms at intersections of different lines. Hence the law must be \(\sum_i p_iU_i\). On the two open portions of \(S_c\), the stationarity equation \(\mu|_{S_c}=p_c(P_c)_\#\mu\) reduces to
\[
 \frac{1-p_c}{c}=\frac{p_b}{b\cos A}=\frac{p_a}{a\cos B}.
\]
For all three target sides, equality of the two incoming densities is equivalent to \(p_i\cos A_i/\ell_i\) being independent of \(i\). Normalization gives precisely \(p=p^*\). Conversely, when \(p=p^*\), these densities agree on complementary subintervals on *every* side, and their integrated mass is \(1-p_i\). Thus the full measure (not merely its moments) satisfies the stationarity equation. The alternate dot-product expression follows from \(d_i=\ell_j\ell_k\cos A_i\), so \(\ell_i/\cos A_i=(\ell_1\ell_2\ell_3)/d_i\).

**2. Existence, uniqueness, and convergence.** For two synchronously coupled trajectories with the same random index sequence, their difference evolves by \(D_{n+1}=Q_{I_{n+1}}D_n\), where \(Q_i\) is the rank-one linear orthogonal projector onto the direction of \(S_i\). For two successive indices, \(\|Q_jQ_i\|^2\) is one when \(i=j\), and \(\cos^2 A_{k(i,j)}\) when \(i\ne j\). Conditioning on the past and averaging over two new independent indices gives
\[
 \mathbb E[\|D_{n+2}\|^2\mid D_n]\le q_2(p)\|D_n\|^2.
\]
The strict inequality \(q_2(p)<1\) follows from positive index probabilities and nonparallel distinct side directions. The Markov map on finite-second-moment probability laws contracts after two steps in \(W_2\), a complete metric. Banach's theorem supplies a unique invariant law for the two-step kernel. Its image under one step is another two-step invariant, hence the same law; it is therefore invariant for the one-step kernel. The contraction estimate follows by iterating the synchronous coupling and using the nonexpansiveness of any additional one-step projection.

For uniqueness among **all** invariant probability laws, couple a point distributed according to any other invariant law to a point from the finite-moment invariant law, independently of the indices. Every pair of differing successive indices yields a strict contraction by at most \(\max_{i\ne j}|\cos A_{k(i,j)}|<1\); such pairs occur infinitely often almost surely. Thus the paired distance tends to zero almost surely, even for initial laws lacking moments. Bounded-Lipschitz test functions and dominated convergence force the two invariant laws to coincide.

**3. Perimeter criterion and equilateral moment.** A perimeter-uniform law has side masses \(\ell_i/(\ell_1+\ell_2+\ell_3)\). Comparing this to the unique sidewise-uniform sampling weights forces the three values \(\cos A_i\) to agree, hence the triangle is equilateral. The reverse implication is immediate. On any equilateral side, tangential displacement from its midpoint has variance \(s^2/12\), and the squared distance of that midpoint to the centroid is \(s^2/12\); averaging the three sides gives \(s^2/6\).

## Verification
The standalone checker `verification/check_triangle_stationary.py` requires Python and SymPy. Running `python verification/check_triangle_stationary.py` tests the two acute triangles with vertices \((0,0),(4,0),(1,2)\) and \((0,0),(5,0),(2,3)\). Their exact sampling weights, ordered by the vertex opposite each side, are respectively \((3/16,1/16,3/4)\) and \((1/5,2/15,2/3)\). It checks the twelve incoming density conditions and 72 independent exact polynomial Markov identities up to total degree seven. These finite tests corroborate the construction; the analytic density argument proves invariance on every Borel set, and the contraction argument is dimension-independent within the stated planar family.

## Relationship to prior work
Zeng, Han, Su and Xie analyze adaptive-step randomized Kaczmarz for inconsistent linear systems (arXiv:2301.00176, posted 2022-12-31), obtaining convergence to least-squares solutions for their modified method, not the explicit invariant law of unrelaxed random projections onto three triangle lines. Hermer, Luke and Sturm study general nonexpansive random iterations and invariant measures, including inconsistent projections (arXiv:2205.15897, posted 2022-05-31). Their general existence/convergence theory does not itself specify a stationary density or a unique arclength-uniformizing index law for a given triangle. Li and Wu study semi-randomized **augmented** Kaczmarz for inconsistent systems (arXiv:2310.14175, posted 2023-10-22), a different transition. The present exact geometric balance classification and explicit sampling vector are the assessed additions; basic stochastic projection and contraction tools are established mathematics.

## Limitations
Only acute triangles, the three entire supporting lines, and fixed iid positive sampling probabilities are treated. For obtuse/right triangles, a perpendicular foot need not lie in the open opposite segment, invalidating the complementary-interval balance used here. The invariant law generally describes a stochastic error floor on an inconsistent problem, **not** convergence of individual iterates to a common solution or to the least-squares minimizer. The displayed two-step Wasserstein constant is guaranteed but not claimed sharp. A related older expected-projection literature, notably Butnariu's 1995 work identified through later references, was not materially inspected; priority against all specialized sources is therefore not independently certified.

## References
1. Yun Zeng, Deren Han, Yansheng Su, Jiaxin Xie, *Randomized Kaczmarz method with adaptive stepsizes for inconsistent linear systems*, arXiv:2301.00176 (first public 2022-12-31), https://arxiv.org/abs/2301.00176.
2. Neal Hermer, D. Russell Luke, Anja Sturm, *Nonexpansive Markov Operators and Random Function Iterations for Stochastic Fixed Point Problems*, arXiv:2205.15897 (first public 2022-05-31), https://arxiv.org/abs/2205.15897.
3. Shunchang Li, Gang Wu, *A semi-randomized and augmented Kaczmarz method with simple random sampling for large-scale inconsistent linear systems*, arXiv:2310.14175 (first public 2023-10-22), https://arxiv.org/abs/2310.14175.
