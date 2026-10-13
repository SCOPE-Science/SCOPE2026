# Exact kernel of quantum average mixing on Kulli path windmills

## Finding

**Theorem.** Let \(m\geq 2\) and \(b\geq 3\) be integers. Form the graph
\(W_{b,m}=K_1\vee(bP_m)\), where \(P_m\) is the path on \(m\) vertices,
\(bP_m\) is the disjoint union of \(b\) copies, and the unique new vertex is
adjacent to **every** vertex of every copy. Give its edges weight one. Let
\(A\) be its real symmetric adjacency matrix and
\[
\widehat M=\lim_{T\to\infty}\frac1T\int_0^T
  \bigl(e^{itA}\circ e^{-itA}\bigr)\,dt.
\]
Write \(z=(z_0,z_{\ell,k})\), with center coordinate \(0\), blade
\(1\leq\ell\leq b\), and path position \(1\leq k\leq m\). Then
\[
\boxed{\ker\widehat M=\left\{z:\ z_0=0,\quad
 z_{\ell,k}=-z_{\ell,m+1-k}\quad\text{for all }\ell,k\right\}.}
\]
In particular,
\[
\boxed{\operatorname{rank}\widehat M=1+b\left\lceil\frac m2\right\rceil,
\qquad \dim\ker\widehat M=b\left\lfloor\frac m2\right\rfloor.}
\]
This proves the at-least-three-blade rank prediction for Kulli path
windmills in Kimmerling's 2023 Conjecture 5.1.5 and supplies its exact
nullspace. For example, the ten-vertex graph \(W_{3,3}\) has rank seven.

## Assumptions and scope

The assertion concerns *unweighted adjacency-Hamiltonian*, continuous-time
quantum walks and the infinite-time Cesàro average. All graph vertices are
distinct, no loops are present, and \(b\geq3\) is essential to the proof.
The assertion does not classify \(b=1\) or \(b=2\), instantaneous mixing,
or the nonzero eigenvalues of \(\widehat M\). A **Dutch** windmill of paths
identifies a path endpoint with a common vertex and is a different graph for
\(m>2\); here the center joins every path vertex.

## Proof

**1. The exact kernel criterion.** For the distinct adjacency eigenvalues
\(\lambda\), let \(E_\lambda\) denote the real orthogonal spectral
projectors. The standard time-average identity (References 1 and 2) is
\(\widehat M=\sum_\lambda E_\lambda\circ E_\lambda\). For a real vector
\(z\), put \(D_z=\operatorname{diag}(z)\). Orthogonality and idempotence give
\[
 z^T\widehat Mz=\sum_\lambda
   \operatorname{tr}\!\bigl((E_\lambda D_zE_\lambda)^2\bigr)
 =\sum_\lambda\|E_\lambda D_zE_\lambda\|_F^2.
\]
Hence \(z\in\ker\widehat M\) if and only if
\(E_\lambda D_zE_\lambda=0\) for every distinct \(\lambda\).
This is an exact statement for signed \(z\) and includes all repeated
eigenspaces.

**2. Path modes and spectral separation.** Set \(L=m+1\). The path adjacency
matrix \(B\) has simple eigenvalues and normalized eigenvectors
\[
 \alpha_j=2\cos\frac{j\pi}{L},\qquad
 \phi_j(k)=\sqrt{\frac2L}\sin\frac{jk\pi}{L},\qquad 1\leq j\leq m.
\]
Under reflection of positions \(k\mapsto L-k\), \(\phi_j\) has parity
\((-1)^{j+1}\). Consequently
\(\langle\mathbf1,\phi_j\rangle=0\) precisely for even \(j\);
for odd \(j\) it is nonzero (the sine-sum formula proves this).
The adjacency block matrix is
\[
 A=\begin{pmatrix}
 0&\mathbf1_b^T\otimes\mathbf1_m^T\\
 \mathbf1_b\otimes\mathbf1_m&I_b\otimes B
 \end{pmatrix}.
\]
For even \(j\), the \(\alpha_j\)-eigenspace contains exactly the
\(b\)-dimensional space \(\mathbb R^b\otimes\phi_j\) with zero center.
For odd \(j\), it contains exactly the \((b-1)\)-dimensional space
\(\mathbf1_b^\perp\otimes\phi_j\) with zero center. To justify **exactly**,
we exclude collisions with the remaining coupled block as follows.

That block is the center joined to the blade-symmetric, path-symmetric
subspace spanned by the odd \(\phi_j\). In the odd-path eigenbasis it is a
real symmetric arrowhead matrix with diagonal entries \(\alpha_j\) and
nonzero couplings \(\sqrt b\langle\mathbf1_m,\phi_j\rangle\). Its eigenvalues
are simple, distinct from every odd \(\alpha_j\), and its eigenvectors
all have nonzero center coordinate: these facts follow directly by solving
the eigenvector equations at an arrowhead pole and by strict monotonicity of
the secular equation between successive poles.

Could an even \(\alpha_j\) be an eigenvalue of that block? Take even
\(j\), set \(\theta=j\pi/L\), \(\lambda=2\cos\theta\), and define
\[
 w_k=\frac{1-\cos(k\theta)}{\lambda-2},\qquad 1\leq k\leq m,
 \qquad w_0=w_L=0.
\]
Since \(j\) is even, the boundary conditions hold. The cosine recurrence
shows \((\lambda I-B)w=\mathbf1_m\) on the symmetric path subspace,
and the nontrivial root-of-unity sum yields
\[
 \mathbf1_m^Tw=\frac{L}{\lambda-2}.
\]
If a coupled eigenvector at \(\lambda\) had center coordinate \(c\ne0\),
its symmetric path profile in each blade would be \(cw\), and the center
equation would force
\(\lambda(\lambda-2)=bL\). But \(-2<\lambda<2\) implies
\(\lambda(\lambda-2)<8\), whereas \(bL\geq9\). Thus no collision occurs.
This establishes a complete, pairwise spectrally separated decomposition:
the listed repeated path eigenspaces and \(1+\lceil m/2\rceil\) simple
coupled eigenspaces account for all \(1+bm\) dimensions.

**3. All blade coordinates in a kernel vector are antisymmetric.** Suppose
\(z\in\ker\widehat M\). For each \(j\) and blade \(\ell\), put
\[
 s_{\ell,j}=\sum_{k=1}^m z_{\ell,k}\phi_j(k)^2.
\]
Compressing \(D_z\) to the even-\(j\) eigenspace yields
\(s_{\ell,j}=0\) for every blade. For odd \(j\), compression to
\(\mathbf1_b^\perp\otimes\phi_j\) says that the diagonal form
\(\operatorname{diag}(s_{1,j},\ldots,s_{b,j})\) vanishes on
\(\mathbf1_b^\perp\). Testing \(e_r-e_s\) gives
\(s_{r,j}+s_{s,j}=0\) for every distinct \(r,s\). Since \(b\geq3\), all
\(s_{\ell,j}=0\). Thus, for every blade separately,
\[
 \sum_{k=1}^m z_{\ell,k}
  \sin^2\!\left(\frac{jk\pi}{L}\right)=0
  \quad\text{for all }1\leq j\leq m.
\]
These conditions force precisely antisymmetry under \(k\mapsto L-k\).
Indeed, let \(a_k=(z_{\ell,k}+z_{\ell,L-k})/2\) for
\(1\leq k\leq m\) and \(a_0=0\). Write \(S=\sum_{k=1}^m a_k\).
The sine-square identity implies the discrete Fourier coefficients
\(\widehat a(j)=\sum_{k=0}^{L-1}a_ke^{2\pi ijk/L}\) all equal \(S\)
for \(j=1,\ldots,L-1\); by definition \(\widehat a(0)=S\) as well.
Fourier inversion gives \(a_0=S\) and \(a_k=0\) for \(k\ne0\).
Since \(a_0=0\), all \(a_k=0\), proving the required antisymmetry.

**4. The center coordinate and the converse.** Take any normalized
simple coupled eigenvector \(v\). Its center coordinate \(v_0\) is
nonzero, and its entries in every blade are reflection-symmetric.
The condition \(v^TD_zv=0\), together with the antisymmetry just proved,
gives \(v_0^2 z_0=0\), so \(z_0=0\).

Conversely, let \(z_0=0\) and let each blade of \(z\) be reflection-
antisymmetric. Products of two vectors in any single repeated path
eigenspace have within-blade profile proportional to \(\phi_j(k)^2\),
which is reflection-symmetric; their \(D_z\)-matrix elements vanish.
Each simple coupled eigenvector has reflection-symmetric blade profiles,
so its diagonal \(D_z\)-expectation also vanishes. Because the preceding
spectral separation leaves no mixed-parity eigenvalue collisions, we have
\(E_\lambda D_zE_\lambda=0\) for every \(\lambda\). The kernel criterion
then proves the displayed kernel equality. Each blade contributes
\(\lfloor m/2\rfloor\) independent antisymmetric coordinates, finishing
the rank calculation. \(\square\)

## Verification

Run `python3 verify_windmill.py` with NumPy installed. The script constructs
independent adjacency matrices, groups their computed equal eigenvalues,
forms all spectral projectors, and tests the resulting Schur-square average
mixing matrices. It checks 40 graph cases with \(2\leq m\leq11\) and
\(3\leq b\leq6\), 10 independent path-profile rank tests, and 30 explicit
even-mode resolvent identities. It checks all identified antisymmetric
kernel directions numerically and verifies the concrete case
\(\operatorname{rank}\widehat M(W_{3,3})=7\). The unrestricted mathematical
assertion is proved above, not inferred from these finite tests.

## Relationship to prior work

The spectral-projector and commutant/Gram descriptions of average mixing
were established by Godsil and by Coutinho, Godsil, Guo and Zhan
(References 1 and 2). The exact-arithmetic quantum-walk framework of
Coutinho and collaborators (Reference 3) is relevant but does not give the
Kulli path rank formula. Kimmerling's dissertation (Reference 4,
Section 5.1.3 and Conjecture 5.1.5) reports finite Kulli path windmill
rank data and explicitly leaves the \(b\geq3\) pattern conjectural.
It separately proves results for Dutch and French windmills and Kulli
cycle windmills; those families should not be conflated. The present proof
establishes the previously conjectured infinite-family rank law and the
stronger exact antisymmetric kernel description.

## Limitations

The statement is specific to adjacency quantum walks on
\(K_1\vee(bP_m)\) with \(b\geq3\). It does not settle the two-blade or
one-blade Kulli path cases, nor does it determine the positive eigenvalues
or convergence rates of the finite-time average. The dissertation's
repository-hosted full PDF was not available for complete retrieval during
the literature comparison; the publicly indexed Section 5.1.3 passage and
table were accessible. Thus there remains a literature-access risk of an
unseen theorem or a later proof under different terminology. The rank law
for \(m=2\) is a known windmill boundary case and is included for a uniform
domain statement, not claimed independently as new.

## References

1. C. Godsil, *Average Mixing of Continuous Quantum Walks*, Journal of
   Combinatorial Theory A 120 (2013), 1649–1662,
   https://doi.org/10.1016/j.jcta.2013.05.006.
2. G. Coutinho, C. Godsil, K. Guo, H. Zhan, *A New Perspective on the
   Average Mixing Matrix*, Electronic Journal of Combinatorics 25 (2018),
   P4.14, https://doi.org/10.37236/7867.
3. G. Coutinho, P. F. Baptista, C. Godsil, T. J. Spier, R. Werner,
   *Irrational Quantum Walks*, arXiv:2208.08971 (first version public
   2022-08-18), https://arxiv.org/abs/2208.08971;
   https://doi.org/10.1137/22M1521262.
4. P. R. Kimmerling, *Continuous-Time Quantum Walks on Windmill Graphs*,
   PhD dissertation, Washington State University (2023),
   Section 5.1.3 and Conjecture 5.1.5,
   https://doi.org/10.7273/000006322.
