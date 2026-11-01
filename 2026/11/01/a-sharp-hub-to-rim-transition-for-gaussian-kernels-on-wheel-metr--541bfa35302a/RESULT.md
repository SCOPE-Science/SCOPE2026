# A sharp hub-to-rim transition for Gaussian kernels on wheel metrics

## Finding

Let \(W_n\) be the wheel graph formed by adjoining one hub to each vertex of a cycle \(C_n\), with \(n\ge4\) rim vertices. Write \(d\) for unweighted graph shortest-path distance on its \(n+1\) vertices and set
\[
K_n(t)_{uv}=\exp(-t\,d(u,v)^2),\qquad t>0.
\]
There is a single sharp bandwidth threshold \(\tau_n>0\): \(K_n(t)\) is positive semidefinite exactly when \(t\ge\tau_n\), and positive definite exactly when \(t>\tau_n\).

Put \(c_n=1\) for even \(n\) and \(c_n=\cos(\pi/n)\) for odd \(n\), and define
\[
f_n(x)=1-2c_n x+(2c_n-1)x^4,\qquad H_n(x)=1+3x-(n-3)x^2(1+x).
\]
Let \(a_n\) denote the unique zero of \(f_n\) in \((0,1)\). When \(n\ge6\), let \(b_n\) denote the unique zero of \(H_n\) in \((0,1)\). The exact threshold is
\[
\tau_n=-\log\xi_n,\qquad
\xi_n=\begin{cases}
a_n,&4\le n\le8,\\
b_n,&n\ge9.
\end{cases}
\]
In particular, all even orders \(n=4,6,8\) have the same value \(a_n=0.543689012692\ldots\), while \(a_5=0.721596398543\ldots\) and \(a_7=0.621251656594\ldots\). At the threshold, the nullity is \(2\) for \(n=5,7\), and \(1\) for every other \(n\ge4\).

The controlling eigenmode changes exactly at \(n=9\): a nonconstant Fourier mode on the rim controls \(4\le n\le8\), whereas a hub-versus-uniform-rim mode controls \(n\ge9\). In the latter regime,
\[
\xi_n=n^{-1/2}+n^{-1}+n^{-3/2}+O(n^{-2}),\qquad
\tau_n=\tfrac12\log n-n^{-1/2}-\tfrac12 n^{-1}+O(n^{-3/2}).
\]
For the degenerate wheel \(n=3\), the graph is \(K_4\), and its Gaussian matrix is positive definite for every \(t>0\).

## Assumptions and scope

The graph is finite, simple, and unweighted; its vertices are the hub and the \(n\) cyclic rim vertices. Distances are combinatorial shortest-path distances, **not** Euclidean chordal distances nor distances between continuous points along geometric edges. The parameter \(t\) is real and strictly positive. A positive definite matrix means strictly positive quadratic form on every nonzero real or complex vector, and positive semidefinite allows zero eigenvalues. At \(t=0\) the matrix is the all-ones matrix, positive semidefinite but not positive definite; the sharp classification stated above concerns \(t>0\).

## Proof

**Step 1 (complete spectral reduction).** Put \(x=e^{-t}\in(0,1)\), so the entry at graph distance \(1\) is \(x\) and the entry at distance \(2\) is \(x^4\). Every pair of distinct non-neighboring rim vertices is at distance \(2\) through the hub. With \(A\) the adjacency matrix of \(C_n\), \(J\) the all-ones \(n\times n\) matrix, and \(I\) the identity, the rim block is
\[
R=(1-x^4)I+(x-x^4)A+x^4J.
\]
The nonconstant cyclic Fourier characters \(r=1,\ldots,n-1\) are eigenvectors of \(R\) with eigenvalues
\[
\lambda_r(x)=1-x^4+2(x-x^4)\cos(2\pi r/n).
\]
Since \(x-x^4>0\), their smallest eigenvalue is exactly \(f_n(x)\), with multiplicity one when \(n\) is even and two when \(n\) is odd. The constant rim vector has eigenvalue \(L_n(x)=1+2x+(n-3)x^4\). With the unit hub vector and unit constant rim vector, the remaining invariant block is
\[
B_n(x)=\begin{pmatrix}1&\sqrt n\,x\\\sqrt n\,x&L_n(x)\end{pmatrix},
\qquad
\det B_n(x)=g_n(x)=1+2x+(n-3)x^4-nx^2.
\]
Because its top-left entry is \(1\), the block is positive semidefinite exactly when \(g_n(x)\ge0\), and is positive definite exactly when \(g_n(x)>0\). Thus the full matrix is positive semidefinite if and only if both \(f_n(x)\ge0\) and \(g_n(x)\ge0\).

**Step 2 (each obstruction has just one positive crossover).** On \((0,1)\), the value \(c_n\) lies above \(2/3\). Therefore \(f_n''(x)=12(2c_n-1)x^2>0\), \(f_n(0)=1\), \(f_n(1)=0\), \(f_n'(0)=-2c_n<0\), and \(f_n'(1)=6c_n-4>0\). Strict convexity shows that \(f_n\) has one interior zero \(a_n\), is positive on \((0,a_n)\), and negative on \((a_n,1)\).

The determinant factors as
\[
g_n(x)=(1-x)H_n(x),\qquad H_n(x)=1+3x-(n-3)x^2(1+x).
\]
At \(n=5\) one has \(g_5(x)=(1-x)^2(2x^2+4x+1)>0\). Moreover, \(g_n(x)=g_5(x)+(n-5)(x^4-x^2)\), so \(g_4(x)>g_5(x)>0\). For every \(n\ge6\), \(H_n(0)=1\), \(H_n(1)=10-2n<0\), and \(H_n''(x)=-2(n-3)(1+3x)<0\); its derivative decreases from \(3\). Hence \(H_n\) has precisely one interior zero \(b_n\), is positive below \(b_n\), and negative above \(b_n\).

**Step 3 (the exact order at which the controlling mode switches).** Let \(\alpha\) be the interior zero of \(1-2x+x^4\), so the preceding convexity argument gives \(27/50<\alpha<11/20\). For even \(n\), \(a_n=\alpha\). For odd \(n\),
\[
f_n(x)=(1-2x+x^4)+2(1-c_n)(x-x^4),
\]
so \(a_n\ge\alpha\).

Exact rational evaluations give \(g_8(11/20)>0\) and \(g_9(27/50)<0\). Because \(g_n(x)\) decreases strictly with \(n\) for fixed \(x\in(0,1)\), it follows that \(b_6,b_8>11/20>\alpha\), while for every \(n\ge9\), \(b_n<27/50<\alpha\le a_n\). It remains to compare the single odd case \(n=7\): one has \(g_7(63/100)>0\) and \(f_7(63/100)<0\), so \(a_7<63/100<b_7\). For a wholly exact verification of the latter sign, use \(\cos(\pi/7)>1-(22/49)^2/2\), from \(\pi<22/7\) and \(\cos u\ge1-u^2/2\), and substitute that rational lower bound into \(f_7(63/100)\). For \(n=4,5\), \(g_n\) has no interior zero. These observations prove the stated complete partition at \(n=9\).

**Step 4 (endpoint ranks).** At the controlling threshold the strict positivity of the other spectral block follows from the comparisons in Step 3. For \(n=5,7\), the minimum nonconstant rim eigenvalue occurs at the two distinct conjugate Fourier modes, giving nullity two. For even \(n=4,6,8\), it occurs at the sole antipodal Fourier mode, giving nullity one. For \(n\ge9\), only the \(2\times2\) hub–constant-rim block has determinant zero and its upper-left entry is one, so its nullity is exactly one. This also proves strict positive definiteness above the threshold and indefiniteness below it.

**Step 5 (asymptotic).** For \(n\ge9\), the root satisfies \(H_n(\xi_n)=0\). Write \(\epsilon=n^{-1/2}\), \(\xi_n=\epsilon z(\epsilon)\). The root equation becomes
\[
1+3\epsilon z-(1-3\epsilon^2)z^2(1+\epsilon z)=0.
\]
At \((\epsilon,z)=(0,1)\), the partial derivative with respect to \(z\) is \(-2\ne0\). The analytic implicit-function theorem gives \(z=1+\epsilon+\epsilon^2+O(\epsilon^3)\), by matching coefficients. Substituting into \(-\log(\epsilon z)\) gives both claimed asymptotic expansions.

## Verification

The accompanying `check.py` reconstructs all finite wheel Gaussian matrices independently of the spectral formula and checks their symmetric eigenvalues on both sides of the specified threshold, plus kernel nullities exactly at the critical parameter. It checks all orders \(4\le n\le120\) at three parameters each, with 351 actual matrix spectral comparisons, along with rational threshold-separation inequalities and three asymptotic checks. It requires Python, NumPy, and SciPy; run it as `python check.py`. The numerical root/eigenvalue checks are supporting evidence, not a proof for unbounded \(n\). The argument in the Proof section supplies the all-order proof.

## Relationship to prior work

Feragen, Lauze and Hauberg study geodesic exponential kernels and identify global obstacles to Gaussian positive definiteness in general geodesic spaces [1]; their main result assumes a continuous geodesic metric space and positivity for **every** bandwidth. The present finite vertex set is not itself a geodesic metric space, and the result determines a **single sharp admissible bandwidth ray** for its graph distance.

Obata calculates the quadratic embedding constant of wheel distance matrices [2], and Lou, Obata and Huang derive graph-join formulas including the wheel [3]. Those results concern conditional negative definiteness of the **unsquared** graph distance, equivalent to the behavior of \(\exp(-t\,d)\) for all \(t\), not the squared-distance Gaussian \(\exp(-t\,d^2)\). The circular Fourier decomposition in the present proof is elementary; the new assessed output is the uniform, exact all-order Gaussian bandwidth classification, the spectral-mode crossover at order nine, and its logarithmic large-wheel asymptotic.

## Limitations

This is a theorem about wheel **vertex** metrics, not about the corresponding one-dimensional metric graph including edge interiors, Euclidean embeddings, or general graph joins. It does not claim positivity below threshold or strict positivity at threshold. Related published work might imply an equivalent special-case formula through a more general matrix family; the literature comparison is bounded and independent review remains outstanding.

## References

[1] A. Feragen, F. Lauze, and S. Hauberg, *Geodesic Exponential Kernels: When Curvature and Linearity Conflict*, arXiv:1411.0296, first posted 2014-11-02.

[2] N. Obata, *Quadratic Embedding Constants of Wheel Graphs*, Interdisciplinary Information Sciences 23 (2017), 171–174, doi:10.4036/iis.2017.S.02.

[3] Z. Lou, N. Obata, and Q. Huang, *Quadratic Embedding Constants of Graph Joins*, arXiv:2001.06752.
