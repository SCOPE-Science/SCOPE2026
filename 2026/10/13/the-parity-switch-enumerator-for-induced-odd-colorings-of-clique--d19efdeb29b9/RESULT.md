# The parity-switch enumerator for induced-odd colorings of clique coronas

## Finding

Let \(G\) be an arbitrary nonempty finite simple graph with \(n\) vertices. For integers \(r\ge1\) and \(q\ge1\), let \(X_r=G\odot K_r\) be its **clique corona**, formed by attaching a private copy of \(K_r\) to every vertex of \(G\) and joining that vertex to every vertex of its private clique.

A coloring from \(q\) named colors is **induced-odd** if each vertex has an odd number of neighbors of its own color; it is **induced-even** if every vertex has an even number of neighbors of its own color. Neither condition requires proper coloring, and unused colors are permitted. Let \(O_H(q)\) and \(E_H(q)\) count these two kinds of colorings of a graph \(H\), respectively. The entire induced-odd coloring enumerator of the clique corona satisfies

\[
O_{X_r}(q)=\begin{cases}
\left(r!\,[z^r]\sinh z\,(\cosh z)^{q-1}\right)^n E_G(q),&r\text{ odd},\\[3pt]
\left(r!\,[z^r](\cosh z)^{q-1}\right)^n O_G(q),&r\text{ even}.
\end{cases}
\]

Here coefficient extraction uses formal power series with rational coefficients. The factors are nonnegative integers for all indicated parameters. In particular, writing \(\chi_{\mathrm{indodd}}\) for the minimum number of nonempty color classes that each induce an odd graph, with value \(\infty\) when no such partition exists,

\[
\chi_{\mathrm{indodd}}(G\odot K_r)=\begin{cases}
1,& r\text{ odd and every vertex of }G\text{ has even degree},\\
2,& r\text{ odd and some vertex of }G\text{ has odd degree},\\
\max\{2,\chi_{\mathrm{indodd}}(G)\},&r\text{ even}.
\end{cases}
\]

The final line uses the convention \(\max\{2,\infty\}=\infty\). Thus odd clique attachments collapse the invariant to at most two, whereas even clique attachments preserve any value at least two and preserve non-colorability.

Let \(L_G\) be the ordinary graph Laplacian reduced modulo \(2\), and write \(\nu(G)=n-\operatorname{rank}_{\mathbf F_2} L_G\). When \(r\) is odd there is also an exact labeled two-color count:

\[
O_{G\odot K_r}(2)=2^{(r-1)n+\nu(G)}.
\]

These conclusions apply to disconnected graphs and isolated base vertices. For an unbounded separation, take \(G\) to be the graph obtained by subdividing every edge of \(K_m\), with \(m\equiv3\pmod4\), \(m\ge3\). Its induced-odd chromatic number is \(m\), whereas its clique corona has induced-odd chromatic number \(1\) for every odd \(r\) and \(m\) for every even \(r\). The base family and its value \(m\) were already known; the corona transfer is the conclusion here.

## Assumptions and scope

All graphs are finite, undirected, loopless, and simple. A \(q\)-coloring is a function into a fixed \(q\)-element palette, not necessarily surjective. A nonempty vertex class is an odd induced subgraph precisely when every vertex of that class has odd degree within that class. Empty color classes are allowed in the counting functions. There is at least one core vertex, and \(r,q\) are positive integers; no connectivity or degree assumptions are made on \(G\). The term induced-odd coloring must not be confused with *proper neighborhood-parity odd coloring*, which is a different graph invariant.

For clarity, write \(a_{r,q}=r![z^r]\sinh(z)(\cosh z)^{q-1}\) and \(b_{r,q}=r![z^r](\cosh z)^{q-1}\). When \(r\) is odd, \(a_{r,q}>0\) for every \(q\ge1\). When \(r\) is even, \(b_{r,1}=0\) and \(b_{r,q}>0\) for every \(q\ge2\).

## Proof

Fix a core vertex \(v\) and a color \(c\) assigned to it. Let \(t_j\) be the number of vertices of color \(j\) in its private \(r\)-clique. A private vertex whose color is \(j\ne c\) has exactly \(t_j-1\) same-color neighbors, so the induced-odd condition there is equivalent to \(t_j\) being even whenever \(t_j>0\). A private vertex of color \(c\) has exactly \(t_c\) same-color neighbors: it is adjacent to the \(t_c-1\) other private vertices of color \(c\) and to the root. Therefore, whenever \(t_c>0\), the condition is that \(t_c\) be odd. Thus every non-root color has an even private-clique multiplicity, and \(t_c\) is either zero or odd.

Because \(\sum_jt_j=r\), the parity of \(r\) forces the remaining choice. If \(r\) is odd, then \(t_c\) is odd. The rooted clique contributes an odd number of same-color neighbors to \(v\), so the total induced-odd condition at \(v\) requires its number of same-color neighbors **in the base graph** to be even. If \(r\) is even, then \(t_c=0\), and the condition at \(v\) requires its number of same-color base neighbors to be odd. These equivalences hold independently at every root; there are no edges between different private cliques.

For an odd \(r\), the numbers of ways to color a given private clique with prescribed root color are precisely the permutations of \(r\) labeled positions into one positive odd-sized bin for that root color and \(q-1\) even-sized bins for the other colors. The exponential generating function is \(\sinh z\,(\cosh z)^{q-1}\), yielding \(a_{r,q}\). For an even \(r\), the root-color bin is empty and the other bins are even, giving \(b_{r,q}\). For any fixed admissible root coloring these choices are independent across all \(n\) roots. Taking the products proves both branches of the enumerator, including all cases \(q=1\).

The positivity assertions follow by choosing all private vertices in the root color when \(r\) is odd, and all private vertices in one non-root color when \(r\) is even and \(q\ge2\). For odd \(r\), a one-color base coloring is induced-even precisely when all degrees of \(G\) are even. Every graph has an induced-even coloring with at most two colors: this is Gallai's even-partition theorem, or equivalently follows from the binary calculation below. Hence the first two cases of the chromatic-number formula are exact. For even \(r\), no one-color extension exists, whereas an odd coloring with at least two named colors extends root by root. Conversely every odd coloring of the corona restricts to an odd coloring of \(G\), so its minimum number of colors is exactly the indicated maximum. The argument also covers \(\chi_{\mathrm{indodd}}(G)=\infty\).

For the count with two colors, encode a base vertex's color as \(x_v\in\mathbf F_2\). Let \(d_v\) be its degree modulo \(2\). The parity of its number of same-color neighbors is
\[
d_v+\sum_{u\in N_G(v)}(x_u+x_v)=d_v+(L_Gx)_v.
\]
Thus a binary induced-even coloring is exactly a solution to \(L_Gx=d\) over \(\mathbf F_2\). This system is always consistent. Indeed, if \(y\) belongs to \(\ker L_G\), then
\[
y^{\mathsf T}d=\sum_{\{u,v\}\in E(G)}(y_u+y_v)=y^{\mathsf T}L_Gy=0,
\]
so \(d\) is orthogonal to \(\ker L_G\), hence lies in \(\operatorname{im}L_G\) by symmetry. Its solution set has size \(2^{\nu(G)}\). For odd \(r\),
\[
a_{r,2}=r![z^r]\sinh z\cosh z=r![z^r]\frac{\sinh(2z)}2=2^{r-1},
\]
which yields the formula for \(O_{G\odot K_r}(2)\).

Finally, the cited subdivided-clique construction has \(\chi_{\mathrm{indodd}}(G)=m\) whenever it is colorable, and \(m\equiv3\pmod4\) ensures its order is even. Each subdivision vertex has degree \(2\), and each original vertex has degree \(m-1\), also even. Apply the two parity cases just proved to obtain the unbounded contrast.

## Verification

The standalone standard-library script `verify_induced_odd_clique_corona.py` and the captured output `verify_induced_odd_clique_corona_output.txt` are supplied with this result. After extracting both, run `python3 verify_induced_odd_clique_corona.py`; the script prints `VERIFY_OK` only if every assertion succeeds. The code constructs clique coronas from adjacency lists, directly checks the same-color neighbor parity of every vertex, and independently counts the local multiplicities using integer multinomial coefficients.

It compares **4,467,792 complete color assignments** across **99** direct corona-counting instances with the formula; independently checks local factors for \(1\le r\le5\) and \(1\le q\le4\); and tests one-color boundaries and GF(2)-based two-color equalities on all **1,099 labeled base graphs** of orders \(1\) through \(5\). It also checks the six-cycle distinction between two and three induced-odd colors. Finite tests are not the proof of the infinite statement: the proof above is symbolic and does not rely on finite extrapolation.

## Relationship to prior work

Belmonte and Sau [1] study the **same induced-odd partition** invariant, including its polynomial-time two-colorability test via a system of binary equations (Section 3 and Theorem 3). That earlier fact, and Gallai's classical even-partition theorem, are used rather than asserted as new. Belmonte, Harutyunyan, Köhler, and Melissinos [2] develop structural bounds and record Scott's previously known subdivided-clique examples with arbitrarily large induced-odd chromatic numbers; those base values are also not new. Their accessible original version and the later journal text do not give this complete clique-corona enumerator.

The 2026 paper by Mounisha and coauthors [3] has a superficially matching *corona/odd chromatic* title, but defines a **proper** coloring for which each non-isolated vertex has some neighborhood color of odd multiplicity. It consequently studies a different parameter; neither its displayed exact formulas nor its general upper/lower bounds determine the induced-odd enumerator above. The new claim is the full arbitrary-base odd-induced coloring factorization, its parity-sharp chromatic transfer, and its exact odd-attachment two-color count, not the classical even partition or a routine case of the other odd-coloring notion.

## Limitations

This theorem counts all labeled \(q\)-colorings by a formula in terms of base-graph counting functions; it does not provide a closed form for \(O_G(q)\) or \(E_G(q)\) for arbitrary \(q\). Nor does it give an efficient algorithm for those base counting functions when \(q\) is unrestricted. The special two-color formula applies only to odd clique sizes. It makes no claim that a failed literature search proves historical uniqueness; other unindexed or inaccessible work might contain related factors. No independent mathematical review has been performed.

## References

[1] Rémy Belmonte and Ignasi Sau, *On the complexity of finding large odd induced subgraphs and odd colorings*, first publicly posted 14 February 2020, arXiv:2002.06078, https://arxiv.org/abs/2002.06078. Relevant material: Sections 1, 3, 5.

[2] Rémy Belmonte, Ararat Harutyunyan, Noleen Köhler, Nikolaos Melissinos, *Odd Chromatic Number of Graph Classes*, first publicly posted 6 March 2023, arXiv:2303.03225, https://arxiv.org/abs/2303.03225. The published version is in *Journal of Graph Theory*, 108 (2025), 722–744, DOI:10.1002/jgt.23200.

[3] M. Mounisha, M. Venkatachalam, Marsidi, Dafik, and Gopalakrishnan, *On Odd Chromatic Number of Corona Product of Graphs*, *Palestine Journal of Mathematics* 15 (Special Issue II) (2026), 126–132, https://pjm.ppu.edu/sites/default/files/papers/PJM_15%28Special%20Issue%20II%29_2026%29_126_to_132.pdf. Its definition differs from induced-odd coloring.
