# Sharp refinement thresholds for nonnegative graph diffusion under extrapolated backward Euler

## Finding
Let \(G\) be any finite connected undirected graph with at least two vertices and strictly positive finite edge conductances. Let \(L\) be its (unnormalized) weighted Laplacian, and let \(r\ge2\) be an integer. Define the second-order two-level Richardson extrapolation of backward Euler by
\[
T_r(h)=\frac{r(I+hL/r)^{-r}-(I+hL)^{-1}}{r-1},\qquad h\ge0.
\]
Every \(T_r(h)\) has row sums one, but not necessarily nonnegative entries. Say \(T_r\) is **locally Markov-positive** on \(G\) when there is a graph-dependent \(\varepsilon>0\) such that all entries of \(T_r(h)\) are nonnegative for every \(0\le h<\varepsilon\).

**Theorem (two sharp refinement thresholds).** For every such weighted graph, independently of its size or conductances:

1. If \(3\le r\le17\), then \(T_r\) is locally Markov-positive **if and only if** \(\operatorname{diam}(G)\le3\).
2. If \(r=18\), then \(T_r\) is locally Markov-positive **if and only if** \(\operatorname{diam}(G)\le4\).
3. At \(r=2\), every graph of diameter at most two is locally Markov-positive, and every graph of diameter at least four is not. Diameter three does not suffice: there is an explicit simple unweighted 13-vertex diameter-three counterexample, although the four-vertex path is locally Markov-positive.

Thus among the standard integer refinements, **three** is the smallest number of microsteps that guarantees local Markov positivity for all diameter-three graphs, and **eighteen** is the smallest that guarantees it for all diameter-four graphs. For \(3\le r\le17\), every matrix entry associated with distance exactly four is negative for all sufficiently small \(h>0\). At \(r=18\), the analogous assertion holds for every pair at distance exactly five. These are *small-time* rather than global-in-step assertions; they do not give a graph-independent timestep threshold.

## Assumptions and scope
All vertices are distinct finite states; graph distance uses positive-conductance edges and does not depend on their weights. The Laplacian is \(L_{ii}=\sum_{j\ne i}w_{ij}\) and \(L_{ij}=-w_{ij}\) for \(i\ne j\), with \(w_{ij}=w_{ji}\ge0\), and positive weights exactly on graph edges. The inverses exist for \(h\ge0\) because \(L\) is symmetric positive semidefinite.

The extrapolate is the endpoint **combination** of a full macrostep of backward Euler and \(r\) refined substeps; it is neither a stagewise-positive convex combination nor a claim about arbitrary multilevel extrapolations. Here the same scalar \(h\) multiplies every conductance; the graph is fixed while \(h\downarrow0\). Entries are tested in exact mathematics, not floating-point sign tests. Unweighted graphs are included.

## Proof
Write \(f_r(z)=[r(1+z/r)^{-r}-(1+z)^{-1}]/(r-1)\). Binomial expansions around zero give
\[
f_r(z)=\sum_{k\ge0}(-1)^k a_k(r)z^k,\quad a_0(r)=1,\quad
 a_k(r)=\frac{\binom{r+k-1}{k}-r^{k-1}}{(r-1)r^{k-1}}\ (k\ge1).
\]
In particular, exactly for every integer \(r\ge2\),
\[
a_1=1,\quad a_2=\frac12,\quad
 a_3=\frac{r-2}{6r},\quad
 a_4=\frac{r^2-17r-6}{24r^2}.
\]
The common first three Taylor terms \(1-z+z^2/2\) establish second-order consistency. Factoring the numerator of \(a_4\) shows that \(a_4<0\) for every integer \(2\le r\le17\) and \(a_4>0\) at \(r=18\). Furthermore,
\[
a_5(18)=\frac{\binom{22}{5}-18^4}{17\cdot18^4}<0
\]
because \(\binom{22}{5}=26334<104976=18^4\).

For vertices \(u\ne v\) at graph distance \(d\), the off-diagonal entry \((L^k)_{uv}\) is zero for every \(k<d\), since a nonzero term in the matrix product requires at least \(d\) off-diagonal moves. At length exactly \(d\), every move is along a shortest path, so
\[
(L^d)_{uv}=(-1)^d\, W_d(u,v),\qquad
W_d(u,v)=\sum_{P:\,u\to v,\,|P|=d}\ \prod_{e\in P}w_e>0.
\]
Therefore, whenever \(a_d(r)\ne0\),
\[
(T_r(h))_{uv}=a_d(r)W_d(u,v)h^d+O(h^{d+1})\qquad (h\downarrow0).
\]
Each diagonal entry equals \(1+O(h)\), and the number of pairs is finite. Consequently, if all coefficients \(a_d\) for distances occurring in the graph are strictly positive, a common sufficiently small positive timestep exists making all entries nonnegative. If any occurring distance has a negative coefficient, the corresponding entry is negative for all sufficiently small positive steps. If a connected graph has diameter at least \(d\), it contains a pair at distance exactly \(d\) along a diameter-realizing geodesic.

For \(3\le r\le17\), the coefficients \(a_1,a_2,a_3\) are strictly positive and \(a_4\) strictly negative. The first assertion follows. At \(r=18\), \(a_1,a_2,a_3,a_4\) are strictly positive and \(a_5\) negative, proving the second. Since \(a_4(r)<0\) for every integer \(r\le17\), no smaller integer refinement can guarantee local nonnegativity on a graph of diameter four: the unweighted five-vertex path already fails. Likewise \(r=2\) is not a universal guarantee for diameter-three graphs, as the following construction demonstrates.

For \(r=2\), \(a_3(2)=0\) while \(a_4(2)=-3/8\). Construct a graph on the vertices \(\{u,a,b,v,c\}\cup X\cup Y\), with \(|X|=|Y|=4\) and all edges unweighted. Include exactly the edges of the path \(u-a-b-v\), every \(u-x\) and \(x-c\) for \(x\in X\), and every \(c-y\) and \(y-v\) for \(y\in Y\). The graph has diameter three and \(\operatorname{dist}(u,v)=3\). Its single three-edge \(u\)-\(v\) path is \(u-a-b-v\), while its four-edge walks consist of the 16 paths \(u-x-c-y-v\). In the fourth Laplacian power, those walks contribute \(+16\); placing one diagonal factor on the three-edge path contributes \(-(\deg u+\deg a+\deg b+\deg v)=-(5+2+2+5)=-14\). Thus \((L^4)_{uv}=2\), and
\[
(T_2(h))_{uv}=-\frac34h^4+O(h^5)<0
\]
for all sufficiently small \(h>0\). By contrast, the unweighted four-vertex path has diameter three, a unique three-step endpoint path, \((L^4)_{uv}<0\) for its endpoints, and therefore a *positive* fourth-order leading term (the remaining entries have positive first- or second-order leading terms). Hence it is locally Markov-positive, establishing the boundary distinction.

Finally \((I+tL)^{-1}\mathbf1=\mathbf1\) for \(t\ge0\), so the displayed linear combination satisfies \(T_r(h)\mathbf1=\mathbf1\) regardless of whether its entries are nonnegative. This completes the proof.

## Verification
`verify.py` is a standalone Python 3 program requiring NumPy (`requirements.txt`). It reconstructs every coefficient identity using exact rational arithmetic and checks the signs for all integer refinements from two through eighteen. It builds the explicit 13-vertex graph, verifies its diameter and the exact values \((L^3)_{uv}=-1\), \((L^4)_{uv}=2\), and reproduces representative matrix evaluations and path witnesses. Run `python verify.py` from the directory containing the files.

These finite tests supplement the binomial-coefficient proof, exact graph construction, and shortest-walk leading-term argument; they cannot establish the universal claim by themselves.

## Relationship to prior work
Classical extrapolation and its correction weights, order and numerical-stability analysis are prior art. Constantinescu and Sandu (2008, Sections 2--3) give the multi-substep implicit Euler extrapolation framework and recurrence; Mona, Lagzi and Havasi (2015, Sections 2--4) study reaction-diffusion simulations using Richardson extrapolation of explicit Euler. Neither inspected source states a uniform **graph-diameter-dependent entrywise positivity guarantee** or the sharp microstep count 18.

The published result *Richardson acceleration creates a sharp positivity barrier for backward Euler* (2026) already proves the exact *scalar* sign threshold for this same \(f_r\) and all integer \(r\); that scalar assertion is not claimed anew. Its full displayed result only treats scalar decay, and scalar positivity does not imply matrix entrywise positivity. The distinct claim here is a universal small-time graph criterion through weighted shortest paths, with sharp refinement thresholds and an explicit diameter-three exception.

Strong-stability/absolute-monotonicity literature gives general positivity limitations for integrators, but such scalar or arbitrary-Metzler conditions do not by themselves give the two graph-diameter cutoffs for finite symmetric diffusion networks. No statement is made about every alternative numerical method or higher extrapolation columns.

## Limitations
The conclusions are local in timestep, for fixed finite weighted graphs; \(\varepsilon\) may be arbitrarily small under variations of weights and graph size. No all-timestep Markov positivity is asserted. The result classifies refinements \(2\le r\le18\) to the stated extent, not every larger integer \(r\) and not the ambiguous individual diameter-three graphs when \(r=2\). A generic graph at \(r=2\) can have cancellations at distance three that require higher-order analysis.

The novelty assessment depends on inspected indexed literature and accessible mathematical records; an unknown equivalent graph-specific theorem could exist. The work has not undergone independent mathematical audit.

## References
1. E. M. Constantinescu and A. Sandu, *On Extrapolated Multirate Methods*, Virginia Tech Technical Report TR-08-12, first public record 2008-07-01, https://vtechworks.lib.vt.edu/items/ebb67866-cdc5-4201-a065-a2a4f68566d2.
2. E. M. Constantinescu and A. Sandu, *Extrapolated Implicit-Explicit Time Stepping*, SIAM Journal on Scientific Computing 31 (2010), 4452--4477, doi:10.1137/080732833.
3. T. Mona, I. Lagzi and A. Havasi, *Solving Reaction-Diffusion and Advection Problems with Richardson Extrapolation*, Journal of Chemistry (2015), article 350362, doi:10.1155/2015/350362.
4. *Richardson acceleration creates a sharp positivity barrier for backward Euler*, published mathematical record (2026), https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-richardson-acceleration-creates-a-sharp-positivity-barrier-for-b--c9c2b9f6d7e1.
