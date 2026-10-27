# Diameter-sharp transient Lipschitz amplification by graph heat on finite trees

## Finding
For an integer \(D\ge2\), let \(\mathcal G_D\) denote the class of all finite connected simple unweighted graphs of combinatorial diameter \(D\). For \(G\in\mathcal G_D\), let \(L_G\) be its unnormalized combinatorial Laplacian and \(H_t=\exp(-tL_G)\). Then the sharp class-wide Lipschitz amplification is
\[
\sup_{G\in\mathcal G_D}\ \sup_{t\ge0}\ \|H_t\|_{\mathrm{Lip}(G)\to\mathrm{Lip}(G)}=D.
\]
The same supremum is obtained when \(G\) ranges only over trees. For each *fixed* finite graph of diameter \(D\ge2\), however, the supremum over time is strictly less than \(D\).

More quantitatively, put \(h=\lfloor D/2\rfloor\), choose a branching factor \(b\ge2\), and set
\[
t_b=b^{-1/2},\qquad
\varepsilon_{b,h}=b^{-1/2}+e^{-\sqrt b}\sum_{j=0}^{h-1}\frac{b^{j/2}}{j!}.
\]
If \(D=2h\), the complete rooted \(b\)-ary tree of height \(h\) has a real, one-Lipschitz function \(f\) such that
\[
\operatorname{Lip}(H_{t_b}f)\ge D\bigl(1-2\varepsilon_{b,h}-b^{-1}\bigr).
\]
If \(D=2h+1\), the tree obtained by joining the roots of two complete rooted \(b\)-ary trees of height \(h\) has a real, one-Lipschitz function with
\[
\operatorname{Lip}(H_{t_b}f)\ge D\bigl(1-2\varepsilon_{b,h}\bigr).
\]
The right sides converge to \(D\) as \(b\to\infty\). A negative finite-branching lower estimate is harmless: the limiting assertion remains nontrivial.

## Assumptions and scope
Graphs are finite, simple, connected, and unweighted, with graph distance \(d_G\). For a complex- or real-valued vertex function,
\[
\operatorname{Lip}_G(f)=\max_{\{u,v\}\in E(G)}|f(u)-f(v)|
=\max_{u\ne v}\frac{|f(u)-f(v)|}{d_G(u,v)}.
\]
The induced operator seminorm is taken on functions modulo constants. The generator is \((L_G f)(v)=\sum_{w\sim v}(f(v)-f(w))\), with a jump rate of one along each incident edge; in particular this is **not** the degree-normalized random walk. The supremum over graphs varies the number of vertices and maximum degree while holding the graph diameter fixed. All inequalities hold for real or complex functions; explicit lower witnesses are real.

## Proof
**Upper bound.** Since \(-L_G\) is the generator of a finite continuous-time Markov chain, \(H_t\) has nonnegative entries and row sums one. Fix adjacent vertices \(u,v\) and a one-Lipschitz function \(f\). The two probability rows \(p_t(u,\cdot)\) and \(p_t(v,\cdot)\) can be coupled, for example by an independent coupling. Under any coupling \(\pi\),
\[
|(H_tf)(u)-(H_tf)(v)|
\le \sum_{x,y}\pi(x,y)|f(x)-f(y)|
\le D.
\]
Taking the maximum over edges proves \(\|H_t\|_{\mathrm{Lip}\to\mathrm{Lip}}\le D\) for every \(t\ge0\) and every \(G\in\mathcal G_D\).

**Strictness for any fixed finite graph.** For \(t>0\), irreducibility implies \(p_t(u,x)>0\) for every pair of vertices. For adjacent \(u,v\), set
\[
\eta_{uv}(t)=\sum_x\min\{p_t(u,x),p_t(v,x)\}>0.
\]
Couple this shared mass along the diagonal; couple the remaining total mass \(1-\eta_{uv}(t)\) arbitrarily. The previous inequality improves to \(D(1-\eta_{uv}(t))<D\). There are finitely many edges, so the operator norm is strictly below \(D\) for every \(t>0\). At \(t=0\), its norm is one, also strictly below \(D\). The norm varies continuously with \(t\), and connectedness gives \(H_tf\to |V|^{-1}\sum_x f(x)\) as \(t\to\infty\), hence the norm tends to zero. Its maximal finite-time norm is consequently strictly below \(D\).

**A high-branching walk lemma.** In any rooted \(b\)-ary tree of height \(h\), a continuous-time walk started at the root or a depth-one child runs along each edge at rate one. If the root is additionally linked to another root across an edge, that cross-edge has rate one as well. Represent the walk using an independent rate-\(b\) Poisson clock for downward steps (selecting one of the \(b\) children uniformly when not at a leaf) and an independent rate-one Poisson clock for the unique upward step, root-bridge step, or no operation when applicable. On the event that the rate-one clock does not ring before \(t\), and that the downward clock rings at least \(h\) times, the walk lies at depth \(h\) within its starting rooted tree. Therefore the probability of this event is at least
\[
1-t-\Pr\{\operatorname{Pois}(bt)<h\}.
\]
At \(t=t_b\), the right-hand failure probability is at most \(\varepsilon_{b,h}\). This argument uses the full continuous-time generator and makes no stationarity or mixing-time assumption.

**Even diameter.** Let \(D=2h\) and take a complete rooted \(b\)-ary tree of height \(h\), with root \(r\). Choose one child \(c\). Put \(f(r)=0\). At depth \(j\) within the subtree of \(c\), put \(f=-j\); in all other root branches put \(f=+j\). Every edge changes \(f\) by exactly one, so \(\operatorname{Lip}(f)=1\). The root-started walk is in the distinguished branch with probability at most \(1/b\) by branch symmetry, and reaches a leaf with probability at least \(1-\varepsilon_{b,h}\). Thus
\[
(H_{t_b}f)(r)\ge h-2h(\varepsilon_{b,h}+b^{-1}).
\]
The walk started at \(c\) reaches a leaf in its own subtree with probability at least \(1-\varepsilon_{b,h}\), whence
\[
(H_{t_b}f)(c)\le-h+2h\varepsilon_{b,h}.
\]
Subtracting gives the stated bound \(2h(1-2\varepsilon_{b,h}-b^{-1})\), measured across the single edge \(\{r,c\}\). Leaves in different root branches are at distance \(2h\), so this graph has diameter exactly \(D\).

**Odd diameter.** Let \(D=2h+1\). Join roots \(r_-\) and \(r_+\) of two complete rooted \(b\)-ary trees of height \(h\) by an edge. On the negative side put \(f=-j\) at depth \(j\) from \(r_-\); on the positive side put \(f=1+j\) at depth \(j\) from \(r_+\). Every edge again changes \(f\) by one. The walk lemma implies
\[
(H_{t_b}f)(r_-)\le-h+D\varepsilon_{b,h},\qquad
(H_{t_b}f)(r_+)\ge h+1-D\varepsilon_{b,h},
\]
which yields \(D(1-2\varepsilon_{b,h})\) across their connecting edge. The longest leaf-to-leaf path has length \(2h+1=D\).

Finally \(\sqrt b\to\infty\), so \(b^{-1/2}\to0\) and the lower Poisson tail \(e^{-\sqrt b}\sum_{j=0}^{h-1}(\sqrt b)^j/j!\to0\) for fixed \(h\). This proves the sharp universal constant for every integer \(D\ge2\) and strict nonattainment on each individual finite graph.

## Verification
The standalone file `branch_heat_check.py` constructs the exact finite lumped Markov generators for even and odd tree families. It evaluates the proposed time and one-Lipschitz witness and checks the explicit finite-branching lower inequality and upper diameter bound in 64 parameter cases (two parities, four heights, eight branching factors). Twelve small instances are independently constructed at full vertex level and cross-checked against the lumped models, including an edgewise Lipschitz check. Executing `python branch_heat_check.py` requires NumPy and SciPy. Numerical matrix exponentials test implementation consistency only; the two Poisson-clock constructions above prove the limiting statements for every fixed diameter.

## Relationship to prior work
Frank and Kovařík (arXiv:1108.6145v1) analyze geometry-sensitive heat kernels on *metric* trees, with differential Laplacians along continuous edges. Bauer et al. (arXiv:1306.2561v1) establish Li–Yau-type graph heat gradient estimates under curvature-dimension hypotheses and discuss tree geometry, but do not assert the fixed-diameter sharp family-wide Lipschitz envelope above. Keller et al. (arXiv:1509.01993v1) derive fixed-graph short-time heat-kernel distance asymptotics, which do not give this simultaneous high-degree/small-time limit. Münch and Wojciechowski (arXiv:1712.00875v1, Theorem 3.8) establish an equivalence between curvature bounds, Lipschitz semigroup estimates and Wasserstein contraction. That characterization does not provide the optimal diameter-only constant or its high-branching saturation. A separately available balanced-double-star computation determines a diameter-three special family; it does not imply arbitrary-diameter sharpness or finite-graph nonattainment. Literature searches do not establish uniqueness, and differently formulated prior coverage remains possible.

## Limitations

## References
- R. L. Frank and H. Kovařík, *Heat Kernels of Metric Trees and Applications*, arXiv:1108.6145v1 (first public 2011-08-31), https://arxiv.org/abs/1108.6145; published in SIAM Journal on Mathematical Analysis 45 (2013), DOI:10.1137/120886297 (primary MSC 47D06).
- F. Bauer, P. Horn, Y. Lin, G. Lippner, D. Mangoubi and S.-T. Yau, *Li-Yau Inequality on Graphs*, arXiv:1306.2561v1 (2013-06-11), https://arxiv.org/abs/1306.2561.
- M. Keller, D. Lenz, F. Münch, M. Schmidt and A. Telcs, *Note on Short Time Behavior of Semigroups Associated to Selfadjoint Operators*, arXiv:1509.01993v1 (2015-09-07), https://arxiv.org/abs/1509.01993.
- F. Münch and R. K. Wojciechowski, *Ollivier Ricci Curvature for General Graph Laplacians: Heat Equation, Laplacian Comparison, Non-explosion and Diameter Bounds*, arXiv:1712.00875v1 (2017-12-04), https://arxiv.org/abs/1712.00875.
