# Curvature obstructions to two generalized one-parameter-mean conjectures

For \(\alpha>0\) and distinct positive \(x,y\), Cheung and Qi define the generalized one-parameter mean
\[
J_\alpha(r;x,y)=
\left[
\frac{r(x^{r+\alpha}-y^{r+\alpha})}
{(r+\alpha)(x^r-y^r)}
\right]^{1/\alpha},
\]
with the continuous definitions at \(r=0,-\alpha\). Their 2007 paper proves monotonicity and logarithmic convexity/concavity properties and then poses:

- **Open Problem 1:** \(J_\alpha(r)\) is strictly concave on \((-\alpha/2,\infty)\).
- **Open Problem 2:** \(J_\alpha(t)J_\alpha(-t)\) is strictly logarithmically convex outside \([-\alpha/2,\alpha/2]\), and strictly concave and strictly logarithmically concave inside.

The first statement is false for every admissible choice of \(\alpha,x,y\). The exterior logarithmic-convexity statement in the second problem is also false for every \(\alpha>0\): any prescribed finite exterior parameter can be made a point of strict logarithmic concavity by taking \(x\) and \(y\) sufficiently close.

## Theorem

Let \(\alpha>0\) and \(x\ne y>0\).

1. \(J_\alpha''(-\alpha/2;x,y)>0\). Consequently there exists \(\delta>0\) such that
   \[
   J_\alpha''(r;x,y)>0
   \qquad
   \left(-\frac{\alpha}{2}<r<-\frac{\alpha}{2}+\delta\right),
   \]
   so Open Problem 1 is false for every \(\alpha>0\) and every distinct pair \(x,y\).

2. Fix any \(r\in\mathbb R\), and put
   \[
   x=m e^{-u},\qquad y=m e^u,\qquad m>0,\ u>0.
   \]
   For
   \[
   P_{\alpha,u}(r)=J_\alpha(r;x,y)J_\alpha(-r;x,y)
   \]
   one has, as \(u\downarrow0\),
   \[
   \frac{d^2}{dr^2}\log P_{\alpha,u}(r)
   =
   -\frac{2\alpha}{15}u^4+O(u^6).
   \]
   Hence for every fixed \(r\) with \(|r|>\alpha/2\), this second derivative is negative for all sufficiently small \(u>0\). Thus the exterior logarithmic-convexity assertion in Open Problem 2 is false.

The second asymptotic is uniform when \(r\) ranges over a fixed compact set. Therefore, as \(y/x\to1\), any possible transition from logarithmic concavity to logarithmic convexity for the product must escape every fixed bounded exterior interval.

## Proof

Because \(J_\alpha\) is homogeneous of degree one in \(x,y\), write
\[
x=m e^{-u},\qquad y=m e^u
\]
with \(m=\sqrt{xy}>0\) and \(u=\tfrac12|\log(y/x)|>0\). Define
\[
\operatorname{sinhc} z=
\begin{cases}
\dfrac{\sinh z}{z},&z\ne0,\\[4pt]
1,&z=0,
\end{cases}
\qquad
\phi(z)=\log(\operatorname{sinhc}z).
\]
Then \(\phi\) is even and real analytic, and direct substitution in the definition gives
\[
J_\alpha(r;x,y)
=
m\left[
\frac{\operatorname{sinhc}(u(r+\alpha))}
{\operatorname{sinhc}(ur)}
\right]^{1/\alpha}.
\]
Thus, with \(L(r)=\log J_\alpha(r;x,y)\),
\[
L(r)=\log m+
\frac{\phi(u(r+\alpha))-\phi(ur)}{\alpha}.
\]

### Exact midpoint obstruction

Since \(\phi\) is even, \(\phi''\) is even and \(\phi'\) is odd. At \(r=-\alpha/2\),
\[
L''\!\left(-\frac{\alpha}{2}\right)=0,
\]
whereas
\[
L'\!\left(-\frac{\alpha}{2}\right)
=
\frac{2u}{\alpha}\phi'\!\left(\frac{\alpha u}{2}\right).
\]
For \(z>0\),
\[
\phi'(z)=\coth z-\frac1z>0,
\]
because \(z\cosh z-\sinh z\) vanishes at \(0\) and has derivative \(z\sinh z>0\). Therefore
\[
J_\alpha''\!\left(-\frac{\alpha}{2}\right)
=
J_\alpha\!\left(-\frac{\alpha}{2}\right)
\left[
L''\!\left(-\frac{\alpha}{2}\right)
+
\left(L'\!\left(-\frac{\alpha}{2}\right)\right)^2
\right]
>0.
\]
Continuity of \(J_\alpha''\) gives a right neighborhood of strict convexity inside \((-\alpha/2,\infty)\). This disproves Open Problem 1.

The mechanism is structural: the reflection identity
\[
J_\alpha(r;x,y)J_\alpha(-r-\alpha;x,y)=xy
\]
forces the logarithmic curvature to vanish at the reflection center \(r=-\alpha/2\), while the nonzero logarithmic slope makes the ordinary curvature strictly positive there.

### Near-diagonal obstruction for the product

Let
\[
K(r)=\log P_{\alpha,u}(r).
\]
Using the evenness of \(\phi\),
\[
K(r)=2\log m+
\frac{
\phi(u(r+\alpha))+
\phi(u(\alpha-r))-
2\phi(ur)}{\alpha}.
\]
Hence
\[
K''(r)=
\frac{u^2}{\alpha}
\left[
\phi''(u(r+\alpha))
+\phi''(u(\alpha-r))
-2\phi''(ur)
\right].
\]
The Taylor expansion
\[
\phi(z)
=
\frac{z^2}{6}
-\frac{z^4}{180}
+\frac{z^6}{2835}
+O(z^8)
\]
gives
\[
\phi''(z)
=
\frac13-\frac{z^2}{15}+\frac{2z^4}{189}+O(z^6).
\]
Substituting,
\[
\begin{aligned}
K''(r)
&=
\frac{u^2}{\alpha}
\left[
-\frac{u^2}{15}
\bigl((r+\alpha)^2+(\alpha-r)^2-2r^2\bigr)
+O(u^4)
\right]\\
&=
-\frac{2\alpha}{15}u^4+O(u^6).
\end{aligned}
\]
For fixed \(\alpha>0\) and fixed \(r\), the leading coefficient is strictly negative, proving the second assertion. Analyticity of \(\phi\) makes the remainder uniform for \(r\) in any fixed compact set.

## A sharper local picture for \(J_\alpha\)

The same expansion also yields
\[
J_\alpha''(r;x,y)
=
m\,\frac{5-6r-3\alpha}{45}u^4+O(u^6)
\qquad (u\downarrow0)
\]
for fixed \(\alpha,r\). Thus, near the diagonal \(x=y\), ordinary convexity persists throughout every compact subinterval of
\[
-\frac{\alpha}{2}<r<\frac56-\frac{\alpha}{2},
\]
while ordinary concavity holds at fixed parameters strictly to the right of \(5/6-\alpha/2\) when \(x/y\) is sufficiently close to \(1\). The number \(5/6-\alpha/2\) is therefore the leading near-diagonal curvature transition, not the logarithmic-curvature transition \(-\alpha/2\).

## Context and originality check

Cheung and Qi's final 2007 Taiwanese Journal of Mathematics article contains the \(1/\alpha\) power in the definition above, proves that \(J_\alpha\) is increasing and changes logarithmic curvature at \(-\alpha/2\), and states Open Problems 1 and 2 explicitly. A 2009 paper by Qi, Cerone, Dragomir and Srivastava gives alternative proofs for the monotonicity and logarithmic-convexity properties of the ordinary one-parameter mean and the monotonicity of its symmetric product; its stated scope does not resolve these ordinary-concavity questions.

A 2025 survey by Yang and Qi revisits one- and two-parameter homogeneous means and cites the 2007 paper. Its discussion of the one-parameter mean records the established monotonicity and logarithmic convexity/concavity results and the monotonicity of \(J_p(a,b)J_{-p}(a,b)\), but the accessible full text does not state a resolution of the two 2007 curvature questions treated here.

Searches using the source title and DOI, the exact open-problem language, "generalized one-parameter mean", ordinary concavity, logarithmic convexity of \(J_\alpha(r)J_\alpha(-r)\), the reflection center \(-\alpha/2\), and equivalent Stolarsky/one-parameter-mean terminology did not locate a published counterexample or the near-diagonal curvature formulas above. Originality is therefore claimed only **to the best of our knowledge**. Because the first obstruction is short and uses identities adjacent to the original conjecture, an unpublished observation or a poorly indexed remark remains a meaningful residual risk.

## Limitations

The result disproves Open Problem 1 and the exterior logarithmic-convexity clause of Open Problem 2; it does not classify the full sign diagram of \(J_\alpha''\) or of \((\log P_{\alpha,u})''\) for arbitrary \(x/y\). It does not contradict Cheung and Qi's proved logarithmic concavity of \(J_\alpha\) on \((-\alpha/2,\infty)\): a positive log-concave function need not be concave. The central concavity and logarithmic-concavity clauses of Open Problem 2 are not settled here. The leading near-diagonal transition \(5/6-\alpha/2\) is an asymptotic statement, not a claim of an exact global inflection point.

## Verification

`artifacts/verify_curvature_obstructions.py` symbolically checks the \(u^4\) coefficients in the two curvature expansions and evaluates representative numerical signs directly from the hyperbolic formulas.

## References

1. W.-S. Cheung and F. Qi, *Logarithmic Convexity of the One-Parameter Mean Values*, Taiwanese Journal of Mathematics **11** (2007), 231--237. DOI: https://doi.org/10.11650/twjm/1500404648
2. F. Qi, P. Cerone, S. S. Dragomir and H. M. Srivastava, *Alternative proofs for monotonic and logarithmically convex properties of one-parameter mean values*, Applied Mathematics and Computation **208** (2009), 129--133. DOI: https://doi.org/10.1016/j.amc.2008.11.023
3. Z.-H. Yang and F. Qi, *Bivariate homogeneous functions of two parameters: Monotonicity, convexity, comparisons, and functional inequalities*, Journal of Mathematical Analysis and Applications **544** (2025), 129091. DOI: https://doi.org/10.1016/j.jmaa.2024.129091
