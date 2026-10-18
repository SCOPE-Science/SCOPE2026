# Exact ternary necklace counts at minimum circular subsequence-universality length

## Finding
Fix the labeled alphabet \(\Sigma=\{0,1,2\}\). A linear word is \(k\)-subsequence universal if every member of \(\Sigma^k\) occurs as an order-preserving (not necessarily contiguous) subsequence. A cyclic word is circularly \(k\)-universal if **one** of its rotations is \(k\)-subsequence universal; the rotation is chosen once, not separately for each pattern. Rotation classes identify cyclic shifts but **not** reversals or alphabet relabelings.

For each integer \(k\ge1\), length \(3k\) is the smallest possible length of a ternary circularly \(k\)-universal word. Let \(L_k\) be the number of *labeled linear representatives* of that length with this circular property, and \(N_k\) the number of their necklaces. Then
\[
L_k=3\cdot6^k-9\cdot2^k+6,
\qquad
N_k=\frac{1}{k}\sum_{d\mid k}\varphi(k/d)\left(6^d-3\cdot2^d+2\right).
\]
Here \(\varphi\) is Euler's totient function. Every admissible word has precisely \(k\) copies of each alphabet letter. If \(A_j\) denotes the class whose cyclic positions can be partitioned into \(k\) three-letter permutation blocks beginning in phase \(j\in\{0,1,2\}\), the admissible class is \(A_0\cup A_1\cup A_2\). The numbers of admissible labeled words belonging to exactly one, two, or three of these phase classes are, respectively,
\[
3\cdot6^k-18\cdot2^k+18,
\qquad 9\cdot2^k-18,
\qquad 6.
\]
Every word in all three classes is a repetition of a length-three permutation. The number of *primitive* admissible necklaces (minimal rotation period equal to \(3k\)) is
\[
P_k=\frac{1}{3k}\sum_{d\mid k}\mu(k/d)\left(3\cdot6^d-9\cdot2^d+6\right),
\]
where \(\mu\) is the Möbius function.

## Assumptions and scope
The alphabet symbols are distinct and fixed; \(k\) ranges over all positive integers. Only circular rotation is quotiented out. A phase-\(j\) block partition means that the triples of positions \(j+3t,j+3t+1,j+3t+2\), interpreted modulo \(3k\) for \(0\le t<k\), all contain each of the three symbols exactly once. For \(k=1\), the three phases coincide as classes; the formulas include this boundary case. The property concerns **one rotation** that is universal for all patterns, following the standard definition of circular subsequence universality.

## Proof
**Step 1: exact minimum-length characterization.** A \(k\)-universal word must contain the scattered constant patterns \(0^k\), \(1^k\), and \(2^k\); thus every symbol occurs at least \(k\) times and the word has length at least \(3k\). The standard arch factorization (also called rich-block factorization) says that \(k\)-universality is equivalent to a concatenation of \(k\) factors, each containing all three letters. For completeness, the forward equivalence follows by greedily ending each block at the first point at which all letters have appeared: if fewer than \(k\) blocks finish, construct an absent length-\(k\) pattern by repeatedly choosing the letter that first finishes a block, then choosing a letter absent from the last incomplete remainder. Conversely, one can select the \(i\)-th letter of any desired length-\(k\) subsequence from the \(i\)-th rich block. At length exactly \(3k\), each rich block is necessarily a permutation of \(\Sigma\). Hence a circularly universal word belongs precisely to \(A_0\cup A_1\cup A_2\).

**Step 2: phase intersections.** Each \(A_j\) has \(6^k\) members, since its \(k\) nonoverlapping triples are arbitrary permutations. In \(A_0\cap A_1\), the shifted triple \((w_{3t+1},w_{3t+2},w_{3t+3})\) must be a permutation. Since \((w_{3t},w_{3t+1},w_{3t+2})\) is already a permutation, its remaining letter is uniquely \(w_{3t}\); therefore \(w_{3t+3}=w_{3t}\) for all cyclic indices \(t\). Every block starts with one fixed letter, and the remaining two may appear in either order independently; thus \(|A_0\cap A_1|=3\cdot2^k\). Rotational symmetry gives \(|A_i\cap A_j|=3\cdot2^k\) for all distinct phases. Meeting all three phases means that every *consecutive* cyclic triple contains all letters. Comparing overlapping triples forces \(w_{i+3}=w_i\) for every \(i\); there are exactly \(6\) such length-three periodic words. Inclusion-exclusion now yields \(L_k=3\cdot6^k-9\cdot2^k+6\). Using the elementary identities that each word in exactly \(j\) phase classes contributes \(j\) single-class incidences and \(\binom j2\) pair incidences gives the displayed exact-one/two/three counts.

**Step 3: rotations and primitive periods.** If a valid word is fixed by a rotation through \(r\) positions with \(3\nmid r\), its phase class is carried successively through all three different phases by multiples of this rotation. It therefore belongs to all three phase classes, so it has period three with three different letters. Such a word cannot be fixed by a nonmultiple-of-three rotation: a contradiction. Hence these rotations have no fixed valid words. If \(r=3j\), with \(0\le j<k\), a fixed word is a repetition of a base word of length \(3d\), \(d=\gcd(k,j)\) (taking \(\gcd(k,0)=k\)). Because the base length is divisible by three, membership in any phase class for the repeated word is equivalent to membership in that phase class for its base. There are exactly \(L_d\) fixed valid words. Burnside's lemma gives
\[
N_k=\frac{1}{3k}\sum_{j=0}^{k-1}L_{\gcd(k,j)}
=\frac{1}{3k}\sum_{d\mid k}\varphi(k/d)L_d,
\]
which simplifies to the announced necklace formula. Any admissible word has least period divisible by three, as just proved. Every admissible word whose least period is \(3d\), with \(d\mid k\), is the \((k/d)\)-fold repetition of a *primitive* admissible word of length \(3d\). By Möbius inversion the number of primitive labeled words of length \(3k\) is \(\sum_{d\mid k}\mu(k/d)L_d\); division by \(3k\) yields \(P_k\). This proves all assertions, including the one-block case \(k=1\).

## Verification
The independent finite-check script `verify/check.py` enumerates every ternary word of lengths \(3,6,9,12\). At lengths \(3,6,9\), it separately tests the existence of a universal rotation by explicit greedy subsequence search for all \(3^k\) target patterns, rather than assuming the permutation-block characterization. It also counts valid phases, rotation classes, and primitive rotation classes by direct comparison of cyclic rotations. At length \(12\) it tests every word using the exact three-phase condition and independently enumerates necklaces and primitive classes. All comparisons to the closed formulas passed, with the following observed quadruples \((k,L_k,N_k,P_k)\):
\[
(1,6,2,2),\quad(2,78,14,12),\quad(3,582,66,64),\quad(4,3750,320,306).
\]
Run `python3 verify/check.py` using Python 3 and no external dependencies. The proof, not the finite tests, establishes the formulas for every \(k\ge1\).

## Relationship to prior work
Barker, Fleischmann, Harwardt, Manea, and Nowotka (arXiv:2003.04629v1, 2020) introduce circular scattered-factor universality, establish arch characterizations, and study decision and repetition problems. Fleischmann, Germann, and Nowotka (arXiv:2104.09063v1, 2021) study remainder-chain and repetition behavior and circular universality. Adamson (arXiv:2304.04583v1, 2023) develops algorithms for **linear** \(k\)-subsequence universal-word counts, ranking, and unranking. The elementary rich-block premise is common to these papers; the new contribution here is the complete ternary **circular minimum-length phase-intersection classification**, exact labeled and necklace counts, and primitive-necklace count. None of the material read in these three texts directly states these formulas. Their general algorithms can recover finite values after computation but do not themselves state the closed cyclic enumeration. The standard Burnside and Möbius identities are classical and not claimed as new.

## Limitations
The formulas apply only to the **fixed ternary alphabet** at minimum possible length \(3k\), not to larger lengths, larger alphabets, or alphabet-relabeling/dihedral equivalence classes. Computational confirmation is exhaustive only through \(k=4\); for \(k=4\) the independent pattern-by-pattern test was not used. Existing general enumerative frameworks could in principle subsume these finite instances; the claimed contribution is the explicit infinite closed-form cyclic and primitive classification. Novelty remains subject to possible unindexed equivalent results; no independent mathematical audit has been performed.

## References
1. L. Barker, P. Fleischmann, K. Harwardt, F. Manea, D. Nowotka, *Scattered Factor-Universality of Words*, 2020, arXiv:2003.04629v1, https://arxiv.org/html/2003.04629v1 .
2. P. Fleischmann, S. B. Germann, D. Nowotka, *Scattered Factor Universality — The Power of the Remainder*, 2021, arXiv:2104.09063v1, https://arxiv.org/abs/2104.09063 .
3. D. Adamson, *Ranking and Unranking k-Subsequence Universal Words*, 2023, arXiv:2304.04583v1, https://arxiv.org/abs/2304.04583 .
