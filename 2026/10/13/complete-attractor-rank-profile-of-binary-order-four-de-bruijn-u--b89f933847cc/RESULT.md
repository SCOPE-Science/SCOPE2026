# Complete attractor-rank profile of binary order-four de Bruijn unfoldings

## Finding
Let \(b=b_0\cdots b_{15}\) be any binary cyclic de Bruijn sequence of order \(4\): the \(16\) cyclic length-four factors at starts \(0,\ldots,15\) are pairwise different. For a cut \(t\in\{0,\ldots,15\}\), let \(r_t(b)\) be the length-\(16\) rotation starting at \(b_t\), and form the length-\(19\) linear unfolding
\[
T_{b,t}=r_t(b)\,\operatorname{pref}_3(r_t(b)).
\]
For a finite word \(T\), a *full string attractor* is a set of positions meeting some occurrence of **every** distinct nonempty factor of \(T\). Let \(\gamma(T)\) be its smallest cardinality. All positions below are zero-based.

**Exact complete classification.** Every such \(T_{b,t}\) has \(\gamma(T_{b,t})\in\{4,5\}\). In fact,
\[
\gamma(T_{b,t})=4\quad\Longleftrightarrow\quad
\{3,7,11,15\}\text{ is a full attractor of }T_{b,t}.
\]
If the right-hand condition fails, \(\gamma(T_{b,t})=5\), and the **same** five-position set \(\{3,6,9,12,15\}\) is a full attractor for every unfolding.

There are exactly \(16\) binary de Bruijn cycles up to rotation, each with \(16\) distinct rooted cuts. Among their \(256\) unfoldings, exactly \(192\) have minimum attractor size \(4\), and the remaining \(64\) have minimum size \(5\). More precisely, the \(16\) rotation classes divide as follows: \(4\) cycles have all \(16\) cuts of minimum size \(4\); \(8\) cycles have exactly \(12\) such cuts; and \(4\) cycles have exactly \(8\). Thus **every** binary order-four de Bruijn cycle admits at least eight optimal four-attractor cuts, although not every cut does.

A full listing of all \(16\) lexicographically least cycle representatives and their optimal zero-based cuts is supplied as `CENSUS.csv`. The complete checker is `verify.py`.

## Assumptions and scope
The alphabet is exactly \(\{0,1\}\); the de Bruijn order is exactly \(4\); the linear word always includes the initial three symbols after its sixteen-symbol cyclic segment. Distinct *rooted* unfoldings are counted separately. The attractor notion is the ordinary linear *full* string attractor, not a circular attractor, an online attractor, or merely a sharp length-four attractor. Indices in the statement, checker, and certificate start at zero. No symmetry beyond cyclic rotation is factored out in the \(16\)-cycle count.

## Proof
**1. All length-four windows force four marks and their unique placement.** There are exactly \(16\) windows of length \(4\) in \(T_{b,t}\), at starts \(j=0,\ldots,15\); each represents a different factor. Thus every attractor must intersect *every one of these particular windows*. A marked position intersects at most four of the windows, so at least four positions are necessary.

Suppose exactly four marks suffice. In order to meet all sixteen windows, each mark must intersect exactly four different windows, with no overlap in the sets of windows they hit. The first window starts at zero, so some mark belongs to \(\{0,1,2,3\}\). Only position \(3\) in that range meets four admissible windows; hence \(3\) must be marked and covers windows starting at \(0,1,2,3\). To cover the next start \(4\) by an unused mark that also meets four windows without overlapping those already hit, the mark must be at \(7\). Repeating gives uniquely \(\{3,7,11,15\}\). This proves both the lower bound and uniqueness of the only possible four-position attractor, independently of the symbols of \(T_{b,t}\).

**2. Reduction from full attractors to lengths at most four.** Let \(S\) be any set of positions intersecting every length-four window of \(T_{b,t}\). Each occurrence of any factor of length at least four contains at least one length-four window, which is itself intersected by \(S\). Consequently the factor occurrence intersects \(S\). Therefore it is necessary and sufficient to check factors of lengths \(1,2,3,4\). For the special four-set above, meeting all length-four windows was established in step 1. For the five-set \(S_5=\{3,6,9,12,15\}\), the covered window starts are respectively \(0,\ldots,3\), \(3,\ldots,6\), \(6,\ldots,9\), \(9,\ldots,12\), and \(12,\ldots,15\); together these meet every window. The finite computation in step 3 is needed only to decide the possible additional obstructions from factors of lengths one, two, and three. This reduction verifies **full** attractors, not only a fixed-length surrogate.

**3. Exhaustive finite classification with an explicit complete certificate.** There are precisely \(2^{16}=65,536\) binary words of length \(16\). The accompanying finite verifier forms the sixteen cyclic length-four factors of each word and retains a word if and only if all sixteen are distinct. Exactly \(256\) words pass. Their lexicographically least rotations form exactly \(16\) classes; each such word has sixteen distinct rotations because a shorter period would repeat a cyclic length-four factor. The verifier computes every cut's length-\(19\) unfolding and, for every factor of lengths \(1,2,3,4\), compares the set of all factors with the set of factors having an occurrence crossing the proposed marks. It checks both the unique possible four-set \(S_4=\{3,7,11,15\}\) and the universal five-set \(S_5=\{3,6,9,12,15\}\). For additional assurance it repeats these comparisons for every length \(1\) through \(19\). All \(256\) five-set checks succeed; precisely \(192\) four-set checks succeed.

Grouping the successful four-set checks by the sixteen cycle representatives yields exactly four classes with sixteen successes, eight with twelve, and four with eight. `CENSUS.csv` records the individual cycle representatives and successful cut indices, and `verify.py` independently reconstructs and compares every entry. Step 1 and the exhaustive four-set test prove that the remaining \(64\) unfoldings have no four-attractor; the universal five-set test then proves they have minimum exactly five. The complete finite enumeration, not extrapolation from a bounded sample, proves the theorem.

## Verification
With Python 3 and only the standard library, place `verify.py` alongside `CENSUS.csv` and execute `python verify.py`. The checker reconstructs all \(65,536\) candidates without importing any precomputed de Bruijn list, checks all claimed attractor conditions, establishes uniqueness of the length-four-window hitting four-set independently by testing the \(\binom{19}{4}\) subsets, verifies each certificate entry, and prints:

`VERIFY_OK all_binary_16_words=65536 rooted_debruijn=256 cycles=16 unique_four_window_hittings=1 four_roots=192 five_roots=64 orbit_classes_8_12_16=4_8_4 universal_five=verified`

The exhaustive search is a finite proof because the complete domain is \(\{0,1\}^{16}\); a machine run is checkable using the supplied executable source, not treated as a substitute for the logical reduction in steps 1 and 2.

## Relationship to prior work
Mantaci, Restivo, Romana, Rosone, and Sciortino, *A Combinatorial View on String Attractors*, §6.2, Proposition 41, establish general upper and lower bounds for linear de Bruijn words and exhibit **one** binary order-four unfolding with a size-four attractor (their one-based set is \(\{4,8,12,16\}\)). That example is consistent with the present result, but it does not give counts across all sixteen rotation classes and all cuts, nor identify the sixty-four five-attractor unfoldings.

Whittington, *Online String Attractors*, §5, raises the question of which general de Bruijn sequences or unfoldings possess an attractor at the sharp order-size threshold; Theorem 29 treats the Lyndon-generated construction at prime order. The present result is a complete solution for the first composite binary order, \(4\), including all cycles and cuts. It does **not** establish Whittington's general conjecture for arbitrary orders and alphabets. Related work on string attractors for special infinite sequences concerns different word families and does not imply this classification.

## Limitations
The theorem is a complete finite classification of binary order-four de Bruijn unfoldings, not a formula for arbitrary order \(k\) or alphabet size. It does not determine optimal *online* or *circular* attractors, and it does not claim that all cuts have optimal cardinality four. Computational assertions are independently reproducible from the complete included script and certificate, but no external audit is represented here. An unpublished or differently indexed earlier equivalent census cannot be excluded by literature searching alone.

## References
1. Philip Whittington, *Online String Attractors*, arXiv:2407.15599, first posted 22 July 2024, especially §5 and Theorem 29. https://arxiv.org/abs/2407.15599
2. Sabrina Mantaci, Antonio Restivo, Giuseppe Romana, Giovanna Rosone, and Marinella Sciortino, *String Attractors and Combinatorics on Words*, arXiv:1907.04660, first posted 10 July 2019; expanded journal treatment *A Combinatorial View on String Attractors*, Theoretical Computer Science 850 (2021), §6.2, Proposition 41. https://arxiv.org/abs/1907.04660 and https://doi.org/10.1016/j.tcs.2020.11.006
