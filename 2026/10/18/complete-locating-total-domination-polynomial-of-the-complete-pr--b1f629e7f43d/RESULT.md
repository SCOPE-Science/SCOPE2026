# Complete locating-total domination polynomial of the complete prisms \(K_2\square K_n\)

## Finding

Let \(G_n=K_2\square K_n\), where \(n\ge 2\). A locating-total dominating set \(S\) has a selected neighbor for every vertex, and the sets \(N(v)\cap S\), as \(v\) ranges over vertices outside \(S\), are pairwise distinct. Its cardinality polynomial is
\[
L_n(z)=\sum_{S\text{ locating-total dominating}}z^{|S|}.
\]
For every integer \(n\ge4\), put \(B(z)=2z+z^2\). Then
\[
\boxed{L_n(z)=B(z)^n+nB(z)^{n-1}-2n^2z^{n-1}-2nz^n.}
\]
The remaining orders are
\[
L_2(z)=4z^2+4z^3+z^4,\qquad L_3(z)=14z^3+15z^4+6z^5+z^6.
\]
In particular the minimum cardinality and its exact multiplicity are
\[
\gamma_t^L(G_n)=\begin{cases}n,&2\le n\le4,\\ n-1,&n\ge5,\end{cases}
\qquad
[z^{\gamma_t^L(G_n)}]L_n(z)=\begin{cases}4,&n=2,\\14,&n=3,\\56,&n=4,\\n(2^{n-1}-2n),&n\ge5.\end{cases}
\]
These assertions follow from an exact structural characterization of *all* locating-total dominating sets, proved below.

## Assumptions and scope

All graphs are finite, simple, undirected and have labeled vertices. The two clique layers are \(A=\{a_1,\ldots,a_n\}\) and \(C=\{b_1,\ldots,b_n\}\): all distinct pairs in either layer are adjacent, and the only cross-layer edges are \(a_ib_i\) for \(1\le i\le n\). The complete prism is also the line graph of \(K_{2,n}\). We use *open* neighborhoods \(N(v)\), and we distinguish only vertices outside the selected set. In particular a selected vertex must itself have a selected neighbor.

For a vertex set \(S\), define the index sets \(X=\{i:a_i\in S\}\) and \(Y=\{i:b_i\in S\}\), and write \(p=|X|\), \(q=|Y|\), and \(h=n-|X\cup Y|\). The exact characterization is:

\(S\) is locating-total dominating if and only if all five conditions hold:

1. \(h\le1\).
2. \(p=0\) implies \(q=n\).
3. \(q=0\) implies \(p=n\).
4. \(p=1\) implies \(X\subseteq Y\).
5. \(q=1\) implies \(Y\subseteq X\).

## Proof

**Characterization: locating within a layer.** For an unselected vertex \(a_j\), its selected-neighbor set is \(\{a_i:i\in X\}\), together with \(b_j\) when \(j\in Y\). Likewise, an unselected \(b_j\) has the selected-neighbor set \(\{b_i:i\in Y\}\), together with \(a_j\) when \(j\in X\). Thus two distinct unselected vertices within the same layer have the same selected-neighbor set exactly when their two columns are both wholly unselected. This establishes that locating inside the two layers is equivalent to \(h\le1\).

**Characterization: total domination.** If \(p\ge2\), each vertex of layer \(A\), including each selected vertex, has a selected neighbor in that layer. If \(p=1\), the sole selected vertex \(a_j\) needs its matched neighbor \(b_j\) selected, equivalent to \(X\subseteq Y\); then every other \(A\)-vertex is adjacent to \(a_j\). If \(p=0\), every \(a_j\) needs its matched \(b_j\) selected, equivalent to \(q=n\). The symmetric conditions characterize total domination on layer \(C\).

**Characterization: locating across layers.** If \(p\ge2\), the selected-neighbor set of every unselected \(A\)-vertex has at least two vertices from \(A\), while that of every unselected \(C\)-vertex has at most one vertex from \(A\). Therefore cross-layer signatures differ. If \(p\le1\) but \(q\ge2\), exchange the layers. Otherwise \(p\le1\) and \(q\le1\). Total domination excludes zero counts and forces \(p=q=1\) with \(X=Y=\{j\}\). All remaining \(A\)-vertices have selected-neighbor set \(\{a_j\}\), whereas remaining \(C\)-vertices have \(\{b_j\}\); these are unequal. (The within-layer requirement permits this case only for the appropriate small orders.) The five stated conditions are therefore necessary and sufficient.

**Polynomial for \(n\ge4\).** First enforce only \(h\le1\). Each represented column has precisely three choices: \(a_i\) alone, \(b_i\) alone, or both, respectively of weights \(z\), \(z\), and \(z^2\). Thus the unrestricted polynomial with no more than one wholly empty column is \(B(z)^n+nB(z)^{n-1}\).

Remove sets with \(p\le1\) or \(q\le1\), then restore those satisfying the total-domination conditions. The \(p\le1\) group, counted with its multiplicities over labeled columns, has polynomial
\[
n^2z^{n-1}+(n^2+1)z^n+nz^{n+1}.
\]
Indeed, the \(p=0\) cases are all second-layer vertices (one case) or all except one (\(n\) cases); for \(p=1\), choose the unique index among \(n\) possibilities, choose whether its second-layer mate is included, and optionally omit one other column. Of these, exactly the \(p=0,q=n\) case and the \(p=1,X\subseteq Y\) cases are valid, contributing
\[
\bigl(1+n(n-1)\bigr)z^n+nz^{n+1}.
\]
The net deletion for \(p\le1\) is therefore \(n^2z^{n-1}+nz^n\). The same deletion occurs symmetrically for \(q\le1\). For \(n\ge4\), the two deleted groups cannot intersect: \(p,q\le1\) would cover at most two columns, contradicting \(h\le1\), which requires at least three represented columns. Subtracting twice the net deletion proves the claimed polynomial.

**Small orders and minima.** Apply the five necessary-and-sufficient conditions directly for \(n=2,3\), grouping the possible choices by cardinality. The resulting coefficient lists, from smallest to largest degree, are \((4,4,1)\) and \((14,15,6,1)\), respectively. For \(n\ge4\), at least \(n-1\) columns must be represented, so no valid set has fewer than \(n-1\) vertices. Equality would require one empty column and exactly one selected vertex in every other column, with \(p,q\ge2\); this is impossible for \(n=4\), where only three vertices would be selected, but possible for every \(n\ge5\). Choose the missing column in \(n\) ways and distribute the other \(n-1\) singleton selections between the two layers, with at least two in each: \(2^{n-1}-2-2(n-1)=2^{n-1}-2n\) possibilities. This proves both the sharp cardinality and the minimum-set count for \(n\ge5\). The coefficient at degree four in the \(n=4\) polynomial is \(56\), and the small-order polynomials give the other stated cases.

## Verification

The standalone Python 3 program `verify.py` builds the graph directly from its adjacency rule, enumerates every subset of vertices for \(2\le n\le9\), independently tests total domination and injectivity of selected-neighborhood signatures, and compares the full coefficient array against the closed formula and the structural characterization. These searches examine exactly \(349{,}520\) vertex subsets. The program also checks the polynomial's minimum degree and coefficient across \(4\le n\le200\). Running `python verify.py` produced the attached `verification-output.txt` with a final PASS line. The proof above is the basis of the infinite quantification; the finite enumerations are consistency checks, not substitutes for it.

## Relationship to prior work

Locating-total domination was investigated by Henning and Jafari Rad (2012), which explicitly records the three-prism numerical instance. Chakraborty, Foucaud, Hakanen, Henning, and Wagler (first publicly posted 25 November 2022) prove a general half-order upper bound for twin-free cobipartite graphs; it gives \(\gamma_t^L(G_n)\le n\) for \(n\ge3\), but does not give the sharp \(n-1\) minimum for \(n\ge5\), the entire generating polynomial, or a classification of all codes. Argiroffo and collaborators (2019) derive locating-domination results under other graph operations; their accessible treatment does not provide this particular exact prism polynomial. Omamalin (2026) studies the *join* polynomial, whereas for \(n\ge3\) the graph \(G_n\) has connected complement and is not a nontrivial graph join, so that advertised family does not directly cover the theorem. No comprehensive uniqueness claim is made from bibliographic search alone.

## Limitations

The theorem concerns the two-clique matched prism \(K_2\square K_n\), not general rook graphs \(K_m\square K_n\) with \(m>2\), and uses locating-total domination rather than stronger open-locating notions. Counts refer to vertex-labeled sets, without quotienting by automorphisms. The available description of the 2026 join-polynomial paper was abstract-level, and other unindexed or inaccessible literature could contain an equivalent statement. All checks are non-independent; no external scientific audit has been performed.

## References

1. M. A. Henning and N. Jafari Rad, *Locating-total domination in graphs*, Discrete Applied Mathematics **160** (2012), 1986–1993, DOI: 10.1016/j.dam.2012.04.004.
2. D. Chakraborty, F. Foucaud, A. Hakanen, M. A. Henning, and A. K. Wagler, *Progress towards the two-thirds conjecture on locating-total dominating sets*, first posted 2022-11-25, arXiv:2211.14178; Discrete Mathematics **347** (2024), 114176, DOI: 10.1016/j.disc.2024.114176.
3. G. R. Argiroffo et al., *The Identifying Code, the Locating-dominating, the Open Locating-dominating and the Locating Total-dominating Problems Under Some Graph Operations*, Electronic Notes in Theoretical Computer Science **346** (2019), DOI: 10.1016/j.entcs.2019.08.013.
4. B. Omamalin, *The Locating Total Domination Polynomial of the Join of Graphs*, International Journal of Mathematics and Computer Science (2026), DOI: 10.69793/ijmcs/02.2026/benjamin (abstract examined; full text unavailable).
