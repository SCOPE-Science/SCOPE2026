# Acute-triangle law and a seven-halves transition for random rectangle-boundary triples

## Finding
Choose three independent points uniformly with respect to normalized arclength on the boundary of a Euclidean rectangle whose long-to-short side ratio is \(r\geq1\). Let \(F(r)\) be the probability that their three pairwise interior angles are strictly acute. Define
\[
 B(r)=2r^2+r^3\left(\frac{17}{9}+\frac r6-\frac23\log r\right),\qquad
 S(r)=2r+\frac{17}{9}+\frac1{6r}+\frac23\log r.
\]
Put \(C(r)=0\) for \(1\leq r\leq2\). For \(r>2\), set \(d=\sqrt{r^2-4}\) and \(T=\operatorname{arcosh}(r/2)\), and put
\[
 C(r)=\left(\frac{2r^3}{3}-4r-4\right)T+
 d\left(-\frac{r^3}{6}-\frac{5r^2}{9}+\frac{5r}{3}+\frac{32}{9}\right).
\]
Then the *complete aspect-ratio law* is
\[
 \boxed{F(r)=1-\frac{3\,[B(r)+S(r)+C(r)]}{4(r+1)^3}}\quad(r\geq1).
\]
In particular \(F(1)=23/96\), a previously published special value, and \(F(2)=0.207907967850363\ldots\). There is a nonanalytic transition at the precise aspect ratio \(r=2\). If \(F_{\mathrm{an}}\) is the analytic continuation of the formula for \(1\leq r\leq2\), then
\[
 \boxed{F(2+\varepsilon)-F_{\mathrm{an}}(2+\varepsilon)
  =\frac4{945}\,\varepsilon^{7/2}+O(\varepsilon^{9/2})}
\qquad(\varepsilon\downarrow0).
\]
Consequently \(F\) is \(C^3\) but not \(C^4\) at \(r=2\). In the thin-rectangle limit,
\[
 \boxed{F(r)=\frac{3\log r-3/2}{r^2}+O\!\left(\frac{\log r}{r^3}\right)}\qquad(r\to\infty).
\]

## Assumptions and scope
The rectangle is \([0,r]\times[0,1]\); scaling and rigid motions leave \(F\) unchanged. The three sampling locations are independent, each distributed proportionally to Euclidean arclength across all four sides, with perimeter \(2(r+1)\). Strict acuteness requires positivity of the three dot products at the sampled vertices. Triples lying on one straight side have positive probability and are declared nonacute (the median vertex has a straight angle). Coincidence, boundary corners, and noncollinear right angles have probability zero.

## Proof
Fix a point \(X=(x,0)\) of the bottom side of a general rectangle \([0,w]\times[0,h]\), and set \(s=x(w-x)\). Let \(A_{w,h}(x)\) be the *unnormalized, ordered* double-arclength measure of pairs \((Y,Z)\) for which \((Y-X)\cdot(Z-X)<0\). Partition according to which sides contain \(Y,Z\). Elementary coordinate products give
\[
 A_{w,h}(x)=2wh+6s+2(L+R+G+H),
\]
where
\[
 L=\int_0^{w-x}\min\!\left(h,\frac{xt}{h}\right)dt,\quad
 R=\int_0^{x}\min\!\left(h,\frac{(w-x)t}{h}\right)dt,
\]
\[
 G=\int_0^h\int_0^h\mathbf1_{uv<s}\,du\,dv,\qquad
 H=\int_0^x\int_0^{w-x}\mathbf1_{uv>h^2}\,du\,dv.
\]
The first term counts ordered pairs with at least one point on the supporting bottom side. The \(L,R\) terms are pairs on one vertical side and the opposite top side; \(G\) counts left–right vertical pairs; \(H\) counts both points on the opposite top side. All other pairings have nonnegative dot product. The factor two in the last three groups reflects the order of \(Y,Z\); the bottom-side term already accounts for ordering without double counting opposite bottom directions.

Normalize the short side to \(h=1\) and write \(w=r\). Direct integration over the parameters \(u,v,t\) yields, with \(s=x(r-x)\),
\[
 A_{r,1}(x)=
 \begin{cases}
 2r+(8+r)s-2s\log s,&0\leq s\leq1,\\
 4r+8s-r/s-2\log s,&s\geq1.
 \end{cases}
\]
The value at \(s=0\) is taken by continuity. On a short side, interchanging width and height yields \(A_{1,r}\), always in the first branch. Its integral equals \(S(r)\) defined above. Similarly integrating the first branch over the entire long side yields \(B(r)\), because
\[
 \int_0^r x(r-x)\,dx=\frac{r^3}{6},\qquad
 \int_0^r x(r-x)\log[x(r-x)]\,dx
 =r^3\left(\frac{\log(r^2)}6-\frac5{18}\right).
\]
For \(r\leq2\), \(x(r-x)\leq r^2/4\leq1\), so there is no correction. For \(r>2\), the second branch occurs on \((\alpha,\beta)\), where \(\alpha=(r-d)/2\), \(\beta=(r+d)/2\), \(\alpha\beta=1\). The second-minus-first branch difference simplifies to
\[
 \Delta A=-\frac{r(s-1)^2}{s}+2(s-1)\log s.
\]
Let \(T=\log\beta=\operatorname{arcosh}(r/2)\). Four elementary definite integrals on \((\alpha,\beta)\) are
\[
 \int s\,dx=\frac{d(r^2+2)}6,\quad
 \int\frac{dx}{s}=\frac{4T}{r},\quad
 \int\log s\,dx=2rT-2d,
\]
\[
 \int s\log s\,dx=\frac{r^3T}{3}-\frac{d(5r^2+4)}{18}.
\]
Substitution into \(\int_{\alpha}^{\beta}\Delta A\,dx\) yields exactly \(C(r)\).

A nondegenerate planar triangle has at most one angle \(\geq\pi/2\). The same exclusivity holds for collinear triples from one side if their median angle is counted as \(\pi\). Thus the failure probability is three times the probability of a nonacute angle at a specified sampled point. Integrating the ordered-pair masses on the two long and two short sides gives
\[
 \Pr(\hbox{angle at }X\hbox{ nonacute})=
 \frac{2\int_0^r A_{r,1}(x)dx+2\int_0^1 A_{1,r}(y)dy}{[2(r+1)]^3}
 =\frac{B(r)+S(r)+C(r)}{4(r+1)^3}.
\]
This proves the complete law, including normalization and all parameter boundaries.

To obtain the transition, write \(r=2+\varepsilon\) and \(x=r/2+\sqrt\varepsilon\,t\) inside the emerging interval \((\alpha,\beta)\). Then \(s-1=\varepsilon(1-t^2)+O(\varepsilon^2)\), and uniformly after rescaling, \(\Delta A=-\varepsilon^3t^2(1-t^2)^2+O(\varepsilon^4)\). Consequently
\[
 C(2+\varepsilon)=-\varepsilon^{7/2}
 \int_{-1}^1t^2(1-t^2)^2dt+O(\varepsilon^{9/2})
 =-\frac{16}{105}\varepsilon^{7/2}+O(\varepsilon^{9/2}).
\]
Multiplying by \(-3/[4(r+1)^3]\) gives \(4/945\). The analytic background has no fractional powers, proving the stated exact differentiability. Lastly, expanding \(d=r\sqrt{1-4/r^2}\) and \(T=\log r+\log[(1+\sqrt{1-4/r^2})/2]\) to sufficient orders and cancelling all larger powers gives the thin-rectangle expansion displayed in the finding.

## Verification
Run `python verify.py` with Python 3 and NumPy, SciPy, and mpmath installed. The script independently evaluates the *unintegrated* ordered side-pair conditions by numerical quadrature (rather than reusing the final antiderivative), directly samples three Cartesian boundary points at six aspect ratios, checks the previously known square value, and tests both new asymptotic coefficients with high precision. Random samples are finite corroboration; the formulas and all limiting claims follow from the analytic proof above.

## Relationship to prior work
The previously published square-boundary calculation yields \(F(1)=23/96\) and explicitly addresses the same arclength-sampling model at the single aspect ratio \(1\) (Mathematics Stack Exchange, 2012 answer, subsequently edited). It is *not* claimed as a new result here. Edelman and Strang (2015) study Gaussian triangle-shape measures, which do not determine non-Gaussian rectangle-boundary probabilities. Portnoy (1994) discusses invariance-based models of random obtuse triangles, not the specified one-parameter rectangle model in its accessible description. The new content is the general all-aspect expression, the sharp aspect-ratio \(2\) differentiability transition, and the thin-rectangle asymptotics. Public literature and mathematical-record searches found no statement with equal or stronger coverage; this is not an exhaustive historical-priority certification.

## Limitations
No monotonicity theorem, extremal theorem among arbitrary convex domains, or arclength density other than uniformity is asserted. The cusp coefficient is attached to the analytic continuation of the short-aspect formula, not to \(F(2+\varepsilon)-F(2)\). The formula is for rectangle boundaries, not interiors. Numerical evaluation at huge \(r\) should use arbitrary precision because the elementary closed form has cancellations. Related historical material may be incompletely indexed, and independent validation is not performed.

## References
- Mathematics Stack Exchange, “What's the probability that three points determine an acute triangle?”, question 126719, answer published 9 April 2012, later edited; the boundary-square calculation appears in the accessible answer. https://math.stackexchange.com/questions/126719/
- A. Edelman and G. Strang, “Random Triangle Theory with Geometry and Applications”, arXiv:1501.03053, first posted 9 January 2015. https://arxiv.org/abs/1501.03053
- S. Portnoy, “A Lewis Carroll Pillow Problem: Probability of an Obtuse Triangle”, *Statistical Science* 9 (1994), 279–284. https://doi.org/10.1214/ss/1177010497
