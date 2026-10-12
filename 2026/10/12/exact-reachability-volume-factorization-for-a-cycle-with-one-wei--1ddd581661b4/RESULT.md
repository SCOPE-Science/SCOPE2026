# Exact reachability-volume factorization for a cycle with one weighted edge

## Finding

Fix an integer \(n\ge 3\). Label the vertices of a cycle \(0,1,\ldots,n-1\), assign unit weight to the edges \(\{i,i+1\}\) for \(0\le i<n-1\), and assign real weight \(w\) to the closing edge \(\{n-1,0\}\). Let \(L_n(w)\) be the signed weighted graph Laplacian, with each edge of weight \(c\) contributing \(c(e_i-e_j)(e_i-e_j)^{\mathsf T}\). Put \(b=e_0\) and define the ordered Kalman matrix

\[
\mathcal K_n(w)=[\,b,\ L_n(w)b,\ \ldots,\ L_n(w)^{n-1}b\,].
\]

**Theorem.** For every \(n\ge3\) and every real \(w\),

\[
\boxed{\det\mathcal K_n(w)=(-1)^{n+1}
(w-1)^{\lfloor(n-1)/2\rfloor}\bigl(1+(n-1)w\bigr).}
\]

In particular, for a physical conductance \(w>0\), the one-input continuous-time system \(\dot x=-L_n(w)x+bu\) is controllable precisely when \(w\ne1\). The open-path limit \(w=0\) is controllable as well. The other real singular parameter, \(w=-1/(n-1)\), is the zero-mode resonance of a signed network.

For fixed \(n\), the squared volume of the ordered Krylov vectors satisfies

\[
\det\bigl(\mathcal K_n(w)\mathcal K_n(w)^{\mathsf T}\bigr)
=(w-1)^{2\lfloor(n-1)/2\rfloor}\bigl(1+(n-1)w\bigr)^2.
\]

Thus a single nonuniform edge restores rank, but as \(w\to1\), the squared reachability volume vanishes to exact order \(2\lfloor(n-1)/2\rfloor\). This is an algebraic volume of the finite Krylov matrix, not a claim about a normalized finite-time minimum-control-energy Gramian.

## Assumptions and scope

All statements use the combinatorial, not normalized, Laplacian, the above vertex ordering, and the **positive powers** of \(L_n(w)\) in the columns. Replacing \(L_n(w)\) by \(-L_n(w)\) multiplies the displayed determinant by \((-1)^{n(n-1)/2}\), without changing its zeros. Negative \(w\) is permitted solely to state the polynomial identity and its algebraic second root; positivity of graph conductances is needed only for the network-design interpretation. No time discretization or stochastic normalization is assumed.

## Proof

**1. Reflection blocks.** Let \(J e_i=e_{n-1-i}\). This reflection fixes the distinguished closing edge and commutes with \(L_n(w)\). Split the state space orthogonally into the \(+1\) and \(-1\) eigenspaces \(H_+\) and \(H_-\), of respective dimensions \(p=\lceil n/2\rceil\) and \(q=\lfloor n/2\rfloor\). Denote the restrictions by \(S\) and \(A_w\). The vector \(v=e_0-e_{n-1}\) lies in \(H_-\), and

\[
L_n(w)=L_n(0)+w vv^{\mathsf T},
\qquad A_w=A_0+2w ff^{\mathsf T},
\quad f=v/\sqrt2.
\]

Consequently \(S\) is independent of \(w\). In the bases made from successive reflected vertex pairs, \(S\) and \(A_w\) are real symmetric tridiagonal matrices with nonzero consecutive subdiagonals; these subdiagonals do not depend on \(w\). (A one-dimensional block is included.) The projections of \(b\) onto the two blocks are both the first basis coordinate times \(1/\sqrt2\).

**2. Cross-spectral determinant identity.** For any tridiagonal matrix \(T\) with nonzero fixed subdiagonals and first-coordinate input, the columns \([e_1,Te_1,\ldots,T^{d-1}e_1]\) form a triangular matrix: the entry in row \(j+1\), column \(j+1\) is the product of the first \(j\) subdiagonals. Its determinant is nonzero and does not depend on diagonal entries. Hence the two within-block Krylov determinants are nonzero constants independent of \(w\).

For a generic real \(w\) the spectra of \(S\) and \(A_w\) are disjoint. Diagonalize each symmetric block; applying the Vandermonde formula to the full Krylov matrix and separately to each block shows that the quotient of the full determinant by the two within-block determinants is, up to a constant sign, the cross-eigenvalue product. Therefore for some nonzero constant \(C_n\), independent of \(w\),

\[
\det\mathcal K_n(w)
=C_n\prod_{\lambda\in\sigma(S)}\det(\lambda I_q-A_w).
\tag{1}
\]

Here the eigenvalues of \(S\) occur once each. Since both sides are polynomials in \(w\), identity (1) extends from generic parameters to **every real** \(w\). This step does not assume simple eigenvalues of the full cycle at \(w=1\).

**3. Factors from the uniform cycle.** At \(w=1\), Fourier diagonalization of the uniform cycle shows that \(S\) has the distinct eigenvalues

\[
\lambda_j=2-2\cos(2\pi j/n),
\qquad 0\le j\le p-1.
\]

For each \(1\le j\le p-1\), \(\lambda_j\) also occurs **simply** in \(A_1\); when \(n\) is even, the additional antisymmetric eigenvalue \(4\) is not in \(S\). This follows by pairing sine and cosine Fourier modes under the edge reflection. The rank-one formula \(A_w=A_1+2(w-1)ff^{\mathsf T}\) makes \(\det(\lambda_jI_q-A_w)\) affine in \(w\), vanishing at \(w=1\). Its slope is nonzero: an eigenvector of an irreducible symmetric tridiagonal matrix has nonzero first component whenever its eigenvalue is simple, and the first-order eigenvalue derivative here is \(2|f^{\mathsf T}u_j|^2>0\). Thus, for every such \(j\),

\[
\det(\lambda_jI_q-A_w)=c_j(w-1),\qquad c_j\ne0.
\]

There are exactly \(p-1=\lfloor(n-1)/2\rfloor\) of these factors.

**4. The remaining factor.** Since the graph at \(w=0\) is a connected path, \(A_0\) has no zero eigenvalue: the constant null vector of the full path Laplacian belongs to \(H_+\). Thus \(\det(-A_w)\) is a nonzero affine function of \(w\). The antisymmetric vector with components \(z_i=i-(n-1)/2\) satisfies \(L_n(w)z=0\) precisely at \(w=-1/(n-1)\): every interior second difference vanishes, and at the endpoint the equation is \(-1-w(n-1)=0\). Therefore

\[
\det(-A_w)=c_0\bigl(1+(n-1)w\bigr),\qquad c_0\ne0.
\]

Substitution into (1) shows that \(\det\mathcal K_n(w)=C(w-1)^{\lfloor(n-1)/2\rfloor}(1+(n-1)w)\), with \(C\ne0\).

**5. Exact constant.** At \(w=0\), the matrix \(L_n(0)\) is the path Laplacian from endpoint \(0\). The \(j\)-th Krylov column has no entry beyond vertex \(j\), and its entry at vertex \(j\) is \((-1)^j\), for \(0\le j<n\). Thus \(\mathcal K_n(0)\) is triangular with

\[
\det\mathcal K_n(0)=(-1)^{n(n-1)/2}.
\]

Solving for \(C\) and checking the two parities of \(n\) gives \(C=(-1)^{n+1}\), completing the identity. The Kalman rank condition and the displayed Gram determinant identity are immediate.

## Verification

Run `python3 verify.py` from the directory containing this file. The Python-standard-library checker forms the weighted Laplacian using integers after clearing each rational weight's denominator, constructs every Krylov column, and computes the determinant by fraction-free Bareiss elimination. It performs **112 exact rational comparisons** with the theorem in dimensions \(3\) through \(18\), including the open path, uniform cycle, positive nonuniform weights, and signed-edge resonance. Its successful output begins `VERIFY_OK`. These finite checks independently test normalization and signs but do not prove the all-dimensions theorem.

## Relationship to prior work

Xiang, Zhu, Chen, and Chen (2013) study controllability of weighted and directed networks and include a single-leader **directed** cycle. Their controllability criteria motivate the network question but do not give a walk-matrix determinant for the present symmetric one-defect cycle. Zelazo and Bürger (2014) relate singularity under a negative edge weight to effective resistance; for a unit path their criterion explains the signed root \(w=-1/(n-1)\), but does not give the high-order factor at \(w=1\) or the determinant.

Grudsky, Maximenko, and Soto-González (2022) analyze **the same one-weighted-edge cycle**, proving eigenvalue localization and formulas for eigenvectors and their norms. Their spectral formulas supply data from which a Kalman determinant could in principle be reconstructed. The closed finite polynomial for the ordered Krylov determinant and the exact symmetry-restoration multiplicity are not stated in the inspected results. The theorem above obtains these facts by a reflection-block resultant argument. This relationship leaves a residual historical-priority risk; the result should not be interpreted as independent certification of novelty.

## Limitations

The theorem specifies a particular actuator at an endpoint of the distinguished edge. Actuators elsewhere can have additional exceptional weights or can fail permanently, so the determinant formula must not be transferred to them. The algebraic Krylov volume is not a finite-horizon continuous-time control-energy Gramian. The source comparison is not exhaustive, and an equivalent closed factorization could exist under the names *walk-matrix determinant*, *resultant*, or *controllability volume*.

## References

1. L. Xiang, J. J. H. Zhu, F. Chen, and G. Chen, “Controllability of Weighted and Directed Networks with Nonidentical Node Dynamics,” *Mathematical Problems in Engineering* (first published May 26, 2013), DOI: 10.1155/2013/405034.
2. D. Zelazo and M. Bürger, “On the Definiteness of the Weighted Laplacian and its Connection to Effective Resistance,” arXiv:1408.2187v1 (August 10, 2014).
3. S. M. Grudsky, E. A. Maximenko, and A. Soto-González, “Eigenvalues of the Laplacian Matrices of the Cycles with One Weighted Edge,” arXiv:2205.12457v1 (May 25, 2022); *Linear Algebra and its Applications* 653 (2022), 86–115, DOI: 10.1016/j.laa.2022.07.011.
