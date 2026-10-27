# A complete two-link resistance-interdiction hierarchy for clique windmills

## Finding

Write \(W_{t,m}=K_1\vee(tK_m)\) for the unweighted clique windmill formed from \(t\ge2\) copies of \(K_{m+1}\), \(m\ge3\), by identifying their hub vertices \(o\). Call the \(t\) cliques *blades*. Each blade has \(m\) nonhub vertices. A *spoke* joins \(o\) to a nonhub vertex, and a *rim edge* joins two nonhub vertices in the same blade. Define the Kirchhoff index \(\operatorname{Kf}(H)=\sum_{\{u,v\}\subseteq V(H)}R_H(u,v)\), where edges have unit electrical conductance and \(R_H\) is effective resistance. For every set \(F\) of two distinct existing edges, define its interdiction damage \(\Delta(F)=\operatorname{Kf}(W_{t,m}-F)-\operatorname{Kf}(W_{t,m})\). Every such deletion leaves the graph connected.

Set
\[
 s=\frac{m^2(t-1)+3mt-m+2}{m^2-1},\qquad
 r=\frac{2(mt+1)}{m^2-1},
\]
\[
 I_{SS}=\frac{2(m+1)(m(t-1)+1)}{m(m-2)(m-1)},\quad
 I_{SR}=\frac{3mt-m+2}{m(m-2)(m-1)},\quad
 I_{RR}=\frac{2(mt+1)}{m(m-2)(m-1)}.
\]
The single-edge damages of a spoke and a rim edge are respectively \(s\) and \(r\). All two-edge damage values are exactly the following six expressions:

| Type | Deleted-edge geometry | Exact \(\Delta(F)\) |
|---|---|---|
| \(SS_+\) | Two spokes in the **same** blade | \(2s+I_{SS}\) |
| \(SR_+\) | A spoke and a rim edge sharing a nonhub vertex in the same blade | \(s+r+I_{SR}\) |
| \(RR_+\) | Two rim edges sharing a nonhub vertex in the same blade | \(2r+I_{RR}\) |
| \(SS_0\) | Two spokes from **different** blades | \(2s\) |
| \(SR_0\) | One spoke and one rim edge either from different blades or disjoint within one blade | \(s+r\) |
| \(RR_0\) | Two rim edges either from different blades or disjoint within one blade | \(2r\) |

The disjoint-rim configuration in a single blade exists only for \(m\ge4\); the \(RR_0\) type still exists for \(m=3\) because \(t\ge2\).

**Complete strict ranking.** If \(m=3\) and \(t=2,3\),
\[
 SS_+>SR_+>SS_0>RR_+>SR_0>RR_0.
\]
If \(m=3\) and \(t\ge4\),
\[
 SS_+>SR_+>SS_0>SR_0>RR_+>RR_0.
\]
If \(m\ge4\),
\[
 SS_+>SS_0>SR_+>SR_0>RR_+>RR_0.
\]
Here each symbol in an inequality denotes its damage, not a graph or edge set. Thus the **unique maximizing structural type**, for every \(t\ge2,m\ge3\), consists of two spokes within one blade. Exactly \(t\binom m2\) unordered deletion pairs maximize damage. The unique runner-up type is \(SR_+\) for \(m=3\), numbering \(tm(m-1)\) pairs, and \(SS_0\) for \(m\ge4\), numbering \(\binom t2m^2\) pairs.

**Failure interaction.** For distinct edges \(e,f\), set \(\mathcal I(e,f)=\Delta(\{e,f\})-\Delta(\{e\})-\Delta(\{f\})\), where singleton damage is defined analogously. This interaction is strictly positive **exactly when** the edges are incident *within the same blade*, and is zero otherwise. In particular, two spokes from different blades share the global hub but have **zero interaction**. Their effect is exactly the sum of their isolated effects.

## Assumptions and scope

All graphs are finite, simple and undirected. Parameters \(t,m\) are integers with \(t\ge2\), \(m\ge3\). All edges have conductance one; there are no vertex failures, conductance changes, or cascading dynamics. The damage is the absolute unnormalized increase of the all-unordered-pairs Kirchhoff index. The optimization ranges over **all** \(\binom{|E(W_{t,m})|}{2}\) unordered pairs of *distinct* edges, where \(|E(W_{t,m})|=tm(m+1)/2\). A blade contains its hub, so two spokes from different blades share the hub but are assigned to different blades. No claims are made for triangular blades \(m=2\), because deleting two incident edges from \(K_3\) can disconnect a blade vertex.

## Proof

**1. Cut-vertex reduction.** Let \(B_i\cong K_{m+1}\) be the \(i\)th blade. Since distinct blades meet only at the hub \(o\), effective resistances within one blade equal those computed in that blade alone; for \(x\in B_i-o\), \(y\in B_j-o\), \(i\ne j\),
\[
 R(x,y)=R_{B_i}(x,o)+R_{B_j}(o,y).
\]
This remains true after deleting at most two edges, since every \(K_{m+1}\) with \(m\ge3\) remains connected after two edge deletions (its edge connectivity is \(m\)). Consequently
\[
 \operatorname{Kf}(W_{t,m}-F)
 =\sum_{i=1}^t\left[
 \sum_{\{u,v\}\subseteq B_i}R_{B_i-F_i}(u,v)
 +(t-1)m\sum_{u\in B_i-o}R_{B_i-F_i}(u,o)
 \right],
\]
with \(F_i=F\cap E(B_i)\). Different blades therefore contribute **additively** to the total damage.

**2. Exact one- and two-edge losses inside a blade.** Put \(b=m+1\), \(c=(t-1)m\), and let \(S\) denote the hub-centered star on the \(b\) blade vertices. The weighted Laplacian representing the bracketed objective is
\[
 W=L(K_b)+cL(S).
\]
Orient the deleted edges and assemble their incidence vectors as columns of a matrix \(B\), with \(G=B^{\mathsf T}B\). On the orthogonal complement of the constant vector, \(L(K_b)=bI\). The rank-\(|F_i|\) inverse identity gives the **exact** blade loss
\[
 \Delta_i(F_i)=\frac{1}{b^2}\operatorname{tr}\!\left[
 (I-G/b)^{-1}B^{\mathsf T}WB
 \right].
\]
All inverses exist: two edge removals preserve connectivity.

For a spoke incidence vector \(z\), \(z^{\mathsf T}L(S)z=m+3\); for a rim-edge incidence vector it is \(2\). Hence a single spoke and single rim edge respectively yield \(s\) and \(r\) as above. For two same-blade incident spokes, orient both from the hub; their incidence inner product is \(1\), and their star-form cross product is \(m+2\). For an incident spoke/rim pair or incident rim/rim pair, choose orientation so both incidence and star-form cross products are \(1\). In all three cases \(G=\bigl(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\bigr)\), giving the three displayed positive interactions \(I_{SS},I_{SR},I_{RR}\). For two nonincident edges in the same blade, both cross products vanish, and the damage is the sum of the single-edge losses. For edges from different blades it is also additive by Step 1. This proves all six formulas and the interaction theorem.

**3. Exhaustion of edge-pair types.** Every edge is either a spoke or a rim edge. If both lie in the same blade, the only alternatives are their three type combinations and adjacency/nonadjacency (two same-blade spokes are always incident); otherwise their blade losses add. These possibilities are exhaustive. The numbers of the eight more finely distinguished orbit classes are \(t\binom m2\) (same-blade spoke/spoke), \(\binom t2m^2\) (cross-blade spoke/spoke), \(tm(m-1)\) (same-blade incident spoke/rim), \(tm\binom{m-1}{2}\) (same-blade disjoint spoke/rim), \(t(t-1)m\binom m2\) (cross-blade spoke/rim), \(tm\binom{m-1}{2}\) (same-blade incident rim/rim), \(3t\binom m4\) (same-blade disjoint rim/rim), and \(\binom t2\binom m2^2\) (cross-blade rim/rim), respectively. Their sum is \(\binom{tm(m+1)/2}{2}\), verifying no edge pairs are omitted.

**4. Strict ranking.** Write the damage expressions as their type labels. All denominators below are strictly positive in the stated range. The following exact differences settle the adjacent comparisons:
\[
\begin{aligned}
 SS_+-SR_+&=\frac{(m+1)(t-1)}{m-2},\\
 SS_+-SS_0&=I_{SS},\\
 SR_+-SS_0&=-\frac{(m+1)(m(m-3)(t-1)-2)}{m(m-2)(m-1)},\\
 SR_+-SR_0&=I_{SR},\\
 SS_0-SR_0&=\frac{m(t-1)}{m-1},\\
 SR_0-RR_+&=\frac{m(m^2-2m-2)(t-1)-2m-2}{m(m-2)(m-1)},\\
 RR_+-RR_0&=I_{RR},\\
 SR_0-RR_0&=\frac{m(t-1)}{m-1}.
\end{aligned}
\]
The third difference is positive exactly for \(m=3\); it is negative for \(m\ge4\), because then \(m(m-3)(t-1)\ge4>2\). The numerator in the sixth difference is \(3t-11\) when \(m=3\), so changes sign between \(t=3\) and \(t=4\) without an integer tie. When \(m\ge4\), this numerator is already \(14\) at \((m,t)=(4,2)\) and increases strictly in both variables: its partial derivatives are \((3m^2-4m-2)(t-1)-2>0\) and \(m(m^2-2m-2)>0\). All remaining displayed differences are positive. This proves the complete three-case ranking. The maximizing and runner-up pair counts follow from Step 3. \(\square\)

## Verification

The accompanying `verify_windmill.py` derives the six damages symbolically from the rank-two formula, tests the equality of the disjoint and cross-blade cases, verifies all eight rational comparison identities and their parameter-boundary signs, and independently computes the Kirchhoff index from direct exact inverses of the **full** hub-grounded graph Laplacian. It compares 57 exact direct-inverse values against the symbolic expressions on parameter cases \((m,t)=(3,2),(3,3),(3,4),(4,2),(4,3),(5,2)\). It prints `VERIFY_OK 57 independent exact grounded inverse comparisons, symbolic sign factorizations`. Run `python -m pip install -r requirements.txt` if SymPy is not already installed, then `python verify_windmill.py`. The symbolic computations support but do not replace the general mathematical proof in Steps 1–4.

## Relationship to prior work

Koç, Warnier, Kooij and Brazier (2013, arXiv:1312.6606, Section V) motivate electrical effective-graph-resistance changes as a structural line-vulnerability measure and assess single outages on a power-grid example; their inspected full text does not classify two-link damage on windmills. Sardar and Xu (published online 4 July 2024, DOI 10.2174/0115701794299562240606054510) study resistance distances and Kirchhoff indices of windmill graphs themselves; only their public abstract and bibliographic sections were accessible, not the complete paper, leaving an explicit coverage risk.

Tamura (6 August 2026, arXiv:2608.05924, Sections 3–7) gives general edge-defect formulas for complete graphs with deleted edges. Those formulas are substantially relevant to the within-blade calculation; its inspected statements do not give the **global weighted hub-to-leaf objective**, the cross-blade additivity/zero-interaction distinction, the full six-level windmill interdiction ordering, or its sharp runner-up transition. Combining a general complete-graph resolvent with the cut-vertex decomposition enables derivation of the present formulas, but the ranking and maximizing geometry require the separate rational comparisons in Step 4. The general algorithmic ability to compute each case is acknowledged rather than presented as an unprecedented matrix method.

## Limitations

The theorem concerns unit conductances, equal complete blades, exactly two edge failures, and absolute Kirchhoff-index damage. It does not cover heterogeneous blades, weighted spokes, larger deletion sets, edge-disjoint survivability under more than two deletions, or power-grid cascading dynamics. A plausible specialized full-text source on windmill resistances could not be inspected and remains an originality risk; absence of a covering match in accessible searches is not a proof of historical uniqueness. The work provides a complete optimization classification for the specified family, not a claim that the rank-two inverse method is new.

## References

1. Y. Koç, M. Warnier, R. E. Kooij, and F. M. T. Brazier, *Structural Vulnerability Assessment of Electric Power Grids*, arXiv:1312.6606v1 (first public: 2013-12-19). https://arxiv.org/html/1312.6606v1
2. M. S. Sardar and S.-J. Xu, *Resistance Distance and Kirchhoff Index in Windmill Graphs*, *Current Organic Synthesis* 22 (2025), 159–168 (online 2024-07-04), DOI:10.2174/0115701794299562240606054510. https://doi.org/10.2174/0115701794299562240606054510
3. S. Tamura, *Edge-defect matrices and stability of the Kirchhoff index for complete graphs with deleted edges*, arXiv:2608.05924 (2026-08-06). https://arxiv.org/abs/2608.05924
