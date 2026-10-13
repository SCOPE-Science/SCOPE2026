# Extraspecial group pseudo-algebras recover order but not type

## Finding

Let \(G\) be an extraspecial \(p\)-group of order
\[
p^{1+2n},
\qquad
n\ge1.
\]
Thus
\[
Z(G)=G'=\Phi(G)\cong C_p,
\qquad
G/Z(G)\cong C_p^{2n}.
\]

For
\[
\operatorname{cod}(\chi)
=
\frac{|G:\ker\chi|}{\chi(1)},
\]
let \(m_G(d)\) be the number of irreducible characters of codegree \(d\). Then
\[
\boxed{
C(G)
=
\left\{
(1,1),\,
(p,p^{2n}-1),\,
(p^{n+1},p-1)
\right\}.
}
\]

Therefore, for extraspecial groups \(G\) and \(H\),
\[
\boxed{
C(G)=C(H)
\iff
|G|=|H|.
}
\]
The smallest nontrivial codegree recovers \(p\); the largest codegree is \(p^{n+1}\), so it recovers \(n\), and hence
\[
|G|=p^{1+2n}.
\]

Nevertheless, the two nonisomorphic extraspecial groups of every order \(p^{1+2n}\) have identical pseudo-algebras. Thus the invariant determines order but not extraspecial type.

## Assumptions and scope

The group pseudo-algebra is the codegree-multiplicity set
\[
C(G)=\{(d,m_G(d)):d\in\operatorname{cod}(G)\}.
\]

The theorem is a classification internal to the extraspecial family. It does not assert that every finite group sharing this pseudo-algebra is extraspecial.

For odd \(p\), the two extraspecial types are distinguished by exponent behavior. For \(p=2\), they are the plus and minus types.

## Proof

Because
\[
G'=Z(G)\cong C_p,
\]
the abelianization is
\[
G/G'\cong C_p^{2n}.
\]
Hence \(G\) has exactly \(p^{2n}\) linear irreducible characters.

The principal character has codegree \(1\). Every nonprincipal linear character has kernel of index \(p\), because it is a nonzero linear functional on the elementary abelian quotient. Therefore
\[
m_G(p)=p^{2n}-1.
\]

Standard extraspecial character theory gives exactly \(p-1\) nonlinear irreducible characters. They are indexed by the nonprincipal characters
\[
\lambda\in\operatorname{Irr}(Z(G))
\]
and each has degree \(p^n\). For the character \(\psi_\lambda\),
\[
\psi_\lambda(g)=0
\]
when \(g\notin Z(G)\), while
\[
\psi_\lambda(z)=p^n\lambda(z)
\]
for \(z\in Z(G)\).

Since \(Z(G)\) has prime order, every nonprincipal \(\lambda\) is faithful. Therefore no nonidentity central element lies in \(\ker\psi_\lambda\). No noncentral element lies in its kernel either, because its value there is \(0\), not the degree \(p^n\). Hence
\[
\ker\psi_\lambda=1.
\]
Thus every nonlinear irreducible has codegree
\[
\frac{|G|}{p^n}=p^{n+1}.
\]
There are \(p-1\) such characters.

The degree-squared check is
\[
p^{2n}+(p-1)p^{2n}=p^{2n+1}=|G|,
\]
so these characters exhaust \(\operatorname{Irr}(G)\). This proves the formula.

The least nontrivial codegree is \(p\), so \(p\) is recovered from \(C(G)\). The largest codegree is \(p^{n+1}\), so \(n\) is recovered. Hence the order is recovered.

The formula depends only on \(p\) and \(n\), not on the extraspecial type. Since there are two nonisomorphic extraspecial types for every order \(p^{1+2n}\), they have the same pseudo-algebra.

## Verification

The included checker evaluates the formula for
\[
p\in\{2,3,5,7\},
\qquad
1\le n\le4.
\]
It checks the total number of irreducibles, the degree-squared identity, and reconstruction of \(p\), \(n\), and \(|G|\) from the pseudo-algebra.

It also checks the smallest type collisions:
\[
D_8,\ Q_8:
\qquad
C(G)=\{(1,1),(2,3),(4,1)\},
\]
and the two extraspecial groups of order \(27\):
\[
C(G)=\{(1,1),(3,8),(9,2)\}.
\]

The checker returns `VERIFY_OK`.

Finite arithmetic checks are not used to prove the theorem.

## Relationship to prior work

Lewis and Yan study group pseudo-algebras of finite groups. They show that equal pseudo-algebras do not determine group order in general and prove positive rigidity statements for restricted classes of \(p\)-groups. Their inspected full text contains no extraspecial specialization.

Moretó introduced the group pseudo-algebra and asked whether it determines group order. His paper proves rigidity in several settings but does not discuss extraspecial groups in the inspected full text.

The ordinary character theory of extraspecial groups is classical. A modern source by Sin and Sorci records the standard character structure used here: \(p^{2n}\) linear characters and \(p-1\) nonlinear characters of degree \(p^n\), with the nonlinear characters supported on the center.

The result above extracts the exact codegree multiplicities from that character structure and gives a complete invariant statement: within the extraspecial family, pseudo-algebras recover order exactly but cannot distinguish the two extraspecial types.

Targeted database and literature searches under extraspecial, pseudo-algebra, character-codegree, and exact-multiplicity formulations did not locate this classification.

## Limitations

The underlying extraspecial character table is standard. The new content is the exact pseudo-algebra formula and the resulting rigidity/type-blindness classification.

Order recovery is proved only within the extraspecial family. The theorem does not exclude collisions with non-extraspecial groups.

An equivalent short calculation may exist in older codegree literature without the later term “group pseudo-algebra.”

Failed searches do not prove novelty.

## References

1. M. L. Lewis and Q. Yan, “On the group pseudo-algebra of finite groups,” arXiv:2402.12648v1, first public version 20 February 2024; *Comptes Rendus. Mathématique* 362 (2024), 1661–1665, DOI 10.5802/crmath.671. MSC 2020: 20C15, 20D15.
2. A. Moretó, “Multiplicities of character codegrees of finite groups,” *Bulletin of the London Mathematical Society* 55 (2023), 234–241, first published online 8 September 2022, DOI 10.1112/blms.12724.
3. P. Sin and J. Sorci, “Continuous-time Quantum Walks on Cayley Graphs of Extraspecial Groups,” arXiv:2011.07566v1, first public version 15 November 2020; *Algebraic Combinatorics* 5 (2022), 81–101, DOI 10.5802/alco.237.
