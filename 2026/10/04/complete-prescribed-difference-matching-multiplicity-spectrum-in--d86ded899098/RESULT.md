# Complete prescribed-difference matching multiplicity spectrum in dimension four

## Finding
Let \(V=\mathbb F_2^4\). For a multiset \(M\) of eight nonzero vectors with XOR sum zero, define \(R(M)\) to be the number of unordered perfect matchings of the sixteen vertices of \(V\) whose eight edge differences, counted with multiplicity, form \(M\).

There are exactly \(20{,}295\) admissible multisets \(M\), and every one is realized. More precisely, the complete distribution of the realization number is
\[
\begin{array}{c|rrrrrrrrrrrrrrrr}
r&1&4&6&12&16&24&32&40&48&64&88&96&128&160&224&384\\
\hline
\#M&15&210&105&1365&735&420&1890&840&840&3360&105&3360&2520&1575&2520&435.
\end{array}
\]
The fifteen profiles with \(R(M)=1\) are exactly the constant profiles containing eight copies of one nonzero vector. Consequently every nonconstant admissible profile has at least four distinct perfect-matching realizations.

## Assumptions and scope
Vertices are the vectors of \(\mathbb F_2^4\), encoded by four-bit words. The difference of an unordered edge \(\{x,y\}\) is \(x+y\), which is nonzero because \(x\ne y\). A profile is an unordered multiset of eight such nonzero differences. The necessary zero-sum condition is \(\bigoplus_{d\in M}d=0\), because every vertex occurs exactly once in a perfect matching.

The count \(R(M)\) regards a perfect matching as an unordered set of eight unordered edges. Reordering equal or unequal requests does not create a new realization.

## Proof
The statement is a finite exact classification. The attached verifier uses two exhaustive enumerations whose coverage can be checked directly from their recursion invariants.

First, it enumerates perfect matchings. At each recursion node it chooses the least unused vertex \(x\) and pairs it once with each possible other unused vertex \(y\). This produces every perfect matching exactly once: every matching has a unique edge incident with its least currently unused vertex, and deleting that edge leaves the same canonical subproblem. The recursion produces \(2{,}027{,}025=15!!\) matchings, the independent closed count for perfect matchings on sixteen labeled vertices. For each matching it sorts the eight XOR differences and increments the resulting canonical profile.

Second, independently of the matching recursion, it enumerates every nondecreasing eight-tuple with entries in \(\{1,\ldots,15\}\) and retains exactly those whose bitwise XOR is zero. Nondecreasing tuples are in bijection with multisets, so this is an exhaustive enumeration of the admissible profiles. It obtains exactly \(20{,}295\) profiles.

The two key sets agree exactly. This simultaneously verifies that every admissible profile is realized and that no nonadmissible profile has entered the table. Tallying the exact integer realization counts gives the displayed sixteen-value histogram, whose frequencies sum to \(20{,}295\), while its multiplicity-weighted sum is \(2{,}027{,}025\).

Finally, the profiles of multiplicity one are checked directly from the same exact table: there are fifteen and each is constant. Conversely, for a fixed nonzero \(d\), the edges \(\{x,x+d\}\) form the unique perfect matching all of whose differences equal \(d\), so all fifteen constant profiles indeed have one realization. The smallest realization count among the remaining profiles is four.

## Verification
Running `verify_bgs_s4_counts.py` rebuilds the classification from no stored table of matchings. It checks the independent totals \(15!!=2{,}027{,}025\) and \(20{,}295\), equality of the independently generated admissible-profile and matching-profile sets, the full histogram, the characterization of the fifteen unique profiles, and the gap from one to four. On the packaged source it ends with `VERIFY_OK`.

The exhaustive argument is finite: it proves only the dimension-four classification stated here and makes no inference about higher dimensions from the observed spectrum.

## Relationship to prior work
Balister, Győri and Schelp introduced the prescribed-difference problem, and the dimension-four existence case is already known. Yohananov and Essayag later reformulated the problem in functional-batch-code language and emphasized that the general conjecture remains open. A recent character-theoretic treatment by Zabokritskiy states that dimensions at most five are known solvable and develops exact realization-count coefficients for the all-crossing Hall subfamily, explicitly highlighting enumerative information beyond existence.

The present statement is different from those existence results and from the Hall-subfamily coefficient theorem: it gives the complete exact realization-count distribution over all zero-sum prescribed-difference multisets in the full dimension-four BGS problem, including mixed profiles with respect to every hyperplane. Focused searches for this full \(20{,}295\)-profile spectrum, the realization counts, and the uniqueness gap found no prior table or theorem that implies it.

## Limitations
This is an exact finite census for \(\mathbb F_2^4\), not a formula in arbitrary dimension. It does not classify the \(20{,}295\) profiles up to linear equivalence, nor does it provide a closed formula for \(R(M)\) from profile invariants. The literature comparison cannot exclude an unindexed computation using different terminology. No independent audit has been performed.

## References
1. A. L. Zabokritskiy, “Perfect Matchings with Prescribed Differences Beyond Hall: The Two-Hole Problem,” arXiv:2607.08630, 2026.
2. L. Yohananov and I. B. Essayag, “Optimal Functional \(2^{s-1}\)-Batch Codes: Exploring New Sufficient Conditions,” arXiv:2501.11122, 2025.
3. P. N. Balister, E. Győri and R. H. Schelp, “Coloring vertices and edges of a graph by nonempty subsets of a set,” European Journal of Combinatorics 32 (2011), 533–537, DOI:10.1016/j.ejc.2010.11.008.
