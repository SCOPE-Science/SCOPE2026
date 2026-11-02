# Domination polynomial and hub threshold for \(F_2(K_{2,n})\)

## Finding

Let \(H_n=F_2(K_{2,n})\), with \(n\ge2\). The complete **ordinary** domination polynomial \(D_n(z)=\sum_{D\text{ dominating in }H_n}z^{|D|}\) has the following finite closed form. Write \(M=\binom n2\) and, for \(t,s\ge0\) with \(t+s\le n\), define
\[
Q_{n,t,s}(z)=
\begin{cases}
 z^{\binom t2}\displaystyle\sum_{j=0}^{s}(-1)^j\binom sj(1+z)^{\binom{n-j}2-\binom t2},&t\ge2,\\[4pt]
 \displaystyle\sum_{j=0}^{s+t}(-1)^j\binom{s+t}j(1+z)^{\binom{n-j}2},&t\in\{0,1\}.
\end{cases}
\]
Then the exact polynomial is
\[
\boxed{\begin{aligned}
D_n(z)={}&z\sum_{t=0}^{n}\binom nt\,z^{\binom t2}(2z+z^2)^{n-t}(1+z)^{M-\binom t2}\\
&+\sum_{\substack{t,s,u\ge0\\t+s+u=n\\s+u>0}}
\frac{n!}{t!s!u!}(2z)^s z^{2u}Q_{n,t,s}(z).
\end{aligned}}
\]
The first line counts dominating sets containing the vertex \(h=\{a_1,a_2\}\) of \(H_n\); the second counts those omitting it. Every coefficient counts labelled subsets without symmetry quotienting.

The minimum size is \(\gamma(H_n)=n\). **The number of minimum dominating sets** is
\[
\boxed{[z^n]D_n(z)=\begin{cases}
9,&n=2,\\33,&n=3,\\80,&n=4,\\n(n+3)2^{n-3},&n\ge5.
\end{cases}}
\]
There is a sharp finite threshold: **every minimum dominating set contains \(h\) if and only if \(n\ge5\)**. The numbers of minimum sets that omit \(h\) are respectively \(4,15,24\) at \(n=2,3,4\), and zero for all \(n\ge5\).

## Assumptions and scope

For a simple graph \(G\), the two-token graph \(F_2(G)\) has the unordered two-element subsets of \(V(G)\) as vertices. Two such subsets are adjacent exactly when their symmetric difference consists of two adjacent vertices of \(G\). A dominating set contains or neighbours every graph vertex. The unweighted host \(K_{2,n}\) has fixed distinguished vertices \(a_1,a_2\) in its size-two part and labelled vertices \(b_1,\ldots,b_n\) in its size-\(n\) part. The theorem assumes integer \(n\ge2\), ordinary closed-neighbourhood domination and formal indeterminate \(z\), with no probability or asymptotic hypotheses.

For each \(i\in[n]\), let \(x_{r,i}=\{a_r,b_i\}\), \(r=1,2\), and let \(y_{ij}=\{b_i,b_j\}\) for \(1\le i<j\le n\). In \(H_n\), the neighbours of \(h\) are all \(x_{r,i}\); the neighbours of \(y_{ij}\) are \(x_{r,i}\) and \(x_{r,j}\) for \(r=1,2\); and the neighbours of \(x_{r,i}\) are \(h\) and \(y_{ij}\) for \(j\ne i\). These formulas completely define the graph for the proof.

## Proof

**1. An exact condition on every dominating set.** Given a candidate \(D\subseteq V(H_n)\), partition \([n]\) into \(T,S,U\) by the number of selected vertices from the pair \(\{x_{1,i},x_{2,i}\}\): zero for \(i\in T\), one for \(i\in S\), two for \(i\in U\). Let \(E\subseteq\binom{[n]}2\) consist of those \(\{i,j\}\) for which \(y_{ij}\in D\). Every \(y_{ij}\) with \(i,j\in T\) is undominated by selected cross vertices and must itself lie in \(D\). Thus \(\binom T2\subseteq E\), whether or not \(h\in D\).

If \(h\in D\), all cross vertices are dominated; the forced clique is the **only** condition on \(E\). If \(h\notin D\), the vertex \(h\) requires at least one selected cross vertex, so \(|S|+|U|>0\). Moreover an unselected cross vertex in a column \(i\in T\cup S\) must be dominated by some selected \(y_{ij}\), so every vertex of \(T\cup S\) must have positive degree in \(([n],E)\). For \(i\in U\), both cross vertices are already in \(D\). These conditions are also sufficient, by the explicit neighbourhood list above.

**2. The full polynomial.** Suppose \(h\in D\). Choosing \(|T|=t\) contributes \(\binom nt\); the other \(n-t\) columns have one or two selected cross vertices, contributing \((2z+z^2)^{n-t}\). The forced clique on \(T\) contributes \(z^{\binom t2}\), the other \(M-\binom t2\) possible \(y\)-vertices each contribute \(1+z\), and \(h\) contributes \(z\). Summing over \(t\) proves the first line.

Suppose \(h\notin D\). If \(|T|=t,|S|=s,|U|=u\), then \(t+s+u=n\), \(s+u>0\), and the column assignments contribute \(\frac{n!}{t!s!u!}(2z)^s z^{2u}\). It remains to count selected edges \(E\) containing \(\binom T2\) and incident to every vertex of \(T\cup S\). If \(t\ge2\), the forced clique itself covers every vertex of \(T\); inclusion-exclusion over the \(s\) vertices of \(S\) that might be isolated gives
\[
z^{\binom t2}\sum_{j=0}^s(-1)^j\binom sj(1+z)^{\binom{n-j}2-\binom t2}.
\]
If \(t\le1\), there are no forced edges and inclusion-exclusion must cover all \(s+t\) vertices of \(S\cup T\), giving the other branch of \(Q_{n,t,s}\). This proves the second line. Every \(D\) has exactly one partition and one \(E\), so nothing is counted twice. The explicit expression is a polynomial with nonnegative integer coefficients despite its signed inclusion-exclusion presentation.

**3. Minimum sets containing the hub.** Such a set has at least \(1+(n-t)+\binom t2=n+\frac{(t-1)(t-2)}2\) vertices. Equality at size \(n\) requires \(t\in\{1,2\}\), exactly one selected \(x\)-vertex in each remaining column, and no selected \(y\)-vertices other than the required clique. Hence the number is
\[
n2^{n-1}+\binom n2 2^{n-2}=n(n+3)2^{n-3}
\]
(for \(n=2\), the uncombined expression gives integer \(5\)). These configurations prove \(\gamma(H_n)\le n\).

**4. All hub-free optimal configurations.** A hub-free dominating set has \(q=|S|+2|U|=n-t+u\) selected cross vertices, where \(t=|T|\), \(u=|U|\), and \(e=|E|\) selected \(y\)-vertices. Thus \(|D|=n-t+u+e\). For \(t\ge3\), \(e\ge\binom t2\ge t\). For \(t=2\), at least the edge joining the two vertices of \(T\) belongs to \(E\); if it is the only selected edge, all remaining \(n-2\) columns are isolated in \(([n],E)\), hence must belong to \(U\), so \(u\ge n-2\). When \(n=2\), this one-edge possibility has no cross vertices and fails to dominate \(h\); otherwise \(e+u\ge2=t\). For \(t=1\), the sole zero column needs an incident edge, whence \(e\ge1=t\). For \(t=0\), trivially \(e+u\ge t\). Therefore every hub-free dominating set also satisfies \(|D|\ge n\).

At equality \(|D|=n\), we have \(e+u=t\). Cases \(t\ge4\) are impossible since \(\binom t2>t\). At \(t=3\), equality forces \(E=\binom T2\) and \(u=0\); every column outside \(T\) would then be isolated in \(([n],E)\) and require double selection, while if there is no outside column then \(h\) is not dominated. So \(t=3\) is impossible. At \(t=2\) either (a) \(e=1,u=1\), forcing \(n=3\), with three choices of \(T\), or (b) \(e=2,u=0\), where the one extra edge must cover all \(n-2\) outside columns. This gives \(3\cdot2\cdot2=12\) possibilities for \(n=3\), and \(\binom42 2^2=24\) for \(n=4\). At \(t=1\), equality forces \(e=1,u=0\); its one selected edge must meet every column, giving exactly \(2\cdot2=4\) possibilities at \(n=2\). At \(t=0\), equality would have \(E=\emptyset\), \(U=\emptyset\) and a single selected cross vertex in each column, leaving the other cross vertex in every column undominated. Thus the hub-free minimum counts are \(4\) at \(n=2\), \(3+12=15\) at \(n=3\), \(24\) at \(n=4\), and zero thereafter. Adding the hub-containing counts proves all minimum-set statements and the sharp hub threshold.

## Verification

The included standalone `verify_token_dom.py` evaluates the two polynomial branches by exact integer arithmetic and constructs the token graph independently from the symmetric-difference definition. It exhaustively checks all vertex subsets for \(n=2,3,4,5\), totaling \(2{,}131{,}008\) tested subsets, and compares **every** coefficient, also split by whether the hub is selected. It additionally calculates the exact formula for \(n=6,\ldots,11\) and checks the minimum-set formula and absence of hub-free minima. Execute with `python3 verify_token_dom.py` from the extracted package. These finite checks are not the proof for unbounded \(n\); Steps 1–4 give that proof.

For orientation, \(D_2(z)=9z^2+16z^3+15z^4+6z^5+z^6\). The minimum counts for \(n=2,3,4,5,6,7\) are respectively \(9,33,80,160,432,1120\).

## Relationship to prior work

Chinman–Cortijo–Pedroni–Seong–Stenger (October 20, 2026) and Acosta Troncoso–Caldera Caldera–Rivera (October 22, 2026) independently determine \(\gamma(F_2(K_{m,n}))\), giving \(n\) in the present size-two case. The latter paper's Lemma 2.2 is a full general feasibility characterization and is an important prior structural input; the present proof specializes the neighbourhood relations and adds an **explicit all-cardinality enumeration**, an inclusion-exclusion calculation, an **exact labelled count of all minimum sets**, and the sharp hub-forcing threshold. These enumerations are not stated in either paper. The present claim does **not** extend their minimum cardinality formula to new \(m,n\).

The 2019 article by Prabhu and Manjula presents double-vertex-graph domination bounds and existence results; its relevant results were inspected and do not enumerate these ordinary dominating sets. Fabila-Monroy and Gómez-Galicia (2025) address stars and complete graphs, not \(K_{2,n}\). Related total-domination and independent-domination enumerators concern strictly different families of admissible sets, so their coefficients do not determine the ordinary domination polynomial here. A broad general graph-theoretic counting theorem may still imply a special representation of this polynomial; priority beyond the checked sources is not asserted.

## Limitations

This result is restricted to two indistinguishable tokens on labelled \(K_{2,n}\) for \(n\ge2\) and **ordinary**, not total or independent, domination. It does not enumerate arbitrary \(K_{m,n}\) with \(m>2\), higher token counts, inclusion-minimal sets of all sizes, or symmetry orbits. The formula is a finite summation whose number of terms grows polynomially with \(n\), not a single rational generating function over \(n\). Its evaluation involves alternating inclusion-exclusion terms even though final coefficients are nonnegative. Historical priority outside the inspected primary texts remains open, as does independent mathematical validation.

## References

1. N. Chinman, A. Cortijo, B. Pedroni, I. Seong and L. Stenger, *The domination number of the \(k\)-token graph of the complete bipartite graph \(K_{m,n}\)*, arXiv:2610.28936v1 (first public 2026-10-20), https://arxiv.org/html/2610.28936v1.
2. E. Acosta Troncoso, I. Caldera Caldera and L. M. Rivera, *The domination number of the 2-token graph of the complete bipartite graph*, arXiv:2610.31557v1 (first public 2026-10-22), https://arxiv.org/html/2610.31557v1.
3. R. Prabhu and K. Manjula, *Domination in Double Vertex Graphs*, Journal of Informatics and Mathematical Sciences 11 (2019), 339–343, DOI:10.26713/jims.v11i3-4.1308.
4. R. Fabila-Monroy and S. G. Gómez-Galicia, *Domination number of Token Graphs*, arXiv:2509.16448v1 (2025), https://arxiv.org/html/2509.16448v1.
