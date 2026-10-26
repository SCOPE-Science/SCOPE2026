# Minimum maximal double Roman functions on one-leaf coronas: complete optimizer classification and sunlet counts

## Finding
For every finite simple graph \(G\) of order \(n\ge1\), let \(W(G)=G\circ K_1\) be the graph obtained by adjoining one private leaf \(v'\) to each \(v\in V(G)\). Write \(\gamma(G)\) for the minimum size of a dominating set. A *maximal double Roman dominating function* (MDRDF) is defined in the next section. The minimum weight is
\[
\gamma^m_{dR}(W(G))=2n+\gamma(G).
\]
The **novel assertion here is not this scalar equality**, which follows from an earlier result on ordinary double Roman domination of coronas, but the following complete classification of all MDRDFs attaining the minimum.

Let \(q=\gamma(G)\). Choose an ordinary minimum dominating set \(D\subseteq V(G)\) and a subset \(S\subseteq D\) such that every vertex of \(V(G)\setminus D\) has a neighbor in \(S\). The labels \((f(v),f(v'))\) are forced to be \((0,2)\) when \(v\notin D\). For each \(v\in S\), choose independently \((2,1)\) or \((3,0)\); for each \(v\in D\setminus S\), choose independently \((1,2)\) or \((0,3)\). Exclude precisely the one global choice that assigns \((3,0)\) on all of \(S\) and \((0,3)\) on all of \(D\setminus S\). This is a bijective parametrization of the minimum-weight MDRDFs, with vertices and labels distinguished. In particular,
\[
\mathcal M(G)=(2^q-1)\!\sum_{\substack{D\subseteq V(G),\;|D|=q\\D\text{ dominates }G}}
\#\{S\subseteq D: V(G)\setminus D\subseteq N_G(S)\}.
\]
Here \(N_G(S)\) denotes the union of open neighborhoods of the vertices in \(S\). Empty complements are allowed and isolates cause no exception.

For the sunlet \(W(C_n)\), \(n\ge3\), put \(q=\lceil n/3\rceil\). Then the exact number \(\mathcal M(C_n)\) is
\[
\mathcal M(C_n)=(2^q-1)\begin{cases}
3,&n\equiv0\pmod3,\\
n(n+11)/6,&n\equiv1\pmod3,\\
n,&n\equiv2\pmod3.
\end{cases}
\]
In particular, the cycle length \(4\) has \(30\) distinct minimum MDRDFs; this extra multiplicity arises from distinct eligible subsets \(S\) of a fixed minimum dominating set.

## Assumptions and scope
All graphs here are finite, simple, undirected and may be disconnected or have isolated vertices. A double Roman function \(f:V(H)\to\{0,1,2,3\}\) satisfies: each zero-labeled vertex has a neighbor labeled \(3\), or two **distinct** neighbors labeled \(2\); and each one-labeled vertex has a neighbor labeled \(2\) or \(3\). It is *maximal* if its zero-vertex set is **not** a dominating set of \(H\) (equivalently, some positive-labeled vertex has no zero-labeled vertex in its closed neighborhood). The weight is the sum of its labels. This use of 'maximal' is not maximality under pointwise ordering. \(N_G(S)\) is the open neighborhood of \(S\); when \(S=\varnothing\), it is empty.

## Proof
**1. Local lower bound and equality types.** Fix an arbitrary MDRDF \(f\) on \(W(G)\). For a core vertex \(v\) and its private leaf \(v'\), the pair weight \(f(v)+f(v')\) is at least \(2\): weights \(0\) or \(1\) would leave the leaf labeled \(0\) without a label-\(3\) neighbor or two label-\(2\) neighbors, or leave a label-\(1\) leaf without a high-labeled neighbor. If the pair has weight exactly \(2\), its labels must be \((0,2)\). Indeed, \((2,0)\) fails at the leaf, \((1,1)\) fails the label-\(1\) condition there, and the other pairs of weight \(2\) are excluded by the leaf condition. If its weight is \(3\), its possibilities are exactly \((0,3),(1,2),(2,1),(3,0)\), all locally admissible (further core constraints may apply).

Let \(D\) consist of core vertices with pair weight at least \(3\). Every core vertex \(u\notin D\) has label \(0\) and its leaf has label \(2\). Thus the zero condition at \(u\) requires at least one additional core neighbor labeled \(2\) or \(3\); that neighbor belongs to \(D\). Therefore \(D\) dominates \(G\), so \(|D|\ge\gamma(G)\), and
\[
w(f)\ge 2(n-|D|)+3|D|=2n+|D|\ge2n+\gamma(G).
\]
For any minimum dominating set \(D\), assigning \((2,1)\) at vertices of \(D\) and \((0,2)\) elsewhere yields a feasible function of weight \(2n+\gamma(G)\). It is maximal because every positive leaf at a vertex of \(D\) is adjacent to a positive core vertex and has no zero neighbor. Hence the bound is attained.

**2. Exhaustive equality classification.** Equality in the displayed chain forces \(|D|=q=\gamma(G)\), every pair in \(D\) to have weight exactly \(3\), and every pair outside \(D\) to equal \((0,2)\). Define \(S\subseteq D\) to be precisely the core vertices given label \(2\) or \(3\), namely those carrying \((2,1)\) or \((3,0)\). A core vertex outside \(D\) has exactly one private leaf labeled \(2\); the double Roman condition at that zero core is equivalent to having a high-labeled core neighbor in \(S\). Thus \(V(G)\setminus D\subseteq N_G(S)\) is necessary and sufficient for all double Roman constraints: every other zero or one is defended by its own partner.

To check maximality, the positive leaf in a pair \((2,1)\) has no zero neighbor, as does the positive leaf in \((1,2)\). Conversely, if neither pair occurs, every pair is \((0,2),(0,3)\) or \((3,0)\), so each positive vertex has its zero-labeled partner as a neighbor; consequently the zero set dominates all vertices, and the MDRDF condition fails. Therefore among the \(2^{|S|+|D\setminus S|}=2^q\) independent choices for each admissible \((D,S)\), exactly one is excluded. The map from an optimal function to \((D,S)\) and its pair-type choices is unique, proving the bijection and counting identity.

**3. The sunlet census.** A minimum dominating set \(D\) in a cycle \(C_n\) has \(q=\lceil n/3\rceil\) vertices. Write the cyclic gaps between consecutive selected vertices as integers in \(\{1,2,3\}\), which necessarily sum to \(n\). Conversely, exactly these gap conditions characterize domination. Their deficits from \(3\) total \(3q-n\).

If \(n=3k\), all gaps equal \(3\). There are exactly three distinct minimum sets \(D\), and each selected vertex is essential for dominating the complement, so only \(S=D\) qualifies.

If \(n=3k+2\), one gap equals \(2\) and all others equal \(3\); there are \(n\) distinct minimum sets, and again only \(S=D\) qualifies.

If \(n=3k+1\), either one gap equals \(1\) (all others \(3\)), or two gaps equal \(2\) (all others \(3\)). The first type gives exactly \(n\) minimum sets, each with only \(S=D\). The second type gives \(n(q-1)/2\) minimum sets, counting the positions of the two short gaps and dividing by the \(q\) choices of cyclic starting selected vertex. Every such set allows \(S=D\). Additionally, precisely when the two short gaps are adjacent cyclically can their common selected vertex be omitted from \(S\) without losing coverage outside \(D\). There are \(n\) such omission choices. For \(q=2\) (the four-cycle), both gaps are short and each of the \(n/2\) opposite pairs permits two distinct singleton choices for \(S\), so the same count \(n\) applies. Thus the number of admissible ordered pairs \((D,S)\) is \(n+n(q-1)/2+n=n(q+3)/2=n(n+11)/6\). Multiplication by \(2^q-1\) completes the sunlet formula. \(\square\)

## Verification
The standalone Python script `verify.py` evaluates the original definition directly (including failure of zero-set domination) on every labeled graph of order at most four and five additional order-five graph families. It compares the brute-force optimum weight and **number** of functions to the independent dominating-set/subset formula. Across 80 base graphs, it visits 2,696,420 candidate labelings of weight at most the constructive bound. It separately checks all three sunlet cases for cycle orders \(3\) through \(15\) using the dominating-set formula. The original, actual output appears in `verification_output.txt`. This is bounded corroboration, not an infinite proof; the general result follows from the arguments above.

## Relationship to prior work
Abdollahzadeh Ahangar, Chellali, Sheikholeslami and Valenzuela-Tripodoro introduced maximal double Roman domination (the non-dominating-zero-set condition) and studied graph-theoretic bounds, paths, cycles and trees. Cariaga and Jamil, **Corollary 3(i)**, proved an ordinary double Roman corona minimum formula \(\gamma_{dR}(G\circ K_1)=3n-\max\{|V_0|:f\in\operatorname{DRD}(G)\}\) for connected nontrivial \(G\). Since \(\max|V_0|=n-\gamma(G)\), their statement **already implies** the scalar equality \(2n+\gamma(G)\) for those graphs. This note does not claim that numeric corollary as new. The additional result is the **complete equality-case classification** and the labeled exact census of all minimum maximal double Roman functions, including the three residue classes of sunlets. Related published-finding corpus records concern other variants of Roman domination or other graph classes and do not, by their stated claims, imply this census. Priority remains subject to unindexed equivalent work.

## Limitations
The enumeration distinguishes graph vertices and all four labels, not equivalence under graph automorphisms. The general formula involves enumerating minimum dominating sets and need not be efficient to evaluate. The classification concerns one attached private leaf per core vertex and no other corona product. Computer checks extend only to finite instances and independent literature verification has not been performed.

## References
1. H. Abdollahzadeh Ahangar, M. Chellali, S. M. Sheikholeslami and J. C. Valenzuela-Tripodoro, *Maximal double Roman domination in graphs*, Applied Mathematics and Computation **414** (2022), 126662, DOI: 10.1016/j.amc.2021.126662. Lawful open preprint: arXiv:2402.07013v1, publicly posted 2024-02-10, https://arxiv.org/pdf/2402.07013.
2. J. B. G. Cariaga and F. P. Jamil, *On Double Roman Dominating Functions in Graphs*, European Journal of Pure and Applied Mathematics **16** (2023), 847–863, DOI: 10.29020/nybg.ejpam.v16i2.4653; full article: https://www.ejpam.com/index.php/ejpam/article/view/4653/1399, especially Corollary 3(i).
