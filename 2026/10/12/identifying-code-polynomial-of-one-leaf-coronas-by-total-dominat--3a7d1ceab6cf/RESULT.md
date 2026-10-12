# Identifying-code polynomial of one-leaf coronas by total domination and true twins

## Finding

Let \(G\) be a finite, nonempty, simple undirected graph with \(n=|V(G)|\), with no connectedness assumption. Construct \(W(G)=G\circ K_1\) by attaching a distinct private leaf \(v'\) adjacent only to each vertex \(v\in V(G)\). The identifying-code polynomial counts every vertex subset \(C\subseteq V(W(G))\) for which the intersections \(N_{W(G)}[u]\cap C\) are nonempty and pairwise distinct:

\[\mathcal I(W(G);x)=\sum_{C\text{ identifying code}}x^{|C|}.\]

A subset \(R\subseteq V(G)\) is *total dominating* when \(N_G(v)\cap R\ne\varnothing\) for every \(v\in V(G)\). For a nonempty total dominating \(R\), let \(\mathcal T(G[R])\) be the partition of \(R\) by equality of closed neighborhoods *within the induced graph* \(G[R]\): two vertices are in one class precisely when \(N_{G[R]}[u]=N_{G[R]}[v]\). Put \(c(R)=|\mathcal T(G[R])|\).

**Theorem.** For every such \(G\),

\[\boxed{\mathcal I(W(G);x)=x^n\sum_{\substack{R\subseteq V(G)\\ N_G(v)\cap R\ne\varnothing\ \forall v\in V(G)}}x^{|R|-c(R)}\prod_{Q\in\mathcal T(G[R])}(x+|Q|).}\]

The sum is zero when no total dominating set exists. Equivalently, the identifying-code subsets of \(W(G)\) are classified without duplication by selecting a total dominating root set \(R\) and omitting zero or one private leaf from each closed-twin class of \(G[R]\); all private leaves whose roots are not selected must be selected.

The formula also determines the minimum-size coefficient:

\[[x^n]\mathcal I(W(G);x)=|\{R\subseteq V(G):R\text{ is total dominating and }G[R]\text{ has no closed twins}\}|.\]

Thus it gives every cardinality count and, at \(x=1\), the total number of identifying codes, \(\sum_{R\text{ total dominating}}\prod_{Q\in\mathcal T(G[R])}(1+|Q|)\).

## Assumptions and scope

Graphs are finite, simple, undirected, and nonempty; they may be disconnected. Neighborhoods without brackets are open, and neighborhoods in brackets are closed. An identifying code separates all vertices using nonempty intersections with their closed neighborhoods. The empty sum is zero; no limiting or asymptotic interpretation is involved. If \(G\) has an isolated vertex, the attached root-leaf edge is a two-vertex component of \(W(G)\) whose endpoints are closed twins, so the identifying-code polynomial is zero, in agreement with the formula.

## Proof

Fix a vertex subset \(C\) of \(W(G)\). Write \(R=C\cap V(G)\) for the selected roots and \(L=\{v\in V(G):v'\in C\}\) for the roots whose private leaves are selected.

For every \(v\), the leaf's identifying signature is \(N_{W(G)}[v']\cap C=C\cap\{v,v'\}\). It is nonempty exactly when \(v\in R\cup L\). Therefore every private leaf at a root outside \(R\) must belong to \(C\). Moreover,

\[N_{W(G)}[v]\cap C=(C\cap\{v,v'\})\cup(N_G(v)\cap R).\]

Since these two sets are disjoint, the signatures of \(v\) and \(v'\) differ exactly when \(N_G(v)\cap R\ne\varnothing\). Requiring this for every \(v\) is precisely the condition that \(R\) total-dominates \(G\).

Assume now that both conditions hold. Distinct leaves have nonempty, disjoint signatures. A root \(u\) and a leaf \(v'\) with \(u\ne v\) are distinct because the signature of \(u\) contains a selected element from its own pair \(\{u,u'\}\), disjoint from the signature of \(v'\). A root and its own leaf have already been distinguished by total domination.

For two distinct roots \(u,v\), if \(u'\in C\) or \(v'\in C\), that private leaf belongs only to its root's closed neighborhood, so their signatures differ. Otherwise both leaves are omitted; nonemptiness then forces \(u,v\in R\). Their signatures are \(N_G[u]\cap R\) and \(N_G[v]\cap R\), respectively. These are equal exactly when \(u,v\) are closed twins of \(G[R]\). Thus the remaining identification constraints say that no closed-twin class of \(G[R]\) may have more than one omitted private leaf. This proves the characterization in both directions.

For a fixed total dominating \(R\), the selected roots contribute \(x^{|R|}\) and the mandatory leaves outside \(R\) contribute \(x^{n-|R|}\). A class \(Q\subseteq R\) of size \(k\) permits either all \(k\) private leaves to be selected (weight \(x^k\)) or exactly one of them to be omitted (\(k\) choices, weight \(k x^{k-1}\)). Its factor is therefore \(x^{k-1}(x+k)\). Multiplying over the \(c(R)\) disjoint classes yields

\[x^{|R|}x^{n-|R|}\prod_{Q\in\mathcal T(G[R])}x^{|Q|-1}(x+|Q|)=x^{n+|R|-c(R)}\prod_{Q\in\mathcal T(G[R])}(x+|Q|).\]

Summing disjointly over all possible \(R\) proves the polynomial formula. Every identifying code has at least one selected vertex in each of the \(n\) disjoint root-leaf pairs, hence cardinality at least \(n\). The exponent \(n\) in the formula occurs for a fixed \(R\) precisely when every closed-twin class has size one. This proves the coefficient statement.

## Verification

The accompanying standard-library script `verify_identifying_corona.py` compares a direct test of all closed-neighborhood identifying signatures with the structural characterization, and separately counts coefficients by the displayed formula. It exhaustively checks every labeled graph on one through five vertices, and additionally checks deterministic pseudorandom samples and both empty and complete bases on six and seven vertices. In total it examines 1,239 graph instances and 1,860,132 candidate vertex subsets; all checks agree. These are finite corroborations, not substitutes for the universal proof.

For an independent symbolic boundary check, if \(G=K_m\) for an integer \(m\ge2\), every total dominating root set has at least two vertices and induces one closed-twin class. The theorem specializes to

\[\mathcal I(K_m\circ K_1;x)=x^m\bigl((1+x)^m-1-mx+m((1+x)^{m-1}-1)\bigr).\]

The coefficient of \(x^{m+1}\) is \(m(m-1)\), consistent with the previously known minimum code size \(m+1\). For a star \(G=K_{1,m}\) with \(m\ge2\), the coefficient of \(x^{m+1}\) (the smallest degree) is \(2^m-m-1\). The bundled verifier checks these family coefficients independently of direct subset tests.

## Relationship to prior work

Feng and Wang (arXiv:1301.4295v1, 2013), especially Theorems 4.5–4.6, determine the *minimum size* of identifying codes of \(H\circ K_1\) for complete and connected noncomplete base graphs. The size statements are credited here and are not new. Their constructions do not enumerate all code subsets of each size. Argiroffo, Bianchi, Lucarini, and Wagler (2019), Section 3, consider generalized pendant coronas and give scalar code numbers when every support has at least two pendant leaves; they do not cover the one-leaf all-size formula. Foucaud and Lehtilä (first arXiv version 11 April 2022, arXiv:2204.05250v1) analyze identifying-code bounds and one- and two-corona extremal cases, not the present enumerator. Argiroffo, Bianchi, and Wagler (2018) provide a general set-cover encoding for identifying codes; the current result is its explicit total-domination/closed-twin specialization for every one-leaf corona, not a claim to invent the underlying identification constraints. The closest known published enumerations for threshold and chain graphs have different graph-family hypotheses, with no implication of this arbitrary-base identity.

## Limitations

The sum over total dominating subsets can be exponentially large, so the identity is not asserted to yield a polynomial-time algorithm on arbitrary base graphs. It is a complete exact structural enumeration. The universal proof is elementary but is not independently refereed; finite tests do not establish the infinite statement. Although no equivalent polynomial was found in the checked sources, unindexed or differently titled prior enumerations remain a possible originality risk.

## References

1. M. Feng and K. Wang, *Identifying codes of corona product graphs*, arXiv:1301.4295v1 (18 January 2013), Sections 2–4, especially Theorems 4.5 and 4.6. https://arxiv.org/abs/1301.4295
2. G. R. Argiroffo, S. M. Bianchi, Y. P. Lucarini, and A. K. Wagler, *The Identifying Code, the Locating-dominating, the Open Locating-dominating and the Locating Total-dominating Problems Under Some Graph Operations*, Electronic Notes in Theoretical Computer Science 346 (2019), 135–145, Section 3. DOI:10.1016/j.entcs.2019.08.013.
3. F. Foucaud and T. Lehtilä, *Revisiting and improving upper bounds for identifying codes*, arXiv:2204.05250v1 (11 April 2022), Sections 1–3. https://arxiv.org/abs/2204.05250
4. G. R. Argiroffo, S. M. Bianchi, and A. K. Wagler, *Polyhedra associated with identifying codes in graphs*, Discrete Applied Mathematics 245 (2018), 16–27. DOI:10.1016/j.dam.2017.06.005.
