# Exact automatic-warmup phase diagram for RAdam
## Finding

RAdam uses
\[
\rho_t
=
\rho_\infty-\frac{2t\beta_2^t}{1-\beta_2^t},
\qquad
\rho_\infty=\frac{2}{1-\beta_2}-1,
\]
and activates its adaptive denominator and variance-rectification factor exactly when
\[
\rho_t>4.
\]

Write
\[
b=\beta_2\in(0,1)
\]
and define
\[
T(b)=\min\{t\ge1:\rho_t>4\},
\]
with \(T(b)=\infty\) if the gate never opens.

Then
\[
T(b)=\infty
\quad\Longleftrightarrow\quad
0<b\le\frac35.
\]

For each integer \(t\ge5\), define
\[
P_t(b)
=
-3-b+\sum_{j=2}^{t-1}(2j-3)b^j.
\]
There is a unique root
\[
b_t\in\left(\frac35,1\right)
\]
of \(P_t\). Setting \(b_4=1\),
\[
1=b_4>b_5>b_6>\cdots>\frac35,
\]
and the first rectified step is classified exactly by
\[
T(b)=t
\quad\Longleftrightarrow\quad
b_t<b\le b_{t-1}.
\]

Thus the source rule performs exactly \(T(b)-1\) unadapted momentum updates before the first rectified update.

The first thresholds are
\[
b_5\approx0.7733030257,\quad
b_6\approx0.6900101730,\quad
b_7\approx0.6509077338,
\]
\[
b_8\approx0.6301877301,\quad
b_9\approx0.6184164052,\quad
b_{10}\approx0.6114341784,\quad
b_{11}\approx0.6071765266.
\]
Hence
\[
T(0.8)=T(0.9)=T(0.99)=T(0.999)=5,
\]
while
\[
T(0.7)=6,\qquad T(0.65)=8,\qquad T(0.61)=11.
\]

The thresholds approach the source degeneracy boundary exponentially:
\[
b_t
=
\frac35
+
\frac4{25}
t
\left(\frac35\right)^t
(1+o(1)).
\]
Therefore RAdam's automatic unadapted phase is not intrinsically a fixed four- or five-step phenomenon: it is a sharply quantized function of \(\beta_2\), and it becomes arbitrarily long as \(\beta_2\downarrow0.6\).

## Assumptions and scope

The theorem concerns Algorithm 2 of the defining RAdam paper and its source criterion \(\rho_t>4\). It analyzes only when rectification is activated. The schedule is independent of gradients, the objective, \(\beta_1\), and the base learning rate.

Some later implementations use a different numerical gate such as \(\rho_t>5\). Those variants have a different threshold sequence.

The result is exact conditional on RAdam's published effective-SMA statistic; it does not validate the statistical approximation used to motivate that statistic.

## Proof

Since
\[
\rho_\infty=\frac{1+b}{1-b},
\]
\[
\rho_t
=
\frac{1+b}{1-b}
-
\frac{2tb^t}{1-b^t}.
\]

For fixed \(0<b<1\), \(\rho_t\) is strictly increasing. Indeed,
\[
\frac{tb^t}{1-b^t}
>
\frac{(t+1)b^{t+1}}{1-b^{t+1}}
\]
is equivalent to
\[
t-(t+1)b+b^{t+1}>0.
\]
The latter expression decreases to zero as \(b\uparrow1\), because its derivative is
\[
(t+1)(b^t-1)<0.
\]

Also
\[
\lim_{t\to\infty}\rho_t=\frac{1+b}{1-b}.
\]
Thus activation is impossible exactly when
\[
\frac{1+b}{1-b}\le4,
\]
namely \(b\le3/5\); for \(b>3/5\), strict monotonicity gives a finite activation index.

For \(t\le4\), \(\rho_t<t\le4\), so the gate cannot open before step \(5\).

For \(t\ge5\), \(\rho_t>4\) is equivalent to
\[
5b-3
>
b^t\left[(2t-3)+(5-2t)b\right].
\]
Let
\[
F_t(b)
=
5b-3
-
b^t\left[(2t-3)+(5-2t)b\right].
\]
A finite-sum expansion gives
\[
F_t(b)=(b-1)^2P_t(b).
\]

The coefficient sequence of \(P_t\) has exactly one sign change, so Descartes' rule gives exactly one positive root. Moreover
\[
F_t\left(\frac35\right)
=
-\frac{4t}{5}\left(\frac35\right)^t<0,
\]
whereas
\[
P_t(1)
=
-4+\sum_{j=2}^{t-1}(2j-3)
=
t(t-4)>0.
\]
Hence the unique positive root lies in \((3/5,1)\), and
\[
\rho_t>4
\quad\Longleftrightarrow\quad
b>b_t.
\]

Since \(\rho_{t+1}(b)>\rho_t(b)\), one has \(b_{t+1}<b_t\). Their limit is \(3/5\), because every fixed \(b>3/5\) eventually satisfies the gate. This proves
\[
T(b)=t
\quad\Longleftrightarrow\quad
b_t<b\le b_{t-1}.
\]

For the asymptotic, write
\[
b_t=\frac35+\delta_t.
\]
At \(F_t(b_t)=0\),
\[
5\delta_t
=
b_t^t
\left[
\frac{4t}{5}+(5-2t)\delta_t
\right],
\]
so
\[
\delta_t
=
\frac{(4t/25)b_t^t}
{1+((2t-5)/5)b_t^t}.
\]
This makes \(\delta_t\) exponentially small; consequently
\[
\left(\frac{b_t}{3/5}\right)^t\to1
\]
and the denominator tends to one. Therefore
\[
\delta_t
\sim
\frac4{25}t\left(\frac35\right)^t.
\]

## Verification

The accompanying `verify.py` evaluates the source formula, computes the threshold roots by bisection, checks the polynomial factorization, verifies representative activation indices, and checks the asymptotic ratio.

These calculations are transcription guards. Root uniqueness, the exact phase partition, and the asymptotic law are proved analytically above.

## Relationship to prior work

Liu, Jiang, He, Chen, Liu, Gao, and Han introduced RAdam to control the large early variance of Adam's adaptive learning rate. Their paper defines \(\rho_t\), activates the adaptive rate only when \(\rho_t>4\), states that \(\beta_2\le0.6\) makes RAdam degenerate to momentum SGD, and says that RAdam automatically controls warmup behavior through the moving-average rule.

The inspected defining paper does not partition \(\beta_2\) into exact first-activation intervals, give the threshold polynomials \(P_t\), or state the exponential accumulation of the thresholds at \(0.6\).

The official project documentation emphasizes the warmup motivation and practical robustness but likewise does not give the exact first-rectification index as a function of \(\beta_2\).

Focused published-record searches for RAdam activation steps, exact warmup length, threshold polynomials, and effective-SMA phase diagrams did not identify a covering statement.

## Limitations

The theorem uses the source gate \(\rho_t>4\). Other software gates require separate threshold sequences.

The result determines timing, not whether a given timing is optimal for a training problem.

The source effective-SMA statistic is itself motivated by an approximation; the theorem is exact only after that statistic is adopted.

The long-warmup asymptotic occurs near \(\beta_2=0.6\), below common modern defaults.

## References

1. Liyuan Liu, Haoming Jiang, Pengcheng He, Weizhu Chen, Xiaodong Liu, Jianfeng Gao, and Jiawei Han, “On the Variance of the Adaptive Learning Rate and Beyond,” arXiv:1908.03265v1, 2019.
2. LiyuanLucasLiu/RAdam, official public implementation repository and project documentation.
