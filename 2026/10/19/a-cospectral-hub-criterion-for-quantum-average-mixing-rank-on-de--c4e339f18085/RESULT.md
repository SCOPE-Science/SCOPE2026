# A cospectral-hub criterion for quantum average-mixing rank on detuned weighted double stars

## Finding

**Theorem.** Let \(p,q\ge2\) be integers. Construct a tree with adjacent hubs \(u,v\), \(p\) pendant leaves at \(u\), and \(q\) pendant leaves at \(v\). Give each left pendant edge hopping \(a>0\), each right pendant edge hopping \(b>0\), and the hub edge hopping \(w>0\). Set real onsite energies \(c\) at \(u\) and \(d\) at \(v\), with zero onsite energy on every leaf. Let \(H\) be the resulting real symmetric Hamiltonian, and let \(\widehat M\) be the infinite-time continuous-time quantum average-mixing matrix. Then

\[
\boxed{\dim\ker\widehat M=\mathbf1_{\{p=2\}}+\mathbf1_{\{q=2\}}+\mathbf1_{\{c=d\,\land\,pa^2=qb^2\}}.}
\]

The kernel is exactly the span of the left-leaf difference \(e_{L_1}-e_{L_2}\) when \(p=2\), the right-leaf difference \(e_{R_1}-e_{R_2}\) when \(q=2\), and the hub difference \(e_u-e_v\) when \(c=d\) and \(pa^2=qb^2\). In particular,

\[
\boxed{\widehat M\succ0\ \Longleftrightarrow\ p,q\ge3\ \text{and}\ (c\ne d\ \text{or}\ pa^2\ne qb^2).}
\]

The exceptional condition is independent of the positive inter-hub coupling \(w\). It can occur even when \(p\ne q\), so its hub indistinguishability need not arise from a graph automorphism. For example, \(p=4,q=9,a=3,b=2,c=d=0\) produces one hub null direction for every \(w>0\), whereas changing \(d\) to any nonzero real value removes it without changing the graph or edge couplings.

## Assumptions and scope

All graphs are finite. There are \(N=p+q+2\) labelled vertices, and every hopping strength is real and strictly positive. Onsite energies \(c,d\) may be arbitrary reals. No uniformity is assumed between \(a,b,w\). The case \(p=1\) or \(q=1\) is excluded from this statement. Define

\[
U(t)=\exp(-\mathrm i tH),\qquad \widehat M_{xy}=\lim_{T\to\infty}\frac1T\int_0^T |U(t)_{xy}|^2\,dt.
\]

For the distinct eigenvalues \(\theta\) of \(H\) and their full orthogonal projectors \(E_\theta\), elementary Fourier averaging gives \(\widehat M=\sum_\theta E_\theta\circ E_\theta\), with \(\circ\) denoting entrywise multiplication. This convention includes all spectral multiplicities and is insensitive to the sign convention in \(U(t)\).

## Proof

**1. Bright and dark decomposition.** Write \(A=a\sqrt p\), \(B=b\sqrt q\). The two normalized uniform leaf vectors, followed by the two hubs in the order left-leaf, \(u\), \(v\), right-leaf, span an invariant four-dimensional bright sector with matrix

\[
Q=\begin{pmatrix}
0&A&0&0\\ A&c&w&0\\0&w&d&B\\0&0&B&0
\end{pmatrix}.
\]

The orthogonal complement comprises left and right leaf-contrast spaces of dimensions \(p-1\) and \(q-1\), each annihilated by \(H\). The tridiagonal matrix \(Q\) has simple spectrum because all its off-diagonal entries are strictly positive (the recurrence determines an eigenvector from its first coordinate, forcing each eigenspace to have dimension at most one). Also \(\det Q=A^2B^2>0\), so none of its four eigenvalues is zero. Thus the zero projector of \(H\) is exactly the sum of the independent leaf-contrast projectors,

\[
E_0|_L=I_p-J_p/p,\quad E_0|_R=I_q-J_q/q,
\]

and all its entries touching a hub or different leaf groups are zero.

**2. Positive semidefinite separation.** As the projectors are real symmetric and positive semidefinite, every \(E_\theta\circ E_\theta\) is positive semidefinite by the Schur product theorem. Therefore the kernel of their sum is the intersection of their individual kernels. On a leaf group of size \(s\ge2\),

\[
(I_s-J_s/s)\circ(I_s-J_s/s)=(1-2/s)I_s+J_s/s^2.
\]

This matrix has eigenvalue \((s-1)/s>0\) on the constant vector and eigenvalue \(1-2/s\) on the orthogonal contrasts. Each nonzero spectral eigenvector is constant on each leaf group, hence its squared-entry profile is also constant there. Consequently the leaf contrasts contribute precisely one null direction for each group of size two, and no other contrast null directions. On the four-dimensional orbit-constant sector, the zero-projector Schur square is strictly positive on the two leaf-constant directions, leaving only the hub-coordinate plane to be tested.

**3. Central spectral profiles and cospectrality.** Let \(\psi_1,\ldots,\psi_4\) be an orthonormal real eigenbasis of \(Q\), with distinct eigenvalues \(\lambda_j\). Each nonzero-eigenvalue projector in the full graph is rank one, so its Schur square is \(z_jz_j^{\mathsf T}\), where \(z_j\) is the vector of the squared vertex coordinates of the corresponding normalized eigenvector. On vectors supported at \(u,v\), its quadratic form is

\[
\bigl(|\psi_j(u)|^2 x_u+|\psi_j(v)|^2 x_v\bigr)^2.
\]

Therefore an additional hub-supported null vector exists if and only if the two length-four nonnegative vectors \((|\psi_j(u)|^2)_j\) and \((|\psi_j(v)|^2)_j\) are linearly dependent. Each has sum one by orthonormality, so dependence is equivalent to their equality. Since the eigenvalues are distinct, that equality means the two hubs have identical spectral measures, equivalently

\[
(Q^k)_{uu}=(Q^k)_{vv}\quad\text{for every integer }k\ge0.
\]

Already \(k=1\) forces \(c=d\), and \(k=2\) forces \(A^2+w^2+c^2=B^2+w^2+d^2\), hence \(A^2=B^2\) and therefore \(pa^2=qb^2\). Conversely, when \(c=d\) and \(A=B\), the bright matrix \(Q\) is invariant under reflection interchanging the two leaf coordinates and the two hub coordinates. Its simple-spectrum eigenvectors are reflection-even or reflection-odd, so their squared hub coordinates agree for every eigenvalue. In that case \(e_u-e_v\) belongs to the kernel; otherwise the hub quadratic form has rank two and no hub null direction remains.

The leaf contrasts and hub vector have disjoint supports and are linearly independent. These observations establish the complete kernel basis, nullity formula, and positive-definiteness criterion. The argument includes equality and boundary cases \(p=2\), \(q=2\), and arbitrary negative, zero, or positive hub onsite energies.

## Verification

The accompanying standalone Python 3 checker `verify.py` requires only the standard library. Run `python3 verify.py` in the directory containing the file. It separately computes the exact rational dimension of the diagonal image of the symmetric commutant \(\{Z=Z^{\mathsf T}:ZH=HZ\}\), rather than using the bright-sector spectral proof. This dimension equals the rank of the average-mixing matrix by the spectral conditional-expectation identity. The checker also performs an independent direct spectral-projector calculation using a standard-library Jacobi diagonalizer, including the onsite-detuned and effectively balanced cases. The expected console line is recorded in `VERIFICATION.md`. These finite tests check examples but do not establish the unrestricted parameter theorem; the preceding proof does.

## Relationship to prior work

The general spectral-projector Schur-square identity and commutant formulation are antecedents in the works of Coutinho, Godsil, Guo, and Zhan (2018) and Coutinho, Baptista, Godsil, Spier, and Werner (2022/2023). Godsil, Guo, and Sinkovic (2017/2018) address tree average-mixing rank, especially the simple-spectrum case, and provide small-tree examples. A previously established unweighted double-star rank law covers only unit hoppings with no onsite detuning and is not claimed again here. The new content is the exact **simultaneous weighted-coupling and independent central-onsite** classification and its cospectral-hub criterion for arbitrarily large, possibly asymmetric leaf groups. An August 2026 study of double stars addresses the trace/laziness of **Laplacian** quantum walks; its accessible abstract is not a decisive statement comparison for the present adjacency-plus-potential rank classification. See `REVIEW.md` and `AUDIT.json` for qualified scope and remaining literature-access risk.

## Limitations

The theorem concerns Cesàro average mixing, not instantaneous state transfer, arbitrary initial mixed states, Laplacian walks, nonuniform observation-time laws, or general trees. It requires uniform hopping and zero onsite energy **within each leaf group**, strictly positive inter-hub coupling, and at least two leaves at each hub. It does not claim independent novelty certification or cover inaccessible literature beyond the inspected material. The finite checks are corroborative only.

## References

1. G. Coutinho, P. F. Baptista, C. Godsil, T. J. Spier, and R. Werner, *Irrational quantum walks*, arXiv:2208.08971v1 (first public 2022-08-18), SIAM J. Appl. Algebra Geom. 7 (2023), 567–584, DOI: 10.1137/22M1521262.
2. G. Coutinho, C. Godsil, K. Guo, and H. Zhan, *A New Perspective on the Average Mixing Matrix*, arXiv:1709.03591v1 (2017), Electron. J. Combin. 25 (2018), P4.14.
3. C. Godsil, K. Guo, and J. Sinkovic, *Average mixing matrix of trees*, arXiv:1709.07907v1 (2017), Electron. J. Linear Algebra 34 (2018).
4. A. Mohan, C. Tamon, Y. Xu, and H. Zhan, *Laziness of Quantum Walks on Graphs*, arXiv:2608.20739 (2026; abstract inspected; full text not available during review).
