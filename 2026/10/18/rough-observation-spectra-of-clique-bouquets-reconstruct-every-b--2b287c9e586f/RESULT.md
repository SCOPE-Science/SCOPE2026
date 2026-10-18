# Rough-observation spectra of clique bouquets reconstruct every block size

## Finding
Let \(r\ge 2\), and let \(s_1,\ldots,s_r\ge 2\) be integers. Form the clique bouquet \(W(s_1,\ldots,s_r)\) from disjoint cliques \(B_i\) of \(s_i\) peripheral vertices by adjoining a single hub \(h\) adjacent to every peripheral vertex; no edges join different \(B_i\). Use the same reflexive adjacency relation for both rough approximation operators. Put \(a_i=2^{s_i}-1\) and \(P=\prod_{i=1}^r a_i\).

The collection of distinct observations \(\rho(X)=(L(X),U(X))\), for all vertex subsets \(X\), contains exactly \(2^{r+1}-1\) elements. Its **unlabeled inverse-fiber multiplicity multiset**, including repetitions for distinct observations, is exactly
\[
\{1,1,2P\}\ \uplus\ \biguplus_{\varnothing\ne S\subsetneq [r]}
\left\{\prod_{i\in S}a_i,\prod_{i\in S}a_i\right\}.
\]
The unique maximum fiber is the completely uncertain observation \((\varnothing,V)\), of cardinality \(2P\). The second-largest fiber cardinality is \(P/\min_i a_i\), attained by exactly twice the number of minimum-size peripheral cliques. Moreover, this unlabeled multiset uniquely determines the multiset \(\{s_1,\ldots,s_r\}\), hence determines the clique bouquet up to graph isomorphism. In contrast, the number \(2^{r+1}-1\) of distinct observations is independent of all clique sizes.

For uniformly random \(X\subseteq V\), the observation min-entropy is exactly
\[
H_\infty(\rho(X))=\sum_{i=1}^r\left(s_i-\log_2(2^{s_i}-1)\right).
\]

## Assumptions and scope
The graph is finite, simple, undirected; every peripheral clique has at least two vertices and there are at least two cliques. For each vertex \(v\), write \(N[v]\) for its closed neighborhood. For all \(X\subseteq V\) define \(L(X)=\{v:N[v]\subseteq X\}\) and \(U(X)=\{v:N[v]\cap X\ne\varnothing\}\). An inverse fiber comprises all subsets \(X\) with one fixed ordered pair \((L(X),U(X))\). Observations are counted as *distinct ordered pairs*, even if their fibers have equal size. The spectrum forgets observation labels but retains these multiplicities. The cases of a single peripheral clique or singleton peripheral cliques are not asserted.

## Proof
The neighborhoods are \(N[h]=V\) and \(N[v]=\{h\}\cup B_i\) for \(v\in B_i\). First suppose \(h\notin X\). Then \(L(X)=\varnothing\). Let \(S=\{i:X\cap B_i\ne\varnothing\}\). If \(S=\varnothing\), then \(U(X)=\varnothing\); otherwise \(U(X)=\{h\}\cup\bigcup_{i\in S}B_i\). Each active clique may contribute any of its \(a_i\) nonempty subsets, while inactive cliques contribute none, so the corresponding inverse fiber has size \(\prod_{i\in S}a_i\).

Now suppose \(h\in X\). Then \(U(X)=V\). Let \(T=\{i:B_i\subseteq X\}\). If \(T\subsetneq[r]\), then \(L(X)=\bigcup_{i\in T}B_i\) because the hub is lower-certain only when \(X=V\); for \(T=[r]\), the lower approximation is \(V\). The proper-\(T\) fiber cardinality is \(\prod_{i\notin T}a_i\), because each non-full clique has exactly \(a_i=2^{s_i}-1\) choices.

There are \(2^r\) observations of the first form, one per \(S\), and \(2^r\) of the second, one per \(T\). Within each form, the observations are distinct. Between forms, equality forces \(U=V\) and \(L=\varnothing\), hence precisely the conjunction \(S=[r]\) and \(T=\varnothing\). Those two fibers merge into the single completely uncertain observation, of total size \(2P\). The two endpoint observations have singleton fibers, and all remaining proper nonempty subsets of indices occur twice with the multiplicities stated. This proves the spectrum and count.

Since every \(a_i>1\), every noncentral fiber has size at most \(P/a_{\min}\), attained precisely by deleting a single factor of minimum size from the full product, in either of the two observation families. Therefore the central fiber is the unique maximum and the exact runner-up count follows.

To reconstruct without labels, read \(r\) from the observation count \(2^{r+1}-1\) and \(P\) from half the largest multiplicity. Remove the unique largest entry and two singleton entries from the spectrum, halve the remaining entry multiplicities, and adjoin the two entries \(1\) and \(P\). The result is the multiset \(M\) of all \(2^r\) subproducts \(\prod_{i\in S}a_i\), including the empty and full products. This multiset has a unique factor multiset with factors greater than one: begin with the accounted multiset \(A=\{1\}\). The least element of the multiset difference \(M\setminus A\) equals the smallest as-yet-undetermined factor \(a\), because every new product uses an undetermined factor and multiplying it by other factors greater than one can only increase it. Replace \(A\) with its multiset union with \(aA\), and repeat \(r\) times. This handles repeated factors and accidental equalities between different subset products because multiplicities are retained. The recovered factors uniquely determine \(s_i=\log_2(a_i+1)\) as integers. The unlabeled bouquet is thereby reconstructed.

Finally, with \(n=|V|=1+\sum_i s_i\), a uniformly sampled \(X\) has probability \(2P/2^n\) of the central observation, and no other observation has as much probability. By the definition \(H_\infty=-\log_2\max_Q\mathbb P(\rho(X)=Q)\), the stated formula follows.

## Verification
The accompanying standalone Python program `verify_clique_bouquet.py` constructs the closed neighborhoods, enumerates all input vertex subsets, directly computes both rough approximations, and compares the complete observed inverse-fiber spectrum with the theorem. It also verifies the runner-up multiplicity and the factor-reconstruction procedure with multiplicities. In the completed run it returned: `VERIFY_OK profiles= 141 vertex_subsets= 551328 fiber_spectrum=PASS central_uniqueness=PASS runnerup=PASS size_reconstruction=PASS`. These checks include nonsymmetric clique sizes and repeated clique sizes. The all-parameter claim follows from the explicit proof, not from finite exhaustive testing.

## Relationship to prior work
Järvinen and Radeleczki (2023) study rough sets from arbitrary reflexive relations and their Dedekind–MacNeille completions, in particular the same lower/upper approximation definitions. Their treatment concerns pseudo-Kleene and related algebraic structures, not inversion of a rough observation map for clique bouquets. Dhanalakshmi and Parvathi (2017) study prime labeling of upper-approximation subgraphs for friendship graphs (the all-two-vertex-blade specialization); the accessible abstract addresses labeling rather than exact inverse-fiber spectra. The latter paper's full text was not available in this examination, so its details beyond the abstract are not asserted. The subset-product recovery step is a standard positive-factor reconstruction argument; novelty is not claimed for that elementary device alone. The contribution assessed here is the combined exact observation spectrum, sharp multiplicity ranking, and complete graph reconstruction on the entire heterogeneous bouquet family.

## Limitations
This is an exact theorem only for clique bouquets with at least two peripheral cliques of size at least two. No extension to arbitrary block graphs, trees of cliques, or relations other than reflexive adjacency is claimed. A published equivalent reformulation of the specialized inverse-fiber theorem could exist; novelty has not been independently adjudicated. The finite verifier is corroborative, not a substitute for the proof.

## References
- Jouni Järvinen and Sándor Radeleczki, *Pseudo-Kleene algebras determined by rough sets*, first arXiv posting 2023-04-12, https://arxiv.org/abs/2304.05641 .
- S. Dhanalakshmi and N. Parvathi, *Prime Labeling of Rough Approximations for Some Special Graphs*, *Indian Journal of Science and Technology* **10** (2017), 1–5, DOI:10.17485/ijst/2017/v10i25/97915 .
