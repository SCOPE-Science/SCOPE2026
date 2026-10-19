# A sharp one-eighth switching threshold for four-phase temporal asymmetry in skew tent dynamics

## Finding

For every \(0<\delta<1\) and \(0<p<1\), consider a stationary symmetric two-state Markov chain \((S_j)_{j\ge0}\) on \(\{-1,+1\}\), with probability \(p\) of keeping its current sign at each step. Independently initialize \(X_0\) uniformly on \([0,1]\), and set
\[
 X_{j+1}=T_{a_{S_j}}(X_j),\qquad
 a_s=\frac{1+s\delta}{2},\qquad
 T_a(x)=\begin{cases}x/a,&0\le x\le a,\\(1-x)/(1-a),&a<x\le1.\end{cases}
\]
Each \(X_j\) remains uniform. Write \(Y_j=X_j-1/2\). Define the directional third moment
\[
 \Delta_n=\mathbb E[Y_0^2Y_n]-\mathbb E[Y_0Y_n^2],\qquad n\ge1.
\]
Set \(d=\delta^2\), \(b=(1+3d)/4\), and \(z=d(2p-1)\). Then for **every** integer \(n\ge1\),
\[
\boxed{\displaystyle
 \Delta_n=-\frac{1-d}{48}\sum_{j=0}^{\lfloor(n-1)/2\rfloor}b^{n-1-2j}z^j,
 \qquad \mathbb E[Y_0Y_n^2]=0.}
\]
Its rational generating function is
\[
 \boxed{\displaystyle \sum_{n\ge1}\Delta_n v^n
 =-\frac{(1-d)v}{48(1-bv)(1-zv^2)}.}
\]
There is a **complete, sharp sign classification**:

- If \(z>-b^2\), every \(\Delta_n<0\).
- If \(z=-b^2\), then \(\Delta_n=0\) precisely for \(n\equiv0,3\pmod4\); all remaining values are negative.
- If \(z<-b^2\), then \(\Delta_n>0\) precisely for \(n\equiv0,3\pmod4\), and \(\Delta_n<0\) for \(n\equiv1,2\pmod4\).

In particular, a positive directional third moment occurs for some lag **if and only if** \(p<1/8\) and
\[
 d_- (p)<\delta^2<d_+(p),\qquad
 d_\pm(p)=\frac{10-32p\pm\sqrt{(10-32p)^2-36}}{18}.
\]
At the **unique onset point** \(p=1/8\), \(\delta^2=1/3\), all lags congruent to \(0\) or \(3\) modulo \(4\) have zero directional moment, while every other lag is negative. These are exact statements for all lags, not asymptotic approximations.

The autocovariance has the simultaneous exact law
\[
 \mathbb E[Y_0Y_n]=\begin{cases}0,&n\text{ odd},\\z^{n/2}/12,&n\text{ even}\end{cases}\quad(n\ge0).
\]
The environment Markov chain is itself time-reversible. Yet \(\Delta_1=-(1-d)/48<0\) for every interior parameter, so the stationary observed process is never time-reversible. The phase transition describes the *sign* of its higher-lag asymmetry, not an onset of irreversibility.

## Assumptions and scope

The maps are the full-branch continuous skew tent maps above, with the standard choice of branch endpoint irrelevant to the uniform law. The environment is **stationary**, symmetric and independent of the initial uniform spatial state, with exactly the two complementary turning points \(a_+=(1+\delta)/2\), \(a_-=(1-\delta)/2\) and the same stay probability in each environmental state. The intervals \(0<\delta,p<1\) exclude degenerate branch and deterministic-switching endpoints. Expectations average over both the environment and the initial spatial state. The directional moment concerns the real amplitude observable \(Y=x-1/2\), not a binary threshold or the switching labels alone.

## Proof

**1. Common invariant probability and polynomial transfer.** For every \(a\in(0,1)\), both branches cover \([0,1]\), and the Frobenius--Perron operator acting on densities is
\[
 (\mathcal P_a h)(x)=a h(ax)+(1-a)h(1-(1-a)x).
\]
It preserves the constant density \(1\). Consequently the conditional spatial law at every time, even given the full environmental trajectory up to that time, is uniform; the joint law of spatial position and current environment is stationary. For \(Y(x)=x-1/2\) and \(H(x)=Y(x)^2-1/12\), direct polynomial expansion gives
\[
 \mathcal P_aY=(2a-1)Y,\qquad
 \mathcal P_aH=\bigl(1-3a(1-a)\bigr)H-a(1-a)Y.
\]
For the two chosen turning points, these identities reduce to
\[
 \mathcal P_{a_s}Y=s\delta Y,\qquad
 \mathcal P_{a_s}H=bH+cY,\qquad
 c=-\frac{1-d}{4},
\]
where \(b,c\) are independent of the sign \(s\).

**2. Exact two-time third moments.** Conditional on an environmental word \(s_0,\ldots,s_{n-1}\), the coefficient of \(Y\) in \(\mathcal P_{a_{s_{n-1}}}\cdots\mathcal P_{a_{s_0}}H\) is
\[
 c\sum_{k=0}^{n-1}b^{n-1-k}\prod_{j=n-k}^{n-1}(s_j\delta),
\]
with an empty product equal to one. Since \(\int_0^1Y^2\,dx=1/12\), this coefficient divided by \(12\) is \(\mathbb E[Y_0^2Y_n\mid s_0,\ldots,s_{n-1}]\). On the other hand, \(\mathcal P_{a_{s_{n-1}}}\cdots\mathcal P_{a_{s_0}}Y\) is a scalar multiple of \(Y\); using \(\int_0^1Y^3\,dx=0\) gives \(\mathbb E[Y_0Y_n^2\mid s_0,\ldots,s_{n-1}]=0\).

**3. Environmental products and the closed law.** Put \(U_j=S_jS_{j+1}\). The variables \((U_j)_{j\ge0}\) are independent, with \(\mathbb E U_j=2p-1\), and independent of the uniform initial sign \(S_0\). For any consecutive block of \(k\) environmental signs, the product has expectation \(0\) if \(k\) is odd, and \((2p-1)^{k/2}\) if \(k\) is even. Thus a product of \(k\) consecutive factors \(S_j\delta\) has mean \(0\) for odd \(k\) and \(z^{k/2}\) for even \(k\). Averaging the formula in step 2 proves the displayed exact \(\Delta_n\), and multiplying the two geometric-series generating functions gives the rational generating function. Applying the same product identity to \(\mathcal P_{a_s}Y\) proves the stated covariance law.

**4. Exact sign phase and sharp envelope.** For every integer \(\ell\ge0\), set
\[
 Q_\ell=\sum_{j=0}^{\ell}b^{2(\ell-j)}z^j.
\]
Then \(\Delta_{2\ell+1}=-(1-d)Q_\ell/48\) and \(\Delta_{2\ell+2}=b\Delta_{2\ell+1}\). For \(z\ne b^2\),
\[
 Q_\ell=\frac{b^{2\ell+2}-z^{\ell+1}}{b^2-z};
\]
when \(z=b^2\), the continuous value is \((\ell+1)b^{2\ell}\). Because \(b>0\), this expression is positive for every \(\ell\) when \(z>-b^2\). At \(z=-b^2\) it vanishes exactly when \(\ell\) is odd. If \(z<-b^2\), it is negative precisely when \(\ell\) is odd and positive when \(\ell\) is even, proving the complete residue-class sign classification.

The strict sign-reversal region \(z<-b^2\) is exactly
\[
 9d^2-(10-32p)d+1<0.
\]
Since \(0<d<1\), this quadratic is negative somewhere exactly when its vertex lies at positive \(d\) and \((10-32p)^2>36\), equivalently \(p<1/8\). Its positive roots are exactly \(d_\pm(p)\) above. The discriminant vanishes in the admissible parameter range precisely at \(p=1/8,d=1/3\), establishing the unique critical onset and equality case.

## Verification

The accompanying standalone `verify.py` uses exact rational arithmetic. It independently enumerates every environmental word and every affine inverse-branch cylinder, integrates both directed cubic expressions over the actual cylinder geometry, and compares the results with the theorem. It does **not** use the transfer-operator recurrence to construct these independent integrals. The executable check returned:

`VERIFY_OK 40 exact independent cylinder comparisons; 6 boundary and sign identities`

Those comparisons include lengths through eight, parameters on either side of the sign boundary, and a rational exact boundary at \(\delta=1/2,p=15/128\). The algebraic identity and all-lag assertions are established by the four-step proof; the finite calculation is corroboration only.

## Relationship to prior work

Tefas and collaborators (2003) developed exact first-, second- and third-order correlations for a **single deterministic** skew tent transformation, including their transfer-operator representation (Appendix A, especially equations (A-12)--(A-14)). Those identities and the underlying polynomial-transfer method are prior mathematics. Bahsoun, Bose and Duan (2013) developed the correlation theory for **independently randomly composed intermittent interval maps**; their main theorem concerns polynomial mixing rates of a different family. Porfiri and Belykh (2017) analyzed **Markov-switching synchronization of coupled tent maps**, with mean-square synchronization rather than this stationary amplitude-reversal statistic. General Markov-switching moment methods also predate these works. The claim here is the evaluated two-parameter, all-lag directional-moment law and the sharp \(p=1/8\) four-phase sign threshold for complementary full-branch maps under persistent switching, not the general existence of a transfer method or of third-order correlations in the deterministic case.

## Limitations

The theorem does not cover noncomplementary turning points, nonsymmetric environmental transitions, parameter-dependent spatial reinjection, or other observables. It is an exact annealed statement, not a quenched pathwise sign theorem. The phase classification describes the sign of one natural antisymmetric third-order observable, not a complete classification of the stationary process or a claim that all other definitions of irreversibility have the same phase diagram. The mathematical methods are standard in part; the exact sharp phase diagram is the contribution. An inaccessible or previously unindexed specialization of general switching-process moment theory remains a historical-priority risk. No independent external validation is asserted.

## References

1. A. Tefas, A. Nikolaidis, N. Nikolaidis, V. Solachidis, S. Tsekeridou and I. Pitas, *Performance analysis of correlation-based watermarking schemes employing Markov chaotic sequences*, IEEE Transactions on Signal Processing **51** (2003), 1979–1994, DOI: 10.1109/TSP.2003.811245. Author-uploaded full text, Appendix A: https://www.researchgate.net/publication/3318629_Performance_analysis_of_correlation-based_watermarking_schemes_employing_Markov_chaotic_sequences.
2. W. Bahsoun, C. Bose and Y. Duan, *Decay of correlation for random intermittent maps*, arXiv:1305.6588, first publicly submitted 2013-05-28; https://arxiv.org/abs/1305.6588.
3. B. Cloez and M. Hairer, *Exponential ergodicity for Markov processes with random switching*, arXiv:1303.6999, first publicly submitted 2013-03-27; https://arxiv.org/abs/1303.6999.
4. M. Porfiri and I. Belykh, *Memory matters in synchronization of stochastically coupled maps*, SIAM Journal on Applied Dynamical Systems **16** (2017), 1372–1396, DOI: 10.1137/17M111136X.
5. A. Timmermann, *Moments of Markov switching models*, Financial Markets Group Discussion Paper 323 (1999), later Journal of Econometrics **96** (2000), 75–111; https://www.fmg.ac.uk/publications/discussion-papers/moments-markov-switching-models.
