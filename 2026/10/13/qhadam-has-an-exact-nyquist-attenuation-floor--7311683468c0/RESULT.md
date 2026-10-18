# QHAdam has an exact Nyquist attenuation floor

## Finding
Consider the scalar, bias-corrected quasi-hyperbolic Adam (QHAdam) rule with zero initial moments,
\[
 m_t=\beta_1m_{t-1}+(1-\beta_1)g_t,\qquad
 \widehat m_t=m_t/(1-\beta_1^t),
\]
\[
 v_t=\beta_2v_{t-1}+(1-\beta_2)g_t^2,\qquad
 \widehat v_t=v_t/(1-\beta_2^t),
\]
\[
 \Delta\theta_t=-\alpha\,
 \frac{(1-\nu_1)g_t+\nu_1\widehat m_t}
 {\sqrt{(1-\nu_2)g_t^2+\nu_2\widehat v_t}+\varepsilon}.
\]
Assume \(0\le\beta_1,\beta_2<1\), \(0\le\nu_1,\nu_2\le1\), \(\alpha>0\), \(\varepsilon\ge0\), and a constant-magnitude alternating input \(g_t=(-1)^{t-1}G\), \(G\ne0\).

Then \(\widehat v_t=G^2\) exactly for every \(t\), so the entire denominator is \(|G|+\varepsilon\), regardless of \(\nu_2\) and \(\beta_2\). Put \(a=(1-\beta_1)/(1+\beta_1)\). The first moment obeys the exact parity law
\[
 \frac{\widehat m_t}{g_t}=a\frac{1-(-\beta_1)^t}{1-\beta_1^t}
 =\begin{cases}
 a,&t\text{ even},\\[2pt]
 a(1+\beta_1^t)/(1-\beta_1^t),&t\text{ odd}.
 \end{cases}
\]
Consequently the first-step update magnitude is \(\alpha|G|/(|G|+\varepsilon)\), every even step already has the limiting attenuation factor, and the odd-step factors decrease *weakly* to it:
\[
 |\Delta\theta_t|=\alpha\frac{|G|}{|G|+\varepsilon}
 \left[(1-\nu_1)+\nu_1\frac{\widehat m_t}{g_t}\right],
\qquad
 q_\infty=1-\frac{2\nu_1\beta_1}{1+\beta_1}.
\]
For each fixed \(\nu_1\in[0,1]\), \(q_\infty\) is nonincreasing in \(\beta_1\), and it is **strictly decreasing if and only if** \(\nu_1>0\). For \(\nu_1=0\), it is identically one. In all cases,
\[
 \boxed{\inf_{0\le\beta_1<1}q_\infty=1-\nu_1}.
\]
Thus, whenever \(\nu_1<1\), QHAdam retains a guaranteed nonzero fraction of the current alternating gradient, whereas the Adam-numerator choice \(\nu_1=1\) has a factor approaching zero as \(\beta_1\uparrow1\). At the paper's WMT16 setting \((\nu_1,\beta_1,\nu_2,\beta_2)=(0.8,0.95,0.7,0.98)\), the limiting factor is \(0.220512820512\ldots\).

## Assumptions and scope
The result concerns precisely the displayed bias-corrected source recurrence, without extra clipping, decay, or other update modifications. The gradient is a prescribed signal; it need not be the gradient sequence along any fixed objective. Its constant squared magnitude is essential for the exact disappearance of second-moment parameters. The immediate discounts are restricted to the natural interpolation interval \([0,1]\), even though the defining paper discusses wider conventions. The parameter \(\beta_1=1\) is excluded; the infimum at this boundary need not be attained. No general optimization convergence conclusion follows.

## Proof
Unrolling the geometric first-moment recurrence, for every \(t\ge1\),
\[
 m_t=(1-\beta_1)\sum_{j=1}^{t}\beta_1^{t-j}(-1)^{j-1}G
 =(-1)^{t-1}G\frac{1-\beta_1}{1+\beta_1}[1-(-\beta_1)^t].
\]
Divide by \((1-\beta_1^t)g_t\) to obtain the stated ratio and parity decomposition. When \(\beta_1=0\), both parity ratios are one; otherwise odd powers \(\beta_1^t\) strictly decrease with odd \(t\), while \(x\mapsto(1+x)/(1-x)\) increases for \(0\le x<1\). Mixing with \((1-\nu_1)g_t\) gives the scalar attenuation \(q_t=(1-\nu_1)+\nu_1\widehat m_t/g_t\). Hence \(q_t\ge q_\infty>0\) for every finite \(t\). Every even \(t\) has \(q_t=q_\infty\); odd factors approach that value from above, with equality identically in degenerate cases \(\nu_1=0\) or \(\beta_1=0\).

For the second moment, the constant squared input implies
\[
 v_t=(1-\beta_2)G^2\sum_{j=0}^{t-1}\beta_2^j
 =G^2(1-\beta_2^t),\qquad\widehat v_t=G^2.
\]
Thus \((1-\nu_2)g_t^2+\nu_2\widehat v_t=G^2\), and the claimed exact update magnitude follows. Finally,
\[
 \frac{\partial q_\infty}{\partial\beta_1}
 =-\frac{2\nu_1}{(1+\beta_1)^2}\le0,
\]
with strict inequality exactly for \(\nu_1>0\). Taking \(\beta_1\uparrow1\) proves the sharp floor including both endpoint cases \(\nu_1=0,1\). The WMT16 value is direct substitution.

## Verification
The source-package checker `verify.py` directly replays the two moment recurrences for alternating gradients, checking the exact parity ratio, denominator cancellation, attenuation factor, boundary behavior, and WMT16 number. Independent spot checks can substitute these parameters into the closed formulas for any positive integer \(t\). Such checks corroborate transcription; the finite geometric sums above prove the all-time identities and the sharp global floor.

## Relationship to prior work
Jerry Ma and Denis Yarats, *Quasi-hyperbolic momentum and Adam for deep learning* (arXiv:1810.06801v1; ICLR 2019), define the QHAdam update and motivate immediate-gradient discounts as protection against stale first-moment information. The defining paper analyzes worst-case update bounds and empirical parameter choices, including its WMT16 setting. Those statements do not themselves give the alternating-input parity identity, the exact disappearance of both second-moment hyperparameters at every time, or the sharp Nyquist attenuation floor. The present result is an elementary, input-specific frequency-response diagnostic built from that published recurrence; its contribution is the joint exact parameter dependence, not the invention of immediate discounting or a general convergence guarantee.

## Limitations
A real Nyquist alternating gradient is a special, externally prescribed input, not a model of general stochastic optimization. Any departure from constant squared magnitude typically restores dependence on \(\beta_2\) and \(\nu_2\). The attenuation floor concerns the scalar QHAdam update and does not imply a universal performance improvement. Equivalent input-response calculations may exist in technical notes outside the inspected literature.

## Reference
Ma, Jerry, and Denis Yarats. *Quasi-hyperbolic momentum and Adam for deep learning*. arXiv:1810.06801v1 (2018), ICLR 2019.
