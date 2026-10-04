# Exact Euclidean Banach--Mazur distance of the two-dimensional Cesàro space
## Finding
For the real two-dimensional Cesàro space \(\mathrm{ces}_2^{(2)}\), with \(\|(x,y)\|=\bigl(|x|^2+((|x|+|y|)/2)^2\bigr)^{1/2}\), the Banach--Mazur distance to the Euclidean plane is exactly \(d_{\mathrm{BM}}(\mathrm{ces}_2^{(2)},\ell_2^2)=\sqrt{1+1/\sqrt5}\).

## Assumptions and scope
All spaces and linear maps are real. For origin-symmetric unit balls \(K,L\subset\mathbb R^2\),
\[
d_{\mathrm{BM}}(K,L)=\inf\{\lambda\ge 1:\exists T\in GL(2),\ T(L)\subset K\subset \lambda T(L)\}.
\]
The two-dimensional Cesàro norm is the \(p=2\) specialization
\[
\|(x,y)\|=\left(|x|^2+\left(\frac{|x|+|y|}{2}\right)^2\right)^{1/2}.
\]

## Proof
A published normalization of this Cesàro plane uses the linear map
\[
T(u,v)=\left(\frac{2u}{\sqrt5},2v\right).
\]
Direct substitution gives
\[
\|T(u,v)\|^2
=u^2+v^2+\frac{2}{\sqrt5}|uv|.
\]
Thus it is enough to compute the Euclidean Banach--Mazur distance for the norm
\[
N_a(u,v)=\sqrt{u^2+v^2+2a|uv|}
\]
at \(a=1/\sqrt5\). We prove the more general identity
\[
d_{\mathrm{BM}}((\mathbb R^2,N_a),\ell_2^2)=\sqrt{1+a},
\qquad 0\le a\le1.
\]

Let \(K_a=\{z:N_a(z)\le1\}\). Since
\[
u^2+v^2\le N_a(u,v)^2\le(1+a)(u^2+v^2),
\]
we have
\[
\frac{1}{\sqrt{1+a}}B_2\subset K_a\subset B_2.
\]
Hence \(d_{\mathrm{BM}}(K_a,B_2)\le\sqrt{1+a}\).

For the reverse inequality, write
\[
Q_+=\begin{pmatrix}1&a\\a&1\end{pmatrix},
\qquad
Q_-=\begin{pmatrix}1&-a\\-a&1\end{pmatrix}.
\]
Because
\[
N_a(z)^2=\max\{z^TQ_+z,z^TQ_-z\},
\]
the unit ball is
\[
K_a=\{z:z^TQ_+z\le1\}\cap\{z:z^TQ_-z\le1\}.
\]

Take any origin-centered ellipse
\[
E_A=\{z:z^TAz\le1\},\qquad
A=\begin{pmatrix}p&r\\r&q\end{pmatrix}>0,
\]
with \(E_A\subset K_a\). Ellipsoid containment gives \(A-Q_+\succeq0\) and
\(A-Q_-\succeq0\). Therefore
\[
p\ge1,\qquad q\ge1,
\]
and the two determinant inequalities imply
\[
(p-1)(q-1)\ge(r-a)^2,\qquad
(p-1)(q-1)\ge(r+a)^2.
\]
Consequently
\[
(p-1)(q-1)\ge(|r|+a)^2\ge a^2,
\]
so
\[
\max\{p,q\}\ge1+a.
\]

If also \(K_a\subset\lambda E_A\), then the coordinate unit vectors belong to
\(K_a\), and hence
\[
p=e_1^TAe_1\le\lambda^2,\qquad
q=e_2^TAe_2\le\lambda^2.
\]
Thus
\[
\lambda^2\ge\max\{p,q\}\ge1+a.
\]
Every admissible ellipsoid pair therefore has ratio at least \(\sqrt{1+a}\).
Together with the Euclidean pair above,
\[
d_{\mathrm{BM}}((\mathbb R^2,N_a),\ell_2^2)=\sqrt{1+a}.
\]
Putting \(a=1/\sqrt5\) proves the stated Cesàro value.

## Verification
The normalization was expanded algebraically and independently checked on random real inputs. The lower bound uses only the equivalence
\[
E_A\subset\{z:z^TQz\le1\}\iff A-Q\succeq0
\]
for \(A>0\), followed by the exact \(2\times2\) positive-semidefinite determinant conditions. No finite search or numerical optimization is used to prove the infinite minimization over linear images.

## Relationship to prior work
Zuo (2012) explicitly defines the two-dimensional Cesàro space, gives the same linear normalization, and computes its Ptolemy constant. The article does not state a Banach--Mazur distance. Its displayed normalization is the literature bridge used here.

Targeted searches for the exact space name, the notation \(\mathrm{ces}_2^{(2)}\), the normalized quadratic form, and the candidate constant did not locate an exact Euclidean Banach--Mazur distance. Modern work on Banach--Mazur distance to the Euclidean ball emphasizes distance ellipsoids and exact planar extremal structure, but the inspected material does not state this Cesàro value.

## Limitations
The originality assessment is a bounded literature comparison rather than a proof that no equivalent formulation exists anywhere in the literature. The theorem proved here is only the Euclidean Banach--Mazur distance of the real two-dimensional \(p=2\) Cesàro section; it does not assert a formula for higher-dimensional or general-\(p\) Cesàro spaces.

## References
1. Z. Zuo, “The Ptolemy constant of absolute normalized norms on \(\mathbb R^2\),” Journal of Inequalities and Applications 2012, 107 (2012). DOI: 10.1186/1029-242X-2012-107.
2. J. S. Shue, “On the Cesàro sequence spaces,” Tamkang Journal of Mathematics 1 (1970), 143–150.
3. F. Grundbacher and T. Kobos, “On certain extremal Banach--Mazur distances and Ader's characterization of distance ellipsoids,” Mathematika (2026). DOI: 10.1112/mtk.70062.
