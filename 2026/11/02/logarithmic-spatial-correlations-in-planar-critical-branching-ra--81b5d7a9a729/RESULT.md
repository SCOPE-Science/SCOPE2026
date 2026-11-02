# Logarithmic spatial correlations in planar critical branching random walks

## Finding

A critical branching random walk on the square lattice exhibits an exact spatial correlation hierarchy. Let \(Z_n(x)\) be the number of generation-\(n\) particles at site \(x\), starting from one particle at the origin. For distinct sites \(x_n,y_n\) satisfying
\[
\frac{x_n}{\sqrt n}\longrightarrow u\in\mathbb R^2,
\qquad \frac{\log\|x_n-y_n\|}{\log n}\longrightarrow\theta\in[0,1/2),
\]
the unconditional occupation-count correlation satisfies
\[
\boxed{\operatorname{Corr}(Z_n(x_n),Z_n(y_n))\longrightarrow 1-2\theta.}
\]
If instead \(\|x_n\|+\|y_n\|=O(\sqrt n)\) and \(\log\|x_n-y_n\|/\log n\to 1/2\), the correlation tends to zero.

More precisely, with
\[
g_t(v)=\frac5{4\pi t}\exp\!\left(-\frac{5\|v\|^2}{4t}\right),\qquad
A=\frac{5\sigma^2}{8\pi},
\]
the normalized covariance in the first regime has the limit
\[
\frac n{\log n}\operatorname{Cov}(Z_n(x_n),Z_n(y_n))
\longrightarrow A g_1(u)(1-2\theta),
\]
while each marginal variance multiplied by \(n/\log n\) converges to \(Ag_1(u)\).

At distinct diffusive locations \(x_n/\sqrt n\to u\) and \(y_n/\sqrt n\to v\ne u\), the smaller, finite macroscopic covariance profile is
\[
\boxed{n\operatorname{Cov}(Z_n(x_n),Z_n(y_n))\longrightarrow
\sigma^2\mathcal K(u,v),}
\]
where
\[
\mathcal K(u,v)=\int_0^1g_{2(1-t)}(u-v)
 g_{(1+t)/2}\left(\frac{u+v}{2}\right)\,dt.
\]
This positive, finite integral has the consistent logarithmic singularity
\[
\mathcal K(u,u+h)\sim\frac5{8\pi}g_1(u)\log\frac1{\|h\|^2}
\qquad(h\to0,\ h\ne0).
\]

## Assumptions and scope

At generation zero there is exactly one particle at the origin of \(\mathbb Z^2\). Each particle independently has \(K\) children, with \(\mathbb E K=1\), \(0<\sigma^2=\operatorname{Var}(K)<\infty\); each child independently moves by an increment uniformly sampled from the origin and the four coordinate neighbors. Reproduction and motion are mutually independent over all particles and times. The process is not conditioned on survival. Covariances and variances refer to generation-\(n\) site counts, not cumulative space-time occupation or indicators of occupation. For the mesoscopic statement, distinct sites, convergence of the first spatial coordinate after diffusive normalization, and the specified logarithmic separation exponent are required; for the macroscopic profile, the two limiting positions must be distinct.

Write \(p_j(w)\) for the \(j\)-step transition probability of the underlying lazy random walk and set \(p_0(w)=\mathbf1_{\{w=0\}}\). The mean occupation satisfies \(\mathbb E Z_n(w)=p_n(w)\). The Gaussian kernel \(g_t\) has covariance matrix \((2t/5)I_2\) and appears in the lattice local central limit theorem.

## Proof

**1. Exact genealogy identity.** Let \(F_n(x,y)\) be the expected number of ordered *distinct* generation-\(n\) particles at \(x,y\). Conditioning on the first generation separates pairs descended from the same child and pairs from different children. The former reproduce \(\sum_w p_1(w)F_{n-1}(x-w,y-w)\); since \(\mathbb E[K(K-1)]=\sigma^2\), the latter contribute \(\sigma^2p_n(x)p_n(y)\). From \(F_0=0\), iteration gives the finite identity
\[
\boxed{F_n(x,y)=\sigma^2\sum_{s=1}^n\sum_{z\in\mathbb Z^2}
 p_{n-s}(z)p_s(x-z)p_s(y-z).}\tag{1}
\]
For \(x\ne y\), \(\operatorname{Cov}(Z_n(x),Z_n(y))=F_n(x,y)-p_n(x)p_n(y)\); on the diagonal,
\[
\operatorname{Var}(Z_n(x))=F_n(x,x)+p_n(x)-p_n(x)^2.\tag{2}
\]
These formulas are valid for every critical offspring distribution of finite variance. No higher moment is used.

**2. Heat-kernel reductions and uniform bounds.** Symmetry and convolution give exactly
\[
\sum_zp_s(x-z)p_s(y-z)=p_{2s}(x-y).\tag{3}
\]
For the specified lazy walk, the lattice local central limit theorem and standard finite-range Gaussian upper bounds imply, uniformly on compact diffusive scales,
\[
p_j(w)=j^{-1}g_1(w/\sqrt j)+o(j^{-1}),\qquad
p_{2s}(r)=\frac5{8\pi s}\exp\left(-\frac{5\|r\|^2}{8s}\right)+o(s^{-1})
\]
when \(s\to\infty\) and \(r/\sqrt s\) remains bounded. They also give \(p_j(w)\le C/j\) and \(p_j(w)\le Cj^{-1}e^{-c\|w\|^2/j}\) for \(j\ge1\), with positive constants \(c,C\). Consequently the part of (1) with \(s\le n/2\) is at most
\[
\frac Cn\sum_{s\le n/2}s^{-1}e^{-c\|x-y\|^2/s},\tag{4}
\]
and the part with \(s>n/2\) is \(O(n^{-1})\), since \(p_s(x-z)\le C/n\) and \(\sum_zp_{n-s}(z)p_s(y-z)=p_n(y)\le C/n\).

**3. Mesoscopic leading constant.** Let \(r_n=\|x_n-y_n\|\) and fix \(\delta>0\) with \(2\theta+2\delta<1\). For integer \(s\) in \([n^{2\theta+\delta},n^{1-\delta}]\), the mass of \(p_s(x_n-z)p_s(y_n-z)\) lies at sites \(z\) within \(o(\sqrt n)\) of \(x_n\); uniformly on its contributing region,
\[
p_{n-s}(z)=\frac{g_1(u)+o(1)}n.
\]
The relative displacement \(r_n/\sqrt s\to0\) uniformly except potentially at a vanishing boundary slice, and (3) yields
\[
\sum_zp_{n-s}(z)p_s(x_n-z)p_s(y_n-z)
=\frac{g_1(u)+o(1)}n\frac5{8\pi s}.
\]
In particular, summing the main range gives
\[
\frac{5g_1(u)}{8\pi n}\big(1-2\theta-2\delta+o(1)\big)\log n.
\]
Bound (4) shows that \(s<n^{2\theta+\delta}\) adds at most \(O(\delta\log n/n)+o(\log n/n)\), and \(s>n^{1-\delta}\) adds at most \(O(\delta\log n/n)+O(n^{-1})\). Sending \(n\to\infty\) and then \(\delta\downarrow0\) gives the stated covariance constant. The same argument with \(x=y\) proves the diagonal limit (take a main range starting at \(n^\delta\)). Since \(p_n(x)p_n(y)=O(n^{-2})\) and \(p_n(x)=O(n^{-1})\), (2) yields the variance limits; division gives the correlation limit.

At \(\theta=1/2\), bound (4) is \(o(\log n/n)\), since \(\log(1+n/r_n^2)=o(\log n)\); the remaining terms contribute \(O(n^{-1})\). The positive marginal variances remain asymptotic to \(Ag_1(x_n/\sqrt n)\log n/n\) and \(Ag_1(y_n/\sqrt n)\log n/n\) in a compact diffusive region, so the correlation vanishes.

**4. Two distinct diffusive positions.** Put \(s/n\to1-t\) and \(z/\sqrt n\to w\). Multiplying (1) by \(n\), the two-dimensional local central limit theorem turns its interior sum into
\[
\sigma^2\int_0^1\int_{\mathbb R^2}
 g_t(w)g_{1-t}(u-w)g_{1-t}(v-w)\,dw\,dt.\tag{5}
\]
Because \(u\ne v\), the factor \(g_{2(1-t)}(u-v)\) makes the upper-time singularity integrable; the lower endpoint is bounded by convolution with \(g_t\). Uniform Gaussian bounds dominate the tails and justify the limiting sum. The Gaussian-product identity
\[
g_s(u-w)g_s(v-w)=g_{2s}(u-v)
 g_{s/2}\left(w-\frac{u+v}2\right)
\]
and Gaussian convolution reduce (5) to the displayed \(\mathcal K\). The subtracted mean product becomes \(o(n^{-1})\).

Finally, as \(v=u+h\to u\), the only divergent part is near \(t=1\). There,
\[
g_{2(1-t)}(h)=\frac5{8\pi(1-t)}
 \exp\left(-\frac{5\|h\|^2}{8(1-t)}\right),
\]
while the second heat factor tends to \(g_1(u)\). Integrating on the scales \(\|h\|^2\ll1-t\ll1\) establishes the logarithmic singularity and its stated coefficient.

## Verification

The included `verify_spatial.py` independently evaluates (1) from a first-generation recursion and from the finite genealogical sum with exact rational arithmetic, for generations one through six and seven selected lattice sites (294 cases). It separately verifies the convolution identity (3) in 294 exact cases and the Gaussian-product identity in 81 floating-point cases: **669 assertions passed**. To reproduce, run `python3 verify_spatial.py` with the standard Python library. This is an exact finite-identity check plus a numerical kernel check, not a substitute for the asymptotic arguments. All limiting statements are supported by the analytical estimates above.

## Relationship to prior work

Bai, Chen and Lin (arXiv:2609.15538; first public date 2026-09-14) prove local survival and one-site Yaglom laws for the same lazy critical branching random walk, but do not give the two-site occupation-count correlation exponent or the finite noncoincident diffusive covariance kernel. Lalley and Zheng (arXiv:0707.3829; first public date 2007-07-25), especially Proposition 25 in Section 5.4, give an exact **one-site** second-moment identity and investigate clustering near a typical occupied site. Their formula is the diagonal predecessor of (1), and their qualitative clustering must not be confused with the present unconditional two-site correlation profile. The off-diagonal genealogy recursion is elementary and is not itself asserted to be a new general method; the claim here is the explicit matched spatial asymptotics. General higher-moment recursions, including Lalley (2009), and prior superprocess covariance identities constitute possible routes to alternative derivations.

## Limitations

The result concerns unconditional particle counts and cannot be read as a statement about survival-conditioned correlations or occupation-indicator correlations. The mesoscopic exponent requires the fixed lazy step law and diffusive-bounded sites; no uniform convergence rate is claimed. The macroscopic integral requires two distinct limiting points; its diagonal is divergent and is handled separately by the logarithmic normalization. The offspring law needs a finite positive variance but not higher moments. The finite checker does not establish infinite-generation assertions. Literature coverage remains subject to historical priority: older many-to-two formulas or Gaussian occupation-field results might implicitly imply portions of this profile after further analysis. No independent external audit has been performed.

## References

1. Tianyi Bai, Xinxin Chen and Shen Lin, *Critical branching random walks on \(\mathbb Z^2\): local survival probabilities and Yaglom limit theorems*, arXiv:2609.15538 (first public 2026-09-14), https://arxiv.org/abs/2609.15538.
2. Steven P. Lalley and Xinghua Zheng, *Occupation Statistics of Critical Branching Random Walks in Two or Higher Dimensions*, arXiv:0707.3829, https://arxiv.org/html/0707.3829v3; Annals of Probability 39 (2011), 327–368.
3. Steven P. Lalley, *Spatial Epidemics: Critical Behavior in One Dimension*, 2009, https://arxiv.org/abs/math/0701698 (general moment recursion cited by Lalley–Zheng, not required for the proof).
4. Gregory F. Lawler and Vlada Limic, *Random Walk: A Modern Introduction*, 2010, for lattice local central limit and heat-kernel estimates.
