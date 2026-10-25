# Perfect Roman domination and all minimum functions on rectangular rook graphs

## Finding

**Theorem.** For all integers \(2\le p\le q\), let \(R_{p,q}=K_p\square K_q\). A perfect Roman dominating function is a map \(f:V(R_{p,q})\to\{0,1,2\}\) such that each vertex labeled \(0\) has exactly one adjacent vertex labeled \(2\); its weight is the sum of its vertex labels. Then

\[
\gamma_R^{\mathrm p}(R_{p,q})=\begin{cases}3,&(p,q)=(2,2),\\2p,&\text{otherwise}.
\end{cases}
\]

The complete number of functions of minimum weight is

\[
M(p,q)=\begin{cases}
4,&(p,q)=(2,2),\\
9,&(p,q)=(2,3),\\
15,&(p,q)=(3,3),\\
2p,&p=q\ge4,\\
q,&\text{otherwise}.
\end{cases}
\]

Every minimum function is one of these explicitly classified configurations:

1. For every board except \((2,2)\), choose one of its \(q\) columns, place label \(2\) at each of its \(p\) vertices, and label every other vertex \(0\).
2. When \(p=q\ge3\), choose one of the \(p\) rows instead, placing \(2\) throughout that row and \(0\) elsewhere.
3. At \((2,2)\), \((2,3)\), and \((3,3)\), a singleton-defender function is also minimum: choose one cell, place \(2\) there, label all its other row and column cells \(0\), and label all remaining cells \(1\). At \((2,2)\) only these singleton functions are minimum.

In the third family the numbers of configurations are respectively \(4,6,9\). These families do not overlap because their sets of \(2\)-labeled vertices have different cardinalities or different orientations.

## Assumptions and scope

Graphs are simple and undirected. Rows and columns are the two complete-graph coordinates; two distinct cells are adjacent exactly when they share a row or a column. The theorem concerns *perfect Roman* rather than ordinary Roman or total perfect Roman domination. It classifies labeled functions and does not divide by graph automorphisms. All integer parameters satisfy \(2\le p\le q\); exchanging factor order covers arbitrary two-factor rook graphs.

## Proof

**Exact completion of a set of defenders.** Fix the set \(T\) of vertices assigned label \(2\), with \(t=|T|\). For each row \(i\), let \(a_i\) be the number of defenders in that row, and for each column \(j\), let \(b_j\) be the number of defenders in that column. Put \(r=|\{i:a_i>0\}|\), \(c=|\{j:b_j>0\}|\), \(r_1=|\{i:a_i=1\}|\), and \(c_1=|\{j:b_j=1\}|\).

For a cell outside \(T\), its number of adjacent defenders equals \(a_i+b_j\). Such a cell can be labeled \(0\) if and only if this sum is exactly \(1\). Because no cell with both an occupied row and an occupied column has sum \(1\), the exact number of eligible zero-cells is

\[
e(T)=r_1(q-c)+(p-r)c_1.
\]

Every other nondefender cell must carry label \(1\). Therefore for each fixed \(T\) there exists a unique minimum-weight completion, and its weight is

\[
w(T)=pq+t-e(T).
\]

A function with the same defenders and additional labels \(1\) at eligible cells has strictly greater weight. In particular, if \(T=\varnothing\), the weight is \(pq\), and generally every function has weight at least \(2t\).

**Lower bound for sparse defenders.** Suppose \(1\le t<p\). Necessarily \(1\le r,c\le t<p\). Since \(r_1\le r\) and \(c_1\le c\),

\[
\begin{aligned}
w(T)&\ge pq+t-r(q-c)-(p-r)c\\
&=(p-r)(q-c)+rc+t\\
&\ge(p-r)(p-c)+rc+\max\{r,c\}.
\end{aligned}
\]

Write \(s=\max\{r,c\}\) and \(\ell=\min\{r,c\}\), so \(1\le\ell\le s\le p-1\). The last bound becomes

\[
h=p(p-s)+\ell(2s-p)+s.
\]

For \(p\ge4\), if \(s\le p/2\), the coefficient of \(\ell\) is nonpositive, whence

\[
h\ge (p-s)^2+s^2+s\ge p^2/2+1>2p.
\]

If instead \(s>p/2\), the coefficient is positive, so

\[
h\ge p(p-s)+(2s-p)+s=p(p-1)-s(p-3)\ge3(p-1)>2p.
\]

Thus any function with fewer than \(p\) defenders has weight strictly greater than \(2p\) whenever \(p\ge4\).

For \(p=3\), \(r,c\le2\). The same lower bound shows equality \(w(T)=6\) is possible only for \((r,c,t)=(1,1,1),(1,2,2),(2,1,2)\) on a square board \(q=3\). The latter two are impossible: two defenders in one row (respectively column) make that occupied row (respectively column) have multiplicity two; the exact formula for \(e(T)\) then gives weight \(7\), not \(6\). For a single defender the unique minimum completion has weight \(pq+1-(q-1)-(p-1)=2q\), equal to \(6\) precisely when \(q=3\). When \(q>3\), every sparse-defender configuration weighs strictly more than \(6\).

For \(p=2\) and \(1\le t<p\), there is precisely one defender. Its minimum completion has weight \(q+1\); this is \(3\) for \(q=2\), \(4\) for \(q=3\), and strictly greater than \(4\) for \(q\ge4\).

**At least \(p\) defenders and equality structure.** For \(t\ge p\), the weight is at least \(2t\ge2p\); equality requires \(t=p\) and every nondefender cell to have label \(0\). Thus each nondefender cell must have exactly one adjacent defender. For the occupied-row and occupied-column sets \(R,C\), any cell of \(R\times C\) outside \(T\) has at least two adjacent defenders; hence \(R\times C\subseteq T\), and therefore \(T=R\times C\). Moreover, an unoccupied row and an unoccupied column cannot coexist, since their intersection would have no adjacent defender. Consequently either \(r=p\) or \(c=q\). From \(t=rc=p\), the former means an entire column; the latter is possible only if \(p=q\) and means an entire row. All such configurations are feasible and have weight \(2p\).

Combining the sparse and dense cases proves the exact minimum and exhaustive classification. When \((p,q)=(2,2)\), a singleton defender attains weight \(3\), which is below all configurations with \(t\ge2\); exactly four positions are available. Otherwise the \(q\) columns always attain weight \(2p\), the \(p\) additional rows do so precisely for \(p=q\), and the singleton exceptions occur only at \((2,3)\) and \((3,3)\). This gives the asserted counting formula. \(\square\)

## Verification

The self-contained Python script `verify.py` tests the defining neighborhood condition directly on \(617{,}544\) ternary assignments for six small rectangular boards, then tests all \(254{,}517\) defender sets of sizes at most \(p\) on eleven boards (through \(5\times6\)), and checks \(9{,}103{,}740\) integer cases of the stated sparse-defender bound. Its run transcript is `verification_output.txt`, ending in `VERIFY_OK`. It makes no external requests and uses only the Python standard library. Execute `python verify.py` in the directory containing the files. These are finite consistency checks; the unrestricted quantifiers follow from the proof above, not from extrapolating computations.

## Relationship to prior work

Almulhim, Akwu and Al Subaiei (2022) study perfect Roman domination of Cartesian products of paths and/or cycles. Their complete open-access article does not determine rectangular products of complete graphs. Paleta and Jamil (2020) give general inequalities for perfect Roman domination, including an upper bound via perfect dominating sets. For the present rook graphs that upper bound already implies \(\gamma_R^{\mathrm p}\le2p\); the upper bound alone is **not** claimed as new. The result here supplies the all-parameter sharp lower bound and complete optimizer classification, with exceptional count transitions at three small boards. Henning and Klostermeyer (2018) develop broader bounds for regular graphs but do not classify these functions. Ordinary Roman and total perfect Roman domination are different parameters and do not imply this classification. The identity \(R_{p,q}\cong L(K_{p,q})\) has also been considered when comparing equivalent formulations.

## Limitations

The theorem is limited to products of exactly two complete graphs with both factor orders at least \(2\). It neither determines the polynomial of all feasible (nonminimum) perfect Roman functions nor addresses general Hamming graphs. A highly relevant full-text Cartesian-product paper and two additional primary papers were inspected; equivalent unindexed literature may still affect priority. Computational checks are finite and do not constitute independent mathematical validation.

## References

1. A. Almulhim, A. D. Akwu and B. Al Subaiei, *The Perfect Roman Domination Number of the Cartesian Product of Some Graphs*, Journal of Mathematics (2022), article 1957027, https://doi.org/10.1155/2022/1957027 (first published 18 October 2022).
2. L. M. Paleta and F. P. Jamil, *More on Perfect Roman Domination in Graphs*, European Journal of Pure and Applied Mathematics **13** (2020), https://doi.org/10.29020/nybg.ejpam.v13i3.3763.
3. M. A. Henning and W. F. Klostermeyer, *Perfect Roman Domination in Regular Graphs*, Applied Analysis and Discrete Mathematics **12** (2018), https://doi.org/10.2298/AADM1801143H.
