# Sharp damping thresholds and a finite Schoenberg test for geodesic waves on \(\mathbb S^3\)

## Finding
Let \(\mathbb S^3=\{x\in\mathbb R^4:\|x\|=1\}\) with shorter great-circle angle \(\theta(x,y)=\arccos\langle x,y\rangle\in[0,\pi]\). For every \(a>0\) and real \(\omega\ge0\), set
\[
K_{a,\omega}(x,y)=e^{-a\theta(x,y)}\cos(\omega\theta(x,y)).
\]
There is an **exact finite test** for positive semidefiniteness on every finite point set. Put \(z=a-i\omega\) and for \(\varepsilon=\pm1\) define
\[
\beta_\varepsilon=z(1-\varepsilon e^{-\pi z}),\quad
P_\varepsilon(X)=A_\varepsilon X^2+B_\varepsilon X+C_\varepsilon,
\]
with
\[
A_\varepsilon=\operatorname{Re}\beta_\varepsilon,\quad
B_\varepsilon=2\operatorname{Re}(\beta_\varepsilon(\overline z^{\,2}-1)),\quad
C_\varepsilon=\operatorname{Re}(\beta_\varepsilon(\overline z^{\,2}+1)^2).
\]
For each sign set \(k_+=1\), \(k_-=2\), and make the following finite comparisons:

* When \(A_\varepsilon<0\), reject. When \(A_\varepsilon=0\), reject if \(B_\varepsilon<0\); otherwise require \(P_\varepsilon(k_\varepsilon^2)\ge0\).
* When \(A_\varepsilon>0\), put \(X_\varepsilon^*=-B_\varepsilon/(2A_\varepsilon)\). If \(X_\varepsilon^*\le k_\varepsilon^2\), require only \(P_\varepsilon(k_\varepsilon^2)\ge0\). Otherwise find the unique nonnegative integer \(j\) with \((k_\varepsilon+2j)^2\le X_\varepsilon^*<(k_\varepsilon+2j+2)^2\), and require \(P_\varepsilon((k_\varepsilon+2j)^2)\ge0\) and \(P_\varepsilon((k_\varepsilon+2j+2)^2)\ge0\).

The kernel is positive semidefinite **if and only if both sign tests pass**. At most four selected quadratic values, plus the leading/slope checks, decide infinitely many harmonic-sign constraints. Every admitted kernel, even at parameter boundaries, is **strictly positive definite** for distinct finite sites.

For the integer-frequency family \(\omega=m\in\mathbb Z_{\ge0}\), the complete classification simplifies to
\[
\boxed{K_{a,m}\text{ positive semidefinite on }\mathbb S^3\iff a^2+4\ge3m^2.}
\]
It is strictly positive definite whenever admitted. Thus \(m=0,1\) allow every \(a>0\), while \(m\ge2\) require \(a\ge\sqrt{3m^2-4}\). At threshold equality with \(m\ge2\), only the degree-zero coefficient vanishes. Below threshold, writing \(r=a^2+m^2\) and \(X_c=1-r+2\sqrt{r(m^2-1)}\), the negative Schoenberg coefficients occur **exactly** in the initial block \((n+1)^2<X_c\); a coefficient is zero at equality, and all higher coefficients are positive.

## Assumptions and scope
All formulas use the unit round three-sphere and its intrinsic geodesic distance, not Euclidean/chordal distance. Parameters are quantified by \(a>0\), \(\omega\ge0\), and all finite point configurations; the integer branch further assumes \(m\in\mathbb Z_{\ge0}\). The sign tests are mathematical exact-real comparisons; floats cannot certify boundary equality. No extension to \(a=0\) or to spheres of other dimensions is asserted.

## Proof
**Exact coefficients.** The normalized three-sphere Gegenbauer polynomial is \(C_n^1(\cos\theta)/(n+1)=\sin((n+1)\theta)/((n+1)\sin\theta)\). Hence the Schoenberg coefficient in the normalized expansion is
\[
b_n=\frac{2(n+1)}{\pi}\int_0^\pi e^{-a\theta}\cos(\omega\theta)\sin\theta\sin((n+1)\theta)\,d\theta.
\]
For \(z=a-i\omega\), elementary integration gives \(\int_0^\pi e^{-z\theta}\cos(j\theta)\,d\theta=z(1-(-1)^j e^{-\pi z})/(z^2+j^2)\). With \(\varepsilon=(-1)^n\), the sine product-to-sum identity yields
\[
b_n=\frac{4(n+1)^2}{\pi}\operatorname{Re}\frac{\beta_\varepsilon}{(z^2+n^2)(z^2+(n+2)^2)}.
\]
The denominator never vanishes because \(a>0\). Put \(X=(n+1)^2\); then \((z^2+n^2)(z^2+(n+2)^2)=Q_z(X)=X^2+2(z^2-1)X+(z^2+1)^2\). Multiplication by \(\overline{Q_z(X)}\) gives
\[
\operatorname{sgn}b_n=\operatorname{sgn}P_{(-1)^n}((n+1)^2).
\]
The coefficient tail is \(O(n^{-2})\), so there is absolute convergence and no summability exception to Schoenberg's theorem.

**Finite reduction.** The square sequences \((n+1)^2\) are \(1,9,25,\ldots\) for even \(n\) and \(4,16,36,\ldots\) for odd \(n\). A quadratic with negative leading coefficient fails on either unbounded sequence. If the leading coefficient vanishes, its linear term must be nonnegative and its first value nonnegative. A quadratic with positive leading coefficient has its minimum on the appropriate square sequence at the first square when the vertex lies to its left, or at one of the two squares bracketing the vertex. These observations prove exactly the stated tests and, using the Schoenberg coefficient criterion, their necessity and sufficiency.

**Strictness.** The number \(\beta_\varepsilon\ne0\) since \(z\ne0\) and \(|e^{-\pi z}|=e^{-\pi a}<1\). When \(\omega=0\), the quadratic leading coefficient is positive. If \(\omega>0\) and \(A_\varepsilon=0\), then \(\beta_\varepsilon\) is purely imaginary and nonzero; since \(\operatorname{Im}(\overline z^{\,2})=2a\omega\ne0\), necessarily \(B_\varepsilon\ne0\). Every passed test thus has an eventually strictly positive polynomial on each parity square sequence. Each parity has infinitely many positive Schoenberg coefficients, which gives strict positive definiteness on \(\mathbb S^3\), including all equalities.

**Integer-frequency threshold and obstruction.** For integer \(m\), \(e^{-\pi(a-im)}=(-1)^m e^{-\pi a}\); thus the factor \(1-\varepsilon(-1)^m e^{-\pi a}\) is strictly positive real. A direct algebraic expansion gives
\[
P_\varepsilon(X)=a(1-\varepsilon(-1)^m e^{-\pi a})\big[(X+r-1)^2+4r(1-m^2)\big],\quad r=a^2+m^2.
\]
For all \(X\ge1\), the bracket has derivative \(2(X+r-1)>0\). Its smallest value, attained at \(X=1\), is \(r(a^2+4-3m^2)\). This proves the sharp threshold, including equality. If it fails, then \(m\ge2\), and the unique root of the bracket above \(1\) is \(X_c\). Monotonicity establishes the claimed exact negative-initial-block description.

## Verification
The included `check.py` evaluates both the finite test and the exact Schoenberg coefficient formula. It passed 40 direct Simpson-quadrature comparisons, 500 deterministic parameter comparisons against coefficients through degree 899, and 20 integer-threshold-side checks. Separately, symbolic polynomial expansion established the integer branch identity. These finite checks are supplemental; the proof above handles unbounded degrees, endpoints, and quantifiers.

## Relationship to prior work
Gneiting's spherical characterization and its three-sphere coefficient-difference identity (arXiv:1111.7077) provide the harmonic framework, but not this evaluated two-parameter finite criterion or its integer-frequency phase boundary. Beatson–zu Castell–Xu (arXiv:1110.2437) gives a sufficient Pólya criterion for other kernel shapes. Huang–Zhang–Robeson (2011) checks unmodulated exponential and undamped sine-over-angle hole-effect models on \(\mathbb S^2\). Jeong–Jun (arXiv:1504.01985) discusses the positive product with \(\cos\theta\), which covers the special frequency \(m=1\), not the thresholds for \(m\ge2\). Euclidean radial and circular-geodesic kernels have different validity conditions and do not imply the present intrinsic three-sphere classification.

## Limitations
The derivation does not prove global novelty beyond inspected sources, and unindexed equivalent classifications may exist. No bound on numerical conditioning near equality, extension to other dimensions, or explicit smallest indefinite finite configuration is claimed. The spectral obstruction is exact; numerical tests do not establish infinite-dimensional completeness. Independent review and validation remain unperformed.

## References
1. T. Gneiting, *Strictly and non-strictly positive definite functions on spheres*, arXiv:1111.7077v1 (posted 2011-11-30); Bernoulli 19 (2013), 1327–1349. https://arxiv.org/abs/1111.7077
2. R. K. Beatson, W. zu Castell, Y. Xu, *A Pólya criterion for (strict) positive definiteness on the sphere*, arXiv:1110.2437v1 (posted 2011-10-11). https://arxiv.org/abs/1110.2437
3. C. Huang, H. Zhang, S. M. Robeson, *On the Validity of Commonly Used Covariance and Variogram Functions on the Sphere*, Mathematical Geosciences 43 (2011), 721–733. https://doi.org/10.1007/s11004-011-9344-7
4. J. Jeong, M. Jun, *Covariance models on the surface of a sphere: when does it matter?*, arXiv:1504.01985v1 (posted 2015-04-08). https://arxiv.org/abs/1504.01985
