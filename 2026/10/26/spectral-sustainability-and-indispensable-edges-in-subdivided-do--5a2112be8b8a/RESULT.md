# Spectral sustainability and indispensable edges in subdivided double brooms

## Finding

**Theorem.** Let \(B(\ell,a,b)\) be formed from a path of \(\ell\) edges by attaching \(a-1\) leaves to its first endpoint and \(b-1\) leaves to its second endpoint. For all integers \(\ell\ge2\) and \(a,b\ge2\), an edge is called *sustainable* if deleting it and adding a different edge yields a connected graph of no smaller adjacency spectral radius. Then

\[
B(\ell,a,b)\text{ is sustainable}\quad\Longleftrightarrow\quad |a-b|\le1.
\]

More strongly, when \(a\ge b+2\), **exactly** the \(a-1\) leaf edges at the degree-\(a\) endpoint are non-sustainable; all other edges are sustainable. The symmetric statement holds when \(b\ge a+2\). In particular this gives the location and exact count of every indispensable edge in the entire family. The restriction \(\ell\ge2\) is essential: the center-to-center edge of a proper double star (\(\ell=1\)) is non-sustainable even for balanced centers.

## Assumptions and scope

All graphs are finite simple undirected trees. Write \(\rho(G)\) for the largest eigenvalue of the adjacency matrix of \(G\), and \(\Phi(G;t)=\det(tI-A(G))\). The tree has \(\ell+a+b-1\) vertices. Every admissible edge replacement reconnects the two components after deleting the edge; when the deleted edge is pendant, it simply reattaches the isolated leaf to a different vertex. Labels on leaves and on the two endpoints do not affect the conclusions.

We use the standard generalized-tree-shift comparison: a nontrivial shift which moves an attached branch toward a branching vertex strictly increases \(\rho\) unless the resulting tree is isomorphic. In particular, every edge incident to a degree-two vertex is sustainable; see the cited references. A separate direct spectral calculation below handles all other candidate attachments, not only those to a new center.

## Proof

**1. Leaf-attachment comparison.** For a tree \(H\) and a vertex \(w\in V(H)\), let \(H_w^+\) be formed by attaching one new pendant vertex at \(w\). Expanding its characteristic polynomial along the pendant vertex gives
\[
\Phi(H_w^+;t)=t\Phi(H;t)-\Phi(H-w;t).
\]
For \(t>\rho(H)\), the resolvent entry
\[
R_w(t)=\frac{\Phi(H-w;t)}{\Phi(H;t)}=((tI-A(H))^{-1})_{ww}
\]
is positive and strictly decreasing, since its derivative is \(-((tI-A(H))^{-2})_{ww}<0\). Thus \(\rho(H_w^+)\) is the unique solution \(t=R_w(t)\) in \((\rho(H),\infty)\). At \(t=\rho(H_u^+)\), a strict inequality \(\Phi(H-u;t)>\Phi(H-w;t)\) consequently implies \(\rho(H_u^+)>\rho(H_w^+)\); equality of the two deleted-vertex polynomials implies equality of the two spectral radii.

**2. Exact comparison along the spine.** In the core \(H=B(\ell,c,d)\), write \(e=c-1\) and \(f=d-1\), and label the spine \(v_0=u,v_1,\ldots,v_\ell=v\). Set \(P_{-1}(t)=0\), \(P_0(t)=1\), \(P_1(t)=t\), and \(P_{j+1}(t)=tP_j(t)-P_{j-1}(t)\). The path-determinant recurrence yields
\[
\begin{aligned}
\Phi(H-u;t)&=t^{e+f}\left(P_\ell-\frac ftP_{\ell-1}\right),\\
\Phi(H-v;t)&=t^{e+f}\left(P_\ell-\frac etP_{\ell-1}\right),\\
\Phi(H-v_i;t)&=t^{e+f}\left(P_i-\frac etP_{i-1}\right)
\left(P_{\ell-i}-\frac ftP_{\ell-i-1}\right)
\quad(1\le i<\ell).
\end{aligned}
\]
For \(e>f\), the endpoint difference is
\[
\Phi(H-u;t)-\Phi(H-v;t)=t^{e+f-1}(e-f)P_{\ell-1}(t)>0\qquad(t>2).
\]
Writing \(k=\ell-i\), expansion of the interior difference gives the **spine comparison identity**
\[
\frac{\Phi(H-u;t)-\Phi(H-v_i;t)}{t^{e+f}P_{i-1}(t)}
=\frac{e-f}{t}P_k(t)+\left(f-1-\frac{ef}{t^2}\right)P_{k-1}(t).
\tag{1}
\]
All \(P_j(t)\) are positive, and \(P_k(t)>P_{k-1}(t)\) for \(t>2\). If \(e\ge f+1\), \(f\ge1\), and \(t>\sqrt{e+2}\), the right side of (1) is positive. Indeed, if the coefficient of \(P_{k-1}\) is nonnegative, this is immediate. Otherwise it exceeds
\[
\frac{P_{k-1}(t)}{t^2}\big((f-1)t^2+(e-f)t-ef\big).
\]
As \(t^2>e+2\) and \(t>2\), the bracket exceeds
\[
(e-f)(t-1)+f-2>0.
\]
These inequalities hold for every interior spine vertex, with no restriction on \(\ell\).

**3. Unsustainable leaf edges at the larger center.** Assume \(a\ge b+2\). Remove a leaf \(x\) at \(u\), leaving \(H=B(\ell,a-1,b)\) with \(e=a-2\ge f+1\) and \(f=b-1\ge1\). Put \(t=\rho(B(\ell,a,b))=\rho(H_u^+)\). The original contains the degree-\(a=e+2\) star as a proper subgraph, so strict Perron monotonicity gives \(t>\sqrt{e+2}\ge2\). Step 2 and Step 1 give \(\rho(H_w^+)<t\) for every other spine vertex \(w\ne u\), including \(v\). If \(w\) is a pendant vertex of \(H\), attaching \(x\) at \(w\) creates a length-two pendant branch. A generalized tree shift from \(w\) to its center produces \(H_u^+\) or \(H_v^+\) with strictly larger spectral radius. In either case the value is strictly below \(t\), unless the shift ends at \(u\), in which case it is precisely \(t\). Therefore no different reconnection of the deleted leaf edge preserves the spectral radius, proving every high-center leaf edge non-sustainable.

**4. All other edges and the boundary.** Every spine edge meets a degree-two interior spine vertex because \(\ell\ge2\), hence is sustainable by the generalized-tree-shift lemma. When \(a\ge b+2\) and \(b\ge3\), removing a leaf at \(v\) gives core \(B(\ell,a,b-1)\) with leaf counts \(e=a-1>f=b-2\); the positive endpoint comparison in Step 2 shows that reattaching it at \(u\) strictly raises the spectral radius. If \(b=2\), every edge at \(v\) meets its degree-two endpoint and is sustainable.

When \(a=b\ge3\), removal of a leaf at either center makes that core center have one fewer leaf than the other. The endpoint comparison strictly favors reattachment to the opposite center. When \(a=b=2\), both endpoints have degree two, so every edge is sustainable. When \(a=b+1\), reattaching a leaf of \(u\) at \(v\) exchanges the endpoint degrees and produces an isomorphic double broom, preserving the spectral radius. The lower-center leaf edges are sustainable either by the positive endpoint comparison (for \(b\ge3\)) or the degree-two lemma (for \(b=2\)). By symmetry this covers \(b>a\) as well and completes the exact edge classification. \(\square\)

## Verification

`verify.py` builds each double broom directly and, for every edge, enumerates *all* legal replacement edges between the components resulting from its deletion. It computes the adjacency spectral radii independently and checks that the observed non-sustainable edges are precisely those predicted by the theorem. It verifies all 75 unordered-center parameter triples with \(2\le\ell\le6\) and \(2\le b\le a\le6\) (not an exhaustive proof of all orders); the executable completed with `VERIFY_OK`. Run `python verify.py` after installing the NumPy dependency from `requirements.txt`. The symbolic spine identity also follows from \(P_{r+s}=P_rP_s-P_{r-1}P_{s-1}\) and the three determinant expressions in Step 2; those identities, not the numeric trials, establish the infinite conclusion.

## Relationship to prior work

Bencs, van Dijk, and Guo introduced tree sustainability as an edgewise spectral-radius robustness property. Their 2026 preprint, first posted on October 12, establishes the degree-two edge lemma, a high-maximum-degree obstruction, and the sustainable special case \(B(2,k,k-1)\). The present theorem treats every path length \(\ell\ge2\) and every pair of center degrees, including unbalanced cases below the established high-degree threshold, and locates *all* non-sustainable edges. Its use of the generalized tree shift and the pendant-vertex characteristic-polynomial comparison builds on, and does not re-claim, their known general lemmas. Csikvári's generalized tree shifts provide the underlying monotonicity. A related 2025 thesis by van Dijk was not accessible in full for priority checking and remains a stated historical-priority risk.

## Limitations

The classification is specific to double brooms with at least one degree-two vertex strictly between the centers. It does not classify arbitrary trees or the \(\ell=1\) double stars, whose center-to-center edge behaves differently. Numerical checks cover only the stated finite parameter window. Priority has not been independently audited, and inaccessible prior literature may contain a stronger equivalent claim.

## References

1. F. Bencs, M. van Dijk, and K. Guo, *Sustainable trees*, arXiv:2610.17078v1 (first public version, 2026-10-12), https://arxiv.org/pdf/2610.17078v1.
2. P. Csikvári, *On a Poset of Trees II*, https://real.mtak.hu/14003/1/poset_treesIIV2.pdf.
3. M. van Dijk, *Sustainable trees: A deep dive into the spectral radii and centers of trees* (Master's thesis, 2025), https://studenttheses.uu.nl/handle/20.500.12932/50792 (full text not accessed).
