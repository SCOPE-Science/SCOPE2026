# A finite mixing-rate maximum of opinion volatility in a four-agent gossip chain

## Finding

Consider two regular agents with opinions \(X,Y\in[0,1]\), one fixed-opinion agent at \(0\), and one fixed-opinion agent at \(1\). Let the four independent directed Poisson meetings and their receiver updates be as specified below. For each stubborn-contact rate \(a>0\), mutual-contact rate \(m\geq0\), and common trust fraction \(0<\theta\leq1\), there is a unique stationary opinion law. Put \(u=m/a\). The two regular agents have stationary means

\[
\mathbb E[X]=\frac{u}{1+2u},\qquad
\mathbb E[Y]=\frac{1+u}{1+2u},
\]

and **identical individual stationary variances**

\[
V_\theta(u):=\operatorname{Var}(X)=\operatorname{Var}(Y)
=\frac{\theta u(1+u)^2}
{(1+2u)^2[(2-\theta)+(4-3\theta)u]}.
\]

For every \(0<\theta<1\), this variance has **exactly one strict global maximum** over finite \(u\geq0\), attained at

\[
u_*(\theta)=\frac{(2-\theta)+\sqrt{(2-\theta)(18-17\theta)}}{8(1-\theta)}.
\]

It increases strictly on \([0,u_*)\) and decreases strictly on \((u_*,\infty)\). Nevertheless the stationary expected opinion gap \(\mathbb E[Y-X]=1/(1+2u)\) strictly decreases for all finite \(u\geq0\). The strong-contact limit is \(\lim_{u\to\infty}V_\theta(u)=\theta/[4(4-3\theta)]\), strictly below the finite maximum. At the full-copying boundary \(\theta=1\), the variance instead increases strictly to its unattained limit \(1/4\), with no finite maximum. The maximizing rate diverges according to \(\lim_{\theta\uparrow1}(1-\theta)u_*(\theta)=1/4\).

For example, at \(\theta=1/2\), the maximum occurs at \(u_*=(3+\sqrt{57})/8\approx1.3187293044\), with variance \((19\sqrt{57}-143)/8\approx0.0558567838\), exceeding the infinite-mixing limit \(1/20\).

## Assumptions and scope

The directed interactions follow four independent Poisson processes. At rate \(a\), the first regular agent encounters the stubborn opinion \(0\) and updates \(X\leftarrow(1-\theta)X\); at rate \(a\), the second regular agent encounters the stubborn opinion \(1\) and updates \(Y\leftarrow(1-\theta)Y+\theta\). At rate \(m\) for each direction, the first regular agent encounters the second and updates \(X\leftarrow(1-\theta)X+\theta Y\), or the second encounters the first and updates \(Y\leftarrow(1-\theta)Y+\theta X\). The other agent never changes at that event. Only the receiver updates, and the meeting clocks are not normalized to a fixed aggregate meeting rate.

All claims apply to every \(a>0\), \(m\geq0\), \(0<\theta\leq1\), and initial \((X,Y)\in[0,1]^2\). They concern limiting stationary moments, not sample-path convergence to a fixed opinion. The stubborn opinions \(0,1\) may be replaced by any distinct constants by an affine change of opinion units, multiplying the stated variances by the square of their difference.

## Proof

Each update preserves the compact state square and is nonexpansive in the supremum norm under synchronous coupling. For any \(a>0\), the specific two-event block consisting of first a contact with the stubborn opinion \(0\) and then a contact with the stubborn opinion \(1\) has strictly positive probability in the sequence of Poisson meeting types (also when \(m=0\)). Such a block contracts the coupled opinion-vector difference by at least \(1-\theta\), while every other update is nonexpansive. Infinitely many independent blocks of this type occur almost surely; hence all initial states couple asymptotically. Compactness gives an invariant law, and the coupling proves its uniqueness.

Write \(Z=(X+Y-1)/2\), \(D=(Y-X)/2\), and
\[
L=a(2-\theta)+m(4-3\theta)>0.
\]
Stationarity of the infinitesimal generator applied to \(Z,D,ZD,Z^2,D^2\) gives, successively,
\[
\mathbb E[Z]=0,\quad
\mathbb E[D]=\frac{a}{2(a+2m)},\quad
\mathbb E[ZD]=0,
\]
\[
\mathbb E[Z^2]=\frac{m\theta(a+m)}{2(a+2m)L},\qquad
\mathbb E[D^2]=\frac{a[a(2-\theta)+m\theta]}{4(a+2m)L}.
\]
These identities follow by substituting the four affine update maps in the generator and solving its two remaining linear quadratic-moment equations. Since \(X=1/2+Z-D\), \(Y=1/2+Z+D\), and \(\mathbb E[ZD]=0\), one has
\[
\operatorname{Var}(X)=\operatorname{Var}(Y)
=\mathbb E[Z^2]+\mathbb E[D^2]-(\mathbb E[D])^2.
\]
Algebraic simplification gives the displayed rational expression for \(V_\theta(u)\) and the means.

Direct differentiation, with the denominator positive throughout the allowed domain, yields
\[
\frac{dV_\theta}{du}=
\frac{\theta(1+u)[(2-\theta)(1+u)-4(1-\theta)u^2]}
{(1+2u)^3[(2-\theta)+(4-3\theta)u]^2}.
\]
For \(0<\theta<1\), the quadratic in the numerator has a positive constant term and negative leading coefficient, so it has exactly one positive root. Solving for that root gives \(u_*(\theta)\), with the derivative positive before and negative after it. The limiting variance is obtained by comparing the highest powers of \(u\) in the rational expression. This proves strict global maximality and the contrast with the monotone decreasing mean gap.

For \(\theta=1\), cancellation gives \(V_1(u)=u(1+u)/(1+2u)^2\) and \(dV_1/du=(1+2u)^{-3}>0\); thus no finite maximizer exists. Finally, multiplying the formula for \(u_*\) by \(1-\theta\) and taking \(\theta\uparrow1\) gives \(1/4\). This exhausts all asserted parameter boundaries.

## Verification

The standalone `verify.py` constructs the four-event polynomial generator independently in \(X,Y\), solves five stationary moment equations by exact rational linear algebra at 48 parameter triples (including \(m=0\) and \(\theta=1\)), checks both predicted variances and means, tests nonnegative covariance determinants, verifies the derivative symbolically, and reconstructs the \(Z,D\) stationary identities symbolically. Run `python verify.py` with Python 3 and SymPy. The executed program reported all checks passing. The infinite-domain sign and uniqueness results are proved analytically above; finite checks are not substituted for those proofs.

## Relationship to prior work

Acemoglu, Como, Fagnani and Ozdaglar (arXiv:1009.2653; first posted 2010-09-14) introduce the stochastic pairwise-averaging model with stubborn agents, prove stationary-moment characterizations through coupled Markov chains, and discuss line-graph examples. These general stationary equations and existence theory are established results, not claimed here. Their explicit tree variance calculation in Section 5 addresses full copying, \(\theta=1\). The present statement specializes the same model to a four-node motif, derives its partial-trust rational variance, and solves the **entire rate-dependence and optimization problem** for \(0<\theta<1\), including the singular \(\theta\uparrow1\) boundary.

Yildiz, Acemoglu, Ozdaglar, Saberi and Scaglione (2011 preprint; 2013 journal) analyze binary full-copying opinion dynamics and network-related variances; their binary setting corresponds to \(\theta=1\), not the partial-trust interior optimum. Frasca, Ravazzi, Tempo and Ishii (arXiv:1304.2268; posted 2013-04-08) analyze gossip with persistent personal prejudices; the core question there is ergodicity and mean convergence under a different update mechanism, rather than the present exact stationary individual-variance maximizer. A general-purpose stationary-moment solver could of course recover the rational formula, but the global sign classification and sharp trust boundary require the additional parameter analysis above.

## Limitations

This is an exact theorem for a symmetric four-agent chain with identical trust fractions and Poisson meeting clocks. It does not assert the same rate-volatility profile for heterogeneous graphs, trust fractions, synchronous interactions, or empirical social groups. Individual variance is a mathematical fluctuation measure, not a directly validated welfare or polarization index. The result has no claim of independent audit; novelty is qualified by possible older equivalent parameter optimizations not found in the inspected sources.

## References

1. D. Acemoglu, G. Como, F. Fagnani, A. Ozdaglar, *Opinion fluctuations and disagreement in social networks*, arXiv:1009.2653 (first posted 2010-09-14), https://arxiv.org/abs/1009.2653 .
2. E. Yildiz, D. Acemoglu, A. Ozdaglar, A. Saberi, A. Scaglione, *Discrete Opinion Dynamics with Stubborn Agents*, 2011 preprint; *ACM Transactions on Economics and Computation* 1(4) (2013), https://web.mit.edu/Asuman/Desktop/asuman/www/documents/voter-submit.pdf ; https://doi.org/10.1145/2538508 .
3. P. Frasca, C. Ravazzi, R. Tempo, H. Ishii, *Gossips and Prejudices: Ergodic Randomized Dynamics in Social Networks*, arXiv:1304.2268 (first posted 2013-04-08), https://arxiv.org/abs/1304.2268 .
