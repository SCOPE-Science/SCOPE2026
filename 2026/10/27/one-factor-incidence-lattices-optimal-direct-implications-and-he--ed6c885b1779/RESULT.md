# One-factor incidence lattices: optimal direct implications and Hermite Möbius invariants

## Finding

Fix an integer \(n\ge3\), and let \(E\) be the edges of the complete simple graph \(K_{2n}\). Regard all perfect matchings (one-factors) of \(K_{2n}\) as objects of a formal context, and edges as attributes, with membership incidence. Define the attribute closure \(c(S)\) of any \(S\subseteq E\) as the intersection of all perfect matchings containing \(S\); by convention the intersection of an empty family is \(E\).

The closed sets are precisely \(E\), all perfect matchings, and all matchings of cardinality at most \(n-2\). The inclusion lattice \(L_n\) is graded, with rank polynomial
\[
R_n(t)=\sum_{k=0}^{n-2}\frac{(2n)!}{(2n-2k)!\,2^k k!}t^k+(2n-1)!!\,t^{n-1}+t^n.
\]

The inclusion-minimal nonclosed subsets (equivalently, the Duquenne–Guigues pseudo-intents) are exactly the unordered pairs of incident distinct edges and the \((n-1)\)-edge matchings. The implications from each such premise to its actual closure form a **one-synchronous-round direct basis with the globally smallest possible number of multi-conclusion implications**:
\[
B_n=2n\binom{2n-1}{2}+n(2n-1)!!.
\]
The minimality assertion holds among all complete implication bases, including bases allowed to use repeated forward-chaining passes, and counts each nontrivial multi-conclusion implication as one rule.

Every interval of \(L_n\) has an explicit Möbius value. If \(A\subseteq B\) are closed matching sets with \(|B|\le n-2\), then \(\mu(A,B)=(-1)^{|B|-|A|}\). If \(A\) is a closed matching of size at most \(n-2\) and \(M\supset A\) is perfect, then, writing \(r=n-|A|\),
\[
\mu(A,M)=(-1)^{r-1}(r-1).
\]
For the greatest element \(E\), if \(A\) is a closed matching of size at most \(n-2\), put \(m=n-|A|\). Then
\[
\boxed{\mu(A,E)=-\operatorname{He}_{2m}(1)
=-\sum_{k=0}^{m}(-1)^k\frac{(2m)!}{(2m-2k)!\,2^k k!},}
\]
where \(\operatorname{He}_{j}\) is the probabilists' Hermite polynomial; \(\mu(M,E)=-1\) for perfect \(M\), and \(\mu(X,X)=1\) for every closed \(X\). These formulas cover every comparable pair.

For each closed partial matching \(A\) leaving \(2m\ge4\) uncovered vertices, the open interval \((A,E)\) has the **simple-homotopy type** of the ordinary matching complex \(\mathcal M(K_{2m})\). In particular, \((\varnothing,E)\) in \(L_3\) is homotopy equivalent to a wedge of sixteen circles, and the corresponding interval in \(L_4\) to a wedge of 132 two-spheres; those matching-complex homotopy types are known results transferred here, not newly determined homotopy types of the matching complexes.

## Assumptions and scope

All graphs are finite, simple, and loopless. A matching is a set of pairwise vertex-disjoint edges; a perfect matching has \(n\) edges. The ground set \(E\) contains \(\binom{2n}{2}\) attributes. For a family \(\mathcal F\) of subsets of \(E\), the intersection \(\bigcap\varnothing=E\). An implication \(P\to Q\) is nontrivial when \(Q\nsubseteq P\). A simultaneous pass applies all rules whose premises are subsets of the *original* input, without allowing conclusions derived during that pass to trigger further rules. For the basis in the theorem, use \(P\to c(P)\setminus P\) for each listed minimal nonclosed \(P\). The claim intentionally excludes \(n=2\): there singleton assertions already force completions, and the minimal-premise classification changes.

The lattice order is inclusion of closed attribute sets; its bottom is the empty matching and its top is the full edge set \(E\). The order complex of \((A,E)\) is the simplicial complex of its nonempty chains. The ordinary matching complex \(\mathcal M(G)\) has nonempty faces equal to nonempty matchings of \(G\), together with the empty face as the simplicial convention.

## Proof

**1. Closure and its fixed sets.** If \(S\) has two incident distinct edges, no perfect matching can contain it, so \(c(S)=E\). Otherwise \(S\) is a matching of size \(k\), leaving a complete graph on \(2(n-k)\) vertices for completion. If \(k=n\), the completion is already unique and \(c(S)=S\). If \(k=n-1\), precisely two unmatched vertices remain and their joining edge is forced: \(c(S)\) is the unique perfect extension. If \(k\le n-2\), at least four vertices remain. Each unused edge is absent from some perfect matching of the remaining complete graph: choose two alternative partners among four residual vertices, and pair the remaining residual vertices arbitrarily. Thus no unused edge belongs to the intersection, and \(c(S)=S\). Since \(n\ge3\), \(E\) is not itself a matching and is distinct from the other closed sets. This proves the classification.

**2. Minimal nonclosed premises and sharp basis.** Every incident edge pair is nonclosed and its two singleton subsets are closed (as \(n\ge3\)). Every \((n-1)\)-matching is nonclosed, whereas all its proper subsets are closed. Conversely a nonclosed set is either an infeasible set containing an incident pair or a feasible \((n-1)\)-matching. Therefore these and only these are inclusion-minimal nonclosed sets. Any implication basis that generates this closure needs at least one rule with *exactly* each minimal nonclosed \(P\) as premise: starting from \(P\), a first rule adding a genuinely new attribute cannot have a proper subset as its premise, since every proper subset is closed, and the premise cannot strictly contain \(P\). Distinct minimal nonclosed sets require distinct rules. The proposed rules suffice in a single synchronous round, because every nonclosed input contains one of these premises, while no premise fires with a new conclusion inside a closed input. Hence the lower bound is attained even among arbitrary iterative bases. The number of incident unordered edge pairs is \(2n\binom{2n-1}{2}\): each pair shares exactly one vertex, and there are \(\binom{2n-1}{2}\) choices around each vertex. The number of perfect matchings is \(P_n=(2n-1)!!\); deleting one of its \(n\) edges gives a distinct \((n-1)\)-matching, each of which has a unique completion, so there are \(nP_n\) such premises. A nonclosed set has no proper nonclosed subset unless it contains one of these minimal premises; hence the recursive pseudo-intent condition eliminates all other nonclosed sets, and the two stated families are precisely the pseudo-intents.

**3. Rank polynomial and Möbius function.** The number of \(k\)-matchings in \(K_{2n}\) is
\[
a_{n,k}=\binom{2n}{2k}\frac{(2k)!}{2^k k!}=\frac{(2n)!}{(2n-2k)!2^k k!}.
\]
A perfect matching has rank \(n-1\) because the near-complete rank is missing, and \(E\) has rank \(n\); all other matchings have rank equal to cardinality, which establishes grading and the rank polynomial. Intervals \([A,B]\) between partial closed matchings are Boolean. The interval below a perfect \(M\supsetneq A\), with \(r=n-|A|\), consists of all submatchings \(A\cup F\) for \(|F|\le r-2\), and \(M\) itself. The Möbius recurrence gives
\[
\mu(A,M)=-\sum_{j=0}^{r-2}(-1)^j\binom rj=(-1)^{r-1}(r-1).
\]
The interval \([A,E]\) is isomorphic to \(L_m\) for \(m=n-|A|\), by deleting vertices covered by \(A\). The recurrence for \(\mu(A,E)\), together with the previous formula and \(a_{m,m-1}=mP_m\), gives
\[
\mu(A,E)=-\left[\sum_{j=0}^{m-2}(-1)^j a_{m,j}+(-1)^{m-1}(m-1)P_m\right]
=-\sum_{j=0}^{m}(-1)^j a_{m,j}.
\]
This is \(-\operatorname{He}_{2m}(1)\) by the elementary explicit Hermite sum. Every perfect matching is covered by \(E\), giving \(\mu(M,E)=-1\). All diagonal intervals have Möbius value one.

**4. Topological identification.** Fix a closed partial matching \(A\), leaving \(2m\ge4\) vertices uncovered. Let \(P\) be the face poset of nonempty matchings on these vertices, and let \(Q=(A,E)\), ordered by inclusion. The map \(\varphi:P\to Q\) sends \(F\) to \(c(A\cup F)\). It is order preserving and surjective. For each \(B\in Q\), the inverse image of its principal downset is exactly the nonempty matchings \(F\subseteq B\setminus A\), a poset with greatest element \(B\setminus A\). Each such fiber is contractible. The finite poset fiber lemma (with its simple-homotopy strengthening) yields a simple-homotopy equivalence of their order complexes. The order complex of \(P\) is the barycentric subdivision of \(\mathcal M(K_{2m})\), which has the same simple-homotopy type. Published homotopy types for \(\mathcal M(K_6)\) and \(\mathcal M(K_8)\) therefore transfer to the stated intervals.

## Verification

The standalone `verify.py` constructs all perfect matchings independently, reconstructs closure by literal intersection, and compares it with both the structural classification and the proposed simultaneous rule basis. It tests all \(2^{15}=32768\) subsets of the fifteen edges of \(K_6\), all 345 predicted closed sets of \(K_8\), and 15,000 reproducible additional subsets of the 28 edges of \(K_8\). It also computes, directly from the finite closed-set poset, all 138 comparable intervals of \(L_3\) and all 2502 comparable intervals of \(L_4\), testing every listed Möbius formula. It confirms 105 rules and 32 closed sets for \(n=3\), and 588 rules and 345 closed sets for \(n=4\). Run with `python verify.py`; no third-party Python packages are needed. These tests are finite corroboration, not substitutes for the general proof or for an independent literature review.

## Relationship to prior work

Baixeries and Napoli (arXiv:2404.12229, first public version 2024-04-18) study the tradeoffs between minimum-size and one-pass direct implication bases in general closure systems. The statements above supply a special-context optimality classification not reported in their relevant definitions and comparison sections. Mondal, Mukherjee and Saha (arXiv:2305.02973, first public version 2023-05-04) investigate the ordinary matching complexes of complete graphs and provide the known homotopy types of \(\mathcal M(K_6)\) and \(\mathcal M(K_8)\); the current assertion is a transfer to a different, explicitly defined lattice, not a claim to have discovered those matching-complex homotopy types. Barmak's finite-poset version of Quillen's fiber theorem supplies the general simple-homotopy tool; the concrete fibers are established above.

The corresponding complete-bipartite permutation-incidence closure has different matching counts, Laguerre rather than Hermite Möbius polynomials, and chessboard rather than complete-graph matching complexes. Its published or independently recorded special-case statements do not imply the nonbipartite formulas merely by changing notation. The elementary count of matchings in \(K_{2n}\), standard Hermite identities, and generic fiber theorem are established ingredients; novelty is asserted only for their precise incidence-closure synthesis, subject to external priority review.

## Limitations

The result applies to complete *nonbipartite* graphs on \(2n\ge6\) vertices and to **positive** edge-attribute incidence. It does not classify closure systems of arbitrary matching-covered graphs, alternative incidence conventions, or minimal numbers of single-conclusion rules. Its finite checks do not prove the infinite-parameter formulas, which depend on the proof. Known matching-complex homotopy results are transferred, not independently reproved. Equivalent results under the terminology of one-factors, matching-hypergraph logical consequences, or closure quotients might exist outside the inspected literature; no universal publication-priority claim is made.

## References

1. J. Baixeries and A. Napoli, *A minimal base or a direct base? That is the question!*, arXiv:2404.12229, first submitted 2024-04-18, https://arxiv.org/abs/2404.12229.
2. A. Mondal, S. Mukherjee and K. Saha, *Topology of matching complexes of complete graphs via discrete Morse theory*, arXiv:2305.02973, first submitted 2023-05-04, https://arxiv.org/abs/2305.02973.
3. J. A. Barmak, *On Quillen's Theorem A for posets*, Journal of Combinatorial Theory, Series A 118 (2011), 2445–2453, arXiv:1005.0538, https://arxiv.org/abs/1005.0538.
