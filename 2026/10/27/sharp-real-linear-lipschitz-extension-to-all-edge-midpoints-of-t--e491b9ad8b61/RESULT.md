# Sharp real-linear Lipschitz extension to all edge midpoints of the Euclidean square and cube

## Finding
Let \(V_d=\{0,1\}^d\subset\mathbb R^d\) for \(d\in\{2,3\}\), let \(M_d\) consist of the midpoints of every edge of the Euclidean unit cube, and put \(S_d=V_d\cup M_d\). Equip these finite sets with their *ambient Euclidean distances*, not their shortest-path graph distances. Denote by \(\operatorname{Lip}(X)/\mathbb R\) the real Lipschitz space modulo constants, with its usual Lipschitz norm. The smallest operator norm of a real-linear extension right inverse to restriction is
\[
\Lambda_d=\inf\left\{\|E\|:\ E:\operatorname{Lip}(V_d)/\mathbb R\longrightarrow\operatorname{Lip}(S_d)/\mathbb R,\quad R\circ E=I\right\}.
\]
Set
\[
b_2=\frac{1+\sqrt2-\sqrt5}{2\sqrt2(1+\sqrt5)},\qquad
b_3=\frac{1+\sqrt2-\sqrt5}{4\sqrt{10}+2(1+\sqrt2-\sqrt3)}.
\]
Then
\[
\boxed{\Lambda_2=\frac{2+\sqrt2}{1+\sqrt5}=1+2\sqrt2\,b_2},\qquad
\boxed{\Lambda_3=1+4\sqrt2\,b_3}.
\]
Numerically these constants are \(1.055050013198716\ldots\) and \(1.071912669955583\ldots\), respectively. Both optima are attained by *positive*, cube-symmetry-equivariant operators, even though the infima range over **all** real-linear extensions, including nonpositive and nonsymmetric ones. Ordinary arithmetic midpoint interpolation has strictly larger respective norms \((1+\sqrt2)/\sqrt5\) and \((1+\sqrt3)/\sqrt6\).

## Assumptions and scope
All points are elements of real Euclidean space with edge length one; scaling the complete configuration changes no norm ratio. An extension is defined on Lipschitz functions modulo constants and reproduces all vertex values. It may be represented by coefficients at each new midpoint that sum to one, even if an arbitrary competing operator has signed coefficients.

For \(m\in M_d\), let \(i\) be the unique coordinate with \(m_i=1/2\). For \(v\in V_d\) let \(h_m(v)\) count the mismatches between \(v\) and \(m\) among the other \(d-1\) coordinates. Put \(a_d=\tfrac12-(d-1)b_d\), and define an extension by
\[
(E_df)(v)=f(v)\ (v\in V_d),\qquad
(E_df)(m)=a_d\sum_{h_m(v)=0}f(v)+b_d\sum_{h_m(v)=1}f(v).
\]
For \(d=3\), the two vertices with \(h_m(v)=2\) receive weight zero. There are two terms in the first sum and \(2(d-1)\) in the second, so \(2a_d+2(d-1)b_d=1\). Both coefficients are positive.

## Proof
**1. Universal lower bounds via symmetry.** The signed-coordinate-permutation group of \(V_d\) acts by isometries on \(V_d\) and \(S_d\). Averaging any right-inverse extension over the group preserves its extension property and does not increase its norm. At a given edge midpoint, invariance under the stabilizer forces coefficients constant on the level sets of \(h_m\). Thus in dimension two every averaged competitor has weights \(a,b\) with \(2a+2b=1\), and in dimension three it has weights \(a,b,c\) with \(2a+4b+2c=1\). Importantly, these parameters are arbitrary real numbers in the lower-bound argument.

For a norm-one Lipschitz test function \(f\) on \(V_d\), the norm of an extension is at least \(|(Ef)(p)-(Ef)(q)|/\|p-q\|_2\). Use the vertex \(o=(0,\dots,0)\) and \(f_+(v)=\|v-o\|_2\).

In dimension two, test \(o\) against the near midpoint \((1/2,0)\) and the opposite-side midpoint \((1/2,1)\). Directly summing the four coefficients gives
\[
\|E\|\ge1+2\sqrt2\,b,\qquad
\|E\|\ge\frac{1+\sqrt2-2\sqrt2\,b}{\sqrt5}.
\]
The first affine lower bound increases with \(b\), the second decreases, and their intersection occurs at \(b=b_2\), proving \(\|E\|\ge\Lambda_2\) without assuming positivity.

In dimension three, the same distance test for \(o\) and the near midpoint \(m=(1/2,0,0)\) yields
\[
\|E\|\ge1+4\sqrt2\,b+2(\sqrt2+\sqrt3-1)c.
\]
There is a second, distinct 1-Lipschitz vertex potential \(f_-\), given by
\[
\begin{array}{c|rrrrrrrr}
v&000&100&010&001&110&101&011&111\\ \hline
f_-(v)&0&1&1&1&\sqrt2&\sqrt2&0&\sqrt2-1
\end{array}
\]
(the displayed bitstrings are vertex names, not arithmetic expressions). Every pairwise difference in this row is bounded by the Euclidean distance between the named vertices. The same near-midpoint test now yields
\[
\|E\|\ge1+4\sqrt2\,b+(2\sqrt2-4)c.
\]
The coefficient of \(c\) is positive in the first inequality and negative in the second. Therefore, regardless of its sign, every averaged competing operator satisfies
\[
\|E\|\ge1+4\sqrt2\,b.
\]
Testing \(o\) against \((1/2,0,1)\) with \(f_+\) supplies the independent inequality
\[
\|E\|\ge\frac{1+\sqrt2-2(1+\sqrt2-\sqrt3)b}{\sqrt5}.
\]
Here the contributions of \(c\) cancel *exactly*. The two displayed bounds have opposite monotonicity as functions of \(b\), and intersect at \(b=b_3\). Hence \(\|E\|\ge\Lambda_3\) for every real-linear competitor.

**2. Constructive upper bounds.** For the positive probability coefficients of \(E_d\), attach to every \(p\in S_d\) the probability \(\mu_p\) on \(V_d\) whose average of \(f\) equals \((E_df)(p)\). At vertices \(\mu_v=\delta_v\). Kantorovich--Rubinstein duality on the finite vertex metric gives
\[
\|E_d\|=\max_{p\ne q\in S_d}\frac{W_1(\mu_p,\mu_q)}{\|p-q\|_2}.
\]
The statement can alternatively be checked directly using any coupling, since \(W_1\) is at most its transportation cost. Cube isometries reduce pair types as follows.

For \(d=2\), vertex--vertex ratios equal one. The two vertex--midpoint pair types have ratios \(1+2\sqrt2\,b_2\) and \((1+\sqrt2-2\sqrt2\,b_2)/\sqrt5\); these coincide at \(\Lambda_2\). The two midpoint--midpoint types (opposite parallel edges and adjacent perpendicular edges) each admit a coupling with transport-cost ratio \(1-4b_2\), strictly below \(\Lambda_2\). To see this, identify the common masses and transport the remaining equal mass between the opposite relevant vertices.

For \(d=3\), vertex--vertex ratios again equal one. Vertex--midpoint types are indexed by the \(0,1,2\) mismatches in the two fixed coordinates. At the first two levels their ratios are exactly \(\Lambda_3\). At level two their ratio is
\[
\frac23\left[a_3(\sqrt2+\sqrt3)+b_3(2+2\sqrt2)\right]
\le\frac{\sqrt2+\sqrt3}{3}<\Lambda_3.
\]
There are four midpoint--midpoint pair types. Parallel midpoints differing in one or two fixed coordinates, and perpendicular midpoints whose remaining common coordinate agrees, each have explicit couplings of cost ratio \(1-4b_3\). For example, in the perpendicular agreeing-coordinate case \((1/2,0,0)\) versus \((0,1/2,0)\), keep the common mass in place and move mass \(a_3-b_3\) from vertex \(100\) to vertex \(010\), together with mass \(b_3\) from \(101\) to \(011\): the cost is \(a_3\sqrt2\) and the target-point distance is \(1/\sqrt2\).

The remaining perpendicular type is represented by \(p=(1/2,0,0)\), \(q=(0,1/2,1)\). One feasible transport plan is: keep mass \(b_3\) at vertices \(000,001,010,101\); send mass \(a_3-b_3\) from \(000\) to \(001\), mass \(a_3\) from \(100\) to \(011\), and mass \(b_3\) from \(110\) to \(111\). Both marginals are correct and the transportation cost is \(a_3(1+\sqrt3)\). Its ratio is at most
\[
\frac{(1-4b_3)(1+\sqrt3)}{\sqrt6}<\Lambda_3.
\]
The last two strict inequalities follow, for instance, from \(0.012<b_3<0.014\), \(1.414<\sqrt2<1.415\), \(1.732<\sqrt3<1.733\), and \(2.449<\sqrt6<2.450\), which show that the last ratio is below \(1.063\) while \(\Lambda_3>1.067\). These elementary rational bounds may be checked by squaring. Thus the explicit operators achieve the lower bounds in both dimensions.

**3. Ordinary interpolation.** Taking \(b=0\) gives the arithmetic average of the two endpoints at each midpoint. In the square its largest pair ratio is \((1+\sqrt2)/\sqrt5\), attained at vertex--opposite-midpoint pairs. In the three-cube it is \((1+\sqrt3)/\sqrt6\), attained at perpendicular midpoints with differing common coordinate; the other pair types have smaller ratios. Both are strictly greater than the displayed optima.

## Verification
The accompanying standard-library Python program `verify_cube_midpoints.py` directly constructs all coefficient measures and independently computes finite transportation costs via a successive shortest augmenting-path algorithm. For the square it checks all \(28\) unordered pairs of \(8\) points; for the three-cube all \(190\) unordered pairs of \(20\) points. It confirms the analytical sharp norms and the strict improvement over midpoint averaging, and verifies the second three-cube dual potential on all \(28\) pairs of input vertices. Run with `python3 verify_cube_midpoints.py`. These floating-point checks supplement, and do not replace, the finite geometric proof above.

## Relationship to prior work
Ambrosio and Puglisi (2016) develop probability-measure-valued random projections and Kantorovich--Rubinstein linear extension; Bruè, Di Marino and Stra (2018 preprint) give general bounded extension constructions for doubling subsets. Their general extension mechanisms are used as context and do not claim either cubical sharp constant. Basso (2021) relates finite metric linear-extension norms to relative Lipschitz-free-space projection constants and studies exact small-cardinality extremal examples, not the full Euclidean square/cube edge-midpoint configurations. Existing computations for a regular simplex, a cross-polytope, and the *center* of a hypercube concern different base-point and target-point sets; none implies these values by symmetry or by restriction, because simultaneous midpoint interactions affect operator norms. The claimed contribution here is the two exact constants, their globally optimal *positive* realization, and the explicit dual-witness/coupling proof, not the general extension or transport framework.

## Limitations
The theorem treats the unsnowflaked Euclidean metric in dimensions two and three, with real scalar-valued data and real-linear operators. No assertion is made for all higher-dimensional cubes, other ambient metrics, complex-linear extensions, or arbitrary Banach-valued extensions. Symmetry averaging establishes existence of an equivariant optimizer, not uniqueness among all optimizers. The literature comparison does not establish exhaustive worldwide priority, and independent mathematical validation has not been performed.

## References
1. E. Bruè, S. Di Marino, F. Stra, *Linear Lipschitz and \(C^1\) extension operators through random projection*, preprint dated January 23, 2018, arXiv:1801.07533; https://arxiv.org/abs/1801.07533.
2. G. Basso, *Absolute Lipschitz extendability and linear projection constants*, preprint dated April 29, 2021, arXiv:2104.14238; https://arxiv.org/abs/2104.14238.
3. L. Ambrosio, D. Puglisi, *Linear extension operators between spaces of Lipschitz maps and optimal transport*, preprint dated September 2016, arXiv:1609.01450; https://arxiv.org/abs/1609.01450.
