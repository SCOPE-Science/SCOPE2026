# Sharp random-distance moment envelopes and inverse rigidity for rectangular max-metric tori

## Finding
For every integer \(d\ge2\), the **entire random-distance law** of a rectangular flat torus with its quotient max metric recovers its dimension and every circle length up to permutation. Moreover, for all real exponents \(p>q>0\), the ratio of the \(p\)-th distance moment to the \(p/q\)-power of the \(q\)-th moment has the exact sharp bounds
\[
\boxed{\frac{d/(d+p)}{(d/(d+q))^{p/q}}\ \le\
\frac{\mathbb E[D^p]}{(\mathbb E[D^q])^{p/q}}\ <\
\frac{1/(1+p)}{(1/(1+q))^{p/q}}.}
\]
The left equality holds **only** for equal circle lengths; the right-hand supremum is not attained by any strictly positive length vector and is approached when all but one circle collapse relative to the longest. In particular,
\[
\boxed{1+\frac{1}{d(d+2)}\le \frac{\mathbb E[D^2]}{(\mathbb E D)^2}<\frac43.}
\]
The sharp bounds hold simultaneously for every pair of real exponents and show that the cubic max-metric torus has the smallest normalized dispersion. The upper limit is a one-dimensional collapse law.

## Assumptions and scope
Fix an integer \(d\ge2\) and arbitrary \(a_i>0\). Define the rectangular torus
\[
T=\prod_{i=1}^d(\mathbb R/a_i\mathbb Z)
\]
with the quotient of the norm \(\|x\|_\infty=\max_i|x_i|\). Its translation-invariant shortest-path distance is
\[
\rho([x],[y])=\max_i\min_{k\in\mathbb Z}|x_i-y_i+k a_i|.
\]
Sample \(X,Y\) independently according to normalized Haar measure; set \(D=\rho(X,Y)\) and \(c_i=a_i/2\), with \(b=\max_i c_i\). The metric is the **max-Finsler** quotient metric, not the quotient of the Euclidean \(\ell_2\) norm. All expectations are exact population moments, and \(p,q\) are arbitrary real numbers satisfying \(p>q>0\).

The full cumulative distribution function of \(D\) is
\[
F(t)=\begin{cases}0,&t<0,\\\prod_{i=1}^d\min\{t/c_i,1\},&t\ge0.\end{cases}
\]
The support endpoint is \(b\). For \(0<t<b\) outside the finitely many numbers \(c_i\), its logarithmic slope equals
\[
\frac{tF'(t)}{F(t)}=\#\{i:c_i>t\}.
\]
The behavior for small positive \(t\) recovers \(d\), and the jumps, including multiplicities, recover the complete multiset of \(c_i\), hence of \(a_i\). The terminal multiplicity at \(b\) is read from the last jump to zero. Thus the law is a complete isometry invariant **within this family**.

## Proof
**1. Reduction to independent uniforms.** The coordinate difference of two independent Haar-uniform points on a circle of circumference \(a_i\), reduced modulo the period, is Haar-uniform. Taking the shorter circular arc distance maps it to a uniform random variable on \([0,a_i/2]\). Independence of the torus coordinates gives independent variables \(U_i\sim\operatorname{Uniform}[0,c_i]\) and the equality in law
\[
D\ \overset{\mathrm{law}}=\ \max_{1\le i\le d} U_i.
\]
The displayed CDF and its logarithmic slope follow by multiplication; the slope has one unit of downward jump for each coordinate threshold, with simultaneous jumps summing their multiplicities. This proves inverse rigidity, including repeated side lengths.

**2. Two scale-free quantile comparisons.** Write \(Q(u)=\inf\{t:F(t)\ge u\}\) for \(0<u<1\), so \(Q(u)>0\) and \(Q\) is strictly increasing. Every factor \(\min\{t/c_i,1\}\) has logarithmic derivative \(1/t\) below its saturation point and zero above. Thus, away from breakpoints,
\[
\frac{d\log F(t)}{d\log t}=m(t):=\#\{i:c_i>t\},\qquad 1\le m(t)\le d
\]
throughout \(0<t<b\). It follows that \(F(t)/t^d\) is nonincreasing and \(F(t)/t\) is nondecreasing. By inverse substitution, the two ratios
\[
\frac{Q(u)}{u^{1/d}}\quad\text{and}\quad\frac{Q(u)}{u}
\]
are respectively nondecreasing and nonincreasing in \(u\). The first is constant precisely when all \(c_i=b\). The second cannot be constant for \(d\ge2\), since the CDF has power \(d\) near zero.

**3. Monotone quantile-ratio lemma.** For any two positive continuous increasing bounded quantile functions \(A,B\) on \((0,1)\) with a monotone ratio \(h=B/A\), define \(Z_t=A h^t\) for \(0\le t\le1\). It is increasing for these applications because both \(A,B\) are increasing; more generally \(\log Z_t=(1-t)\log A+t\log B\). Set
\[
\mathcal R(Z_t)=\frac{\int_0^1 Z_t(u)^p\,du}{\left(\int_0^1 Z_t(u)^q\,du\right)^{p/q}}.
\]
Differentiation (first on \([\epsilon,1]\), then by dominated convergence) gives
\[
\frac d{dt}\log\mathcal R(Z_t)=p\left(\frac{\int Z_t^p\log h}{\int Z_t^p}-\frac{\int Z_t^q\log h}{\int Z_t^q}\right).
\]
The \(p\)-tilted distribution of \(u\) is stochastically larger than the \(q\)-tilted one: their density ratio is a positive constant times \(Z_t^{p-q}\), an increasing function. Therefore this derivative has the sign of the monotonicity of \(h\). Strict sign holds when \(h\) is nonconstant and \(Z_t\) strictly increasing. The bounded power-law behavior of all three relevant quantiles near zero justifies differentiation and dominated convergence for every \(p,q>0\), because \(|\log u|u^\gamma\) is integrable for \(\gamma>-1\).

Apply this lemma first with \(A(u)=u^{1/d}\) and \(B(u)=Q(u)\). Their ratio is nondecreasing, hence
\[
\mathcal R(u^{1/d})\le\mathcal R(Q).
\]
Apply it again with \(A(u)=Q(u)\) and \(B(u)=u\). Their ratio is nondecreasing, because \(Q(u)/u\) is nonincreasing, hence \(\mathcal R(Q)\le\mathcal R(u)\). In this second application the ratio is nonconstant for \(d\ge2\), so the inequality is strict. Since \(\int_0^1 u^{s/d}du=d/(d+s)\) and \(\int_0^1u^sdu=1/(1+s)\), the claimed explicit bounds follow. For the lower equality, strictness in the first comparison forces \(Q(u)\) to be a constant multiple of \(u^{1/d}\), so every threshold \(c_i\) equals \(b\), and conversely this case attains equality.

**4. Sharpness of the strict upper endpoint.** Normalize \(b=1\), choose \(c_d=1\), and let the other \(d-1\) lengths tend to zero. Then \(\max_i U_i\) converges almost surely to \(U_d\sim\operatorname{Uniform}[0,1]\), so each positive moment converges by dominated convergence. Hence the right endpoint is a true but unattained supremum. Setting \(p=2,q=1\) gives the stated coefficient-of-variation relation.

**5. Optional reproducible exact moment formula.** For integers \(s\ge1\) and ordered half-lengths \(0<c_1\le\cdots\le c_d=b\), put \(c_0=0\). Integrating \(\mathbb E D^s=b^s-s\int_0^b t^{s-1}F(t)dt\) separately on intervals yields
\[
\mathbb E D^s=b^s-\sum_{j=0}^{d-1}\frac{s\big(c_{j+1}^{s+d-j}-c_j^{s+d-j}\big)}{(s+d-j)\prod_{i=j+1}^d c_i}.
\]
The formula remains valid for repeated \(c_i\), where some integration intervals have zero length.

## Verification
The accompanying `verify.py` verifies 1,651 exact rational moment-ratio instances across dimensions \(2\) to \(7\), using independent choices of integer side ratios and five exponent pairs. It also checks 12 independent numerical quadratures of the CDF-based integral, simulates 180,000 independent point pairs on a three-dimensional torus using wrapped coordinate differences, and verifies both sharp endpoint patterns. Run `python3 verify.py` (Python standard library only); the expected output is `VERIFY_OK exact_moment_profiles=1651 independent_quadratures=12 simulation_draws=180000`. These finite checks are supplemental: the proof above covers every positive length vector and every real \(p>q>0\).

## Relationship to prior work
Kochar and Torrado (first publicly posted 10 June 2015) study reverse-hazard and likelihood-ratio comparisons of largest order statistics in general scale models, focusing on generalized gamma examples. Their manuscript, including its theorem sections, concerns comparisons between majorized parameter vectors and does not assert the present simultaneous sharp continuum of scale-free maximum-uniform moments, its unique all-equal extremizer, or its rectangular max-Finsler-torus reconstruction. The more general theory of star-shaped stochastic orders (Krieger, 1991) supplies relevant conceptual background for the quantile-ratio argument; the abstract was inspected, not its full manuscript. The elementary stochastic-order transfer lemma is proved here rather than claimed as a new general discovery.

The inverse-law component is specific to the max quotient metric. Earlier Euclidean flat-torus inversion and random-distance results are not equivalent because the Euclidean quotient distance is a sum-of-squares model, while this law is the maximum of independent uniforms. The present claim is a complete exact theorem for the stated geometric family, not a general rigidity theorem for arbitrary Finsler tori.

## Limitations
The theorem concerns rectangular (orthogonally split) product tori and the quotient max norm. It does not extend unproved claims to skew lattices, Euclidean \(\ell_2\) distances, arbitrary Finsler norms, noisy moments, or stochastic reconstruction from finite samples. The full distance distribution identifies side lengths, but finitely many moments are not asserted to do so. Historical priority, including possible equivalent uniform-order-statistic inequalities expressed via star ordering, remains subject to independent literature review. All displayed inequalities are proved analytically; numerical checks alone would not establish their universal quantifiers.

## References
1. S. C. Kochar and N. Torrado, *On stochastic comparisons of largest order statistics in the scale model*, arXiv:1506.03258 (first public post 10 June 2015), later *Communications in Statistics—Theory and Methods*. https://arxiv.org/abs/1506.03258
2. H. Krieger, *Stochastic orderings induced by star-shaped functions* (1991). https://doi.org/10.1155/S016117129100087X
3. M. Shaked and J. G. Shanthikumar, *Stochastic Orders*, Springer (2007), Chapters 3–4. The moment-order transfer used above is independently proved.
