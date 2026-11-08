# A nested balanced-split obstruction for four-by-four interleavings

## Finding

Let \(\mathcal S_{m,n}\) be the binary concept class consisting of all interleavings of two internally ordered disjoint chains of respective lengths \(m\) and \(n\). The query \((i,j)\) asks whether the \(i\)-th element of the first chain precedes the \(j\)-th element of the second chain. For the balanced four-by-four instance,

\[
\operatorname{Ldim}(\mathcal S_{4,4})=5
< 6=\left\lfloor\log_2\binom{8}{4}\right\rfloor.
\]

This is the first **symmetric** two-chain instance in which the Littlestone dimension is strictly smaller than the cardinality information ceiling: for equal chain lengths \(1,2,3,4\), the respective dimensions are \(1,2,4,5\), whereas the corresponding information ceilings are \(1,2,4,6\).

The structural obstruction is strictly deeper than a first-query imbalance: **four** comparisons split the 70 concepts evenly into two classes of 35, yet none begins a complete depth-six mistake tree. Two middle comparisons fail only after a nested 35-to-17/18-to-9/9 split obstruction.

## Assumptions and scope

All chains, interleavings, and query sets are finite. An interleaving retains the specified order within each of the two chains. Equivalently, each concept is one length-eight word containing four `A` letters and four `B` letters; its \(i\)-th `A` is the first chain's element \(a_i\), and its \(j\)-th `B` is the second chain's element \(b_j\). There are exactly \(\binom84=70\) distinct concepts, and the allowable queries are exactly the 16 cross comparisons \(q_{i,j}=[a_i<b_j]\) for \(1\le i,j\le4\). Up to reversing the order of the second-chain coordinate, the resulting sixteen-bit incidence vectors are precisely the order ideals of the product poset \([4]\times[4]\). Thus the same rank statement applies to point-membership concepts of every ideal of this four-by-four grid.

A complete depth-\(d\) mistake tree is a full binary tree with \(d\) queried internal levels such that every root-to-leaf answer sequence is realized by a concept. Its maximum depth defines \(\operatorname{Ldim}\). At each node the query can depend on preceding answers, but every query belongs to the indicated 16-element set. The bound \(\operatorname{Ldim}(\mathcal C)\le\lfloor\log_2|\mathcal C|\rfloor\) follows because depth \(d\) requires \(2^d\) distinct leaf witnesses.

## Proof

**1. A depth-five tree exists.** In any \(\mathcal S_{m,n}\) with positive chain lengths, comparing the first elements \((a_1,b_1)\) and then deleting the earlier element identifies its two answer branches with \(\mathcal S_{m-1,n}\) and \(\mathcal S_{m,n-1}\). In the special case \(\mathcal S_{1,3}\), comparison with the middle element of the length-three chain and one follow-up comparison gives a depth-two tree on its four insertion positions. The same argument proves depth one for \(\mathcal S_{1,2}\). Thus \(\mathcal S_{2,2}\) has depth two, \(\mathcal S_{2,3}\) has depth three, and \(\mathcal S_{3,3}\) has depth four by successive first-element splits. Appending a fixed last `B` embeds \(\mathcal S_{3,3}\) in \(\mathcal S_{3,4}\) without changing queries among the first three elements of each chain; hence \(\mathcal S_{3,4}\) has depth at least four. The symmetric statement holds for \(\mathcal S_{4,3}\). The first-element comparison in \(\mathcal S_{4,4}\) then supplies a complete depth-five tree.

**2. Only four candidate roots could support depth six.** Since \(2^5=32\), each child of a depth-six root requires at least 32 concepts. Direct exact enumeration of all 70 words gives

\[
\{q_{i,j}:\min(|\mathcal S_{4,4}\cap q_{i,j}|,|\mathcal S_{4,4}\setminus q_{i,j}|)\ge32\}
=\{q_{1,1},q_{2,2},q_{3,3},q_{4,4}\}.
\]

Each of these four comparisons actually splits the 70 concepts into 35 and 35.

**3. The two endpoint candidate roots fail immediately.** Either answer to \(q_{1,1}\) leaves an interleaving family of type \(\mathcal S_{3,4}\) or \(\mathcal S_{4,3}\); likewise for \(q_{4,4}\) by the final-element comparison. The 35 words in \(\mathcal S_{3,4}\) have the finite exact split property

\[
\max_{q}\min(|\mathcal S_{3,4}\cap q|,|\mathcal S_{3,4}\setminus q|)=15.
\]

Since depth five requires every root child to contain at least 16 concepts, neither 35-word family supports depth five. Hence neither endpoint comparison begins a depth-six tree.

**4. The middle candidate roots fail two rounds later.** By reversing the entire merged order and reversing the internal index labels in both chains, it suffices to consider \(q_{2,2}\). Condition on the answer \(q_{2,2}=1\), leaving a 35-word subfamily \(F\). A depth-five tree within \(F\) would require a second query whose two branches each contain at least 16 words. The exact finite counts show the **only** eligible query is \(q_{3,2}\), with counts \(17+18\). Inside its 18-word answer branch with \(q_{3,2}=0\), a putative depth-four tree would require a third query dividing that branch into two classes of at least eight concepts. The only eligible queries are \(q_{3,3}\) and \(q_{4,4}\), each yielding \(9+9\). But none of these four nine-word children admits any comparison splitting it into classes containing at least four concepts apiece. A complete depth-three continuation in any such child is therefore impossible. Thus \(F\) has no depth-five tree and \(q_{2,2}\) cannot root a depth-six tree. Reversal handles \(q_{3,3}\).

The finite counts in steps 2–4 are exact integer exhaustions over all \(\binom84\) words, with every one of the 16 allowed query predicates evaluated, rather than a randomized search or an incomplete enumeration. The included standalone `verify.py` independently regenerates all words, evaluates all comparisons, checks the decisive candidate sets and counts, and recomputes Littlestone dimensions by the full minimax recurrence. It also checks the four equal-chain dimensions reported above.

All potential depth-six roots fail, while a depth-five tree exists; therefore \(\operatorname{Ldim}(\mathcal S_{4,4})=5\).

## Verification

Run `python verify.py` using Python 3.9 or later with only the standard library. It prints `FOUR_BY_FOUR_INTERLEAVING_CERTIFICATE_PASS` and checks that the critical nested candidate counts are exactly \(35\), \(17+18\), and \(9+9\), with no eligible \(4+4\) final split. The independent recurrence also calculates dimensions \(1,2,4,5\) on the four square profiles. The program exhausts finite concept sets and supplies no conclusion for larger chains.

## Relationship to prior work

The 2019 query-learning theory of Chase and Freitag establishes general use of Littlestone dimension; its studied bounds and examples do not directly calculate this two-chain cross-comparison profile. The 2016 analysis by Li, Sun, and Zhang studies the **different minimax problem** of worst-case numbers of comparisons needed to *identify* a complete merge; that worst-case merging number is not the maximum depth of a *full binary* realizable mistake tree. The familiar cardinality ceiling for shattering is elementary and is not claimed as new.

The asymmetric \(3+4\) interleaving has an already-known simpler root-size obstruction; this finding does not claim that case. Its distinctive new content is the **first balanced square** for which perfectly balanced first queries still fail, certified by the deeper nested obstruction.

## Limitations

No general formula for \(\operatorname{Ldim}(\mathcal S_{m,n})\) beyond the identified finite square instance is asserted. Reuse of the 70-word enumeration as a proof is justified only because it covers every concept and query in the stated finite domain. Other earlier terminology or exhaustive comparison tables might contain an equivalent observation; independent mathematical and historical-priority audits have not been performed.

## References

- H. Chase and J. Freitag, *Bounds in Query Learning*, arXiv:1904.10122v1, first publicly posted April 23, 2019, https://arxiv.org/abs/1904.10122. Full-text sections 1–2 on Littlestone dimension and query-learning complexity.
- Q. Li, X. Sun and J. Zhang, *On the Optimality of Tape Merge of Two Lists with Similar Size*, arXiv:1610.03266v1, first posted October 11, 2016, https://arxiv.org/abs/1610.03266. Full-text introduction and results on standard worst-case merge comparison complexity; cited as contextual prior art, not as source for the present online-shattering claim.
