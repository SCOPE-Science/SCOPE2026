# Chromatic repair radii of friendship graphs and an unbounded three-copy gap

## Finding

For an integer \(m\ge 1\), let \(F_m=K_1\vee(mK_2)\) be the friendship graph of \(m\) triangles with a common hub. Colors are the three named labels \(\{0,1,2\}\). A word is any assignment of these colors to the \(2m+1\) vertices, without a properness requirement. Write \(d(w,y)\) for the number of vertices on which two words differ, and let \(\mathcal P\) be the set of proper three-colorings.

Define the unrestricted three-color fixing radius by
\[
\operatorname{Fix}_3(F_m)=\max_w\min_{y\in\mathcal P}d(w,y).
\]
For a source word \(w\) having the color-multiplicity vector of at least one proper coloring, ordinary chromatic villainy minimizes over proper targets with the **same named multiplicity vector**, while weak chromatic villainy minimizes over all proper targets. Write their maxima over such sources as \(B(F_m)\) and \(B_{\mathrm w}(F_m)\).

**Theorem.** For every integer \(m\ge2\),
\[
B(F_m)=m+1,\qquad
B_{\mathrm w}(F_m)=
\begin{cases}
m,&m\in\{2,3\},\\
m+1,&m\ge4.
\end{cases}
\]
For every integer \(m\ge1\),
\[
\operatorname{Fix}_3(F_m)=m+\left\lfloor\frac{m+2}{3}\right\rfloor,\qquad
B_{\mathrm w}(3F_m)=3m+3\left\lfloor\frac{m+2}{3}\right\rfloor,
\]
where \(3F_m\) denotes the disjoint union of three copies, not the third friendship graph. Consequently, for every integer \(m\ge4\),
\[
B_{\mathrm w}(3F_m)-3B_{\mathrm w}(F_m)
=3\left\lfloor\frac{m-1}{3}\right\rfloor.
\]
Thus a natural family of connected three-chromatic graphs has an unbounded weak-villainy superadditivity gain already upon taking three identical copies. At the boundary \(m=1\), \(F_1=K_3\) has \(B(F_1)=B_{\mathrm w}(F_1)=0\), while the unrestricted fixing radius equals \(2\).

## Assumptions and scope

All graphs are finite and simple. The \(m\) peripheral edges of \(F_m\) are labelled only for the proof and verifier; no quotient by graph automorphisms is taken. The distance is Hamming distance in **vertices recolored**, rather than the number of swaps. A proper three-coloring gives one color to the hub and the two other colors, in either order, to the endpoints of each peripheral edge. Hence for \(m\ge2\) every proper coloring has multiplicities \(1,m,m\), up to permutation of the named colors. For \(m=1\), all proper three-colorings use each color once.

For any word \(w\) and hub-target color \(c\), let \(D_c(w)\) be the smallest distance to a proper coloring whose hub has color \(c\). This is an exact independently optimizable sum over peripheral edges. If the source endpoint colors are \(x,y\), the least peripheral repair cost is
\[
\delta_c(x,y)=
\begin{cases}
2,&x=y=c,\\
0,&x\ne y\text{ and }c\notin\{x,y\},\\
1,&\text{otherwise}.
\end{cases}
\]
Therefore
\[
D_c(w)=\mathbf1_{\{w(\mathrm{hub})\ne c\}}+
\sum_{j=1}^{m}\delta_c(w(u_j),w(v_j)).
\]
This identity is both the proof's local invariant and the verifier's target-distance rule.

## Proof

**Unrestricted radius.** For each peripheral edge whose source endpoint colors are equal, the sum of the three possible peripheral repair costs is \(4\). For an edge whose endpoint colors differ, it is \(2\). The three possible hub penalties sum to \(2\). Hence
\[
\sum_{c=0}^{2}D_c(w)\le 4m+2.
\]
Since the distances are integers,
\[
\min_cD_c(w)\le\left\lfloor\frac{4m+2}{3}\right\rfloor
=m+\left\lfloor\frac{m+2}{3}\right\rfloor.
\]
For equality, put \(t=\lfloor(m+2)/3\rfloor\), color the source hub \(0\), and take respectively \(t,t-1,m-2t+1\) monochromatic peripheral edges of source colors \(0,1,2\). These counts are nonnegative and sum to \(m\) because \(3t-2\le m\). The three repair costs are \(m+t\), \(m+t\), and \(2m-2t+2\), the third being at least \(m+t\) because \(m\ge 3t-2\). Therefore the lower bound matches the upper bound for all \(m\ge1\).

**Ordinary villainy.** Suppose \(m\ge2\), and name the singleton source color \(0\). A proper target with the same color counts must put \(0\) at the hub. If the source hub already has \(0\), every peripheral edge has endpoint colors drawn from \(\{1,2\}\) and can be repaired by at most one change. If the source hub has a different color, change it to \(0\); exactly one peripheral vertex then has color \(0\), and its edge requires at most one further change, as does each other peripheral edge. Thus \(B(F_m)\le m+1\).

For the opposite inequality put \(k=\lfloor m/2\rfloor\). If \(m=2k\), give the source hub color \(1\), one peripheral edge the ordered colors \((0,1)\), \(k-1\) edges \((1,1)\), and \(k\) edges \((2,2)\). If \(m=2k+1\), give the source hub color \(1\), one peripheral edge \((0,2)\), \(k\) edges \((1,1)\), and \(k\) edges \((2,2)\). In either case the source profile is \((1,m,m)\), its hub and the unique edge containing color \(0\) cost one change each, and all other peripheral edges cost one. Thus \(D_0(w)=m+1\).

**Weak villainy.** It is always bounded by ordinary villainy. For even \(m=2k\), the last construction has repair costs
\[
(D_0,D_1,D_2)=(m+1,\ 3k-1,\ 3k).
\]
For odd \(m=2k+1\), it has costs
\[
(D_0,D_1,D_2)=(m+1,\ 3k,\ 3k+2).
\]
For every \(m\ge4\), all three are at least \(m+1\), so \(B_{\mathrm w}(F_m)=m+1\).

For \(m=2\), a source with the singleton color at the hub needs at most two changes. Otherwise, at most one peripheral edge is monochromatic. The three repair costs then sum to at most \(2+2m+2=8\), so their minimum is at most \(2\). The source consisting of a singleton-color hub and peripheral edges monochromatic in each of the other two colors realizes two changes, giving \(B_{\mathrm w}(F_2)=2\).

For \(m=3\), a source with the singleton color at the hub needs at most three changes. Otherwise, at most two peripheral edges are monochromatic. If at most one is monochromatic, then the three repair costs sum to at most \(2+2m+2=10\), forcing their minimum to be at most three. If exactly two are monochromatic, the remaining edge contains the singleton color. By the profile \((1,3,3)\) and parity, after renaming colors the source hub is color \(1\), the mixed edge has colors \((0,2)\), and the two monochromatic edges have colors \((1,1)\) and \((2,2)\). Choosing target hub color \(1\) changes exactly three peripheral vertices. This source also realizes weak repair distance three, so \(B_{\mathrm w}(F_3)=3\).

**Three copies.** For any source on \(3F_m\), weak repair can optimize each component independently, so
\[
B_{\mathrm w}(3F_m)\le3\operatorname{Fix}_3(F_m).
\]
Take one source word realizing \(\operatorname{Fix}_3(F_m)\), and place on three separate copies its three cyclic color relabelings. Every named color appears exactly \(2m+1\) times in the resulting triple word. This global profile is feasible: take any proper coloring of \(F_m\) and use its three cyclic relabelings on the three components. Therefore the triple word is an admissible disturbance, and its optimal weak repair cost is \(3\operatorname{Fix}_3(F_m)\). The reverse inequality holds, proving the three-copy formula. Subtracting three times the single-copy value gives the stated unbounded gap for \(m\ge4\).

## Verification

The self-contained `verify.py` enumerates all \(3^{2m+1}\) source words for each \(1\le m\le6\), computing exact repair distances by explicitly comparing the two proper color orientations on each peripheral edge. It also filters legal source profiles and independently checks the ordinary and weak maxima. Across these six orders, it examines \(1{,}793{,}610\) words and \(15{,}590\) legal profile words. Explicit extremal constructions and cyclic-label tripling are checked for every \(2\le m\le100\).

Execute from the extracted files with `python3 verify.py`. The expected outcome is `VERIFY_OK m=1..6 all_words=1793610 legal_words=15590 construction_m=2..100`. These finite tests are checks of the proof, not substitutes for its infinite arguments.

## Relationship to prior work

Clark, Holliday, Holliday, Johnson, Trimm, Rubalcaba, and Walsh introduced ordinary and weak chromatic villainy and studied general graph families. Garnero and collaborators introduced the color-fixing radius as an unrestricted repair invariant. Jiang, Jiang, Li, Wang, and Zhang (arXiv:2610.13580v1) established refined profile-radius formulas for odd cycles, complete multipartite graphs, and extremal bounds. Their companion work (arXiv:2610.13556v1) proves the general identity \(B_{\mathrm w}(kG)=k\operatorname{Fix}_k(G)\) for \(k=\chi(G)\). That general identity is acknowledged as prior work: the three-copy argument above is given solely to make this application self-contained.

The claimed contribution is the exact determination of **all three single-copy repair radii for the friendship family**, including the small weak-repair exceptions and its unbounded difference between unrestricted and feasible-profile fixing. The repeated-copy expression is a consequence of this new input and the previously known general theorem. The cited works' general results do not themselves give the friendship-family formulas; a friendship graph with at least two blades is not complete multipartite.

## Limitations

No value is asserted for arbitrary clique windmills of larger blade size, arbitrary cactus graphs, or general three-chromatic graphs. The three-copy calculation is not a new general disjoint-union theorem. The originality comparison is bounded by accessible literature and research records; an older full-text treatment of fixing numbers was not accessible during this examination. Formal independent mathematical review remains outstanding.

## References

1. S. A. Clark, J. E. Holliday, S. H. Holliday, P. D. Johnson Jr., J. E. Trimm, R. R. Rubalcaba, and M. Walsh, *Chromatic villainy in graphs*, Congressus Numerantium **182** (2006), 171–182.
2. V. Garnero, K. Junosza-Szaniawski, M. Liedloff, P. Montealegre, and P. Rzążewski, *Fixing improper colorings of graphs*, Theoretical Computer Science **711** (2018), 66–78, DOI: 10.1016/j.tcs.2017.11.013.
3. J. Jiang, Y. Jiang, Y. Li, L. Wang, and A. Zhang, *Exact and extremal values of chromatic villainy*, arXiv:2610.13580v1 (first publicly posted 2026-10-09).
4. J. Jiang, Y. Jiang, Y. Li, L. Wang, and A. Zhang, *Disjoint unions and fixed-parameter algorithms for chromatic villainy*, arXiv:2610.13556v1 (first publicly posted 2026-10-09).
