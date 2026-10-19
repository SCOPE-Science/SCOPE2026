# A re-entrant fourth-order Gauss positivity window on the seven-dimensional cube

## Finding
For the continuous-time unit-edge heat equation on the binary hypercube, the two-stage, fourth-order Gauss–Legendre Runge–Kutta endpoint map has a sharp small-step positivity obstruction in dimension seven, even though it is symmetric, mass preserving, and positive definite at every positive step. Precisely, on the seven-dimensional cube \(Q_7\), the map is entrywise nonnegative exactly for
\[
 h\in\{0\}\cup[\alpha,\beta],
\]
where \(\alpha\) and \(\beta\) are the unique positive roots of the explicit integer polynomials \(P_7\) and \(P_1\) below. Numerically,
\[
 \alpha=0.077269592923024155\ldots,\qquad
 \beta=0.665356334285853390\ldots.
\]
Thus the zero timestep is isolated: every sufficiently small *positive* timestep produces a negative antipodal entry; positivity is restored on a bounded intermediate window, then is lost again. Moreover, seven is the smallest hypercube dimension exhibiting arbitrarily-small-step negativity: each \(Q_d\), \(1\le d\le6\), has an entrywise nonnegative endpoint map at all sufficiently small nonnegative steps, whereas every \(Q_d\), \(d\ge7\), fails positivity for every sufficiently small positive step.

## Assumptions and scope
For each integer \(d\ge1\), the graph \(Q_d\) has vertex set \(\{0,1\}^d\) and unit-weight edges between vectors differing in one coordinate. Let \(L_d=dI-A_d\) be its combinatorial Laplacian. Let \(h\ge0\) be the dimensionless timestep, and define
\[
 T_d(h)=(12I-6hL_d+h^2L_d^2)(12I+6hL_d+h^2L_d^2)^{-1}.
\]
This is the linear endpoint update \(u_{n+1}=T_d(h)u_n\) of the two-stage Gauss–Legendre method for \(u'=-L_du\). Entrywise nonnegative means every matrix entry is nonnegative, equivalently that every nonnegative initial vector yields a nonnegative one-step output. This statement is about the endpoint map, not the internal stages or general nonlinear equations. All denominators below are strictly positive for \(h\ge0\).

Introduce
\[
\begin{aligned}
P_7(h)&=4356h^6+13132h^5+13538h^4+5880h^3+966h^2-9,\\
P_1(h)&=1259580h^{12}+6107220h^{11}+13035142h^{10}+14937006h^9\\
&\quad+8744306h^8+525420h^7-3302157h^6-2835756h^5\\
&\quad-1282716h^4-362880h^3-64908h^2-6804h-324,\\
P_2(h)&=251580h^{11}+620340h^{10}-301154h^9-3084234h^8\\
&\quad-5491500h^7-5305620h^6-3255021h^5-1331316h^4\\
&\quad-364770h^3-64800h^2-6804h-324.
\end{aligned}
\]

## Proof
**Spectral reduction.** The Walsh characters indexed by subsets of \(\{1,\ldots,d\}\) diagonalize \(L_d\) with eigenvalues \(2k\), where \(0\le k\le d\). Two vertices of Hamming distance \(r\) therefore have the same matrix entry \(K_{d,r}(h)\) of \(T_d(h)\), given by
\[
K_{d,r}(h)=\frac1{2^d}\sum_{k=0}^d H_{d,r,k}\frac{3-3kh+k^2h^2}{3+3kh+k^2h^2},\qquad
H_{d,r,k}=\sum_j(-1)^j\binom rj\binom{d-r}{k-j},
\]
where a binomial coefficient outside its ordinary integer range is zero. This follows directly by expanding the characters and grouping subsets by cardinality and their overlap with the \(r\) differing-coordinate positions. In particular, this identity computes **every** matrix entry from \(d+1\) scalar expressions rather than a \(2^d\)-dimensional inverse.

For \(d=7\) put \(q_k(h)=3+3kh+k^2h^2\), \(D(h)=\prod_{k=1}^7q_k(h)>0\), and \(N_r(h)=128D(h)K_{7,r}(h)\). The Walsh formula and \(\sum_{k=0}^7H_{7,r,k}=128\mathbf1_{r=0}\) give the exact integer-polynomial identity
\[
N_r(h)=128\mathbf1_{r=0}D(h)-6h\sum_{k=1}^7 kH_{7,r,k}\prod_{\substack{1\le j\le7\\j\ne k}}q_j(h).
\]
Exact polynomial multiplication yields
\[
N_1=-864hP_1,\qquad N_2=-864h^2P_2,\qquad N_7=90720h^7P_7.
\]
The remaining off-diagonal numerators have manifestly positive coefficients after extraction of their positive leading factors:
\[
\begin{aligned}
N_3&=864h^3(81060h^{10}+723660h^9+2381978h^8+4038216h^7\\
&\quad+4115676h^6+2705976h^5+1181061h^4+341712h^3+63234h^2+6804h+324),\\
N_4&=864h^4(242340h^9+1167180h^8+2513210h^7+3059880h^6\\
&\quad+2302020h^5+1111824h^4+345303h^3+66528h^2+7182h+324),\\
N_5&=4320h^5(67956h^8+265692h^7+442010h^6+407778h^5\\
&\quad+225540h^4+75852h^3+14931h^2+1512h+54),\\
N_6&=90720h^7(3876h^6+13132h^5+17290h^4+11682h^3\\
&\quad+4326h^2+828h+63).
\end{aligned}
\]
The diagonal \(K_{7,0}(h)\) is strictly positive, since each eigenvalue of \(T_7(h)\), namely \((s^2-6s+12)/(s^2+6s+12)\) for \(s\in\{0,2h,\ldots,14h\}\), is strictly positive. Thus only \(P_1,P_2,P_7\) can constrain entrywise positivity for positive \(h\).

By Descartes' sign rule, each of \(P_1,P_2,P_7\) has at most one positive root. Each has a negative constant and positive leading coefficient, so each has exactly one positive root. Denote the roots of \(P_7,P_1,P_2\) by \(\alpha,\beta,\gamma\), respectively. Their exact sign evaluations give
\[
P_7(1/20)<0<P_7(1/10),\quad
P_1(1/2)<0<P_1(1),\quad
P_2(1)<0,
\]
so \(0<\alpha<1/10<1/2<\beta<1<\gamma\). Consequently \(N_7\ge0\) exactly when \(h\ge\alpha\), \(N_1\ge0\) exactly when \(h\le\beta\), and \(N_2\ge0\) exactly when \(h\le\gamma\), for positive \(h\). All other shells are positive. Their intersection is precisely \([\alpha,\beta]\). At \(h=0\), \(T_7(0)=I\), proving the full exact window.

**Sharp dimension boundary.** The Taylor coefficients of
\[
R(z)=\frac{12+6z+z^2}{12-6z+z^2}
\]
are \(1,1,1/2,1/6,1/24,1/144,0,-1/1728\) through degree seven. For two distinct cube vertices at distance \(r\), the coefficient of \(h^j\) in \(R(-hL_d)\) vanishes for \(j<r\), because a walk requires at least \(r\) off-diagonal transitions. If \(1\le r\le5\), its first nonzero coefficient equals \(r!c_r\), where \(c_r>0\) is the degree-\(r\) Taylor coefficient of \(R\), and hence is positive. When \(r=6\), the order-six coefficient vanishes; among length-seven matrix products connecting the vertices, exactly six positive edge moves and one negative diagonal stay are possible (a seventh edge move would have the wrong hypercube parity). For the \(d\)-regular cube, their combined coefficient is \(-7d\,6!\), hence the first nonzero coefficient of \(K_{d,6}\) is \(7d\,6!/1728>0\). Therefore all entries for \(1\le d\le6\) are nonnegative for sufficiently small positive \(h\), because there are finitely many distances and all diagonal entries approach one.

For \(d\ge7\), pick two vertices at distance seven. The degree-seven term has exactly \(7!\) ordered shortest paths and the Padé Taylor coefficient \(-1/1728\); therefore
\[
K_{d,7}(h)=-\frac{35}{12}h^7+O_d(h^8)<0
\]
for every sufficiently small positive \(h\). This proves minimality of cube dimension seven and its persistence in every higher dimension. Finally \(T_d(h)\mathbf1=\mathbf1\) and its spectrum is strictly positive for every finite \(d\), \(h\ge0\), by \(R(0)=1\) and positivity of the scalar ratio, proving the ancillary conservation and positive-definiteness claims.

## Verification
The standalone Python 3 file `artifacts/verify_hypercube_pade.py` uses only the standard library and exact rational/integer arithmetic. It regenerates the Walsh-shell numerators, checks the three signed factors, checks strict coefficient signs of all other off-diagonal shells, proves the one-positive-root sign patterns and rational root brackets, and independently recomputes sample spectral entries with exact fractions. It checks the Taylor coefficient at degree seven and the dimension-six boundary. Execute from the package root using `python3 artifacts/verify_hypercube_pade.py`; a successful run prints `VERIFY_OK`. No floating-point search or finite enumeration is used to justify the universal statements.

## Relationship to prior work
Zappavigna, Colaneri, Kirkland, and Shorten established in 2012 that diagonal Padé approximants need not preserve positivity of general Metzler systems. Their primary full text features an eight-state nilpotent/shift construction and Hurwitz shifts, not an undirected conservative cube or its exact positivity window. A published eight-state Markov refinement develops an absorbing pure-birth chain and an intermediate positivity interval; it is **directed**, and its stochasticity interval does not imply the seven-cube's exact endpoint interval. Earlier graph-specific investigations on cycles and complete multipartite graphs concern different graph spectra and cannot imply positivity or negativity on the seven-cube. Lóczi and Ketcheson investigate *uniform* radii of absolute monotonicity of rational functions, which are insufficient to determine the exact graph-specific window proved here. The present claim is the complete seven-dimensional **undirected reversible** graph classification and the dimension threshold within hypercubes, not a claim of a new general Padé obstruction or a new Padé series coefficient.

## Limitations
The result covers finite unweighted binary hypercubes, the specified fourth-order endpoint map, and exact arithmetic. It does not assert minimal *vertex count* among undirected graphs, characterize arbitrary reversible Markov chains or Cartesian products, or extend to weighted cube edges, internal Gauss–Legendre stages, nonlinear equations, or floating-point implementations. The lower-dimensional claim only guarantees sufficiently-small-step positivity for each fixed cube; it does not give all-step intervals for each dimension \(1\le d\le6\). Originality comparisons may miss unindexed prior work on cube-specific rational transition kernels.

## References
1. A. Zappavigna, P. Colaneri, S. Kirkland, R. Shorten, “Essentially Negative News About Positive Systems,” *Linear Algebra and its Applications* **436** (2012), 3425–3442, doi:10.1016/j.laa.2011.12.021. Public manuscript: https://mural.maynoothuniversity.ie/id/eprint/3761/ (deposit 2012-06-19).
2. L. Lóczi and D. I. Ketcheson, “Rational functions with maximal radius of absolute monotonicity,” *LMS Journal of Computation and Mathematics* **17** (2014), 159–205, doi:10.1112/S1461157013000326; first preprint arXiv:1303.6651v1 (2013-03-26).
3. “Eight-state barrier for Markov positivity of the [2/2] Padé map,” published research note (2026), https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-eight-state-pade-markov-positivity-barrier--4aad2a3f58ab.
