# Domination-weighted maximal abelian subalgebra census for graph Lie algebras

## Finding
Let \(G=(V,E)\) be any finite simple graph with at least one vertex, and let \(q\) be a prime power. For the graph Lie algebra \(L_G=\mathbb F_q^V\oplus\mathbb F_q^E\), the dimensions of all inclusion-maximal abelian Lie subalgebras have the exact distribution
\[
M_G(q,t)=\sum_{\substack{S\subseteq V\\ S\text{ dominating in }G}}
(q-1)^{|S|-c(G[S])}\,t^{c(G[S])},
\]
where \(c(G[S])\) is the number of components of the subgraph induced on \(S\), including singleton components. The coefficient of \(t^d\) counts subalgebras of dimension \(|E|+d\), as embedded subspaces, not isomorphism types. This is a complete classification as well as a numerical formula.

More precisely, write \(x_i\) for the basis of the vertex space and \(z_e\) for the edge-central basis. Each inclusion-maximal abelian subalgebra is uniquely
\[
H=\mathbb F_q^E\oplus\bigoplus_{C\in\pi_0(G[S])}\mathbb F_q v_C,
\quad v_C=\sum_{i\in C}a_i x_i,\quad a_i\in\mathbb F_q^\times,
\]
where \(S\) dominates \(G\). Each \(v_C\) is identified up to one common nonzero scalar, and different components are chosen independently. In particular, there are \((q-1)^{|S|-c(G[S])}\) distinct maximal abelian subalgebras for each dominating support \(S\).

The degree of \(M_G(q,t)\) is exactly the independence number \(\alpha(G)\), so the largest abelian subalgebra dimension is \(|E|+\alpha(G)\). For two vertex-disjoint graphs, their census polynomials multiply. For the complete bipartite graph \(K_{r,s}\), where \(r,s\geq1\),
\[
M_{K_{r,s}}(q,t)=\frac{(q^r-1)(q^s-1)}{q-1}t+t^r+t^s.
\]
The formula is valid for every characteristic, including two, and also for isolated vertices and disconnected graphs.

## Assumptions and scope
The graph is a finite, undirected, simple graph; edge labels in the central basis are independent. Define the Lie bracket by \([x_i,x_j]=z_{\{i,j\}}\) for an edge with \(i<j\), by skew-symmetry for the opposite order, and by zero on all other generator pairs; all edge basis elements are central. Over characteristic two the alternating bracket is still well-defined because \([x_i,x_i]=0\) by construction. An *abelian subalgebra* is a linear subspace on which all brackets vanish. *Maximal* means inclusion-maximal among abelian subalgebras, not necessarily maximum dimension. A subset \(S\) dominates \(G\) when each vertex outside \(S\) has a neighbor in \(S\). The empty induced graph has zero components.

No restriction on the number of vertices, edges, or the prime-power field order is imposed. These are actual linear subalgebras, not orbits under automorphisms. The full central space \(\mathbb F_q^E\) need not be the full center when the graph has isolated vertices, but maximality forces it into every maximal abelian subalgebra.

## Proof
**Step 1 (central reduction).** Let \(H\) be an inclusion-maximal abelian subalgebra. Since the edge space \(Z=\mathbb F_q^E\) is central, \(H+Z\) is abelian. Hence \(Z\subseteq H\) and \(H=Z\oplus U\), with \(U\) a linear subspace of the vertex space. Thus it is enough to classify inclusion-maximal subspaces \(U\) with \([U,U]=0\).

**Step 2 (coordinate proportionality).** For each vertex \(i\), let \(\lambda_i:U\to\mathbb F_q\) be the restriction of the \(i\)-th coordinate functional. For each edge \(\{i,j\}\), the edge coefficient of \([u,v]\) is \(\lambda_i(u)\lambda_j(v)-\lambda_j(u)\lambda_i(v)\), so \([U,U]=0\) holds exactly when \(\lambda_i\wedge\lambda_j=0\) for every edge. Define the active support \(S=\{i:\lambda_i\ne0\}\). If an edge is contained in \(S\), its two nonzero functionals are proportional. Along every connected component \(C\) of \(G[S]\), there is one nonzero linear functional \(\phi_C\in U^*\) and nonzero coefficients \(a_i\) such that \(\lambda_i=a_i\phi_C\) for all \(i\in C\). Consequently every \(u\in U\) is a sum of multiples of vectors \(v_C=\sum_{i\in C}a_i x_i\). Hence \(U\subseteq W_S:=\bigoplus_C\mathbb F_q v_C\).

**Step 3 (maximality and domination).** The subspace \(W_S\) is abelian: within one induced component its coordinate vectors are proportional, while different components have no edges between them. If \(U\) was maximal, the preceding inclusion forces \(U=W_S\). If \(S\) fails to dominate, an outside vertex \(j\) has no neighbor in \(S\); then \(x_j\) centralizes \(W_S\) but is not in it, contradicting maximality. Conversely, suppose \(S\) dominates. Let \(w\) centralize \(W_S\). For any outside vertex \(j\), choose an adjacent \(i\in S\), lying in component \(C\). The \(\{i,j\}\)-coordinate of \([w,v_C]\) is a nonzero scalar times \(w_j\), so \(w_j=0\). Along an edge \(\{i,j\}\) internal to \(C\), the same equality gives \(a_j w_i=a_i w_j\); by connectivity, the ratios \(w_i/a_i\) are constant throughout \(C\). Thus \(w\in W_S\). Therefore the centralizer of \(W_S\) in the vertex space is exactly \(W_S\), proving maximality. This proves the claimed bijection.

**Step 4 (counting).** In a component of size \(s\), vectors with all \(s\) coefficients nonzero number \((q-1)^s\); quotienting by scalar rescaling of their line gives \((q-1)^{s-1}\). Multiply over components to obtain \((q-1)^{|S|-c(G[S])}\). Each component adds one generator, and all of \(Z\) is already present, so \(\dim H=|E|+c(G[S])\). Summation over dominating supports proves the displayed polynomial and its uniqueness assertion.

**Step 5 (consequences).** Selecting one vertex from each component of \(G[S]\) gives an independent set, hence \(c(G[S])\le\alpha(G)\). Conversely every maximum independent set is dominating and has \(c(G[S])=|S|=\alpha(G)\); this proves the polynomial degree assertion. On a disjoint union both domination and induced component counts split, proving multiplicativity. In \(K_{r,s}\), every dominating set either meets both vertex classes (giving one connected component) or equals one whole class (giving \(r\) or \(s\) singleton components). Summing the nonempty choices of coefficients in each class gives the displayed complete-bipartite formula.

## Verification
An independent exact finite-field implementation is embedded as `verify.py`. It generates every subspace of \(\mathbb F_q^n\) using reduced row-echelon matrices. It tests the edgewise alternating equations and separately computes the linear centralizer to decide inclusion-maximality. The predicted counts are computed from graph domination and connected-component enumeration, without sharing the algebraic counting route. All unlabeled edge subsets of the labeled graphs on \(1\le n\le4\) vertices were checked over each of \(\mathbb F_2\), \(\mathbb F_3\), \(\mathbb F_4\), and \(\mathbb F_5\): \(75\) graphs per field, \(300\) graph-field combinations, all matching the theorem.

As a strict-refinement example, the paw graph with edges \(\{01,02,03,12\}\) and the four-cycle with edges \(\{02,03,12,13\}\) both have the ordinary independence polynomial \(1+4t+2t^2\), yet their maximal-abelian censuses differ:
\[
M_{\mathrm{paw}}(q,t)=q^3t+(q+1)t^2,
\qquad M_{C_4}(q,t)=(q^3+q^2-q-1)t+2t^2.
\]
In particular, for \(q=2\) these are \(8t+3t^2\) and \(9t+2t^2\). The test program reproduces both independently. Finite testing supports the general proof but does not establish the infinite-field-size statement by itself.

## Relationship to prior work
DeCoste, DeMeyer, Mainkar, and Ray (2022) determine the **central abelian direct-summand factor** for graph-built two-step Lie algebras, including stars and cycles. In the independent-edge construction considered here, this factor consists of isolated-vertex directions; their factor result does not enumerate inclusion-maximal abelian subalgebras or their dimension distribution. Aldi and collaborators (2025/2026) study the Lie-theoretic independence polynomial and bounds on dimensions of abelian subalgebras, not the count of all inclusion-maximal embedded abelian subalgebras over finite fields. The paw versus four-cycle comparison proves that the ordinary graph independence polynomial alone does not determine the present census. Sriwongsa (2025) relates maximal independent sets of the **large projective non-commuting graph** to maximal abelian subalgebras for general Lie algebras; that correspondence does not itself evaluate the closed weighted-domination polynomial on the original construction graph. Existing Lie-subalgebra dimension results likewise do not determine the complete count. The proof here is self-contained and does not require new results from those papers.

## Limitations
The result applies to the independent-central-edge graph construction and not automatically to quotients identifying several edge labels. It counts distinct embedded maximal abelian subalgebras, not conjugacy classes, all abelian subalgebras, or abelian ideals. It does not determine the computational complexity of evaluating the weighted graph polynomial on arbitrary large inputs. Complete priority relative to every historical, possibly unindexed algebra or graph-enumeration source is not certified; a general projective-noncommuting-graph reformulation could offer an equivalent nonexplicit expression.

## References
1. R. DeCoste, L. DeMeyer, M. Mainkar, A. Ray, *Abelian Factor in 2-step Nilpotent Lie Algebras Constructed from Graphs*, arXiv:2208.09541 (first posted 2022-08-19), https://arxiv.org/abs/2208.09541 .
2. M. Aldi, T. Gabrielsen, D. Grandini, J. Harris, K. Kelley, *Independence Polynomials of 2-step Nilpotent Lie Algebras*, arXiv:2504.19836, https://arxiv.org/abs/2504.19836 .
3. S. Sriwongsa, *Non-commuting graphs of projective spaces over central quotients of Lie algebras*, arXiv:2505.00726, https://arxiv.org/abs/2505.00726 .
4. M. Mainkar, *Graphs and two-step nilpotent Lie algebras*, Groups Geom. Dyn. 9 (2015), 55–65; arXiv:1310.3414, https://arxiv.org/abs/1310.3414 .
