# Arithmetic rank law for quantum average mixing on paths with a single marked site

## Finding

Let \(n\ge2\) and \(1\le i\le n\) be integers. Let \(A_n\) be the adjacency matrix of the unweighted path with consecutively numbered vertices \(1,\ldots,n\). For every nonzero real \(\tau\), set \(H=A_n+\tau e_i e_i^{\mathsf T}\), and let \(\widehat M(H)\) be its infinite-time continuous-time quantum average-mixing matrix. Put \(d=\gcd(i,n+1)\). Then

\[
\operatorname{rank}\widehat M(H)=
\begin{cases}
(n+1)/2,&n\text{ odd and }i=(n+1)/2,\\
n-\lfloor(d-1)/2\rfloor,&\text{otherwise.}
\end{cases}
\]

The rank is **independent of the magnitude and sign** of the nonzero marking potential. In particular, \(\widehat M(H)\) is positive definite precisely if \(i\) is not the central vertex of an odd-order path and \(\gcd(i,n+1)\le2\). At zero marking, \(\operatorname{rank}\widehat M(A_n)=\lceil n/2\rceil\). The integer \(\lfloor(d-1)/2\rfloor\) measures the complete noncentral rank defect, whereas a centered mark preserves the unmarked rank.

## Assumptions and scope

The Hamiltonian acts on \(\mathbb C^n\) with unit real edge couplings, one diagonal entry \(\tau\) at the chosen site, and zero other diagonal entries. This is the adjacency-generated coherent walk with one on-site potential, **not** the graph Laplacian or a discrete-time walk. Write \(U(t)=e^{itH}\) and

\[
\widehat M(H)=\lim_{T\to\infty}\frac1T\int_0^T U(t)\circ\overline{U(t)}\,dt.
\]

The Schur product \(\circ\) is entrywise. The limit exists for every finite real symmetric \(H\). No assumption that \(\tau\) is integral or rational is needed for the theorem.

## Proof

**1. Reduction from average mixing to vertex-deleted polynomials.** A real symmetric tridiagonal matrix whose first subdiagonal entries are all nonzero has simple eigenvalues: its eigenvector is determined by its first entry via the three-term recurrence; an eigenvector with first entry zero is identically zero. Let the distinct eigenvalues of \(H\) be \(\lambda_1,\ldots,\lambda_n\), with unit real eigenvectors \(v_1,\ldots,v_n\). The Cesàro average deletes cross-frequency terms, giving

\[
\widehat M(H)=\sum_{k=1}^{n}(v_k\circ v_k)(v_k\circ v_k)^{\mathsf T}.
\]

Consequently, \(\operatorname{rank}\widehat M(H)\) is the rank of the matrix \((v_k(j)^2)_{k,j}\). The moment matrix \(W\), with entries \(W_{rj}=(H^r)_{jj}\) for \(0\le r\le n-1\), equals this matrix left-multiplied by the invertible Vandermonde matrix \((\lambda_k^r)_{r,k}\). Thus \(\operatorname{rank}\widehat M(H)=\operatorname{rank}W\).

Define \(p(z)=\det(zI-H)\) and \(q_j(z)=\det(zI-H^{(j)})\), where \(H^{(j)}\) deletes vertex \(j\). The diagonal adjugate formula and formal expansion at infinity give

\[
\frac{q_j(z)}{p(z)}=[(zI-H)^{-1}]_{jj}
=\sum_{r\ge0}(H^r)_{jj}z^{-r-1}.
\]

Because multiplication by the fixed monic \(p(z)\) gives a triangular invertible linear map between the first \(n\) Laurent coefficients and the coefficients of a polynomial of degree at most \(n-1\), \(\operatorname{rank}W=\dim\operatorname{span}\{q_1,\ldots,q_n\}\).

**2. Separate parities and reflection differences.** Introduce the monic path polynomials \(U_0(z)=1\), \(U_1(z)=z\), \(U_{r+1}(z)=zU_r(z)-U_{r-1}(z)\), i.e. the Chebyshev polynomials of the second kind evaluated at \(z/2\). The unmarked deleted-vertex polynomials are

\[
q_j^{(0)}(z)=U_{j-1}(z)U_{n-j}(z).
\]

They have parity \(n-1\) and satisfy \(q_j^{(0)}=q_{n+1-j}^{(0)}\). Moreover, \(q_1^{(0)}=U_{n-1}\) and \(q_j^{(0)}-q_{j-1}^{(0)}=U_{n-2j+1}\) for \(2\le j\le\lceil n/2\rceil\); the displayed polynomials have distinct leading degrees and span the \(\lceil n/2\rceil\)-dimensional space of polynomials of parity \(n-1\) and degree at most \(n-1\).

Deleting vertex \(j\) leaves a determinant affine in \(\tau\), so \(q_j=q_j^{(0)}-\tau r_j\), where \(r_j\) has parity \(n-2\) (or is zero). Projecting the span of the \(q_j\)'s onto parity \(n-1\) has full image as above, and its kernel consists exactly of reflection-antisymmetric combinations \(q_j-q_{n+1-j}\), one for each \(1\le j\le m:=\lfloor n/2\rfloor\). Therefore for \(\tau\ne0\),

\[
\operatorname{rank}\widehat M(H)=\lceil n/2\rceil+\dim\operatorname{span}\{T_j:1\le j\le m\},\qquad T_j=(q_j-q_{n+1-j})/\tau.
\]

A centered marked site in odd order is preserved by path reflection, so then every \(T_j\) vanishes, proving the central case.

**3. An exact formula for the reflection differences.** By path reflection it suffices to assume \(i\le m\). The unmarked resolvent satisfies

\[
[(zI-A_n)^{-1}]_{ab}
=\frac{U_{\min(a,b)-1}(z)U_{n-\max(a,b)}(z)}{U_n(z)}.
\]

The rank-one resolvent identity for the potential, applied to the diagonal minors, gives

\[
T_j=U_n\left(R_{0,ij}^{\,2}-R_{0,i,n+1-j}^{\,2}\right),\qquad R_0=(zI-A_n)^{-1}.
\]

The elementary Chebyshev identity \(U_a^2-U_b^2=U_{a+b+1}U_{a-b-1}\) for integers \(a\ge b\ge0\) cancels denominators and yields the **polynomial** identities

\[
T_j(z)=
\begin{cases}
U_{n-2i}(z)U_{j-1}(z)^2,&1\le j\le i,\\
U_{i-1}(z)^2U_{n-2j}(z),&i<j\le m.
\end{cases}
\]

**4. Count exactly the Chebyshev-gcd dependencies.** Put \(A=U_{n-2i}\) and \(B=U_{i-1}^2\). A linear relation among these \(m\) polynomials is equivalent to

\[
AC+BD=0,
\quad C\in\mathbb R[z]_{\mathrm{even},\deg\le2i-2},\quad
D\in\mathbb R[z]_{\mathrm{parity}\ n,\deg\le n-2i-2}.
\]

Indeed, the polynomials \(U_{j-1}^2\) for \(1\le j\le i\) form a triangular basis for the indicated even polynomials, and the polynomials \(U_{n-2j}\) for \(i<j\le m\) form a triangular basis of the second space (the latter is zero when its degree bound is negative).

Chebyshev root formula \(U_r(2\cos(k\pi/(r+1)))=0\), for \(1\le k\le r\), shows that the polynomials \(U_r\) have simple roots and

\[
G:=\gcd_{\mathbb R[z]}(A,B)=U_{d-1},
\qquad d=\gcd(i,n+1).
\]

Here \(\gcd(i,n-2i+1)=\gcd(i,n+1)=d\). Writing \(A=GA'\) and \(B=GB'\), with coprime \(A',B'\), every relation is uniquely of the form \(C=B'E\), \(D=-A'E\). The condition on \(D\) forces \(\deg E\le d-3\) and the parity condition forces \(E(-z)=(-1)^{d-1}E(z)\). Conversely every polynomial \(E\) meeting these conditions produces exactly one relation, since both \(C\) and \(D\) then belong to their specified spaces. The dimension of this \(E\)-space is precisely \(\lfloor(d-1)/2\rfloor\). Thus

\[
\dim\operatorname{span}\{T_1,\ldots,T_m\}=m-\lfloor(d-1)/2\rfloor.
\]

Adding the \(\lceil n/2\rceil\) symmetric dimensions proves the noncentral formula. For zero marking all antisymmetric differences vanish and only the \(\lceil n/2\rceil\) unmarked directions remain. The positive-semidefinite Gram representation in Step 1 shows that full rank is equivalent to positive definiteness, completing the proof.

## Verification

The bundled standalone Python checker `verify_marked_path.py` uses only the Python standard library. Run `python verify_marked_path.py`. It independently computes exact integer diagonal walk moments and their rational ranks for every site on all paths with \(2\le n\le18\) and potentials \(\tau\in\{-2,3/2,1,3\}\). It also verifies every coefficient of the Chebyshev reflection-difference identity for those orders. Expected summary: `VERIFY_OK symbolic_antisymmetric_minor_identities=1014 exact_moment_rank_instances=680 negative_potential_instances=170 site_cases=170 path_orders=2..18`.

The computation checks finite examples only. The unrestricted theorem follows from the four analytical steps above; no finite enumeration is used as an infinite proof.

## Relationship to prior work

Godsil [1] derived the general spectral-projector expression and computed the unperturbed path average-mixing matrix, whose rank is \(\lceil n/2\rceil\). Godsil's characteristic-minor factorization is a key ingredient here. Coutinho, Godsil, Guo and Zhan [2] further analyzed rank through commutant geometry. The exact-arithmetic treatment of quantum average mixing in [3] motivates the invariant. Kempton, Lippner and Yau [4] studied how diagonal potentials modify **state-transfer** properties on paths and symmetric graphs; their symmetric endpoint potentials do not imply the rank formula for a *single interior* marked site. The new contribution here is the closed arithmetic rank law, including its central exception, from the explicit polynomial dependency classification.

## Limitations

Only unweighted paths with **one** nonzero diagonal potential are classified. Multiple on-site marks and arbitrary edge weights are not covered, and no statement is made about instantaneous or pretty-good state transfer or mixing time. The rank discontinuity at \(\tau=0\) does not mean that average transition probabilities are discontinuous at finite times. The proof assumes the mathematical idealization of infinite-time averaging. Although published theory supplies general methods for computing the rank, a broader existing theorem on Jacobi-matrix squared eigenvectors could subsume this specialization; publication novelty merits further independent literature review.

## References

[1] C. Godsil, *Average Mixing of Continuous Quantum Walks*, arXiv:1103.2578, Sections 1, 3 and 4; https://arxiv.org/abs/1103.2578.

[2] G. Coutinho, C. Godsil, K. Guo, H. Zhan, *A New Perspective on the Average Mixing Matrix*, arXiv:1709.03591; https://arxiv.org/abs/1709.03591.

[3] G. Coutinho, P. F. Baptista, C. Godsil, T. J. Spier, R. Werner, *Irrational Quantum Walks*, arXiv:2208.08971, first posted 2022-08-18, primary MSC 81P68; https://arxiv.org/abs/2208.08971.

[4] M. Kempton, G. Lippner, S.-T. Yau, *Pretty Good State Transfer in Graphs with an Involution*, arXiv:1702.07000; https://arxiv.org/abs/1702.07000.
