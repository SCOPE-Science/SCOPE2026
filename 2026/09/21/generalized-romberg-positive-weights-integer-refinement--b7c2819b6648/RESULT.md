# Positive-weight generalized Romberg quadrature for every integer refinement factor

## Setting

Let \(a<b\), let \(s\ge 1\) and \(r\ge 2\) be integers, and let \(T_k\) be the composite trapezoidal rule on the uniform grid with
\[
N_k=s r^k,\qquad h_k=\frac{b-a}{s r^k},\qquad k=0,1,\ldots,d.
\]
Consider the depth-\(d\) Richardson extrapolation
\[
Q_d=\sum_{k=0}^d c_{d,k}T_k,
\]
where the coefficients are chosen to cancel the first \(d\) even powers in the Euler--Maclaurin expansion:
\[
\sum_{k=0}^d c_{d,k}=1,\qquad
\sum_{k=0}^d c_{d,k}r^{-2jk}=0\quad (j=1,\ldots,d).
\]
For \(r=2\) this is the usual Romberg construction, up to the choice of starting grid. The result below concerns every integer refinement factor \(r\ge2\).

## Theorem 1: all final sample weights are strictly positive

Write \(q=r^2\) and
\[
P_0=1,\qquad P_j=\prod_{t=1}^j(q^t-1).
\]
Then the extrapolation coefficients are
\[
\boxed{
 c_{d,k}=(-1)^{d-k}\frac{q^{k(k+1)/2}}{P_kP_{d-k}},
 \qquad k=0,\ldots,d.
}
\]
When \(Q_d\) is collected as a single quadrature rule on the finest grid
\[
x_i=a+iH,\qquad H=\frac{b-a}{s r^d},\qquad i=0,\ldots,sr^d,
\]
so that
\[
Q_d[f]=\sum_{i=0}^{sr^d}w_i f(x_i),
\]
every weight is strictly positive:
\[
\boxed{w_i>0\quad\text{for all }i.}
\]
This includes the endpoints.

### Proof

The displayed formula for \(c_{d,k}\) is the Lagrange coefficient for evaluating at zero the degree-\(d\) interpolant through the nodes \(q^{-k}\), equivalently the unique solution of the Richardson moment conditions above.

Consider an interior finest-grid node and let \(\ell\) be the first trapezoidal level on which that node appears. Its weight is
\[
 w_i=\frac{b-a}{s}\sum_{k=\ell}^d c_{d,k}r^{-k}.
\]
At an endpoint the same formula holds with an additional factor \(1/2\) and \(\ell=0\). Define
\[
A_k=|c_{d,k}|r^{-k}.
\]
Adjacent magnitudes satisfy
\[
\frac{A_{k+1}}{A_k}
=\frac1r\,\frac{q^{k+1}(q^{d-k}-1)}{q^{k+1}-1}
>\frac{q-1}{r}=r-\frac1r>1.
\]
Thus \(A_0<A_1<\cdots<A_d\). Since \(c_{d,k}\) alternates in sign and \(c_{d,d}>0\), every tail
\[
\sum_{k=\ell}^d c_{d,k}r^{-k}
=A_d-A_{d-1}+A_{d-2}-\cdots
\]
is positive: pair terms from the right as \((A_d-A_{d-1})+(A_{d-2}-A_{d-3})+\cdots\), with a positive unpaired term when needed. Hence every collected sample weight is positive. \(\square\)

The same argument applies to any consecutive entry of the extrapolation table: a nonzero starting level can be absorbed into the base subdivision count \(s\).

## Theorem 2: exact largest weight

The largest final-grid sample weight occurs at any node that first appears on the finest trapezoidal grid. It is
\[
\boxed{
\max_i w_i
=H\prod_{j=1}^d\left(1-r^{-2j}\right)^{-1}.
}
\]
Indeed, a newly introduced finest-level node has weight \(Hc_{d,d}\), and
\[
c_{d,d}=\frac{q^{d(d+1)/2}}{P_d}
=\prod_{j=1}^d(1-r^{-2j})^{-1}.
\]
Every earlier node has a positive alternating tail strictly smaller than its final positive term \(Hc_{d,d}\), and endpoint weights have the additional factor \(1/2\).

Consequently the normalized largest-weight factor is uniformly bounded in depth by
\[
C_r=\prod_{j=1}^{\infty}(1-r^{-2j})^{-1}<\infty.
\]
For comparison, \(C_2\approx1.45235364245\), reproducing the classical Romberg upper weight scale, while \(C_3\approx1.14082275726\).

## Corollary: sharp sample-noise stability

Because constants are integrated exactly,
\[
\sum_i w_i=b-a.
\]
Together with strict positivity this gives
\[
\boxed{\sum_i|w_i|=b-a.}
\]
Therefore, if the sampled values are perturbed independently with \(|\delta_i|\le\varepsilon\), then
\[
\boxed{
\left|\sum_i w_i\delta_i\right|\le (b-a)\varepsilon.
}
\]
The bound is sharp, for example for equal-sign perturbations.

Moreover, no quadrature rule that is exact for constants can have a smaller operator norm from sample \(\ell_\infty\) error to integration error, because
\[
\sum_i|w_i|\ge\left|\sum_iw_i\right|=b-a.
\]
Thus these generalized integer-ratio Romberg rules achieve the minimum possible worst-case amplification of bounded absolute sample errors. Equivalently, after normalizing by \(b-a\), their sample-noise condition number is exactly one.

This statement concerns the already collected quadrature weights. It does not claim that the usual recursive extrapolation tableau is free of floating-point cancellation.

## Polynomial exactness

The Euler--Maclaurin expansion of the composite trapezoidal rule contains only even powers \(h^{2j}\). The Richardson conditions cancel the terms \(h^2,\ldots,h^{2d}\). Hence
\[
\boxed{Q_d[p]=\int_a^b p(x)\,dx\quad\text{for every polynomial }\deg p\le2d+1.}
\]

## Relation to known work and originality boundary

Positivity for classical dyadic Romberg quadrature is old and is not claimed here. Welsch's 1966 Algorithm 281 describes the usual power-of-two Romberg rule with positive equally spaced weights and the classical approximately \(0.484h\) to \(1.4524h\) weight range. Bauer--Rutishauser--Stiefel and later treatments also analyze positivity of the classical Romberg coefficients. Camargo gives a modern proof and further separation results for classical Romberg quadrature.

The broader extrapolation literature allows arbitrary division sequences. Farzi (2014), following Davis and Rabinowitz, explicitly contrasts three standard choices: the dyadic Romberg sequence, the alternating Bauer sequence \(1,2,3,6,9,18,\ldots\), and the Bulirsch sequence. The checked text states positivity for dyadic Romberg prefixes and for selected Bauer prefixes, while Bulirsch has no positive subsequence of the stated type. It does not state positivity for every pure geometric integer sequence \(s,sr,sr^2,\ldots\) with \(r\ge3\).

Sidi's generalized Richardson theory treats geometric extrapolation points and includes generalized Romberg applications, but the accessible theorem/abstract material checked did not state the final-sample positivity result above. General positivity criteria for quadrature formulas also go back at least to Sottas and Wanner.

Accordingly, the claimed new content is limited to the all-integer-refinement extension \(r\ge3\), its short alternating-tail certificate, the exact largest-weight product for this family, and the resulting sharp sample-noise norm. The general Richardson/Romberg framework and the \(r=2\) positivity theorem are prior work. Older generalized-extrapolation books and papers remain a material historical-equivalence risk.

## Limitations

- The construction uses nested uniform composite trapezoidal grids with an integer refinement factor \(r\ge2\). It is not a positivity theorem for arbitrary division sequences, nonnested grids, or rational extrapolation.
- The polynomial exactness statement assumes the usual exact-arithmetic quadrature model. Smooth-function error constants and finite-precision tableau stability are separate questions.
- The sharp robustness statement is for bounded absolute errors in the final sampled function values. It is not a model of relative error, stochastic noise, correlated error, or intermediate rounding in the extrapolation recursion.
- Larger \(r\) uses many more samples at a fixed extrapolation depth. No efficiency superiority over dyadic Romberg, Gaussian quadrature, Clenshaw--Curtis, or other high-order methods is claimed.
- The older extrapolation literature is broad. The literature search found no equivalent pure-integer-geometric positivity theorem for \(r\ge3\), but historical equivalence cannot be excluded.

## Reproducibility

`artifacts/verify.py` performs exact rational checks for \(r=2,3,4,5\), three starting subdivision counts, and depths 1 through 5. It verifies positivity, unit weight sum on \([0,1]\), exactness through degree \(2d+1\), and monotonic growth of the alternating tail magnitudes. `artifacts/verification.txt` records the deterministic output.

## References

1. J. H. Welsch, *Algorithm 281: Abscissas and weights for Romberg quadrature*, Communications of the ACM 9(4) (1966), 271--272. https://dblp.org/rec/journals/cacm/Welsch66a
2. F. L. Bauer, H. Rutishauser and E. Stiefel, *New aspects in numerical quadrature*, Proc. Sympos. Appl. Math. 15 (1963), 199--218.
3. A. Camargo, *A Chebyshev-Markov-Stieltjes separation type theorem for classical Romberg quadrature*, Numerical Algorithms 91 (2022). https://doi.org/10.1007/s11075-022-01393-w
4. J. Farzi, *Generalized extrapolation methods for solving nonlinear Fredholm integral equations*, Mathematical Communications 19(2) (2014), 375--390. https://www.mathos.unios.hr/mc/index.php/mc/article/view/619
5. A. Sidi, *A Complete Convergence and Stability Theory for a Generalized Richardson Extrapolation Process*, SIAM Journal on Numerical Analysis 34(5) (1997). https://doi.org/10.1137/S0036142994278589
6. G. Sottas and G. Wanner, *The number of positive weights of a quadrature formula*, BIT 22 (1982), 339--352. https://doi.org/10.1007/BF01934447
7. NIST Digital Library of Mathematical Functions, §3.5(iii), *Romberg Integration*. https://dlmf.nist.gov/3.5.iii
