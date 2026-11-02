# A sharp signed-Roman lower bound and an even-order Kneser construction

## Finding
For every integer \(n\ge12\), let \(G=K(n,2)\). Then
\[
\gamma_{sR}(G)\ge3;\qquad
\gamma_{sR}(G)=3\quad\text{if \(n\) is odd};\qquad
3\le\gamma_{sR}(G)\le4\quad\text{if \(n\) is even}.
\]
The upper bound in the odd case is previously known; the contributions here are the uniform strengthened lower bound and the weight-four even construction. The exact even value, either three or four, is not determined.

## Assumptions and scope
The vertices of \(K(n,2)\) are the two-element subsets of \([n]\); distinct vertices are adjacent exactly when disjoint. A signed Roman dominating function is \(f:V(G)\to\{-1,1,2\}\) such that (i) every closed-neighborhood sum \(\sum_{u\in N[v]}f(u)\ge1\), and (ii) every vertex labeled \(-1\) has a neighbor labeled \(2\). Its weight is \(W=\sum_{v\in V(G)}f(v)\), and \(\gamma_{sR}\) is its minimum weight. All inequalities are for integral \(n\ge12\).

## Proof
**A stronger lower bound.** Write \(f_{ij}=f(\{i,j\})\), let \(s_i=\sum_{j\ne i}f_{ij}\) and \(W=\sum_{i<j}f_{ij}\), so \(\sum_i s_i=2W\). The closed-neighborhood inequality at \(\{i,j\}\) is exactly
\[
C_{ij}=W-s_i-s_j+2f_{ij}\ge1.
\]
Indeed all edges contribute \(W\); removing the edges meeting either endpoint removes \(s_i+s_j-f_{ij}\), and the closed neighborhood restores the edge \(\{i,j\}\). Because each vertex has exactly \(\binom{n-2}{2}\) neighbors, summing the closed-neighborhood inequalities globally yields
\[
\left(1+\binom{n-2}{2}\right)W\ge\binom n2.
\]
For \(n\ge12\), the right-hand ratio is strictly greater than one, so integrality implies \(W\ge2\). Next, summing \(C_{ij}\ge1\) over all \(j\ne i\), with \(i\) fixed, gives
\[
(n-3)W-(n-4)s_i\ge n-1.
\]
If \(W=2\), this forces \(s_i\le(n-5)/(n-4)<1\). As each \(s_i\) is integral, every \(s_i\le0\), contrary to \(\sum_i s_i=2W=4\). Thus \(W\ge3\), without needing the Roman defender condition.

**Odd-order upper bound.** Suppose \(n\ge13\) is odd and partition \([n]=X\sqcup Y\), with \(|X|=a=(n-3)/2\ge5\) and \(|Y|=b=(n+3)/2\). Give every cross pair label \(-1\), every within-part pair label \(1\), and raise to \(2\) precisely the \(a\) edges of a Hamiltonian cycle within \(X\). The baseline weight is \(((b-a)^2-n)/2=(9-n)/2\), and the \(a\) upgrades give \(W=3\). Row sums are \(s_x=-2\) for \(x\in X\) and \(s_y=2\) for \(y\in Y\). Hence \(C_{ij}\ge9\) on \(X\)-pairs, \(C_{ij}=1\) on \(Y\)-pairs, and \(C_{ij}=1\) on cross pairs. For every negative cross pair, a cycle edge of \(X\) avoids its one endpoint in \(X\) because \(a\ge5\), providing a disjoint neighbor labeled \(2\). This is a valid weight-three function. This upper construction is already present in the literature [1] and is included to demonstrate exactness from the new lower bound.

**Even-order upper bound.** Suppose \(n\ge12\) is even and partition \([n]=X\sqcup Y\) with \(|X|=a=n/2-1\ge5\) and \(|Y|=b=n/2+1\ge7\). Give cross pairs label \(-1\), all within-part pairs label \(1\), then upgrade to label \(2\) the \(a\) edges of one Hamiltonian cycle in \(X\), together with three pairwise disjoint edges in \(Y\). The baseline weight is \(((b-a)^2-n)/2=2-n/2\), so the \(a+3\) upgrades produce \(W=4\). The row sums are \(s_x=-1\) for \(x\in X\); for \(y\in Y\), they are \(s_y=1+\varepsilon_y\), where \(\varepsilon_y\in\{0,1\}\) records incidence with one of the three added matching edges. Therefore \(C_{ij}\ge8\) for an \(X\)-pair, \(C_{ij}\ge2\) for a \(Y\)-pair, and for a cross pair \(\{x,y\}\) we have
\[
C_{xy}=4-(-1+s_y)+2(-1)=3-s_y\ge1.
\]
Every negative cross pair has a disjoint positively labeled cycle edge in \(X\), by \(a\ge5\). Hence the weight-four labeling satisfies both defining conditions, yielding the upper bound \(4\).

## Verification
The standalone Python file `VERIFY.py` reconstructs all vertices and disjointness edges, evaluates every closed-neighborhood inequality and every negative-vertex defender condition for \(12\le n\le20\), and directly evaluates all row-sum identities and defenders for \(21\le n\le40\). Run `python3 VERIFY.py`; successful execution prints `VERIFY_OK`. The computer checks are finite corroboration; the arguments above prove the theorem for every \(n\ge12\).

## Relationship to prior work
Zec and Grbić [1] proved \(2\le\gamma_{sR}(K(n,2))\le3\) for odd \(n\ge12\) and \(2\le\gamma_{sR}(K(n,2))\le5\) for even \(n\ge12\). Thus the previous bounds neither excluded weight two nor achieved weight four in the even case. Here the point-incidence sum rules out weight two for both parities; the odd case becomes exact, and the new even cycle-plus-matching construction lowers the previous upper bound by one. The existing weight-three odd construction is expressly not claimed as new. An unindexed equivalent proof or construction remains possible.

## Limitations
The value of \(\gamma_{sR}(K(n,2))\) for even \(n\) is not resolved beyond the interval from three to four. No statement about smaller orders, other Kneser parameters, or the complete classification of optimal functions is proved. Verification examples do not establish uniqueness or priority. A full independent mathematical audit and exhaustive historical literature review have not been performed.

## References
[1] M. Zec and D. Grbić, *Several Roman domination graph invariants on Kneser graphs*, arXiv:2204.05664v1 (publicly posted 2022-04-12); *Discrete Mathematics & Theoretical Computer Science* 25(1) (2023), DOI:10.46298/dmtcs.10506. Theorem 3, pages 6–7 in the journal PDF, gives the prior signed-Roman bounds and constructions. https://arxiv.org/abs/2204.05664 ; https://doi.org/10.46298/dmtcs.10506
