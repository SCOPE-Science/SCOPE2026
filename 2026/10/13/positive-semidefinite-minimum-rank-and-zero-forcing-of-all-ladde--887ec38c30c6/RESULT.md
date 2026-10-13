# Positive semidefinite minimum rank and zero forcing of all ladder powers
## Finding
Let \(L_\ell=P_2\square P_\ell\) be the Cartesian-product ladder on two rails and \(\ell\) columns. Let \(G=L_\ell^k\) be its ordinary \(k\)-th graph power, joining distinct vertices at ladder distance at most \(k\). For every pair of integers \(k\ge1\) and \(\ell\ge k+1\),
\[
Z(G)=Z_+(G)=M(G)=M_+(G)=2k,\qquad
\operatorname{mr}_{\mathbb R}(G)=\operatorname{mr}_+(G)=2(\ell-k).
\]
Here \(Z\) and \(Z_+\) denote ordinary and positive semidefinite zero forcing numbers; \(M\) and \(M_+\) are maximum nullities for, respectively, arbitrary real symmetric and real positive semidefinite matrices having precisely the graph edges as nonzero off-diagonal entries. Their corresponding minimum ranks are \(\operatorname{mr}_{\mathbb R}\) and \(\operatorname{mr}_+\). In particular, the two-row case of the grid-power zero-forcing conjecture is valid for **every** permitted length and power, and admits a positive semidefinite rank certificate.

## Assumptions and scope
All graphs are finite, undirected, and simple. Vertices of the base ladder are \((a,t)\) with rail \(a\in\{1,2\}\) and column \(1\le t\le\ell\), with graph distance
\[
\operatorname{dist}_{L_\ell}((a,t),(b,s))=|a-b|+|t-s|.
\]
For a graph \(H\), write \(\mathcal S(H)\) for symmetric real matrices whose off-diagonal nonzero pattern is exactly \(E(H)\), with unrestricted diagonal. Set \(\mathcal S_+(H)=\{A\in\mathcal S(H):A\succeq0\}\). Maximal nullity and minimal rank are the corresponding extrema over these two matrix classes. The ordinary zero forcing rule colors a white vertex if it is the unique white neighbor of an already black vertex. The positive semidefinite zero forcing rule allows the uniqueness test within each white connected component. The standard inequalities are
\[
M_+(H)\le Z_+(H)\le Z(H),\qquad M(H)\le Z(H),\qquad M_+(H)\le M(H).
\]
The claim concerns \(k\ge1\) and \(\ell\ge k+1\); it neither asserts the same expression outside that range nor resolves the higher-width grid conjecture.

## Proof
**Upper forcing bound.** Start with all vertices in the first \(k\) columns black. There are \(2k\) of them. Suppose the first \(t\) columns are black, where \(k\le t<\ell\). For each rail \(a\), the black vertex \((a,t-k+1)\) has exactly one white neighbor in \(L_\ell^k\), namely \((a,t+1)\). Indeed, every still-white vertex is in a column at least \(t+1\); its ladder distance from \((a,t-k+1)\) is at least \(k\), and equality is possible only in the same rail, in column \(t+1\). After making both forces, the first \(t+1\) columns are black. Iteration yields \(Z(G)\le2k\).

**A positive semidefinite matrix with nullity \(2k\).** Put \(h=\ell-k\). Introduce two-dimensional integer vectors \(u_j,v_j\) for offsets \(0\le j\le k\):
\[
 u_0=(1,0),\quad u_k=(1,1),\quad
 v_0=(1,-1),\quad v_k=(0,1),
\]
with, for every interior offset \(1\le j\le k-1\),
\[
 u_j=(1,3),\qquad v_j=(3,7).
\]
When \(k=1\), there are no interior offsets. For every window starting at \(r\in\{1,\ldots,h\}\), take a separate copy of \(\mathbb R^2\). Form a real \(2h\)-by-\(2\ell\) matrix \(X\) whose column for \((1,t)\) has the vector \(u_{t-r}\) in window \(r\) if \(0\le t-r\le k\), and zero otherwise. Likewise the column for \((2,t)\) has \(v_{t-r}\) in that window if \(0\le t-r\le k\), and zero otherwise. Define \(A=X^{\mathsf T}X\). This matrix is real positive semidefinite.

We verify **exactly**, not just as a contained support, that \(A\in\mathcal S_+(G)\). Two columns at separation greater than \(k\) have disjoint window supports, giving zero inner product. If their columns differ by exactly \(k\), the one common window contributes \(u_0\cdot u_k=1\) on rail 1, \(v_0\cdot v_k=-1\) on rail 2, or \(u_0\cdot v_k=u_k\cdot v_0=0\) across rails. This is precisely correct because vertices on different rails at column gap \(k\) have ladder distance \(k+1\), while same-rail vertices are adjacent in \(G\).

For column gap less than \(k\), all pairs on the first rail have strictly positive window contributions: every inner product of two \(u\)-vectors is positive. On rail 2, the possible contributions at distinct offsets are \(-4\) (\(v_0\cdot v_j\) for interior \(j\)), \(7\) (\(v_j\cdot v_k\)), and \(58\) (two interior offsets); the only other nonzero gap case is \(-1\) at gap \(k\). At a fixed nonzero gap less than \(k\), there is at most one \(-4\) term and at most one \(7\) term, with the remaining terms equal to \(58\); every nonempty such sum is nonzero. In particular, no cancellations create a spurious zero near the strip ends.

For opposite rails in the *same* column, corresponding-offset products are \(u_0\cdot v_0=1\), \(u_k\cdot v_k=1\), and \(u_j\cdot v_j=24\) for interior \(j\), so the total is positive. When the first-rail column is *earlier* than the second-rail column, contributions at gaps less than \(k\) are among \(3\), \(24\), and the zero endpoint contribution \(u_0\cdot v_k=0\). The latter occurs only at gap exactly \(k\), hence the sum at smaller gap is positive. When the first-rail column is *later*, contributions at smaller gaps are among \(-2\), \(10\), and \(24\), with at most one \(-2\), while the zero endpoint contribution \(u_k\cdot v_0=0\) occurs only at gap \(k\). A nonempty sum cannot vanish. Since every pair of column positions at gap at most \(k\) shares at least one window, these cases prove the exact edge pattern, including all boundary columns.

Finally, \(X\) has rank exactly \(2h\). Restrict it to both rail columns in each of the first \(h\) positions, ordered by column and then rail. Its window blocks form an upper-triangular matrix with identical diagonal blocks having columns \(u_0\) and \(v_0\):
\[
\begin{pmatrix}1&1\\0&-1\end{pmatrix}.
\]
Each block has determinant \(-1\), so the \(2h\)-by-\(2h\) minor has nonzero determinant. Thus \(\operatorname{rank}(X)=2h\), and since \(A=X^{\mathsf T}X\),
\[
\operatorname{rank}(A)=2h=2(\ell-k),\qquad
\operatorname{null}(A)=2\ell-2h=2k.
\]
Therefore \(M_+(G)\ge2k\). The universal inequalities above, together with \(Z(G)\le2k\), force \(Z(G)=Z_+(G)=M(G)=M_+(G)=2k\), and the two rank identities follow by subtracting from the \(2\ell\) vertices. This argument proves the result for all permitted parameters, not merely the tested instances.

## Verification
The self-contained Python 3 verifier `verify.py` generates each original ladder by its rail and rung edges, independently obtains its graph powers by breadth-first search, constructs the integer factor \(X\), compares every pair's Gram inner product with the independently computed graph adjacency, and checks an invertible full-row-rank minor over a prime field. It separately executes the first-\(k\)-columns forcing strategy and, for small graphs, exhausts every smaller initial set to independently recover the ordinary zero forcing minimum. Running `python3 verify.py` gave `ALL CHECKS PASSED`; the exact console output is included as `verification_output.txt`. The 130 tested factor-and-forcing profiles and 12 additional exhaustive-minimum profiles are finite corroboration of the universally quantified proof, not substitutes for it. Python's standard library is the only dependency.

## Relationship to prior work
Abiad, Flagg, Ghasemi Nezhad, and Zeijlemaker (arXiv:2610.03892v1, first public October 2, 2026) establish \(Z((P_b\square P_\ell)^k)\le bk\) in their Proposition 11 and pose equality as Conjecture 12; they report computational equality in a restricted small grid range. Their work supplies the conceptual question and the upper bound, neither of which implies a lower bound for the infinite ladder-power family. The theorem above establishes the two-row case uniformly and additionally exhibits a positive semidefinite matrix attaining that bound. Earlier work on minimum rank of powers of **trees** and on maximum nullity of **circulant graphs** does not directly cover powers of finite Cartesian ladders, which have four degree-two corners and are generally nonregular. Standard zero forcing/nullity inequalities are used as established tools, not claimed as new.

## Limitations
No claim is made for grids of width three or higher, for parameter combinations outside \(\ell\ge k+1\), for arbitrary graph products, or for distinct minimum zero forcing sets. The proof does not establish a full classification of minimum-rank matrices. The originality comparison covers the full initiating source and accessible related mathematical literature; undiscovered equivalent literature remains possible. Independent external validation has not been performed.

## References
1. A. Abiad, M. Flagg, S. Ghasemi Nezhad, and S. Zeijlemaker, *The Zero Forcing Number of Graph Powers*, arXiv:2610.03892v1 (first public 2026-10-02), Section 3, Proposition 11 and Conjecture 12. https://arxiv.org/html/2610.03892v1
2. AIM Minimum Rank—Special Graphs Work Group, *Zero forcing sets and the minimum rank of graphs*, Linear Algebra and its Applications 428 (2008), 1628–1648. Classical nullity bound \(M\le Z\).
3. F. Barioli et al., *Zero forcing parameters and minimum rank problems*, Linear Algebra and its Applications 433 (2010), 401–411, arXiv:1003.2028, DOI:10.1016/j.laa.2010.03.008. Introduces positive semidefinite zero forcing and its nullity bound.
4. L. DeAlba et al., *Minimum rank of powers of trees*, Electronic Journal of Linear Algebra 23 (2012), DOI:10.13001/1081-3810.1511.
5. L. Duong, B. K. Kroschel, M. Riddell, K. N. Vander Meulen, and A. Van Tuyl, *Maximum nullity and zero forcing of circulant graphs*, Special Matrices 8 (2020), 221–234, arXiv:1906.03079, DOI:10.1515/spma-2020-0106.
