# Sharp weighted-cycle \(p\)-heat gradient criterion and six-edge conductance rigidity

## Finding

For every finite cycle \(C_n\), \(n\ge3\), with arbitrary positive vertex masses and positive edge conductances, there is an explicit **sharp** coefficient controlling the largest unit-edge slope of each solution to the weighted nonlinear \(p\)-heat equation, simultaneously for every \(1<p<\infty\). The coefficient gives a necessary-and-sufficient condition for global one-input edge-Lipschitz contraction. The formula has four distinct cycle-length regimes: triangles, quadrilaterals, pentagons, and cycles of at least six vertices.

In particular, for every \(n\ge6\), **contraction holds for every initial state and every time if and only if all edge conductances are identical**, independently of vertex masses and of \(p\). For a pentagon, contraction can depend sharply on \(p\) below \(2\): unit masses and consecutive edge conductances \((1,1,1,1,3/2)\) give contraction exactly for \(p\ge p_*\), where \(p_*\in(1,2)\) is the unique root of
\[
\left(1+(3/2)^{1/(2-p_*)}\right)^{2-p_*}=2,
\qquad p_*\approx 1.336485730165.
\]
The endpoint \(p=2\) and its linear weighted-graph gradient interpretation are not claimed as independent novelties.

## Assumptions and scope

Index the vertices \(v_0,\ldots,v_{n-1}\) cyclically (indices are modulo \(n\)). Edge \(v_i v_{i+1}\) has conductance \(c_i>0\), and vertex \(v_i\) has mass \(m_i>0\). **Every edge has metric length one**, irrespective of conductance. Fix \(1<p<\infty\), put \(\phi_p(s)=|s|^{p-2}s\) for \(s\ne0\) and \(\phi_p(0)=0\), and let \(S_tu\) solve
\[
m_i\dot u_i=c_i\phi_p(u_{i+1}-u_i)+c_{i-1}\phi_p(u_{i-1}-u_i).
\]
Define \(e_i=u_{i+1}-u_i\) and \(L(u)=\max_i|e_i|\). Set
\[
a_i=\frac{c_{i-1}}{m_i},\qquad
b_i=\frac{c_{i+1}}{m_{i+1}},\qquad
d_i=c_i\left(\frac1{m_i}+\frac1{m_{i+1}}\right).
\]
For \(a,b>0\) define
\[
H_{n,p}(a,b)=
\begin{cases}
-\min\{a,b\}, & n=3,\ 1<p\le2,\\
-\left(a^{-1/(p-2)}+b^{-1/(p-2)}\right)^{-(p-2)},&n=3,\ p>2,\\
|a-b|,&n=4,\\
\left(a^{1/(2-p)}+b^{1/(2-p)}\right)^{2-p},&n=5,\ 1<p<2,\\
\max\{a,b\},&n=5,\ p\ge2,\\
a+b,&n\ge6.
\end{cases}
\]
Let the **optimal normalized instantaneous coefficient** be
\[
K_{n,p}(c,m)=\max_{0\le i<n}\bigl(H_{n,p}(a_i,b_i)-d_i\bigr).
\]
Here \(D^+\) denotes the upper right Dini derivative of a scalar function of time.

**Theorem.** For every initial function \(u\) and every \(t\ge0\),
\[
D^+L(S_tu)\le K_{n,p}(c,m)L(S_tu)^{p-1}.
\]
At \(t=0\), this coefficient is optimal and attained:
\[
\sup_{L(u)=1}D^+L(S_tu)\big|_{t=0}=K_{n,p}(c,m).
\]
Consequently, \(L(S_tu)\le L(u)\) for all \(u\) and \(t\ge0\) **if and only if** \(K_{n,p}(c,m)\le0\). If \(K_{n,p}<0\), comparison with the scalar \(p\)-power ODE also gives quantitative decay (and finite-time consensus for \(1<p<2\)).

## Proof

**Well-posedness.** The finite-dimensional operator is the negative mass-metric gradient of the convex energy \(p^{-1}\sum_i c_i|u_{i+1}-u_i|^p\). Its negative is monotone; uniqueness follows by differentiating the squared mass-weighted distance of two solutions. A vertex attaining the current maximum has nonpositive derivative, and a minimum has nonnegative derivative. Thus all solutions remain uniformly bounded and extend globally. Since the vector field is continuous for \(p>1\), trajectories are continuously differentiable, including at zero gradients.

**Edge evolution.** Direct subtraction of the adjacent vertex equations gives
\[
\dot e_i=a_i\phi_p(e_{i-1})+b_i\phi_p(e_{i+1})-d_i\phi_p(e_i),
\qquad \sum_i e_i=0.
\]
If \(e_i\) is an edge attaining the largest absolute slope \(R=L(u)>0\), replace all edge values by their common sign and divide by \(R\). By oddness and homogeneity of \(\phi_p\), it suffices to maximize \(a_i\phi_p(x)+b_i\phi_p(y)\) over feasible normalized neighboring edge values \(x,y\), subject to \(|e_j|\le1\), the chosen edge being \(1\), and cyclic closure \(\sum_j e_j=0\). The diagonal term then contributes \(-d_i\).

**All four feasible-edge polytopes.** For \(n=3\), closure forces \(x+y=-1\), so \(x=-h\), \(y=-(1-h)\), \(0\le h\le1\). Minimizing \(a h^{p-1}+b(1-h)^{p-1}\) gives the two negative formulas for \(H_{3,p}\): an endpoint minimum for \(1<p\le2\), and a strictly convex interior minimum for \(p>2\). For \(n=4\), closure with the opposite edge is equivalent to \(-2\le x+y\le0\). Since the flux is strictly increasing, a maximizer can be chosen at \(x+y=0\), and \(a\phi_p(x)+b\phi_p(-x)=(a-b)\phi_p(x)\) has maximum \(|a-b|\). For \(n=5\), the other two edges can close the cycle precisely when \(x+y\le1\), the lower bound being automatic for \(x,y\in[-1,1]\). Monotonicity allows \(x+y=1\), with \(x,y\in[0,1]\). The resulting maximum of \(a x^{p-1}+b(1-x)^{p-1}\) is the stated \(\ell_{1/(2-p)}\)-expression in the strictly concave regime \(1<p<2\), and \(\max\{a,b\}\) for \(p\ge2\). For \(n\ge6\), both neighbors can simultaneously equal \(1\), since the remaining \(n-3\) edges may all be chosen as \(-3/(n-3)\in[-1,0]\). Therefore the optimal value is \(a+b\).

Every maximum just described is **attainable**, not merely an upper bound. In each case, select the feasible normalized edge values as above; their sum is zero, so they integrate to an actual cyclic vertex function. For any chosen edge \(i\), its signed derivative is exactly \(H_{n,p}(a_i,b_i)-d_i\), even if other edges are also maximal. Because the Dini derivative of a finite maximum is the maximum of the active derivatives, the full global supremum equals \(K_{n,p}\).

**Global conclusion and necessity.** At each time with \(L>0\), the preceding maximal-edge argument gives \(D^+L\le K_{n,p}L^{p-1}\); at \(L=0\) the solution is constant and remains so. Scalar comparison proves nonincrease whenever \(K_{n,p}\le0\). If \(K_{n,p}>0\), choose an attaining edge configuration with \(L=1\); that edge increases strictly at time zero, whence \(L(S_tu)>1\) for sufficiently small positive \(t\). This proves necessity as well as sharpness.

**Six-edge rigidity.** For \(n\ge6\), put \(k_i=a_i+b_i-d_i\). Cyclic reindexing gives \(\sum_i k_i=0\). If all \(k_i\le0\), they must all vanish, so
\[
\frac{c_i-c_{i-1}}{m_i}=\frac{c_{i+1}-c_i}{m_{i+1}}
\]
for every \(i\). Hence \((c_i-c_{i-1})/m_i\) is constant in \(i\). Summing these differences around the cycle and using \(m_i>0\) forces the constant to be zero, and therefore all conductances coincide. Conversely, constant conductances give every \(k_i=0\). This proves the claimed independence of the positive vertex masses and the exponent.

**Five-edge phase example.** With unit masses and \(c=(1,1,1,1,3/2)\), exactly two edges give the possible positive coefficient, namely
\[
K_{5,p}=H_{5,p}(1,3/2)-2.
\]
The two highlighted edges attain this maximum; the remaining coefficients are strictly smaller for all \(p>1\). For \(1<p<2\), the \(\ell_r\)-norm of the positive vector \((1,3/2)\), with \(r=1/(2-p)\), decreases strictly with \(p\), from the limit \(5/2\) to \(3/2\). It therefore crosses \(2\) once, at the displayed \(p_*\). For \(p\ge2\), every relevant coefficient is negative. Thus contraction holds exactly for \(p\ge p_*\).

## Verification

The bundled standalone Python checker constructs sharp unit-slope witnesses, reconstructs exact cubic-flux derivatives using rational arithmetic, tests a finite exact-rational slope grid, examines numerical upper bounds on normalized cyclic slope data, and verifies the pentagon transition and long-cycle rigidity diagnostics. Run `python3 verify_weighted_cycle_pheat.py` with Python 3; no third-party libraries are needed.

The recorded output is:

```
NUMERIC_SHARP_WITNESSES_AND_DINI_BOUNDS_OK 3600
EXACT_RATIONAL_CUBIC_WITNESSES_OK 630
EXACT_RATIONAL_GRID_UPPER_BOUNDS_OK 1712
PENTAGON_EXPONENT_PHASE_TRANSITION_OK 1.336485730165
SIX_VERTEX_CONDUCTANCE_RIGIDITY_CHECKS_OK
ALL_WEIGHTED_CYCLE_P_HEAT_CHECKS_OK
```

These finite checks are independent diagnostics of the explicit formula, **not** exhaustive proofs of its all-weight/all-exponent validity. The proof above supplies the universal closure and scalar maximization arguments.

## Relationship to prior work

Mugnolo's discrete \(p\)-heat theory provides the nonlinear weighted-graph energy, solution theory, and vertex-function \(\ell^q\)-contractions. Hua and Mugnolo develop time regularity and asymptotic behavior of nonlinear graph \(p\)-heat. These results are foundational but a vertex-function norm contraction does not imply an edge-Lipschitz contraction. Münch and Wojciechowski characterize *linear* graph heat Lipschitz decay in terms of Ollivier curvature: the entire \(p=2\) subcase is accordingly treated as prior-method coverage and not asserted independently new. Earlier related evaluated claims include unit-conductance cycle one-input contraction and a weighted-tree criterion; the first does not address nonuniform cycle conductances, and a tree lacks the cyclic closure constraints producing the four regimes here. The claimed contribution is the **sharp nonlinear arbitrary-mass/edge-conductance cycle formula**, the exponent-sensitive five-cycle, and the six-edge conductance rigidity. The possibility of an unindexed equivalent nonlinear gradient formula remains open.

## Limitations

The metric underlying \(L\) has **unit edge lengths**, even when physical conductances are nonuniform. The result is one-input (gradient of an individual solution), not the Lipschitz norm of the difference between two nonlinear solutions. The sharp constant is instantaneous; integrated scalar bounds need not be attained at all times. The theorem excludes \(p\le1\), infinite graphs, other topologies, nonautonomous weights, and arbitrary metric edge-length rescalings. Its novelty assessment is based on the sources identified below and explicit implication comparisons, not a claim of exhaustive bibliographic uniqueness. Independent mathematical verification has not been performed.

## References

1. D. Mugnolo, *Parabolic theory of the discrete p-Laplace operator*, arXiv:1207.1996, first public posting 2012-07-09; journal publication later. https://arxiv.org/abs/1207.1996
2. B. Hua and D. Mugnolo, *Time regularity and long-time behavior of parabolic p-Laplace equations on infinite graphs*, arXiv:1410.1584, first posted 2014-10-06. https://arxiv.org/abs/1410.1584
3. F. Münch and R. K. Wojciechowski, *Ollivier Ricci curvature for general graph Laplacians: Heat equation, Laplacian comparison, non-explosion and diameter bounds*, arXiv:1712.00875, first posted 2017-12-04. https://arxiv.org/abs/1712.00875
