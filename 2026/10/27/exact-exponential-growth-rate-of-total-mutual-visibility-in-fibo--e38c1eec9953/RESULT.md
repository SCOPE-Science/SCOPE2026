# Exact exponential growth rate of total mutual visibility in Fibonacci cubes

## Finding
For every integer \(n\ge 2\), let \(\Gamma_n\) be the graph of binary words of length \(n\) with no consecutive ones, adjacent when they differ in one coordinate. Let \(\mathcal E_n\) consist of words containing at least one one, with at most two leading zeros, at most two trailing zeros, and at most three zeros between successive ones. Put \(a_n=|\mathcal E_n|\). Then
\[
\sum_{n\ge2}a_nz^n=\frac{z(1+z+z^2)^2}{1-z^2-z^3-z^4}-z,
\qquad
\frac{a_n}{1+\binom n2}\le\mu_{\mathrm t}(\Gamma_n)\le a_n.
\]
Here \(\mu_{\mathrm t}(G)\) is the maximum cardinality of a set \(X\subseteq V(G)\) such that every two graph vertices admit a shortest path with no internal vertex in \(X\). Consequently, for the unique real \(\lambda>1\) satisfying \(\lambda^3-\lambda^2-1=0\),
\[
\lim_{n\to\infty}\bigl(\mu_{\mathrm t}(\Gamma_n)\bigr)^{1/n}=\lambda
=1.465571231876768\ldots.
\]
Moreover, the total mutual-visibility sets are **exactly** the independent vertex sets of the following explicit conflict graph \(R_n\): its vertices are \(\mathcal E_n\), and two vertices are adjacent precisely when they are opposite corners of a four-cycle of \(\Gamma_n\). In particular, the bound \(a_n\) is the exact count of vertices that can individually belong to a total mutual-visibility set, not a claim that the full set \(\mathcal E_n\) is total visible.

## Assumptions and scope
All graphs are finite, simple and undirected; graph distance uses unit-length edges. Binary coordinates are ordered along a path, and an empty initial or terminal zero-run has length zero. In the definition of \(\mathcal E_n\), consecutive ones are already forbidden by membership in \(V(\Gamma_n)\); hence every internal zero-run has length at least one. The theorem concerns every integer \(n\ge2\), with no assertion of an exact closed form for the finite value \(\mu_{\mathrm t}(\Gamma_n)\). The asymptotic statement identifies an exponential rate, not a multiplicative constant.

## Proof
**1. Distance-two local criterion.** For any connected graph \(G\) and \(X\subseteq V(G)\), total mutual visibility is equivalent to the following condition: each vertex pair \(u,v\) at distance two has a common neighbor outside \(X\). Necessity is immediate because all shortest \(u,v\)-paths have two edges. For sufficiency, take any shortest path between arbitrary vertices \(s,t\), minimizing the number of internal vertices in \(X\). If it contains \(x\in X\) between consecutive vertices \(u,v\), then \(d_G(u,v)=2\). The local condition supplies another common neighbor \(y\notin X\). Replacing the segment \(u,x,v\) by \(u,y,v\) preserves the path length, and the resulting walk is automatically a simple shortest path (a repeated vertex would permit shortening). The number of forbidden internal vertices decreases, a contradiction. This criterion is used as an elementary lemma, not asserted as a literature novelty.

**2. Local obstruction for a singleton.** The graph \(\Gamma_n\) is isometric in the binary cube: between words \(u,v\), remove all ones of \(u\) not in \(v\), then insert all ones of \(v\) not in \(u\). Every intermediate word has no consecutive ones, and exactly the Hamming-distance number of flips is used. For any two neighbors of \(w\in\Gamma_n\), obtained by flips in distinct coordinates \(i,j\), their possible common neighbors in \(\Gamma_n\) are exactly \(w\) and the double flip of \(w\), if that double flip is allowed. As each single flip is allowed, the double flip is forbidden exactly when both flips insert ones in two adjacent zero positions. Therefore \(\{w\}\) satisfies the distance-two criterion exactly when \(w\) has no pair of adjacent zeros that are both individually flippable to one.

Consider a maximal run of zeros in a word containing at least one one. In a leading run, the first two zeros are both individually flippable precisely when the run has length at least three; in a trailing run the symmetric statement uses the last two zeros. In an internal run bounded by ones, two adjacent zeros can both be flipped to one precisely when the run has length at least four. Thus singleton feasibility is equivalent to the stated zero-run restrictions. The all-zero word is forbidden when \(n\ge2\), because any adjacent coordinates are both individually flippable. Hence the individually feasible vertices are exactly \(\mathcal E_n\).

**3. Complete set characterization.** Any total mutual-visibility set \(X\) lies in \(\mathcal E_n\), by the singleton test. In an induced four-cycle, the two opposite vertices are the complete common-neighbor set of the other opposite pair (a cube has at most two common neighbors at distance two). Consequently, \(X\) cannot contain opposite corners, so it is independent in \(R_n\). Conversely, suppose \(X\subseteq\mathcal E_n\) is independent in \(R_n\). Every pair at distance two has either one or two common neighbors. If it has one, that neighbor lies outside \(\mathcal E_n\), since it fails the singleton test. If it has two, they are opposite corners of a four-cycle, so at most one belongs to \(X\). Thus every distance-two pair has an unselected common neighbor. The local criterion proves total mutual visibility. Therefore \(\mu_{\mathrm t}(\Gamma_n)=\alpha(R_n)\).

**4. Enumeration and bounds.** Every word in \(\mathcal E_n\) has \(k\ge1\) ones. Before and after them are zero-runs of lengths in \(\{0,1,2\}\); between successive ones are zero-runs in \(\{1,2,3\}\). The ordinary length enumerator is therefore
\[
\sum_{k\ge1}z^k(1+z+z^2)^2(z+z^2+z^3)^{k-1}
=\frac{z(1+z+z^2)^2}{1-z^2-z^3-z^4}.
\]
The coefficient at degree one counts the one-letter word consisting of a one. Omitting that degree gives the displayed series for \(n\ge2\). The initial values are \(a_2=2\), \(a_3=4\), \(a_4=5\), \(a_5=8\); for \(n\ge6\),
\[
a_n=a_{n-2}+a_{n-3}+a_{n-4}.
\]
Every edge of \(R_n\) joins words at Hamming distance two, so a vertex of \(R_n\) has degree at most \(\binom n2\). The greedy independent-set bound gives
\[
\alpha(R_n)\ge\frac{|V(R_n)|}{1+\binom n2}.
\]
The opposite inequality \(\alpha(R_n)\le |V(R_n)|=a_n\) is immediate.

Finally, \(1-z^2-z^3-z^4=(1+z)(1-z-z^3)\). Its smallest-modulus pole is the unique positive root \(r\in(0,1)\) of \(r+r^3=1\); the other poles have greater modulus. Hence, with \(\lambda=1/r\), the series coefficients satisfy \(a_n=C\lambda^n+O(1)\) for an explicit \(C>0\). The two bounds differ only by a factor at most quadratic in \(n\), so their \(n\)-th roots share the limit \(\lambda\). Equivalently, \(\lambda^3-\lambda^2-1=0\).

## Verification
Run `python3 verify_fibonacci_visibility.py` using Python 3.10 or newer. The program independently constructs the allowed word graph, matches the zero-run criterion to actual singleton midpoint obstructions, and tests *every* candidate subset against direct all-pairs shortest-path visibility for \(2\le n\le6\). A separate recursion enumerates independent sets of the explicit conflict graph component by component for \(2\le n\le14\), cross-checks conflict edges from two different constructions, and checks the zero-run recurrence. It terminates with `VERIFICATION_OK`. The small-order finite maxima are auxiliary checks, not the basis of the all-dimension proof or a separate priority claim. The infinite asymptotic conclusion follows from the proven formulas and greedy bound, not from finite computation.

## Relationship to prior work
Bujtás, Klavžar and Tian [1, Theorem 6] characterize total mutual-visibility sets of full Hamming graphs by excluding selected pairs at distance two. Fibonacci cubes are induced isometric subgraphs, not Hamming graphs; their missing square corners create *singleton* obstructions absent from [1]. The present theorem's forbidden-zero-run classification, explicit conflict graph and exponential base are not implied by [1]. Cicerone et al. [2] develop visibility problems in hypercube-like networks; the journal extension [3] treats ordinary mutual visibility in Fibonacci cubes and explicitly leaves their total mutual visibility as open. A publicly available abstract for forthcoming work by Podrug and collaborators [4] announces bounds and small-dimensional values for exactly this graph family, but does not give formulas or a growth rate. There is a real priority risk of overlap with its unavailable mathematical details; no disjointness from that work is claimed.

## Limitations
The bounds are only polynomially tight, not constant-factor tight; no explicit formula for \(\mu_{\mathrm t}(\Gamma_n)\) at arbitrary \(n\) is obtained. The full text of the forthcoming work [4] was unavailable for an implication comparison; the abstract could conceal an equivalent or stronger rate theorem. The open-access publisher PDF for [3] could not be retrieved in the consulted interface; the comparison there uses accessible article sections and conclusions. Enumeration through \(n=14\) is a finite cross-check, not an infinite certificate.

## References
[1] C. Bujtás, S. Klavžar, J. Tian, *Total mutual-visibility in Hamming graphs*, arXiv:2307.05168, first posted 2023-07-11, Theorem 6, https://arxiv.org/abs/2307.05168.

[2] S. Cicerone, A. Di Fonso, G. Di Stefano, A. Navarra, F. Piselli, *Mutual visibility in hypercube-like graphs*, arXiv:2308.14443v1, first posted 2023-08-28, https://arxiv.org/abs/2308.14443.

[3] The same authors, *Mutual and total mutual visibility in hypercube-like graphs*, *Applied Mathematics and Computation* 491 (2025), 129216, DOI:10.1016/j.amc.2024.129216 (Fibonacci-cube discussion and conclusion).

[4] L. Podrug, with C. Bujtás, S. Klavžar and E. Tan, *Total mutual visibility in Fibonacci cubes*, KolKom 2026 contributed-talk abstract, https://kolkom26.zib.de/ (announcement for 2026-11-13, not a fully available research paper).
