# Full star-isolation spectra and parity-rigid minimum sets on rook graphs

## Finding
Let \(m,n\ge2\) and \(\ell\ge1\) be integers, and put \(R_{m,n}=K_m\square K_n\). A set \(S\subseteq V(R_{m,n})\) is *\(\ell\)-star isolating* if the induced graph on vertices outside the closed neighborhood \(N[S]\) has no (not necessarily induced) copy of \(K_{1,\ell}\). Define the polynomial
\[
\mathcal I_{m,n,\ell}(z)=\sum_{S\text{ is }\ell\text{-star isolating}}z^{|S|}.
\]
For \(0\le a\le m\) and \(0\le b\le n\), define \(\Phi_\ell(a,b)=1\) when \(a=m\), or \(b=n\), or \(m+n-a-b\le\ell+1\); otherwise \(\Phi_\ell(a,b)=0\). Then the **complete cardinality distribution** is
\[
\boxed{\mathcal I_{m,n,\ell}(z)=\sum_{a=0}^m\sum_{b=0}^n \Phi_\ell(a,b)\binom ma\binom nb\sum_{i=0}^a\sum_{j=0}^b(-1)^{a+b-i-j}\binom ai\binom bj(1+z)^{ij}.}
\]
Assume \(m\le n\), and set
\[
t=\min\left\{m,\max\left\{0,\left\lceil\frac{m+n-\ell-1}{2}\right\rceil\right\}\right\},\qquad L=m+n-\ell-1.
\]
Then \(\iota(R_{m,n},K_{1,\ell})=t\), and every minimum set is classified as follows. If \(t=0\), the empty set is the unique optimum. If \(t=m\) and \(\ell<n-m\), the optimum sets are precisely the sets choosing one cell of each row; their number is \(n^m\). If \(t=m\) and \(\ell=n-m\), these same sets coexist with configurations using \(m-1\) rows and \(m\) columns, with one row used twice; their total number is
\[
n^m+m\binom nm(m-1)!\binom m2.
\]
In the remaining case \(1\le t<m\), the optima have precisely \((a,b)=(t,t)\), and additionally \((t,t-1)\) or \((t-1,t)\) when \(L=2t-1\). Their count is
\[
\boxed{\binom mt\binom nt t!+\mathbf1_{\{L=2t-1\}}\binom t2(t-1)!\left[\binom mt\binom n{t-1}+\binom m{t-1}\binom nt\right].}
\]
In particular an independent optimum always exists, so the independent \(\ell\)-star isolation number equals \(t\). The number of independent optima is \(\binom mt\binom nt t!\) in every regime (including \(t=0\)). In the interior regime, all optima are independent when \(L\) is even, while for odd \(L\) the only possible departure is **one repeated row or one repeated column**.

As a reconstruction consequence, the family of polynomials \(\{\mathcal I_{m,n,\ell}(z):\ell\ge1\}\) determines the unordered factor orders: any polynomial has degree \(mn\), and its constant coefficient first becomes nonzero at \(\ell=m+n-1\). These give both the product and sum of \(m,n\).

## Assumptions and scope
All graphs are finite, simple, undirected. The rook graph has vertex set \([m]\times[n]\) and two distinct cells are adjacent iff they share a row or column. A star is meant as an ordinary subgraph, not an induced subgraph. The parameter \(\ell\) is the **number of leaves** of the forbidden star, so the residual maximum-degree requirement is \(\Delta\le\ell-1\), with empty graphs allowed. Some literature indexes this invariant by \(k=\ell-1\); that convention is not adopted here. Every set of cells is labeled by its coordinates. Empty binomial sums use their usual combinatorial values, \(\binom ab=0\) outside \(0\le b\le a\), and \(0!=1\).

## Proof
**1. Exact residual structure.** For a selected set \(S\), let \(A\subseteq[m]\) be its occupied rows and \(B\subseteq[n]\) its occupied columns; write \(a=|A|\), \(b=|B|\). A vertex is dominated by \(S\) exactly if its row belongs to \(A\) or its column belongs to \(B\). Consequently the residual induced graph is *exactly* \(K_{m-a}\square K_{n-b}\), under the convention that a zero factor gives the empty graph. If both residual factors are nonzero, every residual vertex has degree \((m-a-1)+(n-b-1)=m+n-a-b-2\). Therefore there is no \(K_{1,\ell}\) subgraph exactly when \(a=m\), or \(b=n\), or \(m+n-a-b\le\ell+1\). This is \(\Phi_\ell(a,b)=1\) including \(S=\varnothing\).

**2. Exact polynomial.** Choose \(a\) occupied rows and \(b\) occupied columns in \(\binom ma\binom nb\) ways. The selected cells must form a subset of the resulting \(a\times b\) rectangle meeting each of those rows and columns. Inclusion-exclusion over omitted rows and columns gives their weighted enumerator
\[
B_{a,b}(z)=\sum_{i=0}^a\sum_{j=0}^b(-1)^{a+b-i-j}\binom ai\binom bj(1+z)^{ij}.
\]
This includes \(B_{0,0}(z)=1\) and \(B_{0,b}(z)=B_{a,0}(z)=0\) when exactly one support size is zero. Each selected set has a unique pair of occupied row and column supports. Multiplying by \(\Phi_\ell(a,b)\) and summing thus proves the polynomial with neither overcounting nor omitted configurations.

**3. Minimum cardinality.** Suppose \(m\le n\), and \(|S|=p<m\). Neither row nor column support can exhaust its factor. Since \(a\le p\) and \(b\le p\), feasibility from step 1 implies \(2p\ge a+b\ge L=m+n-\ell-1\). A set of fewer than \(m\) vertices therefore has size at least \(\max\{0,\lceil L/2\rceil\}\). Conversely, for each \(0\le p\le m\), we can select \(p\) cells in pairwise distinct rows and columns. If \(p<m\), its residual has degree \(m+n-2p-2\), and hence is feasible whenever \(2p\ge L\); if \(p=m\), its residual is empty. Choosing \(p=t\) proves the stated exact minimum, including the zero-set and complete-row-support boundary cases.

**4. Equality cases when \(1\le t<m\).** Every minimum set uses \(t\) cells, hence \(1\le a,b\le t\) and \(a+b\ge L\). By definition of \(t\) in this regime, \(L=2t\) or \(L=2t-1\). In the even case, only \((a,b)=(t,t)\) is possible; these are partial permutation matrices counted by \(\binom mt\binom nt t!\). In the odd case, additionally \((a,b)=(t,t-1)\) or its transpose is allowed. In the first additional case, the \(t\) selected cells occupy distinct rows and exactly \(t-1\) columns, so exactly one column has two of the chosen rows: after choosing supports there are \(\binom t2(t-1)!\) arrangements. The transposed case is symmetric. No other support sizes reach \(a+b\ge L\). For \(t=1\), the additional type has zero multiplicity by \(\binom12=0\).

**5. Equality cases when \(t=m\).** This requires \(\ell\le n-m\), in particular \(n>m\). Every selected set of cardinality \(m\) meeting all \(m\) rows is feasible, and exactly one cell is chosen in each row, yielding \(n^m\) sets. If \(a<m\), then \(a+b\le(m-1)+m=2m-1\). When \(\ell<n-m\), \(L\ge2m\), making such a set impossible. At \(\ell=n-m\), one has \(L=2m-1\), forcing \((a,b)=(m-1,m)\); its distinct columns have one cell each and exactly one row is used twice. Choosing its supports and double row's two columns yields \(m\binom nm\binom m2(m-1)!\), as claimed. The cases in steps 3–5 exhaust all optima.

**6. Independence and reconstruction.** A partial permutation matrix is an independent set in a rook graph, and the construction in step 3 is optimal. Such optimum sets are counted by \(\binom mt\binom nt t!\), also for \(t=m\) and \(t=0\). The strict-interior equality characterization proves the parity assertion. Finally, the all-vertex set always contributes \(z^{mn}\), so every polynomial has degree \(mn\). The empty set is star isolating exactly when the original regular graph has degree \(m+n-2<\ell\); thus the first nonzero constant term occurs at \(\ell=m+n-1\). The unordered factor orders are the integer roots of \(X^2-(m+n)X+mn\).

## Verification
A standalone standard-library program, `verify.py`, constructs each rook graph's adjacency masks independently of the support-count formula and exhaustively enumerates all subsets for all \(2\le m\le n\le4\) and all \(1\le\ell\le m+n-1\). It compares every coefficient with the inclusion-exclusion formula and checks both the minimum and the optimizer count; there are 30 parameter triples and 487472 graph-subset tests. It separately samples larger graphs by direct adjacency checks and checks the minimum formula and optimizer enumerations against exact support sums. Run `python3 verify.py`; a successful run prints `VERIFICATION_OK`. Finite checks corroborate the proof; they do not replace its universal reasoning.

## Relationship to prior work
The concept belongs to star/generalized isolation. Zhang and Wu's *k-Isolation in Graphs*, publicly posted on 2023-11-16 (SSRN 4634672, subsequently Discrete Applied Mathematics 357 (2024)), studies general upper bounds for isolation parameters; their index uses a different star-size shift. Brešar et al. (arXiv:2508.16338) study isolation in graph products and explicitly give the scalar value \(\iota(K_n\square K_n)=n-1\), which is included here at \(\ell=1\). Brešar and Rall (arXiv:2608.25752) establish general forbidden-subgraph isolation bounds in graph products. Their inspected Cartesian-product theorems do not give the complete all-size star-isolation polynomial or the parity-refined optimizer classification for \(K_m\square K_n\). These earlier scalar/general bounds are not claimed as new.

## Limitations
The theorem concerns exactly two complete-graph factors, stars forbidden as ordinary subgraphs, and integer \(m,n\ge2\), \(\ell\ge1\). It makes no claim about arbitrary Cartesian products, induced-star isolation, or higher-dimensional Hamming graphs. The 2023 Zhang–Wu full text could not be inspected here; its public abstract was compared, and potential unindexed exact enumerations remain a bibliographic risk. Finite computations do not establish the universal claim.

## References
1. G. Zhang and B. Wu, *K-Isolation in Graphs*, SSRN 4634672, public preprint 16 November 2023; journal version *Discrete Applied Mathematics* 357 (2024), 99–111, DOI: 10.1016/j.dam.2024.06.005. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4634672
2. B. Brešar, T. Dravec, D. P. Johnston, K. Kuenzel, D. F. Rall, and A. Tepeh, *Isolation number: Cartesian and lexicographic products and generalized Sierpiński graphs*, arXiv:2508.16338 (2025). https://arxiv.org/abs/2508.16338
3. B. Brešar and D. F. Rall, *On the isolation numbers in graph products*, arXiv:2608.25752 (2026). https://arxiv.org/abs/2608.25752
