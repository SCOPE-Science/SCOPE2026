# Connected-domination polynomials of cycle powers: the one-long-gap theorem

## Finding

For integers \(n\ge 3\) and \(r\ge 1\), let \(C_n^r\) be the graph on \(\mathbb Z/n\mathbb Z\) in which distinct vertices are adjacent when their shortest circular distance is at most \(r\). Let \(Q_{n,r}(z)=\sum_S z^{|S|}\), summed over **nonempty connected dominating vertex sets** \(S\) of \(C_n^r\). Write
\[
A_r(u)=u+u^2+\cdots+u^r,\qquad
B_r(u)=u^{r+1}+u^{r+2}+\cdots+u^{2r+1}.
\]

**Complete size distribution.** For each \(1\le k\le n\),
\[
[z^k]Q_{n,r}(z)
=\frac{n}{k}[u^n]A_r(u)^k+
n[u^n]B_r(u)A_r(u)^{k-1}.
\]
With the harmless complete-graph conventions \(C_1^r=K_1\) and \(C_2^r=K_2\), the following formal power-series identity simultaneously encodes all orders:
\[
\sum_{n\ge1}\frac{Q_{n,r}(z)}n\,u^n
=-\log(1-zA_r(u))+\frac{zB_r(u)}{1-zA_r(u)}.
\]

**Extremal classifications.** When \(n\le 2r+1\), the graph is complete and \(Q_{n,r}(z)=(1+z)^n-1\). When \(n\ge2r+2\), set
\[
k=\left\lceil\frac{n-r-1}{r}\right\rceil,\qquad d=n-rk.
\]
Then \(2\le d\le r+1\), the connected-domination number is \(k\), and the exact number of minimum sets is
\[
[z^k]Q_{n,r}(z)
=n\binom{k+r-d}{r+1-d}.
\]
Every minimum set has exactly one circular gap longer than \(r\). Moreover, **every** subset of cardinality at least \(n-2r+1\) is connected dominating, and for \(n\ge2r+2\) this is the sharp universal cardinality threshold.

## Assumptions and scope

Graphs are finite and simple, and domination means that vertices outside \(S\) each have a neighbor in \(S\); vertices in \(S\) dominate themselves in the ordinary closed-neighborhood sense. The induced graph \(C_n^r[S]\) must be connected. No empty set is counted. Binomial coefficients with inadmissible integer parameters are zero.

For \(S\) of size \(k\), list its selected vertices in clockwise cyclic order. Let \(g_1,\ldots,g_k\) be the positive successive clockwise distances, so \(\sum_i g_i=n\). When \(k=1\), the unique gap is \(n\). A *long* gap has \(g_i>r\), and an excessively long gap has \(g_i>2r+1\).

## Proof

**Lemma (one-long-gap characterization).** A nonempty vertex set is connected dominating if and only if (i) all its cyclic gaps satisfy \(g_i\le2r+1\) and (ii) at most one satisfies \(g_i>r\).

To prove domination, consider the unselected vertices strictly between consecutive selected endpoints of a gap of length \(g\). Their nearest selected vertices on the circular order are the endpoints. All such vertices are dominated exactly when the gap contains no vertex at distance greater than \(r\) from both endpoints, equivalently \(g\le2r+1\). This equivalence also handles a singleton selected set, whose gap has length \(n\).

For connectivity, if all but at most one gap have length at most \(r\), the selected vertices can be joined in cyclic order using edges across those short gaps, giving a connected spanning path (or a connected cycle if none is long). Conversely, if at least two gaps exceed \(r\), remove two such gap interiors and partition the selected vertices into the two nonempty circular intervals between them. Every circular arc between a selected vertex in the first interval and one in the second crosses at least one of these long gaps, and therefore has length greater than \(r\). No edge joins the intervals. Hence the induced graph is disconnected. This proves the lemma.

**Enumeration.** Every oriented, anchored connected dominating \(k\)-set corresponds to a positive \(k\)-tuple of gaps summing to \(n\), with either all entries in \(\{1,\ldots,r\}\) or exactly one entry in \(\{r+1,\ldots,2r+1\}\), the rest short. The respective numbers of tuples are
\[
[u^n]A_r(u)^k
\quad\text{and}\quad
k[u^n]B_r(u)A_r(u)^{k-1}.
\]
Counting selected starting vertices gives \(n\) anchors per tuple; each \(k\)-set has exactly \(k\) such anchors. Dividing by \(k\) proves the coefficient formula. Summing after division by \(n\) over all \(k\ge1\) gives the logarithmic identity, as a formal series since \(A_r(0)=B_r(0)=0\).

**Minimum size and multiplicity.** Assume \(n\ge2r+2\). A permitted \(k\)-tuple of gaps has total length at most
\[
(k-1)r+(2r+1)=rk+r+1.
\]
Consequently \(k\ge\lceil(n-r-1)/r\rceil\). For this least \(k\), the integer \(d=n-rk\) belongs to \(\{2,\ldots,r+1\}\); a tuple with \(k-1\) gaps of size \(r\) and one of size \(r+d\) has sum \(n\), is permitted and attains equality. Thus the stated \(k\) is the exact minimum.

Every minimum tuple has one long gap, because \(n=rk+d>rk\). Write the other \(k-1\) gaps as \(r-e_1,\ldots,r-e_{k-1}\), where \(e_i\ge0\). Their total deficit \(E=\sum e_i\) determines the long gap to be \(r+d+E\). Its upper bound gives \(E\le r+1-d\le r-1\), so each \(r-e_i\) is automatically positive. For fixed \(E\) there are \(\binom{E+k-2}{k-2}\) possibilities. Summing \(E=0,\ldots,r+1-d\) gives \(\binom{k+r-d}{r+1-d}\). Since the unique long gap canonically identifies the first selected vertex after it, each pattern yields precisely \(n\) distinct labeled sets. This proves the exact minimum multiplicity.

**Sharp saturation threshold.** A long gap contains at least \(r\) omitted vertices, while an excessively long gap contains at least \(2r+1\) omitted vertices. Therefore, if at most \(2r-1\) vertices are omitted, neither two long gaps nor a single excessively long gap can occur; the lemma makes every remaining set connected dominating. When \(n\ge2r+2\), choose two disjoint runs of \(r\) omitted vertices separated in both circular directions by at least one selected vertex. Their complement has \(n-2r\) selected vertices and two long gaps, hence is not connected dominating. The threshold cannot be reduced.

Finally, when \(n\le2r+1\), every pair of distinct cycle vertices has circular distance at most \(r\), so the graph is complete and every nonempty set qualifies.

## Verification

The accompanying `verify.py` constructs the graphs directly and independently checks domination and induced connectivity by adjacency tests and breadth-first search, without using the gap lemma. It exhaustively compares all coefficients with the closed formula for 26 noncomplete parameter pairs with \(1\le r\le4\), inspecting 74,390 nonempty subsets in total. It also compares minimum multiplicities, saturation thresholds, and the known ordinary-cycle case, and checks complete powers up to 11 vertices. These finite checks corroborate, but do not replace, the proof for all integers \(n,r\).

## Relationship to prior work

Galvin and Zhang, *The domination polynomial of powers of paths and cycles* (first posted 2024-08-22), enumerate **ordinary** dominating sets of these graph powers, without requiring the induced selected subgraph to be connected. Their results do not directly give the one-long-gap restriction or the complete connected polynomial.

Mojdeh and Emadi, *Connected domination polynomial of graphs* (2018), establish the notion and treat ordinary paths and cycles, among other families. In particular, the special case \(r=1\) of the formula above agrees with their preexisting ordinary-cycle polynomial \(z^n+nz^{n-1}+nz^{n-2}\) for \(n\ge4\). That special case is not claimed as new. Caputi, Celoria, and Collari (first posted 2022-01-03) relate connected domination polynomials to graph homology but do not evaluate these polynomials for all powers of cycles. General bounds for circulant connected-domination numbers likewise do not determine all coefficients or optimal-set multiplicities.

The intended advance is the **complete two-parameter size distribution** together with a structural criterion, exact minimum-set counts, and a sharp universal large-set threshold.

## Limitations

Only ordinary connected dominating vertex sets of cycle powers are addressed; connected *total* domination, weighted graphs and general circulant generators are not. The sources inspected and searches performed do not establish definitive worldwide publication priority; alternative formulations in older combinatorial enumerations remain a possible overlap risk. Finite computational checks are not infinite proof certificates. No independent mathematical audit has been performed.

## References

1. D. Galvin and Y. Zhang, *The domination polynomial of powers of paths and cycles*, arXiv:2408.12731, initial public submission 2024-08-22. https://arxiv.org/abs/2408.12731
2. D. A. Mojdeh and A. S. Emadi, *Connected Domination Polynomial of Graphs*, Fasciculi Mathematici 60 (2018), 103–121, DOI:10.1515/fascmath-2018-0007. https://doi.org/10.1515/fascmath-2018-0007
3. L. Caputi, D. Celoria and C. Collari, *Categorifying connected domination via graph überhomology*, arXiv:2201.00721, initial public submission 2022-01-03. https://arxiv.org/abs/2201.00721
4. Tamizh Chelvam and Mutharasu, *Bounds for domination parameters in circulant graphs* (2012), for relevant circulant domination bounds.
