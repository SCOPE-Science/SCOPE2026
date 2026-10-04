# A parity classification of just-infinite generalized Chein doubles over the infinite cyclic group

## Finding
Let \(G=\langle a\rangle\cong\mathbb Z\). For every admissible generalized Chein triple \((G,*,g_0)\), the double \(M(G,*,g_0)\) is just-infinite exactly in the following cases:

- \(a^*=a^{{-1}}\), in which case admissibility forces \(g_0=1\);
- \(a^*=a\) and \(g_0=a^k\) with \(k\) odd.

In the first case the double is the infinite dihedral group. In the second case one has
\[
M(G,*,g_0)\cong \mathbb Z\oplus \mathbb Z/\gcd(2,k)\mathbb Z.
\]
Hence an identity-involution triple with even \(k\) gives \(M(G,*,g_0)\cong\mathbb Z\oplus C_2\), which is not just-infinite. This completely answers the generalized-double loop-level question for the infinite cyclic base group.

## Assumptions and scope
The generalized Chein construction is the one in arXiv:2609.21016v1: \(G\) is a group, \(*\) is an involutory anti-automorphism, \(g_0\in Z(G)\), \(g_0^*=g_0\), and \(gg^*\in Z(G)\) for every \(g\in G\). The multiplication on \(G\sqcup Gu\) is
\[
gh=gh,\qquad g(hu)=(hg)u,\qquad (gu)h=(gh^*)u,\qquad (gu)(hu)=g_0h^*g.
\]
The claim is restricted to the base group \(G\cong\mathbb Z\). It does not classify generalized doubles of other just-infinite groups.

## Proof
Because \(G\) is abelian, an anti-automorphism is simply an automorphism. Since \(\operatorname{{Aut}}(\mathbb Z)=\{{1,-1}\}\), an involutory anti-automorphism has exactly two possibilities on the generator: \(a^*=a\) or \(a^*=a^{{-1}}\).

Suppose first that \(a^*=a^{{-1}}\). Write \(g_0=a^k\). The admissibility condition \(g_0^*=g_0\) gives \(a^{{-k}}=a^k\), hence \(2k=0\). Since \(\mathbb Z\) is torsion-free, \(k=0\), so \(g_0=1\). The construction is then the standard Chein double \(M(G,2)\). Theorem 4.1 of arXiv:2609.21016v1 states that \(M(G,2)\) is just-infinite if and only if \(G\) is just-infinite. The infinite cyclic group is just-infinite because each nontrivial subgroup has finite index. Thus this double is just-infinite; explicitly it is \(D_\infty\).

Now suppose that \(a^*=a\). Every \(g_0=a^k\) is admissible. The multiplication rules give \(ua=au\) and \(u^2=a^k\). Conversely, these relations reproduce all four generalized Chein multiplication rules on the normal forms \(a^n\) and \(a^nu\). Therefore
\[
M(G,*,a^k)\cong \langle a,u\mid [a,u]=1,\ u^2=a^k\rangle.
\]
In additive notation this is \(\mathbb Z^2/\langle(-k,2)\rangle\). Smith normal form of the one-row relation matrix \((-k,2)\) gives
\[
\mathbb Z^2/\langle(-k,2)\rangle\cong \mathbb Z\oplus \mathbb Z/\gcd(2,k)\mathbb Z.
\]
If \(k\) is odd, the torsion factor is trivial, so the double is infinite cyclic and hence just-infinite. If \(k\) is even, the double is \(\mathbb Z\oplus C_2\). Its subgroup \(\{{0}\}\oplus C_2\) is nontrivial, normal, finite, and therefore has infinite index, so the double is not just-infinite. This proves the classification.

## Verification
The proof uses only the two automorphisms of \(\mathbb Z\), the displayed generalized Chein multiplication, Theorem 4.1 for the standard inversion case, and the Smith normal form of the relation vector \((-k,2)\). The crucial boundary cases are explicit: \(k=0\) yields \(\mathbb Z\oplus C_2\), while \(k=1\) yields an infinite cyclic group. No finite computation is used as a substitute for an infinite-group argument.

## Relationship to prior work
Paiva's arXiv:2609.21016v1 introduces the just-infinite comparison for generalized Chein doubles, proves the loop-level equivalence for the standard Chein construction, proves an algebra-level generalized result under a nonabelian hypothesis, and then asks in Question 9.2 which admissible triples satisfy the loop-level equivalence. The present result resolves that question completely for the basic just-infinite abelian group \(\mathbb Z\), including both possible involutions and every admissible central parameter.

Kinyon, Phillips, and Vojtěchovský's 2005 paper develops generalized index-two constructions of Bol-Moufang type, including the generalized Chein framework. It predates the just-infinite question and does not state the parity classification above.

## Limitations
The result is a complete classification only for the infinite cyclic base group. It does not imply a criterion for arbitrary abelian, polycyclic, or nonabelian just-infinite groups. Literature searches cannot prove absolute novelty, although the motivating 2026 paper explicitly leaves the generalized loop-level problem open and the inspected earlier construction paper does not address just-infiniteness.

## References
1. T. F. V. Paiva, *Just-Infinite Loops and Loop Algebras*, arXiv:2609.21016v1, 17 September 2026; especially Section 6, Theorem 4.1, and Question 9.2.
2. M. K. Kinyon, J. D. Phillips, and P. Vojtěchovský, *Loops of Bol-Moufang type with a subgroup of index two*, arXiv:math/0506085, 2005.
