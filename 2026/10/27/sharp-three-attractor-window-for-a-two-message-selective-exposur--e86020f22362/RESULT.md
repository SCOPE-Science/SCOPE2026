# Sharp three-attractor window for a two-message selective-exposure map

## Finding

Let \(\beta>1\), and set \(b=\beta-1\). The scalar, infinite-source message-preference map with zero intrinsic anchoring, preference parameter \(\alpha=1\), and equally probable source messages \(0\) and \(1\) is
\[
F_b(x)=\frac{[x(2-x)]^b}{[x(2-x)]^b+(1-x^2)^b},\qquad 0\leq x\leq1.
\]
For every initial opinion \(x_0\in[0,1]\), define \(x_{t+1}=F_b(x_t)\). Its complete fixed-point and basin classification is:

1. If \(1<\beta\leq2\), the fixed points are exactly \(0,1/2,1\). Every initial opinion in \((0,1)\) converges to \(1/2\); the two endpoints are fixed but repel interior opinions.
2. If \(2<\beta<5/2\), there are exactly five fixed points \(0,1-r_\beta,1/2,r_\beta,1\), with \(1/2<r_\beta<1\). The three points \(0,1/2,1\) attract nonempty open intervals and the two separating points repel. More precisely, the three open basins are \((0,1-r_\beta)\), \((1-r_\beta,r_\beta)\), and \((r_\beta,1)\), in that order. Each separator stays fixed when initialized exactly there.
3. If \(\beta\geq5/2\), the fixed points are exactly \(0,1/2,1\). Every opinion in \((0,1/2)\) converges to \(0\), and every opinion in \((1/2,1)\) converges to \(1\). The midpoint is repelling, including at the nonhyperbolic threshold \(\beta=5/2\).

In the five-point regime, \(r_\beta\) is the **unique** solution in \((1/2,1)\) to
\[
\frac{\log(x/(1-x))}{\log((1+x)/(2-x))}=\frac{\beta-1}{\beta-2}.
\]
As \(\beta\uparrow5/2\) from below, its distance from the midpoint has the sharp collision law
\[
r_\beta-\frac12=\frac{3}{2\sqrt2}\sqrt{\frac52-\beta}+O\!\left((\frac52-\beta)^{3/2}\right).
\]
At the critical endpoint the local drift is
\[
F_{3/2}\left(\frac12+u\right)-\left(\frac12+u\right)=\frac{16}{27}u^3+O(u^5).
\]
The five-point regime is stable under modest **source-probability asymmetry**: for each fixed \(2<\beta<5/2\), there is \(\delta_\beta>0\) such that replacing the equiprobable messages with probability \(p\in(1/2-\delta_\beta,1/2+\delta_\beta)\) of message \(1\) leaves exactly five fixed points, three attracting and two repelling, with the same basin alternation.

## Assumptions and scope

A scalar opinion is in \([0,1]\); two available message values are \(0\) and \(1\). The message-preference rule assigns weight \([1-(x-s)^2]^{\beta-1}\) to message \(s\) when \(\alpha=1\), following the cited two-step communication model. The opinion-leader's intrinsic anchoring parameter is zero. In the infinite-source expectation limit with source \(1\) probability \(p\in(0,1)\), the resulting deterministic update is
\[
F_{b,p}(x)=\frac{p[x(2-x)]^b}{p[x(2-x)]^b+(1-p)(1-x^2)^b}.
\]
The principal theorem has \(p=1/2\). Finite numbers of freshly sampled source messages instead produce a random, time-dependent update and **are not** asserted to have these deterministic basins or stationary point values. Neither opinions of downstream agents nor networks of interacting leaders are part of this claim. All statements concern the full domain \(x\in[0,1]\), real \(\beta>1\), and discrete time \(t\in\{0,1,2,\ldots\}\).

## Proof

**1. Exact reduction and order.** Under the binary distribution, the expected weighted message numerator is \(p[1-(1-x)^2]^b\), and the normalizing denominator adds \((1-p)[1-x^2]^b\). This is exactly the stated \(F_{b,p}\). For \(p=1/2\), its endpoint values are \(F_b(0)=0\) and \(F_b(1)=1\), and it obeys \(F_b(1-x)=1-F_b(x)\). The ratio of positive-to-negative message weights is strictly increasing for \(x\in(0,1)\) because \(x(2-x)\) is increasing and \(1-x^2\) decreasing. Hence \(F_b\) is strictly increasing and continuous. The midpoint is fixed by symmetry.

**2. Uniqueness of any additional fixed point.** For \(1/2<x<1\), introduce
\[
P(x)=\log\frac{x}{1-x},\qquad Q(x)=\log\frac{1+x}{2-x},\qquad K(x)=\frac{P(x)}{Q(x)}.
\]
Both \(P\) and \(Q\) are positive there and vanish at \(1/2\). Since the log-odds function is strictly increasing,
\[
\operatorname{sgn}(F_b(x)-x)
=\operatorname{sgn}\bigl[(b-1)P(x)-bQ(x)\bigr]
=\operatorname{sgn}\bigl[(b-1)K(x)-b\bigr].
\]
Differentiation gives
\[
\frac{P'(x)}{Q'(x)}=\frac13+\frac{2}{3x(1-x)},
\]
which strictly increases on \((1/2,1)\). Since \(P(x)=\int_{1/2}^xP'(u)\,du\) and \(Q(x)=\int_{1/2}^xQ'(u)\,du\), their ratio \(K(x)\) is strictly increasing (the weighted-average form of the monotone l'Hôpital rule). It has limits \(3\) at \(1/2\) and \(+\infty\) at \(1\).

If \(0<b\leq1\), then \((b-1)K-b<0\) on \((1/2,1)\), so there is no other fixed point. If \(1<b<3/2\), the level \(b/(b-1)>3\) is crossed exactly once by \(K\), defining \(r_\beta\), with \(F_b(x)<x\) on \((1/2,r_\beta)\) and \(F_b(x)>x\) on \((r_\beta,1)\). If \(b\geq3/2\), then \((b-1)K-b>0\) for every \(x>1/2\), including strict positivity when \(b=3/2\) because \(K(x)>3\). Reflection supplies the complete fixed-point census on \((0,1/2)\).

**3. Dynamics and boundary types.** An increasing continuous interval map cannot overshoot a fixed point. On each fixed-point interval the sign of \(F_b(x)-x\) is constant, so all forward orbits are monotone, bounded, and converge to an endpoint of that interval. Step 2 then gives exactly the advertised basins. The midpoint derivative is \(F_b'(1/2)=2b/3\). For \(b>1\), \(F_b(x)\sim(2x)^b\) as \(x\downarrow0\), proving attraction to the endpoints when \(b>1\); for \(b\leq1\) the drift points away from the endpoints. The interior separators are strictly repelling: at their positive-side root \(r\), the derivative of the log-odds difference is \((b-1)Q(r)K'(r)>0\), implying \(F_b'(r)>1\). The midpoint is repelling for \(b>3/2\) by its derivative. At \(b=3/2\), the strictly outward drift from Step 2 gives repulsion despite derivative one.

**4. Sharp collision.** Set \(x=1/2+u\). Direct Taylor expansions yield
\[
K(1/2+u)=3+\frac{32}{9}u^2+O(u^4),
\qquad\frac{b}{b-1}=3+4(3/2-b)+O((3/2-b)^2).
\]
Monotonicity and inversion prove the square-root law, with the asserted \(O((3/2-b)^{3/2})\) remainder. Substituting \(b=3/2\) into the map and expanding gives the cubic drift shown above.

**5. Stability against unequal source frequencies.** For any fixed \(1<b<3/2\), the three interior fixed points at \(p=1/2\) are hyperbolic; the two endpoints are also hyperbolically attracting because the one-sided derivative is zero. Their fixed-point equations therefore persist locally as \(p\) varies near \(1/2\), with types unchanged, while \(0\) and \(1\) remain exact fixed points. On compact subintervals excluding these five neighborhoods, \(F_{b,1/2}(x)-x\) is bounded away from zero, so small changes of \(p\) create no roots there. Uniformly for \(p\) near \(1/2\), the endpoint asymptotics \(F_{b,p}(x)=O(x^b)\) and \(1-F_{b,p}(1-x)=O(x^b)\) exclude hidden extra roots near endpoints. Local derivative bounds exclude extra roots in the three interior neighborhoods. Thus the census and attracting/repelling alternation persist.

## Verification

The included `verify.py` checks, using SymPy exact identities and high-precision mpmath computations, the log-derivative identity, the critical cubic coefficient, the root equation for several noninteger exponents, the drift signs, the square-root collision, numerical persistence under small source asymmetry, and monotonicity of sample trajectories. It prints a pass total when all checks succeed. These finite checks are supplementary; the monotonic-quotient and interval arguments above prove the all-parameter statements.

## Relationship to prior work

Wang, Li, Lin and Zhao [1] introduced the two-step model and the precise message-preference weights used here. Their infinite-source equation (9) is the parent nonlinear fixed-point equation; their treatment focuses on empirically fitted steady-state approximations and beta-distributed message experiments rather than exact binary-message fixed-point multiplicity. The three-attractor window and two sharp thresholds are the claimed new specialization, not the underlying model.

Mao, Bolouki and Akyol [2] studied a different state-dependent source-weight cyber-social model and gave a sufficient contraction criterion for unique equilibrium; their news-source weights are strictly positive and their theorem is conditional on a Lipschitz bound, which does not imply the present five-fixed-point classification. Xia, Ye, Liu, Cao and Sun [3] treated a different nonlinear biased-assimilation rule involving the neighbors' weighted opinions and powers of the agent's opinion; their network phase distinctions do not imply the stated thresholds for the source-normalized \([1-(x-s)^2]^b\) kernel. In general, confirmation-bias-driven polarization predates this analysis. No universal claim of priority over every equivalent scalar-map formulation is made.

## Limitations

The exact classification uses a two-atom message distribution, no intrinsic anchoring, one scalar opinion, and the deterministic infinite-source limit. Distinct source distributions, finite random source batches, positive anchoring, or interacting leaders can exhibit different phase diagrams. Stability of equilibria is dynamical in the deterministic map, not a statement about the real-world reliability of an opinion. The numerical verifier alone is not a proof. Publication-priority uncertainty from potentially unlocated equivalent scalar maps remains, and no independent audit is claimed.

## References

[1] H. Wang, Y. Li, Y. Lin and H. V. Zhao, *Opinion Dynamics in Two-Step Process: Message Sources, Opinion Leaders and Normal Agents*, arXiv:2309.05370v1 (first submitted 2023-09-11), especially Eqs. (2), (3), (9) and Sections IV–V. https://arxiv.org/html/2309.05370v1

[2] Y. Mao, S. Bolouki and E. Akyol, *Spread of Information with Confirmation Bias in Cyber-Social Networks*, arXiv:1803.06377v1 (2018), model Eq. (1) and Theorem 1. https://arxiv.org/pdf/1803.06377

[3] W. Xia, M. Ye, J. Liu, M. Cao and X.-M. Sun, *Analysis of a Nonlinear Opinion Dynamics Model with Biased Assimilation*, arXiv:1912.01778v1 (2019), model Eq. (1) and Section III. https://arxiv.org/pdf/1912.01778
