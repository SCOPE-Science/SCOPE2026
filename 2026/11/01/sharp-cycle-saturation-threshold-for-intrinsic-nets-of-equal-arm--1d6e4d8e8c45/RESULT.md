# Sharp cycle-saturation threshold for intrinsic nets of equal-arm multipath graphs

## Finding
For integers \(m\ge2\) and \(p\ge1\), let \(G_{m,s,L}\) consist of two common vertices \(A,B\) joined by one edge of length \(L\) and \(m\) further parallel edges each of length \(s\), where \(L\ge s>0\). Equip the entire compact graph, including edge interiors, with its intrinsic shortest-path metric. Define the unrestricted \(p\)-point covering radius by
\[
\rho_p(G)=\min_{c_0,\ldots,c_{p-1}\in G}\ \max_{x\in G}\min_{0\le j<p}d_G(x,c_j).
\]
Then
\[
\boxed{\rho_p(G_{m,s,L})\ge\frac{L+s}{2p},\qquad
\rho_p(G_{m,s,L})=\frac{L+s}{2p}\quad\Longleftrightarrow\quad L\ge(p-1)s.}
\]
If \(L<(p-1)s\), the inequality is **strict**. The equality threshold is independent of the number \(m\) of short arms and is attained at its boundary. Whenever equality holds, an explicit optimal set lies entirely on the long edge: with
\[
q=\frac{L+s}{2p},\qquad t_0=q-\frac{s}{2}=\frac{L-(p-1)s}{2p},
\]
measure coordinates from \(A\) along the long edge and take \(p\) centers at
\[
\boxed{t_j=t_0+2jq\quad (j=0,\ldots,p-1).}
\]
In particular, the intrinsic two-center radius is \((L+s)/4\) for every \(L\ge s\) and every \(m\ge2\), no matter how large the first Betti number \(m\) is.

## Assumptions and scope
Edges are continuous real intervals; distances are lengths of shortest graph paths, not discrete vertex distances or distances in a planar drawing. The long arm has length \(L\), while every one of the \(m\) remaining arms has the **same** length \(s\). Both endpoints are identified across all arms. Centers can be anywhere in the geometric realization, and the covering quantifiers include all points of all edges. In the equality formula the centers are distinct because \(q>0\). The case \(p=1\) is included. Equality for \(L<(p-1)s\) is impossible; the theorem does not give an exact value in this latter regime.

## Proof
**1. Isometric cycle and universal lower bound.** Choose the long edge and one of the length-\(s\) edges. Their union \(C\) is a circle of circumference \(P=L+s\), embedded *isometrically* in \(G\): every excursion through another short edge can be replaced by the selected short edge with the same length, so no shortcut between points of \(C\) is gained.

Every point on an omitted short edge at coordinate \(u\in[0,s]\) from \(A\) has a counterpart on the chosen short edge at the same coordinate. Distances from that counterpart to each point of \(C\) are no larger: for points on the long edge the two route lengths via \(A\) or \(B\) are unchanged; for points on the chosen short edge a direct route is additionally available. Thus any \(p\)-center cover of \(G\) of radius \(r\) produces a cover of the intrinsic circle \(C\) by \(p\) centers on \(C\) at radius at most \(r\).

A radius-\(r\) ball on a circle of circumference \(P\) covers at most \(2r\) of its arclength when \(r\le P/2\). Consequently any \(p\)-point cover of \(C\) satisfies \(P\le2pr\) (trivially if \(r>P/2\)); hence \(\rho_p(G)\ge P/(2p)\). The minimum exists because \(G^p\) is compact and the maximum-distance objective is continuous.

**2. Explicit attainment when \(L\ge(p-1)s\).** Put \(q=P/(2p)\) and \(t_0=q-s/2\ge0\). The points \(t_j=t_0+2jq\) lie on the long arm, since \(t_0\ge0\) and \(t_{p-1}=L-t_0\le L\). Consecutive center positions differ by \(2q\); the first direct \(q\)-interval starts at \(-s/2\), and the last ends at \(L+s/2\). Their direct intervals cover the whole long arm. On any short arm the first and last centers are at distance \(t_0\) from \(A\) and \(B\), respectively (or no farther via alternative paths); a short-arm point at coordinate \(u\) is therefore within distance
\[
\min\{t_0+u,t_0+s-u\}\le t_0+s/2=q.
\]
Thus the full graph is \(q\)-covered, giving equality.

**3. Sharp obstruction when \(L<(p-1)s\).** Here \(q=P/(2p)<s/2\), necessarily with \(p\ge2\). Suppose \(p\) graph points covered all of \(G\) with radius \(q\). For a center in \(C\), its radius-\(q\) ball meets \(C\) in an arc of length exactly \(2q\). For a center in the *interior* of an omitted short arm, let its distances along that arm to \(A,B\) be \(u,s-u\). Since \(2q<s\), at most one of \(u,s-u\) can be less than \(q\). All routes to \(C\) first pass through a pole, so this center's ball intersects \(C\) in arclength at most
\[
2\max\{0,q-u,q-(s-u)\}<2q.
\]
The strict inequality uses \(0<u<s\). Because the circumference of \(C\) is \(P=2pq\), covering \(C\) at radius \(q\) with only \(p\) balls forces **every** center to lie in \(C\), otherwise their total covered arclength is strictly less than \(P\). But another short edge exists because \(m\ge2\). Its midpoint has distance at least \(s/2>q\) from every point of \(C\), a contradiction. By attainment of the minimum, \(\rho_p(G)>q\) in this regime. This finishes both directions, including the equality boundary.

## Verification
An independent rational-arithmetic checker is included as `check_cover.py`. It recomputes intrinsic shortest-path distances, tests 344 admissible parameter configurations with 414,723 exact point and obstruction assertions, and checks the placement identities and strict-regime inequalities. Execute `python3 check_cover.py`. Finite sampling is supplementary: universal quantifiers follow from the three analytical steps, not from the checker.

## Relationship to prior work
Continuous network \(p\)-center problems and structural restrictions on their possible optimal values are classical, including Tamir's 1987 work. More recent general covering-complexity results for unit-edge graphs are due to Hartmann, Lendl, and Woeginger (2021). The present statement is an exact metric-geometry saturation/equality threshold for a continuous weighted family with arbitrarily many parallel short arms; neither a general finite algorithm nor a possible-value theorem alone implies its explicit classification. The isometric-circle lower bound is standard, and only its simultaneous attainability and sharp failure for this graph family are proposed here as the added result.

## Limitations
No formula is asserted for the radius when \(L<(p-1)s\); only strict separation from the circle bound is proved. No claims are made for unequal short arms, discrete-only demand, general weighted networks, or uniqueness of the optimal center set. The historical literature has not been exhaustively indexed; the full text of a particularly relevant 1987 paper was not available for substantive comparison, leaving a priority risk.

## References
- A. Tamir, *On the Solution Value of the Continuous p-Center Location Problem on a Graph*, Mathematics of Operations Research 12 (1987), 340–349. DOI: 10.1287/moor.12.2.340. Public date: 1987-05-01.
- T. A. Hartmann, S. Lendl, G. J. Woeginger, *Continuous facility location on graphs*, Mathematical Programming 192 (2022), 207–227; open-access first publication 2021-03-26. DOI: 10.1007/s10107-021-01646-x.
