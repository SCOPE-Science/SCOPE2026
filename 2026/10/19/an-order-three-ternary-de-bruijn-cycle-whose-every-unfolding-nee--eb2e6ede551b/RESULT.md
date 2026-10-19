# An order-three ternary de Bruijn cycle whose every unfolding needs ten attractor positions

## Finding

Let the circular ternary word be the following cyclic ordering of its symbols:

`000110120102202002122211121`.

Its length is \(27\), and its \(27\) cyclic factors of length three are exactly the \(27\) possible ternary triples, each occurring once. For every cut \(c\in\{0,1,\ldots,26\}\), let \(R_c\) be the rotation beginning at zero-based index \(c\), and let \(T_c\) be \(R_c\) followed by its first two symbols. Thus \(|T_c|=29\). A *string attractor* for a finite word is a set of positions intersecting at least one occurrence of every distinct nonempty factor. The minimum string-attractor cardinality of **every** \(T_c\) is exactly \(10\). The same statement holds for 3-attractors (which need only cover factors of lengths at most three).

In particular, for this cyclic de Bruijn word **no choice of unfolding** attains the elementary nine-position bound forced by its distinct length-three factors. This gives a negative answer, for a specific de Bruijn cycle, to the all-cycles unfolding question explicitly raised in Whittington's *Online String Attractors* (2024). It does not refute Whittington's separate, weaker conjecture that at least one suitably chosen de Bruijn cycle has an optimally small attractor for each alphabet and order.

## Assumptions and scope

The alphabet is \(\{0,1,2\}\); positions in a linear word are one-based, while cuts and the tabulated cyclic starts are zero-based. A factor is a contiguous nonempty substring. The minimum in the theorem ranges over **all** subsets of the \(29\) linear positions and every one of the \(27\) cuts. Reversing the orientation, substituting symbols, or allowing circular attractors is not part of the claim. The result is an explicit finite counterexample with exhaustive and symbolic justification, not an assertion about every order-three ternary de Bruijn cycle.

## Proof

**De Bruijn property.** Direct enumeration of the displayed \(27\) overlapping cyclic triples gives all \(27\) elements of \(\{0,1,2\}^3\) exactly once. A concise independent checker below verifies the equality with the Cartesian cube, including the two triples crossing the cyclic boundary. Consequently each \(T_c\) has exactly \(27\) length-three factors, each appearing exactly once, starting at linear positions \(1\) through \(27\).

**Rigidity of nine positions.** Every marked position of a linear word lies in at most three length-three factor occurrences, whose starting positions are consecutive. Since the \(27\) length-three factors of \(T_c\) are distinct, any 3-attractor needs at least \(\lceil27/3\rceil=9\) positions. If nine suffice, each marked position must hit exactly three different triples, with no overlap between the covered triple-start sets. The triple starting at position \(1\) forces the first mark at position \(3\): only this mark can cover exactly the first three triple starts without wasting capacity at the left end. Inductively the next uncovered start forces marks at \(6,9,\ldots,27\). Thus every nine-position 3-attractor would necessarily be

\[E=\{3,6,9,12,15,18,21,24,27\}.\]

**Obstruction in every rotation.** The positions marked by \(E\) correspond, in the original cyclic word, to one residue class modulo three; the class is \(r\equiv c+2\pmod 3\) when the cut is at zero-based position \(c\). The following table lists for each such residue class a two-letter factor whose **all** cyclic starts avoid the marked residue class at both of their letters:

| Marked residue \(r\) | Uncovered two-letter factor | All its zero-based cyclic starts |
| ---: | :---: | :--- |
| \(0\) | `02` | \(10,13,16\) |
| \(1\) | `01` | \(2,5,8\) |
| \(2\) | `12` | \(6,18,24\) |

These starts are obtained directly by inspecting the displayed cyclic word; each indicated factor occurs three times because the word is order-three de Bruijn. For a length-two occurrence beginning at \(i\), its two positions have residues \(i\) and \(i+1\) modulo three. The tabulated positions avoid the marked class in both coordinates. Repeating the first two symbols after any cut does not add marked positions and cannot change this fact. Therefore \(E\) fails to cover the indicated two-letter factor in every unfolding. Since every nine-position 3-attractor must equal \(E\), no unfolding has a 3-attractor (or full string attractor) of size nine.

**Sharp ten-position construction.** For any cut, \(E\) covers all \(27\) length-three occurrences. Direct inspection of the nine cyclic two-letter factors and three letters, equivalently the checks performed in the accompanying standalone verifier for each of the \(27\) cuts, shows that \(E\) covers every letter and exactly eight of the nine possible bigrams. The sole missing bigram is the one specified by the table. It occurs three times in the cycle; in each linear unfolding at least two cyclic occurrences are fully represented. Pick either position in any occurrence of this missing bigram and add it to \(E\). The resulting ten-position set covers every factor of length at most three.

It also covers **every longer factor**: every longer factor contains a length-three subfactor; that triple is unique in \(T_c\), so the marked occurrence of that triple must lie inside the longer factor's occurrence. Hence the ten-position set is a full string attractor. Combining this with the lower bound proves \(\gamma(T_c)=10\) for all \(c\), as claimed.

## Verification

The standalone `debruijn_attractor_check.py` uses only the Python standard library. Running `python3 debruijn_attractor_check.py` checks that the displayed cycle contains all \(27\) distinct cyclic ternary triples, checks the exact residue/omitted-bigram table and its occurrence lists, and checks every factor of every length \(1\) through \(29\) against a constructed size-ten attractor separately for each of the \(27\) cuts. It also checks that the rigid nine-position set misses exactly the tabulated bigram for every cut. The proof of the lower bound is the covering-capacity and uniqueness argument above; the finite enumeration is a reproducible certificate for this explicit instance, not extrapolation from smaller instances.

## Relationship to prior work

Whittington (2024, §5, *Optimal String Attractors for de Bruijn Sequences*) distinguishes the exact-length, or sharp, \(k\)-attractor from the ordinary \(k\)-attractor, gives an example of an unsuccessful unfolding of the ternary order-three Lyndon de Bruijn cycle, and shows that an alternative unfolding of that **same** cycle does attain the small target. He explicitly asks whether every de Bruijn cycle permits some favorable unfolding. The present cycle differs in that **none** of its \(27\) unfoldings does. His Theorem 29 proves that *some* Lyndon-generated cycles at prime orders have favorable unfoldings, which is consistent with this finding. Mantaci et al. (2019) establish general attractor bounds and connections to repetitiveness, not this instance's rotation-uniform obstruction. Fuchs and Whittington (2023/2024) study general 2-attractor complexity rather than de Bruijn unfolding minima. No broader claim is made about an extremum over all de Bruijn cycles.

## Limitations

The theorem concerns one explicitly listed ternary order-three cyclic word, its standard \(29\)-symbol linear unfoldings, and exact position hitting. It does not classify every such cycle, find the largest possible attractor over all cycles, or contradict existence of some favorable cycle at every order. The novelty check is bounded by accessible indexed literature and research records; independently discovered or unindexed equivalent examples remain possible. No independent mathematical audit has been performed.

## References

1. P. Whittington, *Online String Attractors*, arXiv:2407.15599v1 (publicly posted 2024-07-22), especially §5 and Theorem 29. https://arxiv.org/abs/2407.15599
2. S. Mantaci, A. Restivo, G. Romana, M. Rosone, and M. Sciortino, *String Attractors and Combinatorics on Words*, arXiv:1907.04660 (2019). https://arxiv.org/abs/1907.04660
3. J. Fuchs and P. Whittington, *The 2-Attractor Problem is NP-Complete*, arXiv:2304.06523 (2023); STACS 2024. https://arxiv.org/abs/2304.06523
