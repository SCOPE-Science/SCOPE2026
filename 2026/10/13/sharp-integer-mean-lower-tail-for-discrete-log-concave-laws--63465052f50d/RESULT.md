# Sharp integer-mean lower tail for discrete log-concave laws
## Finding
Among finitely supported integer-valued log-concave random variables with integer mean, the exact infimum is
\[
\inf \Pr\{X\le \mathbb E[X]\}=e^{-1}.
\]
Here the infimum ranges over all finitely supported integer-valued random variables whose probability mass function is log-concave with contiguous support and whose mean is an integer.

More explicitly, for every \(\varepsilon>0\) there is a finite log-affine law with integer mean satisfying
\[
 e^{-1}\le \Pr\{X\le \mathbb E[X]\}<e^{-1}+\varepsilon.
\]
Thus the constant in the integer-mean corollary of Alqasem, Aravinda, Marsiglietti and Melbourne is sharp even after imposing the integer-mean constraint; the unrestricted sharpness examples in that paper do not by themselves establish this restricted sharpness.

## Assumptions and scope
A probability mass function \(p\) on a finite integer interval is log-concave when
\[
p(j)^2\ge p(j-1)p(j+1)
\]
for every interior support point. A log-affine law, whose positive masses form a geometric progression, is a special log-concave law.

The published inequality used as the lower-bound half of the statement is: if a discrete log-concave random variable has integer mean, then
\[
\Pr\{X\le\mathbb E[X]\}\ge e^{-1}.
\]
The new content here is a finite-support integer-mean family approaching that constant. No claim is made about attainment of the infimum by a single law, about a best rate in support size, or about subclasses such as Bernoulli sums, Poisson laws, or ultra-log-concave laws.

## Proof
Fix an integer \(k\ge1\). For each integer \(n>2k\) and parameter \(0<r<1\), let \(Y_{n,r}\) be supported on \(\{0,1,\ldots,n\}\) with
\[
\Pr\{Y_{n,r}=j\}=\frac{r^j}{\sum_{i=0}^{n}r^i}.
\]
Write
\[
\mu_n(r)=\mathbb E[Y_{n,r}].
\]
If \(\theta=\log r\), this is a one-parameter exponential family, and differentiation gives
\[
\frac{d}{d\theta}\mu_n(e^\theta)=\operatorname{Var}(Y_{n,e^\theta})>0.
\]
Hence \(\mu_n(r)\) is continuous and strictly increasing on \((0,1)\).

Set
\[
r_k=\frac{k}{k+1}.
\]
The untruncated geometric law with masses proportional to \(r_k^j\) on the nonnegative integers has mean
\[
\frac{r_k}{1-r_k}=k.
\]
The law \(Y_{n,r_k}\) is this geometric law conditioned on being at most \(n\). Since \(n>2k\), the removed tail lies strictly above the unconditioned mean, so conditioning on \(\{Y\le n\}\) strictly lowers the mean. Therefore
\[
\mu_n(r_k)<k.
\]
On the other hand,
\[
\lim_{r\uparrow1}\mu_n(r)=\frac n2>k.
\]
By continuity and strict monotonicity there is a unique
\[
r_{k,n}\in(r_k,1)
\]
such that
\[
\mu_n(r_{k,n})=k.
\]

For fixed \(k\), one has \(r_{k,n}\to r_k\) as \(n\to\infty\). Indeed, fix any \(s\in(r_k,1)\). The truncated geometric mean satisfies
\[
\mu_n(s)\longrightarrow\frac{s}{1-s}>k.
\]
Thus for all sufficiently large \(n\), strict monotonicity gives \(r_k<r_{k,n}<s\). Since \(s>r_k\) was arbitrary, the convergence follows.

Now define
\[
X_{k,n}=n-Y_{n,r_{k,n}}.
\]
Its mass function is proportional to \(r_{k,n}^{\,n-x}\) on \(\{0,\ldots,n\}\), so it is log-affine and therefore log-concave. Its mean is
\[
\mathbb E[X_{k,n}]=n-k\in\mathbb Z.
\]
Moreover,
\[
\{X_{k,n}\le n-k\}=\{Y_{n,r_{k,n}}\ge k\},
\]
and the latter probability is exactly
\[
T_{k,n}=r_{k,n}^{\,k}\frac{1-r_{k,n}^{\,n-k+1}}{1-r_{k,n}^{\,n+1}}.
\]
For fixed \(k\), the convergence \(r_{k,n}\to r_k<1\) implies
\[
T_{k,n}\longrightarrow r_k^k
=\left(\frac{k}{k+1}\right)^k.
\]
Finally,
\[
\left(\frac{k}{k+1}\right)^k
=\left(1+\frac1k\right)^{-k}
\longrightarrow e^{-1}.
\]
Therefore, given \(\varepsilon>0\), first choose \(k\) so that the last display is less than \(e^{-1}+\varepsilon/2\), then choose \(n\) large enough that \(T_{k,n}\) differs from it by less than \(\varepsilon/2\). This produces a finite log-affine law with integer mean and
\[
\Pr\{X_{k,n}\le\mathbb E[X_{k,n}]\}<e^{-1}+\varepsilon.
\]
The published integer-mean inequality supplies the reverse bound \(e^{-1}\), proving the exact infimum.

## Verification
The proof uses only finite geometric-series identities, strict monotonicity of the mean in an exponential family, and two successive limits. The bundled `verify.py` numerically solves the mean constraint for representative \((k,n)\), verifies the resulting means and tail formula, and checks convergence toward \((k/(k+1))^k\). Those finite checks are supplemental; the all-parameter result is the analytic proof above.

A useful closed form for independent reproduction is
\[
\mu_n(r)=\frac{r\bigl(1-(n+1)r^n+nr^{n+1}\bigr)}{(1-r)(1-r^{n+1})},\qquad 0<r<1.
\]
It gives the same unique root \(r_{k,n}\) of \(\mu_n(r)=k\).

## Relationship to prior work
Alqasem, Aravinda, Marsiglietti and Melbourne prove for every discrete log-concave random variable \(X\) that
\[
\Pr\{X<\mathbb E[X]+1\}\ge e^{-1},
\]
and state that the constant is sharp in the unrestricted log-concave class. They then single out the integer-mean consequence
\[
\Pr\{X\le\mathbb E[X]\}\ge e^{-1}.
\]
For that integer-mean setting they note that a stronger \(1/2\) bound holds for several classical families and give an eight-point truncated geometric example showing that \(1/2\) fails for the full log-concave class. Their unrestricted sharpness construction does not impose an integer mean, and the inspected text does not state that \(e^{-1}\) remains sharp under the integer-mean restriction.

Marsiglietti and Melbourne develop the discrete localization framework behind the reduction to log-affine laws and analyze truncated geometric means and tail bounds. Their inspected full text includes monotonicity of the truncated-geometric mean, but it does not state the present sharp integer-mean infimum or the two-scale \((k,n)\) construction above.

Exact-phrase web searches and semantic database searches were also made for the integer-mean sharpness statement, the truncated-geometric formulation, and equivalent lower-tail language. No covering result was located. This negative search is not itself a novelty proof; the substantive comparison is to the full texts just described.

## Limitations
The result identifies an infimum by an approximating family. It does not prove that equality \(e^{-1}\) is attained by any finite or infinite discrete log-concave law with integer mean, and it does not optimize how large the support must be to come within a prescribed distance of \(e^{-1}\). It also does not improve the stronger \(1/2\) bounds available in narrower distributional subclasses.

The principal originality risk is terminological: the same short construction could have appeared in older work on medians or one-sided mass bounds for discrete log-concave sequences without using the Feige terminology. Targeted searches did not locate such a statement.

## References
1. Abdulmajeed Alqasem, Heshan Aravinda, Arnaud Marsiglietti, James Melbourne, *On a Conjecture of Feige for Discrete Log-Concave Distributions*, arXiv:2208.12702v1; SIAM Journal on Discrete Mathematics 38 (2024), 93--102; DOI:10.1137/22M1539514.
2. Arnaud Marsiglietti, James Melbourne, *Geometric and Functional Inequalities for Log-Concave Probability Sequences*, arXiv:2004.12005v4; Discrete & Computational Geometry 71 (2024), 556--586; DOI:10.1007/s00454-023-00528-7.
