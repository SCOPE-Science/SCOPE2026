# Exact transient Lipschitz amplification for complete-bipartite heat semigroups

## Finding

Let \(a,b\) be positive integers and let \(K_{a,b}\) be the complete bipartite graph with unit edge lengths. Write \(L\) for the unnormalized combinatorial Laplacian and \(T_t=e^{-tL}\) for its continuous-time heat semigroup. For a vertex function \(f\), let
\[\operatorname{Lip}(f)=\max_{u\sim v}|f(u)-f(v)|.\]
This is exactly the Lipschitz seminorm for the shortest-path metric. The induced seminorm operator norm on real or complex functions modulo constants is denoted by \(\Lambda_{a,b}(t)\).

**Exact all-time law.** For every \(t\ge0\), writing \(M=\max(a,b)\) and \(m=\min(a,b)\),
\[\boxed{\Lambda_{a,b}(t)=\left(2-\frac2M\right)e^{-mt}-\left(1-\frac2M\right)e^{-(M+m)t}.}\]
For every edge \(xy\), its endpoint heat distributions satisfy \(W_1(p_t(x,\cdot),p_t(y,\cdot))=\Lambda_{a,b}(t)\). A single 1-Lipschitz potential, independent of time, achieves equality for all \(t\).

**Sharp transient-amplification threshold.** If \(M-m\le2\), then \(\Lambda_{a,b}(0)=1\) and \(\Lambda_{a,b}(t)<1\) for every \(t>0\), with strict decrease. If \(M-m>2\), then \(\Lambda_{a,b}\) initially increases above one, has exactly one positive-time maximizer
\[t_* =\frac1M\log\frac{(M-2)(M+m)}{2m(M-1)},\]
and its exact global peak equals
\[\boxed{\Lambda_{a,b}(t_*)=\frac{2(M-1)}{M+m}\left(\frac{2m(M-1)}{(M-2)(M+m)}\right)^{m/M}.}\]
After this peak the norm decreases strictly to zero. For each fixed \(m\ge1\), the peak increases toward \(2\) in the sense that its limit as \(M\to\infty\) is \(2\). In particular the universal bound \(\Lambda_{a,b}(t)<2\) is sharp as a bound across all graph sizes and times.

## Assumptions and scope

The graph has two nonempty parts of sizes \(a,b\); an isolated edge \(K_{1,1}\) and all stars are included. The generator is **not degree-normalized**: \((Lf)(v)=\sum_{w\sim v}(f(v)-f(w))\). Every edge length is one; two distinct vertices in the same part have distance two. The time parameter is \(t\ge0\). The seminorm vanishes on constants, and the induced norm is the supremum over nonconstant functions. Complex-valued functions have the same norm because rotating the phase of any output difference reduces its optimization to a real 1-Lipschitz function.

## Proof

**1. Heat law difference.** Fix an adjacent pair \(x\) in the part of size \(a\), and \(y\) in the part of size \(b\). Put \(U=e^{-bt}\), \(V=e^{-at}\), and \(E=e^{-(a+b)t}\). The Laplacian matrix has block form
\[L=\begin{pmatrix}bI_a&-J_{a,b}\\-J_{b,a}&aI_b\end{pmatrix}.\]
The constant direction has eigenvalue zero; zero-sum vectors on the first and second parts have eigenvalues \(b\) and \(a\), respectively; the part-contrast direction has eigenvalue \(a+b\). Exponentiating these four mutually orthogonal spectral subspaces gives the signed difference \(\nu=p_t(x,\cdot)-p_t(y,\cdot)\):
\[\begin{aligned}
\nu(x)&=\frac{a-1}{a}U+\frac Ea,\\
\nu(z)&=\frac{E-U}{a}&& (z\text{ in the first part},\ z\ne x),\\
\nu(y)&=-\frac{b-1}{b}V-\frac Eb,\\
\nu(z)&=\frac{V-E}{b}&& (z\text{ in the second part},\ z\ne y).
\end{aligned}\]
Terms from empty classes simply disappear. For \(t>0\), positive signed mass is supported at \(x\) and the other vertices of the second part, while negative signed mass lies at \(y\) and the other vertices of the first part.

**2. Exact transport.** Set \(s_x=\nu(x)\), \(s_B=(b-1)(V-E)/b\), and \(d_y=-\nu(y)\). Total positive mass is \(s_x+s_B\). Between the positive and negative supports, transport from \(x\) to \(y\), or from the other second-part vertices to the other first-part vertices, costs one unit per mass; the other two types cost two. An optimal plan fills both cheaper cross-type channels as far as the marginals allow. The unavoidable amount in a cost-two channel is exactly \(|s_x-d_y|\). Hence
\[W_1(p_t(x,\cdot),p_t(y,\cdot))=s_x+s_B+|s_x-d_y|\]
\[=E+2\max\left\{\frac{a-1}{a}(U-E),\frac{b-1}{b}(V-E)\right\}.\]
This remains valid when either part has size one (the corresponding empty-class mass is zero), and at \(t=0\) by continuity.

Suppose \(a\ge b\). Then \(U\ge V\), so \(U-E\ge V-E\); also \((a-1)/a\ge(b-1)/b\). Thus the first branch wins and the preceding formula becomes
\[W_1=E+\frac{2(a-1)}a(U-E)=\left(2-\frac2a\right)e^{-bt}-\left(1-\frac2a\right)e^{-(a+b)t}.\]
Interchanging parts gives the claimed expression with \(M,m\).

**3. Attainment and operator norm.** Any real 1-Lipschitz function \(f\) satisfies \(|T_tf(x)-T_tf(y)|\le W_1(p_t(x,\cdot),p_t(y,\cdot))\) by the finite Kantorovich duality theorem. When \(a\ge b\), define \(f(x)=2\), \(f=0\) at the other vertices of the \(a\)-part, and \(f=1\) throughout the \(b\)-part. Every edge joins values differing by one, so \(\operatorname{Lip}(f)=1\). Substituting the displayed values of \(\nu\) gives
\[T_tf(x)-T_tf(y)=2\nu(x)+\sum_{z\text{ in second part}}\nu(z)=E+\frac{2(a-1)}a(U-E).\]
Thus this *one fixed potential* attains equality at every time. All graph edges are equivalent by the part-preserving automorphism group, so taking the maximum of adjacent-vertex differences proves the exact induced Lipschitz seminorm formula. For \(a<b\), interchange the two parts. The argument for complex functions follows by taking a real part after a unimodular phase rotation.

**4. Time-phase diagram.** For \(M\ge2\), differentiate the exact formula:
\[\Lambda'_{a,b}(t)=\frac{e^{-mt}}{M}\left[-2m(M-1)+(M-2)(M+m)e^{-Mt}\right].\]
The bracket strictly decreases with \(t\) if \(M>2\), and at \(t=0\) equals \(M(M-m-2)\); for \(M=2\), the derivative is strictly negative. For \(M=m=1\), the exact norm is \(e^{-2t}\). Consequently \(M-m\le2\) means strict decrease on \((0,\infty)\), even in the equality case where the initial derivative vanishes. If \(M-m>2\), the derivative changes sign exactly once at the stated \(t_*\). The critical-point equation is
\[(M-2)(M+m)e^{-Mt_*}=2m(M-1).\]
Substitution gives the displayed peak expression. Its limiting value is two when \(M\to\infty\) with fixed \(m\), since \(m\log M/M\to0\). The strict upper bound two follows from \(\Lambda_{a,b}(t)\le2(M-1)e^{-mt}/M<2\) for \(M\ge2\), \(t>0\), and from the separate case \(K_{1,1}\).

## Verification

The standalone file `verify_bipartite.py` constructs the graph Laplacian, evaluates its matrix exponential, and independently solves the finite Kantorovich dual linear program with all metric constraints. For every \(1\le a,b\le7\), it checks five times \(t\in\{0,10^{-4},0.1,0.7,2\}\). It also evaluates the time-independent extremizing potential and checks the analytic peak against direct numerical optimization for several unequal pairs. Run `python verify_bipartite.py` with NumPy and SciPy installed. These finite checks test the formulas but are not substitutes for the arguments in the Proof section.

## Relationship to prior work

Ollivier's 2007 work establishes the Wasserstein-curvature framework for Markov chains. Veysseire (2012) defines coarse Ricci curvature for continuous-time processes and proves exponential \(W_1\) bounds from uniform curvature lower bounds. Münch and Wojciechowski (2017), particularly Theorems 2.6 and 3.8, connect graph curvature to the infinitesimal Lipschitz decay of heat semigroups. Their general curvature theory can recover the *initial derivative* \(\Lambda'_{a,b}(0)=M-m-2\) after a calculation on this graph, so that local sign criterion is not claimed as an independently new abstract phenomenon. The all-time two-exponential equality, a single norming potential for all times, the unique sharp peak and its closed amplitude are not consequences of the cited bound alone, and no identical full-time theorem was identified in the examined material. These distinctions are by mathematical implication rather than title resemblance.

## Limitations

The result applies to finite, unweighted complete bipartite graphs with the unnormalized heat generator and shortest-path Lipschitz seminorm. It does not cover arbitrary graphs, normalized random-walk generators, varying edge conductances, or metric graphs with continuum edges. Independent validation of novelty has not been performed. Absence of a match in indexed results cannot exclude earlier unindexed or differently formulated calculations.

## References

1. Y. Ollivier, *Ricci curvature of Markov chains on metric spaces*, arXiv:math/0701886, first posted 30 January 2007. https://arxiv.org/abs/math/0701886
2. L. Veysseire, *Coarse Ricci curvature for continuous-time Markov processes*, arXiv:1202.0420, first posted 2 February 2012; Definitions 5–6 and Theorem 9. https://arxiv.org/html/1202.0420v1
3. F. Münch and R. K. Wojciechowski, *Ollivier Ricci curvature for general graph Laplacians: Heat equation, Laplacian comparison, non-explosion and diameter bounds*, arXiv:1712.00875, first posted 4 December 2017; Theorems 2.6 and 3.8. https://arxiv.org/abs/1712.00875
