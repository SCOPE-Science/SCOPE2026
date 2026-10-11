# Exact 1-skeleton and simple-vertex exhaustion of transitive-tournament root polytopes

## Finding
For every integer \(n\ge3\), the positive type-A root polytope
\[
P_n=\operatorname{conv}\{r_{ij}=e_i-e_j:1\le i<j\le n\}
\]
has the following complete edge criterion. Distinct vertices \(r_{ij}\) and \(r_{k\ell}\) are joined by an edge if and only if **one** of these disjoint cases applies:

1. They have a common tail \(i=k\) or a common head \(j=\ell\).
2. Their index intervals are disjoint, \(j<k\) or \(\ell<i\).
3. They are successive unit roots \(r_{a,a+1}\) and \(r_{a+1,a+2}\), for \(1\le a\le n-2\).

Put \(\widetilde P_n=\operatorname{conv}(P_n\cup\{0\})\). Its graph induced on the nonorigin vertices has precisely the edges of cases 1 and 2. Removing the origin creates **exactly** the \(n-2\) edges of case 3, a path through the unit-root vertices.

The full edge number is
\[
f_1(P_n)=2\binom n3+\binom n4+n-2,
\]
and the degree at each vertex is
\[
\deg_{P_n}(r_{ij})=(n-i-1)+(j-2)+\binom{i-1}{2}+\binom{n-j}{2}
+\mathbf1_{j=i+1}(\mathbf1_{i>1}+\mathbf1_{j<n}).
\]
The number of simple vertices is \(3\), \(2\), \(1\), and \(0\) for \(n=3\), \(n=4\), \(n=5\), and \(n\ge6\), respectively. Thus \(P_n\) is simple exactly when \(n=3\), and in dimensions at least five it has **no** simple vertices. The edge-graph diameter is \(1\) if \(n=3\), and \(2\) if \(n\ge4\).

## Assumptions and scope
Here \(n\) is any integer at least three, \(e_i\) are the standard coordinate unit vectors of \(\mathbb R^n\), and \(r_{ij}\) is defined only for \(i<j\). A polytope edge means an exposed one-dimensional face; its graph has the extreme points as vertices. All edges and distances are taken in this one-skeleton, not in the underlying tournament. A vertex of a \(d\)-polytope is *simple* when it has exactly \(d\) incident polytope edges. Binomial coefficients are zero for upper index less than two. Indicators are \(1\) if their displayed condition is true, otherwise \(0\).

Every \(r_{ij}\) is a vertex: the linear functional with coordinate values \(h_i=1\), \(h_j=-1\), and all other values zero has its unique maximum \(2\) at \(r_{ij}\). The polytope lies in \(\sum x_i=0\). It has dimension \(n-1\) because the \(n-1\) roots \(r_{1j}\) for \(2\le j\le n\), together with \(r_{23}\), have affine span of dimension \(n-1\) (equivalently, the differences of \(r_{1j}\) span dimension \(n-2\), while \(r_{23}\) is outside their affine hyperplane). The origin is an extreme point of \(\widetilde P_n\), since all roots lie strictly on one side of the linear functional \(\sum_{a=1}^n a x_a\), which evaluates to \(i-j<0\) on \(r_{ij}\) and \(0\) at the origin.

## Proof
**Exposure criterion.** Write \(s_h(i,j)=h_i-h_j\). Since every displayed root is a vertex, a pair \(\{r_{ij},r_{k\ell}\}\) forms an edge precisely when there is a real vector \(h\) such that \(s_h\) attains its maximum at exactly those two pairs. We give explicit integer exposures for all claimed edges, then rule out every remaining pair.

**Same tail or head.** If both chosen roots have tail \(i\), take \(h_i=2\), set their two heads to \(0\), and every other \(h_t=1\). Exactly the chosen two scores equal \(2\). If the selected roots share a head, assign \(2\) to their two tails, \(0\) to the common head, and \(1\) elsewhere. Again the maximum \(2\) occurs precisely twice. Since \(2>0\), these are also edges of \(\widetilde P_n\).

**Disjoint intervals.** After swapping the pair if necessary, write their endpoints \(i<j<k<\ell\). Take \(h_i=4\), \(h_j=0\), \(h_k=6\), \(h_\ell=2\), and \(h_t=3\) elsewhere. The two specified scores are \(4\). The only potential score exceeding \(4\) would be \(h_k-h_j=6\), but it is not associated with a positive root because \(k>j\). Any other positive-root score is at most \(3\). Thus the chosen pair is an edge, also after the origin is adjoined since \(4>0\).

**Consecutive unit roots.** For chosen \(r_{a,a+1}\) and \(r_{a+1,a+2}\), choose \(h_1=0\) and increments \(h_{t+1}-h_t=1\) at \(t=a,a+1\), and increments \(2\) at every other \(t\). Every score \(s_h(i,j)\) is minus the sum of the increments from \(i\) through \(j-1\). The maximum is \(-1\), attained at precisely the chosen roots. Hence they form an edge of \(P_n\).

**Exhaustion.** Two distinct positive roots either have a shared tail or head, have disjoint index intervals, form a chain \(i<j=k<\ell\) (up to swapping), or have interleaved/nested endpoints. In the latter case, after relabeling \(i<k<j\) and \(k<\ell\), the two other valid roots \(r_{i\ell},r_{kj}\) satisfy the parallelogram identity
\[
r_{ij}+r_{k\ell}=r_{i\ell}+r_{kj}.
\]
The other two roots are distinct from the selected pair. If a linear functional maximized exactly at the selected pair with common value \(T\), the two other values would be strictly smaller than \(T\), contradicting equality of their sums. Thus no such edge exists. For a chain \(r_{ij},r_{j\ell}\), the long root \(r_{i\ell}=r_{ij}+r_{j\ell}\) has score \(2T\). If \(T\ge0\) it exceeds \(T\) or ties, contradicting exact two-point exposure. Therefore \(T<0\). If either selected root has length greater than one, it splits into two positive roots. Their two scores are each at most \(T\), so the selected root's score would be at most \(2T<T\), again a contradiction. Only consecutive unit roots survive.

**Effect of adding the origin.** All edges from the first two cases have exposed score \(2\) or \(4\), strictly exceeding the origin's score zero. For successive unit roots, any exposing vector for their pair has shared score \(T<0\), as just proved: at \(T=0\), \(r_{a,a+2}\) ties; at \(T>0\), it exceeds \(T\). Thus those edges disappear in \(\widetilde P_n\). An edge of \(\widetilde P_n\) between nonorigin vertices is necessarily an edge of \(P_n\) because deleting a vertex can only remove inequality constraints on an exposure; hence these are exactly the \(n-2\) newly created edges.

**Counting and degrees.** A shared tail is determined by \(i<j<\ell\) (one triple); a shared head likewise by \(i<k<j\). Thus there are \(2\binom n3\) of the first type. Disjoint pairs correspond bijectively to ordered endpoints \(i<j<k<\ell\), giving \(\binom n4\); consecutive unit pairs contribute \(n-2\). The cases do not overlap, proving the edge formula. The root \(r_{ij}\) meets \(n-i-1\) other roots at its tail and \(j-2\) other roots at its head. Disjoint intervals to its left and right contribute \(\binom{i-1}{2}\) and \(\binom{n-j}{2}\), respectively. The unit-chain contribution is precisely \(\mathbf1_{j=i+1}(\mathbf1_{i>1}+\mathbf1_{j<n})\). This proves the degree formula.

**Simple-vertex exhaustion.** Set \(\ell=j-i\), \(a=i-1\), and \(b=n-j\); then \(a,b\ge0\), \(a+b=n-1-\ell\), and the degree becomes
\[
n+\ell-3+\binom a2+\binom b2+
\mathbf1_{\ell=1}(\mathbf1_{a>0}+\mathbf1_{b>0}).
\]
For \(\ell\ge3\) the degree is at least \(n\), strictly larger than the dimension \(n-1\). For \(\ell=2\), equality to \(n-1\) requires \(a,b\le1\). This gives one choice at \(n=3\) (namely \(a=b=0\)), two at \(n=4\), one at \(n=5\), and none for \(n\ge6\). For \(\ell=1\), the extra sum must equal one: this happens for the two unit roots at \(n=3\), and never for \(n\ge4\), where \(a+b=n-2\ge2\) forces the sum at least two. Therefore the simple-vertex counts are exactly \(3,2,1,0\) in the stated ranges.

**Graph diameter.** Any nonadjacent pair must be interleaved/nested or a nonunit chain. In both cases a third root exists sharing a tail with one chosen root and a head with the other (respectively \(r_{i\ell}\) and \(r_{i\ell}\) in the preceding notation), so their distance is exactly two. For \(n\ge4\), \(r_{13}\) and \(r_{24}\) are not adjacent, and the diameter is two. The three vertices at \(n=3\) form a triangle, giving diameter one.

## Verification
Run `python3 verify.py` from the directory containing this document. It reconstructs every candidate vertex as a coordinate root; checks unique integer exposures for all predicted edges; checks root-sum parallelogram obstructions for interleaved or nested nonedges; checks all degree, edge-number, simple-vertex and diameter formulas for every integer \(3\le n\le12\). If SciPy is installed, it also independently solves every two-vertex face-exposure feasibility linear program for \(3\le n\le8\). A reproducibility run of the checker printed `VERIFY_OK` with \(3+15+45+105+210+378=756\) independently checked feasible-or-infeasible pairs. None of these finite checks substitutes for the proof given above.

## Relationship to prior work
Numata, Takahashi and Tamaki (2022) introduce and analyze faces of directed edge polytopes for general quivers, establishing facet criteria. They do not evaluate the entire transitive-tournament one-skeleton, its edge count, local degrees or simple-vertex cutoff. Setiabrata (first arXiv version 2020) proves general face characterizations for the *origin-adjoined* positive-root polytope \(\widetilde P_n\) (in particular Corollary 5.10), not for every face of \(P_n\) after removing the origin. Our criterion recovers the classes of nonorigin edges retained under origin addition and identifies exactly the new \(n-2\) unit-chain edges. General formulas in the literature imply some of this information after specialization, so the claim is this explicit complete nonorigin graph classification and sharp simple-vertex exhaustion, not invention of the positive-root family itself.

## Limitations
This establishes the one-skeleton but does not determine all higher-dimensional faces, triangulations, or Ehrhart data. A finite checker cannot independently prove the all-dimensional classification. The full text of the older paper by Cho (1999) was not recovered here; a possible equivalent presentation in older work remains a literature risk. Neither an independent audit nor an external formal proof certificate has been performed.

## References
- Y. Numata, Y. Takahashi, D. Tamaki, *Faces of Directed Edge Polytopes*, arXiv:2203.14521v1, posted 2022-03-28, primary MSC 52B05. https://arxiv.org/pdf/2203.14521
- L. Setiabrata, *Faces of Root Polytopes*, arXiv:2001.05191, first version posted 2020-01-15. https://arxiv.org/pdf/2001.05191 (especially Corollary 5.10 and Remark 5.11).
- S. Cho, *Polytopes of Roots of Type A*, Bulletin of the Australian Mathematical Society 59 (1999), 391–402. https://doi.org/10.1017/S0004972700033062 (historical literature; full text not inspected).
