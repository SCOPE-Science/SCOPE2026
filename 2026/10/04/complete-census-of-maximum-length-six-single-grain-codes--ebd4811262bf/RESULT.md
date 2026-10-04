# Complete census of maximum length-six single-grain codes
## Finding
For the binary overlapping single-grain channel at length \(6\), the known optimum \(M(6,1)=16\) has a rigid extremal structure: there are exactly four labeled maximum codebooks. Exactly one is an \(\mathbb F_2\)-linear subspace of \(\mathbb F_2^6\). Exactly two are invariant under global bit complement, and complement exchanges the remaining two. The four codebooks are listed in `enumeration.json`.

## Assumptions and scope
A stored word is \(x=(x_1,\ldots,x_6)\in\{0,1\}^6\). A single grain error may occur only at a transition position \(i\in\{2,\ldots,6\}\) with \(x_i\ne x_{{i-1}}\), and replaces \(x_i\) by \(x_{{i-1}}\); the no-error outcome is also allowed. Write \(B(x)\) for this error ball. A code \(C\) corrects one grain error exactly when \(B(x)\cap B(y)=\varnothing\) for all distinct \(x,y\in C\). The claim is only for binary words of length \(6\) and one grain error.

## Proof
Construct the compatibility graph \(G\) on all \(2^6=64\) binary words, joining \(x\) and \(y\) exactly when \(B(x)\cap B(y)=\varnothing\). Then single-grain codes are precisely cliques of \(G\). Every clique in a finite graph is contained in a maximal clique, so the maximum code size and every maximum code are obtained by enumerating all maximal cliques of \(G\).

The included standard-library program `verify.py` constructs every error ball directly from the channel definition and runs deterministic Bron--Kerbosch enumeration with a valid cardinality upper-bound prune. It finds maximum clique size \(16\) and exactly four cliques of that size, and then checks the four listed codebooks directly by pairwise error-ball disjointness. For each maximum it also checks closure under binary addition and under the complement map \(x\mapsto x\oplus 111111\). Exactly one codebook is closed under binary addition; exactly two are complement-closed; the complement permutation on the ordered list of four maxima is \((1\,4)\) with the other two fixed.

## Verification
Running `python3 verify.py` returns exactly:

`VERIFY_OK maximum=16 labeled_maxima=4 linear_maxima=1 complement_closed=2 complement_map=3,1,2,0`

No random search, optimization solver, external package, timeout conclusion, or unproved extrapolation is used. The enumeration is over the complete finite graph on all \(64\) words.

## Relationship to prior work
Gabrys, Yaakobi, and Dolecek define the same overlapping grain-error model and the notation \(M(n,t)\), and their Table II summarizes upper and lower bounds for single-grain codes; its surrounding discussion describes computerized searches and constructions rather than a census of all maximum codebooks. Their paper also emphasizes group-code constructions, making the distinction between the unique linear extremizer and the three nonlinear extremizers structurally relevant. The known value \(M(6,1)=16\) is therefore not claimed as new here; the contribution is the complete labeled extremizer census and the stated linear/complement structure.

Targeted searches using the terms “single-grain”, “grain-error”, \(M(6,1)\), “mineral-error”, “overlapping”, “non-overlapping”, “maximum codes”, “classification”, and the numerical count did not locate a publication stating or implying this four-code census. Sharov and Roth's closely related granular-media work was checked at the bibliographic/abstract level; its full text was not available in the accessible source during this comparison, so an unindexed or unadvertised finite census there remains a residual risk.

## Limitations
This is a finite exact classification at one parameter point. It does not classify maximum single-grain codes at other lengths, nor does it claim a new upper bound for \(M(6,1)\). The literature comparison cannot exclude an obscure unindexed enumeration, especially inside inaccessible supplementary or thesis material.

## References
1. R. Gabrys, E. Yaakobi, and L. Dolecek, “Correcting Grain-Errors in Magnetic Media,” arXiv:1307.7087, first public 2013-07-26; later IEEE Transactions on Information Theory 61(5), 2015, DOI:10.1109/TIT.2015.2409860.
2. A. Sharov and R. M. Roth, “Bounds and Constructions for Granular Media Coding,” IEEE Transactions on Information Theory 60(4), 2014, DOI:10.1109/TIT.2014.2301811.
