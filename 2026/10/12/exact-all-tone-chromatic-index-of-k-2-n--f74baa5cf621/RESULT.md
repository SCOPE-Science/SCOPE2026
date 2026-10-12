# Exact all-tone chromatic index of \(K_{2,n}\)
## Finding
For every pair of integers \(n,t\ge1\),
\[
\tau'_t(K_{2,n})=n\bigl(t+\max\{0,t-n+1\}\bigr).
\]
Equivalently,
\[
\tau'_t(K_{2,n})=
\begin{cases}
nt,&t\le n-1,\\
n(2t-n+1),&t\ge n.
\end{cases}
\]
The transition at \(t=n\) is sharp: the usual local lower bound \(t\Delta=tn\) is attainable exactly for \(t\le n-1\).

## Assumptions and scope
Graphs are finite and simple. A \(t\)-tone edge coloring assigns a \(t\)-element color set to every edge so that edges at distance \(d\) in the line graph share fewer than \(d\) colors. Write the degree-\(n\) vertices of \(K_{2,n}\) as \(u,v\), its other vertices as \(w_0,\ldots,w_{n-1}\), and put \(e_i=uw_i\), \(f_i=vw_i\). The line graph consists of two \(n\)-cliques \(\{e_i\}\) and \(\{f_i\}\), joined by the matching \(e_i f_i\); every unmatched cross-pair \(e_i,f_j\) with \(i\ne j\) is at distance two.

## Proof
Let \(E_i\) and \(F_i\) be the labels of \(e_i\) and \(f_i\). Since the \(e_i\) form a clique, the \(E_i\) are pairwise disjoint. Their union \(U\) therefore has size \(nt\).

Fix \(j\). The adjacent edges \(e_j\) and \(f_j\) force \(F_j\cap E_j=\varnothing\). For each \(i\ne j\), the cross-pair is at distance two, so \(F_j\) contains at most one color from \(E_i\). Hence
\[
|F_j\cap U|\le n-1.
\]
Thus \(F_j\) contains at least \(r=\max\{0,t-n+1\}\) colors outside \(U\). The \(f_j\) also form a clique, so the \(F_j\) are pairwise disjoint; in particular, their outside-\(U\) colors are disjoint. Every coloring therefore uses at least \(nt+nr\) colors.

For equality, let \(q=\min\{t,n-1\}\) and \(r=t-q\). Use colors \(a_{i,s}\) for \(i\in\mathbb Z_n\), \(1\le s\le t\), together with colors \(b_{j,h}\) for \(j\in\mathbb Z_n\), \(1\le h\le r\). Set
\[
E_i=\{a_{i,1},\ldots,a_{i,t}\},
\]
and
\[
F_j=\{a_{j+s,s}:1\le s\le q\}\cup\{b_{j,h}:1\le h\le r\},
\]
where the first index is read modulo \(n\). The \(E_i\) are pairwise disjoint. The \(F_j\) are pairwise disjoint because equality \(a_{j+s,s}=a_{j'+s',s'}\) forces \(s=s'\) and then \(j=j'\). Since \(1\le s\le q\le n-1\), one has \(E_j\cap F_j=\varnothing\). For \(i\ne j\), at most one value of \(s\) satisfies \(i=j+s\pmod n\), so \(|E_i\cap F_j|\le1\). Therefore these labels form a valid \(t\)-tone edge coloring on exactly \(nt+nr\) colors, matching the lower bound. The case \(n=1\) is included: then \(q=0\) and the two adjacent edges receive disjoint \(t\)-sets.

## Verification
The proof is symbolic and covers all integers \(n,t\ge1\). The accompanying `verify.py` reconstructs the displayed labels for every \(1\le n,t\le80\), checks every distance-one and distance-two constraint in the line graph, checks the palette size, and independently recomputes the lower-bound accounting. It also checks the star boundary \(n=1\), the cycle boundary \(n=2\), and the \(t=1,2\) specializations.

## Relationship to prior work
Al Bazzal introduced \(t\)-tone edge coloring and observed the identity \(\tau'_t(G)=\tau_t(L(G))\); the paper's main new results focus on \(t=2\) and do not state a complete-bipartite formula. Bickle's 2013 product result gives the exact \(t=2\) value for \(K_m\square K_n\), which agrees with the present formula after using \(L(K_{2,n})\cong K_2\square K_n\). Bennett and Nichols prove two nearby general-\(t\) results: MOLS give \(\tau_t(K_n^2)=tn\) in specified ranges, and for every fixed connected graph their large-\(t\) theorem is eventually exact. Applied to \(K_2\square K_n\), that large-\(t\) theorem yields the same linear expression only once \(t\ge2n-1\); the present argument lowers the exact onset to \(t=n\) and also determines every smaller \(t\). The 2017 Cooper--Wash Cartesian-product paper was identified as a plausible comparison source; only its bibliographic record and later descriptions were available in the inspected sources, so possible unindexed overlap there remains a residual risk.

## Limitations
This theorem is specific to the two-by-\(n\) complete bipartite family, equivalently the clique-prism line graphs \(K_2\square K_n\). It does not give an exact formula for \(K_{m,n}\) with \(m>2\). The computational checks are finite consistency tests and are not used as an infinite proof. The originality assessment is limited by incomplete access to the full 2017 Cooper--Wash article.

## References
1. H. Al Bazzal, *\(t\)-tone edge coloring of graphs*, arXiv:2605.24571v1, 23 May 2026. AMS 05C15.
2. P. Bennett and J. Nichols, *Some progress on \(t\)-tone coloring*, arXiv:2510.13382v1, 15 October 2025, especially Theorems 13 and 14.
3. A. Bickle, *2-tone coloring of joins and products of graphs*, Congressus Numerantium 217 (2013), 171--190, especially Theorem 30.
4. A. Bickle and B. Phillips, *\(t\)-Tone Colorings of Graphs*, Utilitas Mathematica 106 (2018), 85--102.
5. C. Cooper and K. Wash, *\(t\)-tone colorings in the Cartesian product*, Congressus Numerantium 228 (2017), 199--210.
