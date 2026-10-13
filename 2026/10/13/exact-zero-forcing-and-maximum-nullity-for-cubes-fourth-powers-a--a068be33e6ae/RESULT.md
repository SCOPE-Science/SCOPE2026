# Exact zero forcing and maximum nullity for cubes, fourth powers, and long-arm powers of equal-leg spiders

## Finding

Let \(S_m(\ell)\) be the tree formed by attaching \(m\) vertex-disjoint paths of \(\ell\) vertices each to one common new center (one edge from the center to the first vertex of each path). Let \(G^k\) join distinct vertices of \(G\) when their distance in \(G\) is at most \(k\). Let \(Z(G)\) be the standard zero forcing number, and let \(M(G)\) be the maximum nullity of a real symmetric matrix whose *exact off-diagonal nonzero pattern* is the edge set of \(G\), without restrictions on the diagonal.

**Theorem.** For all integers \(m\ge3\), \(k\ge3\), and \(\ell\ge k+1\), assume that either \(k=3\), or \(k=4\), or \(\ell\ge2k-1\). Then

\[
\boxed{Z(S_m(\ell)^k)=M(S_m(\ell)^k)=k(m-1).}
\]

Consequently, the real symmetric minimum rank of \(S_m(\ell)^k\) is \(1+m\ell-k(m-1)\). In particular, the conjectured sharp spider bound is proved for every cubic and fourth graph power in its allowed arm-length range, and for every higher power when the arms have length at least \(2k-1\). The cases \(k\ge5\) and \(k+1\le\ell\le2k-2\) are not settled here.

## Assumptions and scope

All graphs are finite, undirected, and simple. Index the center by \(c\), and index leg \(i\) by vertices \(v_{i,t}\), for \(1\le i\le m\) and \(1\le t\le\ell\), with edges \(cv_{i,1}\) and \(v_{i,t}v_{i,t+1}\). Fix the adjacency matrix \(A=A(S_m(\ell))\). For a real symmetric matrix, nullity refers to its real kernel dimension. A zero forcing move turns a white vertex black if it is the *only* white neighbor of some black vertex in the current graph. The inequalities \(M(H)\le Z(H)\) and the spider upper bound \(Z(S_m(\ell)^k)\le k(m-1)\) are established prior results; the new lower-bound construction is explicit below.

## Proof

**1. A common kernel of dimension \(k(m-1)\).** The adjacency eigenvalues of the \(\ell\)-vertex path are the distinct real numbers

\[
\lambda_j=2\cos\left(\frac{j\pi}{\ell+1}\right),\qquad1\le j\le\ell.
\]

For every \(j\), the path vector \(u_j(t)=\sin(j\pi t/(\ell+1))\), indexed by \(1\le t\le\ell\), satisfies the path adjacency equation with eigenvalue \(\lambda_j\), including zero boundary values at positions \(0\) and \(\ell+1\). On the spider, take value zero at \(c\), and take \(a_i u_j(t)\) at vertex \(v_{i,t}\), where \(\sum_{i=1}^{m}a_i=0\). At the center the eigenvalue equation holds because the first-vertex contributions sum to zero; elsewhere it is the path equation. This produces \(m-1\) independent eigenvectors of \(A\) with eigenvalue \(\lambda_j\).

Define the monic degree-\(k\) polynomial

\[
p(x)=\prod_{j=1}^{k}(x-\lambda_j),\qquad B=p(A).
\]

Since \(\ell\ge k+1\), all chosen eigenvalues exist and are distinct. The \(k\) eigenspaces constructed above are mutually independent, and each lies in the kernel of \(B\); hence \(\operatorname{null}(B)\ge k(m-1)\). The matrix \(B\) is symmetric. Since its polynomial degree is \(k\), every off-diagonal entry corresponding to a tree distance greater than \(k\) is zero, while at distance exactly \(k\) it equals \((A^k)_{uv}=1\). We now establish that entries at **every shorter positive distance are nonzero**, which is the essential additional step needed to make \(B\) a matrix for the *exact* power graph.

**2. The long-arm range \(\ell\ge2k-1\).** In this range \(\lambda_1,\ldots,\lambda_{k-1}>0\) and \(\lambda_k\ge0\). Let \(e_s\) denote the elementary symmetric polynomial of degree \(s\) in these \(k\) roots, with \(e_0=1\). Then \(e_s>0\) for every \(0\le s\le k-1\), even when the final root vanishes. Expand

\[
p(x)=\sum_{r=0}^{k}(-1)^{k-r}e_{k-r}x^r.
\]

Fix distinct vertices \(u,v\), and put \(d=\operatorname{dist}(u,v)\) with \(1\le d\le k\). Because a tree is bipartite, any walk from \(u\) to \(v\) has length congruent to \(d\) modulo two; moreover no walk has length below \(d\). Thus only powers \(A^r\) with \(r\ge d\) and \(r\equiv d\pmod2\) contribute to \(B_{uv}\). All their coefficients have the same sign \((-1)^{k-d}\), and the first term has magnitude \(e_{k-d}(A^d)_{uv}=e_{k-d}>0\), since a tree has exactly one geodesic between \(u,v\). No cancellation occurs. Therefore \(B_{uv}\ne0\).

**3. The exceptional cube \(k=3,\ell=4\).** The three largest path eigenvalues are \(\varphi,\varphi^{-1},-\varphi^{-1}\), where \(\varphi=(1+\sqrt5)/2\). Therefore

\[
p(x)=x^3-\varphi x^2-\varphi^{-2}x+\varphi^{-1}.
\]

For any adjacent vertices \(u,v\) in a tree, \((A^3)_{uv}=\deg(u)+\deg(v)-1\). In the present spider, each edge has \(\deg(u)+\deg(v)-1\ge2\), so \(B_{uv}=\deg(u)+\deg(v)-1-\varphi^{-2}>0\). If the tree distance is two, \(B_{uv}=-\varphi(A^2)_{uv}=-\varphi\); if it is three, \(B_{uv}=(A^3)_{uv}=1\). All are nonzero.

**4. The exceptional fourth powers \(k=4,\ell\in\{5,6\}\).** For \(\ell=5\), the four largest eigenvalues are \(\sqrt3,1,0,-1\), giving

\[
p(x)=x^4-\sqrt3 x^3-x^2+\sqrt3 x.
\]

At tree distance one, \(B_{uv}=-\sqrt3(\deg(u)+\deg(v)-2)<0\). At distance two, \(B_{uv}=(A^4)_{uv}-(A^2)_{uv}>0\): the unique intermediate neighbor \(w\) yields \((A^4)_{uv}=\deg(u)+\deg(w)+\deg(v)-2\ge2\) while \((A^2)_{uv}=1\). At distances three and four, the entries are respectively \(-\sqrt3\) and \(1\).

For \(\ell=6\), put \(a=2\cos(\pi/7)>1\), \(b=2\cos(2\pi/7)>1\), and \(s=2\cos(3\pi/7)\) with \(0<s<1\). The four largest eigenvalues are \(a,b,s,-s\), so

\[
p(x)=x^4-(a+b)x^3+(ab-s^2)x^2+(a+b)s^2x-abs^2.
\]

Since \(ab-s^2>0\), the tree-distance-two entry \(B_{uv}=(A^4)_{uv}+(ab-s^2)(A^2)_{uv}\) is positive. At distance one it is \((a+b)[s^2-(\deg(u)+\deg(v)-1)]<0\) because all edges in this spider have degree sum minus one at least two. At distances three and four it is respectively \(-(a+b)\) and \(1\). Again every required entry is nonzero.

**5. Sharpness.** Sections 2–4 prove that \(B=p(A)\) has an off-diagonal entry different from zero **if and only if** the corresponding vertices have tree distance at most \(k\). Thus \(B\) belongs to the real symmetric matrix family for \(S_m(\ell)^k\). It follows that

\[
k(m-1)\le\operatorname{null}(B)\le M(S_m(\ell)^k)\le Z(S_m(\ell)^k).
\]

For completeness, the matching prior upper bound has the following direct forcing construction (Abiad–Flagg–Ghasemi Nezhad–Zeijlemaker, Proposition 9). Initially color the outermost \(k\) vertices of each of legs \(1,\ldots,m-1\) black. Sweep each of these legs toward the center using \(v_{i,t+k}\to v_{i,t}\) for \(t=\ell-k,\ldots,1\). Once those legs are black, use \(v_{1,k}\to c\), then \(v_{1,k-j}\to v_{m,j}\) for \(j=1,\ldots,k-1\), then \(c\to v_{m,k}\); finally sweep down the last leg with \(v_{m,t-k}\to v_{m,t}\) for \(t=k+1,\ldots,\ell\). Every listed forcing vertex has exactly one remaining white neighbor in the \(k\)-th power: for a vertex at depth \(h\), its neighbors on other arms lie only at depths at most \(k-h\), and same-arm neighbors lie within depth difference \(k\). This colors every vertex with initially \(k(m-1)\) black vertices. Combining bounds proves the theorem, including the stated minimum-rank formula.

## Verification

Run `python3 verify_all.py` using Python 3 and no third-party packages. The checker constructs the spider, computes all graph distances and adjacency-power support, evaluates the real polynomial matrix \(p(A)\) by repeated sparse-adjacency multiplication, checks that its off-diagonal support equals the exact graph power, checks the explicit path-mode kernel vectors numerically, and simulates the claimed forcing seed. It tested 108 pairs of graph powers and parameters with \(2\le m\le5\), \(3\le k\le6\), and \(k+1\le\ell\le13\), restricted to the claimed range. Five small cases received exhaustive tests of every candidate seed of size \(k(m-1)-1\), totaling 91,793 subsets. All checks passed; `verification_output.txt` contains the complete output. Numerical checks use real floating-point arithmetic; the infinite theorem and exact nonvanishing rest on the symbolic proof, not finite testing or approximate root separation.

## Relationship to prior work

The motivating preprint [1, Proposition 9] proves the upper bound \(Z(S_m(\ell)^k)\le k(m-1)\) and explicitly poses equality as Conjecture 10, supported there by small computational cases. The present theorem proves equality in the stated infinite region, and in addition determines the real symmetric maximum nullity. Reference [1, Theorem 20] already gives the **general conditional eigenvalue-polynomial lower-bound method**; that method is not claimed as new. The additional mathematical point here is the choice of \(k\) repeated spider-arm eigenmodes and the exact, all-edge noncancellation proof for that particular polynomial, including the three short-arm boundary cases. A conditional theorem without the nonvanishing check does not itself settle the conjecture. The earlier minimum-rank treatments [2] and [3] cover path powers, strict powers, and tree squares, but not the present higher-power equal-leg-spider result.

## Limitations

No claim is made for \(k\ge5\) with \(k+1\le\ell<2k-1\), for unequal-leg spiders, or for arbitrary trees. The result does not classify the minimizers or all matrices attaining maximum nullity. Mathematical originality is conditional on the literature inspected: an equivalent result in unindexed or uninspected work may exist. The floating-point tests provide reproducibility and boundary stress-testing, not an exhaustive proof beyond the stated small cases; the proof above is exact. Independent external validation has not been performed.

## References

[1] A. Abiad, M. Flagg, S. Ghasemi Nezhad, and S. Zeijlemaker, *The Zero Forcing Number of Graph Powers*, arXiv:2610.03892v1 (first posted 2026-10-02), especially Proposition 9, Conjecture 10 and Theorem 20. https://arxiv.org/html/2610.03892v1

[2] L. M. DeAlba, J. Grout, I.-J. Kim, S. Kirkland, J. J. McDonald, and A. Yielding, *Minimum rank of powers of trees*, Electronic Journal of Linear Algebra 23 (2012), 151–163. https://journals.uwyo.edu/index.php/ela/article/download/1023/1023/1023

[3] G. J. Chang and J. C.-H. Lin, *Minimum rank of powers of cycles and trees*, available author-hosted manuscript, especially Theorem 4.1 on the square of a tree. https://www-math.nsysu.edu.tw/~chlin/Publications/Articles/GJpower.pdf
