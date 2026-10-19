# Exact augmentation-fibre unit-sumsets in finite-dimensional algebras

## Finding

Let \(F=\mathbb F_q\), \(q>2\), and let \(R\) be any finite-dimensional associative unital \(F\)-algebra with a unital \(F\)-algebra homomorphism \(\varepsilon:R\to F\). Because \(\varepsilon(1)=1\), this homomorphism is surjective. For any \(U\subseteq F^\times\), put

\[
V_U=\{v\in R^\times:\varepsilon(v)\in U\}, \qquad nU=\{u_1+\cdots+u_n:u_i\in U\}.
\]

For **every integer** \(n\ge2\), there is an exact equality of additive subsets of \(R\):

\[
\boxed{\underbrace{V_U+\cdots+V_U}_{n}=\varepsilon^{-1}(nU).}
\]

Neither \(U\) nor \(nU\) is assumed to be a subgroup or a subfield. Empty \(U\) is permitted (both sides are then empty). Thus all additive representation lengths and all augmentation-fibre restrictions are inherited exactly from the finite field. In particular, for every finite group \(G\), the group algebra \(F[G]\) has the \(n\)-sum property using units with augmentation in \(U\) **if and only if** \(nU=F\). This gives an affirmative answer for all finite groups to Question 3.5 in the reference below.

## Assumptions and scope

All rings are associative with identity and all homomorphisms preserve identity. No assumption on the characteristic relative to the group order is imposed. The finite-dimensionality assumption ensures a nilpotent Jacobson radical and a finite product-of-matrix-algebras quotient. The condition \(q>2\) is needed for the universal statement; the principal result is not asserted for \(q=2\). The notation \(nU\) denotes an **exactly** \(n\)-fold sum, with repetitions allowed, and not the union of sums of at most \(n\) elements.

## Proof

**Lemma 1 (matrix blocks have every exact sum length).** If \(K\) is a field with at least three elements, every \(M\in M_d(K)\), for any integer \(d\ge1\), is a sum of exactly \(n\) units for every integer \(n\ge2\).

Indeed, write \(r=\operatorname{rank}M\) and choose invertible \(P,Q\) so that \(PMQ=\operatorname{diag}(I_r,0_{d-r})\). Choose \(t\in K\setminus\{0,1\}\). Then

\[
\operatorname{diag}(I_r,0_{d-r})=
\operatorname{diag}(tI_r,I_{d-r})+
\operatorname{diag}((1-t)I_r,-I_{d-r}).
\]

Both summands are invertible, including when \(r=0\) or \(r=d\) (empty blocks omitted). Multiplication by \(P^{-1}\) and \(Q^{-1}\) gives two invertible matrices summing to \(M\). To obtain any greater exact length, repeatedly express one previously chosen invertible summand as a sum of two invertibles, and replace it by those two. This proves the lemma. In particular, any finite product \(B\) of matrix algebras over finite extensions of \(F\) satisfies \(nB^\times=B\), for every \(n\ge2\); a zero direct factor may simply be omitted.

**Lemma 2 (augmentation splits the semisimple quotient).** Write \(J=\operatorname{Jac}(R)\). Because \(R\) is finite-dimensional, \(J\) is nilpotent. Its image under \(\varepsilon\) lies in the Jacobson radical of \(F\), so \(\varepsilon(J)=0\). The induced surjective algebra map \(\bar\varepsilon:R/J\to F\) therefore splits along a simple direct factor. By the Artin--Wedderburn theorem, there is an \(F\)-algebra identification

\[
R/J\simeq F\times B,\qquad \bar\varepsilon(a,b)=a,
\]

where \(B\) is a possibly zero finite product of full matrix algebras over finite extensions of \(F\). For completeness, an algebra homomorphism from a simple matrix factor onto the field \(F\) is injective as well as surjective, forcing that factor to be \(F\) itself; the kernel is the product of all remaining simple factors. The cases in which \(B\) is zero are interpreted by omitting its coordinate.

**Exact sumset identity.** The units of the quotient with prescribed augmentation are \(U\times B^\times\). Lemma 1 implies that their exactly \(n\)-fold sumset is

\[
 n(U\times B^\times)=nU\times B.
\]

Let \(x\in R\) with \(\varepsilon(x)\in nU\). Thus its image \(\bar x\in R/J\) can be written as \(\bar v_1+\cdots+\bar v_n\) with each \(\bar v_i\) a unit and \(\bar\varepsilon(\bar v_i)\in U\). Lift each \(\bar v_i\) to \(v_i\in R\). These lifts are units, because invertibility lifts modulo the Jacobson radical. Set \(j=x-\sum_i v_i\in J\). Then \(v_1+j\) is still a unit, since it has the same unit image in \(R/J\), and its augmentation remains in \(U\), since \(\varepsilon(J)=0\). We have

\[
x=(v_1+j)+v_2+\cdots+v_n\in nV_U.
\]

Conversely, applying the additive algebra map \(\varepsilon\) to any expression \(x=\sum_i v_i\) with \(v_i\in V_U\) shows \(\varepsilon(x)\in nU\). Therefore \(nV_U=\varepsilon^{-1}(nU)\).

For the group-algebra application, the standard augmentation \(\sum_{g\in G}a_g g\mapsto\sum_g a_g\) is a unital \(F\)-algebra epimorphism. Every finite group algebra is finite-dimensional, and the equivalence follows immediately.

**Boundary counterexample.** Set \(R=\mathbb F_2\times\mathbb F_2\), \(\varepsilon(a,b)=a\), \(U=\{1\}\), and \(n=2\). The sole unit of \(R\) is \((1,1)\), so \(2V_U=\{(0,0)\}\), whereas \(2U=\{0\}\) and \(\varepsilon^{-1}(2U)=\{(0,0),(0,1)\}\). The universal identity fails over the binary field. This is a boundary example for the general algebra theorem, not a counterexample to a group-algebra statement whose field hypothesis is satisfied.

## Verification

Run `python3 verify.py` with Python 3 and no external packages. The verifier computes invertibility by finite-field Gaussian elimination and checks the complete twofold sumsets in the 729-element algebra \(\mathbb F_3[S_3]\), for \(U=\{1\}\) and \(U=\{1,2\}\). It also tests all 2,197 elements of the triangular matrix algebra \(T_2(\mathbb F_{13})\) for a six-element square-residue subgroup and for singleton \(U=\{1\}\), and checks the stated binary boundary example. The output ends with `VERIFY_OK`. These exhaustive finite examples validate implementations and boundary behavior but are not used to infer the infinite-family statement; that statement follows from Lemmas 1 and 2.

## Relationship to prior work

Mináč, Nguyen and Tân explicitly ask in Question 3.5 of their July 2026 paper whether the field \(n\)-sum property with prescribed augmentation values passes to \(F[G]\) for every finite group \(G\). Their Proposition 3.2 handles nilpotent-ideal lifting, Proposition 3.8 handles normal-subgroup extensions with invertible subgroup order, and Propositions 3.7--3.13 establish special classes (including \(p\)-groups, abelian groups, and dihedral groups). They state following Proposition 3.12 that the unrestricted group case remains unclear. The present argument supplies the missing uniform semisimple quotient decomposition with a distinguished field factor and thereby removes **all group-theoretic restrictions**. Its exact identity \(nV_U=\varepsilon^{-1}(nU)\) is stronger than their affirmative-question formulation. The unrestricted two-unit matrix decomposition and nilpotent lifting are classical ingredients and are not claimed as new independently.

## Limitations

The proof requires a unital augmentation map onto a finite field with more than two elements and a finite-dimensional algebra. No claim is made for infinite-dimensional algebras, for arbitrary homomorphisms to nonfield rings, or for the binary-field universal identity (which is false as shown). While the motivating open question appears unresolved in the inspected preprint and targeted literature searches found no covering theorem, an equivalent theorem in unindexed literature remains a bibliographic risk. 
## References

1. J. Mináč, T. T. Nguyen and N. D. Tân, *Sums of units in finite rings and applications to Cayley graphs*, arXiv:2607.00404v1, first public 1 July 2026, especially Question 3.5 and Propositions 3.2, 3.7--3.13. https://arxiv.org/abs/2607.00404
2. Classical Artin--Wedderburn decomposition of finite-dimensional semisimple algebras and Jacobson radical lifting of units; standard ring-theoretic facts, used as background.
3. Classical two-invertible-matrix decomposition (Zelinsky); the proof needed over finite fields of order greater than two is reproduced above.
