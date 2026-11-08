# A graph-uniform contraction certificate for pinned anti-phase logistic checkerboards

## Finding

Consider the output-diffusively coupled logistic map on a finite, connected, undirected, simple, \(d\)-regular bipartite graph \(G=(U\sqcup V,E)\), where \(d\ge1\). Define
\[
 (F_{\mu,\varepsilon}(x))_i=(1-\varepsilon)f_\mu(x_i)+\frac{\varepsilon}{d}\sum_{j\sim i}f_\mu(x_j),\qquad f_\mu(x)=\mu x(1-x).
\]
For each
\[
 \frac{1+\sqrt5}{4}<t\le\frac{3+\sqrt{17}}8,
 \qquad \mu=\frac{4t+2}{4t+1-4t^2},\qquad
 \varepsilon=\frac{4t^2-2t-1}{4t^2-1},
\]
let \(p\) be equal to \(t\) on \(U\) and \(1/2\) on \(V\), and let \(q\) interchange these two values. Then \(F(p)=q\), \(F(q)=p\), and the orbit is of primitive temporal period two. The parameter interval is exactly the admissible part of this *critical-point-pinned, higher-color-value* family under \(\mu\in(0,4]\) and \(0<\varepsilon<1/2\). More specifically, every such two-color-swapping orbit with \(1/2<t<1\), one value equal to \(1/2\), and these parameter restrictions has this parametrization.

Write
\[
 v=\varepsilon\mu(2t-1)
 =\frac{2(4t^2-2t-1)}{4t+1-4t^2}.
\]
For every graph in the stated class, the full two-iterate derivative at either orbit point has spectral radius **exactly** \(v^2\), and the full four-iterate derivative has induced maximum-row-sum norm **exactly** \(v^3(v+2)\). In particular,
\[
 0<v\le\frac{\sqrt{17}-3}{2},\qquad
 \rho(D F^2(p))=v^2\le\frac{13-3\sqrt{17}}2<1,
\]
\[
 \boxed{\ \|D F^4(p)\|_{\infty\to\infty}
 =\|D F^4(q)\|_{\infty\to\infty}
 =v^3(v+2)\le\frac{71-17\sqrt{17}}2<\frac12.\ }
\]
Thus the entire network cycle is attracting for perturbations in **every** network direction, with bounds independent of graph size, degree, and topology within the class. A further quantitative statement holds: for
\[
 \delta=\frac{1}{174080},
\]
any \(x\in[0,1]^{|G|}\) satisfying \(\|x-p\|_\infty<\delta\) obeys \(\|F^{4k}(x)-p\|_\infty\le(3/4)^k\|x-p\|_\infty\) for all integers \(k\ge0\); the same statement holds at \(q\). In particular, a common strictly positive, explicit local basin radius works for all these graphs and all parameters on the curve.

Since \(|U|=|V|\), the directional-sign order parameter \(M_n=|G|^{-1}\sum_i\operatorname{sign}(x_i(n+1)-x_i(n))\), evaluated on either point of this orbit, is exactly zero at every time; hence its mean absolute value is zero.

An exact example is \(t=7/8\), \(\mu=88/23\), \(\varepsilon=5/33\): the cycle interchanges \(7/8\) and \(1/2\) on the graph's two colors, and its two-step spectral radius is \(100/529\). This includes every even-sided square torus of side at least four, but applies to all finite regular bipartite graphs.

## Assumptions and scope

The graph is finite, connected, undirected, simple, \(d\)-regular and bipartite. Each vertex has \(d\ge1\) neighbors. The map acts on \([0,1]^{|G|}\). The coupling is applied *after* the scalar logistic nonlinearity (output diffusion), not to the input before the logistic map. The logistic parameter satisfies \(0<\mu\le4\), so the interval cube is forward invariant for \(0\le\varepsilon\le1\). The exhibited temporal orbit has a spatial two-color pattern at each step and swaps colors at the next step; no assertion is made about all other attractors. The parameter \(t\) is the high site value, not a time index. For the uniqueness assertion about the pinned family, \(t>1/2\) and \(0<\varepsilon<1/2\) are required.

## Proof

**1. Exact color-swapping equations and admissible interval.** For an arbitrary regular bipartite graph the two-color subspace is invariant, and its scalar update is
\[
 (a,b)\longmapsto((1-\varepsilon)f_\mu(a)+\varepsilon f_\mu(b),\;
 \varepsilon f_\mu(a)+(1-\varepsilon)f_\mu(b)).
\]
Requiring \((t,1/2)\mapsto(1/2,t)\) gives, upon adding the equations,
\[
 \mu\bigl[t(1-t)+1/4\bigr]=t+1/2,
\]
so necessarily \(\mu=(4t+2)/(4t+1-4t^2)\). Subtracting them and using
\(f_\mu(1/2)-f_\mu(t)=\mu(t-1/2)^2\) gives
\[
 (1-2\varepsilon)\mu(t-1/2)=1.
\]
Solving for \(\varepsilon\) gives the displayed rational function. Conversely, substituting those functions into the two equations gives exact identities, so the conditions are also sufficient. The map sends \(q\) back to \(p\) by symmetry.

For \(1/2<t<1\) the denominators in the parametrization are positive. The inequality \(\varepsilon>0\) is equivalent to \(t>(1+\sqrt5)/4\). The condition \(\mu\le4\) is equivalent to \(t\le(3+\sqrt{17})/8\); on this interval \(\varepsilon<1/2\). Thus the interval in the statement is exactly the stated admissible pinned subfamily. The two states are distinct because \(t>1/2\). Regular bipartiteness implies \(|U|=|V|\), by counting edges from each color; therefore the two directional signs cancel exactly.

**2. Complete Floquet spectrum.** Order vertices with those in \(U\) first. The normalized adjacency is
\[
 W=\begin{pmatrix}0&R\\ R^{\mathsf T}&0\end{pmatrix},
\]
where \(R\) is a square nonnegative doubly stochastic matrix (row and column sums one). Hence \(\|R\|_2\le1\), while \(R\mathbf1=\mathbf1\) implies \(\|R\|_2=1\). Write \(c=f'_\mu(t)=-\mu(2t-1)\) and \(C=(1-\varepsilon)I+\varepsilon W\). Since \(f'_\mu(1/2)=0\), the one-step derivatives at the two phases are
\[
 J_p=\begin{pmatrix}(1-\varepsilon)cI&0\\ \varepsilon cR^{\mathsf T}&0\end{pmatrix},\qquad
 J_q=\begin{pmatrix}0&\varepsilon cR\\0&(1-\varepsilon)cI\end{pmatrix}.
\]
Consequently
\[
 D F^2(p)=J_qJ_p=\begin{pmatrix}
 \varepsilon^2c^2RR^{\mathsf T}&0\\
 \varepsilon(1-\varepsilon)c^2R^{\mathsf T}&0
\end{pmatrix}.
\]
Its nonzero eigenvalues, with multiplicities, are \(\varepsilon^2c^2\sigma_j(R)^2\). Their maximum is \(v^2=(\varepsilon c)^2\), because the largest singular value of \(R\) is exactly one. There are also zero eigenvalues. The same reasoning applies at \(q\). Thus this is a full-network result, not a stability calculation restricted to the two-color subspace.

**3. An exact four-iterate norm and its sharp uniform upper bound.** Put \(w=(1-\varepsilon)\mu(2t-1)\). The second color-swapping equation above shows \(w-v=2\). Squaring the displayed two-iterate derivative gives nonnegative blocks with row sums \(v^4\) on \(U\) and \(v^3w\) on \(V\). As \(w=v+2>v\),
\[
 \|D F^4(p)\|_{\infty\to\infty}=v^3(v+2).
\]
At \(q\) the two row-sum values are interchanged, giving the same induced norm. Differentiation of the explicit formula for \(v\) yields
\[
 \frac{dv}{dt}=\frac{4(4t^2+1)}{(4t^2-4t-1)^2}>0.
\]
At the upper parameter endpoint, \(v=(\sqrt{17}-3)/2\). Direct substitution gives the two displayed maximal bounds. Finally, \((71-17\sqrt{17})/2<1/2\) is equivalent to \(17\sqrt{17}>70\), which follows on squaring from \(17^3=4913>4900\). The spectral bound is then also strictly below one. Since the whole state space has finite dimension for each graph, the orbit is locally attracting in every direction.

**4. Explicit uniform basin radius.** For every \(x\in[0,1]^{|G|}\), the induced \(\ell_\infty\) norm of \(D F(x)\) is at most \(4\), since the coupling matrix is nonnegative and row stochastic. The bilinear \(\ell_\infty\) operator norm of \(D^2F(x)\) is at most \(8\), by \(f''_\mu=-2\mu\). Let \(B_k\) bound \(\|D^2 F^k\|\) uniformly over all such graphs, parameters and cube states. The chain rule gives
\[
 B_1=8,\qquad B_{k+1}\le8\,16^k+4B_k.
\]
Thus \(B_2\le160\), \(B_3\le2688\), and \(B_4\le43520\). The derivative of \(F^4\) is therefore \(43520\)-Lipschitz on the cube in the induced \(\ell_\infty\) norm. For \(\delta=1/174080\), every point within \(\delta\) of \(p\) satisfies
\[
 \|D F^4(x)\|_{\infty\to\infty}
 <\frac12+43520\delta=\frac34.
\]
The same holds at \(q\). The ball is contained in the cube because its orbit coordinates are between \(1/2\) and \((3+\sqrt{17})/8<9/10\), and \(\delta<1/10\). The mean-value inequality on each ball gives the claimed \(3/4\)-contraction of \(F^4\) and forward invariance of the ball under that fourth iterate. This proves the explicit size-independent local basin assertion. The intermediate iterates converge to the corresponding phases by continuity.

**5. Exact rational witness.** At \(t=7/8\) the formulas yield \(\mu=88/23\), \(\varepsilon=5/33\), \(f_\mu(t)=77/184\), \(f_\mu(1/2)=22/23\), and \(v=10/23\), hence \(\rho(D F^2)=100/529\). The identities in Step 1 establish this witness for any eligible graph without graph-specific numerical solving.

## Verification

The independent-of-graph algebra is established in the proof, including all quantifiers and the exact derivative and second-derivative bounds. An accompanying `check.py` program checks six symbolic identities, five endpoint identities/inequalities, and the exact rational orbit on ten finite regular bipartite graphs (cycles, complete bipartite graphs, hypercubes and even square tori; 116 vertices total). It also computes the full-network Floquet matrices and checks their spectral radii and four-step row-sum norms at the rational witness. Execute with `python check.py` using Python 3 with SymPy and NumPy. All computations are finite corroboration, not substitutes for the all-graph proof or independent verification.

## Relationship to prior work

Dixit, Chauhan and Shrimali (first public September 1, 2026) study precisely the output-diffusive square-lattice logistic model, with the directional-sign order parameter, but numerically examine a fixed coupling \(\varepsilon=0.4\) and do not supply a pinned analytic orbit curve or graph-uniform stability certificate. The present curves have \(0<\varepsilon\le(7-\sqrt{17})/16<0.18\), so they do **not** purport to describe or prove the transition they report at coupling \(0.4\).

Amritkar, Gade, Gangal and Nandakumaran (1991) already analyze stability of periodic coupled logistic-map waves in one-dimensional rings and develop the block/Fourier reduction. In particular, their two-color period-two ring patterns are prior art; neither existence of checkerboard waves in general nor the use of a Jacobian spectral test is claimed as new. The addition here is the *complete critical-point-pinned parameter curve* together with the exact all-regular-bipartite-graph Floquet spectrum, a graph-independent strictly sub-half four-step norm and an explicit graph/parameter-independent local attraction radius.

Xie and Hu (1997) investigate analytically solvable two-dimensional periodic patterns and small-system stability. The accessible abstract does not identify their exact patterns or whether they specialize to the critical-point-pinned curve. Their full article was not available for substantive comparison; this is a historical-priority risk, not evidence of novelty. Other broad studies of regular-graph synchronization concern synchronized or delayed states and do not, in the inspected materials, give this pinned two-color orbit and uniform contraction theorem.

## Limitations

The theorem is a local attraction result and does not assert global basin structure, uniqueness among all periodic orbits, or a phase transition at any parameter. It uses regular bipartite graphs, output rather than input diffusion, and a one-parameter curve with one color at the logistic critical point; neither irregular nor nonbipartite graphs are covered. The explicit basin radius is conservative rather than optimal. A full-text priority comparison with certain older two-dimensional pattern papers remains outstanding. Independent scientific review has not been performed.

## References

1. Shiva Dixit, Swati Chauhan, Manish Dev Shrimali, *Predicting Phase Ordering in Chaotic Maps and Coupled Map Lattices*, arXiv:2609.00983, first public September 1, 2026. https://arxiv.org/abs/2609.00983
2. R. E. Amritkar, P. M. Gade, A. D. Gangal, V. M. Nandakumaran, *Stability of periodic orbits of coupled-map lattices*, Physical Review A 44, R3407–R3410 (1991), https://doi.org/10.1103/PhysRevA.44.R3407
3. Fagen Xie, Gang Hu, *Spatiotemporal periodic and chaotic patterns in a two-dimensional coupled map lattice system*, Physical Review E 55, 79 (1997), https://doi.org/10.1103/PhysRevE.55.79 (abstract inspected; full text not accessible)
4. Fatihcan M. Atay, Özkan Karabacak, *Stability of Coupled Map Networks with Delays*, SIAM Journal on Applied Dynamical Systems 5 (2006), https://doi.org/10.1137/060652531 (abstract inspected; different delayed/synchronized setting)
