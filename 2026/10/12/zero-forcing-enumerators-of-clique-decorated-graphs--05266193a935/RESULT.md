# Zero-forcing enumerators of clique-decorated graphs

## Finding
Let \(G\) be any nonempty finite simple graph, with \(n=|V(G)|\), and assign an integer \(s_v\ge2\) to every vertex \(v\). Form \(H\) by adjoining a private clique \(P_v\cong K_{s_v}\) to each \(v\), joining \(v\) to every vertex of \(P_v\), and adding no edges between different private cliques. Write \(\mathcal Z(F;x)=\sum_{S\subseteq V(F):\, S\text{ zero forcing}}x^{|S|}\) for the ordinary zero-forcing polynomial.

**Structural equivalence.** An initial blue set \(S\subseteq V(H)\) is zero forcing if and only if both conditions hold:

1. Every private clique contains at most one initially white vertex: \(|P_v\setminus S|\le1\) for every \(v\).
2. The effective root set
\[
B(S)=\{v\in V(G):\ v\in S\text{ or }P_v\subseteq S\}
\]
is a zero-forcing set of \(G\).

Consequently, with the indicated products evaluated independently at each root, the **complete** counting identity is
\[
\boxed{\displaystyle
\mathcal Z(H;x)=\sum_{B\subseteq V(G):\,B\text{ zero forcing}}
\prod_{v\in B}x^{s_v}(x+s_v+1)
\prod_{v\notin B}s_vx^{s_v-1}.}
\tag{1}
\]
This enumerates every zero-forcing set by its exact cardinality, for any base graph and any private-clique sizes at least two.

For the ordinary uniform clique corona \(H=G\odot K_s\), where \(s\ge2\), (1) specializes to the polynomial substitution
\[
\boxed{\displaystyle
\mathcal Z(G\odot K_s;x)=s^n x^{(s-1)n}
\mathcal Z\!\left(G;\frac{x(x+s+1)}s\right).}
\tag{2}
\]
In particular, writing \(z_G(k)=[x^k]\mathcal Z(G;x)\), for every integer \(t\) the number of zero-forcing sets of size \((s-1)n+t\) in the uniform corona is
\[
\boxed{\displaystyle
\sum_{k=\lceil t/2\rceil}^{t} z_G(k)\,s^{n-k}
\binom{k}{t-k}(s+1)^{2k-t},}
\tag{3}
\]
where out-of-range binomial coefficients and coefficients are zero. Moreover,
\[
Z(H)=\sum_{v\in V(G)}(s_v-1)+Z(G),
\tag{4}
\]
and the exact number of minimum zero-forcing sets of \(H\) is
\[
\boxed{\displaystyle
\sum_{\substack{B\text{ zero forcing in }G\\|B|=Z(G)}}
\prod_{v\in B}(s_v+1)\prod_{v\notin B}s_v.}
\tag{5}
\]
For uniform \(s\), (5) is \(z_G(Z(G))s^{n-Z(G)}(s+1)^{Z(G)}\). Finally, for fixed \(s\ge2\), the operation \(G\mapsto G\odot K_s\) preserves **and reflects** equality of zero-forcing polynomials (including the order of the graph).

## Assumptions and scope
All graphs are finite, undirected, loopless and without multiple edges. The base graph \(G\) need not be connected or have an edge; isolated roots are permitted. At least one root is assumed to avoid the empty-graph convention. The variable \(x\) is formal; all identities are polynomial identities over the integers despite the rational-looking substitution in (2). The parameter bound \(s_v\ge2\) is essential. A blue vertex forces its unique white neighbor, if one exists; a set is zero forcing when finitely many such moves color every vertex blue. The \(P_v\) are disjoint from each other and from \(V(G)\).

## Proof
**Step 1: an unavoidable local obstruction.** Suppose two vertices \(a,b\in P_v\) are initially white. Every vertex adjacent to \(a\) outside \(\{a,b\}\) is also adjacent to \(b\), because \(P_v\) is a clique and its only exterior neighbor is \(v\). Consider the first moment at which either \(a\) or \(b\) might be forced. Both are still white, and every potential blue forcing neighbor sees both. Hence neither can be the unique white neighbor. This contradiction proves that a zero-forcing \(S\) must satisfy \(|P_v\setminus S|\le1\) for every root.

**Step 2: activation of an effective root.** Assume the local obstruction never occurs. If \(v\in S\) and its clique has one white vertex, some initially blue private vertex (available because \(s_v\ge2\)) sees exactly that one white vertex and forces it. If \(v\notin S\) but \(P_v\subseteq S\), any blue private vertex sees only \(v\) as white and forces \(v\). In both cases the root and its whole clique can be made blue immediately using only private vertices. Thus every root in \(B(S)\), together with its entire private clique, can be activated before any root-to-root force is used.

**Step 3: sufficiency.** Suppose \(B(S)\) is zero forcing in \(G\). Activate all its roots as in Step 2. Follow any legal zero-forcing sequence in \(G\): when a blue root \(u\) should force a white root \(v\) in \(G\), all of \(P_u\) is blue, so \(v\) is still the only white neighbor of \(u\) in \(H\), and the same force is legal. Since \(v\notin B(S)\) before it is reached, \(v\) started white with exactly one white private vertex; an initially blue private vertex of \(P_v\) can now force that remaining private vertex. Consequently each newly forced root becomes fully activated. Iteration colors all of \(H\).

**Step 4: necessity of the projected forcing set.** Now suppose \(S\) forces \(H\). The local obstruction from Step 1 does not occur. For each \(v\notin B(S)\), initially both \(v\) and exactly one private vertex \(w_v\in P_v\) are white. As long as \(v\) remains white, \(w_v\) cannot be forced: each blue private vertex sees both \(v\) and \(w_v\), while the only other neighbor of \(w_v\) is the still-white root \(v\). Likewise, no private vertex can force \(v\) while \(w_v\) is white. Thus the first force making any root outside \(B(S)\) blue must come from another root along an edge of \(G\). Such a root-to-root force is legal in \(G\), because it has exactly one white **root** neighbor in \(H\), and possibly fewer after we regard all vertices of \(B(S)\) as blue from the outset. Project the successive root-to-root forces to \(G\), ignoring root vertices in \(B(S)\). By monotonicity, they form a legal zero-forcing process from \(B(S)\), which reaches every root because the process in \(H\) succeeds. Hence \(B(S)\) is zero forcing in \(G\).

**Step 5: exact enumeration.** For a chosen zero-forcing effective-root set \(B\), the feasible initial colors at a root \(v\in B\) are: blue root and full blue clique (weight \(x^{s_v+1}\)); blue root and precisely one white private vertex (\(s_v\) choices, weight \(s_vx^{s_v}\)); or white root and full blue clique (weight \(x^{s_v}\)). Their sum is \(x^{s_v}(x+s_v+1)\). At a root \(v\notin B\), the root and precisely one private vertex are white, with \(s_v\) choices and weight \(s_vx^{s_v-1}\). The choices are independent across roots, and the structural equivalence shows there are no other zero-forcing sets or double counts. Multiplying and summing over \(B\) proves (1). Setting every \(s_v=s\) yields (2), and the binomial theorem yields (3).

**Step 6: minimum sets and recognition.** Every summand for \(B\) in (1) has least possible exponent \(\sum_v(s_v-1)+|B|\), with positive coefficient. The minimum occurs exactly at base zero-forcing sets of size \(Z(G)\), proving (4), and multiplying their least-degree local coefficients gives (5). Since \(\mathcal Z(G;x)\) has degree \(n\) and leading coefficient one, equality of the corona polynomials for fixed \(s\) implies equal base orders. Dividing the common polynomial by \(s^nx^{(s-1)n}\) and using injectivity of composition by the nonconstant polynomial \(x(x+s+1)/s\) recovers equality of the original zero-forcing polynomials; the converse follows immediately from (2).

## Verification
The standalone script `verify.py` performs exhaustive independent direct forcing checks on all 75 labeled base graphs of orders one through four, with 221 nonuniform clique-size profiles satisfying total decorated order at most twelve. It tests 624,824 initial vertex sets, each both through explicit color propagation on the decorated graph and through the structural criterion from Steps 1–4; it also independently combines the predicted local weights and compares all 1,230 nonzero polynomial coefficients. `verification_output.txt` records the completed run. The script uses only the Python standard library. Reproduce with `python3 verify.py` in a directory containing that script. These finite computations test examples, not the unrestricted theorem, which is established by Steps 1–6.

For a boundary check, when \(G=K_2\) and the private clique size is one, the decorated graph is \(P_4\), whose zero-forcing polynomial is \(2x+6x^2+4x^3+x^4\); substituting \(s=1\) into (2) would instead give \(4x+6x^2+4x^3+x^4\). This confirms why the private-clique-size restriction cannot be discarded.

## Relationship to prior work
Boyer, Brimkov, English, Ferrero, Keller, Kirsch, Phillips and Reinhart (first publicly posted 26 January 2018) introduced the zero-forcing polynomial and studied its graph-theoretic properties and several families; their concluding Question 1 asks for graph-polynomial recurrences or separating-set formulas. The full source does not state the clique-corona transformation (1)–(2).

Javaid, Irshad, Batool and Raza (first publicly posted 14 July 2016) proved the **already-known scalar identity** \(Z(G\odot H)=Z(G)+|V(G)|Z(H)\) for connected graphs in their Theorem 2.3. Their Corollary 2.5 specializes this to complete private cliques. Our equation (4), in the uniform connected case, is therefore **not claimed to be new**. The contribution here is the if-and-only-if classification of **every** initial set, the entire polynomial transfer, exact coefficient profiles, minimum-set multiplicities, and polynomial-equivalence reflection for arbitrary bases and variable clique sizes. These stronger statements do not follow from knowledge of the minimum cardinality alone.

## Limitations
This concerns ordinary zero forcing (not skew, positive-semidefinite, power domination, or a threshold variant). Every private graph must be a complete graph of order at least two; arbitrary attachments are not covered, and the explicit \(s=1\) counterexample shows that this boundary is genuine. The counting identity reduces a decorated graph to the zero-forcing sets of its base; it does not itself supply a polynomial-time algorithm for computing the base polynomial on unrestricted graphs. Independent validation has not been performed. Prior literature searches cannot exclude inaccessible, unpublished, or unindexed equivalent statements, particularly derivations implicit in earlier corona work.

## References
1. K. Boyer, B. Brimkov, S. English, D. Ferrero, A. Keller, R. Kirsch, M. Phillips and C. Reinhart, *The zero forcing polynomial of a graph*, arXiv:1801.08910v1 (26 January 2018), later *Discrete Applied Mathematics* 258 (2019), 35–48. https://arxiv.org/abs/1801.08910
2. I. Javaid, I. Irshad, M. Batool and Z. Raza, *On the zero forcing number of corona and lexicographic product of graphs*, arXiv:1607.04071v1 (14 July 2016), Section 2, Theorem 2.3 and Corollary 2.5. https://arxiv.org/abs/1607.04071
