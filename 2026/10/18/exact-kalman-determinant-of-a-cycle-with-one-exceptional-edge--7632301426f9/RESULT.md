# Exact Kalman determinant of a cycle with one exceptional edge

## Finding

Let \(n\ge 3\) be an integer, and let \(L_n(w)\) be the symmetric Laplacian on the vertex set \(\{0,\ldots,n-1\}\): the edges \(\{i,i+1\}\), \(0\le i<n-1\), have weight one, and the closing edge \(\{n-1,0\}\) has real weight \(w\). Define the single-input Krylov matrix
\[
\mathcal K_n(w)=[e_0,L_n(w)e_0,\ldots,L_n(w)^{n-1}e_0].
\]
With \(r_n=\lfloor(n-1)/2\rfloor\), its determinant is the following **exact polynomial identity**, valid for every real or complex \(w\):
\[
\boxed{\det\mathcal K_n(w)=(-1)^{n+1}(w-1)^{r_n}(1+(n-1)w).}
\]
Consequently, for strictly positive conductances \(w>0\), the pair \((L_n(w),e_0)\), equivalently \((-L_n(w),e_0)\), is controllable if and only if \(w\ne1\). For arbitrary real weights it is uncontrollable exactly at \(w=1\) or \(w=-1/(n-1)\). At \(w=1\), its Kalman rank is exactly \(\lfloor n/2\rfloor+1\).

The finite Krylov-Gramian determinant is therefore
\[
\det\bigl(\mathcal K_n(w)\mathcal K_n(w)^\mathsf T\bigr)
=(w-1)^{2r_n}(1+(n-1)w)^2.
\]
For every fixed \(n\), as positive \(w\) tends to one through unequal weights, the smallest singular value of \(\mathcal K_n(w)\) is \(\Theta_n(|w-1|)\), and the least Krylov-Gramian eigenvalue is \(\Theta_n((w-1)^2)\). Thus full controllability can be restored by an arbitrarily small edge-weight defect, while its smallest finite-Krylov energy collapses quadratically when the defect disappears.

## Assumptions and scope

The underlying undirected graph is a simple cycle with \(n\ge3\) vertices. The input acts at vertex \(0\), which is an endpoint of the exceptional edge. Every other edge has unit weight; the exceptional real weight may be positive, zero, or negative for the polynomial identity. The claim about a connected diffusion network assumes \(w>0\). The Krylov convention uses positive \(L_n(w)\); replacing it by negative \(L_n(w)\) changes column signs but not rank or Gramian eigenvalues. The finite Krylov-Gramian is not the continuous-time finite-horizon input Gramian, and no uniform-in-\(n\) conditioning bound is claimed.

## Proof

**1. Reflection decomposition.** Reflect vertices by \(i\mapsto n-1-i\). The weighted Laplacian commutes with this reflection because the exceptional edge is fixed as an unordered pair. Use the normalized symmetric and antisymmetric vectors \((e_i\pm e_{n-1-i})/\sqrt2\), ordered from the exceptional edge toward the opposite end. In this orthogonal basis,
\[
L_n(w)\simeq S\oplus A(w),\qquad
 e_0\simeq 2^{-1/2}(f_S\oplus f_A),
\]
where \(f_S,f_A\) are the first coordinate vectors. The symmetric tridiagonal matrix \(S\) is independent of \(w\). The antisymmetric matrix has size \(m\) and satisfies
\[
A(w)=A(1)+2(w-1)f_Af_A^\mathsf T.
\]
If \(n=2m+1\), then \(S\) has size \(m+1\), diagonal entries \(1,2,\ldots,2\), and consecutive off-diagonal entries \(-1,\ldots,-1,-\sqrt2\); \(A(w)\) has size \(m\), diagonal \(1+2w,2,\ldots,2\), and all consecutive off-diagonals \(-1\). This description includes \(m=1\). If \(n=2m\), then \(S\) has size \(m\), diagonal \(1,2,\ldots,2,1\), and off-diagonals \(-1\); \(A(w)\) has size \(m\), diagonal \(1+2w,2,\ldots,2,3\), and off-diagonals \(-1\). The even case has \(m\ge2\). Each block is an irreducible Jacobi matrix whose first coordinate vector is cyclic. The consecutive off-diagonals do not depend on \(w\).

**2. A cyclic-block resultant identity.** For any irreducible Jacobi matrix \(J\) of size \(d\), the matrix \([f,Jf,\ldots,J^{d-1}f]\), with \(f\) its first coordinate vector, is upper triangular: its \((k+1)\)-st diagonal entry is the product of the first \(k\) consecutive subdiagonals of \(J\). Its determinant is therefore nonzero and depends on those subdiagonals alone, not on the diagonal entries. For the direct sum \(S\oplus A(w)\), diagonalization at weights where the two simple spectra are disjoint gives the Vandermonde determinant of all their eigenvalues, multiplied by the first-coordinate eigenvector weights. Factor the Vandermonde into the within-block Vandermondes and cross-block differences. Consequently,
\[
\det\mathcal K_n(w)
=C_n\operatorname{Res}_z(P_S(z),P_{A(w)}(z)),
\]
where \(P_J(z)=\det(zI-J)\), \(\operatorname{Res}\) is the ordinary monic-polynomial resultant, and \(C_n\ne0\) is independent of \(w\). The preceding Jacobi observation makes this independence explicit. The identity extends from disjoint spectra to all \(w\) by polynomial continuity.

**3. Factor the resultant.** At \(w=1\), the unweighted cycle has distinct Laplacian spectral values \(\lambda_k=2-2\cos(2\pi k/n)\). For odd \(n=2m+1\), the spectrum of \(S\) is \(\{\lambda_0,\ldots,\lambda_m\}\), while that of \(A(1)\) is \(\{\lambda_1,\ldots,\lambda_m\}\). For even \(n=2m\), the spectrum of \(S\) is \(\{\lambda_0,\ldots,\lambda_{m-1}\}\), while that of \(A(1)\) is \(\{\lambda_1,\ldots,\lambda_m\}\). All listed values are distinct in each block. Thus exactly \(r_n=\lfloor(n-1)/2\rfloor\) nonzero eigenvalues are shared.

Let \(Q(z)\) be the characteristic polynomial of the matrix obtained from \(A(1)\) by deleting its first row and column. The rank-one determinant lemma yields
\[
P_{A(w)}(z)=P_{A(1)}(z)-2(w-1)Q(z).
\]
At each shared eigenvalue \(\lambda_k\), the first term vanishes, and \(Q(\lambda_k)\ne0\) by strict Jacobi interlacing. Every shared eigenvalue therefore contributes exactly one factor \(w-1\) to the resultant. Its remaining factor comes from the nonshared symmetric eigenvalue \(\lambda_0=0\). The continuant recurrences for the explicit antisymmetric blocks give
\[
\det A(w)=\begin{cases}
1+(n-1)w,&n\text{ odd},\\
2(1+(n-1)w),&n\text{ even}.
\end{cases}
\]
Because \(P_{A(w)}(0)=(-1)^m\det A(w)\), the product formula for a monic resultant yields
\[
\operatorname{Res}_z(P_S,P_{A(w)})
=c_n(w-1)^{r_n}(1+(n-1)w)
\]
with a nonzero, \(w\)-independent constant \(c_n\).

**4. Determine the exact constant.** At \(w=0\), the closing edge is absent and the graph is the unit path \(0-1-\cdots-(n-1)\). Each \(L_n(0)^k e_0\) is supported on vertices \(0,\ldots,k\), and its component at vertex \(k\) is \((-1)^k\). Thus \(\mathcal K_n(0)\) is triangular and
\[
\det\mathcal K_n(0)=(-1)^{n(n-1)/2}.
\]
Comparing with the factored expression at \(w=0\) fixes its constant to \((-1)^{n(n-1)/2-r_n}=(-1)^{n+1}\), proving the determinant formula for all \(w\).

**5. Rank and robustness.** Full controllability is equivalent to a nonzero Kalman determinant. At \(w=1\), the unweighted cycle has \(\lfloor n/2\rfloor+1\) distinct Laplacian eigenvalues, and the vertex vector \(e_0\) has a nonzero projection onto every eigenspace. Hence the Kalman rank equals that count. The exact Gram determinant follows by squaring the determinant. Set \(r=r_n\). The \(r\) singular values which vanish at \(w=1\) are each \(O_n(|w-1|)\) by Lipschitz dependence of singular values on matrix entries. The other singular values remain bounded above and below. Since their total product is a positive multiple of \(|w-1|^r\), each vanishing singular value must also be \(\Omega_n(|w-1|)\). This proves the claimed quadratic scaling of the least Gramian eigenvalue.

For the signed-edge extension, the extra exceptional value \(w=-1/(n-1)\) is the boundary where the quadratic form \(\sum_{i=0}^{n-2}(x_i-x_{i+1})^2+w(x_{n-1}-x_0)^2\) develops a second zero mode: Cauchy–Schwarz gives \((x_{n-1}-x_0)^2\le(n-1)\sum_{i=0}^{n-2}(x_i-x_{i+1})^2\), with equality on linear vertex profiles. No assumption of positive physical conductance is made at this algebraic extension.

## Verification

Run `python verify.py` using Python 3 and SymPy. It performs exact symbolic polynomial checks at orders three through six, exact-rational full Krylov determinants at orders three through eighteen and seven real weights per order, unweighted Kalman-rank checks, and signed-edge nullity checks. The observed total is 144 exact assertions. This finite testing is independent corroboration, not a proof for unbounded \(n\); the proof above supplies the universal argument.

## Relationship to prior work

Parlangeli and Notarstefano (2011, arXiv:1109.3556, especially Theorem 4.10) give uniform-path/cycle reachability criteria, including the two-vertex control requirement for unweighted cycles, but do not give the exceptional-edge determinant. Monshizadeh, Zhang, and Camlibel (2014, arXiv:1403.4868) characterize graph-structured controllability through zero-forcing conditions that ensure reachability for **all** matrices of a support pattern. Their two-leader robust guarantee does not exclude a one-leader controllable **particular** weighted Laplacian. Xiang and collaborators (2013) discuss how changing edge weights can improve controllability, without this exact cycle identity. Grudsky, Maximenko, and Soto-González (2022, arXiv:2205.12457) analyze precisely the one-exceptional-edge cycle spectrum and provide explicit eigenvector formulas, supplying substantial prior spectral information; the closed Kalman determinant, Gramian volume, and singular-value scaling are not stated as their results. Because complete spectral information can in principle be combined with general Krylov determinant formulas, those later spectral results are a meaningful originality-risk comparison, not evidence of unrelatedness.

## Limitations

The exact formula fixes the input at an endpoint of the perturbed edge; arbitrary single-input locations have different controllability and determinant behavior. The finite Krylov-Gramian is an algebraic controllability-volume diagnostic, not a direct time-integrated control energy, and its numerical conditioning depends on units and the fixed power basis. The \(\Theta_n\) constants depend on graph order; no uniform large-cycle estimate is established. The spectral literature on the same one-edge-defect matrices leaves a risk of an equivalent, unindexed determinant specialization, and no independent scientific review has occurred.

## References

1. G. Parlangeli and G. Notarstefano, *On the reachability and observability of path and cycle graphs*, arXiv:1109.3556v1, posted 16 September 2011, https://arxiv.org/abs/1109.3556.
2. L. Xiang, J. J. H. Zhu, F. Chen, and G. Chen, *Controllability of Weighted and Directed Networks with Nonidentical Node Dynamics*, Mathematical Problems in Engineering (2013), DOI 10.1155/2013/405034, https://doi.org/10.1155/2013/405034.
3. N. Monshizadeh, S. Zhang, and M. K. Camlibel, *Zero forcing sets and controllability of dynamical systems defined on graphs*, arXiv:1403.4868v1, posted 19 March 2014, https://arxiv.org/abs/1403.4868.
4. S. M. Grudsky, E. A. Maximenko, and A. Soto-González, *Eigenvalues of the laplacian matrices of the cycles with one weighted edge*, arXiv:2205.12457v1, posted 25 May 2022, https://arxiv.org/abs/2205.12457.
