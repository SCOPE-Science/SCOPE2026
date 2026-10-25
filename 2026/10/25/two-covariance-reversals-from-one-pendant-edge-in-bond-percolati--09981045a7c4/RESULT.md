# Two covariance reversals from one pendant edge in bond percolation

## Finding

For every integer \(L\ge3\), let \(G_L\) be the simple unicyclic graph obtained from the cycle \(C_L\) by attaching exactly one new leaf by an edge to one cycle vertex. Retain every edge independently with probability \(p\in(0,1)\). Let \(B\) be the number of bridges (open edges whose deletion increases the component count), and let \(I\) be the number of isolated vertices of the resulting spanning subgraph. Set \(q=1-p\).

**Sharp two-switch theorem.** For \(3\le L\le6\), the covariance \(\operatorname{Cov}(B,I)\) is strictly negative for every \(0<p<1\). For every \(L\ge7\), there are exactly two distinct numbers \(0<p_-(L)<p_+(L)<1\) for which the covariance vanishes. Its signs on the three intervening intervals are, in order, strictly negative, strictly positive, and strictly negative. Each zero is simple.

The exact all-parameter formula is
\[
\operatorname{Cov}(B,I)=p q\,\Phi_L(p),\qquad
\Phi_L(p)=-1-2(L-1)q-3q^2+L p^{L-1}q(L-1+q).
\tag{1}
\]
In particular, the first graph exhibiting this reentrant dependence has eight vertices (a seven-cycle and one leaf). For \(L=7\), the positive phase lies approximately between \(p=0.89279\) and \(p=0.94380\); these decimal values are illustrative, not a proof.

For comparison, on the leafless cycle \(C_L\) the covariance is \(L p q^2(Lp^{L-1}-2)\) and changes sign **once**, at \(p=(2/L)^{1/(L-1)}\). Thus a single pendant leaf eliminates that high-density positive sign, but a positive middle-density phase survives precisely when \(L\ge7\).

## Assumptions and scope

All graphs are finite, simple and labeled only for the purpose of specifying edges. The cycle length is an integer \(L\ge3\). Bond retention is independent and homogeneous with \(0<p<1\). Isolated vertices include vertices of the full original vertex set that have no retained incident edges. A bridge is a retained edge whose removal increases the number of connected components. Correlations are not normalized; claims concern the covariance, not the Pearson correlation coefficient.

A supporting identity holds more generally for *any* finite connected unicyclic graph \(G\) with unique cycle \(C\) of length \(L\) and original vertex degrees \(d_v\):
\[
\operatorname{Cov}(B,I)=-p\sum_{v\in V(G)}d_vq^{d_v}
+L p^L\sum_{v\in V(C)}q^{d_v}.
\tag{2}
\]
The sharp two-switch classification is claimed for \(G_L\), not for arbitrary unicyclic graphs.

## Proof

**Bridge-isolation identity.** For a realized percolation configuration let \(M\) count open edges and let \(Z\) indicate that *every* edge of the unique base cycle is open. Every edge outside that cycle is a bridge whenever open; an open cycle edge is nonbridging precisely when every cycle edge is open. Therefore, pointwise,
\[
B=M-LZ.
\tag{3}
\]
Write \(Y_v\) for the isolated-vertex indicator, so \(I=\sum_vY_v\). If \(e\) is incident to \(v\), then \(X_eY_v=0\), \(\mathbb E X_e=p\), and \(\mathbb E Y_v=q^{d_v}\). If it is not incident, \(X_e\) and \(Y_v\) are independent. Consequently
\[
\operatorname{Cov}(M,I)=-p\sum_v d_v q^{d_v}.
\tag{4}
\]
For \(v\) on the cycle, \(ZY_v=0\) and \(\operatorname{Cov}(Z,Y_v)=-p^Lq^{d_v}\); for vertices off the cycle, the two variables involve disjoint edge sets and have zero covariance. Equations (3)--(4) give (2).

**Single-leaf specialization.** In \(G_L\), the degrees are one vertex of degree \(1\), one cycle vertex of degree \(3\), and \(L-1\) cycle vertices of degree \(2\). Substitution into (2) gives (1). Since \(pq>0\), the sign is that of \(\Phi_L\).

**Polynomial with at most two positive roots.** Put \(u=p/q>0\), so \(p=u/(1+u)\). Multiply \(\Phi_L(p)\) by the strictly positive factor \((1+u)^{L+1}\). The resulting polynomial is
\[
F_L(u)=L u^{L-1}((L-1)u+L)
-(1+u)^{L-1}\bigl(u^2+2Lu+2(L+1)\bigr).
\tag{5}
\]
Its coefficient of \(u^{L+1}\) is \(-1\), that of \(u^L\) is \(L^2-4L+1\), and that of \(u^{L-1}\) is \(-3(L^2-L+2)/2\). Every coefficient of \(u^j\) for \(0\le j\le L-2\) is strictly negative: the first summand in (5) contributes nothing at these degrees, and the second is the negative of a product of polynomials with positive coefficients. For \(L\ge4\), the leading three coefficients have signs \(-,+,-\), and all lower coefficients are negative. Descartes' rule of signs therefore bounds the number of positive roots, counted with multiplicity, by two. At \(L=3\), all coefficients are negative.

**Small-cycle obstruction.** For \(3\le L\le6\), equation (5) obeys, for every \(u>0\),
\[
F_L(u)\le u^{L-1}\bigl[-u^2+(L^2-4L+1)u-3(L^2-L+2)/2\bigr].
\tag{6}
\]
(The inequality is strict because lower-degree coefficients are negative.) The quadratic in square brackets has discriminant, in increasing order of \(L=3,4,5,6\), equal to \(-44,-83,-96,-23\); with negative leading coefficient it is strictly negative on the real line. Hence \(F_L(u)<0\) and the covariance is strictly negative for every \(p\in(0,1)\).

**Positive phase for \(L\ge7\).** Set \(q=1/(2L)\), equivalently \(p=1-1/(2L)\). At \(L=7\), exact rational evaluation gives
\[
\Phi_7(13/14)=\frac{15515949}{210827008}>0.
\tag{7}
\]
For every integer \(L\ge8\), the elementary logarithmic inequality \(\log(1-t)>-t/(1-t)\), with \(t=1/(2L)\), yields
\[
\bigl(1-1/(2L)\bigr)^{L-1}>e^{-1/2}>3/5.
\]
Substituting this strict lower bound into (1) gives
\[
\Phi_L\bigl(1-1/(2L)\bigr)
>\frac{3L-23}{10}+\frac{23}{20L}-\frac{3}{4L^2}>0
\quad(L\ge8).
\tag{8}
\]
On the other hand \(\Phi_L(0)=-2L-2<0\) and \(\Phi_L(1)=-1<0\), where these are continuous endpoint evaluations. The intermediate value theorem produces two *distinct* roots in \((0,1)\), one on each side of the positive witness. The map \(p\mapsto u=p/(1-p)\) is a bijection from \((0,1)\) to \((0,\infty)\); Descartes' bound makes these the only two roots and forces both to have multiplicity one. Continuity then gives precisely the asserted negative--positive--negative sign pattern.

Finally, substituting \(d_v=2\) for every vertex of a leafless cycle into (2) proves the one-switch comparison stated above. This completes the proof.

## Verification

Run the standalone `verify.py` with Python 3. It enumerates *all* retained-edge subsets of \(C_L\) and of \(G_L\) for \(3\le L\le8\), computes actual graph bridges by edge deletion and isolated vertices by degrees, and compares the resulting exact-rational covariance to the respective closed formula at four rational probabilities. It also validates the coefficient pattern for \(3\le L<40\), all four small-length discriminants, and rational positive witnesses at eight cycle lengths including \(L=7\) and \(L=100\). An additional irregular unicyclic host with two leaves checks the general identity. The checker reports 212 successful exact-rational assertions. All unbounded claims are established by the proof, not by the enumeration.

## Relationship to prior work

Bonneau, Biham, Kühn and Katzav analyze bridge statistics in configuration-model networks and covariance of endpoint *degrees* of a randomly selected bridge. Their arXiv version first appeared on 2020-09-06; that covariance is a different random variable and a different model. Elçi, Weigel and Fytas develop exact bridge-density and bridge-fluctuation identities in the random-cluster model, including independent percolation. Their formulas connect bridge density to covariance of total edge count with total component count; they do not give the bridge-count versus isolated-vertex-count phase diagram on the single-leaf cycle. Lanchier and La Salle investigate moments of finite percolation cluster sizes and estimate isolated vertices, but do not study bridges. The closest published published-finding corpus overlap concerning component--triangle covariance compares *component count* with *open triangles*, not the present pair of statistics; its general graph formula does not imply the two-root threshold.

Equation (2) is obtained from standard indicator covariance algebra and is offered as a transparent supporting lemma, not claimed as a new general percolation formalism. The proposed contribution is the exact classification of the two sign reversals with the sharp \(L=7\) threshold. Related methods may allow the result to be extracted from established generating-function frameworks; historical priority beyond the sources inspected is not independently settled.

## Limitations

No extension of the two-switch classification to arbitrary unicyclic hosts or graphs with multiple cycles is claimed. The result concerns covariance, not independence or stochastic monotonicity. It assumes independent equal-probability edge retention and the usual spanning-vertex notion of isolation. Numerical approximations of the zeros are not necessary for the proof, and no elementary closed forms for those zeros are claimed.

## References

1. H. Bonneau, O. Biham, R. Kühn and E. Katzav, "Statistical analysis of edges and bredges in configuration model networks," arXiv:2009.03682, first public 2020-09-06, https://arxiv.org/abs/2009.03682.
2. E. M. Elçi, M. Weigel and N. G. Fytas, "Bridges in the random-cluster model," arXiv:1509.00668, first public 2015-09-02, https://arxiv.org/abs/1509.00668.
3. N. Lanchier and A. La Salle, "First and second moments of the size distribution of bond percolation clusters on regular graphs," arXiv:2111.01982, first public 2021-11-03, https://arxiv.org/abs/2111.01982.
4. "Three-point connectivity exactly controls component–triangle covariance," published-finding corpus, 2026-10-04, public published-finding corpus identifier `2026/10/4/SCOPE-three-point-connectivity-exactly-controls-component-triangle-cov--f947a72b3174`.
