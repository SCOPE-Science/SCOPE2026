# Platonic Goursat curves: cyclic ramification and low-dimensional Jacobian factors
## Finding
For each smooth Platonic Goursat curve \(C=C_{r,t}\) of type \(d=3,4,6\) in the Gegelia--van Straten construction, the rotation-group quotient \(C\to C/G\) is a Galois cover of an elliptic curve **branched at precisely one point** with inertia \(2,3,5\), respectively. The canonical representations and group-algebra Jacobian decompositions are, in the same order,
\[
\begin{array}{c|c|c|c}
d&G&H^0(C,K_C)&J(C)\text{ up to complex isogeny}\\ \hline
3&A_4&\mathbf1\oplus\mathbf3&E_0\times E_1^3\\
4&S_4&\mathbf1\oplus\mathbf2\oplus\mathbf3\oplus\mathbf3'&E_0\times E_2^2\times E_3^3\times E_4^3\\
6&A_5&\mathbf1\oplus\mathbf3\oplus\mathbf3'\oplus2\mathbf4\oplus2\mathbf5&E_0\times B_2^3\times B_4^4\times B_5^5
\end{array}
\]
Here each \(E_i\) is an elliptic curve, \(E_0\cong J(C/G)\), and \(B_2,B_4,B_5\) are abelian surfaces. Factors are defined by rational group-algebra idempotents; their simplicity, distinctness, and mutual non-isogeny are **not** asserted. In particular, **all smooth tetrahedral and octahedral members have completely decomposable Jacobians**.

## Assumptions and scope
Work over \(\mathbf C\). Let \(V\cong\mathbf C^3\) be the complexified standard orthogonal rotation representation of the tetrahedral, octahedral or icosahedral group \(G=A_4,S_4,A_5\). Let \(P=x^2+y^2+z^2\) and let \(Q_d\in\mathbf C[V]^G\) be the respective Goursat invariant of degree \(d=3,4,6\) fixed in [1]. For \(r\in\mathbf C^*\) and \(t\in\mathbf C\), set
\[
C_{r,t}=V(P-rw^2,\;Q_d-tw^d)\subset\mathbf P(V\oplus\mathbf Cw)=\mathbf P^3.
\]
Assume this complete intersection is smooth; all statements are uniform over such \((r,t)\). Its genus is \(g=(d-1)^2\), and the effective action of \(G\) fixes \(w\). The known invariant-theoretic construction [1, §1.4--1.5] identifies its genus-one quotient with \(S^2=F(r,t,R)\). The claim concerns **complex isogenies**, not principally polarized isomorphisms or rational-field isogenies.

## Proof
**Canonical representation.** Write \(W=\mathbf1\oplus V\). Adjunction for the \((2,d)\) complete intersection gives \(K_C\cong\mathcal O_C(d-2)\). The group action on the adjunction isomorphism has no character twist: \(G\subset SO(V)\) has determinant one, and both defining equations are invariant. Put \(N=d-2\). The equivariant Koszul restriction sequence, together with the standard cohomology vanishing for line bundles on projective three-space, gives
\[
H^0(C,K_C)\cong\operatorname{Sym}^{N}(W)/(P-rw^2)\operatorname{Sym}^{N-2}(W)
\quad\text{as }\mathbf C[G]\text{-modules},
\]
with the denominator zero when \(N<2\). In the representation ring, the right side is
\[
\operatorname{Sym}^{N}(V)\oplus\operatorname{Sym}^{N-1}(V)
=\bigoplus_{\ell=0}^{N}\mathcal H_\ell,
\]
where \(\mathcal H_\ell\) is the degree-\(\ell\) trace-free harmonic representation of \(SO(3)\). This last equality uses \(\operatorname{Sym}^{j}V=\mathcal H_j\oplus\mathcal H_{j-2}\oplus\cdots\). Since \(\mathbf C[G]\) is semisimple, the representation-ring equality is an actual module isomorphism. For a rotation of angle \(\theta\), its character is therefore
\[
\chi_d(\theta)=\sum_{\ell=0}^{d-2}\sum_{j=-\ell}^{\ell}e^{ij\theta}
=\left|\sum_{j=0}^{d-2}e^{ij\theta}\right|^2.
\]
Evaluating at the rotation orders gives the character vectors \((4,0,1,1)\) for \(A_4\) (class orders \(1,2,3,3\)), \((9,1,1,0,1)\) for \(S_4\) (class orders \(1,2,2,3,4\)), and \((25,1,1,0,0)\) for \(A_5\) (class orders \(1,2,3,5,5\)). Standard character-table inner products yield the three stated irreducible decompositions. For \(A_5\), the two three-dimensional characters are Galois conjugates over \(\mathbf Q(\sqrt5)\); the other nontrivial characters are rational. The checker's exact cyclotomic reductions and character products independently reproduce these vectors and multiplicities.

**Jacobian splitting.** By the rational group-algebra decomposition of a Jacobian with finite automorphisms [2, §2], the relevant rational simple blocks of \(\mathbf Q[G]\) have matrix sizes \(3\) for the \(A_4\) three-dimensional character; \(2,3,3\) for the three nontrivial \(S_4\) characters; and \(3\) over \(\mathbf Q(\sqrt5)\), \(4\) over \(\mathbf Q\), and \(5\) over \(\mathbf Q\) for the nontrivial \(A_5\) blocks. All have Schur index one. Primitive matrix idempotents yield abelian subvarieties, whose \(H^{1,0}\) dimensions equal the dimension of each isotypic piece divided by its matrix size. They are respectively \(1\) in every tetrahedral or octahedral block and \(2\) in each nontrivial icosahedral rational block. The trivial block is \(J(C/G)\) up to isogeny, and the quotient is genus one by [1]. Multiplication of these primitive factors reconstructs \(J(C)\) up to isogeny, giving precisely the displayed powers. The dimension sums are \(1+3=4\), \(1+2+3+3=9\), and \(1+6+8+10=25\).

**One branch orbit.** The genus of the quotient by a cyclic subgroup of order \(m\) is the invariant dimension \(g_m=m^{-1}\sum_{j=0}^{m-1}\chi_d(h^j)\). The values for orders \(2,3\) in \(A_4\) are \((2,2)\); for orders \(2,3,4\) in \(S_4\), \((5,3,3)\); and for orders \(2,3,5\) in \(A_5\), \((13,9,5)\). Riemann--Hurwitz for \(C\to C/\langle h\rangle\) gives no fixed point of a nonidentity rotation except for the elements of respective orders \(2,3,5\), each having precisely two fixed points. Specifically the tame defect \(2g-2-m(2g_m-2)\) is zero for the other orders and equals \(2(m-1)\) for the indicated order. There are exactly \(3,4,6\) subgroups of these respective orders, and their fixed-point sets are disjoint: stabilizers of smooth complex curve points are cyclic and contain no other nontrivial orders with fixed points. Thus the ramification locus has \(6,8,12\) points, respectively. These are exactly \(|G|/m\) points, the cardinality of a single orbit of inertia order \(m\). Hence the full quotient cover has one branch point and the claimed inertia. This also agrees with \(2g-2=|G|(1-1/m)\) over its elliptic quotient.

## Verification
Run `python3 verification.py` using only the Python standard library. Its exact integer cyclotomic calculations evaluate all indicated rotational harmonic characters, verify the decomposition against the ordinary character tables (with the two golden-ratio characters represented in the basis \(1,\varphi\)), check dimensions and cyclic invariant subspaces, and independently verify the Riemann--Hurwitz defects and one-orbit cardinalities. It prints `VERIFY_OK`. The proof applies to **every** smooth member and rests on equivariant adjunction, character theory and Riemann--Hurwitz, not on sampling parameters.

## Relationship to prior work
Gegelia and van Straten [1] construct the Platonic complete-intersection curves, prove the three genus formulas and identify their elliptic rotation-group quotients by invariant theory. They do not state the complete Hodge characters, full rational group-algebra factor dimensions or one-point branch signatures derived here. Paulhus and Rojas [2] establish the general group-algebra decomposition method, and their genus-four and genus-nine example tables concern other group actions/signatures, not the current elliptic-quotient families. Neither the abstract group-algebra theorem nor the known quotient equation alone records these three explicit decompositions. These established ingredients are not themselves claimed as new.

## Limitations
The factorization is over \(\mathbf C\) and only up to unpolarized isogeny. It neither asserts generic simplicity of the abelian surfaces nor classifies additional automorphisms or degeneration at singular parameters. Known standard representation-theoretic machinery is essential; an unlocated earlier signature calculation could already imply part or all of the displayed formulas. The explicit factor dimensions and single-branch structure are the claimed subject, not novelty of harmonic theory or of group-algebra decompositions.

## References
[1] N. Gegelia and D. van Straten, *The platonic elliptic surfaces*, arXiv:2608.25644v1 (26 August 2026), especially §§1.2--1.5, https://arxiv.org/pdf/2608.25644 .

[2] J. Paulhus and A. M. Rojas, *Completely Decomposable Jacobian Varieties in New Genera*, *Experimental Mathematics* 26 (2017), 430--445, arXiv:1603.00331, §§2,5, https://arxiv.org/pdf/1603.00331 .

[3] S. Reyes-Carocca and R. E. Rodríguez, *On Jacobians with group action and coverings*, arXiv:1711.07552 (2017), https://arxiv.org/abs/1711.07552 .
