# Sharp range-free empirical Cantelli bounds for exchangeable prediction

## Result

Let \(n\ge 2\), and let
\[
X_1,\ldots,X_n,X_{n+1}
\]
be any exchangeable real-valued random variables. No independence, population
moments, or bounded support are assumed. From the first \(n\) observations define
\[
\bar X_n=\frac1n\sum_{j=1}^n X_j,\qquad
S_n^2=\frac1{n-1}\sum_{j=1}^n (X_j-\bar X_n)^2.
\]
Define the externally studentized prediction residual
\[
T_n=\frac{X_{n+1}-\bar X_n}{S_n},
\]
with the natural extended convention when \(S_n=0\): \(T_n=+\infty\) if the
numerator is positive, \(T_n=-\infty\) if it is negative, and \(T_n=0\) if it
is also zero.

For \(t\ge0\), set
\[
R_n(t):=\frac{n^2-1+n t^2}{n-1+n t^2}.
\]

Then the exact worst-case strict upper tail is
\[
\boxed{\;
\sup_{\rm exch}\Pr(T_n>t)
=
\frac{\lceil R_n(t)\rceil-1}{n+1}
\;}\qquad(t\ge0),
\]
and for \(t>0\) the exact worst-case inclusive upper tail is
\[
\boxed{\;
\sup_{\rm exch}\Pr(T_n\ge t)
=
\frac{\lfloor R_n(t)\rfloor}{n+1}.
\;}
\]
By sign reversal the corresponding lower-tail formulas are identical:
\[
\sup_{\rm exch}\Pr(T_n<-t)
=
\frac{\lceil R_n(t)\rceil-1}{n+1},
\qquad
\sup_{\rm exch}\Pr(T_n\le -t)
=
\frac{\lfloor R_n(t)\rfloor}{n+1}.
\]

Every displayed supremum is attained by a finite-support exchangeable law.
Thus these are sharp finite-sample bounds, not merely asymptotic or moment
bounds.

Equivalently, the class of distributions of \(T_n\) has the exact p-box
\[
\underline F_n(x)=
\begin{cases}
0,&x<0,\\[2mm]
1-\dfrac{\lceil R_n(x)\rceil-1}{n+1},&x\ge0,
\end{cases}
\]
and
\[
\overline F_n(x)=
\begin{cases}
\dfrac{\lfloor R_n(|x|)\rfloor}{n+1},&x<0,\\[2mm]
1,&x\ge0.
\end{cases}
\]
Each nontrivial envelope value is attained.

## Deterministic reduction

Take an arbitrary deterministic nonconstant vector
\(y=(y_1,\ldots,y_M)\), where \(M=n+1\). Let
\[
m=\frac1M\sum_i y_i,\qquad
L^2=\frac1M\sum_i(y_i-m)^2,\qquad
u_i=\frac{y_i-m}{L}.
\]
Then
\[
\sum_i u_i=0,\qquad \sum_i u_i^2=M.
\]

For each \(i\), delete \(y_i\), and let \(T_i\) be the externally studentized
residual of the deleted observation relative to the remaining \(M-1=n\)
observations. Direct leave-one-out algebra gives
\[
T_i^2=
\frac{M(M-2)u_i^2}
{(M-1)(M-1-u_i^2)}
\]
whenever the denominator is positive, with the endpoint interpreted as
infinite. The sign of \(T_i\) is the sign of \(u_i\). Hence, for \(t\ge0\),
\[
T_i\ge t
\quad\Longleftrightarrow\quad
u_i\ge a_n(t),
\qquad
a_n(t):=\frac{nt}{\sqrt{n^2-1+nt^2}}.
\]

The needed one-sided count bound is the finite-vector form of Cantelli's
inequality. If
\[
\sum_{i=1}^M u_i=0,\qquad \sum_{i=1}^M u_i^2=M,
\]
then for \(a>0\)
\[
\#\{i:u_i\ge a\}
\le
\left\lfloor\frac{M}{1+a^2}\right\rfloor,
\]
and
\[
\#\{i:u_i>a\}
\le
\left\lceil\frac{M}{1+a^2}\right\rceil-1.
\]

For completeness, if \(r\) coordinates satisfy \(u_i\ge a\), their sum is at
least \(ra\). The remaining \(M-r\) coordinates sum to at most \(-ra\), so
Cauchy--Schwarz gives
\[
M=\sum_i u_i^2
\ge ra^2+\frac{r^2a^2}{M-r}
=\frac{rMa^2}{M-r}.
\]
Thus \(r\le M/(1+a^2)\); strict thresholding yields the strict integer version.

Substitution of \(a=a_n(t)\) gives the exact identity
\[
\frac{M}{1+a_n(t)^2}
=
\frac{n^2-1+nt^2}{n-1+nt^2}
=R_n(t).
\]

Finally, exchangeability implies that each coordinate is equally likely to
be the deleted coordinate. Therefore the probability for \(X_{n+1}\) is the
expected fraction of coordinates satisfying the deterministic event, which
proves the bounds for arbitrary exchangeable laws.

## Sharpness

Fix \(t>0\) and put
\[
r=\lfloor R_n(t)\rfloor
\]
for the inclusive tail. Consider the centered two-level vector of length
\(M=n+1\) having \(r\) copies of \(A>0\) and \(M-r\) copies of
\[
B=-\frac{r}{M-r}A.
\]
Give all permutations of this multiset equal probability. The resulting law
is exchangeable.

For every positive coordinate, its leave-one-out statistic satisfies
\[
T_{\rm high}^2
=
\frac{(M-2)(M-r)}{(M-1)(r-1)}
\]
when \(r\ge2\); for \(r=1\), deleting the unique high coordinate leaves zero
training variance and \(T_{\rm high}=+\infty\). The inequality
\(T_{\rm high}\ge t\) is equivalent to
\[
r\le R_n(t).
\]
Exactly \(r\) of the \(M\) coordinates therefore satisfy the upper-tail
event, giving probability \(r/M\), which attains the inclusive bound.

For the strict tail take
\[
r=\lceil R_n(t)\rceil-1.
\]
Then \(r<R_n(t)\), so the same construction gives
\(T_{\rm high}>t\) and attains the strict bound. Sign reversal gives the
lower-tail extremizers. The trivial sides of the p-box are attained by the
all-equal law.

## Consequences

1. **A range-free empirical Cantelli inequality.** The result uses only
   exchangeability and the observed sample mean and sample standard
   deviation. There is no population-moment assumption and no support or
   range term.

2. **Exact one-sided distribution-free prediction intervals.** The closed
   upper prediction interval
   \[
   (-\infty,\bar X_n+tS_n]
   \]
   has worst-case miscoverage
   \[
   \frac{\lceil R_n(t)\rceil-1}{n+1},
   \]
   and this value is sharp over exchangeable laws.

3. **Finite-sample staircase.** For example, with \(n=20\),
   \[
   t=\frac{19}{\sqrt{20}}=4.248529\ldots
   \]
   gives \(R_{20}(t)=2\), hence
   \[
   \Pr(X_{21}>\bar X_{20}+tS_{20})\le\frac1{21}
   =0.047619\ldots,
   \]
   exactly. The bound is attained.

4. **Classical Cantelli limit.** Away from the integer staircase,
   \[
   \frac{R_n(t)}{n+1}\longrightarrow \frac1{1+t^2}
   \]
   as \(n\to\infty\), recovering the classical one-sided Cantelli constant.

5. **Granularity is unavoidable.** For every finite \(t\),
   \(R_n(t)>1\), so the strict worst-case tail is at least \(1/(n+1)\).
   Under exchangeability alone, no finite multiplier can guarantee
   one-step prediction miscoverage below \(1/(n+1)\).

## Relation to prior work

Saw, Yang and Mo (1984) developed the empirical Chebyshev inequality with
estimated mean and variance and showed that exchangeability suffices.
Stellato, Van Parys and Goulart (2017) extended this empirical Chebyshev
line to the multivariate setting.

Troffaes and Basu (2019) explicitly sought a one-sided Cantelli analogue
based on \(\bar X_n\) and \(S_n\). Their theorem adds a positive
range-dependent correction to the denominator and therefore assumes
boundedness. They state in the introduction that they had not found a way
to avoid that correction; their discussion repeats that the offset is the
critical difference from Saw's bound. Their Lemma 7 already contains the
one-sided deterministic count inequality used above.

The present result keeps that deterministic Cantelli mechanism but combines
it with the exact leave-one-out transformation between the external
studentized residual and the full-sample standardized coordinate. This
removes the range correction entirely, yields the exact finite-\(n\)
integer staircase, and identifies explicit extremizers.

The claim here is specifically about the studentized prediction residual
and its induced p-box. It does **not** claim to solve the stronger problem
of converting such a p-box into a conditional p-box for the unstandardized
future observation after numerically conditioning on observed
\((\bar X_n,S_n)\).

## Reproducibility

`artifacts/check_empirical_cantelli.py` performs exact-rational checks of
the threshold transformation, inclusive and strict staircase formulas, and
two-level extremizers for \(2\le n\le80\) over a grid of rational \(t^2\).
Its recorded output is in `artifacts/verification_output.txt`.

## References

- J. G. Saw, M. C. K. Yang, and T. C. Mo, “Chebyshev Inequality with
  Estimated Mean and Variance,” *The American Statistician* 38(2),
  130–132 (1984). https://doi.org/10.1080/00031305.1984.10483182
- J. G. Saw, M. C. K. Yang, and T. Chin, correction to the preceding
  article, *The American Statistician* 42(2), 166 (1988).
- H. S. Konijn, “Distribution-Free and Other Prediction Intervals,”
  *The American Statistician* 41(1), 11–15 (1987).
  https://doi.org/10.1080/00031305.1987.10475433
- B. Stellato, B. P. G. Van Parys, and P. J. Goulart, “Multivariate
  Chebyshev Inequality With Estimated Mean and Variance,”
  *The American Statistician* 71(2), 123–127 (2017).
  https://doi.org/10.1080/00031305.2016.1186559
- M. C. M. Troffaes and T. Basu, “A Cantelli-Type Inequality for
  Constructing Non-Parametric P-Boxes Based on Exchangeability,”
  *Proceedings of Machine Learning Research* 103, 386–393 (2019).
  https://proceedings.mlr.press/v103/troffaes19a.html

## Limitations

Originality is asserted only to the best of our knowledge. The full text of
Konijn (1987) and the one-page Saw--Yang--Chin (1988) correction were not
inspected; either could in principle contain an equivalent one-sided
finite-sample formula, although the later Troffaes--Basu paper explicitly
identifies removal of its correction term as unresolved. Terminology in
older distribution-free prediction-interval literature may also hide an
equivalent statement.

The exact-attainment statements use the extended convention for zero sample
variance. If one instead restricts the model class to laws satisfying
\(S_n>0\) almost surely, the same inequalities remain valid; endpoint
attainment at some staircase configurations may need to be interpreted as
a limiting statement rather than by the two-level orbit law above.
