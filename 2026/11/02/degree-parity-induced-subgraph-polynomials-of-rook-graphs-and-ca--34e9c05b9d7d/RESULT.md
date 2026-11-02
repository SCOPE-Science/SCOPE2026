# Degree-parity induced-subgraph polynomials of rook graphs and cardinality gaps in complete prisms

## Finding
Let \(R_{m,n}=K_m\square K_n\), with \(m,n\ge1\), be the rook graph on a labeled \(m\)-by-\(n\) board. Let \(E_{m,n}(z)\) and \(O_{m,n}(z)\) count vertex subsets \(S\) by \(|S|\) such that every degree in the induced subgraph \(R_{m,n}[S]\) is respectively even or odd. By the usual vacuous convention, the empty set contributes \(1\) to **both** polynomials.

For \(r,s\ge0\) and \(\alpha,\beta\in\{0,1\}\), define
\[
 B_{\alpha\beta}(r,s;z)=2^{-r-s}\sum_{p=0}^{r}\sum_{q=0}^{s}(-1)^{\alpha p+\beta q}\binom rp\binom sq
 (1+z)^{rs-rq-sp+2pq}(1-z)^{rq+sp-2pq}.
\]
The formula is valid for zero dimensions, with empty products interpreted as \(1\). Then for every \(m,n\ge1\),
\[
 E_{m,n}(z)=\sum_{r=0}^m\sum_{s=0}^n \binom mr\binom ns
 B_{00}(r,s;z) B_{11}(m-r,n-s;z),
\]
\[
 O_{m,n}(z)=\sum_{r=0}^m\sum_{s=0}^n \binom mr\binom ns
 B_{01}(r,n-s;z) B_{10}(m-r,s;z).
\]
These identities determine every cardinality coefficient for arbitrary rectangular rook graphs.

For the complete prism \(R_{2,n}=K_2\square K_n\), the polynomials simplify to
\[
 E_{2,n}(z)=\frac{(1+2z)^n+(1-2z)^n-2}{4}
 +(1+z)^n-(1-z)^n
 +\frac{(1+z^2)^n+(1-z^2)^n}{2},
\]
\[
 O_{2,n}(z)=\frac{(1+2z)^n+(1-2z)^n+2}{4}
 +\frac{(1+z^2)^n-(1-z^2)^n}{2}.
\]
Their exact sets of attained cardinalities, with \(0\) included by convention, are
\[
 \operatorname{supp}E_{2,n}=\{0,1,\ldots,n\}\cup\{4j:1\le j\le\lfloor n/2\rfloor\},
\]
\[
 \operatorname{supp}O_{2,n}=\{0,2,\ldots,2\lfloor n/2\rfloor\}
 \cup\{4j+2:0\le j\le\lfloor(n-1)/2\rfloor\}.
\]
In particular, above degree \(n\), the even-degree-induced polynomial has coefficients only in degrees divisible by \(4\), while the odd-degree-induced polynomial has coefficients only in degrees congruent to \(2\) modulo \(4\). In either polynomial, every supported degree above \(n\) has coefficient \(\binom n{k/2}\); thus each has arbitrarily long families of missing even cardinalities within its possible degree range. This statement concerns *induced* subgraphs, not all edge-selected spanning subgraphs.

## Assumptions and scope
All graphs are finite, simple, undirected, and labeled; an induced vertex set is counted once regardless of graph automorphisms. Cartesian adjacency in \(R_{m,n}\) means sharing precisely one coordinate. The parameter \(n\) in the prism formulas is any integer at least \(1\); the general formula includes all \(m,n\ge1\). A degree condition on an empty induced graph is vacuously true, so the constant coefficients are both \(1\). No connectivity requirement is imposed on selected sets.

## Proof
**Step 1: a degree-parity reduction.** Identify \(R_{m,n}\) with the line graph of the complete bipartite graph \(K_{m,n}\). Every vertex subset of the rook graph corresponds bijectively to a \(0\)-\(1\) incidence matrix \(A=(a_{ij})\) for a selected edge set of \(K_{m,n}\). Write \(d_i=\sum_j a_{ij}\) and \(e_j=\sum_i a_{ij}\). For a selected cell \((i,j)\), its number of selected rook neighbors is exactly \(d_i+e_j-2\). Hence its induced degree is even if and only if the row and column sums have the same parity, and odd if and only if those parities differ.

**Step 2: binary matrices with prescribed margins modulo two.** For nonnegative \(r,s\) define \(B_{\alpha\beta}(r,s;z)\) equivalently as the size enumerator of binary \(r\)-by-\(s\) matrices whose every row sum is \(\alpha\pmod2\) and every column sum is \(\beta\pmod2\). For each row and column, the indicator of the required parity is \(\frac12\sum_{\sigma\in\{\pm1\}}\sigma^{\text{sum}-\alpha}\). Multiplying these indicators and summing binary matrices gives
\[
 2^{-r-s}\sum_{\sigma\in\{\pm1\}^r}\sum_{\tau\in\{\pm1\}^s}
 \left(\prod_i\sigma_i^{\alpha}\right)
 \left(\prod_j\tau_j^{\beta}\right)
 \prod_{i,j}(1+z\sigma_i\tau_j).
\]
When exactly \(p\) row signs and \(q\) column signs are negative, precisely \(rq+sp-2pq\) of the \(rs\) products \(\sigma_i\tau_j\) are negative. Grouping equal sign counts gives the displayed finite binomial Fourier expression. This also establishes nonnegative integer coefficients despite the apparent rational prefactor. If a dimension is zero, a nonzero prescribed parity on a nonempty set of rows or columns is impossible, as correctly enforced by the same formula.

**Step 3: factorization by parity classes.** Each selected matrix has uniquely determined even-row, odd-row, even-column, and odd-column classes, including unused rows/columns in the even classes. Suppose there are \(r\) even rows and \(s\) even columns. For even-degree induced subgraphs, Step 1 forbids cells in the two opposite-parity rectangles, leaving the even/even and odd/odd rectangles. Their feasible binary choices are independent and have enumerators \(B_{00}(r,s;z)\) and \(B_{11}(m-r,n-s;z)\). Choose the row/column classes in \(\binom mr\binom ns\) ways. This proves the formula for \(E_{m,n}\) without overcounting. For odd-degree induced subgraphs, only the even/odd and odd/even rectangles may contain cells, with independent enumerators \(B_{01}(r,n-s;z)\) and \(B_{10}(m-r,s;z)\), proving the other formula.

**Step 4: the complete-prism dichotomy.** Write \(a\) and \(b\) for the numbers of selected cells in the two rows, and \(t\) for the number of columns selected twice. If \(t>0\), any singly selected cell in a row has induced degree one less than a doubly selected cell in that same row: respectively \(a-1\) versus \(a\) (and similarly \(b-1\) versus \(b\)). Therefore a uniform degree parity condition forces both rows to contain no singly selected cells; since \(t>0\), the selected columns are exactly \(t\) full pairs. Every selected degree then equals \(t\), contributing \(\binom nt z^{2t}\) to \(E_{2,n}\) when \(t\) is even and to \(O_{2,n}\) when \(t\) is odd.

If \(t=0\), the induced subgraph is the disjoint union of two cliques of orders \(a\) and \(b\) (empty cliques permitted). Its degrees are all even exactly when each nonempty clique has odd order, and are all odd exactly when both clique sizes are even (including zero). The trivariate labeling of each column as unselected, selected above, or selected below gives the two parity-filtered multinomial enumerators
\[
 \frac{(1+2z)^n+(1-2z)^n-2}{4}+(1+z)^n-(1-z)^n
\]
for even degree and
\[
 \frac{(1+2z)^n+(1-2z)^n+2}{4}
\]
for odd degree. Adding the doubled-column contributions (even or odd \(t\), respectively) proves both prism formulas. In particular \(t=0\) and \(t>0\) are disjoint, so no terms are duplicated.

**Step 5: exact support.** For \(t=0\), the even-degree selections realize every size \(0\le k\le n\): for odd \(k\), use an odd clique of size \(k\) in one row; for even positive \(k\), use two positive odd clique sizes summing to \(k\) in disjoint columns. All odd-degree \(t=0\) selections have even size, and every even \(k\le2\lfloor n/2\rfloor\) occurs by choosing an even number \(k\) of singly selected cells in one row. For \(t>0\), the sizes are \(2t\), with \(t\) positive even in the even-degree case and positive odd in the odd-degree case. These are exactly the displayed support sets. A size above \(n\) cannot arise from \(t=0\), and its coefficient is therefore precisely \(\binom n{k/2}\) when \(k/2\) has the required parity and otherwise zero. This proves the sharp above-\(n\) residue restriction and its unbounded cardinality gaps.

## Verification
A standalone standard-library Python program `verify.py` derives rook adjacency directly from row/column equality, enumerates vertex subsets, and checks every selected vertex's degree parity. Its first implementation does not use the parity-block formula. A second implementation independently enumerates prescribed-parity binary matrices and combines them; a third calculates the Fourier polynomials coefficientwise. It also uses independent two-row column counting to check the closed forms and supports.

Running `python3 verify.py` produced:

`VERIFY_OK general_graphs=19 prism_graphs=10 direct_vertex_subsets=1412734 fourier_blocks=64 symbolic_support_orders=60`

Graph-level checks covered all \(1\le m\le4\), \(1\le n\le6\) with \(mn\le12\), and all complete prisms with \(1\le n\le10\). The binomial Fourier expression was compared with direct binary-matrix enumeration in 64 parity/dimension cases; support identities were compared for all \(1\le n\le60\). All finite tests are corroboration; they are not substitutes for Steps 1–5. Example polynomials include
\[
 O_{2,5}(z)=1+25z^2+40z^4+10z^6+z^{10},
\]
\[
 E_{2,5}(z)=1+10z+20z^2+20z^3+50z^4+2z^5+5z^8.
\]

## Relationship to prior work
Belmonte and Sau's 2020 work studies complexity, algorithms, and extremal questions for even- and odd-degree induced subgraphs in arbitrary graphs. It motivates computing the entire cardinality profile on structured graph families but does not imply the rook-graph parity-block factorization or the closed prism polynomials. Belmonte, Harutyunyan, Köhler, and Melissinos (2023) study odd vertex colorings; this is different from enumerating induced subsets with uniform vertex-degree parity. Dörfler, Roth, Schmitt, and Wellnitz (2021) study general hardness of counting induced subgraphs, rather than these particular explicit coefficient formulas. The line-graph correspondence is standard, and the roots-of-unity parity filter is a standard counting method; novelty is claimed only for the specific joint rook-graph polynomials and their complete-prism support consequences, subject to publication-priority uncertainty.

## Limitations
No novelty proof against all literature is asserted; related results outside inspected sources, alternative terminology, or inaccessible publications may contain equivalent formulas. The large-rook general formula is finite but not simplified to a low-dimensional elementary expression. The complete-prism special case gives the sharp explicit support and residue law. The odd-degree convention includes the empty set despite its lack of positive-degree vertices; to require nonempty sets, subtract \(1\) from \(O_{m,n}(z)\). No statements about connected induced subgraphs, edge-spanning subgraphs, or arbitrary nonrook graph classes are claimed. The work has not undergone independent mathematical audit.

## References
1. R. Belmonte and I. Sau, *On the complexity of finding large odd induced subgraphs and odd colorings*, arXiv:2002.06078, first publicly posted 2020-02-14, https://arxiv.org/abs/2002.06078 .
2. R. Belmonte, A. Harutyunyan, N. Köhler, and N. Melissinos, *Odd Chromatic Number of Graph Classes*, arXiv:2303.03225, first publicly posted 2023-03-06, https://arxiv.org/abs/2303.03225 .
3. J. Dörfler, M. Roth, J. Schmitt, and P. Wellnitz, *Counting Induced Subgraphs: An Algebraic Approach to #W[1]-Hardness*, *Algorithmica* (2021), https://doi.org/10.1007/s00453-021-00894-9 .
