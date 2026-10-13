# Idempotent derivations of Heisenberg Lie algebras: all-characteristic orbits and finite-field rank spectra

## Finding
Let \(K\) be any field and let \(m\ge 1\). Write the \((2m+1)\)-dimensional Heisenberg Lie algebra as \(H_m(K)=V\oplus Kz\), where \(\dim_KV=2m\), \(\omega\) is a fixed nondegenerate alternating form, and \([v+az,w+bz]=\omega(v,w)z\). An idempotent derivation means a \(K\)-linear Lie derivation \(D\) with \(D^2=D\), where the square is composition.

Every such \(D\) has a unique expression
\[
D(v+az)=Av+(\phi(v)+ac)z,
\]
where \(A\in\operatorname{End}_K(V)\), \(\phi\in V^*\), and \(c\in\{0,1\}\) satisfy
\[
A^2=A,\qquad \omega(Av,w)+\omega(v,Aw)=c\,\omega(v,w),\qquad \phi A+c\phi=\phi.
\]
There are precisely **two** conjugacy classes under \(\operatorname{Aut}_K(H_m(K))\) when \(\operatorname{char}K\ne2\): the zero derivation and the derivation \(D(p_i)=p_i\), \(D(q_i)=0\), \(D(z)=z\) on a symplectic basis. In characteristic \(2\), there are precisely \(m+2\) classes: for every \(0\le r\le m\), a central-annihilating derivation fixing the first \(r\) symplectic pairs and killing all other basis vectors, together with the preceding center-fixing derivation. The ranks of those representatives are \(2r\) and \(m+1\), respectively.

For a finite field \(K=\mathbb F_q\), define
\[
s_j(q)=q^{j^2}\prod_{i=1}^{j}(q^{2i}-1),\quad s_0(q)=1,
\qquad C_m(q)=q^{m+m(m+1)/2}\prod_{i=1}^{m}(q^i+1).
\]
The coefficient of \(X^k\) in \(P_{m,q}(X)\) counts all labeled idempotent derivations of linear rank \(k\). The **complete rank polynomial** is
\[
\boxed{P_{m,q}(X)=\begin{cases}
1+C_m(q)X^{m+1},&q\text{ odd},\\
\displaystyle\sum_{r=0}^{m}\frac{s_m(q)}{s_r(q)s_{m-r}(q)}q^{2r}X^{2r}+C_m(q)X^{m+1},&q\text{ even}.
\end{cases}}
\]
Equal powers of \(X\) are added, so that the two characteristic-two contributions are correctly combined if \(2r=m+1\). All statements include characteristic \(2\), and no hypothesis of algebraic closedness is used.

## Assumptions and scope
A symplectic basis is \((p_1,\ldots,p_m,q_1,\ldots,q_m)\) with \(\omega(p_i,q_j)=\delta_{ij}\), all same-type pairings zero. The rank is the rank of \(D\) acting on the full \((2m+1)\)-space. The classification concerns derivations whose **linear operators** are idempotent, not Lie endomorphisms or idempotent elements of a Lie algebra. All conjugacy statements are under actual \(K\)-linear Lie automorphisms, not only under scalar extension.

## Proof
**1. Reduction to a conformal-symplectic projection.** Since \(z=[H_m,H_m]\) spans the center, a derivation has \(D(z)=cz\) and \(D(v)=Av+\phi(v)z\). Comparing the Leibniz identity on \(v,w\in V\) yields exactly
\(\omega(Av,w)+\omega(v,Aw)=c\omega(v,w)\); conversely this equation is sufficient on all pairs. Squaring the block-triangular matrix \(\begin{psmallmatrix}A&0\\\phi&c\end{psmallmatrix}\) proves that idempotence is equivalent to \(A^2=A\), \(c^2=c\), and \(\phi A+c\phi=\phi\). A field has only the scalar idempotents \(0,1\).

**2. The \(c=0\) branch.** Define the adjoint \(A^\dagger\) by \(\omega(Av,w)=\omega(v,A^\dagger w)\). The derivation identity becomes \(A^\dagger=-A\). Since taking adjoints preserves idempotence, \((-A)^2=-A\), and \(A^2=A\) also, so \(2A=0\). If \(\operatorname{char}K\ne2\), this forces \(A=0\); then \(\phi A=\phi\) forces \(\phi=0\), giving just zero. If \(\operatorname{char}K=2\), \(A^\dagger=A\). The eigenspace splitting \(V=\operatorname{im}A\oplus\ker A\) is orthogonal: for \(x=Au\) and \(y\in\ker A\), \(\omega(x,y)=\omega(u,Ay)=0\). Both direct summands are therefore nondegenerate alternating spaces, so \(\dim\operatorname{im}A=2r\) for exactly one \(0\le r\le m\). Conversely, orthogonal projection onto any nondegenerate \(2r\)-subspace is a self-adjoint idempotent, and these are all possibilities. The condition \(\phi A=\phi\) says precisely that \(\phi\) vanishes on \(\ker A\); there are \(q^{2r}\) such functionals over \(\mathbb F_q\). The image of \(D\) is the graph \(\{x+\phi(x)z:x\in\operatorname{im}A\}\), hence \(\operatorname{rank}D=2r\).

**3. The \(c=1\) branch.** Here \(A^\dagger=I-A\). If \(x,y\in\operatorname{im}A\), the derivation identity reads \(2\omega(x,y)=\omega(x,y)\), whence \(\omega(x,y)=0\) over *every* field. If \(x,y\in\ker A\), it reads \(0=\omega(x,y)\). Thus \(\operatorname{im}A\) and \(\ker A\) are transverse isotropic subspaces, necessarily both Lagrangian and of dimension \(m\). Conversely the projection along either member of an ordered pair of transverse Lagrangians obeys the derivation equation with multiplier \(1\). Now \(\phi A=0\), so \(\phi\) vanishes on \(\operatorname{im}A\), providing \(q^m\) choices, and \(D(z)=z\) ensures \(\operatorname{rank}D=m+1\).

**4. Orbits.** A central shear \(S_\psi(v)=v+\psi(v)z\), \(S_\psi(z)=z\) is a Lie automorphism for every \(\psi\in V^*\). Conjugation transforms \(\phi\) into \(\phi+\psi A-c\psi\). For \(c=0\), choose \(\psi=-\phi\); for \(c=1\), choose \(\psi=\phi\). In both cases the linear functional is eliminated. Symplectic changes of basis act transitively on nondegenerate symplectic subspaces of fixed dimension, and transitively on ordered pairs of transverse Lagrangians. The normal forms stated above follow. Distinct \(c\) cannot be conjugate since an automorphism maps \(z\) to a nonzero scalar multiple of itself, and distinct \(r\) in the \(c=0\) branch have distinct ranks.

**5. Finite-field enumeration.** The symplectic group has order \(s_j(q)\). Its action on nondegenerate \(2r\)-subspaces of \(V\) is transitive, with stabilizer \(\operatorname{Sp}_{2r}(q)\times\operatorname{Sp}_{2m-2r}(q)\), because the orthogonal complement is forced. Therefore the number of such subspaces is \(s_m(q)/(s_r(q)s_{m-r}(q))\). The number of Lagrangians in a \(2m\)-dimensional symplectic space is \(\prod_{i=1}^m(q^i+1)\): double-counting pairs consisting of a Lagrangian and one of its lines gives the recurrence \(L_m=(q^m+1)L_{m-1}\). For a fixed Lagrangian, all transverse Lagrangian complements are graphs of symmetric linear maps relative to any fixed complement. Their number is \(q^{m(m+1)/2}\), including in characteristic \(2\). Multiply the respective projection counts by the already established \(q^{2r}\) and \(q^m\) choices for \(\phi\). Uniqueness of \((A,\phi,c)\) prevents double counting. This yields the displayed polynomial and completes the proof.

## Verification
The standalone Python 3 file `verify.py` enumerates all matrices \(A\), central scalars \(c\), and functionals \(\phi\) for \((m,q)=(1,2),(1,3),(1,4),(2,2)\), constructs the full derivation matrices, independently checks the Leibniz identity and idempotence, computes their ranks, and compares the frequencies with the closed formula. It uses an explicit irreducible-polynomial implementation of \(\mathbb F_4\), and no third-party libraries. Its output includes `VERIFY_OK`. An additional direct automorphism-conjugacy enumeration for \((m,q)=(1,2),(1,3)\) yields orbit sizes \((1,12,4)\) and \((1,36)\), respectively, and prints `ORBIT_OK`.

For illustration, \(P_{1,2}(X)=1+16X^2\), \(P_{1,3}(X)=1+36X^2\), \(P_{1,4}(X)=1+96X^2\), and \(P_{2,2}(X)=1+80X^2+480X^3+16X^4\). The computations are finite checks and are not the proof of the all-field or all-rank assertions.

## Relationship to prior work
Ochoa Arango and Rojas (arXiv:1811.09948v1, 2018-11-25 UTC; later *Communications in Algebra* 48 (2020), 625–637) study derivation Lie algebras of current Lie algebras over \(\mathbb C\). Their Section 4, especially the displayed representation of \(\operatorname{Der}(\mathfrak h_m)\) and Theorem 4.1, supplies a complex-field block-matrix framework. It does not state an idempotent-derivation orbit classification or finite-field rank polynomial, nor can its characteristic-zero Levi argument alone provide the extra self-adjoint projection branch in characteristic two. The conformal-symplectic reduction itself is standard and is not claimed as new.

A broader survey of one-dimensional-derived-subalgebra Leibniz algebras (Di Bartolo, La Rosa and Mancini, *Mediterranean Journal of Mathematics*, 2024, DOI 10.1007/s00009-024-02679-0) recalls the Heisenberg Lie model but develops the derivations of a different, nonnilpotent Leibniz family; its main classification does not imply this count. The symplectic orders and Lagrangian incidence formulas used here are classical and are credited as such. The additional claimed content is the complete idempotent-derivation orbit/rank census with its characteristic-two phase transition and central-lift multiplicities.

## Limitations
The result concerns ordinary \(K\)-linear derivations of the standard Heisenberg Lie algebra, not arbitrary two-step nilpotent algebras, superalgebras, endomorphism idempotents, or general current algebras. Its scientific originality has not been independently audited; analogous formulas under different terminology may exist. The computer checks exhaust only the four listed small finite-field instances, not all dimensions or characteristics.

## References
1. J. A. Ochoa Arango and N. Rojas, *The Automorphisms group of a Current Lie algebra*, arXiv:1811.09948v1 (2018-11-25), https://arxiv.org/abs/1811.09948 ; subsequently *The Lie algebra of derivations of a current Lie algebra*, *Communications in Algebra* 48 (2020), 625–637, DOI 10.1080/00927872.2019.1654490.
2. A. Di Bartolo, G. La Rosa and M. Mancini, *Non-Nilpotent Leibniz Algebras with One-Dimensional Derived Subalgebra*, *Mediterranean Journal of Mathematics* (2024), DOI 10.1007/s00009-024-02679-0.
