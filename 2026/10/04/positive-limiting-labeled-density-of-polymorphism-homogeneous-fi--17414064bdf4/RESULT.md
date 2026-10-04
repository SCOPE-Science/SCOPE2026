# Positive limiting labeled density of polymorphism-homogeneous finite abelian groups
## Finding
Let \(p\) be a prime and \(a\ge 1\). Among all abelian group laws on a fixed labeled set of cardinality \(p^a\), the exact proportion that are polymorphism-homogeneous is
\[
\rho_p(a)=\sum_{m\mid a}p^{-(m-1)a}\prod_{j=m+1}^a(1-p^{-j}).
\]
In particular,
\[
\lim_{a\to\infty}\rho_p(a)=\prod_{j=2}^\infty(1-p^{-j})>0.
\]
More generally, if \(n=\prod_p p^{a_p}\), then the proportion among all labeled abelian group laws of order \(n\) is \(\prod_{p\mid n}\rho_p(a_p)\).

Equivalently, the number of polymorphism-homogeneous abelian group laws on a labeled \(n\)-element set is
\[
n!\prod_{p^a\parallel n}\left(\sum_{m\mid a}\frac{p^{-ma}}{\prod_{j=1}^m(1-p^{-j})}\right).
\]
For example, for \(p=2\), the first six proportions are
\[
1,\ 1,\ \frac{43}{64},\ \frac{2731}{4096},\ \frac{624961}{1048576},\ \frac{643318201}{1073741824},
\]
and the limiting value is approximately \(0.577576190173205\).

## Assumptions and scope
A finite algebra \((A,+)\) is called polymorphism-homogeneous in the sense used by Tóth and Waldhauser: every homomorphism from a finitely generated subalgebra of a finite power of \(A\) to \(A\) extends to a homomorphism on the whole power. Their classification states that a finite abelian group has this property exactly when every Sylow subgroup is homocyclic. The present result counts labeled abelian group laws, not isomorphism classes. Two operations on the same label set are counted separately unless the identity permutation is an isomorphism between them.

## Proof
Tóth and Waldhauser prove that a finite abelian group is polymorphism-homogeneous exactly when each Sylow subgroup is homocyclic. For a fixed abstract finite group \(G\) of order \(N\), the number of group laws on a fixed \(N\)-element label set that are isomorphic to \(G\) is \(N!/|\operatorname{Aut}(G)|\), by orbit-stabilizer for the relabeling action of the symmetric group.

Fix \(p\) and \(a\). A homocyclic abelian group of order \(p^a\) has the form
\[
G_m=(\mathbb Z/p^{a/m}\mathbb Z)^m
\]
for a unique divisor \(m\mid a\). Its automorphism group is \(\operatorname{GL}_m(\mathbb Z/p^{a/m}\mathbb Z)\). Reduction modulo \(p\) is onto \(\operatorname{GL}_m(\mathbb F_p)\), with kernel of size \(p^{m^2(a/m-1)}\). Hence
\[
|\operatorname{Aut}(G_m)|
=p^{ma}\prod_{j=1}^m(1-p^{-j}).
\]
Therefore the reciprocal-automorphism mass of the homocyclic groups of order \(p^a\) is
\[
Q_p(a)=\sum_{m\mid a}\frac{p^{-ma}}{\prod_{j=1}^m(1-p^{-j})}.
\]

The classical Hall--Cohen--Lenstra mass identity, equivalently the \(q\)-binomial coefficient identity for the generating function of finite abelian \(p\)-groups, gives the total reciprocal-automorphism mass at order \(p^a\):
\[
W_p(a)=\sum_{|G|=p^a}\frac1{|\operatorname{Aut}(G)|}
=\frac{p^{-a}}{\prod_{j=1}^a(1-p^{-j})}.
\]
Thus the labeled proportion is \(Q_p(a)/W_p(a)\), because the common factor \((p^a)!\) cancels. Multiplying and simplifying gives
\[
\rho_p(a)=\sum_{m\mid a}p^{-(m-1)a}\prod_{j=m+1}^a(1-p^{-j}).
\]

For a general order \(n=\prod_p p^{a_p}\), the Sylow decomposition is unique and automorphism groups split as products across distinct primes. Both the total reciprocal-automorphism mass and the homocyclic-Sylow mass therefore factor over primes, proving the multiplicative formula.

For the limit, the divisor \(m=1\) contributes exactly \(\prod_{j=2}^a(1-p^{-j})\). Every other divisor satisfies \(m\ge2\), so the sum of the remaining terms is at most \(\tau(a)p^{-a}\), where \(\tau(a)\) is the divisor-counting function. Hence those terms vanish, while the finite product converges to \(\prod_{j=2}^\infty(1-p^{-j})\).

## Verification
The accompanying `verify.py` independently enumerates partitions of \(a\), computes automorphism orders of all abelian \(p\)-groups from the standard partition formula, and checks the Hall mass formula against that direct sum for \(p\in\{2,3,5,7}\) and \(1\le a\le8\). It separately computes the homocyclic mass from the \(\operatorname{GL}_m\) formula, checks the displayed density formula, verifies integrality of labeled counts in all tested cases with at most 256 labels, and checks the explicit remainder bound through \(a=24\). The script returns `VERIFY_OK`.

## Relationship to prior work
Tóth and Waldhauser supply the decisive structural classification: polymorphism-homogeneity for finite abelian groups is equivalent to all Sylow subgroups being homocyclic. That classification is prior and is not claimed here. The reciprocal-automorphism weighting and its total mass are likewise classical Hall--Cohen--Lenstra material. The new statement is the synthesis of these two ingredients into an exact labeled density for the polymorphism-homogeneous subclass, together with the positive limiting constant at fixed prime.

Targeted searches for combinations of “polymorphism-homogeneous finite abelian groups”, “homocyclic”, “reciprocal automorphism”, “labeled group laws”, and “Cohen--Lenstra” located the classification and standard mass literature, but no source stating the exact formula for \(\rho_p(a)\), its prime-factor product for general \(n\), or the limit \(\prod_{j=2}^\infty(1-p^{-j})\) for this model-theoretic subclass.

## Limitations
The originality conclusion is literature-search based rather than a formal priority guarantee. The asymptotic statement holds with the prime \(p\) fixed and \(a\to\infty\); no uniform two-parameter asymptotic in \(p\) and \(a\) is claimed. The result counts labeled group laws with the reciprocal-automorphism weighting naturally induced by relabeling; it does not describe the unweighted proportion of isomorphism classes that are homocyclic.

## References
1. E. Tóth and T. Waldhauser, “Polymorphism-homogeneity and universal algebraic geometry,” arXiv:2007.04405, first posted 2020-07-08; Discrete Mathematics & Theoretical Computer Science 23(2), 2022. Theorem 4.7 gives the homocyclic-Sylow classification.
2. P. Majumder, “An elementary proof of a power series identity for the weighted sum of all finite abelian p-groups,” arXiv:1407.3066, 2014. The paper records the classical reciprocal-automorphism mass identity originating with Cohen and Lenstra.
3. H. Cohen and H. W. Lenstra Jr., “Heuristics on class groups of number fields,” Lecture Notes in Mathematics 1068, Springer, 1984, pp. 33--62.
