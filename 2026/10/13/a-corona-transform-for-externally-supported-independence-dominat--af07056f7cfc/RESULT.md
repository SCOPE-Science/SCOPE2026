# A corona transform for externally supported independence, domination, and graph differential

## Finding

Let \(H\) be any finite simple undirected graph on \(n\ge 1\) vertices, with no connectivity assumption. For an integer \(m\ge1\), construct \(G=H\odot\overline{K_m}\) by attaching \(m\) new pendant leaves to **each** vertex of \(H\). An externally supported independent (ESI) set \(S\subseteq V(G)\) is an independent set such that every vertex in its open neighborhood \(N_G(S)\) has a neighbor outside the closed neighborhood \(N_G[S]\). The empty set is included. Write
\[
E_G(z)=\sum_{S\text{ an ESI set of }G}z^{|S|},\qquad
A_m(z)=(1+z)^m-1,\qquad B_m(z)=(1+z)^m-1-z^m.
\]
For a set \(Z\subseteq V(H)\), let \(\partial_H Z=N_H(Z)\setminus Z\) be its external neighborhood, and let \(N_H[Z]=Z\cup\partial_HZ\).

**Exact corona transform.** For every \(H\) and \(m\ge1\),
\[
\boxed{E_{H\odot\overline{K_m}}(z)=
\sum_{Z\subseteq V(H)}A_m(z)^{|\partial_H Z|}
 B_m(z)^{n-|N_H[Z]|}.}
\tag{1}
\]
The convention \(P(z)^0=1\) includes the case \(P(z)=0\). Equation (1) determines the complete ESI-set cardinality distribution and the ESI independence number \(\alpha_{\rm es}(G)=\deg E_G(z)\), where the zero polynomial never occurs because the empty set is ESI.

In particular, if \(D_H(z)=\sum_{Z\text{ dominating }H}z^{|Z|}\) is the ordinary domination polynomial, then a *single* pendant leaf per vertex gives the exact reversal
\[
\boxed{E_{H\odot K_1}(z)=z^nD_H(z^{-1}),\qquad
\alpha_{\rm es}(H\odot K_1)=n-\gamma(H).}
\tag{2}
\]
(The right-hand side is understood as a polynomial after cancellation.) Thus optimal ESI sets correspond bijectively to minimum dominating sets of \(H\).

For \(m\ge2\), define the weighted external-neighborhood differential
\[
\partial_{m}(H)=\max_{Z\subseteq V(H)}
\left(|\partial_H Z|-(m-1)|Z|\right).
\]
Then
\[
\boxed{\alpha_{\rm es}(H\odot\overline{K_m})=(m-1)n+\partial_m(H).}
\tag{3}
\]
The number of maximum-cardinality ESI sets is exactly
\[
\boxed{\sum_{\substack{Z\subseteq V(H)\\
 |\partial_H Z|-(m-1)|Z|=\partial_m(H)}}
 m^{n-|N_H[Z]|}.}
\tag{4}
\]
At \(m=2\), \(\partial_2(H)\) is the classical graph differential \(\partial(H)\). The established identity \(\gamma_R(H)+\partial(H)=n\), where \(\gamma_R\) denotes the Roman domination number, therefore gives
\[
\boxed{\alpha_{\rm es}(H\odot\overline{K_2})=n+\partial(H)=2n-\gamma_R(H).}
\tag{5}
\]
For \(m\ge2\), the baseline value \((m-1)n\) is attained exactly when \(m\ge\Delta(H)+1\), with \(\Delta(H)\) the maximum degree of \(H\). For \(m\ge\max\{2,\Delta(H)+2\}\), the only maximizing zero-leaf set is empty, and there are exactly \(m^n\) largest ESI sets, each selecting exactly \(m-1\) of the \(m\) leaves at every base vertex.

## Assumptions and scope

All graphs here are finite, simple, undirected; the base graph may have isolated vertices or multiple components. The integer \(m\) is uniform and at least one. Vertices in the base graph and the attached leaves are distinguishable, and all ESI sets are counted as labeled vertex subsets. The external-neighborhood notation \(\partial_H Z\) is defined here and is not the graph differential \(\partial(H)\); the latter is a maximum of \(|\partial_H Z|-|Z|\). The formulas are exact integer-polynomial identities, not estimates or asymptotic statements. The results concern the leaf-corona graph, not the ESI number of an arbitrary graph without this construction.

## Proof

Let \(L_v\) be the \(m\)-element leaf bundle attached to \(v\in V(H)\). If an ESI set contained a base vertex \(v\), one of the pendant leaves at \(v\) would belong to \(N_G(S)\), but its only neighbor \(v\) would lie in \(S\subseteq N_G[S]\). This violates external support. Hence every ESI set is contained in \(\bigcup_v L_v\). This is the support-vertex exclusion in the motivating literature, and it also follows directly from the definition.

For any subset \(S\) of the leaves, put \(S_v=S\cap L_v\), and define the *zero-leaf base set* \(Z=\{v:S_v=\varnothing\}\). Because selected leaves have only their own base vertices as neighbors,
\[
N_G(S)=\{v\in V(H):S_v\ne\varnothing\}.
\]
No unselected pendant leaf lies in \(N_G[S]\); a base vertex belongs to \(V(G)\setminus N_G[S]\) precisely when it is in \(Z\). Thus a core vertex \(v\) with \(0<|S_v|<m\) has an unselected leaf as its required external neighbor, while a core vertex \(v\) with \(|S_v|=m\) has an external neighbor precisely when \(v\) has a base neighbor in \(Z\). Base vertices in \(Z\) are not in \(N_G(S)\) and require no condition. These cases are necessary and sufficient, and no other vertex can violate the ESI requirement.

Consequently \(S_v=\varnothing\) for \(v\in Z\); any *nonempty* subset of \(L_v\) is allowed for \(v\in\partial_HZ\); and only nonempty *proper* subsets of \(L_v\) are allowed for \(v\in V(H)\setminus N_H[Z]\). The respective cardinality-generating weights are \(1\), \(A_m(z)\), and \(B_m(z)\). The zero-leaf set \(Z\) is uniquely determined by \(S\), so summing disjoint cases gives (1), including \(m=1\) and isolated vertices.

If \(m=1\), then \(A_1(z)=z\) and \(B_1(z)=0\). A summand in (1) is nonzero exactly when \(N_H[Z]=V(H)\), meaning \(Z\) dominates \(H\); in this case \(|\partial_HZ|=n-|Z|\). This gives (2), with minimum dominating sets corresponding to maximum-degree terms.

Now suppose \(m\ge2\). Both factors \(A_m\) and \(B_m\) have nonnegative coefficients and positive top coefficients: \(A_m\) has degree \(m\) with leading coefficient \(1\); \(B_m\) has degree \(m-1\) with leading coefficient \(m\). For a fixed \(Z\), the degree of its nonzero term in (1) is
\[
m|\partial_HZ|+(m-1)(n-|N_H[Z]|)
=(m-1)n+|\partial_HZ|-(m-1)|Z|.
\]
No cancellation of leading terms is possible. Taking the maximum degree proves (3), and adding their leading coefficients gives the exact witness count (4). Setting \(m=2\) gives the first equality in (5); the second invokes the *previously known* classical differential–Roman-domination identity, not a new proof of that identity.

Finally, \(|\partial_HZ|\le\sum_{v\in Z}d_H(v)\le\Delta(H)|Z|\). For \(m\ge\Delta(H)+1\), every term in the maximum defining \(\partial_m(H)\) is at most zero, and \(Z=\varnothing\) gives zero. If \(2\le m\le\Delta(H)\), a singleton \(Z\) consisting of a maximum-degree vertex gives a strictly positive value; this proves the exact threshold. If \(m\ge\max\{2,\Delta(H)+2\}\), all nonempty \(Z\) give strictly negative values, so (4) reduces to \(m^n\).

## Verification

The included script `corona_esi_verify.py` independently builds graph coronas, tests every candidate subset directly against independence and the external-support definition, and compares the resulting cardinality counts against (1). It additionally tests (2) using a separate brute-force domination enumeration and tests (3) against a separate subset maximization. Run from a directory containing both artifacts with `python corona_esi_verify.py` (Python 3 and `networkx`). The recorded execution in `corona_esi_verify_output.txt` reports 278 unlabeled-base-graph/multiplicity profiles, 2,576,060 directly examined corona-vertex subsets, 208 single-leaf reversals and 70 weighted-differential extremal checks, all passing. These are finite corroborations only; the preceding proof establishes the general result.

## Relationship to prior work

Božović, Peterin, Roux, and Tepeh introduced externally supported independence in arXiv:2606.22972v1 (2026-06-22), including the support-vertex exclusion (Lemma 8/Corollary 9), a construction for trees (Section 5), and a linear-time tree algorithm (Section 6). Their discussion of Roman domination in the conclusion motivates the present connection. Their Theorem 16 already implies a particular high-\(m\) extremal threshold for **tree** bases; that special consequence is not separately asserted as new here. The assessed new statement is the complete polynomial identity (1) for **arbitrary** base graphs, including cycles, together with its domination-polynomial reversal and exact differential/witness consequences.

The domination polynomial is classical; its definition and study of the *ordinary domination polynomial of a corona* appear in Alikhani and Peng (arXiv:0905.2251). Indeed, the ordinary domination polynomial of \(H\odot K_1\) is \((2z+z^2)^n\), independent of the edges of \(H\), whereas (2) recovers the full domination polynomial of \(H\) from the ESI polynomial of the same corona. The graph differential and its relationship to Roman domination were established in Bermudo, Fernau, and Sigarreta (2014). Neither of those prior results alone gives (1).

## Limitations

Equation (1) has \(2^n\) explicit summands, so it is not claimed to give a polynomial-time algorithm for arbitrary base graphs. The theorem does not classify nonuniform leaf bundles or solve the general ESI problem outside the indicated corona family. The novelty comparison concerns publicly accessible, checked literature; an independently stated equivalent under different terminology remains a possible residual risk. Finite tests do not establish all-parameter correctness independently of the analytic proof. No independent external audit has been performed.

## References

1. D. Božović, I. Peterin, A. Roux, A. Tepeh, *On externally supported independence number of graphs*, arXiv:2606.22972v1, first public 2026-06-22, https://arxiv.org/abs/2606.22972 (Definition, Lemma 8, Corollary 9, Theorem 16, Section 6, conclusion).
2. S. Alikhani and Y. H. Peng, *Introduction to Domination Polynomial of a Graph*, arXiv:0905.2251, 2009, https://arxiv.org/abs/0905.2251 (ordinary domination polynomials and the corona construction).
3. S. Bermudo, H. Fernau, J. M. Sigarreta, *The differential and the Roman domination number of a graph*, Applicable Analysis and Discrete Mathematics 8 (2014), 155–171, DOI:10.2298/AADM140210003B (the classical differential–Roman identity).
