# Block-nuclear lower bounds and exact low-rank regularizers for quadratic neural networks

## Result

Consider a one-output degree-two polynomial-activation network
\[
f(x)=\sum_{j=1}^m \alpha_j\bigl(a(w_j^\top x)^2+b\,w_j^\top x+c\bigr),
\qquad \|w_j\|_2=1,
\]
with the usual output-layer penalty \(\sum_j|\alpha_j|\). Introduce the aggregate quadratic and linear coefficients
\[
Z=\sum_j\alpha_j w_jw_j^\top,\qquad
z=\sum_j\alpha_j w_j.
\]
Because \(\|w_j\|_2=1\),
\[
\sum_j\alpha_j=\operatorname{tr}Z,
\]
so the predictor is
\[
f(x)=a\,x^\top Zx+b\,z^\top x+c\,\operatorname{tr}Z.
\]

Define the induced atomic regularizer
\[
\mathcal R(Z,z):=
\inf\left\{
\sum_j|\alpha_j|:
Z=\sum_j\alpha_j w_jw_j^\top,\ 
z=\sum_j\alpha_j w_j,\ 
\|w_j\|_2=1
\right\}.
\]
This is the gauge represented by the exact neural-spectrahedron formulation when the width is sufficient to realize the decomposition.

Let
\[
M(Z,z):=
\begin{bmatrix}
Z&z\\
z^\top&\operatorname{tr}Z
\end{bmatrix}
\]
and define
\[
\Omega(Z,z):=
\max\left\{
\|Z\|_*,
\frac12\|M(Z,z)\|_*
\right\}.
\]

Then, for every symmetric \(Z\) and vector \(z\),
\[
\boxed{\mathcal R(Z,z)\ge \Omega(Z,z).}
\]
Moreover,
\[
\boxed{
\Omega(Z,z)\ge
\max\{\|Z\|_*,\|z\|_2\}
\ge
\frac12(\|Z\|_*+\|z\|_2).
}
\]

Consequently, replacing the exact output-weight regularizer by
\[
\beta\,\Omega(Z,z)
\]
produces a convex lower-bound problem that is pointwise no weaker than both regularizers used in the lower bounds of Theorems 3.3 and 3.4 of Rodrigues--Van Egmond--Fard (2026): respectively
\[
\frac{\beta}{2}\bigl(\|Z\|_*+\|z\|_2\bigr)
\quad\text{and}\quad
\beta\|Z\|_*.
\]
The second of those source relaxations leaves the aggregate linear coefficient unpenalized; this is also noted in the source paper's Remark 3.5.

The block-nuclear certificate is exact on several nontrivial families, and the exact atomic regularizer itself admits simple closed forms.

### Exact axes

For every symmetric \(Z\) and every \(z\),
\[
\boxed{\mathcal R(Z,0)=\|Z\|_*},
\qquad
\boxed{\mathcal R(0,z)=\|z\|_2}.
\]
Thus the nuclear-only lower bound is exact on the pure-quadratic axis but can assign zero penalty to a pure-linear aggregate whose true regularization is \(\|z\|_2\).

### Exact aligned rank-one family

For any unit vector \(v\) and scalars \(s,t\),
\[
\boxed{
\mathcal R(svv^\top,tv)=\max\{|s|,|t|\}.
}
\]
On this family,
\[
\Omega(svv^\top,tv)=\mathcal R(svv^\top,tv).
\]

In particular, when the input dimension is one, every aggregate pair is of this form. Hence a scalar-input quadratic network with width at least two has the exact convex training formulation
\[
\boxed{
\min_{s,t\in\mathbb R}
\ell\!\left(
a s\,x^{\odot2}+b t\,x+c s\,\mathbf 1,\ y
\right)
+\beta\max\{|s|,|t|\}.
}
\]
No semidefinite variables are required.

### Exact orthogonal rank-one family

Let \(u,v\) be orthonormal, and let \(S=|s|\), \(T=|t|\). Then
\[
\boxed{
\mathcal R(svv^\top,tu)
=
\frac{S^2+2ST+2T^2}{S+2T}
}
\]
when \(S+T>0\), with value \(0\) at \(S=T=0\).

This family shows both that the source lower bounds can be substantially loose and that the block-nuclear certificate, while strictly stronger, is not generally exact. For example,
\[
Z=\begin{bmatrix}1&0\\0&0\end{bmatrix},
\qquad
z=\begin{bmatrix}0\\1\end{bmatrix}
\]
gives
\[
\|Z\|_*=1,\qquad
\frac12(\|Z\|_*+\|z\|_2)=1,
\]
whereas
\[
\boxed{
\Omega(Z,z)=\frac{1+\sqrt5}{2}=1.6180339887\ldots
}
\]
and
\[
\boxed{
\mathcal R(Z,z)=\frac53=1.6666666667\ldots.
}
\]

## Proofs

### Universal block-nuclear lower bound

For any atomic representation,
\[
M(Z,z)
=
\sum_j
\alpha_j
\begin{bmatrix}w_j\\1\end{bmatrix}
\begin{bmatrix}w_j\\1\end{bmatrix}^{\!\top}.
\]
Since \(\|w_j\|_2=1\), each rank-one matrix in the sum has nuclear norm \(2\). Therefore
\[
\|M(Z,z)\|_*
\le
2\sum_j|\alpha_j|.
\]
Likewise
\[
\|Z\|_*
\le
\sum_j|\alpha_j|\,\|w_jw_j^\top\|_*
=
\sum_j|\alpha_j|.
\]
Taking the infimum over representations proves
\[
\mathcal R(Z,z)\ge\Omega(Z,z).
\]

To see that the block term controls the linear coefficient, if \(z\ne0\) set \(q=z/\|z\|_2\) and
\[
H=
\begin{bmatrix}
0&q\\
q^\top&0
\end{bmatrix}.
\]
Then \(\|H\|_{\mathrm{op}}=1\), so nuclear/operator duality gives
\[
\|M(Z,z)\|_*
\ge
\langle H,M(Z,z)\rangle
=
2\|z\|_2.
\]
Hence \(\Omega\ge\max\{\|Z\|_*,\|z\|_2\}\), and the arithmetic-mean bound follows.

### Exact axes

For \(z=0\), the universal nuclear lower bound gives
\(\mathcal R(Z,0)\ge\|Z\|_*\).
Write a spectral decomposition
\[
Z=\sum_i\lambda_i v_iv_i^\top.
\]
For each \(i\), use the two atoms \(v_i,-v_i\), both with coefficient
\(\lambda_i/2\). Their linear contributions cancel, their quadratic contributions sum to \(\lambda_i v_iv_i^\top\), and their total absolute coefficient is \(|\lambda_i|\). Summing over \(i\) proves
\(\mathcal R(Z,0)\le\sum_i|\lambda_i|=\|Z\|_*\).

For \(Z=0\), write \(z=T v\) with \(T=\|z\|_2\). The two atoms
\[
(\alpha_1,w_1)=(T/2,v),\qquad
(\alpha_2,w_2)=(-T/2,-v)
\]
have zero aggregate quadratic term, aggregate linear term \(Tv=z\), and total cost \(T\). The Euclidean lower bound proves equality.

### Exact aligned rank-one family

Take
\[
\alpha_1=\frac{s+t}{2},\quad w_1=v,
\qquad
\alpha_2=\frac{s-t}{2},\quad w_2=-v.
\]
Then the aggregates are \(svv^\top\) and \(tv\), while
\[
|\alpha_1|+|\alpha_2|
=
\frac{|s+t|+|s-t|}{2}
=
\max\{|s|,|t|\}.
\]
The reverse inequality follows from
\(\mathcal R\ge\max\{\|Z\|_*,\|z\|_2\}\).
For the same pair, the nonzero part of \(M\) is
\[
\begin{bmatrix}s&t\\t&s\end{bmatrix},
\]
whose half nuclear norm is also
\((|s+t|+|s-t|)/2\). Thus \(\Omega=\mathcal R\).

### Exact orthogonal rank-one family

The regularizer is unchanged by independently flipping the signs of \(Z\) and \(z\), so assume \(s=S\ge0\), \(t=T\ge0\). The axis cases are already proved. For \(S,T>0\), put
\[
r=\frac{T}{S+T},\qquad
A=\frac{(S+T)^2}{S+2T},\qquad
B=\frac{T^2}{S+2T}.
\]
Use
\[
w_\pm=\pm\sqrt{1-r^2}\,v+r u,\qquad
w_0=-u
\]
with coefficients \(A/2,A/2,-B\). Direct substitution gives
\[
\sum\alpha_j w_jw_j^\top=Svv^\top,\qquad
\sum\alpha_j w_j=Tu,
\]
and total absolute coefficient
\[
A+B
=
\frac{S^2+2ST+2T^2}{S+2T}.
\]

For the matching lower certificate, define on \([-1,1]\)
\[
p(y)=1-2\left(\frac{y-r}{1+r}\right)^2.
\]
Because \(0<r<1\), \(p(r)=1\), \(p(-1)=-1\), and
\[
|p(y)|\le1\qquad(-1\le y\le1).
\]
Write
\[
p(y)=A_0+C_0y^2+q_0y,
\]
where
\[
A_0=1-\frac{2r^2}{(1+r)^2},
\qquad
C_0=-\frac{2}{(1+r)^2},
\qquad
q_0=\frac{4r}{(1+r)^2}.
\]
Set
\[
Q=A_0I+C_0uu^\top,\qquad q=q_0u.
\]
For every unit \(w\),
\[
|w^\top Qw+q^\top w|
=
|p(u^\top w)|
\le1.
\]
Therefore every atomic representation obeys
\[
\sum_j|\alpha_j|
\ge
\langle Q,Svv^\top\rangle+q^\top(Tu)
=
SA_0+Tq_0.
\]
Substituting \(r=T/(S+T)\) simplifies the right-hand side to
\[
\frac{S^2+2ST+2T^2}{S+2T},
\]
which matches the construction.

## Relation to recent literature

Rodrigues, Van Egmond and Amiri Fard (2026) derive regularized least-squares lower bounds for quadratic neural-network training and connect one of them to nuclear-norm minimization. In their exact lifted variables, their Theorem 3.3 lower bound uses the arithmetic mean of separate nuclear- and Euclidean-norm bounds, while Theorem 3.4 retains only the nuclear norm of the quadratic aggregate. Their Remark 3.5 explicitly notes that the linear aggregate is then unpenalized.

Bartan and Pilanci's neural-spectrahedron formulation gives an exact semidefinite lift of degree-two polynomial-activation networks with \(\ell_1\) output-weight regularization. The present result starts from the same aggregate geometry but keeps the full signed lifted block before taking a nuclear norm. The scalar-input \(\ell_\infty\) regularizer and the orthogonal rank-one closed form are induced-gauge calculations, not claims that nuclear-norm regularization itself is new.

## Originality boundary

To the best of our knowledge, the checked literature does not state the combined result above: the full-block nuclear certificate that pointwise dominates both 2026 lower-bound penalties, its exactness on the aligned family and both coordinate axes, the scalar-input \(\ell_\infty\) reduction, and the orthogonal rank-one formula.

The exact neural-spectrahedron SDP, the lifted variables, nuclear-norm inequalities, atomic/gauge duality, and convex training of degree-two polynomial networks are prior art and are not claimed as new. The 2026 source itself already observes the unpenalized-linear behavior of its nuclear-only relaxation.

The main residual originality risk is that the induced gauge of the neural spectrahedron may have been analyzed under different convex-geometric or moment-problem terminology. The Bartan--Pilanci paper was inspected at its neural-cone/spectrahedron definitions and its one-dimensional illustration; no closed form matching the scalar \(\ell_\infty\) or orthogonal rank-one formulas was found there. No high-risk inaccessible source was identified.

## Limitations

The result concerns the one-output, unit-hidden-weight, \(\ell_1\)-output-regularized degree-two network underlying the cited exact convexification. The lower bound \(\Omega\) is convex but is not exact in general dimension, as the displayed \(5/3\) example itself shows. The scalar exact reduction requires enough width to realize the two-atom representation; the orthogonal rank-one construction uses three atoms. No claim is made about generalization error, statistical optimality, floating-point conditioning, or computational superiority over the exact SDP. The result strengthens a lower-bound surrogate; it does not replace the exact neural-spectrahedron program when an exact global optimum is required.

## Reproducibility

`artifacts/verify_block_nuclear.py` checks the universal inequalities on deterministic pseudorandom atomic decompositions, verifies the aligned and orthogonal closed forms, and evaluates the strict two-dimensional example. `artifacts/verification_output.txt` records the resulting numerical residuals. These checks support the algebraic derivations but do not replace them.

## References

1. L. Rodrigues, Z. Yetman Van Egmond, M. R. Amiri Fard, *Regularized Least Squares Training of Quadratic Neural Networks with Applications to System Identification*, arXiv:2609.17654, 2026. https://arxiv.org/abs/2609.17654
2. B. Bartan, M. Pilanci, *Neural spectrahedra and semidefinite lifts: global convex optimization of degree-two polynomial activation neural networks in polynomial-time*, Mathematical Programming 213 (2025), 737--769. https://doi.org/10.1007/s10107-024-02153-5
