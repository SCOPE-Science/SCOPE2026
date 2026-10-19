# A sharp all-step positivity criterion for fourth-order diffusion with three Laplacian eigenvalues

## Finding

The fourth-order two-stage Gauss–Legendre rational heat step has an exact, graph-wide entrywise-positivity threshold on every connected, undirected weighted graph whose Laplacian has exactly three eigenvalues. The threshold depends on only the two nonzero spectral values, graph order, and the largest individual edge conductance. Unlike an unrestricted matrix-exponential approximation, the positivity times form a single initial interval; a second positivity window cannot occur in this spectral class.

**Theorem.** Let \(G\) have \(n\ge3\) vertices, nonnegative symmetric edge conductances \(w_{ij}=w_{ji}\) (and \(w_{ii}=0\)), and connected weighted Laplacian \(L\). Assume the distinct eigenvalues of \(L\) are exactly \(0<a<b\), with the zero eigenvalue simple. Define \(s=a+b\), \(p=ab\), \(c=s/n\), and \(w_*=\max_{i<j}w_{ij}>0\). For every \(h\ge0\), let
\[
T(h)=(12I-6hL+h^2L^2)(12I+6hL+h^2L^2)^{-1}.
\]
Then \(T(h)\) is symmetric, preserves the all-ones vector, and has strictly positive diagonal entries for all \(h\ge0\). Put
\[
Q(h)=(12+6ah+a^2h^2)(12+6bh+b^2h^2)>0.
\]
For each distinct pair \(i\ne j\), the exact entry is
\[
T_{ij}(h)=\frac{12h}{Q(h)}\left[12w_{ij}+\frac{6ph}{n}+ph^2\left(\frac{s}{n}-w_{ij}\right)\right].
\]
If \(w_*\le c\), the step is entrywise nonnegative for **every** \(h\ge0\). Otherwise, define
\[
H=\frac{6p/n+\sqrt{(6p/n)^2+48pw_*(w_*-c)}}{2p(w_*-c)}.
\]
The **complete** positivity-preserving time set is exactly \([0,H]\): \(T(h)\) is entrywise nonnegative precisely for \(0\le h\le H\). At \(h=H\), the off-diagonal entries that first vanish are exactly the pairs of maximal edge conductance \(w_*\); for every \(h>H\) those entries are strictly negative. Every nonedge has a strictly positive matrix entry for every \(h>0\).

**Strongly regular graphs.** Let \(G\) instead be a connected noncomplete unweighted strongly regular graph with parameters \((v,k,\lambda,\mu)\), where every adjacent pair has \(\lambda\) common neighbors and every nonadjacent pair has \(\mu>0\) common neighbors. Define \(s=2k-\lambda+\mu\). Then its fourth-order Gauss–Legendre step preserves entrywise nonnegativity for **all** \(h\ge0\) if and only if \(s\ge v\). If \(s<v\), its exact positivity interval is
\[
0\le h\le\frac{3+\sqrt{9+12(v-s)/\mu}}{v-s}.
\]
For example, the Petersen graph has cutoff \(1+\sqrt5\); every Paley graph of prime-power order \(q\equiv1\pmod4\) satisfies the all-step condition. The triangular graph \(T_m=L(K_m)\) has all-step positivity for \(4\le m\le6\), and a finite sharp horizon for every \(m\ge7\). Thus these closely related regular graph families exhibit genuinely different positivity behavior under one and the same fourth-order integrator.

## Assumptions and scope

The differential equation is \(u'(t)=-Lu(t)\) for an arbitrary initial nonnegative state \(u(0)\ge0\), with no boundary inputs. The update is the diagonal \([2/2]\) Padé approximation to the heat semigroup, equivalently the two-stage Gauss–Legendre Runge–Kutta step. Entrywise positivity is necessary and sufficient to preserve **every** nonnegative vector. All edge weights, the timestep, and spectral eigenvalues are real; graph connectivity makes the eigenvalue \(0\) simple. Repeated nonzero eigenvalues are allowed by the phrase “exactly three distinct eigenvalues.” The theorem makes no assertion for graphs with four or more distinct Laplacian eigenvalues, for nonsymmetric/directed generators, or for methods other than the specified Padé step. Self-loops have no effect on \(L\) and are excluded from the conductance maximum.

## Proof

Write \(E_0=J/n\) for the orthogonal zero-eigenspace projection and \(E_a,E_b\) for the other orthogonal spectral projections. Since \(G\) is connected and \(L\) is symmetric,
\[
E_a+E_b=I-J/n,\qquad aE_a+bE_b=L.
\]
For each pair \(i\ne j\), solving these two scalar equations in the entries of \(E_a,E_b\), using \(L_{ij}=-w_{ij}\), gives
\[
(E_a)_{ij}=\frac{w_{ij}-b/n}{b-a},\qquad
(E_b)_{ij}=\frac{a/n-w_{ij}}{b-a}.
\]
Set \(q_x(h)=12+6xh+x^2h^2\) and \(r_x(h)=(12-6xh+x^2h^2)/q_x(h)\). On each eigenspace the step has multiplier \(r_x(h)\). In particular \(r_0(h)=1\) and \(r_x(h)=1-12xh/q_x(h)\). Therefore
\[
T(h)=I-12h\left(\frac{a}{q_a(h)}E_a+\frac{b}{q_b(h)}E_b\right),
\]
and elementary substitution yields the displayed off-diagonal identity. To verify its numerator directly, note
\[
aq_b(h)-bq_a(h)=-(b-a)(12-ph^2),\quad
q_a(h)-q_b(h)=-(b-a)(6h+sh^2).
\]
For any \(x\ge0\),
\[
r_x(h)=\frac{(xh-3)^2+3}{(xh+3)^2+3}>0.
\]
Every diagonal \(T_{ii}(h)\) is a sum of strictly positive scalar multipliers weighted by the nonnegative diagonal entries of the three orthogonal projections; the weights sum to one. Thus \(T_{ii}(h)>0\) for every \(i\) and \(h\ge0\). Since \(L\mathbf1=0\), also \(T(h)\mathbf1=\mathbf1\). The denominator \(Q(h)>0\) for every \(h\ge0\).

For each edge conductance \(w\ge0\), define the bracket
\[
F_w(h)=12w+\frac{6p}{n}h+p(c-w)h^2.
\]
If \(w\le c\), then \(F_w(h)>0\) for every \(h>0\). If \(w>c\), \(F_w\) has positive initial value and negative leading coefficient, and therefore exactly one positive zero, whose quadratic formula is
\[
H_w=\frac{6p/n+\sqrt{(6p/n)^2+48pw(w-c)}}{2p(w-c)}.
\]
For \(h<H_w\), the bracket is positive, and for \(h>H_w\) it is negative. At this root \(ph^2>12\), because \(ph^2(w-c)=12w+6ph/n>12(w-c)\). Consequently, if \(w'>w>c\), then
\[
F_{w'}(H_w)=F_w(H_w)+(w'-w)(12-pH_w^2)<0;
\]
so \(H_{w'}<H_w\). The first loss of positivity therefore occurs precisely on the edges whose conductance equals \(w_*\). The full assertions about sign, the boundary, and nonedges now follow by taking the minimum over all pairs, including \(w=0\), whose bracket is strictly positive for \(h>0\). This proves the general theorem.

For the strongly regular corollary, let \(A\) be the adjacency matrix. The standard common-neighbor identity is
\[
A^2=kI+\lambda A+\mu(J-I-A).
\]
Since \(L=kI-A\) and \(G\) is noncomplete and connected, restriction to \(\mathbf1^\perp\) gives a quadratic spectral equation with nonzero Laplacian eigenvalues \(a,b\) satisfying
\[
a+b=2k-\lambda+\mu=s,\qquad ab=v\mu=p.
\]
Every edge has conductance one, so the general criterion \(w_*\le s/v\) is exactly \(s\ge v\). Otherwise substituting \(p=v\mu\) into the general root simplifies to the stated strong-regular cutoff. The Petersen, Paley and triangular examples follow by their standard parameters: respectively \((10,3,0,1)\), \((q,(q-1)/2,(q-5)/4,(q-1)/4)\), and \((\binom m2,2(m-2),m-2,4)\). For the triangular family, \(s=3m-2\), so \(s\ge\binom m2\) for \(4\le m\le6\), with strict reverse inequality for \(m\ge7\). \(\square\)

## Verification

The included standalone Python 3 program `verify.py` uses only the standard library and exact rational arithmetic. Run it in the same directory using `python3 verify.py`. It reconstructs weighted graph Laplacians independently of the closed formula and tests the exact quadratic spectral relation, both sides of the matrix Padé equation, all off-diagonal formulas, row sums, and entrywise signs at rational timesteps. It also performs independent exact-rational matrix inversion in the smaller instances. The completed run printed `VERIFY_OK 45967 exact rational identities/inequalities 17 weighted graph instances` and checked the Petersen graph, triangular graphs, rook graphs, Paley graphs, a five-cycle, a complete bipartite graph, weighted equal-spoke stars, and unequal-weight triangles. These are finite consistency tests, not an exhaustive certificate for the general theorem, which is proved above.

## Relationship to prior work

Padé positivity of general positive linear systems and limitations of Runge–Kutta discretizations are studied by Zappavigna, Colaneri, Kirkland and Shorten (2010 and 2012). Their applicable passages provide positive-systems criteria, restrictions and counterexamples, not the present necessary-and-sufficient edgewise threshold on the distinct-three-eigenvalue class. Standard strongly regular spectral identities and graph parameters appear in Brouwer and Haemers' *Spectra of Graphs*, and are used, not claimed as new. Special cases within unweighted complete multipartite graphs and the weighted three-vertex setting are known separately and are **not** represented here as independent novelties. The distinct contribution assessed here is the graph-wide maximal-conductance criterion and sharp positivity horizon, with its primitive strongly regular graph phase classification and the impossibility of reentrant positivity in this spectral class. Source-specific equivalence comparisons and residual novelty risks are recorded in `AUDIT.json`.

## Limitations

The result is confined to connected undirected weighted graph Laplacians with two distinct positive eigenvalues. It does not assert all-step positivity for general weighted graphs, and the sharp horizon may become infinite only under the stated conductance inequality. A few related source records have incomplete historical indexing; an equivalent prior result or general theorem of which this is a corollary cannot be excluded with certainty. The finite verification run cannot establish an infinite-family identity independently of the proof. Independent mathematical audit has not been performed.

## References

1. A. Zappavigna, P. Colaneri, S. Kirkland and R. Shorten, *On the preservation of co-positive Lyapunov functions under Padé discretization for positive systems* (2010). Author repository and full text: https://mural.maynoothuniversity.ie/id/eprint/2195/ and https://mural.maynoothuniversity.ie/id/eprint/2195/1/SK-pade_MTNS10_long.pdf .
2. A. Zappavigna, P. Colaneri, S. Kirkland and R. Shorten, *Essentially Negative News About Positive Systems* (2012). Author repository and full text: https://mural.maynoothuniversity.ie/id/eprint/3761/ and https://mural.maynoothuniversity.ie/id/eprint/3761/1/SK_Essentially_Negative.pdf .
3. A. E. Brouwer and W. H. Haemers, *Spectra of Graphs*, author preprint, Chapter 9 (strongly regular graphs). https://homepages.cwi.nl/~aeb/math/ipm/ipm.pdf .
