# Exact kernel and sharp full-rank boundary for quantum average mixing on double-star trees

## Finding

For integers \(p,q\ge1\), the **double-star tree** \(D_{p,q}\) has adjacent hubs \(x,y\), \(p\) pendant vertices \(L_1,\ldots,L_p\) adjacent to \(x\), and \(q\) pendant vertices \(R_1,\ldots,R_q\) adjacent to \(y\). Let \(A\) be its ordinary, unweighted adjacency matrix. Its continuous-time quantum-walk average mixing matrix is
\[
\widehat M(D_{p,q})=\lim_{T\to\infty}\frac1T\int_0^T
(e^{\mathrm i tA})\circ(e^{-\mathrm i tA})\,dt,
\]
where \(\circ\) is entrywise multiplication. For every \(p,q\ge1\), its nullity is exactly
\[
\boxed{\dim\ker\widehat M(D_{p,q})=
\begin{cases}
2,&p=q=1,\\
3,&p=q=2,\\
1,&p=q\ge3,\\
\mathbf1_{\{p\le2\}}+\mathbf1_{\{q\le2\}},&p\ne q.
\end{cases}}
\]
The rank is \(p+q+2\) minus this nullity. In particular, \(\widehat M(D_{p,q})\) is positive definite **if and only if** \(p,q\ge3\) and \(p\ne q\). This is a sharp transition for a natural family of trees with arbitrarily large repeated zero-adjacency eigenspaces.

An explicit basis for the entire kernel is given by the following independent vectors, taking exactly those that satisfy the stated conditions:

- \(e_{L_1}-e_{L_2}\) when \(p=2\), and \(e_{R_1}-e_{R_2}\) when \(q=2\).
- \(e_x-e_y\) when \(p=q\).
- \(e_{L_1}-e_{R_1}\) additionally when \(p=q=1\).
- \((q-1)e_{L_1}-q e_x+e_y\) when \(p=1<q\).
- \((p-1)e_{R_1}-p e_y+e_x\) when \(q=1<p\).

Thus, for example, \(D_{2,2}\) has six vertices and rank three, while \(D_{3,4}\) has nine vertices and rank nine.

## Assumptions and scope

All graphs are finite, simple, undirected and unweighted. Evolution uses adjacency, not ordinary or normalized Laplacian dynamics. Both hub degrees are at least two; the allowed positive integers \(p,q\) count pendant leaves, not hub degrees. The claimed rank, kernel and positive-definiteness criterion hold for **every** pair \(p,q\ge1\), including equal sizes and the small boundaries. No assertion is made about other tree families, weighted couplings, noisy walks, or finite-time convergence rates.

## Proof

**1. Spectral decomposition.** Order the vertices as \((L_1,\ldots,L_p,x,y,R_1,\ldots,R_q)\). The graph is bipartite. In the bipartition with cells \((x,R_1,\ldots,R_q)\) and \((y,L_1,\ldots,L_p)\), the adjacency block has rank two. On the subspaces constant on each leaf cell, its squared singular-value matrices are
\[
T_X=\begin{pmatrix}p+1&\sqrt q\\\sqrt q&q\end{pmatrix},
\qquad
T_Y=\begin{pmatrix}q+1&\sqrt p\\\sqrt p&p\end{pmatrix}.
\]
Both have characteristic polynomial
\[
F(s)=s^2-(p+q+1)s+pq.
\]
Put
\[
\Delta=\sqrt{(p+q+1)^2-4pq}>0,\qquad
\mu_\pm=\frac{p+q+1\pm\Delta}{2}.
\]
Because \(p,q>0\), both roots are positive and distinct. The nonzero adjacency eigenvalues are exactly \(\pm\sqrt{\mu_+}\) and \(\pm\sqrt{\mu_-}\), all simple. The remaining eigenspace, at zero, consists of independently zero-sum amplitudes on the two leaf sets. Its projector \(E_0\) has leaf blocks \(Q_p=I_p-J_p/p\) and \(Q_q=I_q-J_q/q\), and zero hub rows and columns.

**2. Squared eigenvector profiles.** Let \(v_\pm\) be real unit eigenvectors of the **positive** adjacency eigenvalues \(\sqrt{\mu_\pm}\). Set \(w_\pm(u)=v_\pm(u)^2\). From the two reduced symmetric matrices and their one-dimensional spectral projectors, their squared hub amplitudes are
\[
\begin{array}{c|cc}
 & x & y\\\hline
w_+ & a_+=(\mu_+-q)/(2\Delta)&b_+=(\mu_+-p)/(2\Delta)\\
w_- & a_-=(q-\mu_-)/(2\Delta)&b_-=(p-\mu_-)/(2\Delta).
\end{array}
\]
The leaf eigenvalue equations imply
\[
w_\pm(L_i)=a_\pm/\mu_\pm,
\qquad w_\pm(R_j)=b_\pm/\mu_\pm.
\]
In particular, all four hub weights are strictly positive. Bipartite sign switching maps an eigenvector at positive energy to one at the corresponding negative energy without changing its squared coordinates. The spectral-projector identity for average mixing therefore gives the **exact full matrix decomposition**
\[
\boxed{\widehat M=E_0\circ E_0+
2w_+w_+^{\mathsf T}+2w_-w_-^{\mathsf T}.}
\]
No distinct eigenvalues have been combined in this step; all nonzero eigenvalues are simple and the zero space is treated as one eigenspace.

**3. Rank of the zero sector.** For every integer \(s\ge1\),
\[
Q_s\circ Q_s=(1-2/s)I_s+J_s/s^2.
\]
Its eigenvalue on the constant vector is \((s-1)/s\), and its eigenvalue on the orthogonal complement is \((s-2)/s\). Hence its rank is \(f(1)=0\), \(f(2)=1\), and \(f(s)=s\) for \(s\ge3\). The two leaf sectors of \(E_0\circ E_0\) are orthogonal, so their combined rank is \(f(p)+f(q)\). Whenever a leaf sector is nonzero, its range contains its constant vector.

**4. Rank of the two nonzero modes.** Since all three summands in the boxed decomposition are positive semidefinite, the rank of their sum equals the dimension of the sum of their ranges. After quotienting out the two nonzero leaf-sector ranges, the two profile vectors project onto their two hub coordinates whenever \(p,q\ge2\). Their hub matrix has determinant
\[
\det\begin{pmatrix}a_+&b_+\\a_-&b_-\end{pmatrix}
=\frac{p-q}{4\Delta}.
\]
Thus this quotient has rank two if \(p\ne q\) and rank one if \(p=q\ge2\). If exactly one of \(p,q\) equals one, the quotient retains that singleton leaf as well as both hubs; its rank is still two, because the same nonzero hub determinant gives a two-dimensional minor. If \(p=q=1\), there is no zero sector, and the two vectors \(w_+,w_-\) are independent: they both sum to one, but their squared hub weights differ (indeed \(a_+-a_-=1/(2\Delta)\) in this case). Consequently,
\[
\operatorname{rank}\widehat M=
\begin{cases}
f(p)+f(q)+2,&p\ne q,\\
f(p)+f(q)+1,&p=q\ge2,\\
2,&p=q=1.
\end{cases}
\]
Subtracting from \(p+q+2\) proves the asserted nullity formula and positive-definiteness criterion.

**5. Complete kernel basis.** A vector lies in the kernel of the positive-semidefinite matrix above if and only if it is orthogonal to both profiles \(w_\pm\) and lies in the kernel of each \(Q_s\circ Q_s\) block. When \(s\ge3\), this forces all coordinates on that leaf set to vanish; when \(s=2\), it permits only the leaf-pair difference; when \(s=1\), it imposes no condition. For \(p=q\), \(a_\pm=b_\pm\), so the hub difference lies in the kernel. With \(p=1<q\), the explicit additional vector is orthogonal to each \(w_\pm\) because
\[
(q-1)\frac{a_\pm}{\mu_\pm}-q a_\pm+b_\pm=0,
\]
which follows upon inserting the hub formulas and \(F(\mu_\pm)=0\) for \(p=1\). The other singleton boundary follows by swapping the sides. When \(p=q=1\), reflection interchanges both pairs of corresponding vertices, giving both listed differences. These vectors are linearly independent, satisfy the full kernel conditions, and their numbers equal the computed nullities. They therefore form complete bases.

## Verification

The standalone `verify.py` independently constructs each double-star adjacency matrix and its spectral projectors. It compares the analytic matrix with direct numerical diagonalization for all \(1\le p,q\le12\), tests the complete kernel basis and ranks, and compares exact projector identities at four boundary examples. Run `python verify.py` with Python 3, NumPy and SymPy installed. A successful execution prints a line beginning `VERIFY_OK`; its exact counts and maximum numerical residual are recorded in `VERIFICATION.md`. Numerical enumeration is supportive evidence only; Steps 1–5 prove the theorem for all permitted positive integers.

## Relationship to prior work

The Schur-square spectral-projector formula and its connection with commutants are established in Coutinho, Godsil, Guo and Zhan [1]. Fan and Godsil [2] develop the adjacency quantum walk on precisely the double-star family and classify forms of state transfer; their state-transfer conditions are not statements about average-mixing rank. The 2022 work of Coutinho and collaborators [3] develops exact computation of average mixing for integral adjacency Hamiltonians; it does not provide the present two-parameter double-star rank and kernel formula. Godsil's quantum-walk lecture notes [4] explain both double-star transfer and the fact that a difference of two strongly cospectral vertices belongs to the average-mixing kernel. The singleton-leaf nullvectors above can instead involve **three** vertices, and the theorem characterizes all kernel directions, not only those arising from strongly cospectral pairs. Mohan and collaborators [5] study double-star laziness for Laplacian quantum walks; their stated observable is the trace for a different Hamiltonian, which does not give the present adjacency-kernel result.

## Limitations

The structural classification is proved only for unweighted adjacency evolution on double stars. It does not quantify eigenvalue condition numbers, finite-time convergence or robust stability under graph perturbations. Finite numerical checks are not an infinite proof. The literature comparison cannot exclude unpublished results, differently indexed equivalent theorems, or an adjacency-side statement hidden in a source whose complete text was not available. The result is not an independent certification.

## References

[1] G. Coutinho, C. Godsil, K. Guo and H. Zhan, *A New Perspective on the Average Mixing Matrix*, Electronic Journal of Combinatorics 25(4), #P4.14 (2018), arXiv:1709.03591, DOI:10.37236/7867.

[2] X. Fan and C. Godsil, *Pretty Good State Transfer on Double Stars*, arXiv:1206.0082 (first posted 2012).

[3] G. Coutinho, P. F. Baptista, C. Godsil, T. J. Spier and R. Werner, *Irrational Quantum Walks*, arXiv:2208.08971 (first posted 2022-08-18), SIAM Journal on Applied Algebra and Geometry 7 (2023), DOI:10.1137/22M1521262; primary MSC 81P68.

[4] C. Godsil, *Graph Spectra and Quantum Walks*, lecture notes, sections 11.5 and 13.5, https://homepages.dcc.ufmg.br/~gabriel/assets/files/coutinho-grafspec.pdf.

[5] A. Mohan, C. Tamon, Y. Xu and H. Zhan, *Laziness of Quantum Walks on Graphs*, arXiv:2608.20739 (2026), abstract referring to Laplacian quantum walks and double stars.
