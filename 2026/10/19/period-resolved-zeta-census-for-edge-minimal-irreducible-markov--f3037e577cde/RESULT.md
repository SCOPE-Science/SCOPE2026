# Period-resolved zeta census for edge-minimal irreducible Markov shifts

## Finding
For every integer \(N\ge2\), let \(\mathcal G_N\) be the irreducible directed graphs on \(N\) vertices with exactly \(N+1\) edges, permitting loops but excluding parallel edges. Consider their one-sided vertex Markov shifts. All of these shifts belong to one continuous-orbit-equivalence class: the class of the full two-shift.

The exact spectrum of Artin–Mazur zeta functions is
\[
\mathcal Z_N=\left\{\frac1{1-z^a-z^b}:1\le a\le b\le N,\ a+b\ge N+1,\ (a<b\text{ or }a=b<N)\right\}.
\]
Each listed pair gives a distinct zeta function. The corresponding graph has dynamical period \(\gcd(a,b)\).

Put \(T(m)=0\) when \(m\le1\), and \(T(m)=\frac12\sum_{k=1}^m\varphi(k)\) when \(m\ge2\), where \(\varphi\) is Euler's totient. For every positive integer \(d\), the exact number of period-\(d\) zeta functions in \(\mathcal Z_N\) is
\[
P_N(d)=T(\lfloor N/d\rfloor)+\mathbf1_{\{d<N<2d\}}.
\]
Thus there are exactly \(T(N)\) different zeta functions among mixing shifts in \(\mathcal G_N\), with
\[
T(N)=\frac12\sum_{k=1}^N\varphi(k)=\frac{3}{2\pi^2}N^2+O(N\log N).
\]
For \(N\ge3\), increasing the vertex budget from \(N-1\) to \(N\) adds exactly \(\varphi(N)/2\) new mixing zeta profiles.

## Assumptions and scope
A directed graph here may have loops but has at most one edge for each ordered vertex pair. Strong connectivity means that every ordered pair of vertices is connected by a directed path. The period of a strongly connected graph is the gcd of the lengths of all its directed cycles; period one is equivalent to primitivity (topological mixing) of its adjacency matrix. The zeta function of the one-sided vertex Markov shift is \(\zeta_A(z)=\exp(\sum_{n\ge1}\operatorname{tr}(A^n)z^n/n)\). Distinct zeta functions distinguish nonconjugate shifts; no converse assertion is made. The edge budget \(N+1\) is the smallest possible budget for a non-permutation strongly connected graph on \(N\ge2\) vertices.

## Proof
**1. Two-cycle structure.** Every vertex has positive outdegree, and the sum of all outdegrees is \(N+1\). Consequently exactly one vertex \(p\) has outdegree two and all other vertices have outdegree one. Follow each of the two outgoing edges from \(p\). Strong connectivity forces each deterministic path to return to \(p\), giving two distinct simple directed cycles with lengths \(a,b\). Every vertex is on their union: a route from \(p\) to any vertex must follow one of those branches. As indegrees also sum to \(N+1\), there is at most one merging vertex away from \(p\). Thus the two cycles share precisely one oriented path (possibly only \(p\)), comprising \(t\ge1\) shared vertices. Counting vertices gives \(N=a+b-t\), so \(a+b\ge N+1\); the individual simple cycles have \(1\le a,b\le N\). If \(a=b\), the two outgoing edges prevent the cycles from being identical, so \(t<a\), giving \(a=b<N\).

Conversely, let \(a,b\) satisfy the displayed conditions and put \(t=a+b-N\). For \(t=1\), form two oriented cycles of lengths \(a,b\) sharing one vertex. For \(t>1\), form a common directed return path of length \(t-1\) from a merging vertex to \(p\), and two internally disjoint directed paths from \(p\) to that merging vertex, of lengths \(a-t+1\) and \(b-t+1\). In the equal-length case these branch lengths are at least two; otherwise if one branch has length one the other is longer. Thus no parallel edges arise. There are exactly \(a+b-t=N\) vertices and \(N+1\) edges, and the graph is strongly connected. This realizes every pair.

**2. Zeta and period.** Every simple directed cycle of the graph is one of the two constructed cycles, and they are not vertex-disjoint. The vertex-disjoint directed-cycle expansion of the determinant therefore gives the exact polynomial identity
\[
\det(I-zA)=1-z^a-z^b.
\]
By the trace-log determinant identity, \(\zeta_A(z)=1/\det(I-zA)\). These polynomials determine their unordered exponent pair uniquely, including the case \(a=b\). The directed period is \(\gcd(a,b)\). At \(z=1\), \(\det(I-A)=-1\); hence \(\mathbb Z^N/(I-A^{\mathsf T})\mathbb Z^N=0\). The full two-shift has a two-state all-ones adjacency matrix, whose determinant at one is also \(-1\) and whose Bowen–Franks group is zero. The classification by Bowen–Franks group, distinguished unit and determinant therefore yields continuous orbit equivalence for every graph under consideration.

**3. Exact arithmetic census.** Fix \(d\ge1\), and first consider unequal lengths. Write \(a=du,\ b=dv\), with \(1\le u<v\le M=\lfloor N/d\rfloor\). Their gcd is exactly \(d\) precisely when \(\gcd(u,v)=1\). The vertex requirement \(a+b\ge N+1\) is equivalent to \(u+v\ge M+1\). Let \(T(M)\) count these coprime pairs. All coprime pairs with \(1\le u<v\le M\) number \(\sum_{v=2}^M\varphi(v)\). The excluded pairs with \(u+v\le M\) number \(\frac12\sum_{s=3}^M\varphi(s)\), by pairing \(u\) with \(s-u\) for each sum \(s\). As \(\varphi(1)=\varphi(2)=1\), subtraction yields \(T(M)=\frac12\sum_{s=1}^M\varphi(s)\) for \(M\ge2\), and zero for smaller \(M\).

Equal-length cycles have period equal to their common length. The only equal-length pair of period \(d\) is \((d,d)\), realizable exactly when \(d<N<2d\). Adding this one exceptional profile proves the period-stratified formula. For \(d=1\) the exceptional term vanishes, giving the mixing count. Finally, the classical totient summatory estimate \(\sum_{k\le N}\varphi(k)=3N^2/\pi^2+O(N\log N)\) follows by counting coprime pairs with Möbius inversion. This proves the asymptotic and the exact increment \(T(N)-T(N-1)=\varphi(N)/2\) for \(N\ge3\).

## Verification
The accompanying standalone Python 3 program `VERIFY_SPARSE.py` exhaustively checks binary adjacency patterns with \(N+1\) edges for \(N=2,3,4\), tests constructive realizations through \(N=7\) using exact determinant arithmetic, and verifies the totient and period formulas for \(2\le N\le150\). It performs 12,007 exact integer assertions. The all-\(N\) conclusions follow from the proof, not the finite checks. The verifier uses only the standard library.

## Relationship to prior work
Klech (2026, arXiv:2609.17334, Sections 4–5) already classifies the underlying \(N+1\)-edge strongly connected butterfly digraphs and computes their two-cycle entropy polynomials. The graph normal form, determinant shape and extremal entropy observations are **not** asserted to originate here. Matsumoto and Matui (2026, arXiv:2606.16283, Introduction and Sections 2–3) establish entropy flexibility inside continuous orbit equivalence classes and state the known classification by Bowen–Franks data. Their 2014 zeta-function paper relates periods through orbit cocycles. The precise period-by-period sparse zeta-function spectrum, its totient census, and their joint placement in the full two-shift continuous-orbit-equivalence class are the specific findings assessed here.

## Limitations
Only \(0\)-\(1\) adjacency matrices, exactly \(N+1\) edges, irreducible vertex Markov shifts, and ordinary Artin–Mazur zeta functions are considered. The count is of **distinct zeta functions** (which is also the number of length-pair types), not of labelled graph presentations, conjugacy classes for arbitrary matrices or all zeta functions within the entire orbit-equivalence class. Related prior butterfly enumeration makes the incremental originality of this arithmetic refinement modest; an undiscovered equivalent period census remains possible. No external independent priority verification has been conducted.

## References
1. K. Matsumoto and H. Matui, *Topological entropy in continuous orbit equivalence of one-sided topological Markov shifts*, arXiv:2606.16283v1 (first public 2026-06-15), https://arxiv.org/abs/2606.16283.
2. R. Klech, *Generating Functions and the Entropy Hierarchy of Strongly Connected Digraphs*, arXiv:2609.17334v1 (2026-09-15), https://arxiv.org/abs/2609.17334.
3. K. Matsumoto and H. Matui, *Continuous orbit equivalence of topological Markov shifts and dynamical zeta functions*, arXiv:1403.0719 (2014), https://arxiv.org/abs/1403.0719.
4. S. Kiefer and A. Ryzhikov, *The complexity of computing the period and the exponent of a digraph*, arXiv:2408.05762 (2024), https://arxiv.org/abs/2408.05762.
