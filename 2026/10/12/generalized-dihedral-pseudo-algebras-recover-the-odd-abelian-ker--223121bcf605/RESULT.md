# Generalized dihedral pseudo-algebras recover the odd abelian kernel

## Finding

Let \(A\) be a finite abelian group of odd order, and let
\[
G=\operatorname{Dih}(A)=A\rtimes\langle t\rangle,
\qquad t^2=1,
\]
where
\[
tat^{-1}=a^{-1}
\]
for every \(a\in A\).

For \(d\ge1\), write
\[
N_A(d)
=
\left|
\{a\in A:o(a)=d\}
\right|.
\]
If \(m_G(d)\) denotes the number of irreducible characters of \(G\) with codegree \(d\), then
\[
\boxed{
C(G)
=
\{(1,1),(2,1)\}
\cup
\left\{
\left(d,\frac{N_A(d)}2\right):
d>1,\ N_A(d)>0
\right\}.
}
\]

Thus the group pseudo-algebra of \(\operatorname{Dih}(A)\) is exactly the element-order spectrum of \(A\), with every nontrivial multiplicity divided by \(2\), together with the two linear codegrees \(1\) and \(2\).

Consequently the pseudo-algebra determines the odd abelian kernel:
\[
\boxed{
C(\operatorname{Dih}(A))
=
C(\operatorname{Dih}(B))
\iff
A\cong B
}
\]
for finite abelian groups \(A,B\) of odd order. Equivalently,
\[
\boxed{
C(\operatorname{Dih}(A))
=
C(\operatorname{Dih}(B))
\iff
\operatorname{Dih}(A)
\cong
\operatorname{Dih}(B).
}
\]

There is also an explicit reconstruction procedure. Fix an odd prime \(p\), and write
\[
A_p
\cong
\bigoplus_i C_{p^{\lambda_i}}.
\]
For \(k\ge1\), the pseudo-algebra gives
\[
M_k
=
1+
2\sum_{j=1}^{k}m_G(p^j).
\]
Then
\[
\boxed{
M_k
=
|A_p[p^k]|
=
p^{\sum_i\min(k,\lambda_i)}.
}
\]
Hence, if
\[
s_k=\log_p M_k,
\qquad
s_0=0,
\]
then
\[
s_k-s_{k-1}
=
\#\{i:\lambda_i\ge k\}.
\]
These successive differences recover the invariant-factor partition of every Sylow subgroup of \(A\).

## Assumptions and scope

The group pseudo-algebra is
\[
C(G)
=
\{(d,m_G(d)):d\in\operatorname{cod}(G)\},
\]
where
\[
\operatorname{cod}(\chi)
=
\frac{|G:\ker\chi|}{\chi(1)}.
\]

The theorem assumes that \(A\) has odd order. This ensures that inversion has no nontrivial fixed character on \(\operatorname{Irr}(A)\), so every nonprincipal character lies in an orbit of size \(2\).

The conclusion is internal to generalized dihedral groups over odd abelian kernels. No claim is made that an arbitrary finite group sharing the same pseudo-algebra must itself be generalized dihedral.

## Proof

Because \(A\) has odd order, the squaring map on \(A\) is bijective. Therefore
\[
[G,G]=A,
\]
since
\[
[a,t]=a^{-2}
\]
and every element of \(A\) is a square.

It follows that
\[
G/G'\cong C_2.
\]
Hence \(G\) has exactly two linear characters. The principal character has codegree \(1\), and the nontrivial linear character with kernel \(A\) has codegree \(2\).

Now let
\[
1_A\ne\lambda\in\operatorname{Irr}(A).
\]
Conjugation by \(t\) sends
\[
\lambda
\quad\text{to}\quad
\lambda^{-1}.
\]
Since \(A\) has odd order, so does its dual group \(\operatorname{Irr}(A)\). Therefore
\[
\lambda=\lambda^{-1}
\]
would imply
\[
\lambda^2=1,
\]
and hence \(\lambda=1_A\), a contradiction.

Thus every nonprincipal character of \(A\) has orbit
\[
\{\lambda,\lambda^{-1}\}
\]
of size \(2\).

By Clifford theory,
\[
\chi_\lambda=\lambda^G
\]
is irreducible of degree \(2\), and
\[
\chi_\lambda=\chi_{\lambda^{-1}}.
\]
Conversely, every nonlinear irreducible character of \(G\) arises in this way.

On \(A\),
\[
(\chi_\lambda)_A
=
\lambda+\lambda^{-1},
\]
while
\[
\chi_\lambda(g)=0
\]
for
\[
g\in G\setminus A.
\]
Therefore no element outside \(A\) lies in \(\ker\chi_\lambda\).

For \(a\in A\), write
\[
z=\lambda(a).
\]
Then
\[
\chi_\lambda(a)=z+z^{-1}.
\]
Since \(z\) is a complex root of unity,
\[
z+z^{-1}=2
\]
holds exactly when
\[
z=1.
\]
Thus
\[
\ker\chi_\lambda
=
\ker\lambda.
\]

Because
\[
\chi_\lambda(1)=2,
\]
we obtain
\[
\operatorname{cod}(\chi_\lambda)
=
\frac{|G:\ker\lambda|}{2}
=
|A:\ker\lambda|.
\]
For a linear character of a finite abelian group,
\[
|A:\ker\lambda|
=
o(\lambda).
\]
Hence
\[
\operatorname{cod}(\chi_\lambda)=o(\lambda).
\]

The dual group \(\operatorname{Irr}(A)\) is isomorphic to \(A\). Therefore it has exactly
\[
N_A(d)
\]
characters of exact order \(d\). For
\[
d>1,
\]
these characters are paired by inversion into orbits of size \(2\). Each orbit gives one irreducible character of codegree \(d\). Thus
\[
m_G(d)
=
\frac{N_A(d)}2.
\]
This proves the displayed pseudo-algebra formula.

It remains to show that the resulting order spectrum determines \(A\). Fix an odd prime \(p\). The number
\[
1+\sum_{j=1}^{k}N_A(p^j)
\]
counts exactly the elements in the Sylow subgroup \(A_p\) whose order divides \(p^k\), because every other Sylow component must be trivial for an element to have \(p\)-power order.

If
\[
A_p
\cong
\bigoplus_i C_{p^{\lambda_i}},
\]
then
\[
|A_p[p^k]|
=
p^{\sum_i\min(k,\lambda_i)}.
\]
Since
\[
N_A(p^j)=2m_G(p^j),
\]
the pseudo-algebra determines every number
\[
M_k
=
1+
2\sum_{j=1}^{k}m_G(p^j)
=
|A_p[p^k]|.
\]
Taking base-\(p\) logarithms gives
\[
s_k=\sum_i\min(k,\lambda_i).
\]
Hence
\[
s_k-s_{k-1}
=
\#\{i:\lambda_i\ge k\}.
\]
The number of cyclic factors of exact exponent \(p^k\) is therefore
\[
(s_k-s_{k-1})-(s_{k+1}-s_k).
\]
Thus every Sylow invariant is recovered, so \(A\) is recovered up to isomorphism.

## Verification

The included checker independently enumerates the element-order spectra of several odd finite abelian groups, constructs the predicted pseudo-algebras, and reconstructs the Sylow invariant factors from those pseudo-algebras.

The test kernels include
\[
C_9,\quad
C_3\times C_3,\quad
C_9\times C_5,\quad
C_3\times C_9,\quad
C_5\times C_5,
\]
\[
C_3\times C_3\times C_5,\quad
C_9\times C_{25},\quad
C_3\times C_9\times C_5.
\]

For every test case, the checker verifies:

- the formula
  \[
  m_G(d)=N_A(d)/2
  \]
  for every nontrivial odd codegree;
- that the two linear codegrees are \(1\) and \(2\), each with multiplicity \(1\);
- the irreducible degree-squared identity
  \[
  2\cdot1^2+\frac{|A|-1}{2}\cdot2^2=2|A|;
  \]
- exact reconstruction of all Sylow invariant factors from the values
  \[
  1+2\sum_{j\le k}m_G(p^j).
  \]

The checker also confirms that
\[
C_9\times C_5
\]
and
\[
C_3\times C_3\times C_5
\]
have the same order but different generalized-dihedral pseudo-algebras, as the theorem predicts.

The checker returns `VERIFY_OK`.

Finite enumeration is not used to prove the theorem.

## Relationship to prior work

Moretó introduced the group pseudo-algebra and explicitly asked what structural information it determines. For abelian groups, the paper observes that the pseudo-algebra determines the group because character codegrees record the element-order spectrum of the dual group.

The theorem above transfers that mechanism to a natural nonabelian family. For an odd generalized dihedral group, every nonlinear character is induced from an inversion pair in the dual of the abelian kernel, and its codegree is exactly the order of the inducing character. Thus the nonabelian pseudo-algebra retains the complete order spectrum of the kernel.

Lewis and Yan subsequently showed that group pseudo-algebras do not determine group order in general, by constructing \(p\)-group counterexamples, and they prove positive results under additional \(p\)-group hypotheses. Their searchable article description and indexed text do not contain a generalized-dihedral or Frobenius-family theorem.

The ordinary representation theory of generalized dihedral groups makes the character parametrization standard. The new statement is the exact codegree-multiplicity formula, its interpretation as the kernel's element-order spectrum, and the resulting rigidity of the entire odd generalized-dihedral family.

Targeted searches under “group pseudo-algebra,” “generalized dihedral,” “character codegree multiplicity,” “inversion semidirect product,” and “element-order spectrum” did not locate this result.

## Limitations

The odd-order hypothesis on \(A\) is essential for the clean formula. If \(A\) has nontrivial \(2\)-torsion, inversion has fixed nonprincipal characters, producing additional linear characters and a different Clifford-theoretic decomposition.

The theorem establishes rigidity only within the generalized-dihedral family. It does not exclude a finite group outside this family from sharing the same pseudo-algebra.

The character classification used in the proof is standard. The claimed new content is the exact pseudo-algebra formula and the resulting reconstruction theorem.

Failed searches do not prove novelty.

## References

1. A. Moretó, “Multiplicities of character codegrees of finite groups,” *Bulletin of the London Mathematical Society* 55 (2023), 234–241, DOI 10.1112/blms.12724. First published online 8 September 2022.
2. M. L. Lewis and Q. Yan, “On the group pseudo-algebra of finite groups,” arXiv:2402.12648v1, first public version 20 February 2024; *Comptes Rendus. Mathématique* 362 (2024), 1661–1665, DOI 10.5802/crmath.671.
