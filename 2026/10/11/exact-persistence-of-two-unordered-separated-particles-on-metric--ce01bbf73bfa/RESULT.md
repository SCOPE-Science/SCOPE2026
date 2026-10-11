# Exact persistence of two unordered separated particles on metric stars

## Finding
For every integer \(k\ge 3\), every positive arm-length vector \(\mathbf L=(L_1,\ldots,L_k)\), and every real separation threshold \(r>0\), consider the unordered configuration space \(U_r(\mathbf L)\) of two distinct points on the metric \(k\)-arm star at path-metric distance at least \(r\). As \(r\) decreases, the inclusions \(U_{r'}(\mathbf L)\hookrightarrow U_r(\mathbf L)\) for \(r\le r'\) induce the following **complete integral homotopy and field-persistence description**.

Write \(L_{(1)}\ge\cdots\ge L_{(k)}\) for the sorted lengths and select one pair \(\{i_*,j_*\}\) realizing the largest pair sum \(L_{(1)}+L_{(2)}\). With the convention that an interval \((a,b]\) consists of the separation values \(a<r\le b\), the persistent barcodes over **every field** are
\[
\mathcal B_0=\bigl\{(0,L_{(1)}+L_{(2)}]\bigr\}\;\uplus\!
\biguplus_{\substack{1\le i<j\le k\\\{i,j\}\ne\{i_*,j_*\}}}
\bigl\{(\max\{L_i,L_j\},L_i+L_j]\bigr\},
\]
\[
\mathcal B_1=\biguplus_{j=3}^{k}(j-2)\,\bigl\{(0,L_{(j)}]\bigr\},\qquad
\mathcal B_d=\varnothing\quad(d\ge2).
\]
If the maximal pair sum is tied, any maximizing pair can be selected: all choices give the same multiset of intervals. There are no zero-length bars because every arm length is positive. The intervals ending at zero are essential on the domain \(r>0\), not assertions about a space at \(r=0\).

More concretely, put
\[
m(r)=|\{i:L_i\ge r\}|,\qquad q(r)=|\{\{i,j\}:i<j,\ L_i<r,\ L_j<r,\ L_i+L_j\ge r\}|.
\]
Then \(U_r\) is homotopy equivalent to the disjoint union of \(q(r)\) isolated points and (when \(m(r)>0\)) one connected graph of first Betti number \(\binom{m(r)-1}{2}\), with the latter interpreted as zero when \(m(r)\le 2\). Consequently, \(\beta_0(r)=q(r)+\mathbf{1}_{m(r)>0}\), \(\beta_1(r)=0\) if \(m(r)\le2\), and \(\beta_1(r)=(m(r)-1)(m(r)-2)/2\) if \(m(r)\ge3\), and integral homology is free abelian and concentrated in degrees zero and one.

## Assumptions and scope
The star is the quotient of \(\bigsqcup_i[0,L_i]\) identifying all zero endpoints. The path metric makes points on distinct arms at radii \(s,t\) have distance \(s+t\), while points on one arm have distance \(|s-t|\). The space \(U_r\) uses unordered two-element subsets with the quotient topology from ordered pairs; since \(r>0\), the coordinate swap acts freely. The filtration runs **from larger to smaller separation thresholds**. Critical equality is included because separation is \(\ge r\). Arm lengths may be repeated or incommensurable.

## Proof
**1. A fixed embedded filtered graph.** For every \(r>0\), define a graph \(H_r\subset U_r\) with a vertex \(c_{ij}=\{L_i\text{ on arm }i,L_j\text{ on arm }j\}\) whenever \(L_i+L_j\ge r\); a vertex \(a_i=\{0,L_i\text{ on arm }i\}\) whenever \(L_i\ge r\); and, for each such \(a_i\) and each \(j\ne i\), the whole path moving the point on arm \(j\) from its leaf to the common center while the point on arm \(i\) remains at its leaf. This gives exactly one edge \(c_{ij}a_i\), provided \(L_i\ge r\). It is literally an inclusion of the same geometric graph as \(r\) varies, with vertices introduced at arm sums or arm lengths.

**2. A strong deformation retract for all boundary cases.** The unordered configurations with points on distinct arms \(i,j\) form the convex (possibly lower-dimensional) polygon
\[
Q_{ij}(r)=\{(s,t):0\le s\le L_i,\ 0\le t\le L_j,\ s+t\ge r\}.
\]
Same-arm unordered configurations form the triangle
\[
T_i(r)=\{(s,t):0\le s\le t\le L_i,\ t-s\ge r\}.
\]
A nonempty \(Q_{ij}\) never contains \((0,0)\). Define \(u(s,t)=\max\{s/L_i,t/L_j\}\). At homotopy parameter \(\theta\in[0,1]\), send \((s,t)\in Q_{ij}\) to
\[
R_{\theta}(s,t)=\left((1-\theta)+\frac{\theta}{u(s,t)}\right)(s,t).
\]
Since the scalar lies between \(1\) and \(1/u\), this stays in \(Q_{ij}\); it fixes the outer boundary \(s=L_i\) or \(t=L_j\) and at \(\theta=1\) reaches that boundary. On each nonempty \(T_i\) use
\[
S_{\theta}(s,t)=((1-\theta)s,(1-\theta)t+\theta L_i).
\]
The resulting particle separation is \((1-\theta)(t-s)+\theta L_i\ge r\), and the terminal configuration is \(a_i\). At every shared boundary configuration \(\{0,t\text{ on arm }i\}\), the formulas both send its nonzero radius to \((1-\theta)t+\theta L_i\). Thus these maps glue to a continuous strong deformation retraction of \(U_r\) onto the union of the outer boundaries of the polygons and the points \(a_i\). This assertion also covers collapsed polygons and triangles at equality.

Every retained outer-boundary segment connecting \(c_{ij}\) to \(a_i\) is exactly an edge of \(H_r\). If \(L_i<r\), the outer segment pointing toward nonexistent \(a_i\) instead terminates in a free tip; its other endpoint is \(c_{ij}\). Such free terminal segments are disjoint except possibly at their \(c_{ij}\) endpoints. Collapse them linearly to those vertices while fixing \(H_r\). This is a second strong deformation retraction. In particular, all inclusion maps \(H_{r'}\hookrightarrow H_r\), \(r\le r'\), commute with the inclusions into \(U_r\). Since these inclusions are objectwise homotopy equivalences, the resulting homology persistence modules are naturally isomorphic for every coefficient group.

**3. Components and cycles.** Let \(I_r=\{i:L_i\ge r\}\) have size \(m\). Vertices \(a_i\), \(i\in I_r\), together with \(c_{ij}\) for both indices in \(I_r\), form the edge subdivision of \(K_m\). Every vertex \(c_{ij}\) with exactly one index in \(I_r\) is a pendant leaf attached to that core. Every admissible \(c_{ij}\) with neither index in \(I_r\) is isolated. This proves the asserted homotopy decomposition and the Betti formulas; a graph has no positive-degree integral torsion or higher homology.

**4. Persistent intervals.** As \(r\) decreases, each \(c_{ij}\) is born at \(L_i+L_j\) and initially forms its own component because neither endpoint arm is yet long. It first attaches to an \(a\)-vertex when \(r=\max\{L_i,L_j\}\). Once any \(a\)-vertex exists, all present \(a\)-vertices lie in a single component, since \(c_{ij}\) joins every two of them. The component born at the globally largest pair sum therefore persists to every positive \(r\), and each other pair contributes the finite interval displayed in \(\mathcal B_0\). Simultaneous events preserve this multiset: maximal-sum ties have equal attachment thresholds, and all other tied attachments merge components at their common threshold. For degree one, no cycle can die in an increasing sequence of graphs, and when the number of long arms rises to \(j\), the subdivided complete core gains exactly \(j-2\) independent cycles. Thus the degree-one interval births, counted with multiplicity, occur at \(L_{(j)}\) for \(3\le j\le k\) and persist to every positive \(r\). This proves the full interval decomposition over every field.

## Verification
The included `verify_polyhedra.py` uses exact rational coordinates to triangulate each actual unordered configuration polygon and same-arm triangle, identifies shared facets, computes exact mod-two ranks of its simplicial boundaries, and compares \((\beta_0,\beta_1,\beta_2)\) with the theorem. Running `python3 verify_polyhedra.py` returned `VERIFY_OK 7065 polygonal-mod-two-chain comparisons, k=3..8`, covering numerous rational edge lengths and critical equalities. The separate exact filtered-graph union-find check `python3 verify_barcodes.py` returned `BARCODES_OK 10000 exact filtered-graph barcode tests, k=3..12`. These finite checks are supporting tests, **not** the proof for arbitrary real lengths or infinitely many arms.

## Relationship to prior work
Li–Özaydın's 2026 paper constructs a persistent weighted-graph model and computes persistence for **ordered** two-point restricted configurations of metric stars; its vertices are explicitly ordered pairs. The explicit ordered graph in that paper is invariant under coordinate exchange and its quotient is (up to graph isomorphism) the incidence graph used here; therefore the underlying graph reduction alone is **not** claimed as new. What is established explicitly here is the **closed-form unordered degree-zero and degree-one barcode for every positive arm-length vector**, with all pair-sum and tied-endpoint events, accompanied by a direct quotient-level deformation argument. The original paper does not state this unordered barcode formula. Deeley (2011) supplied general ordered thick-particle topology and a three-arm equal-length example, not this arbitrary-length unordered interval formula. Dover–Özaydın (2013/2018) established broader parameterized ordered configuration-space structures without explicitly deriving these quotient barcodes. The result is closely related to those constructions, not a claim that the ordered results are new.

## Limitations
The theorem is restricted to **two indistinguishable** points on a metric star and to the one-parameter filtration obtained by varying only the separation threshold with lengths fixed; it does not compute genuine multiparameter interval decompositions when several lengths vary. It does not address three or more particles or general trees. It gives no new result for the ordered-space barcode. A future identification of an existing equivariant quotient calculation could subsume the statement; the source searches do not prove absence of unindexed equivalents. Computations only cover sampled finite rational instances, although the geometric proof covers every positive real vector and every threshold.

## References
1. W. Li and M. Özaydın, *Persistent Combinatorial Model of the Restricted Second Configuration Space of Metric Star Graphs*, arXiv:2603.00914v1 (first publicly submitted 2026-03-01), https://arxiv.org/html/2603.00914v1; §§1–4 and Appendix A.
2. K. Deeley, *Configuration spaces of thick particles on a metric graph*, Algebraic & Geometric Topology 11 (2011), 1861–1892, https://doi.org/10.2140/agt.2011.11.1861; especially introduction and Example 5.2. The physical particle radius in that paper is half the minimum separation used here.
3. J. Dover and M. Özaydın, *Homeomorphism and homotopy types of restricted configuration spaces of metric graphs*, arXiv:1301.5693 (2013), https://arxiv.org/abs/1301.5693.
4. W. Li, *Persistent Homology of Configuration Spaces of Trees*, arXiv:2310.05303 (2023), https://arxiv.org/abs/2310.05303.
