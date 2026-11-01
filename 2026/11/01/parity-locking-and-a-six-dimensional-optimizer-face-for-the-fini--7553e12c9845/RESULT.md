# Parity locking and a six-dimensional optimizer face for the finite \(A_3\) Turán problem

## Finding
Let \(N\ge5\) be an integer and let \(G_N=\{v\in(\mathbb Z/N\mathbb Z)^4:\sum_{i=1}^4v_i=0\}\). With \(e_i\) the standard coordinate vectors, set \(\Omega_N=\{0\}\cup\{e_i-e_j:1\le i\ne j\le4\}\subset G_N\). For complex positive-definite functions \(f:G_N\to\mathbb C\) with \(f(0)=1\) and \(\operatorname{supp}f\subseteq\Omega_N\), define the counting-measure mass \(\mathcal T_N=\max_f\sum_{v\in G_N}f(v)\). Then
\[
\boxed{\mathcal T_N=\begin{cases}4,&N\text{ even},\\[3pt]1+\dfrac{3}{c_N(2-c_N)},&N\text{ odd},\end{cases}\qquad c_N=\cos(\pi/N).}
\]
Every odd-order problem has a **unique optimizer even when complex values are allowed**: \(f(e_i-e_j)=1/[4c_N(2-c_N)]\) for every ordered pair \(i\ne j\). Every even-order problem has a **six-real-dimensional optimizer face**. Precisely, writing \(x_{ij}=f(e_i-e_j)=a_{ij}+ib_{ij}\) for \(1\le i<j\le4\), the full set of even-order optimizers consists of the Fourier-positive functions satisfying
\[
\boxed{a_{12}+a_{34}=a_{13}+a_{24}=a_{14}+a_{23}=\tfrac12,
\qquad b_{ij}=u_i-u_j\quad(1\le i<j\le4)}
\]
for some real \(u_1,u_2,u_3,u_4\). Adding a common constant to the \(u_i\) changes nothing; the remaining Fourier inequalities cut out a compact convex set with nonempty relative interior in this six-dimensional affine space. In particular the even-order optimizer is not unique.

For odd \(N\to\infty\), the excess above the even-order value has a **quartic**, rather than quadratic, leading scale:
\[
\boxed{\mathcal T_N=4+\frac{3\pi^4}{4N^4}+O(N^{-6}).}
\]
The exact finite-order mass is already determined by a known four-root minimization mechanism; the additional contributions here are the complete complex optimizer-face classification, its parity transition, and the exact quartic Turán correction within this natural root-system family.

## Assumptions and scope
The support is the rank-three root neighborhood of type \(A_3\), reduced modulo \(N\); all twelve nonzero roots are distinct when \(N\ge5\). A function is positive definite if \(\sum_{g,h\in G_N}c_g\overline{c_h}f(g-h)\ge0\) for all complex vectors \((c_g)\). Thus \(f(-g)=\overline{f(g)}\), and its unnormalized finite Fourier transform is nonnegative at every character. The counting normalization is deliberate: the objective is a sum, not the uniform-probability mean.

The dual characters are represented by \((z_1,z_2,z_3,z_4)\) of \(N\)-th roots of unity, modulo simultaneous multiplication by a common \(N\)-th root. Write \(S=z_1+z_2+z_3+z_4\). For six coefficients \(x_{ij}\) define the real Fourier polynomial
\[
F_x(z)=1+2\operatorname{Re}\sum_{1\le i<j\le4}x_{ij}z_i\overline{z_j}.
\]
The feasible set is exactly \(F_x(z)\ge0\) for every such quadruple, and its mass is \(1+2\sum_{i<j}\operatorname{Re}x_{ij}\).

## Proof
**1. Root-sum identity and symmetrization.** Permuting the four coordinates acts transitively on the twelve nonzero roots. Averaging any feasible \(f\) over these permutations preserves positivity, the support, normalization and mass, and produces a real common coefficient \(t\) on every nonzero root. Its Fourier polynomial is
\[
F_t(z)=1+t\bigl(|S|^2-4\bigr),
\]
since \(\sum_{i\ne j}z_i\overline{z_j}=|S|^2-4\). Put \(r_N=\min_z|S|\). Since \(r_N<2\), positivity at the minimizing characters forces \(t\le1/(4-r_N^2)\). The positive value at equality is feasible at all characters, so
\[
\mathcal T_N=1+\frac{12}{4-r_N^2},\qquad t_N=\frac1{4-r_N^2}.
\]
This step optimizes over all complex functions because averaging cannot reduce the mass.

**2. Exact four-root minimum.** If \(N\) is even, two opposite pairs give \(S=0\), hence \(r_N=0\). Suppose \(N\) is odd. Four unit vectors have zero sum only when they consist of two antipodal pairs: indeed, if a pair has nonzero sum, the negative of its sum determines the unique opposite chord of the unit circle, while a zero-sum pair is already antipodal. No \(N\)-th root has an antipode at odd \(N\), so \(S\ne0\).

Among four roots, two have angular separation at most \(\pi/2\). Let their sum be \(A\), so \(|A|\ge\sqrt2\), and call the other pair sum \(B\). Any nonzero sum of two \(N\)-th roots points along a direction which is an integral multiple of \(\pi/N\). If \(A\) and \(-B\) are not collinear, their nonzero angular separation is at least \(\pi/N\), implying
\[
|A+B|\ge\sqrt2\sin(\pi/N)>2\bigl(1-\cos(\pi/N)\bigr)
\]
for \(N\ge5\). If they are collinear and opposite, the two pair lengths are \(2\cos(\pi a/N)\) and \(2\cos(\pi b/N)\) for distinct integers \(0\le a,b\le(N-1)/2\). The successive decreases of cosine on \([0,\pi/2]\) are increasing, so their difference is at least \(2[1-\cos(\pi/N)]\). Collinearity in the same direction cannot give a smaller nonzero sum. The bound is attained by the four roots \(1,1,-e^{i\pi/N},-e^{-i\pi/N}\), which are \(N\)-th roots because \(N\) is odd. Therefore
\[
r_N=2(1-c_N)\quad(N\text{ odd}),
\]
and the twelve coordinate permutations of this four-root multiset give twelve distinct minimizing dual characters. Inserting the minimum into step 1 gives the mass formulas. (The underlying small-root-sum formula was already known in the classical roots-of-unity literature.)

**3. Rigidity for odd \(N\).** Since \(F_{t_N}\) vanishes at each of the twelve minimizing characters, every feasible optimizer must vanish at all twelve as well: the permutation-average of its nonnegative Fourier values is \(F_{t_N}\), and every point in this orbit has nonnegative value. Set \(c=c_N\), \(s=\sin(\pi/N)>0\). Index the six positive roots, and hence the \(x_{ij}\), in the order \(12,13,14,23,24,34\). For each choice of a duplicated coordinate pair \(\{i,j\}\), let those two phases equal \(1\), and let the remaining phases, in increasing coordinate order, equal \(-c+is\) and \(-c-is\). Its complex-conjugate character is another contact. Adding and subtracting the two Fourier-zero equations splits the system into
\[
A(c)(a_{12},a_{13},a_{14},a_{23},a_{24},a_{34})^{\mathsf T}=-\tfrac12\mathbf1,
\quad sB(c)(b_{12},b_{13},b_{14},b_{23},b_{24},b_{34})^{\mathsf T}=0.
\]
Here \(A(c)=(1+c)I+(2c^2+c-1)P-cJ\), where \(P\) exchanges each edge with its disjoint complementary edge and \(J\) is the all-ones matrix. The imaginary matrix is
\[
B(c)=\begin{pmatrix}
0&1&-1&1&-1&2c\\
1&0&-1&-1&2c&-1\\
1&-1&0&2c&-1&1\\
-1&-1&2c&0&-1&-1\\
-1&2c&-1&-1&0&1\\
2c&-1&-1&1&1&0
\end{pmatrix}.
\]
The complement involution \(P\) has eigenspaces of respective dimensions one, two and three after separating the all-ones direction. Its three eigenvalues on these subspaces yield, and direct elimination for \(B\) confirms,
\[
\det A=-64c^3(c-2)(c-1)^3(c+1)^5,
\qquad\det B=-64(c-1)^3(c+1)^3.
\]
Both are nonzero for \(\cos(\pi/5)\le c<1\). Thus all imaginary coefficients vanish and the real coefficients are uniquely determined. The common coefficient \(t_N=1/[4c(2-c)]\) solves the system, proving uniqueness among **all complex** positive-definite functions.

**4. Complete even-order face.** The symmetrized optimizer now has coefficient \(1/4\) and Fourier polynomial \(F_{1/4}(z)=|S|^2/4\). Hence every optimizer has zero Fourier value at every zero-sum quadruple. As in step 2, the latter are exactly the two-antipodal-pair configurations. For a partition \(\{i,j\}\mid\{k,l\}\), choose phases \(z_i=1,z_j=-1,z_k=u,z_l=-u\), where \(u\) runs through all \(N\)-th roots. Fourier orthogonality in \(u\) forces
\[
a_{ij}+a_{kl}=\tfrac12
\]
and the vanishing of a certain complex cross-edge coefficient. Across the three partitions, the real cross-edge conditions follow from the displayed three real sums, while the three independent imaginary conditions are precisely the triangle-curl equations for \(b_{ij}\). They are equivalent to \(b_{ij}=u_i-u_j\) for real vertex potentials \(u_i\), unique modulo a common constant. Conversely these relations make every zero-sum Fourier value vanish (the imaginary contribution for gradient coefficients is \(\operatorname{Im}\sum_i u_i z_i\overline S=0\)), and their mass is \(1+2(3/2)=4\). Requiring positivity at all other characters therefore characterizes the **entire** optimizer set.

There are three independent real constraints on six real parts, leaving three degrees of freedom; the imaginary gradient space has dimension three. At the common coefficient \(1/4\), every noncontact Fourier value is strictly positive, because the finite character set has \(|S|^2>0\) outside the contact set. Small perturbations in any of the six allowed affine directions preserve those inequalities. Thus the relative affine dimension is exactly six, not just at most six.

**5. Asymptotics.** For odd \(N\), put \(\delta_N=1-\cos(\pi/N)=\pi^2/(2N^2)+O(N^{-4})\). Since \(c_N(2-c_N)=1-\delta_N^2\),
\[
\mathcal T_N=1+\frac3{1-\delta_N^2}=4+3\delta_N^2+O(\delta_N^4)
=4+\frac{3\pi^4}{4N^4}+O(N^{-6}).
\]

## Verification
The standalone `check_a3.py` derives the two exact contact determinants symbolically, checks that the even-order contact matrix has rank six over the algebraic field generated by sixth roots of unity, and directly evaluates all \(18{,}396\) character samples for \(5\le N\le16\). It reconstructs the invariant Fourier polynomial, checks nonnegativity and the minimum, and checks the exact contact count (twelve for odd \(N\), \(3(N-1)\) for even \(N\)). Its finite enumeration is a consistency check, not a proof for arbitrary \(N\); all infinite quantifiers are proved above. Run `python check_a3.py` with SymPy installed.

## Relationship to prior work
Kolountzakis and Révész introduced general Fourier/packing techniques for Turán extremal positive-definite functions on finite groups, including low-dimensional difference-set examples; those results supply context but not the present finite \(A_3\) complex equality class. The four-root minimum is a classical result discussed and reproved for sufficiently large orders by Barber, building on Myerson; no novelty is claimed for that root-of-unity minimum itself. Dutour Sikirić's treatment of the Fourier transform of an \(A_n\) root set gives the continuous root identity \(|\sum z_i|^2-(n+1)\), but does not give the finite odd-order gap or describe the entire complex optimizer face here. The new issue resolved is **equality rigidity on the finite quotient**, with a six-real-dimensional even-order face versus a unique odd-order optimizer and a quartic arithmetic defect.

## Limitations
The theorem concerns only the twelve-root neighborhood of \(A_3\) for \(N\ge5\), not higher-rank \(A_n\) supports or arbitrary coefficients outside this support. The even-order result describes the full feasible face by explicit affine equations together with the finite Fourier positivity constraints; it does not enumerate its extreme points. Independent mathematical validation has not been performed, and historical overlap with other descriptions of finite root-lattice Cayley graph theta bounds remains possible.

## References
- M. N. Kolountzakis and S. Gy. Révész, *Turán's extremal problem for positive definite functions on groups*, arXiv:math/0312218, first posted 2003-12-10, later *J. London Math. Soc.* 74 (2006), 475–496.
- G. Myerson, *How small can a sum of roots of unity be?*, *American Mathematical Monthly* 93 (1986), 457–459, DOI:10.1080/00029890.1986.11971853 (classical four-root minimum; exact first public day not established).
- B. Barber, *Small sums of five roots of unity*, arXiv:2104.15057, first posted 2021-04-30; see Proposition 3(c) and its proof for the four-root background.
- M. Dutour Sikirić, *Coloring the Voronoi tessellation of lattices*, *J. London Math. Soc.* 104 (2021), 1135–1171, DOI:10.1112/jlms.12456; see Section 5.2.1 for the \(A_n\) root-transform identity.
