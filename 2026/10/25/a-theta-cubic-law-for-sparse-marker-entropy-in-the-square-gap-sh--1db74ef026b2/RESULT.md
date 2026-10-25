# A theta-cubic law for sparse-marker entropy in the square-gap shift

## Finding

Let \(X_{\square}\subset\{0,1\}^{\mathbb Z}\) be the shift in which the number of zeros between consecutive ones belongs to \(\{1,4,9,16,\ldots\}\). For \(0<t<1/2\), set
\[
\mathcal E(t)=\sup\{h_\mu(\sigma):\mu\text{ is shift-invariant on }X_{\square},\ \mu([1])=t\},
\]
using natural logarithms. Put \(k=(2\pi)^{-1/2}\). For every sufficiently small \(t>0\), let \(w(t)\in(0,1/3)\) be the unique small positive solution of
\[
2\pi w(t)^2(1-w(t))=\frac{t}{1-t}.
\]
Then, for some absolute \(t_0,C>0\) and all \(0<t<t_0\),
\[
\boxed{\quad\frac{\mathcal E(t)}t=\log\frac{1-w(t)}{2w(t)}+\frac1{2(1-w(t))}+O(e^{-\pi^2/t}).\quad}
\]
In particular,
\[
\boxed{\quad\frac{\mathcal E(t)}t=\frac12\log\frac1t+\frac12\log\frac\pi2+\frac12
-\frac{\sqrt t}{\sqrt{2\pi}}-\left(\frac12+\frac{3}{8\pi}\right)t+O(t^{3/2}).\quad}
\]
All algebraic-order coefficients are obtained from the displayed cubic: after removing the logarithmic term, the cubic expression is an analytic function of \(\sqrt t\) near zero. The genuine entropy differs from this convergent germ by at most an exponentially small error. For every \(0<t<1/2\), the supremum defining \(\mathcal E(t)\) is attained by exactly one stationary measure, the renewal measure described below.

## Assumptions and scope

The shift is the closure of all bi-infinite concatenations of \(10^{n^2}\) with \(n\ge1\); the all-zero point and one-sided infinite-zero tails are present in this closure. A marker is a symbol \(1\); \(\mu([1])\) is its frequency. Adjacent markers are impossible. A return length is \(R_n=n^2+1\), not \(n^2\). The entropy \(h_\mu\) is measured in natural units per spatial coordinate. The asymptotics are for \(t\downarrow0\), not for the topological entropy of an unconstrained measure.

## Proof

**1. The exact density-constrained variational problem.** For \(s>0\), let
\[
Z(s)=\sum_{n=1}^\infty e^{-s(n^2+1)},\qquad m(s)=-\frac{d}{ds}\log Z(s),\qquad t(s)=m(s)^{-1}.
\]
The variance formula \(m'(s)=-\operatorname{Var}_s(R)<0\) is strict, because at least two return lengths occur. Moreover, \(m(s)\to\infty\) as \(s\downarrow0\), and \(m(s)\to2\) as \(s\to\infty\). Thus \(s\mapsto t(s)\) bijects \((0,\infty)\) onto \((0,1/2)\). Write \(s(t)\) for its inverse.

For any stationary measure \(\mu\) of marker density \(t>0\), condition on a marker at the origin and induce on \([1]\). The successive return lengths form a stationary process on \(\{n^2+1:n\ge1\}\). Its one-coordinate distribution \(p\) satisfies \(\sum p_nR_n\le1/t\); equality holds if \(\mu\) puts no mass on the all-zero fixed point. Indeed, Kac's tower covers total mass \(1-\mu(\{0^{\mathbb Z}\})\). Abramov's formula gives \(h_\mu=t h_{\mathrm{induced}}\). The entropy rate of the induced process does not exceed \(H(p)\), with equality only when its return lengths are independent. For every \(s>0\), relative entropy against \(q_s(n)=e^{-sR_n}/Z(s)\) gives
\[
H(p)\le\log Z(s)+s\sum p_nR_n\le\log Z(s)+s/t.
\]
Consequently \(h_\mu\le t\log Z(s)+s\), with strict inequality for an all-zero atom. At \(s=s(t)\), the stationary iid renewal process with return law \(q_{s(t)}\) attains equality. Equality in the relative-entropy and conditional-entropy inequalities forces this process uniquely. Therefore
\[
\mathcal E(t)=s(t)+t\log Z(s(t)).\tag{1}
\]
This uses no assumption that the square-gap shift has a global Bowen-Gibbs state.

**2. Theta transformation and the algebraic branch.** Put \(u=\sqrt{s}\), \(c=\pi^{-1/2}\), and \(A(u)=\sum_{n\ge1}e^{-u^2n^2}\). Poisson summation for the Gaussian gives the exact identity
\[
A(u)=\frac{\sqrt\pi}{2u}\left(1-cu+2\sum_{j\ge1}e^{-\pi^2j^2/u^2}\right).\tag{2}
\]
The theta tail and any fixed number of its derivatives are bounded by a power of \(u^{-1}\) times \(e^{-\pi^2/u^2}\) as \(u\downarrow0\). Deleting that tail gives \(A_0(u)=(1-cu)/(2cu)\), positive for sufficiently small \(u\), and \(Z_0(s)=e^{-s}A_0(\sqrt{s})\). Direct differentiation yields the exact elementary surrogate mean
\[
-\frac{d}{ds}\log Z_0(s)=1+\frac{1}{2u^2(1-cu)}.\tag{3}
\]
If \(w=cu\), the equation that this surrogate mean equals \(1/t\) becomes
\[
2\pi w^2(1-w)=\frac{t}{1-t}.\tag{4}
\]
Its small positive branch satisfies \(w/\sqrt t\to(2\pi)^{-1/2}\). The implicit function theorem after writing \(w=\sqrt t\,v\) shows that \(v\) is real analytic in \(\sqrt t\) near zero. The corresponding surrogate entropy, obtained by substituting (3) into \(s/t+\log Z_0(s)\), simplifies without approximation to
\[
\frac{\mathcal E_0(t)}t=\log\frac{1-w}{2w}+\frac1{2(1-w)}.\tag{5}
\]

**3. Uniform error control.** Both the true minimizer of \(s+t\log Z(s)\) and the local surrogate minimizer of \(s+t\log Z_0(s)\) satisfy \(s/t\to1/2\) as \(t\downarrow0\), by (2), its derivative and (3). For small enough \(t\), both lie in \([t/3,t]\). On this interval, (2) implies uniformly
\[
|\log Z(s)-\log Z_0(s)|=O(e^{-\pi^2/t}),
\]
with a constant independent of \(s\) and \(t\). Compare the two variational expressions at each other's minimizing arguments; their minima divided by \(t\) differ by at most the displayed uniform logarithmic error. This proves the exponentially accurate formula. (The local surrogate infimum is taken on \([t/3,t]\), where the stationary point is its strict minimum for small \(t\).)

**4. Explicit coefficients.** With \(x=\sqrt t\) and \(k=(2\pi)^{-1/2}\), solving (4) coefficientwise gives
\[
w=kx+\frac{k^2}{2}x^2+\frac{k(5k^2+4)}8x^3+(k^4+k^2/2)x^4+O(x^5).
\]
Substituting in (5) gives
\[
\frac{\mathcal E_0(t)}t=\frac12\log\frac1t+\frac12\log\frac\pi2+\frac12-k\sqrt t
-\left(\frac12+\frac{3k^2}{4}\right)t+O(t^{3/2}).
\]
The exponentially small error is smaller than every power of \(t\), completing the stated expansion. Equations (4)--(5) also provide every higher coefficient by convergent implicit-function expansion.

## Verification

The accompanying `verify.py` checks the cubic and entropy coefficients symbolically through order \(t\) using SymPy. It independently evaluates the original return-length partition series with high-precision Mpmath, checks the Jacobi identity numerically, and compares the exact entropy against the cubic surrogate at several positive densities. Its finite truncation is controlled by the explicitly stated exponentially decaying summand; these computations supplement rather than replace the uniform analytic proof. Run `python verify.py` in an environment with `sympy` and `mpmath` installed.

## Relationship to prior work

Climenhaga and Thompson (arXiv:1011.2780, Section 3.2) prove general intrinsic ergodicity and describe the coding of \(S\)-gap shifts. Dastjerdi and Jangjoo (arXiv:1108.3242) analyze topological and language properties of \(S\)-gap shifts. Baker and Ghenciu (arXiv:1411.7167, Sections 2--4) give a general topological-entropy description. Climenhaga's 2014 explanation of inducing on marker returns explicitly supplies the classical renewal variational framework. These general constructions and uniqueness results are prior work, not novel claims here. The present specific claim is the square-gap, **density-constrained** theta-cubic approximation with its convergent half-power coefficients and exponentially small remainder. A related published calculation for geometrically separated allowable return lengths has a logarithmically periodic, rather than Gaussian/half-power, sparse-density profile; it does not imply equations (4)--(5) for perfect-square zero gaps.

## Limitations

The error estimate is asymptotic; it does not provide a uniform bound for moderate densities without separately bounding theta tails. The maximizing measure is unique for positive density strictly below \(1/2\), not at the zero-density endpoint, where the only invariant measure is the all-zero atom. An equivalent unpublished or unindexed square-gap calculation cannot be excluded. There is no independent mathematical validation of the displayed theorem.

## References

1. V. Climenhaga and D. J. Thompson, *Intrinsic ergodicity beyond specification: beta-shifts, S-gap shifts, and their factors*, arXiv:1011.2780 (first posted 2010-11-11), Section 3.2, https://arxiv.org/abs/1011.2780.
2. D. Ahmadi Dastjerdi and S. Jangjoo, *Dynamics and Topology of S-gap Shifts*, arXiv:1108.3242 (first posted 2011-08-16), https://arxiv.org/abs/1108.3242. Only its definitions and language properties are used as context.
3. S. Baker and A. E. Ghenciu, *Dynamical properties of S-gap shifts and other shift spaces*, arXiv:1411.7167 (first posted 2014-11-26), Sections 2--4, https://arxiv.org/abs/1411.7167.
4. V. Climenhaga, *Entropy of S-gap shifts*, 2014-09-08, https://vaughnclimenhaga.wordpress.com/2014/09/08/entropy-of-s-gap-shifts/ (especially Section 4, induced-return variational formula).
5. The classical Jacobi theta transformation (Poisson summation for the Gaussian), used in identity (2).
