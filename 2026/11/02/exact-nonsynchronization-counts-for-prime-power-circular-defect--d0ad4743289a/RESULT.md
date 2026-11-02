# Exact nonsynchronization counts for prime-power circular defect-one automata

## Finding

Let \(p\) be prime, let \(k\geq2\), and put \(n=p^k\). On the state set \(Q=\mathbb Z/n\mathbb Z\), fix a letter \(a\) acting by \(a(x)=x+1\pmod n\). Let \(b:Q\to Q\) range over **all labeled transformations of rank \(n-1\)**. A binary deterministic automaton \((Q,a,b)\) is *synchronizing* if some finite word in its two letters maps all states to one state.

Write \(E_{p,k}\) for the exact number of transformations \(b\) for which this automaton is **not** synchronizing. For a nonempty set of levels \(J=\{j_1<\cdots<j_t\}\subseteq\{1,\ldots,k-1\}\), put \(j_0=0\), \(L_J=p^{j_t}\), \(m_J=p^{k-j_t}\), and

\[
G_p(J)=\prod_{i=1}^{t}\left((p^{j_i-j_{i-1}})!\right)^{p^{j_{i-1}}}.
\]

Then the exact, finite, all-prime-power formula is

\[
\boxed{E_{p,k}=\sum_{\varnothing\ne J\subseteq\{1,\ldots,k-1\}}(-1)^{|J|+1}\,G_p(J)\,L_J\,(m_J!)^{L_J}\binom{m_J}{2}.}
\]

There are exactly \(n!\binom n2\) possible rank-\((n-1)\) labeled transformations. Accordingly the probability of nonsynchronization under the uniform choice of such a transformation is \(E_{p,k}/(n!\binom n2)\). In addition, the cyclic state-relabeling action on these transformations is free: the exact number of nonsynchronizing equivalence classes under rotation of all state labels is \(E_{p,k}/n\).

For prime-square orders the expression becomes

\[
E_{p,2}=p\,p!\,(p!)^p\binom p2.
\]

Examples, showing *labeled* nonsynchronizing maps and then their rotation classes, are

| \(n\) | Nonsynchronizing maps | Rotation classes |
|---:|---:|---:|
| 4 | 16 | 4 |
| 8 | 14,848 | 1,856 |
| 9 | 11,664 | 1,296 |
| 16 | 182,285,762,560 | 11,392,860,160 |
| 27 | 30,964,600,730,445,078,528 | 1,146,837,064,090,558,464 |

The eight-state count was already known from an earlier finite census; the contribution here is the *all-prime-power exact formula and its structural derivation*, not that previously observed special case.

## Assumptions and scope

All state labels are fixed residues until rotation classes are explicitly taken. A transformation of rank \(n-1\) has exactly one two-element kernel class and all other kernel classes are singletons. No reachability, completeness, or extra transition restrictions are imposed beyond the two specified deterministic letters. The result concerns the presence of *any* reset word, not its shortest length. The parameters satisfy \(p\) prime and \(k\geq2\); the formula is not asserted here for arbitrary composite orders having two distinct prime factors.

A *congruence* is an equivalence relation on \(Q\) preserved by both letters. It is *nontrivial* when it is neither equality nor the indiscrete relation. Preservation of a congruence alone does not generally prevent synchronization; in the present rank-one-defect setting, its induced quotient action must be a permutation, and that is the operative obstruction.

## Proof

**1. Reduce nonsynchronization to congruence preservation.** Volkov's defect-one primitivity theorem states that a primitive deterministic automaton with a letter of rank \(n-1\) is synchronizing (Corollary 2.4 of the cited work). Therefore a nonsynchronizing automaton of the stated type has a nontrivial congruence. Because the letter \(a\) is the full cyclic permutation, invariance under \(a\) also gives invariance under \(a^{-1}=a^{n-1}\). Such translation-invariant equivalence relations are precisely the coset partitions of subgroups of \(\mathbb Z/n\mathbb Z\). Since \(n=p^k\), the nontrivial choices are exactly congruence modulo \(p^j\), with \(1\le j\le k-1\).

**2. Rank forces quotient permutations.** Suppose a rank-\((n-1)\) map \(b\) preserves congruence modulo \(r=p^j\). Its action on the \(r\) residue classes induces a well-defined function \(\bar b\). Every residue class has \(m=n/r\geq2\) states. If \(\bar b\) were not surjective, the whole missing target residue class would be omitted by \(b\), giving \(\operatorname{rank}(b)\leq n-m\leq n-2\), a contradiction. Hence \(\bar b\) is a permutation. Together with the quotient rotation induced by \(a\), every word permutes the quotient, so no word can map the entire original state set to a singleton. Thus **nonsynchronization is equivalent** to preserving at least one of the \(k-1\) residue congruences.

**3. Count an intersection of congruence conditions.** Fix a nonempty set of preserved levels \(J=\{j_1<\cdots<j_t\}\), let \(L=p^{j_t}\), and let \(m=p^{k-j_t}\). The map \(b\) induces a permutation \(\sigma\) of the \(L\) top-level residue classes. The permutation must preserve the chain of all coarser partitions at levels in \(J\). At the first level one may permute \(p^{j_1}\) blocks; at each further level \(j_i\), each one of the \(p^{j_{i-1}}\) previous blocks has \(p^{j_i-j_{i-1}}\) children that may be freely permuted. Consequently the number of allowed quotient permutations is exactly \(G_p(J)\) as defined above.

For a fixed quotient permutation, each of the \(L\) domain fibers of size \(m\) is mapped into a distinct target fiber of size \(m\). To have total rank \(n-1\), precisely one fiber must contribute rank \(m-1\); the other \(L-1\) fiber maps are bijections. The defective fiber is chosen in \(L\) ways. A map from \(m\) labeled inputs onto exactly \(m-1\) of the \(m\) available labeled outputs has \(m\binom m2(m-1)!=m!\binom m2\) choices: choose the omitted output, the unique colliding input pair, and a bijection of the resulting \(m-1\) kernel classes to the remaining outputs. Each other fiber has \(m!\) choices. Therefore the intersection count is exactly

\[
G_p(J)\,L\,(m!)^L\binom m2.
\]

**4. Inclusion-exclusion.** By Step 2, the failure event is the union of the \(k-1\) congruence-preservation events. Ordinary finite inclusion-exclusion over their nonempty intersections gives the boxed formula with no independence assumption.

**5. Denominator and rotation classes.** Every rank-\((n-1)\) map is specified by its unique unordered colliding pair, followed by an injection from the resulting \(n-1\) kernel classes into the \(n\) output states. This yields \(\binom n2 n!\) maps. If a map \(b\) commuted with a nonidentity rotation \(a^s\), then its image would be invariant under \(a^s\). But the complement of its image is a singleton, and a nonidentity cyclic rotation fixes no state. This is impossible. Thus every cyclic-conjugation orbit has size \(n\), so division by \(n\) is exact.

## Verification

Two independent finite constructions accompany this proof. `formula_check.py` evaluates the full inclusion-exclusion expression in exact integers for several prime powers and separately enumerates small symmetric-group permutations to confirm selected nested-chain permutation counts. `census_check.cpp` enumerates rank-defect-one maps at orders four and eight and decides synchronizability by reverse reachability from diagonal pairs in the two-letter pair automaton. It separately tests preservation of each available residue congruence. It finds 16 and 14,848 nonsynchronizing labeled maps, respectively, with no disagreement between the criteria. The order-eight congruence-event counts are 13,824 modulo two, 1,536 modulo four, with 512 in their intersection.

The finite programs check examples and the supporting combinatorics; the proof for unbounded prime-power orders uses the cited primitive-automaton theorem and the finite intersection count proved above. The two computational methods do not constitute an independent external scientific audit.

## Relationship to prior work

Araújo and Cameron's 2013 study gives the established rank-defect-one synchronization theorem for primitive permutation groups and a structural characterization of imprimitive permutation groups. Volkov's 2024 Corollary 2.4 extends the defect-one synchronization implication to primitive automata without requiring permutation primitivity; this is explicitly **used as prior work**, not claimed as a new theorem. Berlinkov and Nicaud (2018) count failures asymptotically in the different almost-group model, where the exceptional letter restricts to a permutation on all but one state. Aistleitner and collaborators study the high-probability synchronization of random circular automata with an *unconditioned* random second letter; that model and its asymptotic probability estimates do not supply the exact rank-\((n-1)\), prime-power enumeration above.

The earlier available eight-state numerical census already contained the result of 1,856 nonsynchronizing rotational classes. This specific numerical count is not new. The stated finding is the all-prime-power enumerative theorem, including precise intersection corrections for multiple compatible congruence levels and all-order rotational orbit counts. The inspected literature and targeted searches did not locate this particular evaluated formula. A more general unindexed enumerative result could still subsume it.

## Limitations

Only prime-power state counts, a *fixed* full-cycle letter, and a second letter of rank exactly one below full are covered. This does not count automata with arbitrary nonpermutation letters, classify reset thresholds among synchronizing automata, or provide a formula for orders with multiple distinct prime divisors. The central primitive-automaton synchronization implication is cited rather than reproved. Literature searches and accessible sources cannot establish historical priority with certainty. Independent scientific validation has not been performed.

## References

1. J. Araújo and P. J. Cameron, *Primitive Groups Synchronize Non-uniform Maps of Extreme Ranks*, first public arXiv version 20 June 2013, [arXiv:1306.4827](https://arxiv.org/abs/1306.4827), especially Theorems 1–2.
2. M. V. Volkov, *Synchronization of Primitive Automata*, *RAIRO—Theoretical Informatics and Applications* **58** (2024), article 3, [doi:10.1051/ita/2024003](https://doi.org/10.1051/ita/2024003), especially Corollary 2.4.
3. M. V. Berlinkov and C. Nicaud, *Synchronizing Random Almost-Group Automata*, first public 6 May 2018, [arXiv:1805.02154](https://arxiv.org/abs/1805.02154), especially Section 4, for an asymptotic count in a different restricted almost-group family.
4. C. Aistleitner et al., *Circular automata synchronize with high probability*, first public 6 June 2019, [arXiv:1906.02602](https://arxiv.org/abs/1906.02602), for the different unconditioned random-circular-automaton model.
