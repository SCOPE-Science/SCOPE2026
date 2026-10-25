# Exact odd-cycle-transversal number of the two-spoke-step generalized Petersen graphs

## Finding
For every integer \(n\ge5\), let \(P(n,2)\) denote the generalized Petersen graph with vertices \(u_i,v_i\) indexed modulo \(n\) and edges \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+2}\). Let \(\tau_{\rm odd}(G)\) be the minimum number of vertices whose deletion makes the remaining induced graph bipartite. Then
\[
\tau_{\rm odd}(P(n,2))=\left\lceil\frac n2\right\rceil+\begin{cases}1,&n\equiv2\pmod4,\\0,&\text{otherwise}.\end{cases}
\]
In particular, the exceptional congruence class \(n\equiv2\pmod4\) needs one more deletion than the universal half-order lower bound. Equivalently, the largest induced bipartite subgraph has \(2n-\lceil n/2\rceil-\mathbf1_{n\equiv2\pmod4}\) vertices.

## Assumptions and scope
All graphs are undirected and simple. The parameter \(n\) is an integer at least five. An odd-cycle transversal is a vertex set meeting every odd cycle; this is equivalent to a vertex-deletion set whose remaining graph admits a proper two-colouring. Deleting all cycles (a feedback vertex set, or decycling set) is a different, more restrictive condition.

## Proof
Encode a putative residual proper two-colouring by columns \(c_i=(a_i,b_i)\in\{-1,0,1\}^2\). The value zero means the corresponding vertex is deleted; the two nonzero values name the bipartition classes. A column is admissible if its two values are unequal whenever both are nonzero, so there are exactly seven admissible columns. The other edge constraints say that any two nonzero consecutive outer values disagree, and any two nonzero inner values at distance two disagree. The number of deletions is \(\sum_i (\mathbf1_{a_i=0}+\mathbf1_{b_i=0})\).

Build a finite directed weighted automaton. A state is an ordered pair \((p,q)\) of admissible columns satisfying the outer-edge constraint; there are 41 states. For admissible columns \(p,q,r\), insert an arc \((p,q)\to(q,r)\) precisely if the outer-edge constraint holds for \(q,r\) and the inner-edge constraint holds for \(p,r\). Give it weight \(w(r)=\mathbf1_{r_1=0}+\mathbf1_{r_2=0}\). Cyclic sequences of length \(n\) are in bijection with length-\(n\) closed directed walks, with equal total deletion weights. This covers disconnected residual graphs without assuming a unique bipartition.

The accompanying dependency-free checker supplies a 41-entry integer potential \(P\), and exhaustively checks on **every arc** \(s\to t\) that
\[
2w(s,t)-1+P(s)-P(t)\ge0.
\]
Summing around any closed walk telescopes the potential and gives \(2\sum_i w_i\ge n\). Hence every transversal has size at least \(\lceil n/2\rceil\).

For a closed walk of length \(n\) and cost exactly \(n/2\), equality forces every arc to have zero reduced weight \(2w-1+P(s)-P(t)=0\). The checker constructs this equality subgraph, finds all its strongly connected components, and verifies that it has exactly one component supporting a directed cycle, with 22 states. It also checks an explicit labelling \(\ell\) of these 22 states by \(\mathbb Z/4\mathbb Z\) with \(\ell(t)-\ell(s)=1\) for **every** equality arc inside that component. Every closed equality walk therefore has length divisible by four. Consequently, when \(n\equiv2\pmod4\), the apparently possible cost \(n/2\) is excluded and the lower bound improves to \(n/2+1\). The full integer potential, component membership, four-level labelling, and the precise enumeration algorithm are printed in the embedded program. The finite tables are independently replayed by the checker rather than assumed to be valid.

For the upper bound, write columns \(A=(0,+1)\), \(B=(-1,+1)\), \(C=(+1,-1)\), \(D=(-1,0)\), \(E=(0,-1)\), and \(F=(+1,0)\). Consider the cyclic words
\[
W_4=ABCD,\quad W_5=ABCED,\quad W_6=ABCDFD,\quad
W_7=ABCDACD,\quad W_8=ABCDABCD.
\]
Each obeys all spoke, rim and distance-two inner constraints, and has respectively 2, 3, 4, 4 and 4 deleted vertices. Every displayed word begins with \(A,B\) and ends in \(D\); its final two inner values are \(-1\) or 0, followed by 0. These boundary conditions directly show that concatenating any of the displayed words preserves the constraints across both junctions, including the distance-two inner constraints. Given any \(n\ge5\), uniquely write \(n=b+4t\) with \(b\in\{5,6,7,8\}\) and \(t\ge0\). The cyclic concatenation \(W_b(W_4)^t\) attains the claimed cost. This proves the upper bound for every integer parameter and completes the equality.

## Verification
Run `python3 VERIFY_GP2_OCT.py`. The checker derives all seven columns, all 41 pair states, all automaton arcs, and independently verifies the stated integer potential inequality. It computes strongly connected components of the equality arcs, asserts the exact cyclic component and its modular levels, and validates each cyclic word and seven repetitions of each concatenation type. As a separate implementation not using the automaton, it constructs each graph directly and exhaustively tests deletion sets for \(5\le n\le12\) by residual breadth-first-search bipartiteness. The latter finite check is supplementary: the finite automaton certificates and concatenation proof establish the infinitely many cases.

## Relationship to prior work
Wei and Li studied *decycling* generalized Petersen graphs, in which deletion must eliminate **every** cycle, not merely odd cycles [1]. Fox, Gera and Stănică established independence-number results for generalized Petersen graphs, including the step-two family [2]; maximal independent sets alone do not determine the maximum union of two disjoint independent sets. Ewell's thesis studies bipartite density via edge deletion, a different optimization variable [3]. Zhu's theorem [5] gives a universal lower bound of \(5/7\) for the induced-bipartite proportion of most 2-connected triangle-free subcubic graphs, whereas the value here is asymptotically \(3/4\); the global bound does not imply a sharp family-specific formula. The well-known criterion for the undeleted graph to be bipartite is distinct from the minimum number of vertices needed to make it bipartite [4]. These distinctions do not themselves certify novelty; they identify the scope of the comparison.

## Limitations
The theorem concerns precisely \(P(n,2)\) for \(n\ge5\); it makes no claim for other inner step sizes, about all minimum transversal configurations, or about the cost of finding them algorithmically in arbitrary graphs. The new certificate gives an exhaustive finite proof of an infinite-periodic formula, while the direct graph experiments cover only \(5\le n\le12\). An unindexed earlier result under the equivalent name “bipartite vertex deletion” or “maximum induced bipartite subgraph” may exist. Relevant publisher and thesis full texts were not all accessible, so no claim of whole-document noncoverage is made for them.

## References
[1] E.-L. Wei and Y.-F. Li, “Decycling Number and Upper-Embeddibility of Generalized Petersen Graphs”, *Acta Mathematica Sinica (Chinese Series)* 56 (2013), 211–216, doi:10.12386/A2013sxxb0022; publisher publication date 2013-03-15.

[2] J. Fox, R. Gera and P. Stănică, “The Independence Number for the Generalized Petersen Graphs”, *Ars Combinatoria* 103 (2012), 439–451; available full text at https://faculty.nps.edu/pstanica/research/GenPetersen.pdf.

[3] J. Ewell, “Bipartite Density of Generalized Petersen Graphs”, University of Mississippi thesis (2011), https://egrove.olemiss.edu/etd/1324/ (bibliographic material; full text not inspected).

[4] M. Krnc and T. Pisanski, “Generalized Petersen Graphs and Kronecker Covers”, *Discrete Mathematics & Theoretical Computer Science*; accessible text at https://dmtcs.episciences.org/articles/5891/download.

[5] X. Zhu, “Bipartite subgraphs of triangle-free subcubic graphs”, *Journal of Combinatorial Theory, Series B* 99 (2009), 62–83, doi:10.1016/j.jctb.2008.04.005; an author-hosted PDF is indexed at https://www.math.nsysu.edu.tw/~zhu/papers/sparse/cubic2008-4-17-erratum-implemented.pdf (relevant indexed Theorem 1.4 inspected; whole PDF retrieval timed out).
