# Exact sign probabilities and a logarithmic instability tail for random three-node quadrature

## Finding

Draw three independent uniform points in \([0,1]\), sort them as \(0<x<y<z<1\), and form the unique interpolatory quadrature rule
\[
Q(f)=W_x f(x)+W_y f(y)+W_z f(z),\qquad Q(p)=\int_0^1p(t)\,dt\quad(\deg p\le2).
\]
All equalities and inequalities below concern this exact rule. With probability one, either all weights are positive or exactly one weight is negative. Their exact probabilities are
\[
\begin{aligned}
\Pr(W_x>0,W_y>0,W_z>0)&=\tfrac12\log3-\tfrac13,\\
\Pr(W_y<0)&=\tfrac23,\\
\Pr(W_x<0)=\Pr(W_z<0)&=\tfrac13-\tfrac14\log3.
\end{aligned}
\]
For the quadrature operator norm \(L=|W_x|+|W_y|+|W_z|\), the *sharp* upper tail is
\[
\boxed{\lim_{t\to\infty}\frac{t}{\log t}\Pr(L>t)=2.}
\]
Consequently, for each real \(q>0\),
\[
\mathbb E[L^q]<\infty\quad\Longleftrightarrow\quad 0<q<1.
\]
The logarithmic factor is caused by simultaneous smallness of both adjacent spacings, not by a single two-node collision alone.

## Assumptions and scope

The nodes are three independent continuous uniform draws on the unit interval, conditioned only by sorting; the density of \((x,y,z)\) on the ordered simplex is six. Nodes are almost surely distinct, and the target integration measure is Lebesgue measure. The signed weights are uniquely determined by exact integration of polynomials of degree at most two. All calculations use exact real arithmetic. The variable \(t\) in the tail formula is the amplification threshold, not a quadrature node. The norm \(L\) is the sharp amplification factor for bounded, independently perturbed sampled values at the three nodes.

## Proof

**1. Weights and sign geometry.** Define
\[
F(a,b)=ab-\frac{a+b}{2}+\frac13
=\left(a-\frac12\right)\left(b-\frac12\right)+\frac1{12}.
\]
Integration of the three Lagrange cardinal polynomials gives
\[
W_x=\frac{F(y,z)}{(x-y)(x-z)},\qquad
W_y=\frac{F(x,z)}{(y-x)(y-z)},\qquad
W_z=\frac{F(x,y)}{(z-x)(z-y)}.
\]
Their sum equals one. Put \(u=2x-1\), \(v=2y-1\), \(w=2z-1\). Because \(F(a,b)=(1+3(2a-1)(2b-1))/12\), the endpoint weight signs are those of \(1+3vw\) and \(1+3uv\), whereas the middle weight sign is opposite to that of \(1+3uw\). If the left weight is negative, then \(v<0<w\) and \(vw<-1/3\); since \(u<v\), also \(uw<-1/3\), so the middle weight is positive, and since \(u,v<0\) the right weight is positive. The reflected statement holds if the right weight is negative. If the middle weight is negative, then \(uw>-1/3\), which precludes either endpoint from being negative by the same ordering argument. Thus no two weights can be negative simultaneously, apart from null boundary events.

For the sign probabilities, the ordered triple \((u,v,w)\) has density \(3/4\) on \(-1<u<v<w<1\). The middle weight is positive precisely when \(u=-a<0<w=b\), where \(a,b\in(0,1)\) and \(ab>1/3\); then \(v\) can range over an interval of length \(a+b\). In the same region, all three weights are positive precisely when
\[
-\frac1{3b}<v<\frac1{3a},
\]
an interval of length \(1/(3a)+1/(3b)\). Therefore
\[
\begin{aligned}
\Pr(W_y>0)&=\frac34\int_{1/3}^1\int_{1/(3a)}^1(a+b)\,db\,da=\frac13,\\
\Pr(W_x,W_y,W_z>0)&=\frac34\int_{1/3}^1\int_{1/(3a)}^1
\left(\frac1{3a}+\frac1{3b}\right)\,db\,da
=\frac12\log3-\frac13.
\end{aligned}
\]
Reflection exchanges the endpoint weights. Since no two weights are negative, the remaining probability \(1/3-(\log3/2-1/3)\) is split equally between the two endpoint-negative events. This proves all four sign probabilities, and their sum is one.

**2. Resolving the logarithmic tail.** Set \(p=y-x>0\), \(r=z-y>0\), and \(s=p+r\); then \((x,p,r)\) has density six on \(x>0,p>0,r>0,x+s<1\). Define \(g(x)=F(x,x)=x^2-x+1/3\), for which
\[
\frac1{12}\le g(x)\le\frac13,
\qquad\int_0^1g(x)\,dx=\frac16.
\]
Fix any sufficiently small \(\delta>0\), for example \(\delta<1/24\). On \(p,r<\delta\), one has \(|F(x,z)-g(x)|\le\delta\) and hence \(F(x,z)>0\). Therefore the middle weight is negative, the other two are positive, and
\[
L=1-2W_y=1+\frac{2F(x,x+p+r)}{pr}.
\]
The exact planar area identity, valid for \(0<\varepsilon<\delta^2\), is
\[
\operatorname{area}\{(p,r)\in(0,\delta)^2:pr<\varepsilon\}
=\varepsilon\left(1+\log\frac{\delta^2}{\varepsilon}\right).
\]
To obtain an upper bound for the near-collision tail, replace \(F\) by \(g(x)+\delta\), enlarge the available interval of \(x\) to \([0,1]\), and apply this area identity with \(\varepsilon=2(g(x)+\delta)/(t-1)\). For a lower bound, use \(g(x)-\delta\) and restrict \(x\) to \([0,1-2\delta]\), which is feasible for every \(p,r<\delta\). These yield
\[
12\int_0^{1-2\delta}(g(x)-\delta)\,dx
\le\liminf_{t\to\infty}\frac{t\Pr(L>t,\ p,r<\delta)}{\log t}
\le\limsup_{t\to\infty}\frac{t\Pr(L>t,\ p,r<\delta)}{\log t}
\le12\int_0^1(g(x)+\delta)\,dx.
\]
Here the factor twelve is the ordered-node density six multiplied by the numerator factor two in the hyperbolic threshold.

For completeness, the complement \(\max\{p,r\}\ge\delta\) does not contribute at logarithmic order. The polynomial \(F\) is bounded uniformly on the unit square. The weight formulas show that if, say, \(p\ge\delta\), then \(L\le C_\delta(1+1/r)\) for a finite constant \(C_\delta\). Consequently \(L>t\) forces \(r=O_\delta(t^{-1})\), a region of probability \(O_\delta(t^{-1})\); the case \(r\ge\delta\) is symmetric. Hence the complement's contribution to \(t\Pr(L>t)/\log t\) tends to zero. Finally let \(\delta\downarrow0\). Both bounds converge to
\[
12\int_0^1g(x)\,dx=12\cdot\frac16=2,
\]
proving the claimed tail coefficient.

**3. Sharp moment boundary.** Since \(L\ge1\), the layer-cake identity gives for every \(q>0\)
\[
\mathbb E[L^q]=q\int_0^\infty t^{q-1}\Pr(L>t)\,dt.
\]
The proved tail is asymptotic to \(2(\log t)/t\), so the integral converges at infinity precisely for \(q<1\); at \(q=1\), logarithmic divergence is strict. This finishes the proof.

## Verification

The accompanying standalone `verify.py` uses standard-library exact fractions to check the three polynomial moments and exclusion of simultaneous negative weights for all 560 ordered node triples from a 16-point rational interior lattice. It also checks the exact sign integrals against high-resolution deterministic numerical integration, the symbolic tail constant \(12\int_0^1g=2\), and the two-spacing area formula, with a fixed-seed simulation used only as an independent sign-frequency sanity check. Invoke `python3 verify.py`. The checker does **not** replace the limiting probability argument or prove the theorem by enumeration.

## Relationship to prior work

Van den Bos, Sanderse, Bierbooms, and van Bussel (2018) develop subsampling and positive-weight quadrature construction from arbitrary sample sets, and explicitly identify the sum of absolute quadrature weights as an operator condition measure. Their construction selects/adapts nodes and weights; it does not supply the present probability distribution for the unique, unmodified three-node interpolatory rule. Van den Bos and Sanderse (2019) characterize deterministic node additions that retain positive quadrature weights; those inequalities are compatible with the present event geometry but do not themselves state the integrated sign probabilities or its logarithmically enhanced instability tail. Yu and Townsend (2022) show negativity can arise on perturbed trigonometric grids and obtain an absolute-weight bound for well-separated node perturbations; those separated grids do not cover freely colliding uniform polynomial nodes. Neumayer, Schäfer, and Ullrich (2026) establish existence of positive rules with independently random candidates after oversampling and adapting the weights; their construction is stronger for obtaining an achievable positive rule but does not imply positivity probabilities or an instability tail for the *unique*, unadapted, three-node square Vandermonde solve. Existing fixed-node Newton–Cotes and related interpolation analyses concern different node laws or norms.

The general formula for Lagrange quadrature weights, the implication of positive weights for a norm-one rule, and elementary two-dimensional hyperbola integration are classical and not claimed as independent discoveries. The contribution assessed here is the combined exact sign law with the sharp logarithmically enhanced tail constant in this natural minimal random-node model. Specialized older random-quadrature literature could contain a prior equivalent and remains an explicit priority-verification risk.

## Limitations

The conclusions are for three independent **uniform** nodes and polynomial exactness through degree two. They do not classify larger node counts, weighted node distributions, optimally chosen/oversampled positive quadrature, Gaussian or adaptive nodes, finite-precision conditioning, or the numerical error of a particular integrand. The infinite expected operator norm is an unconditional risk statement; it does not imply that the error for every fixed smooth integrand is infinite. Independent review and comprehensive priority verification have not been performed.

## References

1. L. M. M. van den Bos, B. Sanderse, W. A. A. M. Bierbooms, and G. J. W. van Bussel, *Generating nested quadrature rules with positive weights based on arbitrary sample sets*, arXiv:1809.09842, first submitted 2018-09-26. https://arxiv.org/abs/1809.09842
2. L. M. M. van den Bos and B. Sanderse, *A geometrical interpretation of the addition of nodes to an interpolatory quadrature rule while preserving positive weights*, arXiv:1902.07477, first submitted 2019-02-20. https://arxiv.org/abs/1902.07477
3. A. Yu and A. Townsend, *On the stability of unevenly spaced samples for interpolation and quadrature*, arXiv:2202.04722, first submitted 2022-02-09. https://arxiv.org/abs/2202.04722
4. S. Neumayer, M. Schäfer, and T. Ullrich, *Random nodes with positive weights: Richter–Tchakaloff rules and optimal positive quadrature*, arXiv:2610.32699, first submitted 2026-10-23. https://arxiv.org/abs/2610.32699
