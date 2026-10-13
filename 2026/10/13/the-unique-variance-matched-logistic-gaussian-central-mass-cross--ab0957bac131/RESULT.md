# The unique variance-matched logistic–Gaussian central-mass crossover
## Finding
Let \(L\) be a logistic random variable standardized to mean \(0\) and variance \(1\), and let \(Z\sim N(0,1)\). Define
\[
C_L(c)=\Pr\{|L|\le c\},\qquad C_N(c)=\Pr\{|Z|\le c\},\qquad c\ge0.
\]
There is exactly one positive crossover radius
\[
c_\star=1.74447161774732\ldots
\]
such that \(C_L(c_\star)=C_N(c_\star)\). The ordering is
\[
C_L(c)>C_N(c)\quad\text{for }0<c<c_\star,
\]
and
\[
C_L(c)<C_N(c)\quad\text{for }c>c_\star.
\]
If \(\beta=\pi/\sqrt3\), then
\[
\frac{1-C_L(c)}{1-C_N(c)}
\sim c\sqrt{2\pi}\exp\!\left(\frac{c^2}{2}-\beta c\right)\to\infty
\qquad(c\to\infty).
\]

## Assumptions and scope
A logistic law with location \(\mu\) and scale \(s>0\) has mean \(\mu\) and variance \(\pi^2s^2/3\). Standardization removes both parameters. The comparison is for symmetric intervals centered at the common mean and measured in units of the common standard deviation. It is not an optimization over logistic scales.

## Proof
Put
\[
a=\frac{\pi}{2\sqrt3},\qquad H(c)=C_L(c)-C_N(c).
\]
The standardized logistic CDF gives
\[
C_L(c)=\tanh(ac),\qquad C_N(c)=2\Phi(c)-1,
\]
so
\[
H'(c)=a\,\operatorname{sech}^2(ac)-2\varphi(c).
\]
Define
\[
R(c)=\log\frac{a\,\operatorname{sech}^2(ac)}{2\varphi(c)}.
\]
Then \(H'(c)\) has the sign of \(R(c)\). If
\[
S(c)=R'(c)=c-2a\tanh(ac),
\]
then
\[
S'(c)=1-2a^2\operatorname{sech}^2(ac),\qquad
S''(c)=4a^3\operatorname{sech}^2(ac)\tanh(ac)>0
\]
for \(c>0\). Hence \(S'\) is strictly increasing. Since \(S'(0)=1-\pi^2/6<0\) and \(S'(c)\to1\), it has exactly one positive zero. Since \(S(0)=0\) and \(S(c)\to\infty\), \(S\) has exactly one positive zero after first decreasing. Thus \(R\) first decreases and then increases.

Moreover,
\[
R(0)=\log\!\left(a\sqrt{\frac{\pi}{2}}\right)>0,
\]
because the square of the logarithm's argument is \(\pi^3/24>1\). The bundled computation gives the safely separated signs
\[
R(1)=-0.101500505268433\ldots<0,\qquad
R(2)=-0.165702102485606\ldots<0.
\]
Since \(R(c)\to\infty\), \(R\) has exactly two positive zeros \(r_1,r_2\) with \(0<r_1<1<2<r_2\). Therefore \(H\) increases on \((0,r_1)\), decreases on \((r_1,r_2)\), and increases on \((r_2,\infty)\).

At \(c=1\),
\[
H(1)=0.036951378155461\ldots>0.
\]
For \(c=2\), repeated integration by parts gives
\[
Q(2)<\varphi(2)\left(\frac12-\frac18+\frac3{32}\right)=\frac{15}{32}\varphi(2),
\]
so
\[
1-C_N(2)<\frac{15}{16}\varphi(2)=0.0506165311061138\ldots.
\]
The standardized logistic two-sided tail is
\[
1-C_L(2)=\frac2{1+\exp(2\pi/\sqrt3)}
=0.0517834658747107\ldots,
\]
hence \(H(2)<0\). The derivative pattern now gives exactly one positive zero: \(H\) is positive before its unique crossing in \((1,2)\), negative afterward, and increases to \(0\) only after its second stationary point.

Finally,
\[
1-C_L(c)\sim2e^{-\beta c},\qquad
1-C_N(c)=2Q(c)\sim\frac{2\varphi(c)}{c},
\]
which yields the stated tail ratio.

## Verification
The bundled `verify.py` recomputes \(R(1)\), \(R(2)\), \(H(1)\), \(H(2)\), the Gaussian-tail upper certificate at \(c=2\), and the unique root on \((1,2)\) by bisection. It also stress-tests the sign pattern on a deterministic mesh. The grid is not used to prove uniqueness; the global theorem follows from the derivative argument.

## Relationship to prior work
Sun, Hu, and Sun study the same variance-normalized central-mass functional. Their arXiv version 2, first public on 2023-05-10, adds the logistic family and proves only the radius-one comparison
\[
C_L(1)=0.719641\ldots>C_N(1)=0.6827\ldots.
\]
The inspected logistic section gives the moments and CDF and evaluates that one radius; it does not state an all-radius crossover.

Bowling, Khasawneh, Kaewkuekool, and Cho study logistic approximations to the normal CDF. Their indexed material discusses the unit-variance logistic scale and then fitted approximation accuracy, but no exact variance-matched unique-crossing theorem or tail-ratio law was located. A full-PDF retrieval attempt for that paper did not complete, so an equivalent numerical observation in its figures or discussion remains a residual risk.

## Limitations
The theorem is specific to the variance-matched logistic and Gaussian laws and symmetric central intervals. It does not optimize logistic scale or classify asymmetric intervals. The decimal value of \(c_\star\) is a locator for the analytically unique root. Older probit-versus-logit approximation literature may contain a numerically equivalent crossing under different terminology.

## References
1. P. Sun, Z.-C. Hu, and W. Sun, *Variation comparison between infinitely divisible distributions and the normal distribution*, arXiv:2304.11459v2, 2023; later *Statistical Papers* 65 (2024), 4405–4429, DOI 10.1007/s00362-024-01561-1.
2. S. R. Bowling, M. T. Khasawneh, S. Kaewkuekool, and B. R. Cho, *A logistic approximation to the cumulative normal distribution*, *Journal of Industrial Engineering and Management* 2 (2009), 114–127, DOI 10.3926/jiem.2009.v2n1.p114-127.
