# Independent resolving bases of clique-path Cartesian graphs

## Finding

Let \(H_{L,q}=P_L\square K_q\), with integer \(L,q\ge 2\). An *independent resolving set* is a vertex subset whose elements are pairwise nonadjacent and whose graph-distance vectors distinguish every pair of vertices. Its smallest possible cardinality is the *independent metric dimension* \(\operatorname{idim}(H_{L,q})\); the parameter is undefined when no such subset exists. For labeled vertices \((i,c)\), where \(0\le i<L\) and \(1\le c\le q\), the complete existence, minimum-size, and minimum-basis classification is as follows.

1. If \(q=2\), such sets exist exactly when \(L\ge3\). Then \(\operatorname{idim}(H_{L,2})=2\), with precisely two bases: \(\{(0,c),(L-1,c)\}\) for either color \(c\).
2. If \(q=3\), such sets exist exactly when \(L\ge3\). Then \(\operatorname{idim}(H_{L,3})=3\). Every basis chooses three distinct path positions \(i<j<k\), with the three colors either all distinct or of the form \((a,b,a)\), where \(a\ne b\). The number of bases is \(12\binom{L}{3}\).
3. If \(q\ge4\), such sets exist exactly when \(L\ge q-1\). Then \(\operatorname{idim}(H_{L,q})=q-1\). Every basis chooses \(q-1\) distinct path positions, assigns distinct colors to these positions, and omits exactly one color. The number of bases is \(q!\binom{L}{q-1}\).

In particular, although the ordinary metric dimension of \(H_{L,q}\) equals \(q-1\) for \(q\ge3\), the independent metric dimension has an exceptional one-landmark penalty at \(q=3\), and independent resolving sets cease to exist entirely when the path is too short.

## Assumptions and scope

All graphs are finite, simple, undirected and connected. The path \(P_L\) has ordered vertices \(0,\ldots,L-1\), and the complete graph \(K_q\) has labeled colors \(1,\ldots,q\). Vertices \((i,c)\) and \((j,d)\) are adjacent if \(i=j\) and \(c\ne d\), or if \(|i-j|=1\) and \(c=d\). Different choices of vertex labels produce distinct bases as counted above. A basis is a minimum-cardinality independent resolving set, not an inclusion-minimal resolving set of arbitrary cardinality. The theorem covers **every** integer pair \(L,q\ge2\).

## Proof

**Distance and projection.** The Cartesian distance is
\[
d((i,c),(t,a))=|i-t|+\mathbf1_{\{c\ne a\}}.
\]
An independent set contains at most one vertex from each path position, because each fixed-position fiber is a clique. If two colors are absent from a resolving set, vertices of those colors in the same fiber have identical distance vectors. Hence any resolving set represents at least \(q-1\) distinct colors. In particular \(q\ge4\) requires at least \(q-1\) landmarks at distinct positions, so \(L\ge q-1\) is necessary. For \(q=3\), at least two colors are needed.

For fixed positions \(i,j\), introduce
\[
f_{i,j}(t)=|i-t|-|j-t|.
\]
Equality of the distances from \((i,c)\) and \((j,d)\) to a landmark \((t,a)\) is equivalent to
\[
f_{i,j}(t)=\mathbf1_{\{d\ne a\}}-\mathbf1_{\{c\ne a\}}.
\]
Two elementary properties will be used: \(f_{i,j}(t)\equiv i-j\pmod2\) for every integer \(t\); and \(f_{i,j}\) is monotone as a function of \(t\) (nondecreasing if \(i<j\), nonincreasing if \(i>j\)). Moreover \(f_{i,j}(s)=f_{i,j}(t)=0\) at two distinct positions \(s<t\) forces \(i=j\), since a point on a line is determined by its distances to two distinct points.

**At least four colors.** Take any \(q-1\) distinct positions and inject any \(q-1\) colors. The chosen vertices are independent: neither their positions nor their colors repeat. Suppose \((i,c)\) and \((j,d)\) have the same distance vector. If \(c=d\), two distinct landmark positions force \(i=j\). If \(c\ne d\), at least one of these two colors is represented because only one color was omitted; its landmark requires \(f_{i,j}(t)=\pm1\). At least one other landmark color differs from both \(c\) and \(d\), because \(q-1\ge3\); that landmark requires \(f_{i,j}(s)=0\). These conclusions contradict the common parity of \(f_{i,j}(s)\) and \(f_{i,j}(t)\). Thus every injection resolves. Conversely any basis has \(q-1\) vertices, and the projection lower bound forces its colors to be all distinct, with distinct positions by independence. This proves the classification and count \(\binom{L}{q-1}\cdot q!\).

**Three colors.** No two landmarks resolve. Indeed the projection bound forces the two landmark colors to be different. Independence forces their positions to be different, say \((s,a),(t,b)\) with \(s<t\). Then the distinct vertices \((s+1,a)\) and \((s,b)\) have equal distances to both landmarks: their distances are respectively \(1\) and \(t-s\) to the displayed landmark pair. Thus at least three landmarks are necessary and \(L\ge3\). For any three distinct positions \(s<t<u\), an assignment of three distinct colors resolves by the same parity argument as above: for two different vertex colors, a landmark of one of them gives \(\pm1\) and the third, neutral color gives \(0\). For the two-color pattern \((a,b,a)\), compare any two vertices with equal distance vectors. Equal vertex colors are separated by two distinct landmark positions. If one vertex color is the omitted third color, a represented-color landmark and a neutral-color landmark again contradict parity. If the colors are \(a\) and \(b\), the landmarks at \(s,u\) require the same signed value \(\pm1\) for \(f_{i,j}\), whereas the landmark at the intermediate position \(t\) requires the opposite signed value. This contradicts monotonicity of \(f_{i,j}\). Therefore both patterns resolve. There are \(3!=6\) all-distinct patterns and \(3\cdot2=6\) alternating two-color patterns per position triple. No other color pattern resolves: one-color patterns omit two colors; a two-color pattern with its repeated color in adjacent positions of the ordered triple has all landmarks of one color strictly before all landmarks of the other. If the last position with color \(a\) is \(s_0\) and the first position with color \(b\) is \(t_0>s_0\), the pair \((s_0+1,a),(s_0,b)\) has equal distances to all landmarks. This proves the full classification and \(12\binom L3\) count.

**Two colors.** The product \(H_{L,2}\) has no one-vertex resolving set: any single landmark has two distinct neighbors at distance one when \(L\ge2\). An independent two-element set must use distinct positions \(s<t\). If its colors differ, the same collision pair \((s+1,a),(s,b)\) defeats resolving. Thus both landmarks have the same color \(a\). If \(s>0\), the distinct vertices \((s-1,a),(s,b)\) have equal distances to both same-color landmarks; if \(t<L-1\), use \((t+1,a),(t,b)\) instead. Hence only \(s=0,t=L-1\) is possible. Conversely with landmarks at these endpoints in color \(a\), equality of two distance vectors for same-colored vertices forces equality of the positions. For different colors, equality would require \(f_{i,j}(0)=f_{i,j}(L-1)=\pm1\), impossible because these two values are \(i-j\) and \(j-i\), respectively. Therefore both endpoint choices resolve, are independent exactly for \(L\ge3\), and give precisely two bases. When \(L=2\), no independent resolving set of higher size exists because independence permits at most two landmarks.

## Verification

Execute `python3 verify_independent_clique_path.py` with Python 3. The standalone script constructs adjacency lists from the graph definition, computes all-pairs shortest-path distances with BFS, enumerates all independent landmark sets up to the minimum feasible size (or all feasible sizes in no-solution instances), and compares the discovered dimensions and numbers of bases against the formulas. The test suite covers \(28\) graphs with \(2\le q\le6\) and \(2\le L\le8\) (the upper length varies with \(q\)). It evaluated \(72{,}202\) independent landmark sets. All \(28\) instances passed. This finite check is supplementary to the preceding infinite proof.

## Relationship to prior work

Chartrand, Saenpholphat and Zhang introduced the general independent resolving number and studied existence and realizations, without the clique–path Cartesian family. Cáceres, Hernando, Mora, Pelayo, Puertas, Seara and Wood proved the Cartesian projection lemma and the ordinary metric-dimension equality \(\dim(K_q\square P_L)=q-1\) for \(q\ge3\); their results do not classify independent resolving sets or count independent bases. Suganya and Arumugam studied the existence of independent resolving sets for Cartesian grids and path–cycle products, among others, but do not give the present clique–path classification in their inspected paper. The theorem here supplies the independence feasibility boundary, the exceptional \(K_3\) penalty, and all independent minimum bases rather than reproving those ordinary metric dimensions.

## Limitations

No claim is made about all independent resolving subsets of nonminimum cardinality, about Cartesian products with noncomplete fibers, or about independently audited novelty. The finite verifier covers only the stated test instances; the general result is justified by the analytic proof. A differently formulated equivalent prior classification could remain undetected despite targeted literature and mathematical-record searches.

## References

1. J. Cáceres, C. Hernando, M. Mora, I. M. Pelayo, M. L. Puertas, C. Seara and D. R. Wood, *On the Metric Dimension of Cartesian Products of Graphs*, SIAM J. Discrete Math. **21** (2007), 423–441; arXiv:math/0507527, DOI:10.1137/050641867. (Especially Lemma 3.1 and the complete-graph/path sections.)
2. G. Chartrand, V. Saenpholphat and P. Zhang, *The independent resolving number of a graph*, Mathematica Bohemica **128** (2003), 379–393, DOI:10.21136/MB.2003.134003. (Definition and general existence/realization results.)
3. B. Suganya and S. Arumugam, *Independent resolving sets in graphs*, AKCE International Journal of Graphs and Combinatorics **18** (2021), 106–109. Published online 2021-08-11, DOI:10.1080/09728600.2021.1963643. (Especially Section 3.)
