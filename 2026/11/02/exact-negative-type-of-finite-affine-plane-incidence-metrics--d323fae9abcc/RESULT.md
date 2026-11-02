# Exact negative type of finite affine-plane incidence metrics

## Finding

Let \(\Pi\) be any finite affine plane of integer order \(q\ge2\) (with no coordinate or transitivity hypothesis), and let \(G_\Pi\) be the bipartite incidence graph on all its points and lines. Equip its vertices \(X\) with the unit-edge shortest-path metric \(d\). For every \(p\ge0\), say \(X\) has \(p\)-negative type if
\[\sum_{x,y\in X}c_xc_y d(x,y)^p\le0\quad\text{whenever }\sum_{x\in X}c_x=0,\]
with \(d(x,x)^0=0\). The supremum of such exponents equals
\[\boxed{\wp(X)=\log_2\!\left(\frac{q}{q-1}\right).}\]
The condition is strict on nonzero zero-sum coefficient vectors for \(0\le p<\wp(X)\), but not strict at equality. The zero-sum nullspace at equality has dimension \(q\) if \(q\ge3\), and dimension \(5\) for \(q=2\). Equivalently, the largest snowflake exponent for an isometric real Hilbert embedding of \((X,d^\alpha)\) is \(\alpha=\wp(X)/2\). At this endpoint the least affine embedding dimension is \(2q^2-1\) for \(q\ge3\) and \(4\) for \(q=2\). At any \(0<p<\wp(X)\) it is \(2q^2+q-1\). Along existing orders, \(\wp(X)=1/(q\log2)+O(q^{-2})\).

## Assumptions and scope

A finite affine plane of order \(q\) contains \(q^2\) points, \(q(q+1)\) lines in \(q+1\) parallel classes of \(q\) lines each, \(q+1\) lines through each point, and \(q\) points on each line. Distinct points lie on a unique line, and lines in different parallel classes meet at a unique point. No existence is assumed at any particular order; statements are conditional on a plane existing. The graph distances are \(2\) for distinct point pairs, \(1\) or \(3\) for incident or nonincident point--line pairs, and \(2\) or \(4\) for lines in different or equal parallel classes, respectively.

## Proof

**1. The exact powered distance matrix.** Index points first, then lines. Let \(N\) be the point--line incidence matrix, \(C\) the block-diagonal line matrix with a \(q\)-by-\(q\) all-ones block for each parallel class, and \(J\) all-ones matrices of the appropriate dimensions. For \(p>0\), set \(a=2^p\), \(b=3^p\). The powered distance matrix is
\[D_p=\begin{pmatrix}a(J-I)&bJ+(1-b)N\\bJ+(1-b)N^{\mathsf T}&aJ+(a^2-a)C-a^2I\end{pmatrix}.\]
The incidence axioms give, exactly,
\[NN^{\mathsf T}=qI+J,\qquad N^{\mathsf T}N=qI+J-C.\]
These identities are sufficient; no automorphism averaging is used.

**2. Invariant zero-sum blocks.** Decompose the real line-coordinate space into constants, the \(q\)-dimensional space \(U\) of vectors constant within each parallel class and summing to zero across classes, and \(W=\ker C\), whose dimension is \(q^2-1\). The point-coordinate zero-sum subspace \(P_0\) also has dimension \(q^2-1\). The map \(N:W\to P_0\) is an isomorphism with all singular values \(\sqrt q\). Therefore the restriction of \(D_p\) to the corresponding paired zero-sum spaces is a direct sum of \(q^2-1\) copies of
\[B_p=\begin{pmatrix}-a&(1-b)\sqrt q\\(1-b)\sqrt q&-a^2\end{pmatrix}.\]
It is negative semidefinite precisely when
\[a^3\ge q(b-1)^2.\]
On \(U\), the distance matrix is the scalar
\[\lambda_U=(q-1)a^2-qa.\]
The remaining one-dimensional zero-sum direction consists of a common point coefficient \(c\) and a common line coefficient \(-qc/(q+1)\). Its quadratic form, divided by \(q^2c^2\), is
\[R_q(a,b)=a(q^2-1)-2q-2qb(q-1)+\frac{q}{q+1}\bigl(aq^2+a^2(q-1)\bigr).\]
Orthogonality and the incidence identities show these blocks exhaust the entire hyperplane of coefficients summing to zero.

**3. The endpoint is negative type.** Put \(p_*=\log_2(q/(q-1))\) and \(a=q/(q-1)\). Then \(\lambda_U=0\). Since \(b=a^\gamma\) with \(\gamma=\log_2 3\), convexity on \(1\le a\le2\) yields
\[1+\tfrac32(a-1)\le b\le2a-1.\]
(The left inequality follows from the tangent at \(1\), since \(\gamma>3/2\); the right one is the chord between \((1,1)\) and \((2,3)\).) Consequently
\[a^3-q(b-1)^2\ge\frac{q(q-2)^2}{(q-1)^3}\ge0.\]
For \(q\ge3\), the lower inequality for \(b\), together with the displayed formula for \(R_q\), gives
\[R_q(a,b)\le-\frac{q(q-2)}{q-1}<0.\]
For \(q=2\), the endpoint has \(a=2,b=3\), the block determinant is zero, and \(R_2(2,3)=-2\). Therefore every zero-sum block is nonpositive at \(p_*\), with precisely the stated nullspace dimensions. The ambient vertex count is \(2q^2+q\); the Hilbert Gram-matrix rank after centering is the dimension of the zero-sum space minus its nullity, proving the asserted endpoint affine dimensions.

**4. Sharpness, strictness, and Hilbert interpretation.** For \(p>p_*\), one has \(a>q/(q-1)\) and hence \(\lambda_U>0\). A nonzero vector taking a constant positive value on one parallel line class, its negative on another, and zero elsewhere is a zero-sum witness that \(p\)-negative type fails. For \(0<p<p_*\), let \(\theta=p/p_*\). Schoenberg's embedding theorem represents the endpoint kernel \(d^{p_*}\) as squared Euclidean distances between distinct points. The Gaussian matrices \(\bigl(e^{-t d(x,y)^{p_*}}\bigr)_{x,y}\) are strictly positive definite for all \(t>0\). Using the standard integral representation of \(s^\theta\) for \(0<\theta<1\) proves strict \(p\)-negative type. At \(p=0\), the zero-diagonal, unit-off-diagonal matrix is strictly conditionally negative definite. Finally, finite Schoenberg embedding identifies negative type of \(d^p\) with isometric embedding of \(d^{p/2}\) into real Hilbert space. The asymptotic follows by expanding \(-\log(1-1/q)/\log2\).

## Verification

The included `affine_negative_type_checker.py` generates prime-field affine planes for \(q=2,3,5,7\), constructs all graph distances by breadth-first search, verifies both incidence identities and the complete distance block structure, and checks centered distance-matrix inertia just below, at, and above the predicted critical exponent. It also evaluates the block determinant, constant-mode form, and an explicit positive-energy parallel-class obstruction above the threshold. Run `python3 affine_negative_type_checker.py` with NumPy installed. This finite check does not establish the universal theorem or certify any non-Desarguesian plane; the proof above uses only affine-plane axioms.

## Relationship to prior work

Bartoli, Héger, Kiss, and Takáts [1] investigate the metric dimension of incidence graphs of arbitrary affine planes, including the role of parallel classes, not their supremal negative type. Robertson [2] establishes a general distance-matrix criterion for maximal generalized roundness and explains its connection with Hilbert embeddings, but does not explicitly evaluate the affine-plane incidence family. Earlier computations for projective-plane or symmetric-design incidence metrics do not automatically apply: these have equal point and line populations, and in the affine graph parallel lines are distance \(4\), rather than distance \(2\) through an ideal point. The exact logarithmic threshold and endpoint dimension drop here arise from the parallel-class eigenspace.

## Limitations

The result applies only to finite affine planes of order at least two and their unweighted point--line incidence graph metrics. It does not address affine-plane existence at unknown orders, weighted incidences, or arbitrary resolvable block designs. This is an analytical derivation with a finite numerical cross-check, not an independent mathematical audit. A historically equivalent calculation under alternate generalized-roundness, design, or kernel terminology cannot be excluded categorically.

## References

[1] D. Bartoli, T. Héger, G. Kiss, and M. Takáts, *On the metric dimension of affine planes, biaffine planes and generalized quadrangles*, first public preprint 20 June 2017, arXiv:1706.06583v1. https://arxiv.org/abs/1706.06583

[2] G. Robertson, *The Maximal Generalised Roundness of Finite Metric Spaces*, first public preprint 23 April 2020, arXiv:2004.10923v1. https://arxiv.org/abs/2004.10923

[3] I. J. Schoenberg, *On certain metric spaces arising from Euclidean spaces by a change of metric and their imbedding in Hilbert space*, Ann. Math. 38 (1937), 787–793 (classical embedding principle).
