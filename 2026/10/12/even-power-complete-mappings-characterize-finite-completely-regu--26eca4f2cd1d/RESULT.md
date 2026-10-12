# Even-power complete mappings characterize finite completely regular semigroups

## Finding

Let \(S\) be any nonempty finite semigroup. For an integer \(k\geq 1\), a **\(k\)-complete mapping** is a permutation \(\alpha:S\to S\) such that the map \(\theta:S\to S\), given by \(\theta(x)=x(\alpha(x))^k\), is also a permutation. Then:

1. For every integer \(k\geq2\), existence of a \(k\)-complete mapping forces \(S\) to be **completely regular** (a union of subgroups).
2. For every **even** integer \(k\geq2\), this condition is also sufficient. Therefore
   \[
   S\text{ admits a }k\text{-complete mapping}\quad\Longleftrightarrow\quad S\text{ is completely regular}\qquad(k\geq2\text{ even}).
   \]
3. The sufficiency is constructive: let \(E\) be the least common multiple of the exponents of the maximal subgroups of \(S\), taking \(E=1\) when all are trivial. There exists a positive integer \(a\) with \(\gcd(a,E)=\gcd(1+ka,E)=1\). The pointwise power permutation \(\alpha(x)=x^a\) has \(\theta(x)=x^{1+ka}\). For \(k=2\), one may simply take the inverse of each element in its own subgroup.

The restriction to even exponents is substantive: the group of order two has no \(k\)-complete mapping for any odd \(k\). The restriction \(k\geq2\) is also substantive: usual complete mappings (\(k=1\)) may exist in finite semigroups which are regular but not completely regular.

## Assumptions and scope

The product in \(S\) is associative; neither commutativity nor an identity is required. All maps act on the underlying finite set. The **principal left ideal** of \(y\) means \(S^1y\), where \(S^1\) is obtained by adjoining an identity when necessary. Write \(z\leq_{\mathcal L}y\) if \(z\in S^1y\), and \(z\mathrel{\mathcal L}y\) if their principal left ideals agree. A **completely regular** semigroup is one in which every element belongs to a subgroup whose identity is an idempotent of \(S\). Powers \(x^a\) are evaluated within the associative semigroup, not in an ambient group assumed in advance.

## Proof

**Necessity for every \(k\geq2\).** Suppose \(\alpha\) and \(\theta\) are permutations and define another permutation \(F=\theta\circ\alpha^{-1}\). For \(y\in S\), put \(x=\alpha^{-1}(y)\); then
\[
F(y)=xy^k\in S^1y^k\subseteq S^1y^2\subseteq S^1y.
\]
Therefore \(F(y)\leq_{\mathcal L}y^2\leq_{\mathcal L}y\). Every element lies on a finite cycle of \(F\); along that cycle the principal left ideals weakly descend and return to their starting ideal. Hence \(F(y)\mathrel{\mathcal L}y\). The sandwiching forces \(y^2\mathrel{\mathcal L}y\), so there is \(u\in S^1\) with \(y=uy^2\). Induction gives \(y=u^{N-1}y^N\) for every positive integer \(N\). Choose \(N\geq2\) for which \(e=y^N\) is idempotent, possible in every finite cyclic subsemigroup. Then \(y=u^{N-1}e\), and hence \(ye=y\). Since \(e\) is a power of \(y\), it commutes with \(y\), so \(ey=y\). Thus \(y\) lies in the local monoid \(eSe\), and \(y^{N-1}\in eSe\) is its two-sided inverse because \(y^N=e\). Since \(y\) was arbitrary, every element of \(S\) lies in a subgroup. This proves necessity without assuming regularity.

**Sufficiency for every even \(k\geq2\).** A finite completely regular semigroup is partitioned by its maximal subgroups, one through each element. Let \(E\) be the least common multiple of their group exponents. For every prime \(p\mid E\), choose a residue \(a_p\bmod p\) excluding both \(0\) and, when \(p\nmid k\), the residue \(-k^{-1}\bmod p\). If \(p\mid k\), any nonzero residue works; if \(p\nmid k\), then \(p\) is odd because \(k\) is even, and at least one residue survives the two exclusions. The Chinese remainder theorem gives an integer \(a\) realizing these residues simultaneously. Adding a suitable multiple of their product makes \(a>0\). Therefore both \(a\) and \(1+ka\) are coprime to \(E\). On each maximal subgroup the maps \(x\mapsto x^a\) and \(x\mapsto x^{1+ka}\) are bijections, their inverse power maps being furnished by multiplicative inverses modulo its exponent. As the maximal subgroups partition \(S\), both maps are permutations of all of \(S\); associativity gives \(x(x^a)^k=x^{1+ka}\). Thus \(\alpha(x)=x^a\) is \(k\)-complete.

**Sharp parity boundary.** In the two-element cyclic group \(C_2\), every odd power fixes every element. For odd \(k\), a candidate \(\theta(x)=x\alpha(x)\) is constant for either permutation \(\alpha\) of \(C_2\), and is never bijective. For \(k=2\) the subgroupwise inverse map is a permutation and satisfies \(x(\alpha(x))^2=\alpha(x)\), so no subgroup-order parity hypothesis is needed.

## Verification

The standalone `verify.py` uses only the Python standard library. Execute `python3 verify.py` from the extracted package. It enumerates all associative multiplication tables on one, two, or three labeled elements (respectively 1, 8, 113 tables), exhaustively checks candidate \(k\)-complete mappings for \(k\in\{2,4,6\}\), checks necessity at \(k=3\), verifies power-permutation witnesses on every completely regular table, includes matrix-unit semigroups and an odd-exponent cyclic-group obstruction, and checks 900 modular arithmetic parameter pairs for the explicit construction. The terminal confirmation is `ASSOCIATIVE_TOTAL 122 COMPLETELY_REGULAR 57 ODD_THREE_COMPLETE 43 CRT_CASES 900 VERIFY_OK`. Enumeration is a corroborating finite test, not a proof of the universal quantifiers; the preceding argument supplies the general proof.

## Relationship to prior work

Araújo, Bentz, Cameron, Hendrey, and Kinyon (2026) introduce \(k\)-complete mappings in Definition 15.1 and ask for their existence classification in Problem 15.8. Their Theorem 2.1 proves regularity for the original \(k=1\) notion. They also obtain completely regularity conclusions under extra hypotheses for other \(k=1\) mapping notions (including their Sections 11 and 13). Neither their original-mapping results nor their stated open problem gives the all-finite-semigroup obstruction for \(k\geq2\), the complete even-\(k\) converse, or the uniform power-map witness here. In particular, regularity is strictly weaker than the necessity conclusion here. The present theorem resolves the even-exponent part of their finite classification problem for the class of **all** finite semigroups.

## Limitations

This does not classify which completely regular semigroups admit an odd-\(k\) complete mapping; the two-element group shows the unconditional converse is false in those exponents. It does not establish analogous claims for infinite semigroups. The proof is a mathematical derivation without independent external certification. Equivalent earlier results using alternative terminology may exist and warrant continued bibliographic checking.

## References

Araújo, J., Bentz, W., Cameron, P. J., Hendrey, K., and Kinyon, M., *Complete Mappings of Semigroups*, arXiv:2608.25092v1, submitted 25 August 2026, especially Definition 15.1, Problem 15.8, Theorems 2.1, 11.2, and 13.1. https://arxiv.org/abs/2608.25092
