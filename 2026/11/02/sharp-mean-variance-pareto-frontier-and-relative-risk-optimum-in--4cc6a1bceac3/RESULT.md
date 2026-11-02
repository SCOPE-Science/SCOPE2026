# Sharp mean–variance Pareto frontier and relative-risk optimum in sticky active escape

## Finding

For a one-dimensional run-and-tumble particle escaping a finite interval with one sticky wall and one absorbing wall, the mean escape time, its absolute variance, and its squared coefficient of variation have **three distinct optimal reversal rates**. The exact attainable mean–variance Pareto frontier consists of one closed parameter interval, whereas the minimum relative uncertainty occurs strictly outside that interval and is dominated in **both** absolute mean and absolute variance.

Let the dimensionless reversal parameter be \(b=\alpha R/v>0\) and dimensionless first-passage time be \(Z=vT/R\). The three objective functions are
\[
M(b)=\mathbb EZ=3+\frac32b+\frac1b,
\qquad V(b)=\operatorname{Var}(Z)=\frac52b^2+10b+12+\frac8b+\frac3{b^2},
\]
\[
Q(b)=\frac{V(b)}{M(b)^2}
=\frac{2(5b^4+20b^3+24b^2+16b+6)}{(3b^2+6b+2)^2}.
\]
There are exactly three unique minimizers, ordered as
\[
\boxed{b_M=\sqrt{2/3}< b_V<1<3<b_Q<4},
\]
where \(b_V\) is the unique positive root of \(5b^4+10b^3-8b-6=0\), and \(b_Q\) is the unique positive root of \(2b^3-3b^2-9b-5=0\). Numerically,
\[
b_M=0.8164965809\ldots,\quad b_V=0.9753318429\ldots,\quad
b_Q=3.1689668551\ldots.
\]
The **entire nondominated mean–variance set** is exactly \(\{(M(b),V(b)):b_M\le b\le b_V\}\). Every interior Pareto point uniquely minimizes \(M(b)+\lambda V(b)\) for a positive weight \(\lambda\). The minimizing \(b_\lambda\) increases strictly from \(b_M\) to \(b_V\) as \(\lambda\) runs from zero to infinity.

The sharp squared-coefficient-of-variation bound is
\[
\boxed{Q(b)\ge Q(b_Q)=1.099983697266\ldots>1},
\]
with equality exactly at \(b_Q\). In particular the relative-risk optimum at \(b_Q\) is strictly dominated in both \(M\) and \(V\) by the absolute-variance optimum \(b_V\). At the small- and large-tumbling ends, \(Q(b)\to3\) and \(Q(b)\to10/9\), respectively.

## Assumptions and scope

The particle moves on \([-R,R]\), with \(v,R>0\). In the interior its instantaneous velocity is either \(+v\) or \(-v\), switching sign independently at Poisson rate \(\alpha/2>0\). The right endpoint \(+R\) is absorbing upon arrival. At the left endpoint \(-R\), a left-moving particle becomes immobile until an independent exponential waiting time of rate \(\alpha/2\) ends; it then resumes motion rightward. Initially the particle is at the center \(0\), and each initial sign has probability \(1/2\). The first-passage time \(T\) includes all immobilization durations. No thermal diffusion, added detachment, wall leakage, spatial inhomogeneity, resetting or asymmetric initial orientation is assumed.

The parameter \(\alpha\) follows the common telegrapher convention: a direction change has rate \(\alpha/2\), not \(\alpha\). Physical first and second centered moments are \(\mathbb ET=(R/v)M(b)\) and \(\operatorname{Var}(T)=(R/v)^2V(b)\), respectively. Only \(b>0\) is admissible. All moments used below are finite for each such \(b\).

## Proof

Set \(y=x/R\) and \(Z=vT/R\). For \(n=0,1,2\), let \(f_{n,\pm}(y)\) denote the conditional \(n\)-th moment of \(Z\), with \(f_{0,\pm}\equiv1\). The backward generator in the moving states is
\[
(\mathcal L f)_+=f'_++\frac b2(f_--f_+),\qquad
(\mathcal L f)_-=-f'_-+\frac b2(f_+-f_-).
\]
The backward recurrence and the physically distinct boundary conditions are
\[
\mathcal L f_n=-n f_{n-1},\quad f_{n,+}(1)=0,
\]
\[
f_{1,-}(-1)-f_{1,+}(-1)=\frac2b,
\]
\[
f_{2,-}(-1)-f_{2,+}(-1)=\frac4b f_{1,+}(-1)+\frac8{b^2}.
\]
The wall equations follow by adding an independent \(\operatorname{Exp}(b/2)\) waiting time to the subsequent right-moving escape time. These equations are uniquely solvable since the process is transient with finite absorption moments at each \(b>0\).

For completeness, the first-moment polynomial solutions are
\[
f_{1,+}(y)=-\frac b2 y^2-(b+2)y+\frac{3b}{2}+2,
\]
\[
f_{1,-}(y)=-\frac b2 y^2-by+\frac{3b}{2}+4+\frac2b.
\]
The corresponding second-moment polynomials solving the displayed recurrence and wall equations are
\[
\begin{aligned}
f_{2,+}(y)={}&\frac{b^2}{12}y^4+
\left(\frac{b^2}3+\frac{2b}3\right)y^3+
\left(1-2b-\frac{3b^2}2\right)y^2\\
&-\left(\frac{11b^2}3+14b+14+\frac4b\right)y
+\frac{19b^2}4+\frac{46b}3+13+\frac4b,\\
f_{2,-}(y)={}&\frac{b^2}{12}y^4+\frac{b^2}3y^3-
\left(\frac{3b^2}2+4b+1\right)y^2\\
&-\left(\frac{11b^2}3+8b+2\right)y+
\frac{19b^2}4+\frac{68b}3+35+\frac{24}b+\frac8{b^2}.
\end{aligned}
\]
Direct differentiation and substitution check both interior equations and both endpoint conditions, for every \(b>0\). At \(y=0\), averaging over the two initial signs gives
\[
\mathbb EZ=\frac{3b^2+6b+2}{2b},\qquad
\mathbb EZ^2=\frac{19b^4+76b^3+96b^2+56b+16}{4b^2}.
\]
Subtracting the square of the first moment gives the displayed \(V(b)\) and \(Q(b)\). As an independent representation, the source's exact first-passage Laplace transform is
\[
\mathbb E e^{-sZ}=
\frac{(s+b)\{\cosh k+(s/k)\sinh k\}}
{(2s+b)\cosh(2k)+2k\sinh(2k)},
\qquad k^2=s(s+b),
\]
with the continuous \(k=0\) interpretation. Its Taylor coefficients at \(s=0\) reproduce the two moments. This transform, rather than the derived moment identities by themselves, belongs to prior work.

The mean has \(M'(b)=3/2-b^{-2}\) and \(M''(b)=2b^{-3}>0\), giving \(b_M\). The variance satisfies
\[
V'(b)=\frac{5b^4+10b^3-8b-6}{b^3},\qquad
V''(b)=5+\frac{16}{b^3}+\frac{18}{b^4}>0.
\]
Thus \(V\) has a unique global minimum at the positive quartic root \(b_V\). The quartic has one sign variation in its coefficient sequence, so Descartes' rule gives exactly one positive root; it changes sign between \(0\) and \(1\). Substituting \(b_M\) in the quartic gives a negative value, hence \(b_M<b_V<1\).

For relative uncertainty, differentiation and cancellation yield the exact factorization
\[
Q'(b)=\frac{16(2b^3-3b^2-9b-5)}{(3b^2+6b+2)^3}.
\]
The cubic has exactly one positive root by Descartes' rule and is negative at \(3\), positive at \(4\); therefore \(Q\) decreases strictly until \(b_Q\), then increases strictly. Further,
\[
Q(b)-1=\frac{b^4+4b^3+8b+8}{(3b^2+6b+2)^2}>0,
\]
which establishes the stated positive floor. The limits at zero and infinity follow from the leading terms.

Finally, on \([b_M,b_V]\), \(M\) strictly increases and \(V\) strictly decreases. Every point outside this interval is dominated by its nearest endpoint; no two distinct points inside dominate one another, giving the complete Pareto set. For every \(\lambda>0\), \(M+\lambda V\) is strictly convex, with derivative negative at \(b_M\) and positive at \(b_V\); it therefore has a unique optimizer \(b_\lambda\in(b_M,b_V)\). Implicit differentiation of its first-order condition gives
\[
\frac{d b_\lambda}{d\lambda}=
\frac{-V'(b_\lambda)}{M''(b_\lambda)+\lambda V''(b_\lambda)}>0.
\]
Every interior point has the unique supporting weight \(\lambda=-M'(b)/V'(b)>0\). Because \(b_Q>3>b_V\), both \(M(b_Q)>M(b_V)\) and \(V(b_Q)>V(b_V)\), proving the relative-versus-absolute-risk separation.

## Verification

The standalone `verify.py` uses only the Python standard library. From the explicit conditional polynomials, it checks exact rational polynomial coefficients of the two generator identities, the absorption and sticking boundary equations, and both centered moments at 16 positive rational parameter choices. Separately, a truncated power-series expansion of the published first-passage transform reproduces the moments exactly at those parameter choices. It isolates the two new algebraic optimizer roots using rational bisection, with intervals narrower than \(10^{-9}\). Running `python3 verify.py` produces `VERIFY_OK`.

The finite checks are reproducibility diagnostics. The universal result for every \(b>0\) is established by the displayed polynomial identities, derivative factorizations, convexity and root-count arguments, not by finite enumeration or numerical sampling.

## Relationship to prior work

Angelani's *Optimal escapes in active matter* (arXiv:2311.11873v1, first public 2023-11-20) introduces this exact sticky-left/absorbing-right center-initialized model, derives its mean first-passage time and mean-optimal reversal parameter, and provides the full first-passage Laplace transform. Thus the stochastic model, the mean optimizer, the full transform and every moment obtainable directly by differentiation **are established prior information** and are not asserted to be new. The present result concerns the previously unreported simultaneous **global optimizer classification** for mean, absolute variance, and relative variance, including the complete Pareto frontier and its strict separation from relative-risk optimality.

Angelani's 2023 *One-dimensional run-and-tumble motions with generic boundary conditions* presents the more general boundary construction and mean exit-time formula; Bressloff's 2023 *Encounter-based model of a run-and-tumble particle II* treats partially absorbing sticky boundaries and occupation times. Neither inspected text gives the risk-optimizer ordering or this Pareto characterization. These comparisons do not establish global publication priority against all related literature.

## Limitations

The result applies only to the specified one-dimensional center-started, initially unbiased, left-sticky/right-absorbing exponential-tumbling model. An independent starting orientation bias, competing wall absorption, nonexponential wall residence, thermal diffusivity or higher-dimensional motion changes the boundary problem and is not covered. It is a sharp exact classification within this model rather than a general active-matter risk-optimality principle. The full Laplace transform and hence the raw moments are already implied by published work; the claim of distinctiveness concerns the complete extremal and Pareto geometry. Implicit coverage in a broader previously published optimization result cannot be ruled out. No independent scientific audit has been performed.

## References

1. L. Angelani, *Optimal escapes in active matter*, arXiv:2311.11873v1 (first public 2023-11-20); *European Physical Journal E* **47**, 9 (2024), doi:10.1140/epje/s10189-023-00402-7. https://arxiv.org/abs/2311.11873
2. L. Angelani, *One-dimensional run-and-tumble motions with generic boundary conditions*, *Journal of Physics A* **56**, 455003 (2023), doi:10.1088/1751-8121/ad009e. https://doi.org/10.1088/1751-8121/ad009e
3. P. C. Bressloff, *Encounter-based model of a run-and-tumble particle II: absorption at sticky boundaries*, arXiv:2302.01158v1 (2023). https://arxiv.org/abs/2302.01158
4. L. Angelani, *Confined run-and-tumble swimmers in one dimension*, *Journal of Physics A* **50**, 325601 (2017). https://doi.org/10.1088/1751-8121/aa74e5
