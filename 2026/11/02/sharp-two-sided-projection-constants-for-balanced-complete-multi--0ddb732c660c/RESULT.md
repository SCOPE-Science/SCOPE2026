# Sharp two-sided projection constants for balanced complete multipartite edge spaces

## Finding
For every pair of integers \(r\ge3\) and \(q\ge2\), let \(G=K_{q,\ldots,q}\) have \(r\) parts, each of size \(q\). Endow its oriented real edge space \(X=\ell_1(E(G))\) with the sum-of-absolute-coordinates norm. Write \(D:X\to\mathbb R^{rq}\) for its incidence map, \(C=\operatorname{ran}D^T\) for its cut space, and \(Z=\ker D\) for its circulation space. Define \(\lambda_X(Y)=\inf\{\|P\|_{1\to1}:P^2=P,\operatorname{ran}P=Y\}\). Then
\[
\lambda_X(C)=\frac{2(q^2r^2-q^2-2qr+2)}{q^2r(r-1)},\qquad
\lambda_X(Z)=\frac{3q^2r^2-q^2r-2q^2-8qr+8}{q^2r(r-1)}.
\]
The Euclidean-orthogonal projections \(Q=D^T(DD^T)^+D\) and \(I-Q\) attain these two minima. In fact, each is the *only* projection onto its respective range commuting with all graph automorphisms. Their norms satisfy
\[
\lambda_X(Z)-\lambda_X(C)=1-\frac{4(rq-1)}{rq^2(r-1)}>0.
\]
For fixed \(r\), the two constants tend respectively to \(2+2/r\) and \(3+2/r\) as \(q\to\infty\); for fixed \(q\), they tend to \(2\) and \(3\) as \(r\to\infty\).

## Assumptions and scope
The graph is simple, undirected, unweighted, and has every edge between different parts and no edge within any part. Choose arbitrary orientations solely to identify \(X\) with \(\mathbb R^{E(G)}\); changing them conjugates matrices by diagonal signs, leaving all stated norms unchanged. Set \(N=rq\) and \(L=DD^T\). The Moore--Penrose inverse is with respect to Euclidean coordinate inner products, and the image of \(D\) is the zero-sum vertex hyperplane \(V_0\). All projections optimized here are arbitrary **linear** projections in the full real edge-\(\ell_1\) space, not just orthogonal or symmetry-constrained projections.

## Proof
**1. Symmetry forces the optimal projections.** The wreath-product permutation group \(H=S_q\wr S_r\) acts transitively on the undirected edges and by signed permutations on their oriented coordinate vectors. Its edge action preserves both \(C\) and \(Z\). Averaging a projection onto either subspace over \(H\) preserves its range, identity restriction to that range, and the projection property, while not increasing its \(\ell_1\) operator norm.

We prove that an \(H\)-equivariant projection \(P\) onto \(C\) must equal \(Q\). Write \(T=DP:X\to V_0\), which is equivariant. Fix an oriented edge \(e_{uv}\) with \(u\) in part \(A\), \(v\) in distinct part \(B\), and \(D e_{uv}=\delta_u-\delta_v\). Permutations fixing \(u,v\) force \(T e_{uv}\) to be constant on \(A\setminus\{u\}\), \(B\setminus\{v\}\), and each remaining part. An automorphism interchanging \(A\) and \(B\), swapping \(u,v\), and fixing all vertices outside \(A\cup B\) sends \(e_{uv}\) to \(-e_{uv}\); therefore the values on the other parts vanish, while corresponding values on \(A,B\) have opposite signs. Thus there exist scalars \(s,t\) such that
\[
T e_{uv}=s(\delta_u-\delta_v)+t({\bf1}_A-{\bf1}_B).
\]
Let \(R:V_0\to V_0\) average a vertex function separately over each part. The equivariant vertex map \(S=sI+tqR\) satisfies \(T e_{uv}=SDe_{uv}\). Edge transitivity implies \(T=SD\) on all of \(X\). Since \(P\) is the identity on \(C=\operatorname{ran}D^T\), it follows that \(SL=TD^T=DD^T=L\) on \(V_0\). Connectivity makes \(L|_{V_0}\) invertible, so \(S=I\), \(DP=D\), and the injectivity of \(D|_C\) yields \(P=Q\).

If \(P\) is instead an equivariant projection onto \(Z\), then its Euclidean adjoint \(P^T\) has kernel \(Z^\perp=C\), and \(I-P^T\) is an equivariant projection onto \(C\). Uniqueness just proved gives \(I-P^T=Q\), hence \(P=I-Q\). Thus these orthogonal projections minimize their respective norms among *all* projections.

**2. Exact orthogonal projection coefficients.** The Laplacian \(L\) acts by \(N\) on partwise-constant zero-sum vertex vectors and by \(N-q=q(r-1)\) on vectors whose coordinate sum within each part vanishes. For the fixed edge \(e_{uv}\), decompose its incidence vector into the two eigenspaces and apply \(L^+\). The vertex potential \(\phi=L^+(\delta_u-\delta_v)\) equals \(a\) at \(u\), \(-a\) at \(v\), \(-b\) at the remaining vertices of \(A\), \(b\) at the remaining vertices of \(B\), and zero elsewhere, where
\[
a=\frac{rq-1}{rq^2(r-1)},\qquad b=\frac1{rq^2(r-1)}.
\]
The \(e_{uv}\) column of \(Q\) is the vector of oriented differences \(\phi_x-\phi_y\) across every edge \(xy\). Counting edge classes gives its absolute column sum
\[
2a+2(q-1)(a-b)+2(q-1)^2b+2(r-2)qa+2(r-2)q(q-1)b
=\frac{2(q^2r^2-q^2-2qr+2)}{q^2r(r-1)}.
\]
All columns have the same norm by edge transitivity; therefore this is \(\|Q\|_{1\to1}\). Its diagonal entries equal \(2a\), with \(0<2a<1\); off-diagonal entries in \(I-Q\) have opposite sign to those in \(Q\). Consequently
\[
\|I-Q\|_{1\to1}=1+\|Q\|_{1\to1}-4a,
\]
which simplifies to the claimed formula for \(\lambda_X(Z)\). Finally \(q(r-1)\ge4\) for the stated parameter range, so \(rq^2(r-1)-4(rq-1)=rq(q(r-1)-4)+4>0\). This proves strict separation. The stated limits follow by dividing numerators and denominators by the dominant powers of \(q\) or \(r\), respectively.

## Verification
The included `balanced_multipartite_checker.py` uses only Python's standard library and exact rational arithmetic. Execute `python balanced_multipartite_checker.py`. It constructs the complete oriented incidence graph, exact orthogonal projection, full matrix idempotence, invariance on cut gradients, and every column norm of both complementary projections for the cases \((r,q)=(2,2),(2,3),(2,4),(3,2),(3,3),(4,2),(4,3),(5,2),(5,3)\). The \(r=2\) cases are supplementary boundary cross-checks, not new-claim parameters. Successful output ends in `CHECK_OK`. The proof for arbitrary \(r,q\) is analytical and does not rest on finite testing.

## Relationship to prior work
Dilworth--Kutzarova--Ostrovskii (2023, arXiv:2305.12582) develop symmetry averaging and invariant minimal projections onto graph cycle spaces, particularly discrete tori and Hamming graphs. Its discussion and section summaries do not give the two formulas above for balanced complete multipartite graphs. Their 2018 paper (arXiv:1807.03814) develops cycle-space methods for free spaces, especially recursive graph families. Existing complete-bipartite matrix-centering results address two parts; the present hypothesis requires at least three parts, and the symmetry type and strict two-sided formulas differ. General invariant-projection techniques are therefore acknowledged as prior tools, not claimed as new.

## Limitations
This result treats equal part sizes and the real coordinate-\(\ell_1\) edge norm. It does not cover unequal multipartite sizes, weighted edges, arbitrary \(\ell_p\) exponents, or the uniqueness of *all* (not merely automorphism-invariant) minimizers. The literature comparison is not an independent priority certification; unindexed equivalent results under electrical-flow or operator-projection terminology remain possible.

## References
- S. J. Dilworth, D. Kutzarova, and M. I. Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, arXiv:2305.12582, first public 2023-05-21, https://arxiv.org/abs/2305.12582.
- S. J. Dilworth, D. Kutzarova, and M. I. Ostrovskii, *Lipschitz free spaces on finite metric spaces*, arXiv:1807.03814, first public 2018-07-10, https://arxiv.org/abs/1807.03814.
