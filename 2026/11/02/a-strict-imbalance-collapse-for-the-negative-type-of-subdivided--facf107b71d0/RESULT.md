# A strict imbalance collapse for the negative type of subdivided bicliques

## Finding
Let \(2\le m<n\) be integers. Replace every edge of \(K_{m,n}\) by a path of two unit edges, and let \(d\) be the shortest-path distance on all \(N=mn+m+n\) vertices of the resulting graph \(S_{m,n}\). Define the conditional negative-type exponent
\[
\tau_{m,n}=\sup\{p\ge0:\sum_{u,v}c_uc_vd(u,v)^p\le0\text{ whenever }\sum_uc_u=0\}.
\]
For \(p=0\), the diagonal of the powered-distance matrix is zero and every off-diagonal entry is one. Put
\[
\beta_{m,n}=\log_2\!\left(\frac{2mn}{2mn-m-n}\right),\qquad
 a=2^p,\quad b=3^p,\quad c=4^p,
\]
and define the symmetric matrix
\[
Q_{m,n}(p)=
\begin{pmatrix}
 c(1-1/m)&a&(1+(m-1)b)/m\\
 a&c(1-1/n)&(1+(n-1)b)/n\\
 (1+(m-1)b)/m&(1+(n-1)b)/n&((m+n-2)a+(m-1)(n-1)c)/(mn)
\end{pmatrix},
\quad
 T=\begin{pmatrix}1&0\\0&1\\-1&-1\end{pmatrix},
\quad H_{m,n}(p)=T^{\mathsf T}Q_{m,n}(p)T.
\]
Then \(\det H_{m,n}(0)>0\), \(\det H_{m,n}(\beta_{m,n})<0\), and the *least* zero of this explicit determinant in \((0,\beta_{m,n})\) exists. It is exactly \(\tau_{m,n}\):
\[
\boxed{\ \tau_{m,n}=\min\{p\in(0,\beta_{m,n}):\det H_{m,n}(p)=0\}\ <\ \beta_{m,n}.\ }
\]
No uniqueness of other, later determinant zeros is asserted or required. In particular, for every \(t>0\), the Schoenberg kernel \(\exp(-t d(u,v)^p)\) is positive definite if \(0\le p\le\tau_{m,n}\); for every \(p>\tau_{m,n}\), it fails positive semidefiniteness for all sufficiently small \(t>0\). At the cutoff, the centered powered-distance form has exactly one zero direction; the minimum squared-Euclidean realization dimension is \(N-2\), versus \(N-1\) for \(p<\tau_{m,n}\).

For each *fixed* integer \(m\ge2\), as \(n\to\infty\),
\[
\boxed{\ \tau_{m,n}=\frac{m+1}{n\big((4m-1)\log2-2m\log3\big)}+O_m(n^{-2}).\ }
\]
By contrast, the unsubdivided complete-bipartite metric has cutoff \(\beta_{m,n}\to\log_2(2m/(2m-1))>0\). Thus *unequal* part sizes cause a strict new obstruction, and for fixed thin side the new cutoff collapses inversely with the long side. The equal-part subdivision has a different behavior and is outside the claim's domain.

## Assumptions and scope
The graph is simple and unweighted before subdivision, and every original edge is subdivided exactly once. All \(m\) original left vertices are collected in \(A\), the \(n\) original right vertices in \(B\), and the \(mn\) new midpoint vertices in \(E\). The original-vertex distances are four within either side and two across sides. An original vertex and a midpoint are at distance one when incident in the pre-subdivision graph and three otherwise. Two distinct midpoint vertices are at distance two when their edges share an endpoint and four otherwise. The theorem quantifies over all integers \(2\le m<n\), all real exponents \(p\ge0\), and all positive bandwidths \(t\). By interchanging parts it also applies to \(2\le n<m\). The positive definite assertion includes the boundary exponent even though the powered-distance form itself is not strictly negative definite there.

## Proof
**1. Orthogonal decomposition.** Write \(D_p=(d(u,v)^p)_{u,v}\), with diagonal zero at \(p=0\). The permutations of the left and right vertices act on \(A\oplus B\oplus E\). Decompose the edge-coordinate space into its constant component, left-row contrasts, right-column contrasts, and the subspace of matrices having all row and column sums zero. The last subspace has dimension \((m-1)(n-1)\) and the eigenvalue \(c-2a\) of \(D_p\). Each of the \(m-1\) left-contrast sectors has the symmetric matrix
\[
R_n(p)=\begin{pmatrix}-c&\sqrt n(1-b)\\\sqrt n(1-b)&(n-2)a-(n-1)c\end{pmatrix},
\]
and each of the \(n-1\) right-contrast sectors has the same matrix with \(m\) replacing \(n\). The remaining three dimensions are the group-constant sector. For a vector constant with total masses \(x,y,z\) on \(A,B,E\) respectively, its quadratic form equals \((x,y,z)Q_{m,n}(p)(x,y,z)^{\mathsf T}\). The zero-sum constraint is \(x+y+z=0\), and setting \(z=-x-y\) gives exactly \(H_{m,n}(p)\). These subspaces are mutually orthogonal in vertex coordinates (the mass parameterization on constants is only a change of basis). Their dimensions total \(N\). Consequently the negative-type inequality holds exactly when the edge-grid eigenvalue, both contrast matrices, and the two-dimensional mass form are all nonpositive.

**2. The nonconstant blocks remain strictly negative.** For \(0\le p\le1\), \(1\le a\le2\), \(c=a^2\), and concavity gives \(0\le b-1\le2(a-1)\). Setting \(h=a-1\in[0,1]\),
\[
\det R_k(p)=a^3(1+(k-1)h)-k(b-1)^2
\ge(1+h)^3(1+(k-1)h)-4kh^2
\ge(1-h)(1+(k+3)h)\ge0.
\]
This determinant is strictly positive: at \(h>0\), the inequality \((1+h)^3\ge1+3h\) used in the final bound is strict; at \(h=0\), the determinant is one. The top-left entry is \(-c<0\), so both \(R_k\) are strictly negative definite. Moreover \(c-2a=a(a-2)<0\) whenever \(p<1\). Since \(m\ne n\) with both at least two gives \(0<\beta_{m,n}<1\), all nonconstant blocks are strictly negative throughout \([0,\beta_{m,n}]\).

**3. A strict imbalance obstruction.** Let \(u=(1,-1,0)\) and \(v=(1,1,-2)\) denote group *mass* vectors. Direct substitution into the displayed matrix gives
\[
u^{\mathsf T}Q_{m,n}(p)u
=\left(2-\frac1m-\frac1n\right)c-2a.
\]
This vanishes at \(p=\beta_{m,n}\) by the definition of \(\beta_{m,n}\), and is strictly negative at smaller \(p\). The mixed form is
\[
u^{\mathsf T}Q_{m,n}(p)v
=\left(\frac1n-\frac1m\right)\bigl(c+2-2b\bigr).
\]
For \(0\le p<1\), \(c+2-2b>0\): its value decreases from one at \(p=0\) to zero at \(p=1\), because
\[
\frac{d}{dp}(4^p+2-2\cdot3^p)
=3^p\big((4/3)^p\log4-2\log3\big)<0.
\]
The derivative inequality follows from \((4/3)^p\le4/3\) and \(4\log4<6\log3\), equivalently \(256<729\). Thus at \(p=\beta_{m,n}<1\), the mass form has a zero diagonal quadratic value on \(u\) but a nonzero mixed value on \(u,v\). Its restriction to their span is indefinite and \(\det H_{m,n}(\beta_{m,n})<0\).

At \(p=0\), the entire \(D_0=J-I\) is strictly conditionally negative definite, so \(H_{m,n}(0)\) is strictly negative definite and has positive determinant. By continuity, the least positive root \(\tau\) of \(\det H\) occurs strictly before \(\beta_{m,n}\); before that root the mass form remains negative definite. At the root it is negative semidefinite. It cannot vanish identically because \(u^{\mathsf T}Qu<0\) there, hence has nullity exactly one. By step 2 the full centered form also has nullity exactly one. To prove sharpness for *all* larger exponents, suppose \(D_q\) were conditionally negative definite for some \(q>\tau\). The distinct points then admit a Euclidean realization of squared distances \(d^q\); strict positive definiteness of the Gaussian kernel on finitely many distinct Euclidean points, together with the standard integral representation of \(s^\theta\) for \(0<\theta<1\), would make \(D_{\tau}=(D_q)^{\tau/q}\) **strictly** conditionally negative definite, contradicting the null vector. Thus the entire allowed exponent set is precisely \([0,\tau]\). Schoenberg's theorem gives the equivalent universal-kernel statement. Strict positivity of each fixed-bandwidth Gaussian follows from the same finite distinct-point Euclidean embedding. The rank of the centered Gram matrix \(-JD_{\tau}J/2\), with \(J=I-\mathbf1\mathbf1^{\mathsf T}/N\), is \(N-2\), proving the endpoint dimension; below the cutoff it is \(N-1\).

**4. The asymmetric asymptotic.** Fix \(m\ge2\), send \(n\) to infinity, and write the entries of \(H=H_{m,n}(p)\) as \(H_{ij}\). At \(p=0\),
\[
H_{11}=-\frac{n+1}{mn},\qquad H_{12}=-\frac1{mn},\qquad H_{22}=-\frac{m+1}{mn}.
\]
For \(p=O_m(n^{-1})\), Taylor expansion of the explicit entries, uniformly for bounded \(np\), gives
\[
H_{11}=-1/m+O_m(n^{-1}),\quad H_{12}=O_m(n^{-1}),\quad
H_{22}=-\frac{m+1}{mn}+L_m p+O_m(n^{-2}),
\]
where
\[
L_m=\left(4-\frac1m\right)\log2-2\log3
=\frac{(4m-1)\log2-2m\log3}{m}>0.
\]
The last inequality follows from \(m\ge2\) and \(2\log(16/9)>\log2\). Set \(C_m=(m+1)/(mL_m)\). For every fixed sufficiently small \(\varepsilon>0\), the same uniform expansion makes \(H_{11}<0\), \(H_{22}<0\), and \(\det H>0\) **throughout** \(0\le p\le(C_m-\varepsilon)/n\) for all sufficiently large \(n\); at \(p=(C_m+\varepsilon)/n\), one has \(\det H<0\). Thus the *first* zero is \(C_m/n+o_m(n^{-1})\), with no possible earlier zero hidden in that shrinking interval. At the zero, \(H_{11}<0\) and \(H_{12}=O_m(n^{-1})\), hence \(H_{22}=H_{12}^2/H_{11}=O_m(n^{-2})\). Substituting into its uniform Taylor expansion improves the error to \(O_m(n^{-2})\). This yields the displayed formula. The positive limiting value of \(\beta_{m,n}\) follows immediately from its definition.

## Verification
The accompanying `check_unbalanced.py` reconstructs shortest-path distances by breadth-first search on the actual subdivided graph, independently forms the group-mass quadratic matrix, finds the least determinant zero numerically, and checks the centered full-matrix inertia on 25 unequal pairs with \(2\le m\le6\), \(m<n\le9\). It additionally probes the asymptotic constant at \(n=5000\) for four fixed thin sides, without constructing those large graphs. The checks run with Python, NumPy, and SciPy by invoking `python check_unbalanced.py` from the extracted package directory. These computations corroborate the analytic proof; no finite list proves the infinite-parameter assertion.

## Relationship to prior work
Sánchez (2011) gives the exact supremal negative-type exponent \(\beta_{m,n}\) for the **unsubdivided** complete-bipartite graph \(K_{m,n}\) and a general finite-metric matrix criterion. That result provides both a motivating comparison and the original-vertex obstruction, but does not determine the effect of adjoining all edge midpoints. The present calculation shows a strict loss in every *unequal* case, identifies its new two-dimensional mass-sector mechanism, and quantifies a collapse from a positive limiting cutoff to an inverse-size cutoff. Murugan (2011) treats vertex-transitive negative-type problems; the subdivided graph here has multiple vertex orbits and is not covered by those symmetry hypotheses. These works supply standard concepts and methods, not the stated asymmetric spectrum comparison or asymptotic.

## Limitations
The implicit determinant equation need not have a closed elementary solution; only its **least** zero before \(\beta_{m,n}\) is used. This theorem concerns one midpoint on every edge and two nontrivial *unequal* bipartition sizes; it does not classify arbitrary or weighted subdivisions, nor does it claim that a kernel is indefinite at every bandwidth above the exponent cutoff. Originality is assessed against the inspected materials and accessible indexed records, not established by an exhaustive search of all earlier literature. No independent mathematical validation has been performed.

## References
1. S. Sánchez, *On the supremal p-negative type of a finite metric space*, arXiv:1108.0451, first posted 2011-08-02, particularly §3 and Theorem 3.1; https://arxiv.org/abs/1108.0451.
2. M. K. Murugan, *Generalized roundness of vertex transitive graphs*, arXiv:1112.5657, first posted 2011-12-23, particularly Theorem 3.1; https://arxiv.org/abs/1112.5657.
3. I. J. Schoenberg, *Metric spaces and positive definite functions*, Transactions of the American Mathematical Society 44 (1938), 522–536, DOI 10.1090/S0002-9947-1938-1501980-0.
