# A unicyclic fiber theorem and an arithmetic mixing dichotomy for rational random billiards

## Finding
Consider the four-branch Feres random-angle map described below with a rational microgeometry angle \(\alpha=m\pi/n\), where \(m,n\) are relatively prime positive integers and \(n>6m\). For every initial angle that is not an integer multiple of \(\pi/n\), its accessible Markov state space has **exactly \(n\) elements**. The undirected positive-transition graph consists of one simple cycle of length \(n-2m\), with exactly \(2m\) pendant vertices, each joined directly to the cycle.

Consequently the finite irreducible chain is aperiodic **if and only if \(n\) is odd**. When \(n\) is even, its period is exactly two. The unique stationary law on each finite orbit has masses proportional to the sines of the angles. For odd \(n\), every point-mass initial distribution converges to this law; for even \(n\), its even and odd iterates converge to the distinct stationary laws conditioned on the two bipartition classes. All convergence statements are on the finite angle fiber, not on the full continuum of angles or the circle-position dynamics.

In particular this classification holds for every reduced numerator \(m\), rather than only for the special \(\alpha=\pi/7\) and \(\alpha=\pi/8\) examples in the literature.

## Assumptions and scope
Take integers \(m,n\ge1\) satisfying \(\gcd(m,n)=1\) and \(n>6m\). Put \(h=\pi/n\), \(\alpha=mh\), and define
\[
T_1(x)=x+2\alpha,\quad T_2(x)=2\pi-4\alpha-x,\quad
T_3(x)=x-2\alpha,\quad T_4(x)=4\alpha-x.
\]
Set \(U_\beta(x)=(1+\tan\beta\,\cot x)/2\). On the interiors of the indicated intervals the four branch probabilities are
\[
\begin{aligned}
p_1(x)&=\begin{cases}1&0<x<\alpha,\\U_\alpha(x)&\alpha<x<\pi-3\alpha,\\2\cos(2\alpha)U_{2\alpha}(x)&\pi-3\alpha<x<\pi-2\alpha,\\0&\pi-2\alpha<x<\pi,\end{cases}\\
p_2(x)&=\begin{cases}0&0<x<\pi-3\alpha,\\U_\alpha(x)-2\cos(2\alpha)U_{2\alpha}(x)&\pi-3\alpha<x<\pi-2\alpha,\\U_\alpha(x)&\pi-2\alpha<x<\pi-\alpha,\\0&\pi-\alpha<x<\pi,\end{cases}\\
p_3(x)&=\begin{cases}0&0<x<2\alpha,\\2\cos(2\alpha)U_{2\alpha}(-x)&2\alpha<x<3\alpha,\\U_\alpha(-x)&3\alpha<x<\pi-\alpha,\\1&\pi-\alpha<x<\pi,\end{cases}\\
p_4(x)&=\begin{cases}0&0<x<\alpha,\\U_\alpha(-x)&\alpha<x<2\alpha,\\U_\alpha(-x)-2\cos(2\alpha)U_{2\alpha}(-x)&2\alpha<x<3\alpha,\\0&3\alpha<x<\pi.\end{cases}
\end{aligned}
\]
These are the probabilities of the established Feres model (see references). Endpoint conventions do not enter the theorem because every considered initial angle avoids the grid \(h\mathbb Z\). The transition sends an angle \(x\) to \(T_i(x)\) with probability \(p_i(x)\).

For each \(t\in(0,h)\), define \(n\) distinct angles
\[
x_j(t)=\big(j+(j\bmod 2)\big)h+(-1)^j t,\qquad j=0,\ldots,n-1.
\]
Thus \(x_j(t)\in(jh,(j+1)h)\). Every angle outside the grid belongs to exactly one such fiber. Write \(P_t\) for the finite Markov transition matrix in this order, and \(Z_t=\sum_{j=0}^{n-1}\sin x_j(t)\).

## Proof
**1. Exact support.** The formulas for \(T_i\) and the strictly positive intervals of \(p_i\) show that the set of positive transitions is precisely the set of undirected edges of the following three disjoint kinds:
\[
\begin{array}{ll}
\{j,j+2m\},&0\le j<n-2m,\\[2pt]
\{j,4m-1-j\},&m\le j<2m,\\[2pt]
\{j,2n-4m-1-j\},&n-3m\le j<n-2m.
\end{array}
\]
The first kind comes from \(T_1,T_3\), the second from \(T_4\), and the third from \(T_2\). The inverse identities \(T_3T_1=T_1T_3=T_2^2=T_4^2=\mathrm{id}\) make every support edge bidirectional. For example, \(T_4(x_j(t))=x_{4m-1-j}(t)\) on its active interval. The displayed ranges give \(n-2m\) shift edges and \(m\) edges of each reflection kind. The three edge families are distinct because shift edges preserve index parity, while reflection edges reverse parity, and the two reflection zones are disjoint. Hence the support has exactly \(n\) vertices and \(n\) edges.

**2. Connectivity.** Shift edges connect each residue class modulo \(2m\) into a path. The low and high reflection bands each cover \(2m\) consecutive indices, hence meet every residue class exactly once. Their induced involutions on the residues \(r\in\mathbb Z/(2m)\mathbb Z\) are
\[
a(r)=-1-r,\qquad b(r)=2n-1-r.
\]
Their composition is the translation \(b\circ a(r)=r+2n\). Because \(\gcd(m,n)=1\), translation by \(2n\) is transitive on each of the even and odd residues modulo \(2m\), and \(a\) exchanges those two classes. Thus all residue paths are joined and the graph is connected.

**3. One cycle and pendant vertices.** The shift edges alone form \(2m\) paths. The added reflection edges make vertices \(0,\ldots,m-1\) and \(n-m,\ldots,n-1\) the *only* degree-one vertices, exactly \(2m\) in number. Every one of these leaves attaches directly to a vertex of degree three in the interior. Removing all leaves from the connected graph leaves a connected graph in which every vertex has degree two. It is therefore a single cycle. Its order is the number \(n-2m\) of remaining vertices. This establishes the asserted graph structure without relying on a picture or finite enumeration.

**4. Arithmetic chain period.** For any irreducible chain supported on a connected undirected graph without loops, a backtrack supplies a closed walk of length two. The period is consequently two on a bipartite graph and one if the graph has an odd cycle. A unicyclic graph is bipartite exactly when its unique cycle has even length. Since \(n-2m\) and \(n\) have identical parity, the claimed dichotomy follows.

**5. Exact stationary weights.** For all active intervals, the elementary identities
\[
\sin x\,U_\beta(x)=\frac{\sin(x+\beta)}{2\cos\beta},\qquad
\sin x\,U_\beta(-x)=\frac{\sin(x-\beta)}{2\cos\beta}
\]
and their \(2\cos(2\alpha)U_{2\alpha}\) analogues show on each of the three edge families that
\[
\sin x_i(t)\,(P_t)_{ij}=\sin x_j(t)\,(P_t)_{ji}.
\]
For reflection edges, use the identity \(\sin(y-\alpha)-2\cos\alpha\sin(y-2\alpha)=\sin(3\alpha-y)\) and substitute the relevant reflected pair of angles; the upper reflection is its \(\pi\)-symmetric counterpart. Thus \(\pi_j(t)=\sin x_j(t)/Z_t\) satisfies detailed balance. Connectedness makes it the unique invariant distribution. Summing the sine progression gives the optional explicit normalization
\[
Z_t=\begin{cases}
\dfrac{\cos(h/2-t)}{\sin(h/2)},& n\text{ odd},\\[5pt]
\dfrac{2\cos(h-t)}{\sin h},& n\text{ even}.
\end{cases}
\]
All masses are positive, so no transient states occur.

**6. Limits.** For odd \(n\), the finite, irreducible, aperiodic Markov-chain convergence theorem gives \((P_t^k)_{ij}\to\pi_j(t)\) for every \(i,j\). For even \(n\), let \(A,B\) be the graph bipartition and \(i\in A\). Stationarity and the absence of within-class edges imply \(\pi(A)=\pi(B)=1/2\); the squared transition matrix is irreducible and aperiodic on each class. Thus
\[
(P_t^{2k})_{ij}\longrightarrow2\pi_j(t)\,\boldsymbol1_{\{j\in A\}},\qquad
(P_t^{2k+1})_{ij}\longrightarrow2\pi_j(t)\,\boldsymbol1_{\{j\in B\}}.
\]
Finite-state spectral theory makes each convergence exponential, with constants that can depend on the fixed parameters and fiber.

## Verification
The accompanying standalone Python 3 program `verify.py` reconstructs the predicted graph using exact integer index arithmetic for all coprime \((m,n)\) with \(7\le n\le100\) and \(n>6m\), and for four interior offsets per pair. It checks connectivity, vertex degrees, unique-core cycle length, and parity. Independently, it evaluates all four original branch probabilities and transformations, compares their observed positive support to the claimed edge set, checks detailed balance and stationarity numerically, and confirms the sine normalizations. It completed **2,024 parameter/offset cases** without exception. Integer assertions are exact; trigonometric checks have explicit numerical tolerances. None of these finite tests is used as an infinite proof.

## Relationship to prior work
Feres introduced the microstructure-derived random angle model and its reversible Markov setting. Pinto-de-Carvalho and Vales (arXiv:2005.01892) proved finiteness and irreducibility of rational-angle orbit chains. Vales (arXiv:2212.00872), Section 3, explicitly identified one period-two chain at \(\alpha=\pi/8\) and one aperiodic chain at \(\alpha=\pi/7\); its principal global mixing theorem instead addresses the entire continuum dynamics and distinguishes rational from irrational \(\alpha/\pi\). These results imply neither the universal unicyclic graph classification for *all* reduced rational angles, nor the denominator-parity criterion and fiberwise two-phase limits. The claim is specific to the finite angle Markov chain and does not contradict the earlier continuum mixing obstruction. Related irrational-triangle work studies a different arithmetic regime.

## Limitations
Grid-boundary angles \(x=j\pi/n\) are excluded, as their branch activation can degenerate. No claim is made that a rational-angle chain converges in the full continuum to the Liouville law, nor that the corresponding full circle-position billiard is mixing. No optimal uniform spectral-gap bounds or exact second eigenvalue are asserted. Priority over possible unindexed equivalent combinatorial descriptions remains unverified by an independent expert.

## References
- Renato Feres, *Random Walks Derived from Billiards*, in *Dynamics, Ergodic Theory and Geometry*, MSRI Publications 54 (2007), pp. 179–222; author manuscript: https://www.math.wustl.edu/~feres/random_billiard.pdf .
- Alberto Pinto-de-Carvalho and Túlio Vales, *A Random Billiard Map in the Circle*, arXiv:2005.01892 (first posted 2020-05-05), https://arxiv.org/abs/2005.01892 .
- Túlio Vales, *Random circular billiards on surfaces of constant curvature: Pseudo integrability and mixing*, arXiv:2212.00872 (first posted 2022-12-01), Section 3, https://arxiv.org/abs/2212.00872 .
- Dingle, Lamb and Lázaro-Camí, *Knudsen's law and random billiards in irrational triangles*, arXiv:1006.4831 (2010), https://arxiv.org/abs/1006.4831 .
