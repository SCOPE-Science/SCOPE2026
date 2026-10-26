# Permutation-successions classification of optimal ternary sparse deletion codes

## Finding
For every integer \(n\ge 2\), let \(\mathcal W_n\) consist of the length-\(n\) words over \(\{0,1,2\}\) containing one \(1\), one \(2\), and \(n-2\) zeros. A code \(C\subseteq\mathcal W_n\) corrects one deletion when no two of its words have a common length-\(n-1\) subsequence obtained by deleting exactly one symbol. The optimal size is exactly
\[
\max_C |C|=n-1.
\]
More strongly, all the optimum codebooks are classified by *signed permutations with an adjacency restriction*. Put \(k=n-1\). For a permutation \(\pi\) of \(\{0,\ldots,k-1\}\), assign a sign \(\epsilon_i\in\{+,-\}\) to each row, forced to \(+\) when \(i<\pi(i)\), forced to \(-\) when \(i>\pi(i)\), and freely chosen when \(i=\pi(i)\). Exactly one optimum code corresponds to each assignment satisfying
\[
\pi(i+1)=\pi(i)+1\quad\Longrightarrow\quad\epsilon_{i+1}\ne\epsilon_i
\qquad(0\le i<k-1).
\]
The correspondence is given explicitly below. Equivalently, a permutation is admissible if each adjacent rising succession is a pair of fixed points; along each maximal consecutive run of fixed points, signs alternate. Thus, if \(r(\pi)\) is the number of maximal nonempty consecutive runs of fixed points,
\[
B_k=\sum_{\substack{\pi\in S_k:\;\pi(i+1)=\pi(i)+1\\\Rightarrow\pi(i)=i\ \text{for all }0\le i<k-1}}2^{r(\pi)}
\]
is the exact number of *labeled* optimal codebooks of length \(k+1\) (no quotient by reversal, renaming, or coordinate permutation). A subset dynamic program with the stated transition rule computes \(B_k\) in \(O(k^3 2^k)\) arithmetic operations. The first values, for \(k=1,\ldots,11\), are
\[
2,\ 3,\ 8,\ 32,\ 158,\ 918,\ 6258,\ 49076,\ 434408,\ 4282508,\ 46532354.
\]

## Assumptions and scope
All words are **linear** and alphabet symbols are distinct. Deletion of *any one* position is allowed; several deletions of different zero positions may yield the same received word, in which case the descendant is counted only once. All codebooks are sets of different length-\(n\) words and are counted with their actual labels. The theorem applies to every \(n\ge2\), including \(n=2\). The source family has precisely the specified composition, not merely Hamming weight two over a binary alphabet.

For any \(w\in\mathcal W_n\), define \(u\in\{0,\ldots,k-1\}\) as the surviving position (zero-based) of symbol \(1\) after deleting symbol \(2\), and \(v\) as the surviving position of symbol \(2\) after deleting symbol \(1\). Write \(+\) for the order \(1\) before \(2\) and \(-\) for the reverse order. The unique source word associated to \((u,v,+)\) has \(1\) at original position \(u\) and \(2\) at \(v+1\), which is valid exactly when \(u\le v\). The unique source associated to \((u,v,-)\) has \(2\) at \(v\) and \(1\) at \(u+1\), valid exactly when \(u\ge v\). At \(u=v\), both orientations are possible and correspond to adjacent marked symbols. These rules define the claimed bijection.

## Proof
**Capacity.** Deleting \(1\) always yields a length-\(k\) word with exactly one \(2\), so there are exactly \(k\) possible such descendants. Their distinctness across codewords is necessary for correction. Hence every code has at most \(k=n-1\) words. Likewise, deleting \(2\) yields \(k\) possibilities with exactly one \(1\). At equality, the \(u\)-coordinates and the \(v\)-coordinates must each occur exactly once, and therefore \(v=\pi(u)\) for a permutation \(\pi\). The source reconstruction above forces the sign except at fixed points.

**Two-marker collision lemma.** After deleting a zero, the original order of the two nonzero symbols is preserved. Record the surviving pair of positions as \((\text{position of }1,\text{position of }2)\). For the \(+\) word labeled \((u,v)\), the possible resulting pairs are
\[
(u-1,v)\ (u>0),\qquad (u,v)\ (u<v),\qquad (u,v+1)\ (v<k-1).
\]
For the \(-\) word labeled \((u,v)\), they are
\[
(u,v-1)\ (v>0),\qquad (u,v)\ (u>v),\qquad (u+1,v)\ (u<k-1).
\]
These lists follow by deleting a zero before, between, or after the marked symbols; the displayed conditions are exact. A \(+\) and a \(-\) word cannot share a two-marker descendant because their marker orders differ. For two different labels with both \(u\)- and \(v\)-coordinates different and having the same sign, direct comparison of the three displayed possibilities shows that an intersection exists if and only if, after ordering the labels by their \(u\)-coordinate, the labels are \((u,v)\) and \((u+1,v+1)\). In that case the first word's trailing-zero deletion and the second word's leading-zero deletion both yield \((u,v+1)\) for sign \(+\); for sign \(-\), they both yield \((u+1,v)\). Both requisite zeros exist: \(v+1\le k-1\) and \(u+1>0\). When either coordinate difference exceeds one, its possible coordinates are disjoint; for oppositely directed differences of one, the only shared coordinate candidates require mutually exclusive before/between/after cases. This proves both directions.

**Classification.** In a maximum code with labels \((i,\pi(i))\), the one-marker descendant sets are automatically pairwise disjoint by the permutation property. By the lemma, an intersection of two-marker descendants occurs exactly when consecutive rows \(i,i+1\) have consecutive columns \(\pi(i),\pi(i)+1\) and equal signs. Therefore the signed-permutation condition is necessary and sufficient. If a rising succession occurs then \(\pi(i)-i=\pi(i+1)-(i+1)\); when this common displacement is nonzero, both signs are forced and identical, so the succession is forbidden. When the common displacement is zero, both entries are fixed points and either of two initial signs is possible on each maximal fixed-point run, followed by forced alternation. Different runs have independent choices. This establishes the sum for \(B_k\).

**Existence at every length.** Take the identity permutation and alternate signs along its single run of fixed points. These are the \(k\) adjacent-pair words whose marked symbols occupy positions \(i,i+1\), with order \(12\) for even \(i\) and \(21\) for odd \(i\). Their descendant sets are disjoint by the proved classification, so the upper bound is attained including \(k=1\).

**Counting recurrence.** For completeness, let \(F_i(S,v,e)\) count legal partial signed permutations on rows \(0,\ldots,i\), using exactly the column set \(S\), ending in column \(v\) with sign \(e\). Initially \(F_0(\{v\},v,e)=1\) for each orientation allowed at \((0,v)\), with all other states zero. From a state at row \(i-1\), choose unused column \(c\) for row \(i\) and any orientation \(f\) allowed by the inequality between \(i\) and \(c\). Add the old count to \(F_i(S\cup\{c\},c,f)\) unless \(c=v+1\) and \(f=e\). Then \(B_k\) is the sum of \(F_{k-1}(S,v,e)\) over full column set \(S\) and all ending states. There are at most \(2k2^k\) states per layer and at most \(2k\) transitions per state, giving the advertised conservative \(O(k^3 2^k)\) total operation bound. Every legal assignment is counted once.

## Verification
Run `python3 checker.py` in the directory containing the embedded standalone checker. It directly builds all one-deletion descendant sets independently of the signed-permutation lemma, exhaustively counts all optimal codebooks as subsets for lengths \(2\) through \(6\), compares all signed permutations with direct descendant intersections for \(k\le8\), evaluates the separate permutation formula through \(k=8\), computes the dynamic-programming counts through \(k=11\), and tests the explicit optimum construction through length \(100\). The checker completed successfully. These finite tests are independent cross-checks, **not** the proof of the infinite theorem, which is the capacity-plus-collision argument above.

## Relationship to prior work
Sloane's *On Single-Deletion-Correcting Codes* (public arXiv version dated 2002-07-22) supplies the standard deletion-descendant definition, binary confusability graph, and survey of general code constructions. It does not classify the fixed ternary composition with one copy of each nonzero symbol or count all optimal codebooks. Tenengolts' 1984 nonbinary construction addresses general alphabets, but the abstract available for this comparison is not a classification of this constant-composition layer; the full text could not be inspected. The earlier study *Counting Successions in Permutations* (Reilly and Tanny, 1979) treats ordinary permutation succession statistics. Du and Ji (2024) study successions, fixed points, excedances and drops in permutation bijections. Their permutation results do not assert this one-deletion-code correspondence or its orientation-dependent restriction. The present coding statement is stronger than simply applying a known succession count, since the binary orientation at fixed points is constrained by adjacent deletion collisions. Published unrestricted small ternary code-size results and a binary weight-two code optimum concern different source families; neither statement logically gives the labeled optimum-codebook classification here.

## Limitations
The theorem is restricted to a single deletion and exact composition \((n-2,1,1)\) over three distinct symbols. The count \(B_k\) is an exact finite sum and a subset recurrence, not a claimed elementary closed form, polynomial-time enumeration algorithm, or classification for general ternary compositions. The original 1984 nonbinary-code paper was not available in full; an earlier equivalent sparse-family treatment remains a priority risk. No independent external audit has been performed.

## References
- N. J. A. Sloane, *On Single-Deletion-Correcting Codes*, arXiv:math/0207197, first publicly posted 2002-07-22, https://arxiv.org/abs/math/0207197 .
- G. Tenengolts, *Nonbinary codes, correcting single deletion or insertion*, IEEE Transactions on Information Theory 30 (1984), 766–769, doi:10.1109/TIT.1984.1056962 .
- J. W. Reilly and S. M. Tanny, *Counting Successions in Permutations*, Studies in Applied Mathematics 61 (1979), 73–81, doi:10.1002/sapm197961173 .
- L. R. Du and K. Q. Ji, *A Refinement of a Theorem of Diaconis-Evans-Graham*, arXiv:2404.00607, 2024, https://arxiv.org/abs/2404.00607 .
