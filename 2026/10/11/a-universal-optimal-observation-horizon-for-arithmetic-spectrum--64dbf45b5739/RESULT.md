# A universal optimal observation horizon for arithmetic-spectrum flows

## Finding
Consider the stable real linear flow with \(2k\) distinct rates \(\lambda_j=a+dj\), where \(a,d>0\), \(k\ge2\), and \(0\le j<2k\). Measure the two-dimensional observable consisting of total amplitude and its instantaneous decay slope. The \(2k\) observations at equally spaced times \(0,t,\ldots,(k-1)t\) uniquely determine the initial state for every \(t>0\). With independent equal-variance measurement noise, there is exactly one positive spacing \(t_k\) that maximizes the determinant of the state Fisher-information matrix within the equally spaced design family. It is characterized exactly and has a universal finite limiting observation horizon.

Write \(q=e^{-dt}\) and
\[
\beta_k=k(k-1)\left(\frac ad+\frac{4k-5}{6}\right).
\]
The square observation matrix satisfies the exact determinant formula
\[
\boxed{\ |\det H_k(t)|=d^k q^{\beta_k}\prod_{h=1}^{k-1}(1-q^h)^{4(k-h)}.\ }
\]
The unique optimum is \(t_k=-d^{-1}\log q_k\), where \(q_k\in(0,1)\) uniquely solves
\[
\boxed{\ \beta_k=4\sum_{h=1}^{k-1}\frac{h(k-h)q_k^h}{1-q_k^h}.\ }
\]
For any fixed \(a/d>0\), as \(k\to\infty\),
\[
\boxed{\ t_k=\frac{c_*}{dk}+O_{a/d}\!\left(\frac{1}{dk^2}\right),\qquad (k-1)t_k\longrightarrow\frac{c_*}{d}.\ }
\]
The universal constant \(c_*\approx2.121467655793\) is the unique positive root of
\[
4\int_0^1\frac{x(1-x)}{e^{c_*x}-1}\,dx=\frac23.
\]
For \(k=2\), the exact optimizer is \(q_2=(2a+d)/(2a+5d)\).

## Assumptions and scope
Fix an integer \(k\ge2\), positive real parameters \(a,d\), and indices \(j=0,\ldots,2k-1\). The state \(u\in\mathbb R^{2k}\) obeys \(\dot u_j=-\lambda_j u_j\) with \(\lambda_j=a+dj\). The measured output is
\[
y(s)=\begin{pmatrix}\sum_{j=0}^{2k-1}u_j(s)\\sum_{j=0}^{2k-1}\lambda_j u_j(s)\end{pmatrix}
=\begin{pmatrix}m(s)\-\dot m(s)\end{pmatrix}.
\]
At each \(s=\ell t\), \(\ell=0,\ldots,k-1\), both scalar output components are measured. Ordering rows by successive time and then by component, the resulting \(2k\times2k\) matrix is
\[
H_{(\ell,0),j}=e^{-\lambda_j\ell t},\qquad H_{(\ell,1),j}=\lambda_j e^{-\lambda_j\ell t}.
\]
Noise, when used to interpret optimality, is centered independent Gaussian with the same fixed variance \(\sigma^2>0\) in every one of the \(2k\) scalar measurements, expressed in these fixed sensor units. Thus the information matrix for the initial coordinates is \(I(t)=\sigma^{-2}H_k(t)^{\mathsf T}H_k(t)\). The result optimizes \(\det I(t)\) over \(t>0\) with **the two fixed sensors and equally spaced time grids**, not among arbitrary grids or sensor allocations.

## Proof
**Confluent determinant.** Set \(x_\ell=e^{-d\ell t}=q^\ell\). Each pair of rows at time \(\ell t\) has the common factor \(e^{-a\ell t}\). After removing it from both rows, subtract \(a\) times the first row from the second and divide the latter by \(d\). The pair then has entries \(x_\ell^j\) and \(j x_\ell^j\). Factor \(x_\ell\) from the second row. The remaining rows are ordinary polynomial value and first-derivative evaluations, \(x_\ell^j\) and \(j x_\ell^{j-1}\), for degrees \(0\le j<2k\).

For distinct \(x_0,\ldots,x_{k-1}\), their confluent Vandermonde determinant has absolute value \(\prod_{0\le\ell<r<k}|x_r-x_\ell|^4\). This identity follows, for example, by taking the paired-node limit of the ordinary Vandermonde determinant after dividing each within-pair difference, and requires no outside computational certificate. Undoing the row factors gives
\[
|\det H_k|=d^k\prod_{\ell=0}^{k-1}e^{-2a\ell t}x_\ell
\prod_{\ell<r}|x_r-x_\ell|^4.
\]
Since \(|q^r-q^\ell|=q^\ell(1-q^{r-\ell})\), the exponent of \(q\) is
\[
\frac ad k(k-1)+\frac{k(k-1)}2+\frac{2k(k-1)(k-2)}3
=k(k-1)\left(\frac ad+\frac{4k-5}{6}\right).
\]
Counting each difference \(h=r-\ell\) with multiplicity \(k-h\) proves the displayed determinant formula. Because \(d>0\), \(\beta_k>0\), and \(0<q<1\), it is nonzero for all \(t>0\), proving exact initial-state recoverability. With fewer than \(k\) two-component sample times, at most \(2(k-1)\) independent scalar equations exist, so recovery of an arbitrary \(2k\)-dimensional initial state is impossible.

**Unique D-optimal spacing.** As \(t\) varies over positive reals, \(q=e^{-dt}\) ranges over \((0,1)\). The fixed-variance information determinant is \(\sigma^{-4k}|\det H_k(t)|^2\). Its maximizers are those of
\[
L(q)=\beta_k\log q+4\sum_{h=1}^{k-1}(k-h)\log(1-q^h).
\]
The stationarity equation \(qL'(q)=0\) is precisely the equation for \(q_k\). Its right side is continuous and strictly increasing from zero to infinity as \(q\) runs from zero to one, so the root exists and is unique. The product vanishes at both endpoints; hence this stationary point is the unique global maximizer.

**Universal horizon.** Put \(c_k=dk t_k=-k\log q_k\). Dividing the stationary equation by \(k^3\), write it as
\[
\frac{\beta_k}{k^3}=\frac4k\sum_{h=1}^{k-1}
\frac{(h/k)(1-h/k)}{\exp(c_k h/k)-1}.
\]
The left side is \(2/3+O_{a/d}(k^{-1})\). For fixed \(c>0\), the summand extends continuously to the origin with value \(1/c\), and the Riemann sum equals
\[
4\int_0^1\frac{x(1-x)}{e^{cx}-1}\,dx+O_c(k^{-1}).
\]
The integral is strictly decreasing and continuous in \(c\), tends to infinity as \(c\downarrow0\), and tends to zero as \(c\to\infty\). Hence the limiting equation has a unique positive root \(c_*\). The same Riemann convergence is uniform on compact positive \(c\)-intervals, which traps the roots \(c_k\) and yields \(c_k\to c_*\). Since the integral's derivative at \(c_*\) is strictly negative, the uniform \(O(k^{-1})\) Riemann-sum bound and the implicit mean-value estimate sharpen this to \(c_k=c_*+O_{a/d}(k^{-1})\). Dividing by \(dk\) proves the spacing and observation-horizon limits.

Finally, \(k=2\) reduces the optimum equation to \(2a/d+1=4q/(1-q)\), giving the stated rational formula.

## Verification
The included standalone `CHECK.py` uses exact rational elimination to independently compute the determinant of the explicit \(2k\times2k\) sampling matrix for \(k=2,3,4,5\), two rational decay factors, and two integer-parameter sensor settings (16 exact determinant cases). It compares against the product identity, then checks the two-time root, uniqueness bracketing, and limiting integral numerically. Run with `python3 CHECK.py`. The reproduced output is `VERIFY_OK 31 exact_or_numeric_tests cstar=2.121467655793`; the diagnostic count refers to the cases actually enumerated in the code. This finite verification is a regression check; it does not replace the general confluent determinant argument or the Riemann-limit proof.

## Relationship to prior work
Liu and Xiu (2026, arXiv:2603.20641v1, Sections 3.1–3.2 and Appendix A) establish finite delay representations for general linear observables, emphasizing existence and generic invertibility. Their theorem does not determine the determinant of a two-sensor arithmetic-spectrum sampling matrix, select its unique D-optimal equally spaced temporal mesh, or evaluate the growing-mode optimal horizon. The distinction is quantitative experimental-design optimality, not general qualitative reconstructibility.

Confluent Vandermonde evaluation and Hermite interpolation are classical; their determinant identity is an input to the proof, not asserted as an independently new discovery. This includes the broad matrix-interpolation literature such as Bolotnikov (2015). Dette, Melas and Wong (2006) investigate locally D-optimal designs for nonlinear sums of two or three exponential terms; their stated design domain differs from fixed-rate, arbitrary-even-dimension, two-sensor, equally spaced initial-state inference. Published mathematical-record searches did not reveal an exact predecessor of the combined all-size design law and universal horizon, but the possibility of an equivalent formulation in older optimal-design literature is a residual priority risk.

## Limitations
D-optimality is only within the one-parameter family of equally spaced sampling times, with the two fixed outputs and a fixed iid equal-variance noise model. It does not claim optimality among arbitrary nonuniform grids, sensor selections, nonisotropic or correlated noise, or other criteria such as minimum singular value. The universal asymptotic fixes \(a/d>0\) as \(k\to\infty\). Positive and arithmetic eigenvalue magnitudes are essential to this determinant formula. The finite checker cannot certify statements for all \(k\). No independent scientific audit has been performed.

## References
1. X. Liu and D. Xiu, *Predictability of Observables of Dynamical Systems*, arXiv:2603.20641v1, first posted 2026-03-21. https://arxiv.org/html/2603.20641v1
2. V. Bolotnikov, *Confluent Vandermonde matrices, divided differences, and Lagrange–Hermite interpolation over quaternions*, arXiv:1505.03574 (2015). https://arxiv.org/abs/1505.03574
3. H. Dette, V. B. Melas, and W. K. Wong, *Locally D-optimal designs for exponential regression models*, Statistica Sinica 16 (2006), 789–803. https://www3.stat.sinica.edu.tw/statistica/j16n3/j16n36/j16n36.html
