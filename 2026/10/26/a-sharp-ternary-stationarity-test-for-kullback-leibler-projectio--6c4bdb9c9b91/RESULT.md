# A sharp ternary stationarity test for Kullback–Leibler projection geometry

## Finding

Fix the **single** three-outcome alphabet \(X=\{-1,0,1\}\) and the **single** statistic \(T(x)=x\). Let \(f\in C^2((0,\infty))\) be strictly convex, satisfy \(f(1)=0\), and have \(f''(1)>0\). For a positive probability vector \(\lambda\) on \(X\), define
\[
D_f(\mu\Vert q)=\sum_{x\in X}q_x f(\mu_x/q_x),\qquad
\mathcal E_f(\lambda)=\{q>0:\sum_xq_x=1,\ f'(q_x/\lambda_x)=a+bx\text{ for some }a,b\in\mathbb R\}.
\]
The family is a smooth one-dimensional curve near \(q=\lambda\). Consider the following **local stationarity test**:

(P) For **every** positive reference law \(\lambda\) on \(X\) and **every** positive target law \(\mu\) with \(\sum_x x\mu_x=\sum_x x\lambda_x\), the point \(q=\lambda\) is stationary for \(q\mapsto D_f(\mu\Vert q)\) along this local curve.

**Theorem.** Property (P) holds if and only if, for constants \(\alpha>0\) and \(\beta\in\mathbb R\),
\[
f(u)=\alpha u\log u+\beta(u-1)\qquad (u>0).
\]
Equivalently, \(D_f=\alpha\,D_{\mathrm{KL}}\). For these generators, \(\lambda\) is in fact a **global** information projection of every same-mean \(\mu\) onto \(\mathcal E_f(\lambda)\). Three distinct outcomes are minimal: on one or two outcomes, an injective first-moment statistic determines the target distribution uniquely, so this same local test imposes no restriction on \(f\).

Thus KL is characterized by a **fixed ternary first-moment experiment with variable reference masses**, using only **first-order stationarity**, without quantifying over arbitrary finite alphabets or higher moments.

## Assumptions and scope

All three reference and target probabilities are strictly positive. The generator is globally \(C^2\) and strictly convex on \((0,\infty)\), with the nondegeneracy \(f''(1)>0\); no hypothesis is made about \(f''(u)\) away from \(1\). In (P), the entire normalization-preserving local \(f\)-exponential curve through \(\lambda\) is tested, not a single selected tangent direction in the unrestricted probability simplex. A stationary point means the derivative with respect to any smooth local parameter of that curve vanishes. The result does not classify the exceptional \(f''(1)=0\) case under only this fixed ternary test.

## Proof

**1. The tangent to the generalized exponential family.** Write \(m=\sum_xx\lambda_x\) and \(c=f''(1)>0\). For \(b\) near zero, the inverse-function theorem at \(f'(1)\), followed by the implicit-function theorem for the normalization equation, provides a unique \(C^1\) function \(a(b)\) with \(a(0)=f'(1)\) such that
\[
f'(q_x(b)/\lambda_x)=a(b)+bx,\qquad\sum_xq_x(b)=1.
\]
Differentiating at \(b=0\) gives \(a'(0)=-m\) and
\[
q_x'(0)=\frac{\lambda_x(x-m)}{c}.
\]
This establishes both smoothness and the precise normalization-dependent tangent.

**2. Stationarity becomes a scalar functional identity.** Put \(h(u)=f(u)-u f'(u)\). It is \(C^1\) and \(h'(u)=-u f''(u)\). Direct differentiation of the divergence in its second argument gives
\[
\left.\frac{\mathrm d}{\mathrm db}D_f(\mu\Vert q(b))\right|_{b=0}
=\frac1c\sum_{x\in X}\lambda_x(x-m)h(\mu_x/\lambda_x).
\]
Consequently (P) implies that this sum is zero for **every** positive equal-mean pair \((\lambda,\mu)\).

**3. Vary the reference asymmetry.** Fix \(0<s<1/2\) and \(0<t<(1-2s)/2\). For sufficiently small positive or negative \(\varepsilon\), set, in the order \((-1,0,1)\),
\[
\lambda(\varepsilon)=\left(s+\frac\varepsilon2,\ 1-2s,\ s-\frac\varepsilon2\right),\qquad
\mu(\varepsilon)=\left(s+\frac\varepsilon2+t,\ 1-2s-2t,\ s-\frac\varepsilon2+t\right).
\]
Both are positive probability vectors with common mean \(-\varepsilon\). The identity from Step 2 is zero for each \(\varepsilon\); differentiate it at \(\varepsilon=0\). With
\[
x=1+\frac ts>1,\qquad y=1-\frac{2t}{1-2s}\in(0,1),
\]
the derivative simplifies **exactly** to
\[
0=(2s-1)[h(x)-h(y)]+\frac ts h'(x).
\]
Since \(x-y=t/[s(1-2s)]\), this is
\[
h(x)-h(y)=(x-y)h'(x).\tag{1}
\]

**4. The identity covers the full cross-region.** Conversely, for **every** \(x>1\) and \(0<y<1\), choose
\[
s=\frac{1-y}{2(x-y)},\qquad t=s(x-1).
\]
Then \(0<s<1/2\) and \(0<t<(1-2s)/2\), and the two ratios in Step 3 are precisely \(x\) and \(y\). Hence (1) holds for all \((x,y)\in(1,\infty)\times(0,1)\). Holding \(x\) fixed and differentiating (1) with respect to \(y\) gives \(h'(y)=h'(x)\). Thus \(h'\) takes the same value on both open intervals, and by continuity on all of \((0,\infty)\). Since \(h'(1)=-f''(1)=-c\),
\[
-u f''(u)=h'(u)=-c,\qquad f''(u)=\frac c u.
\]
Twice integrating and using \(f(1)=0\) yields \(f(u)=c u\log u+\beta(u-1)\), as claimed.

**5. Sufficiency and sharpness.** For the displayed generators, \(D_f=cD_{\mathrm{KL}}\), while the generalized exponential family is exactly
\[
q_x(b)=\frac{\lambda_x\exp(bx/c)}{\sum_z\lambda_z\exp(bz/c)}.
\]
Differentiation shows \(\frac{\mathrm d}{\mathrm db}D_f(\mu\Vert q(b))=\mathbb E_{q(b)}T-\mathbb E_{\mu}T\) and its derivative is \(\operatorname{Var}_{q(b)}(T)/c>0\). Equal means therefore make \(b=0\) the unique global minimizer. For a two-outcome alphabet with a nonconstant statistic, normalization and its mean determine the entire target law: equal mean forces \(\mu=\lambda\), so **every** convex divergence passes the stationarity test. A constant statistic only produces the trivial family. This proves minimality of three outcomes for the stated test.

## Verification

The included `verify.py` uses only Python standard-library exact rational arithmetic to check \(175\) same-mean KL stationarity identities, \(49\) realizations of arbitrary cross-region ratios, and a concrete non-KL failure. For \(f(u)=(u-1)^2/2\), let
\[
\lambda=(3/10,1/2,1/5),\qquad\mu=(29/80,3/8,21/80)
\]
in the order \((-1,0,1)\). Both means equal \(-1/10\), yet the exact first derivative at the moment-matched reference is \(-33/5120\neq0\). A finite-difference computation independently checks its sign and magnitude. These checks do not replace Steps 1–5 and cannot establish universal quantifiers.

## Relationship to prior work

Bec, Le Corre and Garivier (2026), Sections 2.3–4 and Theorem 10, show that for any free moment family, **universal** entropy-adaptedness across *all finite supports* forces the KL divergence. Their Remark 18 identifies a **five-point proof configuration** when a single statistic takes each value at most twice, while Figure 3 gives individual non-KL counterexamples on the ternary support. Neither statement asserts that *one fixed three-point support*, with only a *local stationarity* requirement for all reference masses, characterizes every nondegenerate smooth generator. The present theorem proves exactly that more economical diagnostic. It neither disputes nor reproves their unrestricted theorem for \(f''(1)=0\).

Jiao, Courtade, No, Venkat and Weissman (2014), Section III, characterize KL through Bregman-divergence, sufficiency, and intersection properties and establish notable binary/ternary distinctions. These hypotheses concern **full divergence identities/invariance**, whereas (P) constrains only an infinitesimal projection condition on one generalized exponential curve; the older hypotheses are not assumed here. Classical KL information projection identities (Csiszár, 1975) supply the converse background.

## Limitations

The result is restricted to strictly positive reference/target masses and the normalization \(f(1)=0\), \(f''(1)>0\). It does not show fixed-ternary rigidity for degenerate curvature at one, and it does not treat arbitrary vector moments or infinite supports. Existence of a local curve is enough for necessity; global existence for general \(f\) is not asserted. The literature search cannot exclude a mathematically equivalent ternary stationary-geodesic criterion under different terminology; independent scientific assessment has not been performed.

## References

1. J. Bec, T. Le Corre, A. Garivier, *On Minimum Divergence for Distribution Reconstruction*, arXiv:2610.21872v1 (first public 2026-10-15), https://arxiv.org/html/2610.21872v1.
2. J. Jiao, T. A. Courtade, A. No, K. Venkat, T. Weissman, *Information Measures: The Curious Case of the Binary Alphabet*, arXiv:1404.6810v2, https://arxiv.org/html/1404.6810v2.
3. I. Csiszár, *I-Divergence Geometry of Probability Distributions and Minimization Problems*, Annals of Probability 3 (1975), 146–158.
