# Two-image rigidity at the maximal ternary curling-number boundary

## Finding
Let \(\mathcal E_n\) be the set of length-\(n\) words over the *labeled* alphabet \(\{0,1,2\}\) such that both the word and its curling-number transform are overlap-free. Define the length-\(83\) word \(T\) over \(\{1,2\}\) by the literal digit string

`11211221211212211221211221121221122121121221211221121221122121122112122121121221121`

The following is an exact description of the terminal two levels.

1. \(\lvert\mathcal E_{83}\rvert=5040\). Exactly \(2016\) members have valid one-letter extensions, and **each of those has all three possible extensions**. The other \(3024\) have no valid extension. All \(2016\) extendible members have curling-number transform exactly \(T\).
2. \(\lvert\mathcal E_{84}\rvert=6048\), and \(\mathcal E_{85}=\varnothing\). The complete image of \(\mathcal E_{84}\) under the curling-number transform is exactly \(\{T\!\cdot\!1,T\!\cdot\!2\}\), where \(\cdot\) denotes digit concatenation. Their respective inverse-fiber sizes are
   \[
   \bigl\lvert\{w\in\mathcal E_{84}:C(w)=T\!\cdot\!1\}\bigr\rvert=4032,
   \qquad
   \bigl\lvert\{w\in\mathcal E_{84}:C(w)=T\!\cdot\!2\}\bigr\rvert=2016.
   \]
3. For every \(w\in\mathcal E_{84}\), the final transform digit equals \(2\) precisely when the last two source symbols are equal. Thus each extendible length-\(83\) word has one terminal extension with transform \(T\!\cdot\!2\) and two with transform \(T\!\cdot\!1\).

In particular, all \(6048\) maximal words collapse to just two distinct curling-number images, sharing the same first \(83\) digits. There are \(1008\) source classes under global alphabet permutations, with \(672\) and \(336\) classes in the respective fibers.

## Assumptions and scope
A word \(w\) has an **overlap** if a contiguous factor is of the form \(axaxa\), where \(a\) is one symbol and \(x\) is any finite word, including the empty word. Equivalently, there are integers \(p\ge1\) and \(i\) such that the factor from \(i\) through \(i+2p\) has period \(p\). An overlap-free word contains no such factor.

For a nonempty finite word \(u\), its curling number \(\kappa(u)\) is the largest positive integer \(k\) for which \(u=vy^k\) for some possibly empty word \(v\) and some nonempty word \(y\). The prefix transform \(C(w)\) has \(j\)-th digit \(\kappa(w[0..j])\), with indices beginning at zero. This is the direct-prefix convention of the motivating paper.

All source words are over the full *available* labeled alphabet \(\{0,1,2\}\); they are not required a priori to use every symbol. All counts are for words rather than rotation classes. No claim is made for arbitrary lengths or for other repetition thresholds.

## Proof
**Curling-symbol lemma.** Every overlap-free word is cubefree: a cube \(y^3\) contains a factor of length \(2\lvert y\rvert+1\) with period \(\lvert y\rvert\). Hence \(\kappa(u)\le2\) for every nonempty prefix \(u\) of an overlap-free word. Therefore \(\kappa(u)=2\) if and only if \(u\) has a nonempty square suffix \(y^2\), and otherwise \(\kappa(u)=1\).

**Exhaustion lemma.** Call a prefix admissible when both it and its transform are overlap-free. Admissibility is inherited by prefixes: an overlap cannot disappear when letters are deleted from the right, and \(C(u)\) is a prefix of \(C(uv)\). To enumerate all admissible prefixes of length \(n+1\), append each possible letter to each length-\(n\) admissible word, compute the new transform digit using the curling-symbol lemma, and reject precisely when either newly extended word acquires an overlap ending at its last position. Every newly introduced overlap must end there. For a word \(s\) of length \(m\), a new terminal overlap exists exactly when for some integer \(1\le p\le\lfloor(m-1)/2\rfloor\),
\[
 s[m-2p-1..m-p-1]=s[m-p-1..m-1],
\]
where the two equal blocks each have \(p+1\) symbols. A new transform digit equals \(2\) exactly when some two consecutive length-\(p\) suffix blocks are equal. These are finite exact comparisons, without heuristics.

**Complete finite certificate.** Start with the unique first-symbol-normalized word \(0\), whose transform is \(1\), and apply the exhaustive recurrence through length \(85\). Fixing the first source symbol to \(0\) is lossless because all three source letters are interchangeable, and \(C\) is unchanged by any global alphabet permutation. The independently written Python and C++17 implementations reproduce the full count table supplied in `prefix_counts.tsv`. In particular the normalized admissible levels have sizes \(1680\), \(2016\), and \(0\) at lengths \(83\), \(84\), and \(85\).

The supplied complete normalized terminal set `normalized_extremizers.tsv` has exactly \(2016\) distinct length-\(84\) words and their transforms. Grouping by the length-\(83\) source prefix yields exactly \(672\) distinct parents, **each with all three possible terminal letters**. The other \(1680-672=1008\) normalized admissible length-\(83\) parents have no terminal extension. All \(672\) extending parents have the same transform \(T\); the remaining \(1008\) parents have two other transform values, with multiplicities \(672\) and \(336\).

The same complete terminal set gives exactly two distinct transformed words, \(T\!\cdot\!1\) with \(1344\) normalized preimages and \(T\!\cdot\!2\) with \(672\). The final-digit comparison against the last two source letters holds for every terminal row. Each normalized count is multiplied by three to obtain the labeled count, because each of the three choices of initial source symbol gives an equinumerous, disjoint family and preserves the transform. Every terminal source uses all three symbols, as also directly checked, so the action of all six alphabet permutations on terminal sources is free; dividing the fiber sizes by six gives the stated class counts. This establishes all assertions.

## Verification
The complete terminal manifest is included as `normalized_extremizers.tsv`. The level-by-level count certificate is `prefix_counts.tsv`. From their containing directory, run

```sh
python3 verify.py
c++ -O3 -std=c++17 check_fast.cpp -o check_fast
./check_fast
```

The Python checker constructs the full search afresh, compares *every* manifest row, checks the depth-\(83\) all-or-none branching and exact fiber counts, independently computes each curling number from its definition on every terminal prefix, and checks all terminal source and image words for overlaps. The C++17 program separately performs the exhaustive prefix search using raw character-block comparisons, reaching the same terminal fiber sizes and the empty length-\(85\) level. Neither implementation relies on random testing or a partial search.

## Relationship to prior work
Caveney, Dong, and Shallit [1] defined and analyzed simultaneous repetition avoidance for finite words and their curling-number transforms. Their Theorem 7 establishes the maximum ternary length \(84\) and reports \(6048\) maximal words, displaying one source and one image. Those facts alone do **not** determine the complete transform image set, the two exact inverse-fiber sizes, or the all-or-none extension dichotomy at length \(83\), which are the additional claims proved here. Their Section 2.3 supplies the foundational prefix-hereditary exhaustive-search method. Earlier curling-number work by Chaffin and collaborators [2] studies counts and extensions for other curling statistics, not this constrained terminal image classification.

## Limitations
The theorem is a finite, completely exhausted boundary classification, not a statement for an infinite family of lengths. The certificates are ordinary source-code algorithms and data; they do not constitute external formal certification. Historical priority remains subject to unavailable or unindexed work, including possible unpublished enumerations of the image fibers. The evidence does not establish the novelty of the source and length bound themselves, which are expressly credited to [1].

## References
[1] G. Caveney, H. Dong, and J. Shallit, *Repetition Avoidance in Curling-Number Transforms*, arXiv:2608.15670v1 (first posted 2026-08-16), Sections 2.1, 2.3, 4.1, Appendix B; https://arxiv.org/html/2608.15670.

[2] B. Chaffin, J. P. Linderman, N. J. A. Sloane, and A. R. Wilks, *On Curling Numbers of Integer Sequences*, arXiv:1212.6102 (2012); https://arxiv.org/abs/1212.6102.
