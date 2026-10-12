# Closed-form Lambert-W bandwidth for the Stacy generalized gamma family
## Finding
For the Stacy generalized gamma density
\[
f(x)=\frac{p}{a^d\Gamma(d/p)}x^{d-1}\exp\!\left[-(x/a)^p\right],\qquad x>0,
\]
with \(a>0\), \(d>1\), and \(p>0\), define the full width at \(y\)-maximum for \(0<y<1\) as the distance between the two points where the density equals \(y\) times its maximum. The mode is
\[
m=a\left(\frac{d-1}{p}\right)^{1/p}.
\]
Set
\[
z_y=-e^{-1}y^{p/(d-1)}.
\]
Then the two level points are
\[
x_-(y)=m[-W_0(z_y)]^{1/p},\qquad
x_+(y)=m[-W_{-1}(z_y)]^{1/p},
\]
and hence
\[
\mathrm{FWyM}_y
=m\left([-W_{-1}(z_y)]^{1/p}-[-W_0(z_y)]^{1/p}\right).
\]
The full width at half maximum is the specialization \(y=1/2\). The corresponding generalized octave bandwidth is
\[
\mathrm{BW}_{\mathrm{oct}}(y)
=\frac{1}{p}\log_2\!\left(\frac{W_{-1}(z_y)}{W_0(z_y)}\right).
\]
Both Lambert-W values in the ratio are negative, so the ratio is positive.

## Assumptions and scope
The parameters satisfy \(a>0\), \(d>1\), and \(p>0\). The restriction \(d>1\) is exactly the regime in which the density has a finite positive interior mode and therefore two level points for every \(0<y<1\). The result uses the Stacy parameterization above; other generalized-gamma parameterizations can be converted before applying the formula.

No two-sided width statement is asserted here for \(d\le 1\). At \(d=1\), the maximum occurs at the boundary of the support, while for \(0<d<1\) the density diverges at the origin.

## Proof
Differentiate the log-density. For \(x>0\),
\[
\frac{d}{dx}\log f(x)=\frac{d-1}{x}-\frac{p x^{p-1}}{a^p}.
\]
Because \(d>1\), this vanishes once, at
\[
m=a\left(\frac{d-1}{p}\right)^{1/p},
\]
and the derivative changes from positive to negative there.

Put
\[
c=\frac{d-1}{p},\qquad r=\left(\frac{x}{m}\right)^p.
\]
Since \((m/a)^p=c\), direct cancellation of the normalizing constant gives
\[
\frac{f(x)}{f(m)}
=r^c\exp[-c(r-1)]
=\exp\!\left(c(\log r-r+1)\right).
\]
Therefore \(f(x)=y f(m)\) is equivalent to
\[
\log r-r+1=\frac{1}{c}\log y,
\]
or
\[
r e^{-r}=e^{-1}y^{1/c}=e^{-1}y^{p/(d-1)}.
\]
Writing \(z_y=-e^{-1}y^{p/(d-1)}\), this is
\[
-r=W_k(z_y).
\]
For \(0<y<1\), one has \(-1/e<z_y<0\). Hence exactly two real branches occur: \(W_0(z_y)\in(-1,0)\) and \(W_{-1}(z_y)<-1\). Consequently
\[
r_-=-W_0(z_y)\in(0,1),\qquad r_+=-W_{-1}(z_y)>1.
\]
Converting back from \(r=(x/m)^p\) gives the two displayed level points and their difference.

Finally,
\[
\frac{x_+(y)}{x_-(y)}
=\left(\frac{-W_{-1}(z_y)}{-W_0(z_y)}\right)^{1/p},
\]
so taking \(\log_2\) yields the octave-bandwidth formula.

When \(p=1\), the Stacy density is a gamma density with shape \(d\) and scale \(a\); the formulas reduce to
\[
x_\pm(y)=-(d-1)a\,W_{0,-1}\!\left(-e^{-1}y^{1/(d-1)}\right),
\]
which is exactly the gamma level-set formula in the motivating paper.

## Verification
The proof is algebraic and uses only the real-branch structure of Lambert W on \((-1/e,0)\). Substituting either displayed level point into the normalized density ratio gives exactly \(y\), and the branch inequalities place one point on each side of the mode.

The packaged script `verify_formula.py` evaluates several non-gamma parameter choices and checks both level equations to numerical precision. Those calculations are sanity checks only; the general result follows from the preceding identities.

## Relationship to prior work
LoPrete and Burge derive a Lambert-W expression for the full width at arbitrary height and the octave bandwidth of the ordinary gamma family. Their discussion explicitly names the generalized gamma distribution as future work and states that deriving its bandwidth outside the gamma special case might be impossible. The formula above resolves that stated question for the full positive-parameter Stacy family with an interior mode.

Stacy introduced the generalized gamma family by adding a positive power parameter to the exponential factor of the gamma density. The present result exploits exactly that powered-exponential structure: after the substitution \(r=(x/m)^p\), every density level set reduces to the same universal Lambert-W equation.

Focused searches for generalized-gamma, Stacy, Amoroso, powered-gamma, Lambert-W, full-width, and octave-bandwidth formulations found the ordinary-gamma result but no statement covering the formulas above. The principal residual originality risk is an older equivalent level-set formula under Amoroso or powered-exponential terminology.

## Limitations
The claim concerns density level widths, not quantiles, confidence intervals, hazard-function widths, or widths for shifted or reflected generalized-gamma families. It does not address numerical conditioning near \(y=1\), statistical estimation of the parameters, or boundary-mode conventions when \(d\le1\).

## References
1. A. LoPrete and J. Burge, “Bandwidth of Gamma-Distribution-Shaped Functions via Lambert W Function,” arXiv:2509.19307v1; *Statistics & Probability Letters* 235 (2026), 110707, DOI:10.1016/j.spl.2026.110707.
2. E. W. Stacy, “A Generalization of the Gamma Distribution,” *The Annals of Mathematical Statistics* 33(3) (1962), 1187–1192, DOI:10.1214/aoms/1177704481.
