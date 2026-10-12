# Single-projector positivity for quantum average mixing on odd graphs

## Finding
For every integer \(k\ge1\), let \(G_k=KG(2k+1,k)\) have as vertices the \(k\)-subsets of a \((2k+1)\)-element set, with edges joining disjoint subsets. Let \(A_k\) be its ordinary, unweighted adjacency matrix. Let \(E\) be the orthogonal spectral projector onto the eigenvalue \((-1)^k\) of \(A_k\). Then **the single Schur square \(E\circ E\) is strictly positive definite**. Therefore the continuous-time quantum-walk average mixing matrix
\[
\widehat M_k=\lim_{T\to\infty}\frac1T\int_0^T e^{itA_k}\circ e^{-itA_k}\,dt
\]
is positive definite and
\[
\operatorname{rank}\widehat M_k=\binom{2k+1}{k}.
\]
Here the exponential, entrywise product, and integral are defined on the full \(\binom{2k+1}{k}\)-dimensional real vertex space. This gives a complete infinite-family full-rank statement, not a formula for every eigenvalue. The special cases of small \(k\) are not asserted to be individually novel; the contribution is the arbitrary-size single-projector theorem and its uniform transversal proof.

## Assumptions and scope
Fix an integer \(k\ge1\). Write \(\Omega=\{a_1,b_1,\ldots,a_k,b_k,c\}\), and \(\mathcal X=\binom{\Omega}{k}\). For \(u\in\Omega\), set \(x_u(X)=1\) when \(u\in X\), and \(x_u(X)=0\) otherwise. Let \(S_{2k+1}\) act by relabelling \(\Omega\). Every inner product is the ordinary counting inner product on \(\mathbb R^{\mathcal X}\). Throughout, a spectral projector is the **orthogonal projector onto an entire eigenspace**, not a rank-one projector for a chosen eigenvector. No normalization beyond the usual \(0\)-\(1\) adjacency matrix is used.

## Proof
**1. A signed transversal adjacency eigenvector.** Define
\[
\psi(X)=\prod_{i=1}^k\big(x_{a_i}(X)-x_{b_i}(X)\big).
\]
Its support comprises the \(2^k\) sets selecting exactly one member of each displayed pair (and never \(c\)); on this support \(\psi(X)\in\{-1,1\}\). Directly, \(A_k\psi=(-1)^k\psi\): if \(X\) is such a transversal, its only disjoint transversal is the complementary choice, with sign \((-1)^k\psi(X)\). If \(X\) contains both members of any pair, no transversal is disjoint from \(X\), so the adjacency sum is zero. The only remaining nontransversal \(k\)-sets contain \(c\) and exactly one element from each of \(k-1\) pairs; the two disjoint transversals differ solely in the omitted pair and their signs cancel. Thus \(\psi\) belongs to the \((-1)^k\)-eigenspace \(W\), as do all relabellings \(g\psi\).

**2. A multiplicity-free orthogonal decomposition without character tables.** For \(0\le j\le k\), let \(U_j\) be spanned by functions \(x_T(X)=\mathbf1_{T\subseteq X}\) over all \(j\)-subsets \(T\subseteq\Omega\); set \(U_{-1}=\{0\}\). These spaces are nested, because \(x_T=\frac1{k-j}\sum_{u\notin T}x_{T\cup\{u\}}\) for \(|T|=j<k\). Also \(U_k=\mathbb R^{\mathcal X}\), as each \(x_X\) is a coordinate basis vector. Put \(V_j=U_j\cap U_{j-1}^{\perp}\). They give an orthogonal, \(S_{2k+1}\)-invariant decomposition \(\mathbb R^{\mathcal X}=\bigoplus_{j=0}^kV_j\).

All these pieces are nonzero. Indeed, take \(j\) disjoint **pairs of distinct elements**, and let \(h\) be the product of the corresponding \(j\) indicator differences. Expansion shows \(h\in U_j\). For every \(T\) of size at most \(j-1\), one pair avoids \(T\); swapping its two elements fixes \(x_T\) but reverses \(h\). Thus \(\langle h,x_T\rangle=0\), so \(h\in V_j\). Since \(j\le k\) one can select a \(k\)-set on which \(h\ne0\). The case \(j=0\) uses the constant function.

A matrix commuting with every coordinate permutation induced by \(S_{2k+1}\) has entries depending only on \(|X\cap Y|\), which assumes exactly \(k+1\) values; hence this commutant has dimension \(k+1\). The nonzero mutually orthogonal projections onto \(V_0,\ldots,V_k\) already give \(k+1\) independent commuting matrices and hence span the commutant. In particular each \(V_j\) is irreducible over \(\mathbb R\): a proper nonzero invariant summand would yield an additional orthogonal commuting projector not in the span of these projections. Further, no two \(V_j\) are equivalent, since an intertwiner between them would supply an independent off-diagonal commuting matrix. Therefore every invariant subspace is a direct sum of some of these inequivalent \(V_j\).

**3. Every piece occurs in the orbit of \(\psi^2\).** For \(j=0\), take \(h_0=1\). For \(j=1\), take \(h_1=x_{a_1}-x_c\). For an **even** \(j\ge2\), put \(m=j\) and define
\[
h_j(X)=\prod_{i=1}^{m}\big(x_{a_i}(X)-x_{b_{i+1}}(X)\big),\qquad b_{m+1}=b_1.
\]
For an **odd** \(j\ge3\), put \(m=j-1\), use the same \(m\)-fold cyclic product, and multiply it by \(x_{a_j}(X)-x_c(X)\). In each construction the factors use disjoint pairs of ground-set elements. Hence by step 2, \(h_j\in V_j\).

Under the uniform distribution on the support of \(\psi^2\), the choices \(a_i\) versus \(b_i\) are independent fair signs \(R_i\in\{-1,1\}\), with \(x_{a_i}=(1+R_i)/2\), \(x_{b_i}=(1-R_i)/2\), and \(x_c=0\). A cyclic factor becomes \((R_i+R_{i+1})/2\). For **even** \(m\), the expectation of the \(m\)-fold cyclic product is exactly \(2^{1-m}\): in its expansion exactly two choices pair all signs to even powers, and every other term has expectation zero. In the odd-\(j\) construction the final factor has independent mean \(1/2\). Consequently, for \(0\le j\le k\),
\[
\langle\psi^2,h_j\rangle=\begin{cases}2^k,&j=0,\\2^{k-1},&j=1,\\2^{k+1-j},&2\le j\le k.\end{cases}
\]
All these numbers are strictly positive. Thus \(\psi^2\) has nonzero orthogonal projection into **every** \(V_j\). Since the representation is multiplicity-free, its \(S_{2k+1}\)-orbit spans all of \(\mathbb R^{\mathcal X}\). In particular the set of Schur products \(\{u\circ v:u,v\in W\}\) spans the full vertex space: it contains every translated square \((g\psi)^2\).

**4. The projector Schur square has no kernel.** Choose a real orthonormal basis \(u_1,\ldots,u_d\) of \(W\). Its orthogonal projector satisfies
\[
E=\sum_{p=1}^{d}u_pu_p^{\mathsf T},\qquad E\circ E=\sum_{p,q=1}^{d}(u_p\circ u_q)(u_p\circ u_q)^{\mathsf T}.
\]
The sum is positive semidefinite and its range is the span of all \(u_p\circ u_q\), which by step 3 is the entire vertex space. Therefore \(E\circ E\succ0\). For the other, distinct adjacency eigenvalues \(\lambda\), their projectors \(E_\lambda\) also satisfy \(E_\lambda\circ E_\lambda\succeq0\), by the same basis-square identity. Time averaging cancels unequal spectral frequencies and gives \(\widehat M_k=\sum_\lambda E_\lambda\circ E_\lambda\succeq E\circ E\succ0\). The rank equals the number of vertices, as asserted.

## Verification
The included standalone `verify.py` uses only Python's standard library. Running `python3 verify.py` checks, by exact integer arithmetic, the signed-transversal adjacency eigenvector identities for \(1\le k\le6\), the stated nonzero moments for all \(0\le j\le k\), and the lower-degree orthogonality of each test function for \(1\le k\le4\). It is a finite consistency check of key nonstandard steps, **not** an exhaustive proof for arbitrarily large \(k\). The unrestricted proof is in the preceding sections.

## Relationship to prior work
Coutinho, Godsil, Guo, and Zhan established the basic Schur-square formula and studied rank via commutants [1]. Coutinho and Guo explicitly posed full rank for primitive distance-regular graphs as Open Problem 4.1 in their 2024 survey [2]. The odd graph family forms a natural, nonbipartite distance-regular subfamily; the theorem addresses this subfamily rather than the general problem. Coutinho et al. provide methods for computing exact average mixing on integral-Hamiltonian graphs [3], but those algorithms alone do not provide the present dimension-uniform strict-positivity proof.

The classical Johnson association scheme gives exact idempotents and Krein parameters, and the full-rank assertion can equivalently be expressed as positivity of all coefficients in one top-idempotent Schur square. This standard algebraic setup is credited, not claimed as new. A previously established result for the Johnson triple graphs \(J(n,3)\) covers, in particular, the \(k=3\), \(n=7\) instance and its top projector. The contribution here is a proof valid for **all \(k\)**, especially unbounded \(k\ge4\), using explicit signed transversals rather than fixed-degree case analysis.

## Limitations
The theorem is for **ordinary, unweighted adjacency** quantum walks on \(KG(2k+1,k)\), not all Kneser graphs or all distance-regular graphs. It does not compute the smallest positive eigenvalue of \(\widehat M_k\) or of \(E\circ E\), nor does it establish finite-time mixing rates. The proof is exact but has not undergone independent validation. Classical Krein-parameter identities may yield another route to this conclusion, and an unlocated equivalent publication remains an originality risk.

## References
[1] G. Coutinho, C. Godsil, K. Guo, and H. Zhan, *A New Perspective on the Average Mixing Matrix*, arXiv:1709.03591v1 (2017), especially Sections 1, 4, and 5. https://arxiv.org/html/1709.03591v1

[2] G. Coutinho and K. Guo, *Selected Open Problems in Continuous-Time Quantum Walks*, arXiv:2404.02236v1 (2024), Section 4, Open Problem 4.1. https://arxiv.org/html/2404.02236v1

[3] G. Coutinho, P. Ferreira Baptista, C. Godsil, T. J. Spier, and R. Werner, *Irrational quantum walks*, arXiv:2208.08971v1 (first public submission 2022-08-18), Section 2. https://arxiv.org/html/2208.08971v1

[4] C. Godsil, *Association Schemes*, lecture notes, Section 2.4 (Krein-parameter framework), https://www.math.uwaterloo.ca/~cgodsil/pdfs/assoc2.pdf
