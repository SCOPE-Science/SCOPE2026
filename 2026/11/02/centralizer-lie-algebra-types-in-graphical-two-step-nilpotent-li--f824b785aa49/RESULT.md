# Centralizer Lie-algebra types in graphical two-step nilpotent Lie algebras

## Finding
Let \(G=(V,E)\) be any finite simple graph, \(n=|V|\), \(m=|E|\), and \(k\) any field. Let \(L_G\) have basis \(v_i\) for vertices and central basis \(z_{ij}\) for edges, with \([v_i,v_j]=z_{ij}\) on edges (the opposite bracket is its negative). For \(x=\sum_{i\in V} a_i v_i+z\), put \(S=\{i:a_i\ne0\}\), let \(N[S]\) be the closed graph neighborhood of \(S\), set \(U=V\setminus N[S]\), and write \(c(S)\) for the number of connected components of \(G[S]\), with \(c(\varnothing)=0\).

**Centralizer-type theorem.** For every \(x\), the centralizer Lie algebra is isomorphic to
\[
 C_{L_G}(x)\cong L_{G[U]}\oplus k^{m+c(S)-|E(G[U])|}.
\]
In particular, \([C_{L_G}(x),C_{L_G}(x)]\) has dimension exactly \(|E(G[U])|\). Over \(k=\mathbb F_q\), the complete *centralizer isomorphism-class distribution* is determined by the explicit finite sum
\[
 \sum_{S\subseteq V} q^m(q-1)^{|S|}\,[L_{G[U(S)]}\oplus\mathbb F_q^{m+c(S)-|E(G[U(S)])|}],
\]
where the brackets denote a formal isomorphism-type symbol and equal types are collected. Consequently the joint distribution of centralizer dimension and its derived dimension is
\[
 H_G(q;t,w)=q^m\sum_{S\subseteq V}(q-1)^{|S|}t^{m+c(S)+|U(S)|}w^{|E(G[U(S)])|}.
\]
No assumption on characteristic is needed.

**Separation beyond adjoint rank.** Define two graphs \(A\) and \(B\) on \(\{0,1,2,3,4,5\}\) by
\[
 E(A)=\{01,02,03,04,14,23,35\},\quad E(B)=\{04,05,13,14,23,24,34\}.
\]
Their ordinary adjoint-rank polynomials coincide (a previously known example). Nonetheless, for every \(q\), exactly \(q^7(q-1)\) elements of \(L_B(\mathbb F_q)\) have centralizer derived dimension \(5\), whereas **no** element of \(L_A(\mathbb F_q)\) does. Thus the distribution of centralizer *algebra structures* strictly refines the adjoint-rank distribution.

## Assumptions and scope
Graphs are finite, simple, undirected; empty graphs and isolated vertices are allowed. The edge bracket is alternating in characteristic two as well. The full center contains all edge-basis vectors and all isolated-vertex basis vectors. The notation \(k^d\) means an abelian Lie algebra of dimension \(d\); \(L_{G[U]}\) uses its own edge-space basis. Formula counts all \(q^{n+m}\) elements, including central ones; formal isomorphism-class symbols are not assumed algebraically independent.

## Proof
Write \(x=x_V+z\), \(y=\sum b_i v_i+z'\). Since the edge symbols are independent, \([x,y]=0\) holds exactly when \(a_i b_j-a_j b_i=0\) for each edge \(ij\). If \(i\in S\), \(j\notin S\), and \(ij\in E\), then \(b_j=0\). Thus only coordinates in \(S\cup U\) may survive, with every coordinate in \(U\) free. Within each connected component \(C\) of \(G[S]\), the edge equations force \(b_i=\lambda_C a_i\) for all \(i\in C\); conversely these constraints suffice. Therefore the vertex part of \(C_{L_G}(x)\) has direct-sum basis \(\{x_C:C\in\pi_0(G[S])\}\cup\{v_u:u\in U\}\), where \(x_C=\sum_{i\in C}a_i v_i\). There are no edges from \(U\) into \(S\) by definition, and no edges between distinct components of \(G[S]\). Hence all \(x_C\) bracket trivially with one another and with all \(v_u\), and among the \(v_u\) the brackets are exactly the edge symbols for \(G[U]\). Splitting the global \(m\)-dimensional central edge space into the \(|E(G[U])|\) symbols internal to \(U\) and their complement proves the claimed Lie-algebra direct-sum isomorphism. This proof does not divide by two and therefore works in characteristic two.

The dimension is \(m+c(S)+|U|\), and the derived algebra is the span of the internal-\(U\) edge symbols, so its dimension is \(|E(G[U])|\). Over \(\mathbb F_q\), each prescribed support \(S\) has \((q-1)^{|S|}\) coefficient assignments, and every such vector has \(q^m\) independent edge-central coordinates. Summation gives both distributions.

For the six-vertex example, the only way a noncentral centralizer can have derived dimension \(5\) is for \(U\) to contain at least four vertices. As neither graph has isolated vertices, \(S\ne\varnothing\) and \(|U|\ge4\) requires \(S=\{i\}\) with \(i\) a degree-one vertex. Both graphs have the unique such vertex \(5\). For \(A\), \(U_A(\{5\})=\{0,1,2,4\}\) induces four edges \(01,02,04,14\); for \(B\), \(U_B(\{5\})=\{1,2,3,4\}\) induces five edges \(13,14,23,24,34\). Thus only \(B\)'s support \(S=\{5\}\) produces derived dimension \(5\), contributing \(q^7(q-1)\) elements. The empty support yields the entire algebra with derived dimension \(7\), not \(5\). This establishes the separation claim. The equality of the two ordinary adjoint-rank polynomials is the previously established graph-pair fact, also independently reproducible by the script.

## Verification
Run `python3 verify.py` using only Python 3 standard library. It checks the exact graph-pair equality of adjoint-rank polynomials as formal polynomials, the stated induced-subgraph edge-count separation, and finite-field direct centralizer brackets / derived ranks on small graphs. The direct tests corroborate but do not substitute for the general argument. The centralizer direct-sum proof applies over all fields, without finite-field enumeration assumptions.

## Relationship to prior work
The graphical two-step Lie-algebra construction and characteristic-not-two graph-isomorphism rigidity are established in Mainkar's 2013 work. A previously recorded six-vertex example establishes equality of the ordinary adjoint-rank polynomials for the stated pair and already gives the general formula for that polynomial. These prior contributions are not claimed as new. The new statement determines the full Lie-algebra isomorphism type of **each centralizer** and the full centralizer-type distribution, and proves that the six-vertex pair is separated by a derived-centralizer invariant even though adjoint ranks coincide. This is not implied by the old rank polynomial: it records only centralizer dimensions, not the brackets inside them. General low-dimensional centralizer classifications and support-graph formulae remain possible historical overlap risks.

## Limitations
No claim is made that the centralizer-type distribution completely distinguishes all graph isomorphism classes or that its formal aggregate has a minimal expression. The explicit direct-sum decomposition may admit alternate presentations when induced subgraphs have isolated vertices. Existing graph-isomorphism rigidity results quoted in characteristic different from two are not extended here. Novelty remains subject to independent literature review.

## References
1. M. G. Mainkar, *Graphs and Two-Step Nilpotent Lie Algebras*, arXiv:1310.3414v1, 12 October 2013, https://arxiv.org/abs/1310.3414 .
2. D. Dani and M. G. Mainkar, *Anosov automorphisms on compact nilmanifolds associated with graphs*, Trans. Amer. Math. Soc. 357 (2005), 2235–2255, https://people.se.cmich.edu/maink1m/trans.pdf .
