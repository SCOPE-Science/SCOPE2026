# Exact positivity cone of distance-radial kernels on finite generalized quadrangles

## Finding

For any finite thick generalized quadrangle of order \((s,t)\), \(s,t\ge2\), let \(d\) be graph distance on its point–line incidence graph. For any five real numbers \(f_0,\ldots,f_4\), the kernel \(K_f(x,y)=f_{d(x,y)}\) is positive semidefinite **if and only if** two explicitly specified scalars and two specified real symmetric \(2\times2\) matrices are all positive semidefinite (the scalar inequalities are stated below). The cone, the entire eigenvalue multiset, and therefore the rank are independent of which generalized quadrangle realizes the parameters.

Writing
\[
\begin{aligned}
u&=f_0-(t+1)f_2+t f_4,\\
v&=f_0-(s+1)f_2+s f_4,\\
B_1&=\begin{pmatrix}f_0+(s-1)f_2-sf_4&\sqrt{s+t}(f_1-f_3)\\\sqrt{s+t}(f_1-f_3)&f_0+(t-1)f_2-tf_4\end{pmatrix},\\
B_0&=\begin{pmatrix}f_0+s(t+1)f_2+s^2tf_4&\sqrt{(s+1)(t+1)}(f_1+stf_3)\\\sqrt{(s+1)(t+1)}(f_1+stf_3)&f_0+t(s+1)f_2+st^2f_4\end{pmatrix},
\end{aligned}
\]
we have precisely
\[
K_f\succeq0\quad\Longleftrightarrow\quad u\ge0,\quad v\ge0,\quad B_1\succeq0,\quad B_0\succeq0.
\]
Each eigenvalue of \(B_0\) occurs once, each eigenvalue of \(B_1\) occurs with multiplicity \(h=st(s+1)(t+1)/(s+t)\), and \(u,v\) have multiplicities \(s^2(st+1)/(s+t)\) and \(t^2(st+1)/(s+t)\), respectively. Repeated numerical values have additive multiplicities.

In particular, for \(a\ge0\), the distance-exponential covariance \(K_a(x,y)=\exp(-a d(x,y))\) is positive semidefinite **exactly when**
\[
a=0\quad\text{or}\quad a\ge\tfrac12\log(st).
\]
It has rank one at \(a=0\), rank \((s+t+2)(st+1)-1\) at the positive threshold, and full rank \((s+t+2)(st+1)\) for larger \(a\). Thus graph distance is not conditionally negative semidefinite. All statements hold for non-Desarguesian and unequal-order quadrangles whenever they exist; no transitivity assumption is imposed.

## Assumptions and scope

A finite generalized quadrangle has a set \(P\) of points, a set \(L\) of lines, unique incidence between a point and a line when present, and the quadrangle axiom: given a nonincident point and line there is exactly one point on that line collinear with the original point. Every line has \(s+1\) points and every point has \(t+1\) lines, with integral \(s,t\ge2\). Its incidence graph has vertices \(P\sqcup L\), incident point–line edges, and shortest-path distance \(d\in\{0,1,2,3,4\}\). For a real symmetric matrix, positive semidefinite means \(z^{\mathsf T}Kz\ge0\) for every real vector \(z\). The five coordinates \(f_j\) are arbitrary real numbers, with no monotonicity or normalization conditions.

The point and line cardinalities are
\[|P|=(s+1)(st+1),\qquad |L|=(t+1)(st+1).\]
The multiplicity formulas refer to realized quadrangle parameters, hence yield nonnegative integers even when a displayed quotient is not visibly integral.

## Proof

Let \(M\) be the \(|P|\times|L|\) incidence matrix, and \(A_P,A_L\) be adjacency matrices for the point-collinearity and line-concurrency graphs. As distinct points have at most one common line and distinct lines have at most one common point,
\[MM^{\mathsf T}=(t+1)I+A_P,\qquad M^{\mathsf T}M=(s+1)I+A_L.\]
The point graph is strongly regular with parameters
\[v_P=(s+1)(st+1),\quad k_P=s(t+1),\quad\lambda=s-1,\quad\mu=t+1.\]
Indeed, the quadrangle axiom gives exactly \(t+1\) common neighbors of noncollinear points and \(s-1\) of distinct collinear points. On vectors perpendicular to constants, its strongly regular adjacency identity reduces to
\[A_P^2-(s-t-2)A_P-(s-1)(t+1)I=0,\]
whose two roots are \(s-1\) and \(-(t+1)\). [Equivalently, \(A_P^2=(k_P-\mu)I+(\lambda-\mu)A_P+\mu J\); the displayed polynomial follows on \(\mathbf1^\perp\).] Consequently, the singular values of \(M\) are \(\sqrt{(s+1)(t+1)}\) once and \(\sqrt{s+t}\) on the nonconstant coupled sector, with the remaining singular values zero. Trace and dimension yield multiplicities
\[
h=\frac{st(s+1)(t+1)}{s+t},\quad n_P=|P|-1-h=\frac{s^2(st+1)}{s+t},\quad n_L=|L|-1-h=\frac{t^2(st+1)}{s+t}.
\]
For clarity: the nontrivial point-adjacency root \(s-1\) has multiplicity \(h\) and root \(-(t+1)\) has multiplicity \(n_P\); the dual statement applies to lines. The multiplicities also follow by summing adjacency eigenvalues to zero and using \(|P|\), so no assumption on the rank of \(M\) is circular.

Two points are distance two exactly when collinear and otherwise distance four; likewise for two lines. A point and a line are at distance one exactly when incident, otherwise distance three. Therefore the distance-radial matrix in point/line block form is
\[
K_f=\begin{pmatrix}
(f_0-f_4)I+(f_2-f_4)A_P+f_4J_P&(f_1-f_3)M+f_3J_{P,L}\\
(f_1-f_3)M^{\mathsf T}+f_3J_{L,P}&(f_0-f_4)I+(f_2-f_4)A_L+f_4J_L
\end{pmatrix}.
\]
Use an orthonormal singular-vector decomposition of \(M\). The normalized constants on \(P\) and \(L\) span a two-dimensional invariant subspace because \(M\mathbf1_L=(t+1)\mathbf1_P\) and \(M^{\mathsf T}\mathbf1_P=(s+1)\mathbf1_L\); direct substitution yields \(B_0\). Each of the \(h\) nonconstant singular-vector pairs for \(\sqrt{s+t}\) spans a two-dimensional invariant subspace with restricted matrix \(B_1\). The left nullspace of \(M\), of dimension \(n_P\), has \(A_P\)-eigenvalue \(-(t+1)\), so the restriction there is the scalar \(u\); the right nullspace analog gives \(v\) with multiplicity \(n_L\). These spaces form an orthogonal decomposition of \(\mathbb R^{P\sqcup L}\), and all displayed dimensions add to \(|P|+|L|\). Positivity, eigenvalue multiplicities and rank follow immediately from this exact block diagonalization. In particular, checking a real symmetric \(2\times2\) block requires its two diagonal entries and determinant to be nonnegative.

For the exponential family let \(r=e^{-a}\in(0,1]\) and substitute \(f_j=r^j\). The scalar eigenvalues factor as
\[u=(1-r^2)(1-tr^2),\qquad v=(1-r^2)(1-sr^2).\]
For \(B_1\), its diagonal entries are \((1-r^2)(1+sr^2)\) and \((1-r^2)(1+tr^2)\), and
\[\det B_1=(1-r^2)^2(1+str^4)>0\qquad(0<r<1).\]
For \(B_0\), its diagonal entries are \((1+sr^2)(1+str^2)\) and \((1+tr^2)(1+str^2)\), and
\[\det B_0=(1+str^2)^2(1-r^2)(1-str^2).\]
Thus for \(0<r<1\), positivity forces and is forced by \(r^2\le1/(st)\). At equality \(\det B_0=0\) and \(\operatorname{tr}B_0>0\), while every other sector is strictly positive: since \(s,t\ge2\), \(r^2=1/(st)<1/s,1/t\). Thus the nullspace has dimension one. For smaller positive \(r\), all sectors are positive. At \(r=1\), \(K_f=J\) has rank one. These observations prove the threshold and ranks.

Finally, if the metric \(d\) were conditionally negative semidefinite, the elementary Schoenberg implication would make \(e^{-a d}\) positive semidefinite for every \(a>0\), contrary to the open interval \(0<a<\tfrac12\log(st)\). This proves the stated negative-type failure.

## Verification

The standalone file `checker.py` verifies the symbolic determinant identities using exact symbolic algebra and independently constructs the symplectic generalized quadrangle of order \((2,2)\) on 15 points and 15 lines. It computes all 30 graph-distance rows directly, checks the incidence singular spectrum and compares numerical eigenvalues of four radial profiles with the predicted block multiplicities, including the zero eigenvalue at the exponential threshold. Execute `python checker.py` in a Python environment with SymPy and NumPy installed. The finite example is a diagnostic only; the preceding spectral argument proves the claim for every finite thick generalized quadrangle.

## Relationship to prior work

The cited generalized-quadrangle references give the incidence geometry and strong-regularity data needed for the decomposition. Huang's treatment of bipartite diameter-four distance-regular graphs supplies related spectral background, but is not an arbitrary-radial positive-kernel classification on biregular incidence graphs. DeVille's generalized distance-spectrum theorem applies to **distance-regular graphs**; it therefore subsumes an algorithmic evaluation of kernels when \(s=t\), but does not apply directly to unequal-order generalized quadrangles, whose incidence graphs are biregular. The main assertion makes the full five-value PSD cone and multiplicities explicit uniformly for all realizations, in particular when \(s\ne t\). It should not be interpreted as claiming that SVD or strongly regular graph eigenvalues are themselves new.

## Limitations

Novelty is assessed relative to accessible mathematical sources and does not exclude an equivalent result buried in earlier literature on incidence coherent configurations or bipartite association schemes. The theorem is conditional on the existence of an order-\((s,t)\) generalized quadrangle; it does not assert existence for all integer pairs. It classifies **distance-radial** kernels, not all positive definite kernels or all covariance models. The executable tests do not independently prove the universal theorem. No independent mathematical audit has been performed.

## References

1. Junbo Huang, *Bipartite Distance-Regular Graphs of Diameter Four*, University of Waterloo thesis, repository item dated 2014-08-11. https://uwspace.uwaterloo.ca/items/62154fd0-f656-49d1-8fd2-158a90a730db
2. Lee DeVille, *The generalized distance spectrum of a graph and applications*, arXiv:1708.02294; particularly the distance-regular generalized-distance-matrix theorem and positive-semidefiniteness discussion. https://arxiv.org/html/1708.02294v2
3. E. R. van Dam, J. H. Koolen, H. Tanaka, *Distance-regular graphs*, survey; background on distance-regularity and geometries. https://www.combinatorics.org/ojs/index.php/eljc/article/download/DS22/pdf/
4. G. Aalipour et al., *On the distance spectra of graphs*, arXiv:1509.01196; background on distance spectral methods. https://arxiv.org/abs/1509.01196
