# Exact lattice formulas for commutativity degrees of arbitrary generalized dicyclic groups

## Finding

Let \(A\) be a finite abelian group, let \(y\in A\) have order \(2\), and put
\[
Y=\langle y\rangle,
\qquad
Q=A/Y.
\]
Let
\[
G=\operatorname{Dic}(A,y)
=
\langle A,\gamma\mid \gamma^2=y,\ \gamma^{-1}a\gamma=a^{-1}\text{ for every }a\in A\rangle.
\]
Write
\[
\ell(A)=|L(A)|
\]
for the number of subgroups of \(A\), and
\[
c(A)=|L_1(A)|
\]
for the number of cyclic subgroups of \(A\). Define
\[
\Omega(Q)=\sum_{B\le Q}|Q:B|
\]
and
\[
\Xi(Q)=
\sum_{B,C\le Q}
|Q:B\cap C|\,
\bigl|(Q/(B+C))[2]\bigr|,
\]
where \(X[2]=\{x\in X:2x=0\}\) denotes the \(2\)-torsion subgroup of an abelian group \(X\).

Then the subgroup commutativity degree is
\[
\boxed{
\operatorname{sd}(G)
=
\frac{
\ell(A)^2+2\ell(A)\Omega(Q)+\Xi(Q)
}{
(\ell(A)+\Omega(Q))^2
}.
}
\]
The cyclic subgroup commutativity degree is
\[
\boxed{
\operatorname{csd}(G)
=
\frac{
c(A)^2+2c(A)|Q|+|Q|\,|Q[2]|
}{
(c(A)+|Q|)^2
}.
}
\]

The structural core is an exact parametrization and permutability criterion. Every subgroup of \(G\) outside \(A\) is uniquely
\[
H(B,x)=\langle B,x\gamma\rangle,
\qquad
Y\le B\le A,
\qquad
x\in A/B.
\]
For two such subgroups,
\[
H(B,x)H(C,z)=H(C,z)H(B,x)
\]
holds if and only if
\[
(xz^{-1})^2\in BC.
\]

These formulas apply to every finite abelian kernel, including elementary abelian \(2\)-groups, cyclic kernels, and arbitrary mixed-primary kernels.

## Assumptions and scope

The subgroup commutativity degree of a finite group \(H\) is
\[
\operatorname{sd}(H)
=
\frac{
|\{(U,V)\in L(H)^2:UV=VU\}|
}{|L(H)|^2}.
\]
The cyclic subgroup commutativity degree is defined by restricting to the poset \(L_1(H)\) of cyclic subgroups.

The generalized dicyclic presentation assumes only that \(A\) is finite abelian and that \(y\) has order \(2\). If \(A\) has exponent \(2\), inversion is trivial and \(G\) is abelian; the formulas still give \(1\) for both degrees.

The displayed subgroup formula is an exact finite lattice formula. It does not further compress the double sum \(\Xi(Q)\) into a single product in the invariant factors of \(A\). Such a compression is a separate enumeration problem for finite abelian subgroup lattices.

## Proof

Every subgroup of \(A\) is normal in \(G\). Indeed, conjugation by elements of \(A\) fixes it because \(A\) is abelian, while conjugation by \(\gamma\) acts by inversion and hence preserves every subgroup of \(A\).

Now let \(H\le G\) with \(H\not\le A\). Put
\[
B=H\cap A.
\]
Choose \(x\gamma\in H\setminus A\). Since
\[
(x\gamma)^2=y,
\]
we have \(Y\le B\). Because \(A\) has index \(2\) in \(G\), the image of \(H\) in \(G/A\) has order \(2\), and therefore
\[
H=B\sqcup x\gamma B
=
\langle B,x\gamma\rangle.
\]
Conversely, for every \(B\) with \(Y\le B\le A\) and every \(x\in A\), the set
\[
B\sqcup x\gamma B
\]
is a subgroup: the element \(x\gamma\) normalizes \(B\) by inversion and has square \(y\in B\). Two such subgroups with the same \(B\) are equal exactly when the parameters lie in the same coset of \(B\). Thus the subgroups outside \(A\) are parametrized by pairs
\[
(B,xB),
\qquad
Y\le B\le A,
\qquad
xB\in A/B.
\]
Consequently
\[
|L(G)|
=
\ell(A)+\sum_{Y\le B\le A}|A:B|.
\]
Under the correspondence theorem, subgroups of \(A\) containing \(Y\) are the preimages of subgroups of \(Q=A/Y\), and the index is preserved. Hence
\[
|L(G)|=\ell(A)+\Omega(Q).
\]

It remains to count permuting pairs of subgroups outside \(A\). Let
\[
H=H(B,x),
\qquad
K=H(C,z),
\]
and put
\[
D=BC.
\]
Since \(Y\le B\cap C\), the element \(y\) lies in \(D\). Using
\[
\gamma a\gamma=a^{-1}y
\]
for \(a\in A\), direct multiplication gives
\[
HK
=
D\ \cup\ xD\gamma\ \cup\ zD\gamma\ \cup\ xz^{-1}D
\]
and
\[
KH
=
D\ \cup\ xD\gamma\ \cup\ zD\gamma\ \cup\ zx^{-1}D.
\]
Therefore
\[
HK=KH
\]
if and only if
\[
D\cup xz^{-1}D=D\cup zx^{-1}D.
\]
This is equivalent to
\[
(xz^{-1})^2\in D=BC.
\]

Fix \(B,C\). The map
\[
A/B\times A/C\longrightarrow A/BC,
\qquad
(xB,zC)\longmapsto xz^{-1}BC
\]
is a surjective homomorphism. Every fiber has size
\[
\frac{|A:B|\,|A:C|}{|A:BC|}
=
|A:B\cap C|.
\]
The permutability condition says precisely that the image lies in
\[
(A/BC)[2].
\]
Hence the number of ordered permuting pairs with these fixed intersections \(B,C\) is
\[
|A:B\cap C|\,|(A/BC)[2]|.
\]
Passing to \(Q=A/Y\) gives exactly the summand defining \(\Xi(Q)\).

All ordered pairs with at least one subgroup contained in \(A\) permute, because every subgroup of \(A\) is normal. There are
\[
\ell(A)^2+2\ell(A)\Omega(Q)
\]
such ordered pairs. Adding the outside-outside contribution \(\Xi(Q)\) and dividing by \(|L(G)|^2\) proves the subgroup formula.

For cyclic subgroups, every element outside \(A\) has square \(y\), hence has order \(4\). Its cyclic subgroup is
\[
\langle x\gamma\rangle
=
Y\sqcup x\gamma Y.
\]
Thus the cyclic subgroups outside \(A\) are exactly the subgroups \(H(Y,x)\), parametrized by
\[
xY\in Q,
\]
so there are \(|Q|\) of them. Applying the preceding permutability criterion with \(B=C=Y\), two such cyclic subgroups permute exactly when
\[
(xz^{-1})Y\in Q[2].
\]
For each element of \(Q[2]\), there are exactly \(|Q|\) ordered pairs with that difference. Hence the number of permuting ordered pairs of outside cyclic subgroups is
\[
|Q|\,|Q[2]|.
\]
Adding the pairs involving cyclic subgroups contained in \(A\) gives the claimed formula for \(\operatorname{csd}(G)\).

## Verification

The included replay constructs generalized dicyclic groups directly from finite abelian kernels, enumerates their complete subgroup lattices and cyclic-subgroup posets, tests the condition \(HK=KH\) for every ordered pair, and compares the brute-force degrees with the two formulas above.

The tested kernels include
\[
C_4,
\quad
C_6,
\quad
C_8,
\quad
C_2\times C_2,
\quad
C_2\times C_4,
\quad
C_2\times C_6,
\]
with multiple choices of the distinguished involution when available.

The replay also checks the classical dicyclic specializations
\[
\operatorname{sd}(\operatorname{Dic}_{12})=\frac{29}{32},
\qquad
\operatorname{csd}(\operatorname{Dic}_{12})=\frac{43}{49},
\]
\[
\operatorname{sd}(\operatorname{Dic}_{16})=\frac{113}{121},
\qquad
\operatorname{csd}(\operatorname{Dic}_{16})=\frac78,
\]
and the published generalized examples
\[
\operatorname{sd}(\operatorname{Dic}(C_2\times C_6,y))=\frac{215}{242}
\]
for the relevant involutions, together with the \(C_2\times Q_{16}\) specialization
\[
\operatorname{sd}=\frac{333}{361},
\qquad
\operatorname{csd}=\frac78.
\]
The checker returns `VERIFY_OK`.

Finite enumeration is not used to prove the universal formulas.

## Relationship to prior work

Lazorec and Tărnăuceanu introduced the exact problem addressed here. Their first public version restricts explicit generalized-dicyclic calculations to selected kernels and states as Problem 5.5 the task of computing both commutativity degrees when the abelian kernel is arbitrary. Their ordinary dicyclic formulas and their formulas for \(C_2\times C_n\) agree with the specializations of the theorem above.

The same source reduces its nonabelian subgroup comparisons to dihedral quotients in the cyclic and \(C_2\times C_n\) cases. The new step here is a uniform parametrization for every abelian kernel and the exact quotient criterion
\[
(xz^{-1})^2\in BC,
\]
whose counting introduces the \(2\)-torsion factor
\[
|(Q/(B+C))[2]|.
\]
This factor is invisible in the generalized-dihedral analogue and is exactly what accounts for quaternionic phenomena such as distinct order-four subgroups permuting in \(Q_8\).

A later paper on pronormal subgroups of dicyclic groups cites the 2021 publication but studies pronormality and semimodularity of subgroup lattices rather than subgroup-permutability probabilities. Targeted searches under generalized-dicyclic, subgroup-permutability, arbitrary-abelian-kernel, and cyclic-subgroup-commutativity terminology did not locate the formulas above.

## Limitations

The subgroup formula is expressed as a finite sum over the subgroup lattice of \(Q=A/\langle y\rangle\). Although exact and directly computable, it is not a closed invariant-factor product formula for \(\Xi(Q)\).

The theorem concerns generalized dicyclic groups only. It does not classify all finite groups having the same subgroup commutativity degree or cyclic subgroup commutativity degree.

The main residual risk is bibliographic: an equivalent arbitrary-kernel formula could exist under different notation for generalized dicyclic groups or in unindexed literature.

## References

1. M.-S. Lazorec and M. Tărnăuceanu, “On some probabilistic aspects of (generalized) dicyclic groups,” arXiv:1612.01967v1, 6 December 2016; later published in *Quaestiones Mathematicae* 44 (2021), 129–146, DOI 10.2989/16073606.2019.1673498.
2. S. Mitkari and V. Kharat, “On the lattice of pronormal subgroups of dicyclic, alternating and symmetric groups,” *Mathematica Bohemica* 149 (2024), 427–438, DOI 10.21136/MB.2023.0146-22.
