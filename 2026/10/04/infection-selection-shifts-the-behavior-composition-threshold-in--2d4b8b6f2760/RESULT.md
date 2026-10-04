# Infection selection shifts the behavior-composition threshold in a two-attitude epidemic model
## Finding
Consider the two-attitude disease–opinion system of Tyson, Marshall, and Baumgaertner, with prophylactic and non-prophylactic susceptible classes \(S_p\) and \(S_n\), infection rates \(\beta_p<\beta_n\), infectious prevalence \(I\), and opinion-transfer difference \(\Delta\omega(I)=\omega_p(I)-\omega_n(I)\). Define the total susceptible fraction and the prophylactic share of that susceptible pool by
\[
S=S_p+S_n,\qquad p=\frac{S_p}{S},\qquad S>0.
\]
Then the coupled model has the exact composition law
\[
\dot p=p(1-p)\left[(\beta_n-\beta_p)I+S\Delta\omega(I)\right].
\]
Equivalently, whenever \(S_p,S_n>0\),
\[
\frac{d}{dt}\log\frac{S_p}{S_n}
=(\beta_n-\beta_p)I+S\Delta\omega(I).
\]
The first term is an infection-selection term: non-prophylactic susceptibles are removed by infection faster than prophylactic susceptibles. It changes the composition of the remaining susceptible pool even if there is no net opinion transfer.

For the influence functions in the source,
\[
\Delta\omega(I)=\frac{2\omega_0 I}{k+I}-c,
\]
and the paper's threshold is
\[
I_{\mathrm{cross}}=\frac{ck}{2\omega_0-c}.
\]
That threshold is exactly where the **opinion-transfer term** changes sign. It is not the threshold for the direction of change of the susceptible composition \(p\). Let \(\delta=\beta_n-\beta_p>0\). Multiplying the sign condition for \(\dot p\) by \(k+I>0\) gives the quadratic
\[
F_S(I)=\delta I^2+\left[\delta k+S(2\omega_0-c)\right]I-Sck.
\]
Its unique positive root is
\[
I_{\mathrm{comp}}(S)=
\frac{-A+\sqrt{A^2+4\delta Sck}}{2\delta},
\qquad
A=\delta k+S(2\omega_0-c).
\]
Moreover,
\[
0<I_{\mathrm{comp}}(S)<I_{\mathrm{cross}}.
\]
Hence there is always a nonempty interval \(I_{\mathrm{comp}}(S)<I<I_{\mathrm{cross}}\) in which \(\Delta\omega(I)<0\), so opinion transfer favors non-prophylaxis, but \(\dot p>0\), so the prophylactic **share of the remaining susceptibles increases** because differential infection more than offsets that opinion flow.

With the source's default values \(\beta_n=3/20\), \(\beta_p=3/40\), \(\omega_0=1/10\), \(c=1/100\), and \(k=1/10\), take the admissible simplex state
\[
S=\frac1{10},\qquad p=\frac12,\qquad I=\frac1{250},\qquad R=1-S-I.
\]
Then \(I<I_{\mathrm{cross}}=1/190\) and
\[
\Delta\omega(I)=-\frac3{1300}<0,
\qquad
\dot p=\frac9{520000}>0.
\]
Thus the separation between the opinion-transfer threshold and the composition threshold occurs already with the paper's default model parameters.

## Assumptions and scope
The result concerns equations (2.1)–(2.5) of the cited two-attitude model. It assumes \(S>0\), \(\beta_n>\beta_p\), \(c>0\), \(k>0\), and \(2\omega_0-c>0\); the paper's restriction \(c\leq\omega_0\) implies the last inequality. The log-odds form additionally assumes \(S_p,S_n>0\). The claim distinguishes the direction of change of the **fraction** \(p=S_p/(S_p+S_n)\) from the direction of the explicit opinion-transfer flux. It does not assert that the absolute number \(S_p\) increases on the same interval, nor that every state in the interval lies on the particular numerical trajectories plotted in the paper.

## Proof
From the published equations,
\[
\dot S_p=-\beta_p I S_p+\Delta\omega(I)S_pS_n,
\]
\[
\dot S_n=-\beta_n I S_n-\Delta\omega(I)S_pS_n.
\]
Therefore
\[
\dot S=-I(\beta_pS_p+\beta_nS_n).
\]
Writing \(S_p=pS\) and \(S_n=(1-p)S\), the quotient rule gives
\[
\dot p=\frac{\dot S_pS-S_p\dot S}{S^2}
=p(1-p)\left[(\beta_n-\beta_p)I+S\Delta\omega(I)\right].
\]
Dividing by \(p(1-p)\) gives the log-odds identity.

For \(\Delta\omega(I)=2\omega_0 I/(k+I)-c\), the sign of the bracket in the composition law is the sign of
\[
F_S(I)=\delta I^2+[\delta k+S(2\omega_0-c)]I-Sck,
\qquad \delta=\beta_n-\beta_p>0.
\]
Here \(F_S(0)=-Sck<0\), while the coefficient of \(I\) and the leading coefficient are positive. Thus \(F_S\) is strictly increasing for \(I\geq0\) and has exactly one positive root, the displayed \(I_{\mathrm{comp}}(S)\).

At the paper's opinion threshold, \(\Delta\omega(I_{\mathrm{cross}})=0\). Hence the composition bracket equals \(\delta I_{\mathrm{cross}}>0\), so \(F_S(I_{\mathrm{cross}})>0\). Since \(F_S(0)<0\) and \(F_S\) is strictly increasing, its unique positive root satisfies \(0<I_{\mathrm{comp}}(S)<I_{\mathrm{cross}}\).

For the exact default-parameter witness, \(\Delta\omega(1/250)=1/130-1/100=-3/1300\), while
\[
(\beta_n-\beta_p)I+S\Delta\omega
=\frac3{10000}-\frac3{13000}
=\frac9{130000}>0.
\]
Multiplying by \(p(1-p)=1/4\) gives \(\dot p=9/520000>0\).

## Verification
The accompanying `verify.py` uses exact rational arithmetic to replay the default-parameter witness, the identity between the quotient-rule expression and the closed composition law on several rational states, and the sign tests \(F_S(0)<0<F_S(I_{\mathrm{cross}})\). The universal result is established by the algebraic proof above; the finite replay checks transcription and arithmetic.

## Relationship to prior work
The 2022 source introduces the two-attitude model, the differential infection rates, the influence functions, and \(I_{\mathrm{cross}}\) as the point where \(\omega_p-\omega_n\) changes sign. The paper describes that threshold as the level at which net opinion adoption favors prophylaxis. The earlier four-attitude model by Tyson et al. explicitly notes that the disease preferentially infects less-prophylactic classes, so the qualitative selection mechanism is recognized in that predecessor. However, the inspected sources do not state the two-attitude log-odds identity, the exact state-dependent composition threshold, or the strict inequality \(I_{\mathrm{comp}}(S)<I_{\mathrm{cross}}\).

This finding therefore does not claim that preferential infection is a new biological idea. Its contribution is the exact decomposition of behavioral-composition change in the published two-attitude equations and the resulting correction to how the fixed \(I_{\mathrm{cross}}\) threshold should be interpreted when discussing the composition of the susceptible pool.

## Limitations
The result is local in state space and structural; it does not by itself alter the paper's numerical wave counts, final-size curves, or public-health conclusions. The explicit witness is an admissible state of the model, not a claim that the paper's default initial condition necessarily passes through that state. Literature searches cannot establish absolute novelty, and a mathematically equivalent identity could exist under different terminology outside the indexed sources.

## References
1. R. C. Tyson, N. D. Marshall, and B. O. Baumgaertner, “Transient prophylaxis and multiple epidemic waves,” *AIMS Mathematics* 7(4), 5616–5633 (2022), DOI 10.3934/math.2022311.
2. R. C. Tyson, S. D. Hamilton, A. S. Lo, B. O. Baumgaertner, and S. M. Krone, “The Timing and Nature of Behavioural Responses Affect the Course of an Epidemic,” *Bulletin of Mathematical Biology* 82, 14 (2020), DOI 10.1007/s11538-019-00684-z.
