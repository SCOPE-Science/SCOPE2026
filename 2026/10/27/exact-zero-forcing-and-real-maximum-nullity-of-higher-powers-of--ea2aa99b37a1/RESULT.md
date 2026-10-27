# Exact zero forcing and real maximum nullity of higher powers of uniform spiders

## Finding
For each integer \(m\ge3\), \(r\ge4\), and \(\ell\ge r+1\), define the uniform spider \(S_m(\ell)\) by identifying one endpoint of each of \(m\) disjoint length-\(\ell\) paths as a single centre. Its ordinary \(r\)-th power \(H=S_m(\ell)^r\) connects distinct vertices whose original graph distance is at most \(r\). Then
\[
Z(H)=M_{\mathbb R}(H)=(m-1)r,
\qquad
\operatorname{mr}_{\mathbb R}(H)=m(\ell-r)+r+1.
\]
Here \(Z\) is the standard zero forcing number, \(M_{\mathbb R}\) the maximum nullity of a real symmetric matrix whose nonzero off-diagonal entries correspond **exactly** to edges of \(H\), and \(\operatorname{mr}_{\mathbb R}\) its minimum rank. This settles the higher-power portion of Conjecture 10 of Abiad, Flagg, Ghasemi Nezhad, and Zeijlemaker [1].

## Assumptions and scope
All graphs are finite, simple and undirected. Write the spider centre as \(c\) and the depth-\(s\) vertex on arm \(i\) as \(v_{i,s}\), where \(1\le i\le m\) and \(1\le s\le\ell\). The vertex count is \(m\ell+1\). Distances within one arm are \(|s-t|\); between different arms they are \(s+t\); from the centre to depth \(s\) they are \(s\). A black vertex with exactly one white neighbour may force that neighbour black. The theorem is stated for \(r\ge4\) to isolate the previously unsettled parameter range; the proof itself is valid for \(r\ge1\) whenever \(\ell\ge r+1\).

## Proof
**Upper bound by an explicit forcing order.** Initially colour black the outermost \(r\) vertices of arms \(1,\ldots,m-1\). There are \((m-1)r\) such vertices. For each of these arms in succession and for \(t=\ell-r,\ell-r-1,\ldots,1\), force \(v_{i,t+r}\to v_{i,t}\). At each step the forcing vertex is farther than \(r\) from the centre, hence is adjacent to no other arm or the centre, and its only white neighbour on its arm is \(v_{i,t}\). Thus the first \(m-1\) arms become black. Next the legal forces are
\[
v_{1,r}\to c,\qquad
v_{1,r-j}\to v_{m,j}\ (1\le j\le r-1),\qquad
c\to v_{m,r},\qquad
v_{m,t-r}\to v_{m,t}\ (r+1\le t\le\ell).
\]
For the middle sequence, the only white cross-arm neighbour of \(v_{1,r-j}\) is \(v_{m,j}\), because earlier vertices of that last arm are already black and all other arms are black. The centre then has \(v_{m,r}\) as its only white neighbour. In the final sequence, each forcing vertex sees no white neighbour in the last arm other than the next depth-\(t\) vertex, while all other arms and the centre are black. Hence \(Z(H)\le(m-1)r\).

**Lower bound by an exactly supported low-rank matrix.** Put \(d=\ell-r\ge1\). Define the real \(\ell\times d\) matrix
\[
P_{s,t}=\mathbf1_{\{t\le s\le t+r\}},\qquad
1\le s\le\ell,\quad 1\le t\le d,
\]
and set \(C=PP^\top\). Every position lies in some window, and two positions share a window precisely when their distance is at most \(r\); therefore
\[
C_{s,t}>0\quad\Longleftrightarrow\quad |s-t|\le r.
\]
The first \(d\) rows of \(P\) form a lower-triangular matrix with diagonal entries one, so \(\operatorname{rank}P=d\) and \(\dim\ker(P^\top)=r\). Also \(\ker C=\ker(P^\top)\) because \(C\) is a Gram matrix.

Let \(B\) be the symmetric \(\ell\times\ell\) matrix \(B_{s,t}=\mathbf1_{\{s+t\le r\}}\) and let \(h_s=\mathbf1_{\{s\le r\}}\). Form a symmetric matrix \(A\) indexed by the centre followed by the \(m\) arms, with centre diagonal entry zero, identical centre-to-arm blocks \(h^\top\), every arm diagonal block \(C+B\), and every cross-arm block \(B\). All specified off-diagonal entries are nonnegative. The centre-to-arm positions are nonzero exactly at distances at most \(r\); the cross-arm block at depths \(s,t\) is nonzero exactly when \(s+t\le r\); and the within-arm block off the diagonal is nonzero exactly when \(|s-t|\le r\). Thus \(A\) has precisely the required off-diagonal support: \(A\in\mathcal S_{\mathbb R}(H)\).

Choose vectors \(x_1,\ldots,x_m\in\ker(P^\top)\) satisfying \(\sum_i x_i=0\), and put \(x=(0,x_1,\ldots,x_m)\). The centre coordinate of \(Ax\) is \(h^\top\sum_i x_i=0\). The block for arm \(i\) is
\[
Cx_i+B\sum_jx_j=0.
\]
Such vectors form a space of dimension \((m-1)r\): the first \(m-1\) vectors can be chosen independently in an \(r\)-dimensional space and the last is their negative sum. Therefore \(\dim\ker A\ge(m-1)r\), so \(M_{\mathbb R}(H)\ge(m-1)r\).

For every graph, \(M_{\mathbb R}(G)\le Z(G)\). Indeed, if a kernel vector vanishes at the initial black vertices, each legal force propagates that zero via its forcing vertex's matrix row, since the unique white-neighbour coefficient is nonzero. Therefore restriction of the kernel to the initial black coordinates is injective, proving the inequality. Combining both bounds gives
\[
(m-1)r\le M_{\mathbb R}(H)\le Z(H)\le(m-1)r.
\]
Since \(|V(H)|=m\ell+1\), the minimum-rank formula follows.

## Verification
Run `python3 verify.py` in a standard Python installation. The independent test code constructs the graph from the distance definition, confirms exact symmetric-matrix support, constructs and checks explicit branch-difference kernel vectors, checks full rank modulo two primes, simulates the stated initial forcing set, and independently brute-forces smaller forcing subsets for selected finite cases. It verified 83 exact witness/support/rank/forcing instances, including 47 with \(r\ge4\), and performed 30 exhaustive small-instance zero-forcing checks. These finite tests supplement but do not replace the all-parameter proof above.

## Relationship to prior work
Abiad, Flagg, Ghasemi Nezhad, and Zeijlemaker [1] prove the matching upper bound in their Proposition 9 and pose equality as Conjecture 10, with computational evidence for low powers. The new result supplies an explicit nullity witness for **every higher power** \(r\ge4\), thereby proving the previously missing lower bound. Their results for path and cycle powers do not cover genuine spiders with \(m\ge3\). Earlier work on real minimum rank covers ordinary powers of paths and, for general trees, their squares or strict powers [2,3]; strict graph powers use a different adjacency relation. The isolated cube case has also been established separately, but its fixed-degree polynomial certificate does not imply the arbitrary-power result. No part of those known lower-power results is claimed as new here. The witness method extends uniformly across the entire previously open higher-power range.

## Limitations
The theorem treats equal-length arms, at least three arms, and powers with \(4\le r\le\ell-1\). It does not determine the value for arbitrary unequal-leg trees or for powers beyond this range. The constructed matrix is real symmetric but not asserted positive semidefinite. A correct self-contained proof is given; independent mathematical review and exhaustive historical-priority assessment have not been performed.

## References
[1] A. Abiad, M. Flagg, S. Ghasemi Nezhad, and S. Zeijlemaker, *The Zero Forcing Number of Graph Powers*, arXiv:2610.03892v1 (first submitted 2 October 2026), Proposition 9 and Conjecture 10. https://arxiv.org/html/2610.03892v1

[2] G. J. Chang and J. C.-H. Lin, *Minimum Rank of Powers of Cycles and Trees*, particularly Theorem 4.1 on squares of trees. https://www-math.nsysu.edu.tw/~chlin/Publications/Articles/GJpower.pdf

[3] L. M. DeAlba, J. Grout, I.-J. Kim, S. Kirkland, J. J. McDonald, and A. Yielding, *Minimum Rank of Powers of Trees*, Electronic Journal of Linear Algebra **23** (2012), 151–163. https://doi.org/10.13001/1081-3810.1511

[4] AIM Minimum Rank--Special Graphs Work Group, *Zero forcing sets and the minimum rank of graphs*, Linear Algebra and its Applications **428** (2008), 1628–1648.
