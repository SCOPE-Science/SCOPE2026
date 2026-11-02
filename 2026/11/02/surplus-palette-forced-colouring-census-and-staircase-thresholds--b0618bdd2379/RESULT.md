# Surplus-palette forced-colouring census and staircase thresholds for complete multipartite graphs

## Finding
Let \(r\ge3\), let \(n_1,\ldots,n_r\ge1\), and let \(G=K_{n_1,\ldots,n_r}\) be the labelled simple complete multipartite graph, with \(N=\sum_i n_i\). Fix a palette of \(Q>r\) named colours. The domain-size forcing polynomial \(F_Q(G;z)=\sum_f z^{|\operatorname{dom}f|}\) runs over proper partial assignments which, by repeatedly colouring an uncoloured vertex if its coloured neighbours display exactly \(Q-1\) different colours, force a proper full colouring.

Write \(S(n,s)\) for a Stirling number of the second kind, \(E_i(z)=(1+z)^{n_i}-1\), and \(\mathcal S_Q=\{(s_1,\ldots,s_r):1\le s_i\le n_i,\ \sum_i s_i=Q\}\). For \(\mathbf s\in\mathcal S_Q\) put \(I(\mathbf s)=\{i:s_i=1\}\) and
\[
H_{\mathbf s}(z)=z^{N-\sum_{i\in I(\mathbf s)}n_i}\left(\prod_{i\in I(\mathbf s)} E_i(z)+\sum_{h\in I(\mathbf s)}\prod_{i\in I(\mathbf s)\setminus\{h\}}E_i(z)\right).
\]
Empty products are one and empty sums zero. Let \(P_G(Q)\) be the usual chromatic polynomial evaluation, explicitly
\[
P_G(Q)=\sum_{\substack{1\le s_i\le n_i\\\sum_i s_i\le Q}}(Q)_{\sum_i s_i}\prod_{i=1}^r S(n_i,s_i),
\]
where \((Q)_j=Q!/(Q-j)!\). Then **the entire surplus-palette forced-colouring polynomial** is
\[
\boxed{F_Q(G;z)=P_G(Q)z^N+Q!\sum_{\mathbf s\in\mathcal S_Q}\left(\prod_{i=1}^r S(n_i,s_i)\right)\bigl(H_{\mathbf s}(z)-z^N\bigr).}
\]
The corresponding probability polynomial in Farr's independent partial-colouring model is \(\operatorname{FC}_Q(G;p)=(1-Qp)^N F_Q(G;p/(1-Qp))\), interpreted by polynomial continuation at \(p=1/Q\).

More precisely, every *non-total* successful initial assignment has a unique completion which uses all \(Q\) colours. Relative to that completion, each part containing at least two distinct colours is initially fully coloured; every monochromatic part is initially represented by at least one coloured vertex, except that **at most one** monochromatic part may be completely uncoloured. Conversely, each initial restriction satisfying those conditions is successful. This is a complete classification, not merely a sufficient criterion.

For balanced parts \(G=K_{t,\ldots,t}\), where \(r\ge3\), \(t\ge2\), \(Q>r\), put \(d=Q-r\). If \(1\le d\le(r-1)(t-1)\) and \(k=\lceil d/(t-1)\rceil\), the smallest successful initial domain has size
\[
\boxed{\mu_Q(G)=r-1+k(t-1).}
\]
Its exact multiplicity is
\[
\boxed{[z^{\mu_Q(G)}]F_Q(G;z)=\binom rk(r-k)t^{r-k-1}Q!\,[u^d]\left(\sum_{j=1}^{t-1}S(t,j+1)u^j\right)^k.}
\]
For \(Q>r+(r-1)(t-1)\), **no proper partial colouring with an initially blank vertex can force a full colouring**, and \(\mu_Q(G)=rt\), with \(F_Q(G;z)=P_G(Q)z^{rt}\). For example, on \(K_{2,2,2}\):
\[
\begin{aligned}
F_4(z)&=288z^3+432z^4+288z^5+96z^6,\\
F_5(z)&=360z^4+720z^5+780z^6,\\
F_6(z)&=4080z^6.
\end{aligned}
\]
These exact formulas apply to **every** surplus palette \(Q>r\), including \(Q>N\).

## Assumptions and scope
All graphs are finite, simple and labelled; every partite set is nonempty. Each of the \(Q\) named colours has equal status and unused palette colours are permitted in a complete proper colouring. An initial proper partial assignment may assign the same colour to different vertices of the same independent part, but never to vertices of different parts. A legal forcing step requires exactly \(Q-1\) distinct colours among the *currently coloured neighbours* of the vertex. The rule is deterministic in the resulting colour, and the final proper colouring is unique if the process succeeds. The stated new parameter range is \(r\ge3\), \(Q>r\); chromatic-palette \(Q=r\) results and the separate three-colour complete-bipartite result are pre-existing.

## Proof
**1. Partwise colour restrictions.** A proper full colouring \(c\) of \(G\) uses disjoint sets of colours on distinct parts, so let \(s_i\) be the number of colours used on part \(i\). In particular, \(s_i\ge1\). If a part uses \(s_i\ge2\) colours, then every vertex in that part must be seeded in any successful initial restriction of \(c\). Indeed, at any time the neighbours of a vertex in that part use at most \(Q-s_i\le Q-2\) colours, so no vertex of that part can ever be forced.

If the initial restriction is non-total and successful, consider the first forcing step. Its vertex sees \(Q-1\) colours in the other parts. In a proper full completion, the vertex's part has no colours in common with the other parts. Its own full-colouring palette therefore has exactly one colour, and all \(Q\) colours occur in the completion. Thus the first forced part, and every part with a blank vertex by the preceding observation, is monochromatic. With two monochromatic parts wholly unseeded, every remaining uncoloured vertex sees at most \(Q-2\) colours outside its part at every stage before a force in either empty part, while nonempty monochromatic parts see at most \(Q-2\) because both empty-part colours are absent. No first forcing step can occur. Hence at most one monochromatic part is fully unseeded.

Conversely, fix a surjective proper full colouring \(c\) and seed all vertices in multi-coloured parts. Seed a nonempty subset of each monochromatic part, with at most one monochromatic part completely unseeded. If no part is empty, the seeded vertices collectively display all \(Q\) colours, and each blank vertex sees exactly the other \(Q-1\) colours and is forced to its part's one colour. If one monochromatic part is empty, the seed initially displays all \(Q-1\) other colours, so every vertex in that empty part is forced to its missing colour; then the preceding argument forces all other blanks. This proves both necessity and sufficiency. A successful seed has a unique completion because every forced colour is uniquely determined.

**2. Counting by colour multiplicities.** For any vector \(\mathbf s\) with \(\sum_i s_i\le Q\), the number of proper full colourings having exactly \(s_i\) distinct colours in part \(i\) is
\[
\frac{Q!}{(Q-\sum_i s_i)!}\prod_i S(n_i,s_i).
\]
To see this, partition each part into its \(s_i\) nonempty colour classes in \(S(n_i,s_i)\) ways, then injectively label the resulting classes by named colours. Summing gives \(P_G(Q)\). In a full colouring using exactly \(Q\) colours, each multicoloured part must be seeded completely, contributing \(z^{n_i}\); each monochromatic part \(i\) either contributes a nonempty seed subset \(E_i(z)\), or (for at most one such part) contributes the empty subset \(1\). Thus the complete seed polynomial over the restrictions of that full colouring is exactly \(H_{\mathbf s}(z)\). Subtract \(z^N\) to remove the fully seeded colouring already counted by \(P_G(Q)z^N\); the uniqueness of completion prevents overcounting between full colourings. The displayed Stirling-number formula follows, including the case \(I(\mathbf s)=\varnothing\) when \(H_{\mathbf s}(z)=z^N\).

**3. Balanced critical seed number and multiplicity.** In a surjective full \(Q\)-colouring of \(K_{t,\ldots,t}\), let \(k\) parts use at least two colours. Because each of these parts uses at most \(t\) colours, their extra colours beyond the one-per-part baseline satisfy \(d=Q-r\le k(t-1)\), so \(k\ge\lceil d/(t-1)\rceil\). A successful non-total seed requires at least one monochromatic part, hence \(k\le r-1\). All \(kt\) vertices of multicoloured parts must be seeded; among the \(r-k\) monochromatic parts, all but one require at least one seed. Therefore the seed size is at least \(kt+(r-k-1)=r-1+k(t-1)\). If the indicated range of \(d\) holds, take exactly \(k=\lceil d/(t-1)\rceil\) multicoloured parts and distribute the \(d\) surplus colours among them in positive amounts at most \(t-1\). Such a distribution exists because \(k\le d\le k(t-1)\). A smallest seed colours the multicoloured parts entirely, chooses one unseeded monochromatic part, and seeds one vertex in every other monochromatic part. All these choices force, proving equality.

Choose the \(k\) multicoloured parts in \(\binom rk\) ways, the single unseeded monochromatic part in \(r-k\) ways, and one seeded vertex in each other monochromatic part in \(t^{r-k-1}\) ways. Sum the labelled surjective full colourings over distributions \(d_1+\cdots+d_k=d\), \(1\le d_i\le t-1\): their count is \(Q!\prod_{i=1}^k S(t,d_i+1)\). This yields the displayed exact multiplicity. When \(d>(r-1)(t-1)\), every surjective colouring must use at least two colours in **all** parts, so no blank vertex can ever be forced; nonsurjective full colourings do not enable forcing either. Only full proper initial colourings remain.

## Verification
The accompanying `verify.py` independently enumerates proper partial assignments over the augmented alphabet \(\{0,1,\ldots,Q\}\), with zero denoting blank; applies the original iterative local forcing rule on the labelled graph, counts successful assignments by seed size; and compares this count to the Stirling-number formula calculated separately. It checks 18 graph/palette combinations including \(K_{2,2,2}\), \(K_{1,2,3}\), \(K_{2,2,1,1}\), and \(K_{3,2,1}\), plus boundary bipartite consistency tests. It additionally checks the balanced minimum and leading-coefficient formula for 16 parameter triples. The reconstructed script prints `DIRECT_FORCING_VS_STIRLING_FORMULA_OK 18 cases`, `BALANCED_MINIMUM_AND_MULTIPLICITY_OK 16 cases`, and `VERIFICATION_OK`. Finite computations are corroboration only; the theorem for arbitrary sizes is proved by the part-palette invariant above.

## Relationship to prior work
Farr's *The forced colouring function of a graph* (first public 15 September 2026) introduces the graph-polynomial framework and the exact local rule; its Theorem 7 treats bipartite graphs with two available colours, while its Proposition 9 shows that non-total successful seeds use either \(Q-1\) or \(Q\) colours. The present result explicitly determines how those seed colours are distributed across the parts when \(Q>r\), yielding an all-size Stirling enumerator and a new balanced-palette staircase. Farr's general Proposition 9 alone does not classify successful assignments.

*Forced colourings of complete multipartite graphs at the chromatic palette size* (public 4 October 2026) gives the corresponding product formula only for \(Q=r\). *Forced three-colouring polynomial of complete bipartite graphs* (public 4 October 2026) gives a different, two-part, three-colour case. Their conclusions neither include nor imply the stipulated \(r\ge3\), \(Q>r\) formula or balanced seed threshold; the chromatic-palette formula is recovered formally when \(Q=r\), but is not claimed as new. Complete multipartite graph chromatic-polynomial and Stirling-number identities are standard tools and are not claimed as independent novelties.

## Limitations
The result concerns ordinary proper vertex colouring of complete multipartite graphs, with the *local* forcing rule, not general unique extendability or arbitrary graphs. The balanced multiplicity formula is restricted to equal part sizes; the general polynomial still enumerates every part-size vector. Neither an independent mathematical audit nor an exhaustive historical-priority audit has been performed. Differently named forcing processes or unindexed manuscripts could contain an equivalent surplus-palette result; no such stronger covering theorem was identified in the inspected sources.

## References
1. G. E. Farr, *The forced colouring function of a graph*, arXiv:2609.17108v1, first submitted 2026-09-15. https://arxiv.org/pdf/2609.17108v1
2. *Forced colourings of complete multipartite graphs at the chromatic palette size*, 2026-10-04, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-forced-colourings-of-complete-multipartite-graphs-at-the-chromat--ab08eebc2655
3. *Forced three-colouring polynomial of complete bipartite graphs*, 2026-10-04, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-forced-three-colouring-polynomial-of-complete-bipartite-graphs--3fb93c858f69
