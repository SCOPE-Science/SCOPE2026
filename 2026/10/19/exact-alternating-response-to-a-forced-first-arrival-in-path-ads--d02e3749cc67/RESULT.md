# Exact alternating response to a forced first arrival in path adsorption

## Finding
Let \(P_n\) be the path on \(n\ge1\) vertices, and let \(J_n\) denote the expected final number of occupied sites in random sequential adsorption with nearest-neighbor exclusion and uniformly randomly ordered site proposals. Let \(J_{n,i}^{\mathrm{first}}\) be the corresponding expectation when the proposal at site \(i\) is forced to be first, while the other proposals retain a uniformly random relative order. Set \(\Delta_{n,i}=J_{n,i}^{\mathrm{first}}-J_n\).

**Theorem (first-arrival parity law).** For every \(n\ge1\) and \(1\le i\le n\):

1. If \(n\in\{1,2,4\}\), then \(\Delta_{n,i}=0\) for every \(i\).
2. Otherwise, writing \(d=\min\{i-1,n-i\}\), one has the strict sign law
   \[
   (-1)^d\Delta_{n,i}>0.
   \]
3. At any \(n\) and \(i\) with \(d\ge1\), the response satisfies the factorial localization bound
   \[
   |\Delta_{n,i}|<\frac{3\,2^d}{(d+1)!}.
   \]

Thus a site an even number of edges from its nearer endpoint increases expected occupancy when prioritized; an odd distance decreases it, with just the three stated exceptional path sizes. The sensitivity of deep interior sites decreases faster than exponentially in their boundary distance.

## Assumptions and scope
Every vertex of the finite path independently receives a continuous, identically distributed proposal time, and is occupied upon proposal exactly when both its neighbors (if present) are unoccupied. All vertices are proposed once. Conditioning vertex \(i\) to propose first is equivalent to putting that vertex first in an otherwise uniformly random vertex permutation. There is no desorption, no multiple occupancy, and no periodic identification of path endpoints. All expectations are over relative order only. The result holds for arbitrary finite \(n\), with no thermodynamic-limit assumption. The common proposal-time distribution is irrelevant provided it is continuous and independent.

## Proof
Set \(J_{-1}=J_0=0\). Conditioning the unmodified process on its first vertex gives, for every \(n\ge1\),
\[
J_n=1+\frac{2}{n}\sum_{k=0}^{n-2}J_k.
\]
The corresponding generating function follows by multiplication by \(n z^n\) and solution of the resulting first-order differential equation:
\[
\sum_{n\ge0}J_nz^n=\frac{1-e^{-2z}}{2(1-z)^2}.
\]
If the first proposal is at vertex \(i\), the two surviving path segments have lengths \(i-2\) and \(n-i-1\). They are independent after this first proposal. Consequently
\[
J_{n,i}^{\mathrm{first}}=1+J_{i-2}+J_{n-i-1}.
\]
Put \(a=i-1\), \(b=n-i\), so \(a+b+1=n\). Reflection permits assuming \(a\le b\). Write
\[
q=e^{-2},\qquad c=\frac{1-q}{2},\qquad h=\frac{1-3q}{2},
\qquad e_m=J_m-cm-h\quad(m\ge-1).
\]
The constant and linear terms cancel in the conditional difference, giving the exact identity
\[
\Delta_{n,i}=e_{a-1}+e_{b-1}-e_{a+b+1}.
\]
Here \(e_{-1}=q\). More explicitly, put \(E_m=\sum_{j=0}^{m}(-2)^j/j!\) for \(m\ge0\), and set \(E_{-1}=0\). Extracting coefficients from the generating function gives
\[
e_m=\frac{m+1}{2}(q-E_m)+(q-E_{m-1}),\quad m\ge0.
\]
For \(m\ge1\), apply Taylor's integral remainder identity
\[
q-E_m=\frac{(-2)^{m+1}}{m!}\int_0^1 (1-t)^m e^{-2t}\,dt
\]
and the corresponding identity at \(m-1\); one integration by parts yields the following formula. The case \(m=0\) follows directly by evaluation:
\[
e_m=(-1)^{m+1}u_m,\qquad
u_m=\frac{2^{m+1}}{m!}\int_0^1t(1-t)^m e^{-2t}\,dt>0.
\]
In particular,
\[
u_m<\frac{2^{m+1}}{(m+2)!},\qquad
\frac{u_{m+1}}{u_m}<\frac{2}{m+1}\quad(m\ge0).
\]
Thus \(u_m\) is strictly decreasing for \(m\ge1\). The initial comparison \(u_0>u_1\) follows from \(u_0=(1-3q)/2\), \(u_1=2q\), and \(e^2>7\). Hence \(u_0>u_1>u_2>\cdots>0\).

The strict sign classification is now a parity argument with one small-index estimate. Suppose first \(a\ge1\). If both \(a,b\) are odd, then all three terms in the displayed identity have signs \((-,-,-)\) after accounting for the subtraction, hence \(\Delta_{n,i}<0\). If both are even, they contribute \((+,+,-)\) with magnitudes \(u_{a-1},u_{b-1},u_{a+b+1}\); the first dominates the subtracted term, so \(\Delta_{n,i}>0\). If \(a\) is even and \(b\) odd, then
\[
\Delta_{n,i}=u_{a-1}-u_{b-1}+u_{a+b+1}>0,
\]
because \(a<b\) and \(u_m\) decreases. If \(a\ge3\) is odd and \(b\) even, then
\[
\Delta_{n,i}=-u_{a-1}+u_{b-1}+u_{a+b+1}
<-u_{a-1}+u_a+u_{a+1}<0.
\]
Indeed \(u_a/u_{a-1}<2/a\) and \(u_{a+1}/u_{a-1}<4/[a(a+1)]\); their sum is at most one for \(a\ge3\) and all inequalities are strict. For \(a=1\) and \(b\) even, \(\Delta=-u_0+u_{b-1}+u_{b+2}\). At \(b=2\) this is zero by \(u_0=u_1+u_4\). For all even \(b\ge4\), strict decrease makes this quantity negative.

Finally, suppose \(a=0\). When \(b\ge2\) is even,
\[
\Delta_{n,1}=q+u_{b-1}-u_{b+1}>0.
\]
When \(b\) is odd,
\[
\Delta_{n,1}=q-u_{b-1}+u_{b+1}.
\]
For \(b=1\) and \(b=3\), this vanishes by the identities \(q=u_0-u_2=u_2-u_4\). For odd \(b\ge5\), it is positive because \(u_{b-1}\le u_4<q\). The latter inequality follows from \(u_4=(1-7q)/2\) and \(e^2<9\). At \(b=0\), the difference is zero since \(2q=u_1\). These cases give precisely the listed exceptions and prove the sign law.

For the localization statement, if \(a\ge1\) is the nearer-endpoint distance, then strict decrease of \(u_m\) and \(n=a+b+1\) imply
\[
|\Delta_{n,i}|\le u_{a-1}+u_{b-1}+u_{a+b+1}<3u_{a-1}<\frac{3\,2^a}{(a+1)!}.
\]
This completes the proof.

## Verification
Run `python3 rsa_path_first_arrival_verify.py` from a directory containing the companion script. It evaluates the unmodified expectation recursively over exact rational numbers, independently enumerates every vertex permutation for \(1\le n\le8\), and checks first-conditioned expectations against the splitting formula. It also verifies all signs and the localization bound on each vertex of every path through \(n=100\). The script reports 44 direct-arrival rational comparisons and 5,050 sign/bound comparisons. These finite calculations corroborate, but do not substitute for, the analytic all-size proof.

## Relationship to prior work
The classical nearest-neighbor blocking model and its finite-path expected occupancy are established in the literature. Krivelevich, Mészáros, Michaeli, and Shikhelman derive the same first-vertex conditioning recurrence and record an explicit finite-path expectation formula in their Section 8, equations (10)–(13). The present contribution is **not** that recurrence or expectation formula: it is the complete strict sign classification of the change caused by singling out an early proposal site, including the exceptional paths and a uniform factorial localization inequality. In particular, their unmodified path expectation and tree-extremality results do not state this site-by-site sign theorem. Dhara, van Leeuwaarden, and Mukherjee give an earlier general RSA framework on Erdős–Rényi graphs rather than this deterministic finite-path perturbation. Earlier inhomogeneous RSA work considers periodically varying site or sublattice rates, not one distinguished guaranteed first proposal. A graph-edge perturbation and a proposal-priority perturbation are mathematically distinct operations, and their sign conclusions are not interchangeable.

## Limitations
This is a one-site, infinitely prioritized perturbation of a finite path. No monotonicity for finite nonuniform proposal rates is claimed, nor any analogous sign law for cycles, trees, multiple prioritized sites, or adsorption of objects larger than one vertex. The factorial coefficient is a simple uniform upper bound and is not claimed optimal. The recurrence and the general path expected size were known; novelty is restricted to the sign/exceptions/localization statement. Specialized literature not indexed in the sources examined may contain an equivalent statement. No independent external validation has occurred.

## References
1. S. Dhara, J. S. H. van Leeuwaarden, and D. Mukherjee, “Generalized random sequential adsorption on Erdős–Rényi random graphs,” first posted 2016-04-13, arXiv:1604.03918v1, https://arxiv.org/abs/1604.03918.
2. M. Krivelevich, T. Mészáros, P. Michaeli, and C. Shikhelman, “Greedy maximal independent sets via local limits,” first posted 2019-07-16, arXiv:1907.07216, Section 8, equations (10)–(13), https://arxiv.org/abs/1907.07216.
3. M. J. de Oliveira and T. Tomé, “Inhomogeneous random sequential adsorption on bipartite lattices,” Physical Review E 50 (1994), https://doi.org/10.1103/PhysRevE.50.4523.
4. N. Pippenger, “Random sequential adsorption on graphs,” SIAM Journal on Algebraic and Discrete Methods, https://doi.org/10.1137/0402034.
