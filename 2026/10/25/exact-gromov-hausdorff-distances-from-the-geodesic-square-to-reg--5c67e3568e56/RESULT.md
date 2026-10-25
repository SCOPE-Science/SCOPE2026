# Exact Gromov–Hausdorff distances from the geodesic square to regular \(4k+2\)-gons

## Finding

Let \(P_n\), for \(n\geq 2\), denote the \(n\) equally spaced points on a **unit circle**, endowed with **the restriction of the circle's geodesic (shorter-arc) metric**, rather than the Euclidean chord metric. For **every integer** \(k\geq1\),
\[
d_{\mathrm{GH}}(P_4,P_{4k+2})=\frac{\pi k}{4k+2}=\frac{\pi}{4}-\frac{\pi}{2(4k+2)}.
\]
Thus the first three cases are \(d_{\mathrm{GH}}(P_4,P_6)=\pi/6\), \(d_{\mathrm{GH}}(P_4,P_{10})=\pi/5\), and \(d_{\mathrm{GH}}(P_4,P_{14})=3\pi/14\). Combining this new residue-class formula with the known divisible-case theorem of Talipov gives the exact distances from \(P_4\) to every **even** regular polygon vertex set: when \(m=4q\), \(d_{\mathrm{GH}}(P_4,P_m)=\pi/4-\pi/m\); when \(m=4q+2\), \(d_{\mathrm{GH}}(P_4,P_m)=\pi/4-\pi/(2m)\). This combination is context, not an additional independent finding.

## Assumptions and scope

All lengths refer to the unit circle of circumference \(2\pi\). For a regular \(n\)-point set indexed by \(i\in\{0,\ldots,n-1\}\), its metric is
\[
d_n(i,j)=\frac{2\pi}{n}\,\delta_n(i,j),\qquad
\delta_n(i,j)=\min\bigl\{|i-j|,n-|i-j|\bigr\}.
\]
A correspondence \(R\subseteq X\times Y\) projects onto both \(X\) and \(Y\). Its distortion is \(\operatorname{dis}R=\sup\{|d_X(x,x')-d_Y(y,y')|:(x,y),(x',y')\in R\}\), and for finite metric spaces \(2d_{\mathrm{GH}}(X,Y)=\min_R\operatorname{dis}R\). No assumption of one-to-one matching or of order-preserving correspondences is made in the lower bound. Only the constructed upper-bound matching is cyclically ordered.

## Proof

Fix an arbitrary integer \(k\geq1\), set \(m=4k+2\) and \(t=2\pi/m\), and measure every geodesic distance in units of \(t\). On \(P_m\) these distances are integers \(\delta_m(i,j)\); on \(P_4\), adjacent labels have distance \(\pi/2=(k+\tfrac12)t\) and opposite labels have distance \(\pi=(2k+1)t\).

**Packing lemma.** Every subset of \(P_m\) with at least \(k+1\) distinct vertices contains two at graph distance at least \(k\). To prove this, suppose all distances within a subset \(A\) were at most \(k-1\). Rotate one selected vertex to index \(0\). Each other index has a unique signed representative between \(-(k-1)\) and \(k-1\) (any other choice would exceed the assumed graph distance to \(0\)). Let \(a\geq0\) be the largest nonnegative representative and \(-b\leq0\) the smallest nonpositive one. The circle distance between these extreme representatives equals \(a+b\), because \(a+b\leq2k-2<m/2\). The pairwise-distance assumption therefore forces \(a+b\leq k-1\). Consequently all vertices of \(A\) lie among at most \(a+b+1\leq k\) integer positions, contradicting \(|A|\geq k+1\). The lemma includes \(k=1\).

**Lower bound, for every correspondence.** Let \(R\) be any correspondence between \(P_4\) and \(P_m\). For each of its four square vertices \(u\), let \(F_u=\{v\in P_m:(u,v)\in R\}\) be the fiber. Because the four fibers cover all \(m=4k+2\) vertices, at least one contains \(\lceil m/4\rceil=k+1\) distinct vertices. The packing lemma gives \(v,w\) in this fiber with \(d_m(v,w)\geq kt\). Pairing both with \(u\) makes the square distance zero, so \(\operatorname{dis}R\geq kt\) for **every** correspondence. Hence \(d_{\mathrm{GH}}(P_4,P_m)\geq kt/2\).

**Matching upper bound.** Label \(P_m\) cyclically by integers \(0,\ldots,4k+1\), and partition these indices consecutively into blocks
\[
B_0=[0,k],\quad B_1=[k+1,2k],\quad B_2=[2k+1,3k+1],\quad B_3=[3k+2,4k+1],
\]
where each interval includes both integer endpoints. Their sizes are \(k+1,k,k+1,k\). Define \(f:P_m\longrightarrow P_4\) by mapping all indices in \(B_j\) to square label \(j\). All four blocks are nonempty, so its graph is a correspondence.

The following bounds exhaust all pairs of indices. Within a single block, \(0\leq\delta_m\leq k\), whereas the target distance is \(0\). Between cyclically adjacent blocks, \(1\leq\delta_m\leq2k\), whereas the target in units of \(t\) is \(k+\tfrac12\), giving discrepancy at most \(k-\tfrac12\). Between opposite blocks \(B_0,B_2\), \(k+1\leq\delta_m\leq2k+1\); between \(B_1,B_3\), \(k+2\leq\delta_m\leq2k+1\). The opposite-label target is \(2k+1\), so both discrepancies are at most \(k\). The same conclusions hold for either order of each pair, and every pair of blocks is same, adjacent or opposite. It follows that \(\operatorname{dis}(f)\leq kt\). Equality actually holds for indices \(0\) and \(k\) in \(B_0\), which are \(k\) apart in \(P_m\) but map to one square vertex. Thus \(\operatorname{dis}(f)=kt\) and \(d_{\mathrm{GH}}(P_4,P_m)\leq kt/2\).

The bounds agree: \(kt/2=k\pi/m\), proving the formula for all \(k\geq1\).

## Verification

The file `check_round_polygon.py` is a standalone standard-library Python check. Running `python check_round_polygon.py` verifies the constructed correspondence's exact distortion in doubled integer units for every \(1\leq k\leq100\), and exhaustively checks the packing lemma for all subsets of size \(k+1\) when \(1\leq k\leq4\). The script was executed successfully. These checks test arithmetic and indexing; **they are not substitutes for the uniform proof** above. The analytic steps were separately rechecked at the boundary \(k=1\), the wrap-around adjacent blocks \(B_3,B_0\), the opposite-block cyclic wrap, and arbitrary multivalued correspondences.

## Relationship to prior work

Talipov (2022, arXiv:2210.09971v1), Theorem 3.1, determines \(d_{\mathrm{GH}}(P_n,P_m)\) when \(n\mid m\); its Theorems 3.2–3.3 settle the cases \(n=2,3\). None covers \(n=4\), \(m=4k+2\), since \(4\nmid4k+2\) and \(P_4\) is not an equilateral simplex. Lim–Mémoli–Smith (arXiv:2105.00611v6), Appendix C, poses the general exact-distance question and computes the circle-to-polygon and consecutive-polygon cases, without giving the new residue-class formula. The proof above supplies both a sharp correspondence and a packing-based obstruction in this distinct case. The established chord-metric hyperbolicity and convexity-gap formulas for regular polygon vertex sets concern **different distance functions and invariants**; they do not imply this geodesic-metric Gromov–Hausdorff identity. Literature searches are not proof of absolute publication priority.

## Limitations

The theorem holds only for discrete vertex sets with the inherited **circle geodesic** metric, for source cardinality \(4\) and target cardinalities \(4k+2\) with \(k\geq1\). It says nothing about Euclidean chord distance, the intrinsic path metric along the polygonal perimeter, arbitrary four-point metrics, or odd target cardinalities. The result gives one explicit optimal correspondence but does not classify all optimal correspondences. Its correctness follows from the displayed proof; originality is a best-knowledge scholarly comparison and has not received independent audit.

## References

1. T. Talipov, *Gromov–Hausdorff distance between vertex sets of regular polygons inscribed in a given circle*, arXiv:2210.09971v1, 18 October 2022, https://arxiv.org/html/2210.09971v1. In particular §2 and Theorems 3.1–3.3.
2. S. Lim, F. Mémoli, Z. Smith, *The Gromov-Hausdorff distance between spheres*, arXiv:2105.00611v6, https://arxiv.org/html/2105.00611v6. In particular §1 and Appendix C, Question VI and Propositions C.2–C.5.
