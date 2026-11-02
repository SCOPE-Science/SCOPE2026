# Logarithmic ballistic scattering and a uniform velocity gap in a rational planar map

## Finding
**Theorem.** For arbitrary real parameters \(a>0\), \(c\ne0\), consider the planar rational iteration
\[
F_{a,c}(x,y)=\left( x+\frac{ax}{1+y^2},\ y+cx\right),\qquad (x,y)\in\mathbb R^2.
\]
The equilibrium set is precisely \(\{0\}\times\mathbb R\), and every initial condition on this line is fixed. For **every** initial point \((x_0,y_0)\) with \(x_0\ne0\), there are real constants \(X\ne0\) and \(C\), depending on that point and the parameters, such that \(\operatorname{sgn}X=\operatorname{sgn}x_0\), and, as the positive integer \(n\to\infty\),
\[
\begin{aligned}
x_n&=X-\frac{a}{c^2X}\frac1n+O\!\left(\frac{\log n}{n^2}\right),\\
y_n&=cXn-\frac{a}{cX}\log n+C+O\!\left(\frac{\log n}{n}\right).
\end{aligned}
\]
In particular, \(y_n\to\operatorname{sgn}(cx_0)\cdot\infty\) and \(\lim_{n\to\infty}(y_n-y_0)/n=cX\ne0\). Moreover, writing \(s=\operatorname{sgn}(cx_0)\) and
\[
R^2=\max\{y_0^2,(y_0+s)^2\},
\]
the limiting velocity satisfies the **uniform-in-\(x_0\)** lower bound
\[
\boxed{\ |cX|\ge\frac{a}{1+R^2}>0.\ }
\]
Consequently no nonfixed orbit is recurrent, and the invariant Borel probability measures on \(\mathbb R^2\) are **exactly** the probability measures supported on the fixed line. Thus no nonempty compact forward-invariant set can contain a point outside the fixed line.

## Assumptions and scope
The system is iterated in **exact real arithmetic** with \(a>0\), \(c\in\mathbb R\setminus\{0\}\), and unrestricted real initial coordinates. The two additive parameters of the parent family \(x'=x+ax/(1+y^2)+b\), \(y'=y+cx+d\) are set to \(b=d=0\), the natural equilibrium-line regime. Constants in the error bounds may depend on \(a,c,x_0,y_0\); the explicitly displayed velocity lower bound does not depend on \(x_0\) at fixed \(a,y_0\). Here \(\operatorname{sgn}\) is the usual sign and the displayed \(O\)-terms concern the integer limit \(n\to\infty\). No global smooth dependence of \(X\) or \(C\) on initial conditions is asserted.

## Proof
**1. Exact one-sided triangularization.** The first coordinate is multiplied at every step by \(1+a/(1+y_n^2)>1\). Thus if \(x_0\ne0\), its sign never changes. Set
\[
s=\operatorname{sgn}(cx_0),\quad z_n=s y_n,\quad w_n=|c x_n|.
\]
A direct substitution yields the exact scalar feedback equations
\[
\boxed{\quad z_{n+1}=z_n+w_n,\qquad
w_{n+1}=w_n\left(1+\frac{a}{1+z_n^2}\right),\quad w_0>0.\quad}
\]
Therefore \(w_n\) is strictly increasing and \(z_n\ge z_0+n w_0\to+\infty\). In particular, for all sufficiently large \(n\), \(z_n\ge (w_0/2)n\), and hence
\[
\sum_{n=0}^{\infty}\frac{1}{1+z_n^2}<\infty.
\]
From \(\log(1+t)\le t\) for nonnegative \(t\),
\[
\log\frac{w_n}{w_0}=\sum_{k=0}^{n-1}\log\left(1+\frac{a}{1+z_k^2}\right)
\le a\sum_{k=0}^{\infty}\frac{1}{1+z_k^2}<\infty.
\]
Consequently \(w_n\uparrow W\in(0,\infty)\), with \(W\ge w_0\), and \(x_n=s w_n/c\to X=sW/c\ne0\). By Cesàro summation of \(z_{n+1}-z_n=w_n\), \(z_n/n\to W\).

**2. First tail estimates.** The preceding limits give \(z_n=\Theta(n)\), \(w_n=O(1)\), and
\[
0<w_{n+1}-w_n=\frac{a w_n}{1+z_n^2}=O(n^{-2}).
\]
As the increasing \(w_n\) has finite limit \(W\), tail summation gives \(W-w_n=O(n^{-1})\). Another sum now gives
\[
z_n=z_0+\sum_{k=0}^{n-1} w_k=Wn+O(\log n).
\]
Substitute both estimates into the *exact* increment identity. For all sufficiently large positive integers \(n\),
\[
\frac{a w_n}{1+z_n^2}
=\frac{a}{W n^2}+O\!\left(\frac{\log n}{n^3}\right).
\]
This follows because the numerator is \(aW+O(n^{-1})\) and the denominator is \(W^2n^2+O(n\log n)\). Tail summation of the last display, using
\[
\sum_{k=n}^{\infty}\frac1{k^2}=\frac1n+O(n^{-2}),\qquad
\sum_{k=n}^{\infty}\frac{\log k}{k^3}=O\!\left(\frac{\log n}{n^2}\right),
\]
yields
\[
w_n=W-\frac{a}{Wn}+O\!\left(\frac{\log n}{n^2}\right).
\]
Since \(x_n=s w_n/c\), \(X=sW/c\), and \(c^2X=csW\), the first displayed asymptotic in the theorem follows.

**3. The logarithm and finite renormalized constant.** For sufficiently large \(n\), set
\[
v_n=z_n-Wn+\frac aW\log n.
\]
The exact update and preceding estimate give
\[
\begin{aligned}
v_{n+1}-v_n
&=w_n-W+\frac aW\log(1+1/n)\\
&=O\!\left(\frac{\log n}{n^2}\right).
\end{aligned}
\]
These increments are absolutely summable, so \(v_n\to C_z\in\mathbb R\). Their tail is \(O((\log n)/n)\), proving
\[
z_n=Wn-\frac aW\log n+C_z+O\!\left(\frac{\log n}{n}\right).
\]
Multiplying by \(s\), with \(cX=sW\), gives the asserted expansion for \(y_n\), with \(C=sC_z\). This proves the asymptotic conclusions for **every** nonfixed real orbit, without restrictions on the starting signs.

**4. A positive escape velocity bounded independently of transverse displacement.** Keep \(z_0=s y_0\), and choose \(N\ge1\) to be the first index at which \(z_N\ge z_0+1\); such an index exists by monotone divergence. For \(0\le k<N\) one has \(z_k\in[z_0,z_0+1)\) and hence \(z_k^2\le R^2\), because the maximum squared absolute value on a closed interval occurs at an endpoint. Let
\[
r=1+\frac{a}{1+R^2}>1.
\]
Then \(w_{k+1}\ge r w_k\) for each \(0\le k<N\). Reversing these inequalities and summing the geometric bound gives
\[
1\le z_N-z_0=\sum_{k=0}^{N-1}w_k
\le w_N\sum_{j=1}^{N}r^{-j}
<\frac{w_N}{r-1}.
\]
Thus \(W\ge w_N\ge r-1=a/(1+R^2)\), proving the advertised bound. The argument is valid even for arbitrarily small \(|x_0|\). In fact the asymptotic velocity cannot tend to zero as nonstationary initial points approach the equilibrium line with \(y_0\) fixed.

**5. Recurrence and invariant probabilities.** Since \(z_n\to+\infty\), any nonfixed orbit leaves every compact subset of \(\mathbb R^2\) eventually; it is neither recurrent nor contained in a compact forward-invariant set. Every point with \(x_0=0\) is fixed. If \(\mu\) is an invariant Borel probability, Poincaré recurrence for the probability-preserving endomorphism \(F_{a,c}\) on a countably based metric space implies that almost every point is recurrent; all such points belong to \(x=0\), so \(\mu(\{x=0\})=1\). Conversely, every Borel probability supported on that fixed line is invariant. This completes the proof.

## Verification
The accompanying standalone Python program `verification.py` checks the exact coordinate transformations using three rational parameter/initial-value tuples and examines the stated asymptotics for five independent parameter cases with high-precision decimal arithmetic. It checks the sign invariant, estimated limiting horizontal position, convergence of the renormalized vertical intercept, and the uniform velocity lower bound. It executed without exceptions. In particular one diagnostic takes \(|x_0|=10^{-12}\), illustrating that a tiny transverse displacement does not imply tiny terminal velocity. These finite checks are diagnostic only; all infinite-time, all-initial-data and invariant-measure statements follow from the analytic proof above.

To reproduce: `python3 verification.py`. The program needs only the Python standard library. No approximation or numerical stopping criterion is used in the proof.

## Relationship to prior work
Zhang, Liu, Wei, Jiang and Bi introduced the parent rational map and identified its equilibrium-line regime; the defining paper's full accessible article, notably its system model, fixed-point analysis, Case I and conclusions, was examined. Its experiments and bifurcation diagrams in this regime focus on negative values of \(a\), including chaotic dynamics. The article does not state the positive-feedback global ballistic-scattering theorem, the exact reciprocal-time/logarithmic corrections, the velocity gap, or the invariant-probability classification. A separately known period-two census for the same \(b=d=0\) family concerns \(a<-2\); its absence-of-two-cycles statement for \(a\ge-2\) does not entail the present global results. General escape results for different rational or piecewise systems do not directly imply the displayed coefficients for this map.

## Limitations
All conclusions require \(a>0\), \(c\ne0\), and \(b=d=0\). The results do not classify the negative-feedback chaotic regime, nonzero additive forcings, rates uniform over all real initial \(y_0\), or nonstationary finite-precision implementations. The scattering constant \(X\) and renormalized intercept \(C\) are orbit-dependent and not given as elementary formulas. The review of accessible literature and indexed records does not prove absolute publication novelty; unindexed equivalent arguments remain a residual priority risk. The proof has not undergone independent mathematical audit.

## References
1. L.-P. Zhang, Y. Liu, Z.-C. Wei, H.-B. Jiang, Q.-S. Bi, "A class of two-dimensional rational maps with self-excited and hidden attractors," *Chinese Physics B* **31** (2022), 030503, DOI `10.1088/1674-1056/ac4025`. Full article: https://cpb.iphy.ac.cn/fileCPB/journal/article/cpb/html/2022/1674-1056/cpb_31_3_030503.shtml ; publisher manuscript-online date: 2021-12-05, https://cpb.iphy.ac.cn/EN/10.1088/1674-1056/ac4025 .
2. Poincaré recurrence theorem for invariant finite measures; classical standard result, used only for the stationary-measure corollary.
