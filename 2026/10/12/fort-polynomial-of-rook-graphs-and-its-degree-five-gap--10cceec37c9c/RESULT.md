# Fort polynomial of rook graphs and its degree-five gap

## Finding
For a finite graph \(G\), a **fort** is a nonempty vertex set \(F\) such that every vertex outside \(F\) has either zero or at least two neighbors in \(F\). Define its all-fort cardinality polynomial by
\[
\Phi_G(z)=\sum_{\substack{\varnothing\ne F\subseteq V(G)\\F\text{ a fort}}}z^{|F|}.
\]
For every pair of positive integers \(m,n\), put \(R_{m,n}=K_m\square K_n\) (the rook graph) and \(\Phi_{m,n}=\Phi_{R_{m,n}}\). For positive integers \(p,q\) and \(a,b\in\{1,2\}\), write
\[
H_{p,q}^{a,b}(z)=\sum_{M}z^{\sum_{i,j}M_{ij}},
\]
where the sum runs over all labeled \(p\times q\) zero-one matrices \(M\) whose row sums are all at least \(a\) and whose column sums are all at least \(b\); the sum is zero if no such matrix exists.

**Theorem (all-fort enumerator).** For every \(m,n\ge1\),
\[
\boxed{\displaystyle\Phi_{m,n}(z)=\sum_{p=1}^{m}\sum_{q=1}^{n}\binom mp\binom nq H_{p,q}^{1+\mathbf1_{q<n},\;1+\mathbf1_{p<m}}(z).}
\]
Each auxiliary polynomial has the explicit finite-state recursion proved below, so this evaluates every coefficient using polynomially many integer-arithmetic operations in \(m+n\).

**Corollary (sharp early coefficient gap).** For all \(m,n\ge6\),
\[
[z^4]\Phi_{m,n}=\binom m2\binom n2,\qquad[z^5]\Phi_{m,n}=0,\qquad[z^6]\Phi_{m,n}>0.
\]
For all \(m,n\ge7\), the degree-six coefficient is exactly
\[
\boxed{[z^6]\Phi_{m,n}=\binom m2\binom n3+\binom m3\binom n2+6\binom m3\binom n3.}
\]
Thus these polynomials have an internal zero coefficient between two positive coefficients, so they are not unimodal, not log-concave and not real-rooted.

## Assumptions and scope
All graphs are finite, undirected and simple; \(K_1\) is permitted. Rook-graph vertices are grid cells \((i,j)\), with two distinct cells adjacent precisely when they share a row or a column. A nonempty fort is counted once, even if it contains other forts. All row and column labels remain distinct. Coefficients of absent degrees are zero; the empty vertex set is **not** a fort. The coefficient-gap assertions require both side lengths at least six. The explicit degree-six formula requires both lengths at least seven.

## Proof
**1. Row/column support characterization.** Represent \(F\) by its \(m\times n\) zero-one incidence matrix. Let \(r_i\) and \(c_j\) be the number of its selected cells in row \(i\) and column \(j\). For any unselected cell \((i,j)\), its number of selected graph neighbors is **exactly** \(r_i+c_j\), because the row and column meet only at that unselected cell. Thus \(F\) is a fort precisely when no zero entry has \(r_i+c_j=1\).

Fix the unique sets of occupied rows and occupied columns, of respective cardinalities \(p,q\). Every occupied row has at least one selected cell. If \(q<n\), some column is empty; then a one-cell occupied row would produce an unselected cell with exactly one selected neighbor. Hence every occupied row must have at least two cells when \(q<n\). Conversely, if \(q=n\), no empty column exists, so an occupied row is allowed to have exactly one cell. By the same argument in the transposed picture, every occupied column must contain at least two cells if \(p<m\), and at least one if \(p=m\). These conditions are sufficient: a zero cell at an occupied row and occupied column sees at least two selected neighbors; a zero cell between two empty lines sees none; and when exactly one of its lines is occupied the relevant two-cell bound ensures it sees at least two. Therefore the stipulated row/column lower bounds characterize forts exactly. Choosing the occupied row and column labels yields the displayed sum, with neither omission nor overcounting.

**2. Explicit recurrence for \(H\).** Fix \(p,q,a,b\). Process the \(q\) labeled columns in sequence. For \(0\le t\le q\), define \(T_t(i,j,k;z)\) as the polynomial recording the first \(t\) columns for which each processed column contains at least \(b\) ones, and among the \(p\) labeled rows exactly \(i\) have accumulated zero ones, exactly \(j\) have accumulated one, and exactly \(k\) have accumulated at least two; here \(i+j+k=p\). Initialize \(T_0(p,0,0;z)=1\), with all other states zero. For each state \((i,j,k)\), choose \(s\) rows from the zero class, \(t\) from the one class, and \(u\) from the at-least-two class to receive a one in the next column. To avoid confusion with the column count, let the column step be \(h\), with choices \(s,t,u\) as described. For every \(s+t+u\ge b\), update
\[
\begin{aligned}
T_{h+1}(i-s,\,j+s-t,\,k+t;z)\ &\mathrel{+}=
\binom{i}{s}\binom{j}{t}\binom{k}{u}
\,z^{s+t+u}T_h(i,j,k;z),\\
&0\le s\le i,\quad 0\le t\le j,\quad 0\le u\le k.
\end{aligned}
\]
At the end, retain precisely states with \(i=0\) if \(a=1\), and with \(i=j=0\) if \(a=2\). The sum of the retained state polynomials is \(H_{p,q}^{a,b}(z)\). The state classes partition the labeled rows uniquely and each choice has exactly the displayed binomial multiplicity. Therefore induction on the processed columns proves the recurrence counts every admissible matrix once. There are finitely many polynomially bounded states, transitions and polynomial degrees (at most \(pq\)), giving polynomially many integer operations for all \(m,n\).

**3. The degree gap.** Suppose \(m,n\ge6\) and \(F\) contains at most five vertices. Its support cannot occupy every row or every column: doing so would require at least six selected cells. Thus the support characterization forces every occupied row and every occupied column to have degree at least two. If the fort has \(k\) selected cells, its occupied row and column counts satisfy \(2p\le k\) and \(2q\le k\). For \(k=4\), necessarily \(p=q=2\); all four cells of the chosen \(2\times2\) subarray must be present. This gives \(\binom m2\binom n2\) forts. For \(k=5\), the same inequalities force \(p,q\le2\), allowing at most four cells, a contradiction. On the other hand a full \(2\times3\) rectangle is a six-vertex fort, proving positivity in degree six.

When \(m,n\ge7\), any six-vertex fort again leaves an empty row and column, and satisfies \(2\le p,q\le3\). With \((p,q)=(2,3)\) or \((3,2)\), its six cells fill the whole rectangle. With \((p,q)=(3,3)\), every row and column must have exactly two ones, so its three absent cells form a permutation matrix, with \(3!=6\) choices. No other supports exist; choosing their labels gives the asserted coefficient. (When a side has size six, a six-cell fort may also occupy that entire side; this is why the formula is restricted to lengths at least seven.) Since a coefficient sequence with positive fourth and sixth coefficients but zero fifth coefficient cannot be unimodal or log-concave, both assertions follow. A polynomial with nonnegative coefficients and only real roots has no internal coefficient zero between positive terms, so real-rootedness also fails.

## Verification
The included standalone file `verify.py` uses two independent implementations: direct adjacency-neighbor tests for every nonempty vertex subset of twenty-one small rook graphs, and the support-conditioned polynomial recurrence. They agree on every tested graph (1,423,541 candidate subsets). Additional checks compare low-degree formulas at side lengths five through eight and confirm the degree-six boundary at length six. Run `python3 verify.py` with Python 3 standard library; `verification_output.txt` records the output produced in this package. This finite computation is corroboration, not a replacement for the proof for all positive integers.

## Relationship to prior work
Abara and Pelayo's preprint (2022), citing an earlier theorem, gives the failed zero forcing number \(F(K_m\square K_n)=mn-4\) when the larger side is at least four and the smaller side at least two (their Theorem 3.7). By the fort/stalled-set complement correspondence, this already implies the **minimum fort size four**; that scalar consequence is expressly not claimed as new here. Cameron, Hogben, Kenter, Mojallal and Schuerger (first posted 2023) study fort hypergraphs, fractional forcing and Cartesian products, including general bounds, but their results do not tabulate all cardinalities of forts of rook graphs. Becker and coauthors (first posted 2024) count **minimal** forts in several other families; an all-fort enumerator requires additional intersection and containment information. The present statement refines the scalar perspective by giving every coefficient and the uniform internal gap of the rook-graph polynomial.

## Limitations
The result concerns forts, not the zero forcing polynomial or the domination polynomial, and counts nonminimal as well as minimal forts. It gives an explicit exact dynamic program rather than a closed elementary product formula. Arithmetic-operation complexity does not bound coefficient bit lengths. The displayed degree-six expression is not asserted for either side of size six. Published-record searches cannot exclude a mathematically equivalent formulation under a different graph-theoretic or matrix-enumeration name. Independent audit has not been performed.

## References
1. P. A. B. Pelayo and M. N. M. Abara, *Maximal failed zero forcing sets for products of two graphs*, arXiv:2202.04997v1, first posted 2022-02-10. https://arxiv.org/html/2202.04997v1 . Theorem 3.7 and Section 3.1.
2. T. R. Cameron, L. Hogben, F. H. J. Kenter, S. A. Mojallal, and H. Schuerger, *Forts, (fractional) zero forcing, and Cartesian products of graphs*, arXiv:2310.17904, first posted 2023-10-27. https://arxiv.org/html/2310.17904v3 . Sections 2–4.
3. P. Becker, T. R. Cameron, D. Hanely, B. Ong, and J. P. Previte, *On the number of minimal forts of a graph*, arXiv:2404.05963v1, first posted 2024-04-09. https://arxiv.org/html/2404.05963v1 . Introduction, Section 3 and enumerative sections.
