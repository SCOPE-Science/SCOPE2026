# A one-spike essential-spectrum transition for symmetric and antisymmetric shift tensors

## Finding

Let \(S_a\) be the unilateral forward weighted shift on \(\ell^2(\mathbb N_0)\) with weights \(w_0=a>0\) and \(w_j=1\) for every \(j\ge 1\). On the second Hilbert tensor power define
\[
T_a=\tfrac12(S_a\otimes S_a^*+S_a^*\otimes S_a).
\]
The tensor flip commutes with \(T_a\), so its restrictions \(T_a^+\) and \(T_a^-\) to the flip-even (symmetric) and flip-odd (antisymmetric) subspaces are bounded self-adjoint operators. Their **Fredholm essential spectra are identical**, with an exact transition at \(a=\sqrt2\):
\[
\boxed{
\sigma_{\mathrm{ess}}(T_a^+)=\sigma_{\mathrm{ess}}(T_a^-)=
\begin{cases}
[-1,1], & 0<a\le\sqrt2,\\[2pt]
[-1,1]\cup\{-E_a,E_a\},&a>\sqrt2,
\end{cases}
\quad E_a=\frac{a^2}{2\sqrt{a^2-1}}.
}
\]
In the supercritical case \(E_a>1\). Their exact essential norms are
\[
\boxed{
\|T_a^+\|_{\mathrm e}=\|T_a^-\|_{\mathrm e}=
\begin{cases}1,&0<a\le\sqrt2,\\ E_a,&a>\sqrt2.\end{cases}
}
\]
The two detached points are isolated **essential** spectral points, not merely isolated eigenvalues of a single finite section. For \(a>\sqrt2\), the positive detachment has quadratic onset:
\[
E_a-1=\frac{(\sqrt{a^2-1}-1)^2}{2\sqrt{a^2-1}}
\sim \frac{(a^2-2)^2}{8}\qquad(a\downarrow\sqrt2).
\]

## Assumptions and scope

The Hilbert space is complex \(H=\ell^2(\mathbb N_0)\), with orthonormal basis \((e_j)_{j\ge0}\). We use \(S_a e_j=w_j e_{j+1}\) with \(w_0=a>0\), \(w_j=1\) for \(j\ge1\); no normalization of \(S_a\) to operator norm one is imposed. The flip \(F(e_i\otimes e_j)=e_j\otimes e_i\) has eigenspaces \(H_+=\ker(F-I)\) and \(H_-=\ker(F+I)\). The standard symmetric tensor product \(S_a\odot S_a^*\) equals \(T_a^+\), and the exterior/antisymmetric tensor product \(S_a\wedge S_a^*\) equals \(T_a^-\), in the convention where two-factor symmetrization averages the two orders.

The essential spectrum means \(\sigma_{\mathrm{ess}}(T)=\{\lambda:T-\lambda I\text{ is not Fredholm}\}\). For a bounded self-adjoint operator, it is also the set of spectral accumulation points together with infinite-multiplicity eigenvalues, equivalently the set admitting an orthonormal Weyl sequence. The essential norm means distance to the compact operators. The result concerns the essential spectra, **not** the complete lists of isolated finite-multiplicity eigenvalues or the ordinary operator norms.

## Proof

**1. Homogeneous blocks and reflection.** For each \(k\ge0\), let
\[
V_k=\operatorname{span}\{e_j\otimes e_{k-j}:0\le j\le k\}.
\]
The spaces \(V_k\) are pairwise orthogonal, span \(H\otimes H\), and reduce \(T_a\). With \(n=k+1\), the restriction is the \(n\)-by-\(n\) real Jacobi matrix \(J_n\) with zero diagonal and off-diagonal entries
\[
(J_n)_{j,j+1}=(J_n)_{j+1,j}=\tfrac12w_jw_{n-j-2}
\quad(0\le j<n-1).
\]
For \(n\ge3\) its two outer edges have coefficient \(a/2\), while every interior edge has coefficient \(1/2\). The exceptional blocks \(n=1,2\) are finite dimensional and do not affect the essential spectrum (for \(n=2\), its unique off-diagonal entry is \(a^2/2\)). On \(V_k\), tensor flip is coordinate reflection \(R_n(x_0,\ldots,x_{n-1})=(x_{n-1},\ldots,x_0)\), and \(J_nR_n=R_nJ_n\). Thus
\[
T_a^\pm\cong\bigoplus_{n\ge1}J_n^\pm,
\]
where \(J_n^\pm\) are the restrictions to the \(\pm1\) reflection eigenspaces, omitting zero-dimensional summands. Both parity dimensions tend to infinity.

**2. Exterior eigenvalues and their only possible accumulation points.** Fix real \(|\lambda|>1\) and \(n\ge3\), and put \(m=n-2\). Remove the two end vertices of \(J_n\). The remaining \(m\)-site free Jacobi matrix \(F_m\) has zero diagonal and constant off-diagonal \(1/2\), hence \(\sigma(F_m)\subset[-1,1]\). Define
\[
g_m(\lambda)=\langle e_1,(\lambda I-F_m)^{-1}e_1\rangle,
\qquad
h_m(\lambda)=\langle e_1,(\lambda I-F_m)^{-1}e_m\rangle.
\]
For the Chebyshev polynomials of the second kind \(U_m\), with \(U_0=1\), \(U_1(x)=2x\), \(U_{m+1}(x)=2xU_m(x)-U_{m-1}(x)\), the continuant identity gives
\[
\det(\lambda I-F_m)=2^{-m}U_m(\lambda),\qquad
g_m=\frac{2U_{m-1}(\lambda)}{U_m(\lambda)},\quad h_m=\frac{2}{U_m(\lambda)}.
\]
The last formula follows by evaluating the corner cofactor. These identities also hold for \(m=1\), when the two designated interior endpoints are the same coordinate.

Taking the Schur complement of \(\lambda I-J_n\) in the two end coordinates gives
\[
\begin{pmatrix}
\lambda-\tfrac{a^2}{4}g_m&-\tfrac{a^2}{4}h_m\\
-\tfrac{a^2}{4}h_m&\lambda-\tfrac{a^2}{4}g_m
\end{pmatrix}.
\]
An exterior eigenvalue of the even or odd reflection block is therefore a zero of, respectively,
\[
f_m^\pm(\lambda)=\lambda-\frac{a^2}{4}(g_m(\lambda)\pm h_m(\lambda)).
\]
Set \(\rho(\lambda)=\lambda-\operatorname{sgn}(\lambda)\sqrt{\lambda^2-1}\); then \(|\rho(\lambda)|<1\), \(\lambda=(\rho+\rho^{-1})/2\), and the explicit Chebyshev formula shows that, **uniformly on every compact subset of** \(\mathbb R\setminus[-1,1]\),
\[
\frac{U_{m-1}(\lambda)}{U_m(\lambda)}\longrightarrow\rho(\lambda),
\qquad\frac1{U_m(\lambda)}\longrightarrow0.
\]
Hence both parity functions converge uniformly to the same function
\[
f(\lambda)=\lambda-\frac{a^2}{2}\rho(\lambda).
\]
If infinitely many distinct homogeneous blocks have an eigenvalue approaching an exterior real \(\lambda\), necessarily \(f(\lambda)=0\). Inserting \(2\lambda=\rho+\rho^{-1}\) into that equation yields
\[
(a^2-1)\rho^2=1.
\]
A solution with \(|\rho|<1\) exists **if and only if** \(a>\sqrt2\), when its only possibilities are \(\rho=\pm(a^2-1)^{-1/2}\), corresponding to \(\lambda=\pm E_a\). Compact uniform convergence also excludes any other exterior accumulation of the block spectra. The finitely many exceptional small blocks cannot create an essential spectral point.

**3. Weyl sequences throughout the band, separately in each parity.** Fix \(\lambda=\cos\theta\in[-1,1]\) and let \(L\to\infty\), with \(n=4L+5\). In the interior of \(J_n\), choose a vector equal to \(e^{ij\theta}\) on a run of \(L\) consecutive coordinates well separated from both ends and zero elsewhere; reflect it and add or subtract the reflected vector. The two supports are disjoint, and the resulting vector has reflection parity \(+\) or \(-\). On all but a fixed number of coordinates, \(J_nx=\lambda x\); the residual has uniformly bounded norm while \(\|x\|=\sqrt{2L}\). Normalizing therefore gives an approximate eigenvector with residual \(O(L^{-1/2})\). Choosing each normalized vector in a different \(V_{n-1}\) makes the vectors orthonormal. Weyl's criterion proves \([-1,1]\subset\sigma_{\mathrm{ess}}(T_a^\pm)\).

**4. The detached points belong to both essential spectra.** Assume \(a>\sqrt2\), put \(\rho=(a^2-1)^{-1/2}\in(0,1)\), and let \(E=E_a\). Consider the half-line Jacobi matrix with first off-diagonal \(a/2\) and all subsequent off-diagonals \(1/2\). The square-summable vector
\[
u_0=\frac a{2E},\qquad u_j=\rho^{j-1}\quad(j\ge1)
\]
satisfies \(Ju=Eu\) exactly: the initial row gives \(Eu_0=(a/2)u_1\), and the remaining rows follow from \(2E=\rho+\rho^{-1}\) and \(a^2=1+\rho^{-2}\). Multiplying coordinate \(j\) by \((-1)^j\) gives a square-summable vector for eigenvalue \(-E\).

Truncate either half-line vector at coordinate \(L\), embed it at the left end of a large \(J_n\) with \(n>2L+3\), and add or subtract its reflected copy. The resulting vector lies in the desired parity subspace and its relative residual is \(O(\rho^{L-1})\), since only the exponential tail is cut. Taking \(L\to\infty\) in mutually orthogonal homogeneous blocks yields orthonormal Weyl sequences at \(+E\) and \(-E\) in **each** parity. Hence both points lie in each Fredholm essential spectrum.

The exterior exclusion in step 2 and the Weyl constructions in steps 3–4 prove the asserted essential-spectrum equality for all \(a>0\). For bounded self-adjoint operators, the essential norm equals the maximum modulus of the essential spectrum, giving the claimed essential norm. Finally, the identity for \(E_a-1\) is an elementary rearrangement, and its indicated quadratic asymptotic follows by expansion at \(a^2=2\).

## Verification

The accompanying `VERIFY.py` reconstructs the real Jacobi matrix and its even/odd folded blocks for several spike parameters and finite homogeneous degrees. It checks the folding intertwining, spectral reconstruction, subcritical edge bounds in the tested sizes, supercritical convergence to the predicted detached points, and the half-line eigenvector recurrences. It completed **2,371 deterministic assertions** using NumPy/SciPy. Run with `python VERIFY.py` after installing `numpy` and `scipy`. These finite computations are not a proof of the limiting statements; the uniform Chebyshev-resolvent argument and orthogonal Weyl sequences are the infinite-dimensional certification within this mathematical proof.

## Relationship to prior work

Garcia, O'Loughlin and Yu calculated the unweighted shift/adjoint tensor spectra and posed the weighted-shift problem. Tian, Wang and Zhu gave norm results for regular weighted shifts. Yang and Zhang developed the general **finite-block point-spectrum characteristic-polynomial algorithm** for weighted shifts and their adjoints. Their finite-block formalism is the natural starting point, and the present homogeneous Jacobi reduction is consistent with it; **the reduction alone is not claimed as new**. The present quantitative statement is the explicit Fredholm essential-spectrum limit for a one-spike family, the common symmetric/antisymmetric detachment threshold, and the two detached essential points. Their appearance requires a boundary Green-function limit plus Weyl sequences, rather than only enumerating the finite-block eigenvalues. General half-line Jacobi boundary perturbation techniques are also established mathematical background and not independently claimed as new here.

## Limitations

The theorem treats the scalar one-spike family \(w_0=a\), \(w_j=1\) thereafter, not arbitrary convergent or periodic weights. It determines Fredholm essential spectra and essential norms, not all discrete finite-multiplicity eigenvalues or ordinary norms. Finite numerical checks provide corroboration but not an independent correctness assessment. Literature equivalence under different Jacobi or tensor-product terminology remains a residual publication-priority risk.

## References

1. S. R. Garcia, R. O'Loughlin, J. Yu, *Symmetric and Antisymmetric Tensor Products for the Function-Theoretic Operator Theorist*, arXiv:2306.14807 (first version 2023); Canadian Journal of Mathematics, Theorem 8.1 and Problem 7. https://arxiv.org/abs/2306.14807
2. X. Tian, P. Wang, Z. Zhu, *The norms for symmetric and antisymmetric tensor products of the weighted shift operators*, arXiv:2507.17181 (first version 2025-07-23), Theorem 1.3. https://arxiv.org/abs/2507.17181
3. Y. Yang, Y. Zhang, *On the spectrum of the symmetric tensor products of certain Hilbert-space operators*, arXiv:2509.07374 (first version 2025-09-09), Theorem 3.3 and Corollary 3.5. https://arxiv.org/abs/2509.07374
4. M. Webb, S. Olver, *Spectra of Jacobi operators via connection coefficient matrices*, Communications in Mathematical Physics 382 (2021), 657–707. https://doi.org/10.1007/s00220-021-03939-w
