# A three-phase axial flatness law for disk-forced diagonal contractions

## Finding

Fix \(0<b<a<1\). Let \(B_2=\{(u,v):u^2+v^2\le1\}\), \(A=\operatorname{diag}(a,b)\), and consider the disk-forced set-valued dynamics \(X\mapsto AX+B_2\). Its compact global attracting fixed set is
\[
K=\sum_{n=0}^{\infty}A^n B_2,
\]
where the sum converges in Hausdorff distance. Its topmost point is \(P=(0,H)\), \(H=(1-b)^{-1}\). Write the boundary near \(P\) as a graph \(y=g(x)\), and define its contact deficit \(D(x)=H-g(x)\). The boundary is \(C^2\) everywhere, and its contact with the horizontal tangent at \(P\) has three phases:

\[
\begin{array}{ll}
 a^2<b<a:&D(x)\sim\tfrac12(1-a^2/b)x^2,\\[2pt]
 b=a^2:&D(x)\sim\tfrac12\log(1/a)\,\dfrac{x^2}{\log(1/|x|)},\\[6pt]
 0<b<a^2:&c(a,b)|x|^q\le D(x)\le C(a,b)|x|^q,\quad q=\dfrac{\log b}{\log a}>2,
\end{array}
\]
for all sufficiently small nonzero \(x\), with positive constants \(c,C\) depending only on \(a,b\). Thus \(\lim_{x\to0}\log D(x)/\log|x|=q\) in the third case. At both vertical extrema, the boundary is \(C^2\) but **not** \(C^3\) when \(a^3\le b\le a^2\). These formulas classify the quadratic-to-logarithmic-to-power-flat transition, not the boundary's full higher-order differentiability at every parameter.

## Assumptions and scope

All coordinates, balls, distances and regularity classes are Euclidean. The noise set is the **closed** disk of radius one at every step, not a probabilistic law or a trajectorywise random attractor. The matrix is diagonal with strictly positive distinct eigenvalues \(0<b<a<1\), and there is no affine drift. The contact-deficit statements concern the two axial extrema \((0,\pm H)\); the bottom version follows by central symmetry. The symbol \(\sim\) denotes a ratio tending to one and \(\asymp\) means two-sided positive constant bounds. Regularity is the standard regularity of the embedded planar boundary curve, locally represented as a graph.

## Proof

**1. Exact fixed set and support points.** Iterating \(X\mapsto AX+B_2\) from \(\{0\}\) gives \(\sum_{n=0}^{m}A^nB_2\), convergent because \(\|A\|=a<1\). The set-map contracts Hausdorff distance by at most \(a\); therefore its limit is the unique compact globally attracting fixed set. Its support function is
\[
h(\theta)=\sum_{n\ge0}\sqrt{a^{2n}\cos^2\theta+b^{2n}\sin^2\theta}.
\]
The leading disk makes the support point unique at every normal, so the boundary is a strictly convex \(C^1\) curve. For normal proportional to \((t,1)\), \(t>0\), the support point \((X(t),Y(t))\) satisfies
\[
X(t)=t\sum_{n\ge0}\frac{(a^2/b)^n}{\sqrt{1+(a/b)^{2n}t^2}},\qquad
H-Y(t)=\sum_{n\ge0}b^n\left(1-\frac1{\sqrt{1+(a/b)^{2n}t^2}}\right).
\tag{1}
\]
By symmetry, \(D(-x)=D(x)\), and \(X(t)\downarrow0\) as \(t\downarrow0\). Each \(X(t)>0\) corresponds to the point on the upper graph with that abscissa.

**2. Quadratic regime.** Away from the vertical normals, the curvature radius in normal-angle coordinates equals
\[
\rho(\theta)=\sum_{n\ge0}\frac{a^{2n}b^{2n}}{(a^{2n}\cos^2\theta+b^{2n}\sin^2\theta)^{3/2}}.
\tag{2}
\]
When \(a^2<b\), uniform domination by \((a^2/b)^n/|\sin\theta|^3\) near \(\theta=\pi/2\) gives \(\rho(\pi/2)=\sum_{n\ge0}(a^2/b)^n=(1-a^2/b)^{-1}\). The local graph has \(g''(0)=-1/\rho(\pi/2)\). Consequently \(D(x)=\tfrac12(1-a^2/b)x^2+o(x^2)\).

**3. Critical logarithmic regime.** Set \(b=a^2\). For \(t>0\) put \(N=\lfloor\log(1/t)/\log(1/a)\rfloor\), so \(a^{N+1}<t\le a^N\). In (1), split each series at \(N\). For \(n\le N\), the ratio \(u_n=t a^{-n}\) lies in \([0,1]\). The inequalities
\[
\left|\frac1{\sqrt{1+u^2}}-1\right|\le\frac{u^2}{2},\qquad
1-\frac1{\sqrt{1+u^2}}=\frac{u^2}{2}+O(u^4)
\]
hold uniformly for \(0\le u\le1\). Because \(\sum_{n=0}^N u_n^2=O_a(1)\), \(\sum_{n=0}^N a^{2n}u_n^4=O_a(t^2)\), the two head sums are \(t(N+1+O_a(1))\) and \(\tfrac12t^2(N+1+O_a(1))\). The tails are respectively \(O_a(t)\) and \(O_a(t^2)\): indeed \((1+u_n^2)^{-1/2}\le1/u_n\) and \(\sum_{n>N}a^{2n}=O_a(t^2)\). Thus
\[
X(t)=t(N+O_a(1)),\qquad D(X(t))=\tfrac12t^2(N+O_a(1)).
\]
Since \(\log(1/X(t))=N\log(1/a)+O(\log(N+1))\), division gives
\[
\lim_{x\to0}\frac{D(x)\log(1/|x|)}{x^2}=\frac{\log(1/a)}2.
\tag{3}
\]

**4. Power-flat regime with an exact exponent.** Assume \(b<a^2\), write \(q=\log b/\log a>2\), and \(\Lambda=a^2/b>1\). Every point of \(K\) has a representation \((x,y)=\sum_{n\ge0}(a^nt_n,b^n s_n)\) with \(t_n^2+s_n^2\le1\). At fixed \(x\), the largest possible \(y\) is obtained by choosing \(s_n=\sqrt{1-t_n^2}\); hence the exact variational formula is
\[
D(x)=\min_{\substack{|t_n|\le1\\\sum_{n\ge0}a^nt_n=x}}\sum_{n\ge0}b^n\phi(t_n),\quad
\phi(t)=1-\sqrt{1-t^2},\quad \frac{t^2}{2}\le\phi(t)\le1.
\tag{4}
\]
The minimum exists by compactness. For \(0<|x|\ll1\), select \(N\) by \(a^{N+1}<|x|\le a^N\), set \(t_N=x/a^N\) and all other \(t_n=0\). Formula (4) gives \(D(x)\le b^N\le a^{-q}|x|^q\). For the reverse inequality, let \(E=D(x)<1\), choose \(N\ge0\) by \(b^{N+1}<E\le b^N\), and take any minimizing sequence in (4). Weighted Cauchy--Schwarz and \(\phi(t)\ge t^2/2\) yield
\[
\sum_{n\le N}a^n|t_n|
 \le\sqrt{2E\sum_{n\le N}\Lambda^n}
 \le a^N\sqrt{\frac{2\Lambda}{\Lambda-1}}.
\]
The tail contributes at most \(a^{N+1}/(1-a)\). Therefore, setting \(C_0=\sqrt{2\Lambda/(\Lambda-1)}+a/(1-a)\),
\[
|x|\le C_0 a^N <\frac{C_0}{a}E^{1/q},
\]
where the last strict inequality follows from \(b^N<E/b\) and \(b=a^q\). Hence
\[
\left(\frac a{C_0}\right)^q|x|^q\le D(x)\le a^{-q}|x|^q.
\tag{5}
\]
Taking logarithms in (5) proves the asserted exact exponent.

**5. Global \(C^2\) boundary and sharp \(C^3\) obstruction.** For any normal direction with \(\cos\theta\ne0\), (2) converges locally uniformly because its \(n\)-th term is bounded by \((b^2/a)^n/|\cos\theta|^3\), and \(b^2/a<1\). In those directions the support parametrization is regular and smooth, with strictly positive finite radius of curvature. When \(b\le a^2\), at the vertical normals each summand of (2) tends to \((a^2/b)^n\). Fatou's lemma therefore shows \(\rho(\theta)\to\infty\) as \(\theta\to\pi/2\) or \(-\pi/2\). At nonvertical nearby points the upper graph satisfies \(g'(x)=-\cot\theta\) and \(g''(x)=-1/(\rho(\theta)\sin^3\theta)\). These derivatives tend to \(0\) as \(x\to0\). Continuity of the normal supplies \(g'(0)=0\); the mean-value theorem then gives \(g''(0)=0\), and the graph is \(C^2\). The lower graph is identical by central symmetry. For \(b>a^2\), step 2 and uniform convergence of (2) give \(C^2\) also at the extrema.

Finally, the even function \(D(x)\) satisfies \(D(0)=D'(0)=D''(0)=0\) whenever \(b\le a^2\). If the boundary were \(C^3\) at the top point, evenness would force \(D'''(0)=0\), whence Taylor's theorem would give \(D(x)=o(|x|^3)\). In the critical case, (3) contradicts this. For \(a^3\le b<a^2\), one has \(2<q\le3\), and the lower bound (5) likewise contradicts it. This proves non-\(C^3\) at the top and bottom points.

## Verification

The companion standard-library-only `check_axis_contact.py` evaluates (1), including a cancellation-free expression for the second series; it checks a rational power-flat example \((a,b)=(1/2,1/6)\), the critical example \((1/2,1/4)\), and the positive-curvature example \((1/2,1/3)\). It also checks parameter inequalities using rational arithmetic. These finite computations support the formulas but do not replace the infinite-series estimates in the proof. Reproduce with `python3 check_axis_contact.py`.

## Relationship to prior work

Lamb, Rasmussen, and Tey (2023, arXiv:2310.03437v1) prove existence, strict convexity, global attraction, and \(C^1\) boundary regularity of this same disk-forced linear attractor. Tey's 2022 doctoral thesis, Appendix A.4, explicitly studies diagonal examples and gives a \(C^3\)-regularity obstruction based on a curvature derivative, under the distinct parameter restriction \(a^2<b<a^{3/2}\) (in positive diagonal notation). That prior obstruction does **not** entail the logarithmic contact law at \(b=a^2\), the quantified power-flat order for \(b<a^2\), or the \(C^2\) assertion in the newly analyzed range. The formulas here are compatible with, and explicitly do not claim to originate, either the attractor construction or earlier higher-regularity counterexamples. Kourliouros and collaborators (2023) give persistence criteria assuming smooth boundary normal bundles, without stating this trichotomy.

## Limitations

The theorem does not classify the full \(C^k\) boundary regularity for all \(b<a^3\), the possible log-periodic prefactor of the power-flat contact, smoothness under general nondiagonal matrices, or stochastic stationary densities. Constants in (5) need not be sharp. Priority cannot be proved by database search alone; an unindexed equivalent result remains possible. The proof and computational checks have not undergone an independent mathematical audit.

## References

1. J. S. W. Lamb, M. Rasmussen, W. H. Tey, *Attractors of Linear Maps with Bounded Noise* (2023), arXiv:2310.03437v1, https://arxiv.org/abs/2310.03437 .
2. W. H. Tey, *On Minimal Invariant Sets of Certain Set-Valued Dynamical Systems: A Boundary Map Approach* (doctoral thesis, 2022), Appendix A.4, DOI:10.25560/100849, https://spiral.imperial.ac.uk/entities/publication/379afb15-64aa-4685-8885-cc8dde5c2b27 .
3. K. Kourliouros, J. S. W. Lamb, M. Rasmussen, W. H. Tey, K. G. Timperi, D. Turaev, *Smooth Persistence of Attractors for Set-Valued Dynamical Systems: A Boundary Map Approach* (initial version 2023), arXiv:2303.01895v1, https://arxiv.org/abs/2303.01895 .
