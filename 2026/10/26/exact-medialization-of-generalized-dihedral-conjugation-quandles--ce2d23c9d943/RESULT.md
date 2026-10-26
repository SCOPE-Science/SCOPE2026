# Exact medialization of generalized-dihedral conjugation quandles

## Finding

Let \(A\) be any abelian group and \(D=\operatorname{Dih}(A)=A\rtimes C_2\), with the nonidentity element of \(C_2\) acting on \(A\) by inversion. Write \(Q=\operatorname{Conj}(D)\) for the conjugation quandle, with \(x\triangleright y=y^{-1}xy\). Its universal medial quotient is completely described as follows.

The underlying set of \(Q^{\mathrm{med}}\) is the disjoint union of a copy \(\{R_a:a\in A\}\) of \(A\) and a copy \(\{S_{\bar a}:\bar a\in A/4A\}\) of \(A/4A\). Here \(4A=\{4a:a\in A\}\), and a bar denotes a coset in \(A/4A\). All rotations remain distinct; two reflections become equal exactly when their indices differ by an element of \(4A\). Its operation is

\[
\begin{aligned}
R_a\triangleright R_b&=R_a,&
R_a\triangleright S_{\bar b}&=R_{-a},\\
S_{\bar a}\triangleright R_b&=S_{\overline{a-2b}},&
S_{\bar a}\triangleright S_{\bar b}&=S_{\overline{2b-a}}.
\end{aligned}
\]

For finite \(A\), therefore,

\[
\bigl|\operatorname{Conj}(\operatorname{Dih}(A))^{\mathrm{med}}\bigr|
=|A|+|A/4A|.
\]

If \(A\cong\prod_{i=1}^{r}C_{n_i}\) is finite, this is \(\prod_i n_i+\prod_i\gcd(n_i,4)\). In particular, for a dihedral group of order \(2n\), the medial quotient contains precisely \(n+\gcd(n,4)\) elements. For odd \(n\) it has \(n+1\) elements; for \(n\equiv2\pmod4\), it has \(n+2\); for \(4\mid n\), it has \(n+4\).

## Assumptions and scope

No finiteness hypothesis is needed for the structural assertion. The group \(A\) is written additively, and the involution in the semidirect product acts by \(a\mapsto-a\). The construction includes the cases where the action is trivial, as happens for groups of exponent two. The medial quotient means the quotient by the least quandle congruence imposing

\[
(x\triangleright y)\triangleright(z\triangleright t)
=(x\triangleright z)\triangleright(y\triangleright t)
\]

for every choice of \(x,y,z,t\). It is not the commutativization of the quandle and not the conjugation quandle of a group abelianization.

## Proof

**1. The conjugation table.** Distinguish a rotation \(R_a=(a,0)\) from a reflection \(S_a=(a,1)\). The group law is \((a,\epsilon)(b,\delta)=(a+(-1)^\epsilon b,\epsilon+\delta\pmod2)\). Direct conjugation yields

\[
\begin{aligned}
R_a\triangleright R_b&=R_a,&
R_a\triangleright S_b&=R_{-a},\\
S_a\triangleright R_b&=S_{a-2b},&
S_a\triangleright S_b&=S_{2b-a}.
\end{aligned}
\]

These identities hold in every abelian group \(A\), including one with nontrivial two-torsion.

**2. Every medial quotient identifies reflection indices differing by \(4A\).** In the medial identity, take \(x=S_a\), \(y=S_a\), \(z=R_0\), and \(t=S_{a+b}\). The left-hand side is \(S_a\), since \(S_a\triangleright S_a=S_a\) and \(R_0\triangleright S_{a+b}=R_0\). The right-hand side is \(S_{a+4b}\), since \(S_a\triangleright R_0=S_a\) and \(S_a\triangleright S_{a+b}=S_{a+2b}\). Therefore every congruence with a medial quotient must identify \(S_a\) and \(S_{a+4b}\) for every \(a,b\in A\). The transitive closure contains all pairs of reflections whose index difference lies in \(4A\).

**3. This is the only forced identification.** Define an equivalence relation that leaves each \(R_a\) singleton, never identifies a rotation with a reflection, and identifies \(S_a\) with \(S_b\) precisely when \(a-b\in4A\). The four displayed conjugation formulas show directly that this relation is compatible with \(\triangleright\) and its right-division operation: changing a reflection index by an element of \(4A\) changes every reflected output index by an element of \(4A\), while rotation outputs are unchanged. Hence it is a quandle congruence.

To show its quotient is medial, write \(B=A/4A\); thus \(4B=0\). For each quandle element \(u\), let \(T_u(x)=x\triangleright u\) be its right translation. On the rotation copy of \(A\), each \(T_{R_b}\) is the identity, and each \(T_{S_{\bar b}}\) is inversion. These maps commute. On the reflection copy of \(B\), the maps are translations \(x\mapsto x-2\bar b\) and reflections \(x\mapsto2\bar b-x\). Two translations commute. A translation by \(-2\bar b\) commutes with each reflection because twice its displacement is \(-4\bar b=0\). Two reflections commute because the difference between their two composites is \(4(\bar b-\bar c)=0\). Thus all right translations commute on the entire quotient.

For completeness, every quandle obeys \(T_{u\triangleright v}=T_vT_uT_v^{-1}\), by right self-distributivity. When the right translations commute, this becomes \(T_{u\triangleright v}=T_u\). Therefore

\[
(x\triangleright y)\triangleright(z\triangleright t)
=T_zT_y(x)=T_yT_z(x)
=(x\triangleright z)\triangleright(y\triangleright t),
\]

so the quotient is medial. Its congruence is consequently an admissible medial congruence, while Step 2 shows every admissible medial congruence contains it. Thus it is exactly the universal medial congruence, proving the entire operation table and the nonidentification of distinct rotations.

**4. Cardinalities.** When \(A\) is finite, the quotient has \(|A|\) rotation classes and \(|A/4A|\) reflection classes. For a cyclic factor \(C_n\), the quotient by fourth multiples has \(\gcd(n,4)\) elements; taking finite direct products gives the stated formula.

## Verification

A standalone finite checker, `check_medial.py`, forms the generalized-dihedral group by its actual group multiplication and computes its conjugation table. It initializes the congruence with every medial-identity pair, then closes it under both quandle multiplication and right division. It compares the resulting equivalence classes exactly with the proposed \(A/4A\) reflection fibers and singleton rotation fibers. The checker succeeded on twenty-four complete finite examples: cyclic \(A=C_n\) for \(1\le n\le13\), plus eleven noncyclic products, including \(C_4\times C_4\) and \(C_2\times C_2\times C_4\). These experiments confirm the finite instances only; the proof above establishes the general theorem.

Run the included script using `python3 check_medial.py`. Its expected final line is `VERIFY_OK: 24 complete quotient computations`.

## Relationship to prior work

Bardakov and Sangare, *Constructions and automorphisms of quandles* (first posted October 13, 2026), Section 5, define the universal medial quotient, prove the criterion \(\operatorname{Conj}(G)\) medial if and only if \(\gamma_2(G)\le Z(G)\), and give general lower bounds. They calculate the six-element group \(S_3\) case, obtaining a four-element medial quotient. The current formula agrees with that case and extends it to all generalized dihedral groups, determining the congruence rather than only bounds. Their result on the commutativization of the *core* quandle is a different construction.

Fan, *Signature Modules and the Dihedral Conjugation-Quandle Counting Invariant* (September 11, 2026), gives the same underlying rotation/reflection conjugation laws and extends its link-coloring counts to generalized dihedral groups. Link-coloring signature modules do not identify the least congruence enforcing mediality. The general structure theory of medial quandles in Jedlička–Pilitowska–Stanovský–Zamojska-Dzienio (2015) provides context but no identified generalized-dihedral universal-quotient formula.

## Limitations

This describes the medial quotient for the inversion semidirect products \(A\rtimes C_2\), not arbitrary semidirect products or arbitrary group conjugation quandles. Finite calculations were supplementary and cannot establish the infinite statement by themselves. Mathematical priority remains subject to an unindexed or unlocated equivalent formulation; the general classification of medial quandles might offer alternate derivations but does not alone state this quotient computation. The proof and code do not constitute external or independent certification.

## References

1. V. G. Bardakov and B. Sangare, *Constructions and automorphisms of quandles*, arXiv:2610.18676, first posted 2026-10-13, Section 5, Theorem 5.4. https://arxiv.org/html/2610.18676v1
2. Z. Fan, *Signature Modules and the Dihedral Conjugation-Quandle Counting Invariant*, arXiv:2609.13326, first posted 2026-09-11, Sections 3 and 10. https://arxiv.org/html/2609.13326v1
3. P. Jedlička, A. Pilitowska, D. Stanovský, and A. Zamojska-Dzienio, *The structure of medial quandles*, Journal of Algebra 443 (2015), 300–334, arXiv:1409.8396. https://arxiv.org/abs/1409.8396
