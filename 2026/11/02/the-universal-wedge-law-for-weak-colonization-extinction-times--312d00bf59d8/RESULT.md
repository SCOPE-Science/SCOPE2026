# The universal wedge law for weak-colonization extinction times

## Finding

Let \(G=(V,E)\) be any finite simple undirected graph with \(n=|V|\ge4\) vertices, \(m=|E|\), and
\[
W(G)=\sum_{v\in V}\binom{d(v)}2,
\]
the number of unordered pairs of edges sharing one endpoint. In the continuous-time patch-occupancy process specified below, let \(\tau_G\) be the time until every patch is empty when initially all patches are occupied. Write \(z=c/e\) for the colonization-to-extinction rate ratio and \(H_j=\sum_{i=1}^j1/i\).

**Theorem.** For every fixed graph \(G\), the dimensionless mean extinction time is analytic near \(z=0\), with
\[
e\,\mathbb E[\tau_G]
=H_n+\alpha_n mz+
\left(a_n m+b_n\binom m2+w_n W(G)\right)z^2+O_G(z^3),
\]
where
\[
\alpha_n=\frac{2((n+1)H_n-2n)}{n(n-1)}>0,
\qquad w_n>0\quad\text{for every }n\ge4.
\]
All four coefficients depend only on \(n\), and the explicit finite sums defining \(a_n,b_n,w_n\) appear below. In particular, for any two graphs on the same \(n\) vertices and with the same \(m\) edges, if their wedge counts differ, then **the graph with more wedges has the strictly longer expected time to extinction for every sufficiently small positive \(z\)**. Connectedness is not required.

For the two connected four-vertex trees, the three-leaf star \(K_{1,3}\) has \(W=3\) and the path \(P_4\) has \(W=2\), giving the exact separation
\[
e\left(\mathbb E\tau_{K_{1,3}}-\mathbb E\tau_{P_4}\right)
=\frac{19}{72}z^2+O(z^3).
\]
Both trees have the same zero-order term \(25/12\) and first-order term \(29z/24\); their second-order terms are \(11z^2/16\) and \(61z^2/144\), respectively.

## Assumptions and scope

Each vertex denotes a binary habitat patch, either occupied or empty. At any occupied vertex, local extinction occurs at rate \(e>0\), independently of the others. An empty vertex with \(r\) occupied neighbors receives colonization events at rate \(cr\), where \(c\ge0\); there is no spontaneous immigration. All vertices start occupied; the all-empty state is absorbing. The graph is finite, simple, undirected and fixed while \(z\downarrow0\). Time is continuous. No large-graph or infinite-population limit is taken in the expansion.

For an occupied set \(A\subseteq V\), denote the number of internal edges by \(I(A)\), the boundary cut size by \(C(A)\), the degree of a vertex by \(d(j)\), and the number of its neighbors in \(A\) by \(r_A(j)\). Set \(T_z(A)=e\mathbb E[\tau\mid A]\), so the recovery rate after time rescaling is one. In a state with \(|A|=k\), each occupied patch disappears at rate one and an empty patch \(j\notin A\) is colonized at rate \(zr_A(j)\).

For integers \(r,s\ge0\) with \(r+s\le4\), define the falling factorial \((x)_{\underline{r}}=x(x-1)\cdots(x-r+1)\) (equal to one at \(r=0\)) and
\[
p_{rs}(k)=\frac{(k)_{\underline r}(n-k)_{\underline s}}{(n)_{\underline{r+s}}},
\quad 1\le k\le n-1.
\]
A factor is zero whenever the sample size is insufficient. Define
\[
u_1=0,\quad
u_k=\frac{2((k+1)H_k-2k)}{k(k-1)}\ (k\ge2),
\qquad v_k=\frac{H_{k+1}-1}{k}\ (k\ge1).
\]
For readability all occurrences of \(p_{rs}\) below are evaluated at \(k\). The coefficients in the theorem are
\[
\begin{aligned}
a_n&=2\sum_{k=1}^{n-1}\frac{p_{11}}{k}(u_{k+1}-v_k),\\
b_n&=\sum_{k=1}^{n-1}\frac{4p_{31}(u_{k+1}-u_k)+8p_{22}(v_{k+1}-v_k)}k,\\
w_n&=\sum_{k=1}^{n-1}\frac{1}{k}\Big[(2p_{21}-4p_{31})(u_{k+1}-u_k)\\
&\hspace{1.4cm}+(2p_{11}-8p_{22})(v_{k+1}-v_k)
+2p_{21}(u_{k+1}-2v_{k+1})+2p_{11}v_{k+1}\Big].
\end{aligned}
\]
All summands are exact rational numbers for integer \(n\). These formulas fully specify the theorem without optimization, simulation, or unspecified constants.

## Proof

**1. Analytic expansion and backward recursion.** Put \(T_z(\varnothing)=0\). The first-step equation at every nonempty \(A\), with \(k=|A|\), is
\[
(k+zC(A))T_z(A)=1+\sum_{i\in A}T_z(A\setminus\{i\})
+z\sum_{j\notin A}r_A(j)T_z(A\cup\{j\}).
\tag{1}
\]
At \(z=0\), the finite system is triangular when sorted by \(k\), with diagonal entries \(1,\ldots,n\), so its determinant is nonzero. The solution is therefore analytic at zero. Expand \(T_z(A)=\sum_{q\ge0}z^qT_q(A)\). Equation (1) implies \(T_0(A)=H_k\) and, for \(q\ge1\),
\[
kT_q(A)=\sum_{i\in A}T_q(A\setminus\{i\})+
\sum_{j\notin A}r_A(j)[T_{q-1}(A\cup\{j\})-T_{q-1}(A)].
\tag{2}
\]
The first perturbative forcing is \(C(A)/(k+1)\). The edge bookkeeping identities
\[
\sum_{i\in A}I(A\setminus\{i\})=(k-2)I(A),\quad
\sum_{i\in A}C(A\setminus\{i\})=2I(A)+(k-1)C(A)
\]
therefore give
\[
T_1(A)=u_kI(A)+v_kC(A),
\tag{3}
\]
where the scalar recurrences \(ku_k=(k-2)u_{k-1}+2v_{k-1}\), \(kv_k=(k-1)v_{k-1}+1/(k+1)\), with \(u_1=0\), \(v_1=1/2\), are solved by the \(u_k,v_k\) displayed above. For \(A=V\), \(I(V)=m\), \(C(V)=0\), proving the first-order coefficient \(u_nm=\alpha_nm\).

**2. The quadratic term is controlled by edges and wedges.** Let \(B_k\) be a uniformly random \(k\)-element subset of \(V\). Iterating (2) along the pure-death process beginning from \(V\), which visits exactly one uniform subset of each size, gives
\[
T_2(V)=\sum_{k=1}^{n-1}\frac1k\,
\mathbb E\left[\sum_{j\notin B_k}r_{B_k}(j)
\{T_1(B_k\cup\{j\})-T_1(B_k)\}\right].
\tag{4}
\]
Write \(I=I(B_k)\), \(C=C(B_k)\), \(r=r_{B_k}(j)\). Adding a vertex changes \(I\) by \(r\) and \(C\) by \(d(j)-2r\), so the brace in (4) equals
\[
(u_{k+1}-u_k)I+(v_{k+1}-v_k)C
+(u_{k+1}-2v_{k+1})r+v_{k+1}d(j).
\tag{5}
\]
There are \(W(G)\) unordered adjacent edge pairs and \(D=\binom m2-W(G)\) unordered disjoint edge pairs. Sampling any fixed specified vertices into and out of \(B_k\) gives probability \(p_{rs}(k)\). Counting edge pairs directly yields the four exact identities
\[
\begin{aligned}
\mathbb E[I C]&=2W p_{21}+4D p_{31},\\
\mathbb E[C^2]&=2m p_{11}+2W p_{11}+8D p_{22},\\
\mathbb E\sum_{j\notin B_k}r_{B_k}(j)^2&=2m p_{11}+2W p_{21},\\
\mathbb E\sum_{j\notin B_k}r_{B_k}(j)d(j)&=2(m+W)p_{11}.
\end{aligned}
\tag{6}
\]
For instance, each internal-edge/cut-edge pair meeting at one vertex is counted twice, contributing \(2Wp_{21}\); if the two edges are disjoint there are four orientations, contributing \(4Dp_{31}\). The other identities follow by the same occupied/empty endpoint counting. Substituting (5) and (6) into (4), and using \(D=\binom m2-W\), gives precisely \(a_nm+b_n\binom m2+w_nW\) with the explicit sums above. Consequently no triangle or longer-cycle count can enter the quadratic term except through the already included \(m\) and \(W\).

**3. Strict positivity of the wedge coefficient at every graph size.** Denote the \(k\)-th summand in the displayed formula for \(w_n\) by \(c_{n,k}\). Direct substitution gives
\[
c_{n,1}=\frac{2}{3n}>0,\qquad
c_{n,2}=\frac{11n-26}{18n(n-1)}>0\quad(n\ge4).
\]
For \(3\le k\le n-1\), abbreviate
\[
\begin{aligned}
C_H&=-(k+1)(k+2)[4k+n^2(k-1)+n(k-9)+4],\\
C_0&=k[-2k^3+2k^2+14k+n^2(k^2-k-4)\\
&\hspace{2cm}+n(2k^3+7k^2-11k-26)+10].
\end{aligned}
\]
Exact simplification of the \(p_{rs},u_k,v_k\) formula gives
\[
c_{n,k}=\frac{2(k-n)(H_kC_H+C_0)}{kn(k+1)^2(k+2)(n-1)(n-2)(n-3)}.
\tag{7}
\]
Here \(C_H<0\): the bracket equals \(n[(k-1)n+k-9]+4k+4\), and \((k-1)n+k-9\ge2\) whenever \(n\ge4\) and \(k\ge3\). The elementary harmonic bound
\[
H_k\ge 3-\frac{11}{3k}\qquad(k\ge3)
\tag{8}
\]
holds at \(k=3\) directly and by induction, since the increment of the left side minus the right side from \(k\) to \(k+1\) is \((3k-11)/(3k(k+1))\ge0\) for \(k\ge4\).

To certify the necessary sign without any numerical bound, substitute \(t=k-3\ge0\) and \(r=n-k-1\ge0\). An exact polynomial identity is
\[
\begin{aligned}
-3k\left[C_0+\left(3-\frac{11}{3k}\right)C_H\right]
={}&r^2(6t^4+82t^3+395t^2+797t+586)\\
&+r(6t^5+110t^4+730t^3+2117t^2+2585t+1202)\\
&+10t^5+143t^4+726t^3+1507t^2+1034t+120.
\end{aligned}
\tag{9}
\]
Every coefficient on the right of (9) is strictly positive, so \(C_0+(3-11/(3k))C_H<0\). Since \(C_H<0\), (8) implies \(C_0+H_kC_H<0\). In (7) the factor \(k-n\) is also negative, and the denominator is positive; hence every \(c_{n,k}\) is strictly positive. Summing establishes \(w_n>0\) for every integer \(n\ge4\). Together with analyticity, this proves the stated strict weak-colonization comparison for any two graphs having the same \(n,m\) but different wedge counts.

## Verification

The included standalone `CHECK.py` uses the Python standard library and exact rational arithmetic. It independently solves the Taylor-coefficient recurrence (2) for every occupied-state subset and compares its quadratic coefficient against the graph invariant formula. It checks every labeled simple graph with four or five vertices, plus deterministic sampled graphs with six, seven, and eight vertices: 1,318 graph comparisons in total. It checks the exact star-versus-path constants and positive-coefficient values for 51 graph sizes. Run `python3 CHECK.py` alongside this document.

These finite calculations are consistency checks, not a proof for arbitrary \(n\); the all-size proof is the exact combinatorial argument (1)–(6) and sign certificate (7)–(9). All tabulated constants were obtained as exact fractions rather than fitted numerical estimates.

## Relationship to prior work

The modeled colonization–extinction mechanism is the finite-graph **contact process**, also interpreted as stochastic susceptible–infected–susceptible dynamics; it is not a new model. Mountford, Mourrat, Valesin and Yao (arXiv:1203.2972v1, March 13, 2012) study extinction of this process, with graph-size and metastability asymptotics at fixed rates, not the fixed-graph \(z\downarrow0\) quadratic motif expansion. Yaari, Ben-Zion, Shnerb and Vasseur (2012) investigate how metapopulation dispersal and topology affect persistence across qualitative dispersal regimes; they do not give this universal analytic coefficient formula.

The closest computation-based predecessor, Holme and Tupikina (2018), calculates exact extinction-time behavior for every connected graph with three through eight vertices. Those exact finite-graph calculations **implicitly contain** all coefficient values for their listed graphs and therefore cover individual small-graph instances, including any four-vertex example. The separate contribution here is a graph-independent, all-finite-\(n\) structural expansion proving that only \(m,W\) govern the first two perturbative orders and that the wedge coefficient is strictly positive for every \(n\ge4\). That all-size implication is not supplied by a finite census. van de Bovenkamp and Van Mieghem (2015) derive survival times for complete and star graphs, not the all-graph wedge comparison.

## Limitations

The weak-colonization neighborhood in which a strict comparison holds may depend on the particular two graphs; this theorem asserts no uniform positive radius over unbounded graph sizes. The process assumes exponential independent extinction clocks, additive neighbor-by-neighbor recolonization, no external immigration, fixed patches, no spatially heterogeneous rates, and full initial occupancy. The result does not describe finite-rate rankings, endemic quasi-stationary initial states, large-graph limits, or conservation recommendations for a real landscape. At orders three and higher, additional graph motifs may enter.

Historical priority beyond the materially inspected sources remains provisional: a general perturbative formula or combinatorial contact-process identity elsewhere could imply part of the result. In particular, finite-table coverage must not be confused with a novelty proof for all finite graphs. Independent literature assessment has not been performed.

## References

1. Mountford, T., Mourrat, J.-C., Valesin, D., and Yao, Q. (2012 preprint; 2016 journal). *Exponential extinction time of the contact process on finite graphs*. arXiv:1203.2972v1, first public March 13, 2012. https://arxiv.org/abs/1203.2972 .
2. Yaari, G., Ben-Zion, Y., Shnerb, N. M., and Vasseur, D. A. (2012). *Consistent scaling of persistence time in metapopulations*. Ecology 93, 1214–1227. https://doi.org/10.1890/11-1077.1 ; open-author manuscript https://vasseurlab.yale.edu/sites/default/files/2012_yaari_et_al._ecology.pdf .
3. Holme, P., and Tupikina, L. (2018). *Epidemic extinction in networks: Insights from the 12,110 smallest graphs*. New Journal of Physics 20, 113042. https://doi.org/10.1088/1367-2630/aaf016 ; preprint arXiv:1802.08849.
4. van de Bovenkamp, R., and Van Mieghem, P. (2015). *Survival time of the susceptible-infected-susceptible infection process on a graph*. Physical Review E 92, 032806. https://doi.org/10.1103/PhysRevE.92.032806 .
