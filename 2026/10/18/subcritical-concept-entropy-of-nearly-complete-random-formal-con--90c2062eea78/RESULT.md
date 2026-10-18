# Subcritical concept entropy of nearly complete random formal contexts

## Finding

For a real number \(0<c<1\), let \(\mathcal K_n=(G_n,M_n,I_n)\) be a random formal context with \(|G_n|=|M_n|=n\) and independent incidences, each present with probability \(1-c/n\). Let \(C_n\) be the number of formal concepts, **including concepts with an empty extent or intent**. Then

\[
\frac{\log C_n}{n}\longrightarrow F(c)\quad\text{in }L^1\text{ and in probability},
\]

where the following **absolutely convergent, computationally effective tree series** defines the limit:

\[
F(c)=\sum_{T\in\mathscr T_{\mathrm{bi}}}
 \frac{c^{|V(T)|-1}e^{-c|V(T)|}}{|\operatorname{Aut}_{\mathrm{bi}}(T)|}
 \log m(T).
\tag{1}
\]

Here \(\mathscr T_{\mathrm{bi}}\) consists of representatives of finite connected bipartite trees with an *ordered* left/right coloring, including the two one-vertex trees; \(\operatorname{Aut}_{\mathrm{bi}}(T)\) preserves the two sides; and \(m(T)\) is the number of maximal independent vertex sets of the tree. One-vertex trees contribute zero. The limit is strictly positive and obeys

\[
F(c)\ge ce^{-2c}\log2>0.\tag{2}
\]

The first nontrivial terms, as \(c\downarrow0\), are

\[
F(c)=c\log2-c^2\log2+c^3\left(\log3-\frac23\log2\right)+O(c^4).\tag{3}
\]

Thus an incidence relation whose density tends to one can nevertheless have exponentially many formal concepts: \(C_n=\exp(nF(c)+o_{\mathbb P}(n))\). The claim is specifically about \(0<c<1\), not the critical or supercritical complement graph.

## Assumptions and scope

A formal concept is a pair \((A,B)\) with \(A\subseteq G_n\), \(B\subseteq M_n\), satisfying \(A'=B\) and \(B'=A\), where a prime takes the set of common neighbors in the incidence relation and empty intersections have their usual full-universe meaning. Define the **non-incidence graph** \(H_n\) on the disjoint sets \(G_n\sqcup M_n\): it contains precisely those object–attribute pairs *not* in \(I_n\). Therefore \(H_n\) is the balanced bipartite binomial random graph \(G_{n,n}(c/n)\).

A maximal independent set is independent under graph edges and cannot be enlarged by adjoining another vertex. For finite graphs \(H\), let \(m(H)\) denote their number of maximal independent sets; it is multiplicative across connected components. Natural logarithms are used throughout. A tree with a left/right coloring differing only by a color-preserving graph isomorphism appears once in \(\mathscr T_{\mathrm{bi}}\); a color swap is not imposed as an identification unless a color-preserving isomorphism exists between the colored realizations.

## Proof

**1. Exact semantic–graph-theoretic correspondence.** The rectangle \(A\times B\) lies in \(I_n\) exactly when \(A\cup B\) is independent in \(H_n\). Moreover, \(A'=B\) says that no attribute outside \(B\) can be added to this rectangle, and \(B'=A\) says that no object outside \(A\) can be added. Both conditions together are equivalent to maximal independence of \(A\cup B\) in \(H_n\), including empty sides. Therefore, for **every** realized context,

\[
C_n=m(H_n)=\prod_{Q\in\operatorname{Comp}(H_n)}m(Q),\qquad
\log C_n=\sum_Q\log m(Q).\tag{4}
\]

In particular \(1\le m(Q)\le2^{|V(Q)|}\), whence \(0\le\log m(Q)\le|V(Q)|\log2\).

**2. Fixed tree-component intensities.** Fix a two-colored tree \(T\) with \(a\) left vertices, \(b\) right vertices, \(v=a+b\) total vertices, and \(u=|\operatorname{Aut}_{\mathrm{bi}}(T)|\). Write \(N_T(n)\) for the number of connected components isomorphic to \(T\) with the two sides respected. For a connected tree with \(a,b\ge1\), the exact expectation is

\[
\mathbb EN_T(n)=\frac{(n)_a(n)_b}{u}
 \left(\frac cn\right)^{v-1}
 \left(1-\frac cn\right)^{nv-ab-v+1},\tag{5}
\]

because the component has \(v-1\) specified edges, no other internal edges, and no edges to outside vertices. Hence

\[
\frac{\mathbb EN_T(n)}n\longrightarrow
\lambda_T(c):=\frac{c^{v-1}e^{-cv}}u.\tag{6}
\]

The analogous expectations for either isolated-vertex tree are \(n(1-c/n)^n\), giving intensity \(e^{-c}\), again (6) with \(v=1\). For fixed \(T\), expand \(\operatorname{Var}N_T\) over pairs of labeled component embeddings. Two distinct overlapping candidate components cannot both exist. For disjoint embeddings, the joint probability divided by the product of marginal probabilities is \((1-c/n)^{-ab'-a'b}=1+O_T(1/n)\), where \(a',b'\) are the corresponding sizes of the second copy. Together with \(\mathbb EN_T=O_T(n)\), this gives \(\operatorname{Var}N_T(n)=O_T(n)\). Thus

\[
N_T(n)/n\longrightarrow\lambda_T(c)\qquad\text{in }L^2.\tag{7}
\]

For each fixed size cutoff \(K\), finitely many two-colored tree types have at most \(K\) vertices. The expected number of components of any *fixed* cyclic type is \(O(1)\) or less: a connected cyclic graph has at least as many edges as vertices, whereas a choice of its labeled vertices contributes \(O(n^{v})\) and its required edges contribute \(O(n^{-|E|})\). Therefore the normalized \(\log m\) contribution from components of at most \(K\) vertices tends in \(L^1\) to

\[
F_K(c)=\sum_{\substack{T\in\mathscr T_{\mathrm{bi}}\\|V(T)|\le K}}\lambda_T(c)\log m(T).\tag{8}
\]

**3. Uniform control of large components.** Root a breadth-first exploration of \(H_n\) at a uniformly sampled vertex on either side. Each newly processed vertex discovers at most a \(\operatorname{Binomial}(n,c/n)\) number of candidates, and explorations can be coupled to an independent-offspring Galton–Watson upper bound. Choose \(d\) with \(c<d<1\). For all sufficiently large \(n\), a binomial offspring variable is stochastically dominated by \(\operatorname{Poisson}(d)\): represent every Bernoulli edge as the positivity indicator of an independent Poisson variable of mean \(-\log(1-c/n)\), and note that \(-n\log(1-c/n)<d\). The total progeny of a Poisson-\(d\) Galton–Watson tree has an exponential tail because \(d<1\). Hence constants \(A_c<\infty\), \(\eta_c>0\) satisfy, uniformly for sufficiently large \(n\),

\[
\mathbb P\bigl(|\operatorname{Comp}_{H_n}(V)|>K\bigr)
 \le A_ce^{-\eta_cK}\quad(K\ge1),\tag{9}
\]

where \(V\) is uniform among the \(2n\) vertices. The bound on \(\log m(Q)\) following (4) implies

\[
\mathbb E\left[\frac1n\sum_{Q:\,|V(Q)|>K}\log m(Q)\right]
\le2(\log2)A_ce^{-\eta_cK}.\tag{10}
\]

For fixed \(K\), apply (7) and the cyclic-component estimate, then let \(K\to\infty\) using (10). This proves convergence in \(L^1\) to the series (1); it simultaneously establishes absolute convergence and a quantitative exponentially decaying size-truncation bound.

**4. Positive lower bound and low-density expansion.** A non-incidence component consisting of a single edge has two maximal independent sets. From (6), such components occur at normalized intensity \(ce^{-2c}\). Other contributions to (1) are nonnegative, proving (2).

For \(v=2\), the unique two-colored tree is an edge, with color-preserving automorphism group of order one and \(m=2\). For \(v=3\), two color-distinct paths (left-centered and right-centered) each have automorphism group of order two and \(m=2\). For \(v=4\), a four-vertex path contributes weight one with \(m=3\), while the two color-distinct three-leaf stars contribute combined weight \(1/3\) with \(m=2\). Their contribution is therefore

\[
ce^{-2c}\log2+c^2e^{-3c}\log2+
 c^3e^{-4c}\left(\log3+\frac13\log2\right).\tag{11}
\]

All larger trees have at least four edges. Uniform subcritical branching tails (equivalently the small-\(c\) Borel total-progeny expansion) show that the sum of their \(|V(T)|\)-weighted intensities is \(O(c^4)\) as \(c\downarrow0\). Thus their \(\log m(T)\) contribution is \(O(c^4)\). Taylor-expanding (11) proves (3).

**5. Reproducible tree evaluation.** The tree factor \(m(T)\) can be calculated without enumerating vertex subsets. Root \(T\), and for each vertex with child states \((A_i,B_i,D_i)\), let \(A\) count independent dominating assignments with the root selected; \(B\) count assignments with the root unselected but dominated by a child; and \(D\) count assignments with the root unselected and undominated, to be dominated by its parent. Then

\[
A=\prod_i(B_i+D_i),\qquad
B=\prod_i(A_i+B_i)-\prod_iB_i,\qquad
D=\prod_i B_i,\tag{12}
\]

with empty products one, and \(m(T)=A_{\rm root}+B_{\rm root}\). Formula (12), together with (1) and (10), gives a finite procedure to approximate \(F(c)\) to any prescribed accuracy for fixed \(0<c<1\).

## Verification

The accompanying standalone program `verify_sparse_complement.py` uses two independent finite definitions: Galois derivation closure for formal concepts and brute-force independence plus domination for maximal independent sets. It exhausts **1,226** incidence/non-incidence matrices for bipartition sizes \(1\le a,b\le4\) with \(ab\le9\), checking (4) each time. Separately it enumerates all labeled bipartite trees on two, three and four vertices, checks the rooted recurrence (12) against direct maximal-independent-set enumeration, and verifies the coefficients of (11). The actual packaged program was executed with Python 3 and returned `VERIFY_OK`. These finite tests do not prove (7)–(10); the analytic argument above does.

## Relationship to prior work

Felde, Hanika and Stumme (2020) model random formal contexts and analyze coin-toss/Dirichlet null-model generation, with primary MSC \(03G10\). Sakurai (2021) gives an exact expected-concept formula and superpolynomial expectation bounds in a different random-context regime; those results neither establish the typical logarithmic entropy (1) nor its near-complete scaling. Drmota, Ramos, Requilé and Rué (2018) enumerate maximal independent sets and analyze their sizes in uniformly sampled **graph classes** such as trees and series-parallel graphs; their results concern a distinct probability space and do not give the component-weighted quenched \(\log m\) limit (1) for the sparse Erdős–Rényi bipartite graph. Jenssen, Perkins and Potukuchi (2023) develop algorithms for **all** independent sets in bipartite expanders, rather than maximal independent sets in subcritical random graphs.

The graph-theoretic identity relating maximal incidence rectangles and independent sets of the complement, basic component counting, and the Galton–Watson upper bound are standard ingredients; they are not claimed as individually new. The claimed contribution is their assembled **exact limit, positive entropy, effective tree series, and cubic small-parameter law** for nearly complete random formal contexts.

## Limitations

The result is proved only for a balanced context, independent incidences and fixed \(0<c<1\), with normalization \(n\) rather than \(2n\). No central limit theorem, finite-\(n\) rate, equality at \(c=1\), extension to \(c>1\), or assertion about \(\log\mathbb E C_n\) is proved. The formula is an infinite absolutely convergent series, not an elementary closed form. Absence of a matching record in the consulted sources does not establish publication priority; an older formulation as a random-graph component functional remains a substantive residual originality risk.

## References

1. M. Felde, T. Hanika, and G. Stumme, *Null Models for Formal Contexts*, Information 11(3), 135 (2020), DOI: 10.3390/info11030135. First verified public version: 2020-02-28; MSC 03G10.
2. T. Sakurai, *On formal concepts of random formal contexts*, arXiv:2101.11023 (v1, 2021-01-26), later Information Sciences 578, 615–620 (2021).
3. M. Drmota, L. Ramos, C. Requilé, and J. Rué, *Maximal Independent Sets and Maximal Matchings in Series-Parallel and Related Graph Classes*, AofA 2018, DOI: 10.4230/LIPIcs.AofA.2018.18 (2018-06-18).
4. M. Jenssen, W. Perkins, and A. Potukuchi, *Approximately counting independent sets in bipartite graphs via graph containers*, Random Structures & Algorithms 63, 215–241 (2023), DOI: 10.1002/rsa.21145.
