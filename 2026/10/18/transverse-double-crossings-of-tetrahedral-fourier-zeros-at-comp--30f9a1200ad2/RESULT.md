# Transverse double crossings of tetrahedral Fourier zeros at complete reciprocal nodes

## Finding

Let
\[
T=\{(x_1,x_2,x_3)\in\mathbb R^3:x_j\geq0,\ x_1+x_2+x_3\leq1\},\qquad
F(\xi)=\int_T e^{-i\xi\cdot x}\,dx.
\]
For any three integers \(m_1,m_2,m_3\) such that \(0,m_1,m_2,m_3\) are pairwise distinct, put \(a=2\pi(m_1,m_2,m_3)\). Then \(F(a)=0\), and the **entire real Fourier-zero set in a sufficiently small neighborhood of \(a\)** is the union of exactly two distinct embedded real-analytic curve germs crossing transversely at \(a\). Each punctured branch is a regular common zero of \(\operatorname{Re}F\) and \(\operatorname{Im}F\). In particular, the crossing is an ordinary double point, not a cusp, isolated zero, triple point, or single regular curve.

The two tangent lines are determined explicitly. Set \(a_0=0\), and for \(0\le j\le3\) define
\[
w_j=\prod_{\substack{0\le k\le3\\k\ne j}}(a_j-a_k)^{-1}.
\]
The tangent lines are precisely the two null lines of
\[
\sum_{j=1}^{3}w_j v_j=0,\qquad
\sum_{j=1}^{3}w_j v_j^2=0.
\]
These lines always exist and are distinct. For the node \(a=2\pi(1,2,3)\), they are spanned by \((1,1,0)\) and \((1,2,3)\).

The same statement holds for every nondegenerate real tetrahedron \(S=b+AT\), at \(A^{-\mathsf T}a\), with tangent lines transformed by \(A^{-\mathsf T}\). Here \(A\) is any invertible real \(3\times3\) matrix and \(b\) any translation.

## Assumptions and scope

The Fourier convention is \(\widehat{\mathbf1_T}(\xi)=\int_Te^{-i\xi\cdot x}\,dx\), with unnormalized Lebesgue measure. All frequencies and zeros considered in this theorem are **real**. The three integers are nonzero and pairwise distinct; the theorem makes no classification for reciprocal nodes with repeated phase coordinates and no claim about the global Fourier-zero set away from the stated lattice nodes. The neighborhood can depend on the chosen node.

## Proof

**1. Exact exponential-simplex integral.** Define \(s_0=0\), \(s_j=\xi_j\) for \(j=1,2,3\) and
\[
D_j(s)=\prod_{k\ne j}(s_j-s_k).
\]
On the open set where \(s_0,s_1,s_2,s_3\) are pairwise distinct, the classical exponential-simplex integration formula (Brion's short formula, in the form of [1, Corollary 12]) reads
\[
F(\xi)=(-i)^{-3}\sum_{j=0}^{3}\frac{e^{-is_j}}{D_j(s)}
=-i\sum_{j=0}^{3}\frac{e^{-is_j}}{D_j(s)}.
\]
Indeed the simplex has volume \(1/6\) and \(3!\operatorname{vol}(T)=1\); the linear form is \(x\mapsto-i\xi\cdot x\), so the three denominator factors each contribute \(-i\). The elementary Lagrange-interpolation identity for constants gives
\[
\sum_{j=0}^{3}D_j(s)^{-1}=0.
\]
Consequently, with \(a=2\pi(m_1,m_2,m_3)\) as stated, all four phases are one and \(F(a)=0\).

**2. The exact two-jet at a node.** Write \(\xi=a+\delta\) with \(\delta_0=0\). The denominator identity holds for every sufficiently small real \(\delta\); hence
\[
F(a+\delta)=-i\sum_{j=1}^{3}
\frac{e^{-i\delta_j}-1}{D_j(a+\delta)}.
\]
Since the denominators are real-analytic and real on real arguments, Taylor expansion yields
\[
\operatorname{Re}F(a+\delta)
=-\sum_{j=1}^{3}w_j\delta_j+O(|\delta|^2),
\]
\[
\operatorname{Im}F(a+\delta)
=\frac12\sum_{j=1}^{3}w_j\delta_j^2+O(|\delta|^3).
\]
Here the apparent first- and second-order terms coming from denominator variation in the imaginary expansion vanish because the linear exponential contribution is real after multiplication by \(-i\). The quadratic imaginary term is therefore precisely the displayed diagonal form. Every \(w_j\ne0\), so \(\operatorname{Re}F=0\) is a smooth real-analytic surface \(\Sigma\) through \(a\), with tangent plane
\[
\Pi=\{v\in\mathbb R^3:\sum_{j=1}^{3}w_jv_j=0\}.
\]
The restriction of \(\operatorname{Im}F\) to \(\Sigma\) has a critical point at \(a\) and quadratic term \(Q(v)=\frac12\sum_{j=1}^{3}w_jv_j^2\), restricted to \(\Pi\).

**3. Universal saddle signature.** The same interpolation identity gives \(w_0+w_1+w_2+w_3=0\). Eliminate \(v_3=-(w_1v_1+w_2v_2)/w_3\). The matrix of \(2Q|_\Pi\), in \((v_1,v_2)\), is
\[
M=\begin{pmatrix}
w_1+w_1^2/w_3&w_1w_2/w_3\\
w_1w_2/w_3&w_2+w_2^2/w_3
\end{pmatrix}
\]
with determinant
\[
\det M=-\frac{w_0w_1w_2}{w_3}
=-\frac{w_0w_1w_2w_3}{w_3^2}.
\]
There are six unordered pairs among the four distinct real numbers \(a_0,a_1,a_2,a_3\), so
\[
\prod_{j=0}^{3}D_j(a)
=(-1)^6\prod_{0\le j<k\le3}(a_j-a_k)^2>0.
\]
It follows that \(\prod_j w_j>0\), and hence \(\det M<0\). The restricted quadratic form is therefore a nondegenerate saddle, with two distinct real null lines.

**4. Local zero topology.** The real-analytic Morse lemma applied to \(\operatorname{Im}F|_\Sigma\) produces real-analytic local coordinates \((u,v)\) on \(\Sigma\), centered at \(a\), in which this function is a nonzero multiple of \(uv\). Thus the common real zeros of \(\operatorname{Re}F\) and \(\operatorname{Im}F\) near \(a\) are exactly the two coordinate-axis curves. The Morse coordinate map is a local diffeomorphism: the curves are embedded, distinct, and transverse, and their tangent lines are the null lines of \(Q|_\Pi\). Away from the crossing on these branches, the restriction has nonzero derivative normal to its zero curve within \(\Sigma\), so the pair of real equations has rank two.

**5. Worked node and affine invariance.** At \(a=2\pi(1,2,3)\), writing \(c=(2\pi)^{-3}\), the four weights are
\[
(w_0,w_1,w_2,w_3)=c(-1/6,1/2,-1/2,1/6).
\]
The tangent-plane equation reduces to \(v_3=-3v_1+3v_2\), while the saddle's null equation reduces to \(2v_1^2-3v_1v_2+v_2^2=0\). Its factorization gives the two stated directions. For \(S=b+AT\), a change of variables gives
\[
\widehat{\mathbf1_S}(\xi)
=|\det A|e^{-i\xi\cdot b}F(A^{\mathsf T}\xi).
\]
The prefactor never vanishes; the invertible linear frequency change preserves the real zero set's germ and transversality. This completes the proof.

## Verification

The standalone script `checks/check_tetra_crossings.py` verifies the Lagrange-weight identity and the negative restricted Hessian determinant exactly for 120 triples of distinct nonzero integers. It independently compares the divided-difference transform with its simplex-moment Taylor series (error below \(6\cdot10^{-52}\)), and computes four high-precision nearby zeros on the two analytic crossing branches at the node \(2\pi(1,2,3)\), with complex transform residuals below \(4\cdot10^{-53}\), and checks their predicted tangent slopes. The exact proof above establishes **all** claimed integer triples and tetrahedra; finite tests are diagnostics, not a substitute for the analytic argument. Reproduce with `python checks/check_tetra_crossings.py` using SymPy and mpmath.

## Relationship to prior work

The exponential-integral identity itself is prior work: [1, Corollary 12, Equation (10)] supplies the exact transform of a simplex at regular phase coordinates. In a separate polyhedral-transform treatment, [2, Sections 2 and 4] explains a general reduction from polyhedral volumes to their faces and edges. Neither inspected treatment identifies the reciprocal Fourier-zero nodes as ordinary transverse double points, gives their two tangent lines, or proves the universal negative restricted Hessian determinant. Those nodal statements are the present claim, not the pre-existing transform formula. In two dimensions, Fourier zeros of a triangle are isolated and can undergo parameter-dependent fold splitting; this does not imply the present unperturbed three-dimensional two-curve crossing.

## Limitations

The theorem treats neighborhoods of complete reciprocal nodes only. It does not count all zero-curve components, establish global connectivity, analyze repeated phase coordinates, or classify higher-dimensional simplices. The analytic proof is self-contained after the standard exponential-simplex integral and analytic Morse lemma. The source comparison is not a guarantee of publication priority; unindexed classical Fourier-optics studies could contain an equivalent local nodal statement.

## References

[1] V. Baldoni, N. Berline, J. A. De Loera, M. Köppe, and M. Vergne, *How to Integrate a Polynomial over a Simplex*, arXiv:0809.2083, first posted 11 September 2008, Section 3.2 and Corollary 12. https://arxiv.org/abs/0809.2083

[2] G. M. Gallatin, *Fourier, Gauss, Fraunhofer, Porod and the Shape from Moments Problem*, arXiv:1109.5262, first posted 24 September 2011, Sections 2 and 4; *Journal of Mathematical Physics* **53**, 013509 (2012). https://arxiv.org/abs/1109.5262
