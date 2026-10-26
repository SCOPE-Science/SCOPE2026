# The matching-saturation jump and extremizer restoration for balanced bipartite cut–cycle projections

## Finding

For every integer \(s\ge3\) and \(0\le t\le s\), form \(G_{s,t}\) from the unweighted complete bipartite graph \(K_{s,s}\) by deleting \(t\) edges of a matching. Give every surviving edge the orientation from the first to the second vertex class. On the real edge-coordinate space, let \(Q_{s,t}\) be the Euclidean-orthogonal projection onto the cut space, and let \(P_{s,t}=I-Q_{s,t}\) be the projection onto the cycle space.

Put
\[
 H=s(s-2),\qquad T_{s,t}=s(s-2)+t,\qquad
 R_{s,t}=\frac{2s-1}{s^2}+\frac{t}{s^2 T_{s,t}}.
\]
For all \(0\le t<s\), the exact induced real endpoint norms are
\[
 \boxed{\|Q_{s,t}\|_{1\to1}=\|Q_{s,t}\|_{\infty\to\infty}=3-2R_{s,t}},
 \qquad
 \boxed{\|P_{s,t}\|_{1\to1}=\|P_{s,t}\|_{\infty\to\infty}=4-4R_{s,t}}.
\]
When \(1\le t<s\), **the maximizing columns for both projections are exactly the \((s-t)^2\) edges with neither endpoint incident to the deleted matching**. At \(t=0\) every one of the \(s^2\) columns maximizes both norms. When the matching becomes perfect, \(t=s\), every surviving column maximizes both norms and
\[
 \boxed{\|Q_{s,s}\|=3-\frac4s},\qquad
 \boxed{\|P_{s,s}\|=4-\frac{8s-6}{s(s-1)}}.
\]
Consequently, deleting successive matching edges **strictly decreases both endpoint norms throughout the entire deletion chain**, including the final deletion, but the last step has a larger asymptotic effect. In detail,
\[
 \begin{aligned}
 \|Q_{s,s-1}\|-\|Q_{s,s}\|&=\frac{2(s-2)}{s(s^2-s-1)},\\
 \|P_{s,s-1}\|-\|P_{s,s}\|&=\frac{2(3s^2-7s+3)}{s(s-1)(s^2-s-1)}.
 \end{aligned}
\]
These final-step deficits are respectively \(2s^{-2}+O(s^{-3})\) and \(6s^{-2}+O(s^{-3})\); all preceding deletions together change the norms by only \(O(s^{-3})\). The maximizing-edge count jumps from one at \(t=s-1\) to \(s(s-1)\) at \(t=s\).

There is also a sharp transfer-current sign transition. With the common bipartite edge orientation, every pair of disjoint surviving edges in \(K_{s,s}\) has a negative transfer-current entry. After a matching of size \(t\ge2\) is deleted, certain disjoint edge pairs instead have **strictly positive** entries, with exact values specified below. No such positive disjoint entry exists at \(t=0\) or \(t=1\).

## Assumptions and scope

The graph is finite, simple, connected and unweighted. Its two vertex classes are \(A_1,\ldots,A_s\) and \(B_1,\ldots,B_s\); precisely the edges \(A_iB_i\) for \(1\le i\le t\) are absent. This choice entails no loss of generality because all matchings of the same size are equivalent under graph automorphisms of \(K_{s,s}\). The endpoint norms refer only to the **canonical Euclidean-orthogonal** projections measured in real edge \(\ell_1\) or edge \(\ell_\infty\), not to infima over all projections.

Let \(D\) be the oriented vertex-by-edge incidence matrix and \(L=DD^{\mathsf T}\) the graph Laplacian. Then \(Q=D^{\mathsf T}L^+D\) and \(P=I-Q\), where \(L^+\) denotes the Moore–Penrose inverse. Since \(Q\) and \(P\) are real symmetric, their induced \(\ell_1\) and \(\ell_\infty\) norms coincide and equal their largest absolute column sums. For the electrical discussion use the source orientation \(A_p\to B_q\); reversing an arbitrary edge's reference orientation changes signs in a row and column but not the absolute sums.

## Proof

**1. A finite-rank Laplacian resolvent.** Let \(L_0\) be the Laplacian of \(K_{s,s}\) and \(b_i=e_{A_i}-e_{B_i}\) the incidence vector of the \(i\)-th deleted edge. With \(B=[b_1\ \cdots\ b_t]\), we have \(L=L_0-BB^{\mathsf T}\). On the zero-sum vertex subspace, the standard complete-bipartite resolvent gives
\[
 b_i^{\mathsf T}L_0^+b_j=\frac2s\,\mathbf1_{i=j}-\frac1{s^2}.
\]
Thus
\[
 I_t-B^{\mathsf T}L_0^+B=\frac H{s^2}I_t+\frac1{s^2}\mathbf1\mathbf1^{\mathsf T}>0,
\quad
 (I_t-B^{\mathsf T}L_0^+B)^{-1}
 =\frac{s^2}{H}\left(I_t-\frac{\mathbf1\mathbf1^{\mathsf T}}{T_{s,t}}\right).
\]
The positive definiteness, valid for \(s\ge3\), justifies the inverse update on the zero-sum subspace and confirms that no deletion in the stated range disconnects the graph. For an existing edge \(e=A_pB_q\), set
\[
 z_i(e)=s(\mathbf1_{p=i}+\mathbf1_{q=i})-1\quad(1\le i\le t).
\]
The transfer-current matrix of \(G_{s,t}\) consequently satisfies, for existing edges \(e=A_pB_q\) and \(f=A_aB_b\),
\[
 \boxed{
 Q_{fe}=\frac{\mathbf1_{a=p}+\mathbf1_{b=q}}s-\frac1{s^2}
 +\frac{\displaystyle\sum_{i=1}^t z_i(f)z_i(e)
 -\displaystyle\frac{(\sum_i z_i(f))(\sum_i z_i(e))}{T_{s,t}}}{H s^2}.}
 \tag{1}
\]
Here sums over an empty set vanish, so the formula also covers \(t=0\).

**2. Signs of disjoint transfer currents.** Write \(U_e=s(\mathbf1_{p\le t}+\mathbf1_{q\le t})\), with analogous \(U_f\), and let \(k\in\{0,1,2\}\) count the reciprocal matched-label coincidences \(a=q\le t\) and \(b=p\le t\) between **disjoint** edges \(e,f\). Expanding (1) gives
\[
 \boxed{
 Q_{fe}=\frac{k s^2T_{s,t}-H(H+U_e+U_f)-U_eU_f}
 {H s^2T_{s,t}}.}
 \tag{2}
\]
When \(k=0\), this is strictly negative. A pair of disjoint edges with \(k=1\) has one of the following values, according to matched-endpoint membership: \((t-2s)/(HT_{s,t})\) for two doubly matched edges, \((t-s)/(HT_{s,t})\) for a doubly and a singly matched edge, and \((t-1)/(HT_{s,t})\) for opposing singly matched edge types. All values are nonpositive except the last, which is strictly positive precisely when \(t\ge2\). When \(k=2\), necessarily \(e=A_iB_j\), \(f=A_jB_i\) for distinct matched indices \(i,j\le t\), and
\[
 Q_{fe}=\frac{s^2-4s+2t}{HT_{s,t}}>0.
\]
Indeed \(s^2-4s+2t=(s-2)^2+2t-4\), which is at least \((s-2)^2>0\) for all \(s\ge3\), \(t\ge2\). These alternatives exhaust all disjoint surviving edge pairs; in particular they prove the claimed current-sign threshold.

**3. Absolute column sums.** For an edge \(e\), let \(r_e=Q_{ee}\), its effective resistance. The unit current injected at \(A_p\) and removed at \(B_q\) has strictly highest potential at \(A_p\) and strictly lowest at \(B_q\), by the discrete maximum principle. Hence all edge currents incident to either terminal are strictly positive with the chosen bipartite orientation. Kirchhoff conservation gives a sum of \(1\) for currents incident to each terminal, and a sum of \(1\) for all oriented edge currents. The sum of positive currents incident to either terminal is therefore \(2-r_e\).

Let \(E_e\) be the sum of the additional positive currents on edges disjoint from \(e\). By the preceding sign classification, these extras are explicit. Classify an existing edge by \(\mathrm{MM}\) if both its endpoint labels are matched, \(\mathrm{MU}\) or \(\mathrm{UM}\) if exactly one is matched, and \(\mathrm{UU}\) if neither is matched. For \(\mathrm{MM}\), there is one positive reverse edge; for \(\mathrm{MU}\) and \(\mathrm{UM}\), there are \(s-t\) positive disjoint edges when \(t\ge2\); for \(\mathrm{UU}\), there are none. In symbols,
\[
 E_{\mathrm{MM}}=\frac{s^2-4s+2t}{HT_{s,t}},\qquad
 E_{\mathrm{MU}}=E_{\mathrm{UM}}=\frac{(s-t)(t-1)}{HT_{s,t}},\qquad E_{\mathrm{UU}}=0.
 \tag{3}
\]
Only types that actually occur in the graph are used. Note that \(\mathrm{MM}\) occurs only when \(t\ge2\); the other formulae remain valid at \(t=0,1\) whenever their types occur. Since the algebraic sum of all currents is \(1\), the absolute cut-column sum is
\[
 c_e=2(2-r_e+E_e)-1=3-2r_e+2E_e.
\]
The diagonal of \(P\) at \(e\) equals \(1-r_e\ge0\), so its absolute column sum is
\[
 p_e=(1-r_e)+\sum_{f\ne e}|Q_{fe}|=c_e+1-2r_e=4-4r_e+2E_e.
 \tag{4}
\]
For direct substitution in (3)–(4), let \(a=\mathbf1_{p\le t}\), \(b=\mathbf1_{q\le t}\), and \(U=s(a+b)\). Taking \(f=e\) in (1) yields the exact resistance
\[
 \boxed{
 r_e=\frac{2s-1}{s^2}
 +\frac{t-2U+s^2(a+b)-(U-t)^2/T_{s,t}}{Hs^2}.}
 \tag{5}
\]
This determines every orbit's absolute column sums by elementary rational expressions, without assuming transitivity on all surviving edges.

**4. Maximizing columns while the matching is incomplete.** For \(t<s\), the \(\mathrm{UU}\) type exists and (5) becomes \(r_{\mathrm{UU}}=R_{s,t}\), with \(E_{\mathrm{UU}}=0\). Equations (3)–(5) imply the following four exact comparisons, with \(T=T_{s,t}\):
\[
 \begin{aligned}
 c_{\mathrm{UU}}-c_{\mathrm{MM}}&=\frac{2(s-2)}{sT},\\
 p_{\mathrm{UU}}-p_{\mathrm{MM}}&=\frac{2(3s^2-12s+2t+8)}{s(s-2)T},\\
 c_{\mathrm{UU}}-c_{\mathrm{MU}}&=\frac{2(s^2-st-3s+t^2+3)}{s(s-2)T},\\
 p_{\mathrm{UU}}-p_{\mathrm{MU}}&=\frac{2(2s^2-st-7s+t^2+t+6)}{s(s-2)T}.
 \end{aligned}
 \tag{6}
\]
The \(\mathrm{UM}\) comparisons equal the \(\mathrm{MU}\) comparisons by symmetry. For \(s\ge3\) and \(1\le t<s\), all applicable differences are strictly positive: the first is manifestly positive; the second numerator is \(3(s-2)^2+2t-4>0\) when \(\mathrm{MM}\) exists, so \(t\ge2\); the third numerator equals \((t-s/2)^2+3(s-2)^2/4>0\); and the fourth numerator equals
\[
 \left(t-\frac{s-1}{2}\right)^2+\frac{7s^2-26s+23}{4}>0,
\]
where the last quadratic is positive for all \(s\ge3\). Thus the \(\mathrm{UU}\) edges, and only those edges, maximize both projections until saturation. For \(t=0\), the graph is edge-transitive and every column realizes the same norms.

**5. Saturation and strict monotonicity.** At \(t=s\), the graph is the crown graph; its surviving edges are all of type \(\mathrm{MM}\), and simultaneous label permutations act transitively on them. The trace identity \(\sum_e Q_{ee}=2s-1\) yields \(r_e=(2s-1)/[s(s-1)]\). Its only positive disjoint current is the reverse-edge entry \(1/[s(s-1)]\). Substitution into (4) proves the stated full-matching norms.

For \(0\le t<s\), the function \(t/T_{s,t}=t/[s(s-2)+t]\) strictly increases with \(t\); hence both expressions in the finding strictly decrease at every nonsaturating step. Subtracting the saturated values from the values at \(t=s-1\) gives the two displayed positive final-step deficits. Indeed \(3s^2-7s+3>0\) for all \(s\ge3\). The deficits and the \((s-t)^2\) extremizer count establish the claimed saturation jump and restoration of edge transitivity. Finally, \(t/T_{s,t}\le (s-1)/(s^2-s-1)=O(s^{-1})\) for \(t<s\), giving a uniform \(O(s^{-3})\) cumulative nonsaturating deficit; the explicit final jumps have orders \(s^{-2}\).

## Verification

The accompanying `check.py` uses only exact rational arithmetic and the Python standard library. It independently constructs grounded graph Laplacians and their inverses for all \(3\le s\le8\) and \(0\le t\le s\), checks every edge column against (1), (3)–(5), verifies the asserted maximizer classes for \(1\le t<s\), and checks the sign classification of every entry. Successful output: `MATCHING_DELETION_ENDPOINT_EXACT_OK graphs=39 columns=1370 current_entries=60990 positive_disjoint_entries=1566`.

These finite checks are corroboration, not a substitute for the unrestricted proof in sections 1–5. In particular, all universal assertions rely on the explicit inverse, current-sign case analysis and positive polynomial comparisons, not on extrapolation from \(s\le8\).

## Relationship to prior work

The graph-projection framework and connection to transportation cost spaces follow Dilworth–Kutzarova–Ostrovskii [1]. Their primary calculations concern discrete tori and Hamming graphs. The general transfer-current interpretation used here is standard in electrical networks and random spanning-tree theory [2]. Neither of these works supplies the stated matching-deletion norm interpolation or its maximizing-edge classification. Existing boundary calculations for one deleted edge and a fully deleted matching provide useful comparison values; the new content is the complete nonsaturating matching trajectory, exact signed off-diagonal structure, and the jump and restoration at saturation. General inverse-update identities alone do not determine the signs needed to evaluate absolute operator norms.

## Limitations

The theorem is restricted to **balanced** complete bipartite graphs with the deleted edges forming a matching, unit conductances, canonical Euclidean-orthogonal projections and real endpoint edge norms. The proof makes no claim about arbitrary nonorthogonal projections, general edge-deletion patterns, unbalanced bicliques, edge weights or intermediate \(\ell_p\) norms. The exact formulas do not by themselves classify random spanning-tree correlations beyond the transfer-current entries that are explicitly computed. Publication novelty is not guaranteed by a finite literature search.

## References

[1] S. J. Dilworth, D. Kutzarova and M. I. Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, arXiv:2305.12582 (first public version 21 May 2023), https://arxiv.org/abs/2305.12582.

[2] A. Kassel and W. Wu, *Transfer current and pattern fields in spanning trees*, arXiv:1312.2946, https://arxiv.org/abs/1312.2946.
