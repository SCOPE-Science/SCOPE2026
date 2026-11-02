# Sharp measure-type and mixing transition for Bernoulli-noise proximal gradient

## Finding

A scalar proximal stochastic-gradient recursion for a strongly convex sparse objective has a sharp change in stationary measure type at half the inverse curvature. At smaller steps the stationary law is **purely atomic and dense in a full interval, with geometric convergence in total variation**; at the threshold it is the **uniform non-atomic law**; at larger admissible steps it is a **non-atomic Cantor law**. In the last two regimes total variation from a deterministic initialization stays maximal at every finite iteration.

Precisely, take \(a>0\), \(0<\lambda<\sigma\), and \(0<h<1/a\), and let independent \(\varepsilon_n\) be equally likely to be \(+1\) or \(-1\). On
\[
F(x)=\frac a2x^2+\lambda|x|,
\]
use the unbiased stochastic gradient \(ax+\sigma\varepsilon_n\) of the smooth part and the exact proximal map of the nonsmooth part:
\[
X_{n+1}=S_{h\lambda}((1-ah)X_n-h\sigma\varepsilon_{n+1}),\qquad
S_t(u)=\operatorname{sgn}(u)\max\{|u|-t,0\}.
\]
Put \(q=1-ah\), \(b=h\sigma\), \(t=h\lambda\), \(c=b-t\), and \(B=c/(1-q)=(\sigma-\lambda)/a\). The chain has one invariant probability measure \(\mu_h\), supported inside \(I=[-B,B]\).

**(i) Small steps:** If \(0<h<1/(2a)\), then \(\mu_h\) is purely atomic, is supported densely on all of \(I\), and assigns positive mass to zero. There are integers \(m\ge1\) and \(p=2^{-m}>0\) such that, for all \(x\in I\),
\[
P^m(x,\{0\})\ge p,\qquad
\|P^n(x,\cdot)-\mu_h\|_{\mathrm{TV}}
\le (1-p)^{\lfloor n/m\rfloor}.
\]
Here total variation is \(\sup_E|\nu(E)-\eta(E)|\), with maximum value one.

**(ii) Critical step:** If \(h=1/(2a)\), then \(\mu_h\) is exactly uniform on \([-B,B]\).

**(iii) Large steps:** If \(1/(2a)<h<1/a\), then \(\mu_h\) is the non-atomic, singular, symmetric two-branch self-similar measure with strong separation, a Cantor support, and Hausdorff dimension
\[
\dim_{\mathrm H}(\operatorname{supp}\mu_h)
=\frac{\log2}{-\log(1-ah)}.
\]
The stationary support misses the open central interval \((-g,g)\), where \(g=B(2ah-1)>0\).

In regimes (ii)–(iii), every deterministic start has a finite-support distribution at each finite time and thus remains at total variation distance exactly one from \(\mu_h\), despite convergence in distribution. In regime (i), the invariant law has full topological support but consists entirely of atoms.

## Assumptions and scope

The noise is independent, symmetric, two-point, and persistently nonzero. Each sample smooth objective \(a x^2/2+\sigma\varepsilon x\) is convex, and its gradient is unbiased for \(a x\). The deterministic composite objective has unique minimizer \(x_*=0\). The scalar step range is strictly \(0<h<1/a\), and the strict inequality \(0<\lambda<\sigma\) makes the soft threshold nontrivial without annihilating both innovations at zero. The transition concerns the stationary measure and its total-variation convergence, not a change in deterministic convex optimization stability.

Write \(f_\pm(x)=S_t(qx\pm b)\). Every map is \(q\)-Lipschitz on \(\mathbb R\) with \(0<q<1\). They map \(I\) into itself and satisfy \(f_+ (B)=B\), \(f_-(-B)=-B\). The i.i.d. two-map contractive recursion has a unique invariant law by the elementary coupling bound \(|X_n^x-X_n^y|\le q^n|x-y|\), together with the usual infinite backward-composition construction. Its support is the unique compact nonempty set \(K=f_-(K)\cup f_+(K)\).

## Proof

### 1. The exact image geometry

The endpoints satisfy
\[
f_+(I)=[\ell,B],\qquad f_-(I)=[-B,-\ell],\qquad
\ell=S_t(b-qB).
\]
Since \(qB>0\) and \(b+qB>t\), all endpoint expressions are valid. The endpoint satisfies \(\ell>0\) exactly for \(q<1/2\), while \(\ell=0\) at \(q=1/2\); for \(q>1/2\) it may be negative or zero (if \(b-qB\) belongs to the soft-threshold plateau). Consequently \(\ell\le0\) exactly when \(q\ge1/2\). Hence for \(q\ge1/2\), \(f_-(I)\cup f_+(I)=I\). By uniqueness of the invariant compact set, \(K=I\).

If \(q<1/2\), then \(b-qB>t\). Both maps are affine on the whole of \(I\):
\[
f_\pm(x)=qx\pm c.
\]
The images are disjoint, separated by the gap \((-g,g)\), where \(g=c(1-2q)/(1-q)=B(1-2q)\). Their compact attractor is the classical strongly separated Bernoulli Cantor set. At depth \(n\), its \(2^n\) cylinders have diameter \(2Bq^n\), with each cylinder probability \(2^{-n}\). These imply non-atomicity and the standard Hausdorff-dimension formula \(\log2/(-\log q)\): the upper bound follows by cylinder covers; the lower bound follows from the separated-cylinder mass distribution estimate (or the standard self-similar measure theorem).

At \(q=1/2\) the two maps remain affine on all of \(I\) and map its two halves onto \(I\): \(f_\pm(x)=x/2\pm B/2\). The uniform law on \(I\) is invariant by interval scaling, hence is the unique invariant measure.

### 2. A uniform reset word for \(q>1/2\)

Let \(J=\{x\in I:|qx+b|<t\}\), the relatively open interval whose points are sent to zero by \(f_+\). Because \(b-qB<t\) strictly if \(q>1/2\) (as \(qB>c=b-t\)), while \(b+qB>t\), the preimage of the threshold \(t\) lies strictly inside \(I\). Moving slightly left gives a nonempty open interval \(J\) within \(I\); in particular choose \(y\in J\) and \(\delta>0\) with \((y-\delta,y+\delta)\subseteq J\).

Since \(I=K=\bigcup_{w\in\{-,+\}^n}f_w(I)\) for every \(n\), select a fixed integer \(n\ge0\) with \(2Bq^n<\delta\). For any \(x\in I\), some length-\(n\) word \(w\) has \(y\in f_w(I)\). The image has diameter at most \(2Bq^n\), so \(f_w(x)\in J\) and \(f_+(f_w(x))=0\). Every particular length-\(n+1\) sequence of independent fair signs has probability \(2^{-(n+1)}\). Consequently the Markov kernel satisfies the uniform Doeblin minorization
\[
P^{n+1}(x,\cdot)\ \ge\ 2^{-(n+1)}\delta_0(\cdot)
\quad\text{for all }x\in I.
\]
Standard splitting of the common point mass yields total-variation contraction by \(1-2^{-(n+1)}\) every \(n+1\) transitions, hence the asserted geometric bound.

### 3. Pure point measure with full support

The Doeblin bound and stationarity imply \(\mu_h(\{0\})\ge p>0\). Let
\[
A=\bigcup_{n\ge0}\{f_w(0):w\in\{-,+\}^n\}.
\]
This set is countable. Each \(P^n(0,\cdot)\) gives mass one to \(A\), and its convergence to \(\mu_h\) in total variation implies \(\mu_h(A)=1\). For every point \(z=f_w(0)\), stationarity gives \(\mu_h(\{z\})\ge 2^{-|w|}\mu_h(\{0\})>0\).

Finally, any nonempty relatively open subset \(U\subset I\) contains a point \(y\) and a small ball. Taking cylinders \(f_w(I)\) of sufficiently large depth, some cylinder contains \(y\) and has diameter smaller than that ball. Then \(f_w(0)\in U\). Thus \(A\) is dense and \(\operatorname{supp}\mu_h=I\). The origin is not absorbing: \(f_\pm(0)=\pm c\ne0\).

### 4. Total variation and a small-step check

At \(q\le1/2\), the invariant measure is non-atomic. From any deterministic \(x\), the distribution after a finite number of updates is supported on at most \(2^n\) points, and therefore is mutually singular with \(\mu_h\); its total-variation distance is exactly one.

For all stated steps the nonexpansiveness of soft threshold and the independence of the current innovation imply in stationarity
\[
\mathbb E_{\mu_h}[X^2]\le q^2\mathbb E_{\mu_h}[X^2]+b^2,
\qquad
\mathbb E_{\mu_h}[X^2]\le\frac{h\sigma^2}{a(2-ah)}.
\]
Therefore \(\mu_h\) converges weakly to \(\delta_0\) as \(h\downarrow0\), while every fixed \(0<h<1/(2a)\) has stationary support equal to the entire step-independent interval \(I\). This is another distinction between weak concentration and exact support.

## Verification

Run \(`python3 verify.py`\) using the Python standard library. It checks the interval-image regime algebra over 18 exact rational parameter triples, exhibits an exact five-sign reset word for a concrete small-step case, and propagates an exact rational law for ten steps. It prints:

`VERIFY_OK interval-regimes=18, exact-reset-word=----+, reset_probability>=1/32, exact-distribution-steps=10, mass_zero= 83/512 states= 205`

For the rational example \(q=2/3\), \(t=1\), \(b=2\) (equivalently \(a=1\), \(h=1/3\), \(\lambda=3\), \(\sigma=6\)), the word consisting of four minus maps followed by a plus map sends every \(x\in[-3,3]\) exactly to zero. Therefore one can take \(m=5\) and \(p=1/32\), giving \(\|P^k(x,\cdot)-\mu_h\|_{\rm TV}\le(31/32)^{\lfloor k/5\rfloor}\). The value \(83/512\) is a **ten-step transient probability** of zero from zero, not a claim about its stationary mass.

All infinite-support, measure-type and convergence conclusions are established analytically above; the exact finite verifier is a consistency check, not an exhaustive infinite proof.

## Relationship to prior work

Dai, Wang, Curtis and Robinson (2023) study support identification for variance-reduced, stabilized proximal stochastic-gradient algorithms. Their results use a changing estimator and accuracy assumptions; they do not determine the stationary measure of fixed-step, persistent two-point-noise proximal gradient. Bianchi, Hachem and Salim (2017) analyze invariant distributions for general constant-step random forward–backward schemes, but the present exact atomic/uniform/Cantor transition is not an immediate specialization of the asymptotic invariant-measure existence and small-step statements inspected there. Sun, Jeong, Nutini and Schmidt (2019) distinguish manifold-identification guarantees from methods whose stochastic gradient noise persists. They do not provide the law classification derived here.

The separated Cantor attractor and dimension formula in the large-step regime follow classical self-similar-measure theory (Hutchinson, 1981) and are *not claimed as newly discovered techniques*. The principal mathematical content is the explicit step-size trichotomy for a natural noisy proximal-gradient recurrence, in particular the pure-point **full-support** stationary law with an exact Doeblin reset and total-variation mixing on the small-step side. Novelty is assessed relative to the inspected sources, not asserted as a proof of universal priority.

## Limitations

The theorem is one-dimensional, uses unbiased independent fair two-point additive gradient noise, exact real arithmetic, and a fixed step strictly below the reciprocal curvature. It does not extend automatically to state-dependent gradient noise, higher-dimensional lasso problems, adaptive steps, floating-point implementations, or noise laws with a continuous component. The equality between invariant support and \(I\) does **not** imply a continuous density in the small-step regime. The proof establishes unique invariant law, not publication priority; an equivalent special-case result may exist elsewhere in random-iterated-function, proximal Markov-chain, or Bernoulli-convolution literature.

## References

1. Y. Dai, J. Wang, F. E. Curtis and D. P. Robinson, *A Variance-Reduced and Stabilized Proximal Stochastic Gradient Method with Support Identification Guarantees for Structured Optimization*, arXiv:2302.06790v1, publicly posted 2023-02-14. https://arxiv.org/abs/2302.06790
2. P. Bianchi, W. Hachem and A. Salim, *A constant step Forward-Backward algorithm involving random maximal monotone operators*, arXiv:1702.04144v1, 2017. https://arxiv.org/abs/1702.04144
3. D. Sun, H. Jeong, J. Nutini and M. Schmidt, *Are we there yet? Manifold identification of gradient-related proximal methods*, AISTATS 2019, PMLR 89. https://proceedings.mlr.press/v89/sun19a.html
4. J. E. Hutchinson, *Fractals and Self-Similarity*, Indiana Univ. Math. J. **30** (1981), 713–747. https://doi.org/10.1512/iumj.1981.30.30055
