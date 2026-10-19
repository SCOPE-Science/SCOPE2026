# Exact zero-digit fluctuations and switching-bias extrema in random symmetric doubling

## Finding

For the random symmetric doubling maps at the endpoint parameter \(\alpha=1\), let the branch map \(T_0\) be chosen independently with probability \(p\in(0,1)\), and \(T_1\) with probability \(1-p\). Start the interval coordinate in its absolutely continuous stationary law and write \(D_n\in\{0,1\}\) for the indicator that the \(n\)-th signed binary digit is zero. Let \(H_N=\sum_{n=0}^{N-1}D_n\), \(h=p(1-p)\), and \(q=1-p\).

**Exact finite-length law.** For every integer \(N\ge0\) and complex \(z\), the probability-generating polynomial is

\[
\mathbb E[z^{H_N}]=(q,p)M_p(z)^N\begin{pmatrix}1\\1\end{pmatrix},
\qquad
M_p(z)=\frac12\begin{pmatrix}
1+qz&p\\q&1+pz
\end{pmatrix}.
\]

Its eigenvalues are

\[
\lambda_\pm(z)=\frac{2+z\pm\sqrt{4h+(1-4h)z^2}}4,
\]

where the square root denotes the positive root for real \(z>0\). The digit-zero mean \(\mu=\mathbb E[D_0]=\tfrac12-h\) agrees with the previously known frequency. For every \(k\ge1\),

\[
\operatorname{Cov}(D_0,D_k)
=\frac{h(1-4h)}4\,2^{-(k-1)}.
\]

Thus, within \(0<p<1\), the zero indicators are independent and identically distributed **if and only if \(p=1/2\)**; then they are Bernoulli with success probability \(1/4\). For other biases, every positive-lag covariance is strictly positive.

**Exact finite-length variance and its sharp extrema.** For every \(N\ge1\),

\[
\operatorname{Var}(H_N)
=N\Gamma(p)-2h(1-4h)(1-2^{-N}),
\qquad
\Gamma(p)=\frac14+h-5h^2.
\]

Consequently \(\lim_{N\to\infty}\operatorname{Var}(H_N)/N=\Gamma(p)\), and \(\Gamma\) has its unique global minimum \(3/16\) at \(p=1/2\), whereas its two global maxima are exactly \(3/10\) at

\[
p=\frac{1\pm\sqrt{3/5}}2.
\]

The centered counts satisfy the annealed central limit theorem

\[
\frac{H_N-N\mu}{\sqrt N}\ \xrightarrow{\mathrm d}\ \mathcal N(0,\Gamma(p)).
\]

**Full frequency large deviations.** For every \(t\in\mathbb R\), the limiting logarithmic moment-generating function exists and equals

\[
\Lambda_p(t)=\lim_{N\to\infty}\frac1N\log\mathbb E[e^{tH_N}]
=\log\!\left(\frac{2+e^t+\sqrt{4h+(1-4h)e^{2t}}}{4}\right).
\]

The random frequencies \(H_N/N\) obey a large-deviation principle at speed \(N\) with good rate

\[
I_p(u)=\sup_{t\in\mathbb R}\{tu-\Lambda_p(t)\},\quad 0\le u\le1;
\qquad I_p(u)=+\infty\quad\text{otherwise}.
\]

In particular, the two rare-event endpoints have the explicit rates

\[
I_p(0)=\log\frac2{1+\sqrt h},\qquad
I_p(1)=\log\frac2{\max\{p,1-p\}}.
\]

## Assumptions and scope

The maps act on \([-1,1]\) and are the specialization of the random symmetric doubling family introduced in the cited primary work:

\[
T_0(x)=\begin{cases}
2x+1,&-1\le x\le0,\\
2x,&0<x\le1/2,\\
2x-1,&1/2<x\le1,
\end{cases}\qquad
T_1(x)=\begin{cases}
2x+1,&-1\le x<-1/2,\\
2x,&-1/2\le x<0,\\
2x-1,&0\le x\le1.
\end{cases}
\]

At each step the choices are independent of the past and of the initial point. The stationary interval law has the density

\[
f_p(x)=q\,\mathbf1_{[-1,0]}(x)+p\,\mathbf1_{[0,1]}(x),
\]

up to values on endpoints. The signed digit is the integer in \(\{-1,0,1\}\) subtracted in the branch expression \(2x-d\); \(D_n=1\) precisely when this integer is zero. All stationarity, covariance, and distribution statements here refer to the joint annealed law of map choices and initial point. Endpoint conventions at the finitely many branch boundaries are immaterial for this absolutely continuous law.

## Proof

**1. Uniform-image branch coding.** Divide the interval into the left half \(L=[-1,0)\) and right half \(R=[0,1]\). Each of the four quarter-intervals has length \(1/2\), and each restriction of either \(T_0\) or \(T_1\) to one of these quarters is affine of slope \(2\), mapping bijectively (up to endpoints) onto either \(L\) or \(R\). Conditional on a half-interval and on any preceding finite branch history, the interval coordinate remains uniform within that half: this holds initially by the stated stationary density and is preserved by each affine quarter-branch. Thus the half-state and zero-digit labels are governed exactly, at every finite length, by the following weighted transitions (rows are source halves, columns are target halves):

\[
M_p(z)=\frac12\begin{pmatrix}1+qz&p\\q&1+pz\end{pmatrix}.
\]

For instance, from \(L\) there is a \(q/2\)-weight zero-digit self-transition and two combined \(1/2\)-weight nonzero-digit self-transitions; the remaining \(p/2\)-weight transition goes to \(R\) and has nonzero digit. The analogous right-side accounting gives the second row. At \(z=1\), the row-stochastic matrix has stationary row vector \(\pi=(q,p)\); hence \(\pi M_p(z)^N\mathbf1\) is the exact finite-length probability-generating polynomial. This argument also independently verifies stationarity of the displayed density.

**2. Spectrum and covariance.** Direct expansion gives

\[
\operatorname{tr}M_p(z)=1+\frac z2,\qquad
\det M_p(z)=\frac{1-h+z+hz^2}{4}.
\]

The quadratic formula gives the stated eigenvalues. Set \(P=M_p(1)\), \(B=M'_p(1)=\operatorname{diag}(q/2,p/2)\), and \(\mathbf1=(1,1)^{\mathsf T}\). The stochastic matrix \(P\) has eigenvalues \(1\) and \(1/2\), with exact decomposition

\[
P^m=\mathbf1\pi+2^{-m}(I-\mathbf1\pi),\qquad m\ge0.
\]

The derivative insertion identity for two marked digits gives, for \(k\ge1\),

\[
\mathbb E[D_0D_k]=\pi B P^{k-1}B\mathbf1.
\]

Subtracting \(\mu^2\) yields \(\operatorname{Cov}(D_0,D_k)=2^{-(k-1)}\pi B(I-\mathbf1\pi)B\mathbf1=2^{-(k-1)}h(1-4h)/4\). At \(p=1/2\), each row sum of \(M_p(z)\) is \((3+z)/4\). More strongly, conditional on **any** observed past digit string, the current hidden-half distribution can be arbitrary but the next digit-zero probability is still \(1/4\), since \(B\mathbf1=(1/4)\mathbf1\) for this parameter. Iterated conditioning proves that the digit indicators are independent Bernoulli \(1/4\), hence their joint generating polynomial factors as \(((3+z)/4)^N\) for every \(N\). Conversely, for any other \(p\in(0,1)\), the one-step covariance is positive, excluding independence.

**3. Exact variance and switching optimum.** Since \(D_0\) is Bernoulli with parameter \(\mu=1/2-h\), its variance is \(1/4-h^2\). Summing the geometric covariances gives

\[
\operatorname{Var}(H_N)=N(1/4-h^2)+\frac{h(1-4h)}2\sum_{k=1}^{N-1}(N-k)2^{-(k-1)}.
\]

The sum equals \(2N-4+2^{2-N}\), yielding the exact finite formula and \(\Gamma=1/4+h-5h^2\). As \(p\) runs over \((0,1)\), the variable \(h=p(1-p)\) ranges over \((0,1/4]\). The quadratic \(1/4+h-5h^2\) is maximized uniquely as a function of \(h\) at \(h=1/10\), with value \(3/10\), and minimized on this range at \(h=1/4\), with value \(3/16\) (its limiting value at \(h=0\) is larger, namely \(1/4\)). Solving \(p(1-p)=1/10\) gives the two displayed maximizing biases.

**4. Central limit theorem and large deviations.** For every real \(t\), the matrix \(M_p(e^t)\) has strictly positive entries and therefore a simple positive Perron eigenvalue \(\lambda_+(e^t)\), strictly larger in modulus than its other eigenvalue. Its Perron projection pairs positively with the positive initial row \(\pi\) and terminal column \(\mathbf1\). Hence the logarithmic moment-generating function per step converges to \(\log\lambda_+(e^t)\). Its analyticity near \(t=0\), together with the spectral gap, yields the centered Gaussian limit by the standard moment-generating-function expansion: \(\Lambda'_p(0)=\mu\), \(\Lambda''_p(0)=\Gamma(p)>0\). The same Perron formula is differentiable for all \(t\in\mathbb R\), and \(H_N/N\in[0,1]\) is exponentially tight. The differentiable logarithmic-moment-generating-function theorem gives the upper bound and the lower bound at all exposed interior frequencies \(0<u<1\). Since \(H_N/N\in[0,1]\) is exponentially tight and the Legendre transform is continuous up to both endpoints (as the explicit Perron eigenvalue asymptotics show), the interior lower bounds also give the full lower bound for open neighborhoods meeting \(0\) or \(1\). Thus the full good large-deviation rate is the displayed Legendre transform. Taking the limits \(t\to-\infty\) and \(t\to+\infty\), respectively, in the displayed eigenvalue gives \(I_p(0)\) and \(I_p(1)\).

## Verification

Run `python3 verify.py` from the directory containing this file. The standalone program uses exact rational arithmetic to propagate the eight actual affine quarter-branches, starting from the specified stationary density, and independently compares the resulting length-\(N\) zero-count distributions with the two-state matrix formula. It also checks exact finite-length means and variances, finite-lag covariances, the balanced Bernoulli law and the sharp rational extremal values. It passed 434 exact checks over seven nontrivial rational switching probabilities with lengths through ten, plus five probabilities with lags through ten. These computations corroborate algebra; the all-\(N\) statements, Gaussian limit and large-deviation principle are justified by the proof above rather than finite testing.

## Relationship to prior work

Dajani, Kalle and Maggioni (2020), equation (11), define this random symmetric doubling family, and their equation (22) already supplies the stationary density and the one-digit zero frequency at \(\alpha=1\). Those are **premises, not claimed contributions**. The present finding concerns joint and finite-length digit-count distributions, the independence transition, covariance decay, sharp variance extrema, and explicit large-deviation rates—none follows from a marginal frequency alone. Dajani and Kalle (2017) study deterministic symmetric doubling maps and digit frequencies; that deterministic work does not imply the biased-random endpoint law. General finite-state transfer-matrix principles are standard, but the exact two-state coding and the resulting sharp parameter statistics are model-specific calculations. No claim of exhaustive historical priority is made.

## Limitations

The theorem is restricted to \(\alpha=1\), \(0<p<1\), and stationary annealed sampling. It does not classify fluctuations for other \(\alpha\), nonstationary initial distributions, fixed (quenched) map-selection paths, or all signed-digit observables. General transfer-matrix and large-deviation methods are established mathematics; the potential novelty is the explicit model-specific coding and formulas, not these general theorems. An equivalent earlier analysis in unindexed literature remains possible. No independent mathematical audit is asserted.

## References

1. K. Dajani, C. Kalle, M. Maggioni, *Matching for random systems with an application to minimal weight expansions*, arXiv:2008.04398, initially public 10 August 2020, especially equations (11), (22), Theorem 3.12 and Section 4. https://arxiv.org/abs/2008.04398
2. K. Dajani, C. Kalle, *Invariant measures, matching and the frequency of 0 for signed binary expansions*, arXiv:1703.06335, initially public 18 March 2017, especially the deterministic family and its digit-frequency analysis. https://arxiv.org/abs/1703.06335
