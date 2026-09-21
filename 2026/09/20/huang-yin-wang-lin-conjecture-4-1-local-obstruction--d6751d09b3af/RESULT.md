# A local asymptotic obstruction to Huang–Yin–Wang–Lin Conjecture 4.1

## Result

For \(p>1\), define
\[
\arcsin_p y=\int_0^y(1-u^p)^{-1/p}\,du,\qquad
\operatorname{arsinh}_p y=\int_0^y(1+u^p)^{-1/p}\,du,
\]
let \(\sin_p\) and \(\sinh_p\) be their inverses near the origin, and put
\[
\cosh_p x=(1+\sinh_p^p x)^{1/p}.
\]
Huang, Yin, Wang and Lin (2018, Conjecture 4.1) asked whether, for every
\(p\in(1,2]\),
\[
F_p(x)=\frac{\log(x/\sin_p x)}{\log\cosh_p x}
\]
is strictly increasing on \(0<x\le \pi_p/2\).

Set
\[
p_0=\frac{1+\sqrt7}{3}=1.215250437021530\ldots .
\]

**Theorem.** Conjecture 4.1 is false for every
\[
1<p\le p_0.
\]
More precisely, for each such \(p\),
\[
F_p(x)<\frac1{p+1}
\]
for all sufficiently small \(x>0\), whereas
\[
\lim_{x\downarrow0}F_p(x)=\frac1{p+1}.
\]
Consequently \(F_p\) cannot be strictly increasing.

For \(1<p<p_0\), the obstruction already occurs in the first nonconstant
term:
\[
F_p(x)=\frac1{p+1}
+\frac{3p^2-2p-2}{2(p+1)^2(2p+1)}x^p
+O(x^{2p}).
\]
At the endpoint \(p=p_0\), that coefficient vanishes, but the next term is
strictly negative:
\[
F_{p_0}(x)=\frac1{p_0+1}
+\frac{80\sqrt7-212}{81}x^{2p_0}
+O(x^{3p_0}),
\]
and \(80\sqrt7-212<0\).

Thus a necessary condition for the conjectured monotonicity at a fixed
parameter is
\[
p>\frac{1+\sqrt7}{3}.
\]
No sufficiency claim is made for parameters above this threshold.

## Proof

Write \(t=x^p\). Binomial expansion of the defining integrals gives
\[
\arcsin_p y
=y+\frac{y^{p+1}}{p(p+1)}
+\frac{p+1}{2p^2(2p+1)}y^{2p+1}
+\frac{(p+1)(2p+1)}{6p^3(3p+1)}y^{3p+1}
+O(y^{4p+1}),
\]
and
\[
\operatorname{arsinh}_p y
=y-\frac{y^{p+1}}{p(p+1)}
+\frac{p+1}{2p^2(2p+1)}y^{2p+1}
-\frac{(p+1)(2p+1)}{6p^3(3p+1)}y^{3p+1}
+O(y^{4p+1}).
\]
Series reversion, followed by taking logarithms, yields
\[
\log\frac{x}{\sin_p x}
=
\frac{t}{p(p+1)}
+\frac{p^2-p-1}{2p(p+1)^2(2p+1)}t^2
+\frac{(p-1)(4p^3-3p^2-7p-2)}
{6p(p+1)^3(2p+1)(3p+1)}t^3
+O(t^4),
\]
while the identity
\[
\cosh_p x=(1+\sinh_p^p x)^{1/p}
\]
gives
\[
\log\cosh_p x
=
\frac{t}p
-\frac{p-1}{2p(p+1)}t^2
+\frac{(p-1)(4p^2-p-2)}
{6p(p+1)^2(2p+1)}t^3
+O(t^4).
\]
Dividing the two expansions gives
\[
\begin{aligned}
F_p(x)
={}&\frac1{p+1}
+\frac{3p^2-2p-2}{2(p+1)^2(2p+1)}x^p\\
&+\frac{(p-1)(11p^3-17p^2-24p-6)}
{12(p+1)^3(2p+1)(3p+1)}x^{2p}
+O(x^{3p}).
\end{aligned}
\]

The quadratic \(3p^2-2p-2\) has positive root
\[
p_0=\frac{1+\sqrt7}{3}.
\]
Hence the coefficient of \(x^p\) is negative for \(1<p<p_0\). At
\(p=p_0\), direct substitution into the \(x^{2p}\) coefficient gives
\[
-\frac{212}{81}+\frac{80\sqrt7}{81}<0,
\]
because \(80^2\cdot7=44800<44944=212^2\). This proves the stated local
inequality.

Finally, if \(F_p\) were strictly increasing on \((0,\pi_p/2]\), then for
any fixed \(x>0\) and every \(0<y<x\) one would have \(F_p(y)<F_p(x)\).
Letting \(y\downarrow0\) would imply
\[
\frac1{p+1}\le F_p(x),
\]
contradicting the small-\(x\) expansion. Therefore strict monotonicity
fails.

As a concrete rational-parameter witness,
\[
F_{6/5}(x)
=\frac5{11}-\frac5{2057}x^{6/5}+O(x^{12/5}),
\]
so \(p=6/5\) already disproves the universal conjecture.

## Relation to prior literature and originality

The source paper explicitly states Conjecture 4.1 for all \(p\in(1,2]\).
Searches were made using the exact logarithmic ratio, the conjecture
number and source title/DOI, the polynomial \(3p^2-2p-2\), the threshold
\((1+\sqrt7)/3\), and synonymous generalized-trigonometric terminology.
No source located in those searches stated the counterexample interval
\(1<p\le p_0\) or the asymptotic obstruction above. The originality claim
is therefore **to the best of our knowledge**, not an assertion of
exhaustive coverage.

Later papers located in the same literature continue to study generalized
Wilker, Cusa, Huygens, and power-mean inequalities. The broad 2020
one-parameter paper by Wang, Hong, Xu, Shen and Chu is a particularly
plausible prior-coverage candidate; its abstract and bibliographic
metadata were inspected, but its full theorem set was not used to support
a noncoverage claim. A 2025 weighted-power-mean paper was also found as
related current literature. A differently phrased result in this
surrounding literature remains the main originality risk.

## Limitations

- The theorem disproves the conjecture only for
  \(1<p\le(1+\sqrt7)/3\); it does not classify the global monotonicity
  behavior for larger \(p\).
- The threshold is exact for this local small-\(x\) obstruction, not
  claimed to be the exact global parameter threshold.
- The current-status search cannot exclude terminology-equivalent or
  weakly indexed prior work.


## Reproducibility

`artifacts/verify_series.py` symbolically reverts the defining series,
checks the two displayed coefficients of \(F_p\), verifies the
\(p=6/5\) witness, and verifies the endpoint coefficient at \(p_0\).

## References

1. L.-G. Huang, L. Yin, Y.-L. Wang, X.-L. Lin,
   “Some Wilker and Cusa type inequalities for generalized trigonometric
   and hyperbolic functions,” *Journal of Inequalities and Applications*
   **2018**, 52 (2018). DOI: 10.1186/s13660-018-1644-8.
2. M.-K. Wang, M.-Y. Hong, Y.-F. Xu, Z.-H. Shen, Y.-M. Chu,
   “Inequalities for generalized trigonometric and hyperbolic functions
   with one parameter,” *Journal of Mathematical Inequalities* **14**
   (2020), 1–21. DOI: 10.7153/jmi-2020-14-01.
3. G. Zhong, X. Ma, “Inequalities for the generalized trigonometric
   functions with respect to weighted power mean,” *Demonstratio
   Mathematica* **58** (2025), 20250103.
   DOI: 10.1515/dema-2025-0103.
