# Sharp rank transitions for Laplacian quantum walks on two-conductance stars

## Finding
Let a star have one center \(o\), \(p\ge1\) leaves connected to \(o\) with conductance \(a>0\), and \(q\ge1\) other leaves connected to \(o\) with conductance \(b>0\). Use its weighted combinatorial Laplacian \(L\) as the continuous-time quantum-walk Hamiltonian, and let \(\widehat M\) denote its infinite-time average-mixing matrix.

For every \(p+q\ge3\), if \(a=b\) then \(\widehat M\) is positive definite. If \(a\ne b\), then
\[
\ker\widehat M=\bigoplus_{c\in\{a,b\}:\,m_c=2}
\operatorname{span}\{e_{c,1}-e_{c,2}\},
\qquad m_a=p,\quad m_b=q.
\]
In particular,
\[
\operatorname{nullity}\widehat M
=\mathbf1_{\{p=2\}}+\mathbf1_{\{q=2\}}
\quad(a\ne b,\ p+q\ge3).
\]
For the three-vertex boundary \(p=q=1\), at **all** positive \(a,b\),
\[
\ker\widehat M=\operatorname{span}\{(b-a)e_o+a e_{a,1}-b e_{b,1}\},
\qquad\operatorname{rank}\widehat M=2.
\]
Thus, in a star of at least four vertices, splitting the edges into two different conductances introduces a zero mode precisely for each conductance class of **exactly two leaves**, irrespective of the positive conductance values. A uniform-conductance star of that order has no such zero mode.

## Assumptions and scope
The graph is finite and undirected; the weights \(a,b\) are real and strictly positive, and the integers \(p,q\) are at least one. Vertex basis vectors are \(e_v\). The weighted combinatorial Laplacian has off-diagonal entries \(L_{ov}=L_{vo}=-w_{ov}\), diagonal entries equal to incident conductance sums, and all other entries zero. The unitary evolution is \(U(t)=\exp(-itL)\). With \(\circ\) denoting entrywise multiplication, the average-mixing matrix is
\[
\widehat M=\lim_{T\to\infty}\frac1T\int_0^T U(t)\circ\overline{U(t)}\,dt
=\sum_{\theta\in\operatorname{spec}(L)}E_\theta\circ E_\theta,
\]
where each distinct eigenvalue appears once and \(E_\theta\) is its full orthogonal spectral projector. The latter identity proves that \(\widehat M\) is positive semidefinite.

## Proof
**1. Distinct conductances: spectral sectors.** Suppose \(a\ne b\). On the \(p\) leaves of type \(a\), the vectors whose coordinate sum is zero form a dark eigenspace with eigenvalue \(a\) and projector \(I_p-J_p/p\), embedded by zeros elsewhere. The corresponding type-\(b\) dark space has eigenvalue \(b\) and projector \(I_q-J_q/q\). Either dark sector has dimension zero when its size is one.

The remaining bright subspace, spanned by the center and the normalized constant vectors on the two leaf sets, is three-dimensional. It has eigenvalue zero and two positive nonzero eigenvalues \(\lambda_-,\lambda_+\), which are the roots of
\[
 z^2-\big((p+1)a+(q+1)b\big)z+(p+q+1)ab.
\]
They are distinct (the restriction of a connected weighted Laplacian to this invariant three-dimensional space is symmetric and its nonzero roots cannot coincide: its discriminant equals \(((p+1)a-(q+1)b)^2+4pqab>0\)). Substitution of \(a\) and \(b\) into the quadratic yields respectively \(pa(b-a)\) and \(qb(a-b)\), both nonzero. Thus none of the bright and dark eigenvalues coincide. Each bright spectral projector consequently has rank one.

**2. Full rank of the three bright square profiles, except at three vertices.** A normalized bright eigenvector has constant entries on each leaf class; write its vector of squared entries on the three representative cells as \(s_\theta\). Its projector contributes the rank-one positive semidefinite matrix \(s_\theta s_\theta^{\mathsf T}\) to the restriction of \(\widehat M\) to cell-constant coordinates. Accordingly the bright contribution has rank three exactly when these three profiles are independent.

Let \(T\) be the diagonal-moment matrix, with rows corresponding to \(o\), one type-\(a\) leaf, and one type-\(b\) leaf and columns indexed by moment orders \(0,1,2\), after subtracting the dark-projector contributions to each diagonal moment. Multiply the second row by \(p\) and the third by \(q\) to obtain
\[
T'=\begin{pmatrix}
1&pa+qb&(pa+qb)^2+pa^2+qb^2\\
1&a&(p+1)a^2\\
1&b&(q+1)b^2
\end{pmatrix}.
\]
Indeed, the center diagonal moments are \(1\), \(pa+qb\), and \((pa+qb)^2+pa^2+qb^2\), and the scaled bright diagonal moments for a type-\(a\) leaf are \(1,a,(p+1)a^2\), with the analogous expressions for type \(b\). Since \(T'\) is the matrix of squared bright-eigenvector cell profiles multiplied by an invertible diagonal scaling and a Vandermonde matrix in the three distinct bright eigenvalues, its determinant vanishes precisely when the three square profiles are dependent.

Direct expansion yields the exact identity
\[
\det T'=ab\left[a(p-1)(p+1-q)-b(q-1)(q+1-p)\right].
\]
If \(p>q\), the first bracketed summand is strictly positive and the second is nonnegative after its displayed subtraction; hence the determinant is positive. If \(p<q\), the determinant is negative by the reversed inequalities. If \(p=q\ge2\), the bracket reduces to \((p-1)(a-b)\), which is nonzero because \(a\ne b\). If \(p=q=1\), it is zero. Thus **for all \(p+q\ge3\)** the bright square profiles are independent and the bright part is positive definite on the three-dimensional cell-constant subspace.

**3. Dark contrasts.** On the sum-zero contrast subspace within a leaf class of size \(m\ge2\), the dark contribution to \(\widehat M\) is
\[
(I_m-J_m/m)\circ(I_m-J_m/m)
=(1-2/m)I_m+J_m/m^2.
\]
The corresponding eigenvalue on contrasts is \(1-2/m\): it is zero exactly when \(m=2\) and is strictly positive when \(m\ge3\). All bright contributions, and dark contributions of other classes, vanish on these contrast vectors. The decomposition into the cell-constant sector and class-contrast sectors is orthogonal and invariant under \(\widehat M\). Positivity established in step 2 then gives exactly the asserted kernel and nullity when \(a\ne b\) and \(p+q\ge3\).

**4. Coincident conductances.** When \(a=b\), merge both classes to obtain a uniform star with \(m=p+q\) leaves. There is a two-dimensional bright space, with Laplacian eigenvalues \(0\) and \((m+1)a\), and one dark eigenspace of dimension \(m-1\), with eigenvalue \(a\). The two bright eigenvector square profiles are independent for \(m\ge2\): the constant zero-mode has equal squares everywhere whereas the nonzero bright mode has a center squared amplitude \(m^2\) times that at each leaf. The dark contribution on the \(m-1\) contrasts has eigenvalue \(1-2/m\), strictly positive for \(m\ge3\). Hence \(\widehat M\) is positive definite whenever \(a=b\) and \(p+q\ge3\).

**5. The three-vertex boundary.** If \(p=q=1\), the three eigenvalues are distinct for \(a\ne b\), but the diagonal-moment determinant from step 2 is zero; it is also zero when \(a=b\) by the two-dimensional bright argument. Directly, the vector \(z=(b-a)e_o+a e_{a,1}-b e_{b,1}\) is orthogonal to every spectral-projector diagonal, as seen from its orthogonality to the zeroth, first and second diagonal-moment vectors \((1,1,1)\), \((a+b,a,b)\), and \((2a^2+2ab+2b^2,2a^2,2b^2)\). Spectral Vandermonde invertibility gives \(z\in\ker\widehat M\). Conversely, the constant eigenvector has equal squared coordinates, and any nonzero real eigenvector orthogonal to it cannot have three equal squared coordinates (an odd number of nonzero equal-magnitude real entries cannot sum to zero). Therefore at least two projector-diagonal vectors are independent, proving the rank is exactly two and the kernel exactly as stated. The vector formula also specializes correctly to \(a=b\).

## Verification
The accompanying `verify.py` constructs the **full** Laplacian, numerically diagonalizes it independently of the analytic bright/dark decomposition, groups repeated eigenvalues before forming spectral-projector Schur squares, and checks predicted ranks and explicit kernel contrasts for 245 profiles with leaf-class sizes from one through seven and five representative positive-weight pairs. An independent exact-rational three-by-three determinant calculation verifies the critical moment identity in 192 of those profiles. All assertions passed. The finite tests corroborate rather than replace the proof for arbitrary real conductances and unbounded class sizes.

## Relationship to prior work
Coutinho, Baptista, Godsil, Spier and Werner [1] give the general spectral-projector formula and exact average-mixing methods for adjacency-based quantum walks; it supplies the foundational identity but does not classify weighted-Laplacian stars. Coutinho, Godsil, Guo and Zhan [2] give a commutant-based rank framework for adjacency Hamiltonians, likewise without this weighted-Laplacian classification. The more recent Laplacian-star work of Mohan, Tamon, Xu and Zhan [3] addresses a trace (laziness) extremum for ordinary unweighted stars; its published abstract does not state an arbitrary two-conductance rank or kernel law. The present invariant is **rank/nullspace**, not trace, and the discontinuity between equal and unequal conductances prevents direct deduction from a uniform-star result.

## Limitations
The theorem concerns two positive real conductance values arranged in two nonempty groups on one star, not general weighted trees, more than two distinct conductances, signed/complex weights, instantaneous mixing, or quantum walks driven by weighted adjacency rather than the weighted Laplacian. The conclusions concern infinite-time averages, not finite-time uniformity. Although relevant literature was compared, it is possible that an unlocated stronger general theorem implies the classification; the 2026 Laplacian-star paper's full text was not available for comparison, so priority remains subject to further external review.

## References
[1] G. Coutinho, P. F. Baptista, C. Godsil, T. J. Spier, and R. Werner, *Irrational quantum walks*, arXiv:2208.08971v1, first submitted 18 August 2022, https://arxiv.org/abs/2208.08971.

[2] G. Coutinho, C. Godsil, K. Guo, and H. Zhan, *A New Perspective on the Average Mixing Matrix*, arXiv:1709.03591 (2017), https://arxiv.org/abs/1709.03591.

[3] A. Mohan, C. Tamon, Y. Xu, and H. Zhan, *Laziness of Quantum Walks on Graphs*, arXiv:2608.20739, 21 August 2026, https://arxiv.org/abs/2608.20739 (abstract accessible; full text not inspected).
