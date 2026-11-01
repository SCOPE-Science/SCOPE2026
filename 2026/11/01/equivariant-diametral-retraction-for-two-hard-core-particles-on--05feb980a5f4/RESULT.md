# Equivariant diametral retraction for two hard-core particles on equilateral banana graphs

## Finding
For each integer \(m\ge3\), let \(\Theta_m\) consist of \(m\) closed unit intervals joined at both endpoints. Denote the common initial and terminal poles by \(A\) and \(B\). For \(0<r\le1\), let \(U_r\) be the unordered configurations of two distinct positions in \(\Theta_m\) whose intrinsic graph distance is at least \(r\); let \(F_r\) be the ordered version.

**Theorem.** Every inclusion \(U_1\hookrightarrow U_r\) and \(F_1\hookrightarrow F_r\) is an explicit equivariant *strong deformation retract*. The homotopy, defined below for all positive thresholds simultaneously, takes a configuration at distance \(d\) to one at distance exactly \((1-t)d+t\) at time \(t\). It commutes with permutations of the \(m\) edges, exchange of the two poles, and (in the ordered case) exchange of particles.

The diametral configuration space is a one-vertex graph with precisely \(\binom m2\) loop edges; the ordered diametral space is a two-vertex graph with exactly \(m(m-1)\) edges between its vertices. Consequently, for every \(0<r\le1\),
\[
U_r\simeq\bigvee^{\binom m2}S^1,\quad
F_r\simeq\bigvee^{m(m-1)-1}S^1,
\]
and each positive-threshold inclusion induces isomorphisms on all integral homology groups and fundamental groups.

The action on integral first homology of the unordered space is the \(S_m\times C_2\)-lattice \(\bigwedge^2\mathbb Z^m\boxtimes\varepsilon\), where \(S_m\) permutes the standard basis and \(\varepsilon\) is the nontrivial pole-exchange sign character. The ordinary full-symmetry quotient \(U_r/(S_m\times C_2)\) is contractible.

## Assumptions and scope
Each geometric edge has *exactly* length one, with the intrinsic shortest-path metric. A point on the \(i\)-th edge has coordinate \(u\in[0,1]\) measured from \(A\). All coordinates zero represent \(A\), and all coordinates one represent \(B\). The graph is a metric multigraph; subdividing the edges does not change the graph's metric realization. The parameter is a minimum center-to-center separation, not physical disc radius. No assertion is made for non-equilateral edge lengths or for more than two particles. At \(r=0\), where coincidence is allowed, the argument does not apply. For \(r>1\), there are no configurations.

## Proof
**1. Exact metric.** Two points with coordinates \(u,v\) on the same edge have distance \(|u-v|\). For distinct edges their distance is
\[
d(u,v)=\min\{u+v,\,2-u-v\}.
\]
Indeed the routes through \(A\) and \(B\) realize these lengths, and any route visiting both poles is no shorter. Every distance is at most one, and a pair is diametral precisely when it is \(\{A,B\}\), or lies on distinct edges with \(u+v=1\).

**2. A universal homotopy.** Let \(t\in[0,1]\). On a configuration represented by two points on the *same* edge, order their edge coordinates \(u<v\) and set
\[
(u_t,v_t)=((1-t)u,\ 1-(1-t)(1-v)).
\]
Its new separation is \((1-t)(v-u)+t\). This prescription is invariant under particle exchange.

For positions on *different* edges, put \(s=u+v\). Since the two points are distinct and at positive distance, \(0<s<2\). If \(s\le1\), define
\[
c_t=(1-t)+\frac{t}{s},\qquad (u_t,v_t)=(c_tu,c_tv).
\]
If \(s\ge1\), define
\[
c_t=(1-t)+\frac{t}{2-s},\qquad
(u_t,v_t)=(1-c_t(1-u),\ 1-c_t(1-v)).
\]
The formulas agree along \(s=1\). For \(s<1\), the new sum is \((1-t)s+t\); for \(s>1\), it is \((1-t)s+t\), too. Thus the new graph distance is \((1-t)d+t\). The coordinates remain within \([0,1]\) because, in the first case, each is no larger than the new sum (at most one), and in the second, each complement is no larger than the new sum of complements (at most one). The same exact distance law holds on a single edge.

**3. Continuity at both poles.** The formulas for different edges must descend through the identifications of endpoint coordinates. At a point \(u=0\) and another point of coordinate \(v>0\), the first formula becomes \((0,(1-t)v+t)\), *independent of the nominal edge of the endpoint \(A\)*. This agrees with the same-edge formula applied to \(0<v\). At a point \(u=1\) and another coordinate \(v<1\), the second formula becomes \((1,(1-t)v)\), again independent of the nominal edge of the endpoint \(B\), and agrees with the same-edge formula. All other seams are particle swaps of these. In particular the pair \(\{A,B\}\) stays fixed. By the pasting lemma on the finitely many position cells, the rule descends to a continuous homotopy of the unordered and ordered configuration spaces.

**4. Strong deformation and equivariance.** Every new separation is \((1-t)d+t\ge d\ge r\), so each homotopy stays in the restricted space. Time zero gives the identity; time one gives distance one; and already diametral configurations are fixed pointwise throughout, because the same-edge case is then \(\{A,B\}\) and the distinct-edge case has \(s=1\). Edge permutations preserve all formulas. Pole exchange replaces \(u,v\) by \(1-u,1-v\), exchanging the two distinct-edge branches; the formulas are compatible. The ordered formulas also commute with particle swapping. This establishes all asserted equivariant strong deformation retractions. Since the same homotopy preserves every \(U_r\), the inclusions for any pair of positive thresholds have common equivariant homotopy inverse obtained by restriction of the endpoint retraction onto \(U_1\).

**5. Diametral graph and symmetry.** Each unordered pair of *distinct* edge labels \(\{i,j\}\) contributes the interval of diametral configurations
\[
\bigl\{\{(i,u),(j,1-u)\}:0\le u\le1\bigr\}.
\]
Its two endpoints are the *same* configuration \(\{A,B\}\), which is the only diametral configuration on a single edge. Distinct such intervals meet only at that common vertex. Hence \(U_1\) is a wedge of \(\binom m2\) circles. For ordered configurations, there are two distinct vertices \((A,B)\) and \((B,A)\) and an interval for every *ordered* pair of distinct edge labels, giving \(m(m-1)\) connecting edges. Both integral homology descriptions and the fundamental group ranks follow from these one-dimensional models.

Orient the unordered loop for \(i<j\) by increasing the coordinate on edge \(i\), and denote its homology class by \(z_{ij}\). Under \(\sigma\in S_m\), \(z_{ij}\) goes to \(z_{\sigma(i),\sigma(j)}\), with \(z_{ji}=-z_{ij}\), exactly the exterior-square permutation lattice \(e_i\wedge e_j\mapsto e_{\sigma(i)}\wedge e_{\sigma(j)}\). Pole exchange reverses every such loop and acts by \(-1\). The subgroup \(S_m\) permutes all loops transitively and includes a stabilizer exchanging \(i,j\), which reverses that loop. Accordingly the quotient of the bouquet by \(S_m\) is an interval (the loop folded at its midpoint); adding pole exchange does not change contractibility. Equivariant deformation yields the quotient claim for each \(r\).

## Verification
The accompanying Python program uses exact rational arithmetic to exercise the piecewise homotopy at 46,000 rational parameter/position cases, including shared-pole coordinate identifications, pole-exchange symmetry and all edge permutations through five edges. It separately enumerates the diametral loop labels and their oriented signed action. This is a finite cross-check of the definitions and boundary seams, **not** the proof for real parameters or arbitrary edge count; that proof is the preceding five-step argument. Run \(`python3 verify.py`\) from a directory containing the file.

## Relationship to prior work
Deeley's 2011 work studies two thick particles on metric graphs, gives critical-value methods and component algorithms; the 2011 thesis is an earlier public source. Dover and Özaydın's 2013 preprint gives general finite-polytopal and isotopy-type bounds for restricted graph configurations. Neither inspected article specifies an all-separation equivariant diametral retraction on the equilateral parallel-edge family. Maciążek and Sawicki's 2019 discussion identifies a free group of rank three for *unrestricted* unordered two-point configurations of the three-edge theta graph, which agrees with the \(m=3\) Betti rank but does not determine the restricted-spaces filtration or its symmetric integral module. The novelty claimed here is the *uniform equivariant deformation through every positive hard-core threshold*, not the already known \(m=3\) ordinary braid-group rank.

## Limitations
The special equal-edge metric is essential to the displayed formulas. The statement does not classify unequal lengths, additional particles, or the zero-threshold symmetric square with allowed collisions. The result is a self-contained mathematical argument and exact finite stress tests, not independent certification or a definitive guarantee of literature priority. The full 2011 Durham thesis PDF was not accessible during the literature inspection; its abstract was inspected and it remains an overlap risk.

## References
1. K. Deeley, *Configuration spaces of thick particles on graphs*, Durham University PhD thesis, deposited 7 June 2011, repository record https://etheses.durham.ac.uk/862/.
2. K. Deeley, *Configuration spaces of thick particles on a metric graph*, Algebraic & Geometric Topology 11 (2011), 1861–1892, doi:10.2140/agt.2011.11.1861 (published 14 June 2011).
3. J. Dover and M. Özaydın, *Homeomorphism and Homotopy Types of Restricted Configuration Spaces of Metric Graphs*, arXiv:1301.5693v1, first submitted 24 January 2013.
4. T. Maciążek and A. Sawicki, *Non-abelian Quantum Statistics on Graphs*, Communications in Mathematical Physics 371 (2019), 921–973, doi:10.1007/s00220-019-03583-5, especially Example 4.
