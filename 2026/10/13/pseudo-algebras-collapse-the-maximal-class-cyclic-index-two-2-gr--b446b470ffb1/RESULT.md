# Pseudo-algebras collapse the maximal-class cyclic-index-two 2-groups

## Finding

For every integer
\[
m\ge4,
\]
let
\[
D_{2^m},\qquad Q_{2^m},\qquad SD_{2^m},\qquad M_{2^m}
\]
denote respectively the dihedral, generalized quaternion, semidihedral, and modular maximal-cyclic groups of order \(2^m\).

Then the three maximal-class families have exactly the same group pseudo-algebra:
\[
\boxed{
C(D_{2^m})
=
C(Q_{2^m})
=
C(SD_{2^m})
=
\{(1,1),(2,3)\}
\cup
\{(2^j,2^{j-2}):2\le j\le m-1\}.
}
\]

The modular family has
\[
\boxed{
C(M_{2^m})
=
\{(1,1),(2,3)\}
\cup
\{(2^j,2^j):2\le j\le m-2\}
\cup
\{(2^{m-1},2^{m-3})\}.
}
\]

Consequently, among the four standard nonabelian \(2\)-groups of order \(2^m\) with a cyclic subgroup of index \(2\), the pseudo-algebra takes exactly two values:
\[
\boxed{
D_{2^m},\ Q_{2^m},\ SD_{2^m}
\text{ collide, while }
M_{2^m}
\text{ is separated.}
}
\]

In either value, the largest codegree is
\[
2^{m-1}.
\]
Therefore the pseudo-algebra determines the group order \(2^m\) inside this four-family class, but it does not distinguish the three pairwise nonisomorphic maximal-class groups.

## Assumptions and scope

For a finite group \(G\) and
\[
\chi\in\operatorname{Irr}(G),
\]
the character codegree is
\[
\operatorname{cod}(\chi)
=
\frac{|G:\ker\chi|}{\chi(1)}.
\]
The group pseudo-algebra is
\[
C(G)
=
\{(d,m_G(d)):d\in\operatorname{Cod}(G)\},
\]
where \(m_G(d)\) is the number of irreducible characters of codegree \(d\).

The notation is normalized so that every group in the theorem has order \(2^m\), and its cyclic subgroup of index \(2\) has order
\[
N=2^{m-1}.
\]

The theorem classifies these four named cyclic-index-two families. It does not assert that an arbitrary finite \(2\)-group sharing one of the displayed pseudo-algebras must belong to the same family.

## Proof

Put
\[
N=2^{m-1}
\]
and let
\[
A=\langle a\rangle\cong C_N
\]
be the cyclic subgroup of index \(2\).

For
\[
0\le k<N,
\]
let
\[
\lambda_k(a)=\zeta_N^k.
\]
If conjugation by an element outside \(A\) sends
\[
a\mapsto a^r,
\]
then
\[
\lambda_k\mapsto\lambda_{rk}.
\]

Whenever \(\lambda_k\) is not invariant, Clifford theory gives one irreducible character
\[
\chi_k=\operatorname{Ind}_A^G\lambda_k
\]
of degree \(2\) for the two-element orbit
\[
\{\lambda_k,\lambda_{rk}\}.
\]
The induced character vanishes outside \(A\). Since \(r\) is a unit modulo \(N\),
\[
\ker\lambda_k=\ker\lambda_{rk},
\]
so
\[
\ker\chi_k=\ker\lambda_k.
\]
Therefore
\[
\operatorname{cod}(\chi_k)
=
\frac{2N/|\ker\lambda_k|}{2}
=
\frac{N}{|\ker\lambda_k|}
=
\operatorname{ord}(\lambda_k).
\]

For the dihedral group,
\[
r=-1.
\]
For the semidihedral group,
\[
r=2^{m-2}-1.
\]
In both cases
\[
\gcd(N,r-1)=2.
\]
For the generalized quaternion group, the conjugation action on \(A\) is again inversion. Thus in all three maximal-class families the only invariant \(\lambda_k\) are
\[
\lambda_0
\quad\text{and}\quad
\lambda_{N/2}.
\]
They account for four linear irreducible characters, and the abelianization is
\[
C_2\times C_2.
\]
Hence the linear codegrees are \(1\) once and \(2\) three times.

Every character of \(A\) of order
\[
2^j,
\qquad
2\le j\le m-1,
\]
is noninvariant. There are
\[
\varphi(2^j)=2^{j-1}
\]
such characters, paired into two-element conjugation orbits. Therefore there are
\[
\frac{\varphi(2^j)}2
=
2^{j-2}
\]
degree-\(2\) irreducibles of codegree \(2^j\). This proves the common maximal-class formula.

For the modular maximal-cyclic group,
\[
r=2^{m-2}+1.
\]
The invariance condition
\[
(r-1)k\equiv0\pmod N
\]
holds exactly when \(k\) is even. Thus exactly \(N/2\) characters of \(A\) are invariant, each extending in two ways. Equivalently,
\[
M_{2^m}/M_{2^m}'
\cong
C_{2^{m-2}}\times C_2.
\]

The linear-character codegrees are therefore the element-order multiplicities in this abelianization. There are three elements of order \(2\), and for
\[
2\le j\le m-2
\]
there are
\[
2^{j+1}-2^j
=
2^j
\]
elements of exact order \(2^j\).

The noninvariant \(\lambda_k\) are exactly those with odd \(k\). Each is faithful on \(A\), so every induced degree-\(2\) character has trivial kernel and codegree
\[
2^{m-1}.
\]
There are
\[
2^{m-3}
\]
such irreducibles. This proves the modular formula.

Finally, all four formulas have largest codegree \(2^{m-1}\), so \(m\) and the order \(2^m\) are recovered.

## Verification

The included checker implements the cyclic-index-two orbit calculation directly for all four actions.

For each
\[
4\le m\le12,
\]
it enumerates the characters of
\[
C_{2^{m-1}},
\]
computes the conjugation orbits, and reconstructs the codegree multiplicities.

It also verifies the degree-squared identities. For the maximal-class families,
\[
4+\left(2^{m-2}-1\right)4=2^m.
\]
For the modular family,
\[
2^{m-1}+2^{m-3}4=2^m.
\]

At order \(16\), the checker obtains
\[
C(D_{16})
=
C(Q_{16})
=
C(SD_{16})
=
\{(1,1),(2,3),(4,1),(8,2)\},
\]
while
\[
C(M_{16})
=
\{(1,1),(2,3),(4,4),(8,2)\}.
\]

The checker returns `VERIFY_OK`.

## Relationship to prior work

Moretó introduced the group pseudo-algebra as the multiplicity distribution of character codegrees and asked how much group structure it remembers. Lewis and Yan later showed that equal pseudo-algebras need not force equal group orders in general and developed positive results for restricted \(p\)-group classes.

The semidihedral character table is explicit in the literature on Cayley graphs over semidihedral groups. In the power-of-two specialization relevant here it has four linear characters and the remaining irreducibles have degree \(2\), in agreement with the index-two Clifford derivation above.

A prior calculation for the dihedral and dicyclic families already yields the dihedral–generalized-quaternion collision at powers of \(2\). The new classification here completes the cyclic-index-two picture by adding the semidihedral and modular families and proving that exactly the three maximal-class families collapse to one pseudo-algebra value.

Targeted semantic and literature searches under semidihedral, quasidihedral, modular maximal-cyclic, codegree multiplicity, and group pseudo-algebra formulations did not locate the displayed four-family classification.

## Limitations

The theorem concerns the four standard nonabelian \(2\)-group families with a cyclic subgroup of index \(2\). It does not classify arbitrary \(2\)-groups by pseudo-algebra.

The dihedral–generalized-quaternion collision is already contained in a broader dihedral–dicyclic calculation; the genuinely additional content here is the semidihedral equality and the exact modular contrast completing the four-family classification.

The proof is a short Clifford-theoretic calculation once the four presentations are fixed. An equivalent codegree table may exist in older representation-theoretic literature without the later pseudo-algebra terminology.

Failed searches do not prove novelty.

## References

1. A. Moretó, “Multiplicities of character codegrees of finite groups,” *Bulletin of the London Mathematical Society* 55 (2023), 234–241, first published online 8 September 2022, DOI 10.1112/blms.12724.
2. M. L. Lewis and Q. Yan, “On the group pseudo-algebra of finite groups,” arXiv:2402.12648v1, first public version 20 February 2024; *Comptes Rendus. Mathématique* 362 (2024), 1661–1665, DOI 10.5802/crmath.671. MSC 2020: 20C15, 20D15.
3. T. Cheng, L. Feng, G. Yu, and C. Zhang, “Integral Cayley graphs over semi-dihedral groups,” *Applicable Analysis and Discrete Mathematics* 17 (2023), 334–356, DOI 10.2298/AADM190330001C.
