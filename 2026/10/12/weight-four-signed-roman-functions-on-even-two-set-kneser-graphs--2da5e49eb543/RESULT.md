# Weight-four signed Roman functions on even two-set Kneser graphs
## Finding
**Theorem.** Let \(n=2a+2\), with \(a\ge4\), and let \(K(n,2)\) be the Kneser graph on all two-element subsets of a ground set of size \(n\), with adjacency given by disjointness. Then
\[
\gamma_{sR}(K(n,2))\le4.
\]
Indeed, for any partition of the ground set into \(A\) and \(B\) with
\[
|A|=a,\qquad |B|=a+2,
\]
choose a spanning cycle \(C\) on \(A\) and a three-edge matching \(M\) on \(B\). The following explicit labeling has signed Roman weight exactly \(4\):
\[
f(\{i,j\})=\begin{cases}
-1,&i\in A,\ j\in B\text{ or conversely},\\
2,&\{i,j\}\in E(C)\cup M,\\
1,&\text{otherwise}.
\end{cases}
\]

Moreover, within the natural class of **two-block signings** for such a partition—those labeling every crossing two-set \(-1\), and every two-set internal to either block by \(1\) or \(2\)—the minimum signed Roman weight is exactly \(4\). This latter sharpness is relative to that class, not a lower bound for unrestricted functions.

## Assumptions and scope
All graphs are finite, simple, and undirected. A signed Roman dominating function is a labeling \(f:V(X)\to\{-1,1,2\}\) such that
\[
\sum_{u\in N_X[v]} f(u)\ge1\quad\text{for all }v\in V(X),
\]
and every vertex labeled \(-1\) is adjacent to a vertex labeled \(2\). Its weight is \(\omega(f)=\sum_{v\in V(X)}f(v)\), and \(\gamma_{sR}(X)\) is the minimum possible weight.

The vertices of \(K(n,2)\) are pairs \(\{i,j\}\). The scope is exactly even \(n\ge10\), with adjacency for disjoint pairs. No exact unrestricted minimum is asserted beyond the already published small-order case.

## Proof
Fix \(n=2a+2\) and the construction. There are \(\binom a2+\binom{a+2}2\) internal two-sets and \(a(a+2)\) crossing two-sets. Begin with label \(1\) on every internal two-set and label \(-1\) on every crossing one. Its weight is
\[
\binom a2+\binom{a+2}2-a(a+2)=1-a.
\]
The cycle on \(A\) uses \(a\) edges, and the matching on \(B\) uses three. Changing their labels from \(1\) to \(2\) raises weight by \(a+3\). Therefore
\[
W=\omega(f)=(1-a)+(a+3)=4.
\]

For a ground-set point \(i\), let \(s_i=\sum_{j\ne i}f(\{i,j\})\) be the sum of labels on pairs containing \(i\). Every point in \(A\) has degree two in the selected cycle, so
\[
s_i=(a-1)-(a+2)+2=-1\quad(i\in A).
\]
For \(j\in B\), write \(\varepsilon_j\in\{0,1\}\) according to whether \(j\) belongs to the matching. Then
\[
s_j=(a+1)-a+\varepsilon_j=1+\varepsilon_j\quad(j\in B).
\]

The vertices of \(K(n,2)\) adjacent to \(\{i,j\}\) are precisely the two-sets disjoint from \(\{i,j\}\). Inclusion-exclusion at the two ground-set points gives the exact closed-neighborhood identity
\[
\sum_{h\in N_{K(n,2)}[\{i,j\}]}f(h)=W-s_i-s_j+2f(\{i,j\}).\tag{1}
\]
If \(i\in A\) and \(j\in B\), then \(f(\{i,j\})=-1\) and (1) equals \(2-\varepsilon_j\), which is either \(1\) or \(2\). If both endpoints lie in \(A\), (1) is \(6+2f(\{i,j\})\), hence at least \(8\). If both lie in \(B\) and their pair has label \(1\), (1) is \(4-\varepsilon_i-\varepsilon_j\ge2\); when their pair has label \(2\), it is a matching edge, so \(\varepsilon_i=\varepsilon_j=1\) and (1) equals \(4\). Thus every closed-neighborhood sum is at least \(1\).

Only crossing two-sets receive label \(-1\). For a crossing pair \(\{i,j\}\), with \(i\in A\) and \(j\in B\), the cycle \(C\) has exactly \(a-2\) edges avoiding \(i\). Each is disjoint from \(\{i,j\}\) and carries label \(2\). Since \(a\ge4\), this supplies at least two defenders. Therefore the negative-label condition also holds, proving that \(f\) is signed Roman and \(\gamma_{sR}(K(n,2))\le4\).

It remains to prove the asserted sharpness **within the two-block signing class**. Let an arbitrary such labeling have weight \(w\), and write \(H_A,H_B\) for the graphs consisting of internal pairs receiving label \(2\). If \(d_A(i),d_B(j)\) are their degrees, the base-weight calculation gives
\[
|E(H_A)|+|E(H_B)|=a-1+w.\tag{2}
\]
For each crossing pair, the closed-neighborhood identity (1) becomes
\[
w-d_A(i)-d_B(j)\ge1.\tag{3}
\]
Let \(p=\Delta(H_A)\) and \(q=\Delta(H_B)\). Since (3) holds for all crossing pairs, \(p+q\le w-1\). If \(w\le0\), this is already impossible. For \(1\le w\le3\), the degree sums imply
\[
a-1+w\le\left\lfloor\frac{ap}{2}\right\rfloor+
\left\lfloor\frac{(a+2)q}{2}\right\rfloor.\tag{4}
\]
For \(w=1\), (3) requires \(p=q=0\), contradicting (2). For \(w=2\), at most one of \(p,q\) is \(1\), so the right side of (4) is at most \(\lfloor(a+2)/2\rfloor<a+1\), again contradicting (2).

For \(w=3\), (3) gives \(p+q\le2\). The possibilities \((p,q)=(2,0)\) or \((1,1)\) give at most \(a\) or \(a+1\) selected internal edges, respectively, whereas (2) requires \(a+2\). All smaller degree pairs also fail. The sole numerical possibility is \((p,q)=(0,2)\), with \(H_A\) empty and \(H_B\) two-regular spanning on \(B\). But \(|B|=a+2\ge6\), so it has a pair \(\{i,j\}\subset B\) which is not an edge of \(H_B\). Both endpoints have degree \(2\), so \(s_i=s_j=3\) and this pair has label \(1\). Equation (1) gives its closed-neighborhood sum as \(3-3-3+2=-1\), a contradiction. Thus no two-block signed Roman function has weight at most \(3\), and the constructed weight \(4\) is optimal within the class.

## Verification
The standalone `verify.py` builds the labeled Kneser graph implicitly, checks the signed Roman conditions directly using disjointness, and independently checks the exact identity (1) from endpoint-incidence sums. It tests both methods for every even \(n\) from \(10\) through \(30\), and the incidence identity for every even \(n\) from \(10\) through \(100\). For each tested order it also checks the degree-capacity alternatives underlying the restricted lower bound. All tests pass; the arbitrary-order result is supplied by the proof, not by finite sampling.

## Relationship to prior work
Zec and Grbić introduced the direct Kneser-graph setting for this invariant in a paper first made public on 12 April 2022. Their 2023 published version, Theorem 3, proves \(2\le\gamma_{sR}(K(n,2))\le5\) for even \(n\ge12\), while Remark 3 records the exact value \(4\) for \(n=10\) and \(5\) for \(n=8\). The present construction extends the weight-four phenomenon from that isolated small-order example to **every even order at least ten**, tightening the published general upper bound by one. Its cycle-plus-matching mechanism yields equality within the original bipartition-signing framework and makes the improvement uniform.

The 2025 review *Varieties of Roman domination IV* restates the even-order upper bound \(5\) in Section 2.1. The review's indexed theorem text was available, but the complete publisher page was inaccessible; this is not relied on to claim that all later literature has been exhausted. Results for complete multipartite graphs and other Roman domination variants do not imply a statement about disjointness adjacency among two-element subsets.

## Limitations
This result is an **upper bound**, not a determination of the unrestricted signed Roman domination number for every even \(n\ge12\). Sharpness is proved only for the explicitly defined two-block class of labelings. The previous general lower bound \(2\) remains, leaving the unrestricted values \(2\), \(3\), and \(4\) unresolved for sufficiently large even orders. No analogous statement is claimed for odd orders or for larger Kneser subset size.

## References
1. T. Zec and M. Grbić, *Several Roman domination graph invariants on Kneser graphs*, arXiv:2204.05664 (v1: 12 April 2022); *Discrete Mathematics & Theoretical Computer Science* 25:1 (2023), paper 14, DOI: 10.46298/dmtcs.10506.
2. M. Chellali, N. Jafari Rad, S. M. Sheikholeslami, and L. Volkmann, *Varieties of Roman domination IV*, *AKCE International Journal of Graphs and Combinatorics*, published online 31 December 2025, DOI: 10.1080/09728600.2025.2598772.
