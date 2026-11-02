# Rainbow-matchings characterize all shattered comparisons of single-peaked rankings

## Finding
Fix a known linearly ordered axis \(1<2<\cdots<n\), \(n\geq 1\). Let \(\mathcal{SP}_n\) contain every strict linear preference order that is single-peaked on this axis, viewed as a binary concept on the unordered comparison queries \(\{i,j\}\), \(1\leq i<j\leq n\). A set \(S\) of queries is VC-shattered **if and only if**, for \(d=|S|\), there are \(2d\) distinct axis elements \(a_1<\cdots<a_d<b_d<\cdots<b_1\) such that
\[
S=\big\{\{a_t,b_t\}:1\leq t\leq d\big\}.
\]
The empty support qualifies. In other words, the query intervals form a strictly nested matching (a *rainbow matching*). For each \(d\), exactly \(\binom n{2d}\) supports of cardinality \(d\) are shattered. Consequently the **complete shattering polynomial** is
\[
P_n(z)=\sum_{d=0}^{\lfloor n/2\rfloor}\binom n{2d}z^d
=\tfrac12\big((1+\sqrt z)^n+(1-\sqrt z)^n\big),
\]
and \(\operatorname{VCdim}(\mathcal{SP}_n)=\lfloor n/2\rfloor\). Moreover, \(|\mathcal{SP}_n|=2^{n-1}\), the total number of shattered supports is also \(2^{n-1}\) (the concept family is shattering-extremal), and
\[
\operatorname{Ldim}(\mathcal{SP}_n)=n-1.
\]
Thus the adaptive-versus-static gap is \(n-1-\lfloor n/2\rfloor\), unbounded along a single fixed-axis preference domain.

## Assumptions and scope
A strict preference order is single-peaked on the fixed axis if for every triple \(i<j<k\), the middle alternative \(j\) is not ranked worse than both extremes. Write \(u\succ v\) to mean \(u\) is preferred to \(v\). For comparison \(\{i,j\}\), the concept reports whether \(i\succ j\) when \(i<j\). Shattering means all \(2^{|S|}\) assignments to a *fixed* set of comparison queries are realized by single-peaked orders; Littlestone shattering instead allows queries to depend on earlier answers. The axis is known, complete rankings have no ties, and \(n\) is any positive integer. Neither unknown-axis single-peakedness nor partial/tied ballots are covered.

## Proof
**1. The removal characterization.** A strict order is single-peaked exactly when, from worst to best, it repeatedly removes one of the two endpoints of the surviving axis segment. Indeed, if a middle point were globally worst among the remaining alternatives, it would be below surviving alternatives on both sides, violating the no-valley property. Conversely, removal of endpoints never makes a point lying between two others worst among that triple. The last surviving point is the peak. There are two choices at each of \(n-1\) removals, so \(|\mathcal{SP}_n|=2^{n-1}\).

**2. Every nonnested pair of distinct queries obstructs shattering.** For any axis triple \(i<j<k\), the no-valley axiom forbids \(i\succ j\) together with \(k\succ j\). In particular, \(i\succ j\) forces \(j\succ k\), and \(k\succ j\) forces \(j\succ i\). We distinguish the exhaustive configurations of two comparison intervals that are *not* strictly nested with four distinct endpoints.

* If \(a<b<c<d\), queries \(\{a,b\},\{c,d\}\) cannot simultaneously receive the answers \(a\succ b\), \(d\succ c\): the triples \(a<b<c\) and \(b<c<d\) respectively force \(b\succ c\) and \(c\succ b\).
* If \(a<c<b<d\), queries \(\{a,b\},\{c,d\}\) cannot simultaneously receive \(a\succ b\), \(d\succ c\): triples \(a<c<b\) and \(c<b<d\) force \(c\succ b\) and \(b\succ c\).
* If queries share one axis vertex \(a<b<c\), there are three possibilities. For \(\{a,b\},\{b,c\}\), request \(a\succ b\) and \(c\succ b\). For \(\{a,b\},\{a,c\}\), request \(a\succ b\) and \(c\succ a\), which implies the forbidden two-sided domination of \(b\). For \(\{a,c\},\{b,c\}\), request \(a\succ c\) and \(c\succ b\), likewise leaving \(b\) below both extremes. Every requested assignment is inconsistent with single-peakedness.

Hence a shattered \(S\) must have pairwise disjoint endpoints and pairwise strictly nested query intervals. Ordering its queries by increasing left endpoint makes their right endpoints strictly decrease, giving precisely the asserted rainbow form.

**3. Sufficiency and the extension lemma.** Fix any rainbow matching \(S\). On its \(2d\) endpoints, choose the preference orientation of every queried pair arbitrarily. Construct a worst-to-best ranking by successively removing the less-preferred vertex of the outermost matched pair, then its partner, and continuing with the next nested pair. Each removal is an endpoint of the still-surviving selected axis, so this is single-peaked on the selected set, and it realizes the prescribed comparisons.

Any single-peaked ranking on a subset \(T\) of the axis extends to a single-peaked ranking on the full axis: follow its worst-to-best endpoint-removal sequence. Before removing a selected endpoint, remove all currently surviving *unselected* vertices beyond it on that same axis side. The selected endpoint is now an actual endpoint; remove it and continue. Remove leftover unselected vertices at the end. This constructs the required full single-peaked ranking and preserves every comparison between vertices of \(T\). Thus every assignment on \(S\) occurs, proving sufficiency.

**4. Counts and VC dimension.** For any chosen set \(U\) of \(2d\) axis vertices, exactly one rainbow matching exists: pair the smallest with largest, the second smallest with second largest, and so forth. Conversely, every rainbow support determines \(U\) uniquely. Its count is therefore \(\binom n{2d}\), including the empty set at \(d=0\). The largest attainable \(d\) is \(\lfloor n/2\rfloor\). The stated generating function is the even-degree part of a binomial expansion, and the sum of its coefficients is the number of even subsets of an \(n\)-set, \(2^{n-1}\), equal to the number of concepts.

**5. Littlestone dimension.** A depth-\(d\) complete binary shattering tree needs at least \(2^d\) distinct concepts, so \(\operatorname{Ldim}\le n-1\). A matching complete tree of depth \(n-1\) is obtained as follows. At each node, compare the two endpoints of the surviving axis segment. Exactly the endpoint declared worse must be the worst remaining alternative in any single-peaked ranking, so each branch commits to that endpoint's removal and leaves an unrestricted single-peaked ranking problem on the remaining segment. Repeat until one vertex remains. Every length-\(n-1\) branch sequence specifies a distinct single-peaked preference order, giving the lower bound and equality. The \(n=1\) case has a single concept and both dimensions zero.

## Verification
The accompanying standard-library program `verify_single_peaked.py` independently constructs all fixed-axis single-peaked rankings for each \(1\le n\le 9\), computes the comparison concept masks, enumerates **all** shattered supports by a complete hereditary backtracking, compares them against the exact rainbow-support set generated from axis endpoint choices, and computes the exact Littlestone dimension by a memoized adversarial recursion. Its output, `verification_output.txt`, records the support distribution and state counts for each \(n\), ending with `SINGLE_PEAKED_SUPPORT_CLASSIFICATION_ALL_CHECKS_PASS`. These finite tests corroborate rather than replace the proof for arbitrary \(n\).

To replay: `python verify_single_peaked.py`. No third-party dependencies are required.

## Relationship to prior work
Conitzer, *Eliciting Single-Peaked Preferences Using Comparison Queries* (2009), proves linear comparison-query elicitation bounds and explicitly constructs a family of independently selectable nested comparisons for its information lower bound (Section 3.1, Theorem 1). That construction already supplies a special-case lower bound and is **not** claimed here as new. The present result instead gives an **if-and-only-if characterization of every shattered support**, the exact count at every support size, shattering-extremality, and the exact adaptive dimension.

Fitzsimmons and Lackner, *Incomplete Preferences in Single-Peaked Electorates* (arXiv 1907.00752, first public 2019-07-01), study when incomplete preference constraints extend to single-peaked orders, including efficient consistency testing for a fixed known axis (Section 1.1 and Section 7). Such feasibility algorithms do not themselves state or entail the all-support rainbow classification or counting polynomial without further argument. Peters, Yu, Chan and Elkind, *Preferences Single-Peaked on a Tree* (arXiv 2007.06549, first public 2020-07-13), study structural recognition and multiwinner optimization for general tree axes, not the pair-comparison support enumerator on one fixed path. Mészáros and Rónyai (arXiv 1211.0732, 2012) develop general shattering-extremal set system theory, but do not provide this preference-specific structure. Chase, Freitag and Reyzin (arXiv 2310.04812, 2023) give general Littlestone-dimension theory, not this fixed-axis value.

## Limitations
The proof applies to a **specified known axis** and strict complete single-peaked rankings; changing the axis family, allowing ties, or querying preference statements other than pair comparisons yields different concept classes. The classification does not assert all possible equivalent historical descriptions have been found; overlapping results in older social-choice or learning-theory literature remain a priority risk. The exact structure and all-order proof do not depend on computations, and computational corroboration is restricted to \(n\le9\). No independent scientific audit has been performed.

## References
- V. Conitzer, "Eliciting Single-Peaked Preferences Using Comparison Queries," *Journal of Artificial Intelligence Research* **35** (2009), 161–191, doi:10.1613/jair.2606, https://www.cs.cmu.edu/~conitzer/singlepeakedJAIR.pdf.
- Z. Fitzsimmons and M. Lackner, "Incomplete Preferences in Single-Peaked Electorates," arXiv:1907.00752 (first public 2019-07-01), https://arxiv.org/abs/1907.00752; *JAIR* **67** (2020), 797–833.
- D. Peters, L. Yu, H. Chan, and E. Elkind, "Preferences Single-Peaked on a Tree: Multiwinner Elections and Structural Results," arXiv:2007.06549 (first public 2020-07-13), https://arxiv.org/abs/2007.06549.
- T. Mészáros and L. Rónyai, "Shattering-Extremal Set Systems of Small VC-Dimension," arXiv:1211.0732 (2012), https://arxiv.org/abs/1211.0732.
- H. Chase, J. Freitag and L. Reyzin, "Applications of Littlestone dimension to query learning and to compression," arXiv:2310.04812 (2023), https://arxiv.org/abs/2310.04812.
