# One-state detection and exact sign-count dichotomy in irreversible three-state cycles

## Finding

Consider a stationary, homogeneous-in-time, irreducible continuous-time Markov process on the three states \(0,1,2\), making **only** the directed transitions \(0\to1\to2\to0\), with respective positive rates \(a,b,c\). For every state \(i\), let \(I_i(t)=\mathbf 1_{\{X_t=i\}}\) and
\[
 C_i(t)=\operatorname{Cov}(I_i(0),I_i(t)),\qquad t\ge0.
\]
Write
\[
 \sigma=a+b+c,\qquad q=ab+bc+ca,\qquad \Delta=\sigma^2-4q.
\]
Then the **complete state-by-state classification of sign changes** is as follows.

1. If \(\Delta<0\), each of the three autocovariances has infinitely many simple positive-time zeros and alternating positive and negative intervals. Each state separately detects negative lag covariance.
2. If \(\Delta\ge0\), there is a unique rate at least as large as the sum of the other two plus twice their geometric mean. For the corresponding fastest-exit state, the autocovariance crosses zero **exactly once** and is strictly negative at all later finite times. The other two indicator autocovariances are strictly positive for every finite \(t\ge0\).

Consequently **for every positive triple of directed rates, at least one directly observable binary state indicator has negative stationary autocovariance at some positive lag**. Three states are minimal for this phenomenon among irreducible continuous-time Markov chains, because every two-state chain is reversible and its indicator autocovariances are positive exponentials.

The unique zero in the real-spectrum regime is also explicit. If \(i_*\) has the unique largest exit rate, define
\[
 h=\frac{\sigma}{2},\qquad d=\frac{\sqrt\Delta}{2},\qquad
 r_{i_*}=a_{i_*}+\frac{a_j a_k}{a_j+a_k},
\]
where \((i_*,j,k)\) is any ordering of the three states and \(a_0=a,a_1=b,a_2=c\). When \(\Delta>0\),
\[
 t_*=\frac{1}{2d}\log\!\left(\frac{r_{i_*}-h+d}{r_{i_*}-h-d}\right);
\]
when \(\Delta=0\), \(t_*=(r_{i_*}-h)^{-1}\). All denominators and logarithm arguments here are strictly admissible.

## Assumptions and scope

Time is measured in reciprocal-rate units. The process starts in its **unique stationary law**, has exponentially distributed holding times, has no backwards transitions, and all \(a,b,c\) are strictly positive and finite. The covariance is the ordinary, **centered**, real, stationary two-time covariance; it is not a spectral density, a nonstationary overshoot of an arbitrarily prepared distribution, or a sample-path correlation. Zero means finite positive time, excluding the limit \(t\to\infty\) where every covariance tends to zero.

The row generator is
\[
 Q=\begin{pmatrix}-a&a&0\\0&-b&b\\c&0&-c\end{pmatrix}.
\]
For \(i=0,1,2\), with the other two rates \(y,z\), the stationary weight and initial covariance are
\[
 \pi_i=\frac{1/a_i}{1/a+1/b+1/c},\qquad C_i(0)=\pi_i(1-\pi_i)>0.
\]

## Proof

**1. Exact normalized correlation.** Stationarity gives
\[
 C_i(t)=\pi_i\bigl((e^{tQ})_{ii}-\pi_i\bigr).
\]
The characteristic polynomial is \(\lambda(\lambda^2+\sigma\lambda+q)\). The stationary projector subtracts the simple zero eigenvalue, so the normalized correlation \(f_i(t)=C_i(t)/C_i(0)\) satisfies
\[
 f_i''+\sigma f_i'+q f_i=0,\qquad f_i(0)=1,
 \qquad f_i'(0)=-r_i,
 \quad r_i=a_i+\frac{yz}{y+z}.
\]
Indeed \(f_i'(0)=Q_{ii}/(1-\pi_i)=-a_i/(1-\pi_i)\) and \(1-\pi_i=a_i(y+z)/q\), yielding the stated \(r_i\). No reversibility or diagonalizability is assumed.

Set \(h=\sigma/2\). If \(\Delta<0\), with \(\omega=\sqrt{-\Delta}/2>0\), the unique solution is
\[
 f_i(t)=e^{-ht}\left[\cos(\omega t)
 +\frac{h-r_i}{\omega}\sin(\omega t)\right].
\]
The bracket is a nonzero phase-shifted sinusoid because its cosine coefficient is \(1\). Thus every positive-time zero is simple, infinitely many occur, and signs alternate. In fact the first is
\[
 \frac{\pi/2+\arctan((h-r_i)/\omega)}{\omega}>0,
\]
with all succeeding zeros spaced by \(\pi/\omega\).

**2. Exact rate-dominance criterion.** Suppose \(\Delta\ge0\), and relabel so that \(a=\max(a,b,c)\). Then
\[
 \Delta=(a-b-c)^2-4bc.
\]
Because \(a\ge\max(b,c)>(\sqrt b-\sqrt c)^2\) for strictly positive \(b,c\), the lower branch \(a\le b+c-2\sqrt{bc}\) is impossible. Hence
\[
 a\ge b+c+2\sqrt{bc}.
\]
In particular \(a\) is the unique fastest rate. Conversely that inequality implies \(\Delta\ge0\), proving the complete equivalence.

**3. Signs in the real-spectrum regime.** Put \(d=\sqrt\Delta/2\), and \(\gamma_{\pm}=h\pm d\), with \(0<\gamma_-\le\gamma_+\). For \(\Delta>0\),
\[
 f_i(t)=e^{-ht}\left[\cosh(dt)+\frac{h-r_i}{d}\sinh(dt)\right].
\]
From the strict inequalities \(\sqrt\Delta<a-b-c\) (since \(bc>0\)) one obtains
\[
 \gamma_+<a,\qquad \gamma_->b+c.
\]
For the fastest state \(0\), \(r_0=a+bc/(b+c)>a>\gamma_+\); therefore the coefficient of the slower exponential \(e^{-\gamma_-t}\) is strictly negative, while the faster coefficient is positive. Their sum is \(1\) at \(t=0\), so there is exactly one positive zero. Solving gives the displayed \(t_*\), and the normalized correlation is negative thereafter. For state \(1\),
\[
 r_1=b+\frac{ac}{a+c}<b+c<\gamma_-;
\]
likewise \(r_2=c+ab/(a+b)<b+c<\gamma_-\). Thus \(h-r_1>d\) and \(h-r_2>d\), so their hyperbolic brackets are strictly positive at every \(t\ge0\).

At the repeated-root boundary \(\Delta=0\), the exact formula is
\[
 f_i(t)=e^{-ht}\bigl[1+(h-r_i)t\bigr].
\]
The same dominance ordering yields \(r_0>a>h\) and \(r_1,r_2<b+c<h\). Therefore precisely the fastest state's normalized covariance changes sign, once, at \((r_0-h)^{-1}\), and the other two remain positive. All cases and their boundaries are included.

**4. Minimality.** An irreducible two-state continuous-time Markov chain with rates \(u,v>0\) has generator eigenvalues \(0,-(u+v)\) and stationary indicator covariance \(\pi_i(1-\pi_i)e^{-(u+v)t}>0\). One state has no nonconstant centered indicator. Thus the three-state directed cycle is the smallest Markov environment with a negative individual-state stationary autocovariance.

## Verification

Run `python3 check_threecycle.py` in the same directory. This standard-library-only checker forms transition probabilities independently by Poisson uniformization of the original generator, and compares them against the derived normalized formulas for all three indicators across 900 rate triples and five times (13,500 direct comparisons, plus branch checks). The packaged run passed 13,747 assertions, with maximum absolute discrepancy about \(5.09\times10^{-15}\). The checks include a repeated-eigenvalue boundary and near-boundary regimes. These finite tests are numerical corroboration; the all-rate conclusions come solely from the proof above.

Two exact examples demonstrate distinct branches. For \(a=b=c=1\), every \(\pi_i=1/3\), and
\[
 f_i(t)=e^{-3t/2}\cos\!\left(\frac{\sqrt3}{2}t\right),
\]
whose first zero is \(\pi/\sqrt3\), followed by infinitely many. For \((a,b,c)=(4,1,1)\), \(\Delta=0\), and
\[
 f_0(t)=e^{-3t}(1-3t/2),\qquad
 f_1(t)=f_2(t)=e^{-3t}(1+6t/5).
\]
Only the fastest state crosses zero, precisely at \(t=2/3\).

## Relationship to prior work

Prager, Naundorf and Schimansky-Geier (2002) treated Poisson three-state cycles and derived a renewal-based output power spectrum for a specified indicator, an essential basis for the present model. Chen (2009) proved a broader **existence** distinction between negative autocorrelations in irreversible finite-state chains and positive correlations under detailed balance. Kuang and Chen (2010) supplied general three-state autocorrelation and spectral formulae, and Jia, Qian and Jiang (2014) classified simple versus oscillatory overshoots for three-state kinetic populations.

The claimed additional assertion is not the Markov eigenvalue formula, the possibility of overshoot, or the generic distinction between reversibility and irreversibility. It is the complete **all-positive-rate, all-three-indicator, exact sign-count selection theorem** for the natural directed cycle: in the real-eigenvalue region precisely the fastest-exit indicator crosses, while in the complex region all indicators oscillate, including the repeated-root boundary and explicit crossing times. The closely related 2010 full text was not obtainable during the comparison; priority should be independently checked against it and other historical sources.

## Limitations

The result is restricted to directed three-cycles with only clockwise Poisson jumps. Allowing backward rates, additional edges or more states may invalidate the guaranteed single-indicator detection and the zero-count dichotomy. It does not assert that all irreversible finite-state processes admit a negative state-indicator autocovariance. A negative lag covariance is not a negative probability, and its absence in a selected observable does not establish detailed balance. Earlier broad spectral or overshoot formulae may encode the specialization algebraically even without presenting this classification; historical originality therefore remains provisional pending independent audit and fuller source access.

## References

1. T. Prager, B. Naundorf, and L. Schimansky-Geier, *Coupled three-state oscillators*, arXiv:cond-mat/0211285, first posted 2002-11-14. https://arxiv.org/abs/cond-mat/0211285
2. Y. Chen, *On the Monotonicity of Autocorrelation Function for Finite State Markov Processes*, Acta Scientiarum Naturalium Universitatis Pekinensis 45 (2009), 11 ff. https://xbna.pku.edu.cn/EN/Y2009/V45/I1/11
3. N. Kuang and Y. Chen, *On the fluctuation spectra with respect to complex functions of the three-state Markov processes*, Journal of East China Normal University (Natural Science) 2010 (3), 134–142. https://xblk.ecnu.edu.cn/CN/abstract/abstract24473.shtml
4. C. Jia, M.-P. Qian, and D.-Q. Jiang, *Overshoot in biological systems modelled by Markov chains: a non-equilibrium dynamic phenomenon*, IET Systems Biology 8 (2014), 138–145. https://doi.org/10.1049/iet-syb.2013.0050
