# Sharp unclustered Burrows–Wheeler run bound through length \(80\)

## Finding
For integers \(q\geq 3\) and \(14\leq n\leq 80\), let \(U_q(n)\) be the minimum number of **cyclic** equal-letter runs of a primitive necklace of length \(n\) over the ordered alphabet \(\{0,1,\ldots,q-1\}\), subject to the requirement that its Burrows–Wheeler transform has exactly \(n\) ordinary (linear) runs. Then
\[
U_q(n)=\left\lceil\frac n2\right\rceil\qquad (q\ge3,\ 14\le n\le80).
\]
The upper bound is supplied by one fully explicit ternary witness for each of the \(67\) consecutive lengths. The lower bound follows from the established factor-two BWT run inequality. This is a finite-range theorem; it does not establish the corresponding conjecture for all lengths.

## Assumptions and scope
A primitive necklace is the set of circular rotations of a word that is not a proper power. The cyclic run number \(c(w)\) is \(\#\{i\in\{0,\ldots,n-1\}:w_i\ne w_{(i+1)\bmod n}\}\). The BWT of a necklace is obtained by sorting its length-\(n\) circular rotations lexicographically and reading their last characters; the output has \(n\) runs exactly if its consecutive characters are all distinct. We use zero-based coordinates for the finite certificate and the natural order \(0<1<2\). Each witness uses only these three symbols, hence applies without change to every \(q\ge3\).

## Proof
**Lower bound.** Take the lexicographically least representative \(v\) of any primitive necklace. It is a Lyndon word and is unbordered, so its first and last letters are different. Accordingly, its linear run count equals its cyclic run count. The factor-two inequality of Mantaci, Restivo, Rosone, and Sciortino asserts that \(r(\mathrm{BWT}(v))\le2r(v)\). Therefore a completely unclustered BWT has \(n\le2c(v)\) and hence \(c(v)\ge\lceil n/2\rceil\).

**Upper bound and finite certificate.** `witnesses.json` explicitly lists one length-\(n\) ternary word \(L_n\) for *each* integer \(n\in[14,80]\). For instance, the length-\(14\) entry is `10101210212021`. For a listed word \(L\), let \(F\) be its sorted rearrangement and define the stable-rank permutation \(\pi\) by mapping each position of \(L\) to the position of the same occurrence of its letter in \(F\). This is the standard BWT LF map. Each listed \(L\) satisfies all of the following finite statements, checked by the standalone verifier:

1. \(L_i\ne L_{i+1}\) for every \(0\le i<n-1\).
2. \(\pi\) is one cycle of length \(n\).
3. \(d_H(L,F)=\lceil n/2\rceil\).

The one-cycle condition yields a primitive inverse necklace. Traversing the cycle and reversing its sequence of letters from \(F\) gives a representative \(v\) of the inverse necklace. Along the cycle, its successive letters are \(F_i\) and \(F_{\pi(i)}=L_i\), so its cyclic run number is \(d_H(L,F)=\lceil n/2\rceil\). For an independently checkable direct certificate, `verify.py` also sorts every circular rotation of the reconstructed \(v\), confirms that its last column is precisely \(L\), rules out every proper-power period, and counts the cyclic runs from \(v\) itself. Thus the bound is attained at all the stated lengths over the ternary alphabet, and embedding the ternary alphabet into \(q\) letters preserves the BWT and run counts. This proves the assertion.

## Verification
Run `python3 verify.py` in the directory containing `witnesses.json`. The script uses Python's standard library only, reads precisely the \(67\) entries for lengths \(14\) through \(80\), reconstructs the BWT inverse using an occurrence-ranked LF map, and independently checks forward BWT by explicitly sorting all circular rotations. It checks primitivity, all adjacent-letter inequalities, the one-cycle property, the Hamming identity, and the exact cyclic run target. The expected output is in `output.txt`. The proof needs no randomized computations or unverified extrapolation from the tested range.

## Relationship to prior work
Mantaci, Restivo, Rosone, and Sciortino proved the factor-two upper bound on BWT run amplification, which supplies the lower bound here. Fici, Gabory, Romana, and Sciortino (2026) established the existence of completely unclustered BWT images for all lengths on alphabets of size at least three, without the present optimal cyclic run condition. Kumallagov (2026) formulated the precise minimum \(U_q(n)\), established its universal lower bound, computed initial cases, gave several infinite arithmetic families, and conjectured equality for every \(n\ge7\). Our claim is restricted to the consecutive finite range \(14\le n\le80\); any lengths already covered by those earlier arithmetic families are not separately claimed as novel. Its content is the *complete new consecutive window* backed by explicit witnesses, not an infinite structural solution.

## Limitations
The statement is a finite, initial-length verification of a conjectured optimality law, not a proof beyond length \(80\). The supplied witnesses need not be unique and are not a classification of all extremizers. Relevant full text of one 2026 preprint could not be inspected in the accessible source set; potential unpublished or unindexed finite certificates remain a literature-overlap risk. The lower bound invokes a previously published theorem, with its proof source explicitly cited below; the upper bound is independently checkable from the complete included certificate.

## References
1. D. Kumallagov, *An extremal problem for completely unclustered Burrows–Wheeler images*, arXiv:2606.01267 (first version 2026), https://arxiv.org/abs/2606.01267.
2. G. Fici, E. Gabory, G. Romana, M. Sciortino, *Totally Unclustered BWT Images of Any Length over Non-Binary Alphabets*, CPM 2026, DOI:10.4230/LIPIcs.CPM.2026.13.
3. S. Mantaci, A. Restivo, G. Rosone, M. Sciortino, *Burrows-Wheeler Transform and Run-Length Enconding*, WORDS 2017, DOI:10.1007/978-3-319-66396-8_21 (author postprint at https://pages.di.unipi.it/rosone/Papers/MRRS_WORDS2017.pdf).
