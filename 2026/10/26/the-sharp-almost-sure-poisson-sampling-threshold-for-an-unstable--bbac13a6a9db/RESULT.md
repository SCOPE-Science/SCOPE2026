# The sharp almost-sure Poisson sampling threshold for an unstable scalar plant

## Finding

Consider the unstable scalar plant with zero-order-held sampled-state feedback
\[
\dot x(t)=a x(t)-k x(T_n),\quad T_n\le t<T_{n+1},
\]
where \(a>0\), \(k\in\mathbb R\), \(x(0)\ne0\), \(T_0=0\), and the independent intersample times \(T_{n+1}-T_n\) are exponential with intensity \(\lambda>0\). There exists a **fixed real feedback gain** rendering the entire continuous-time trajectory almost surely exponentially stable **if and only if**
\[
\boxed{\lambda>a/2.}
\]
Precisely, for every gain, the almost-sure physical-time **upper** logarithmic exponent is
\[
\limsup_{t\to\infty}\frac{\log|x(t)|}{t}
=\lambda\,\mathbb E\log\left|\frac{k}{a}+
  \left(1-\frac{k}{a}\right)e^{aH}\right|,
\qquad H\sim\operatorname{Exp}(\lambda).
\]
A gain with negative right-hand side exists exactly when \(\lambda>a/2\); every such gain has an almost surely exponentially decaying continuous-time state. At or below the threshold, every gain has nonnegative upper exponent, and every gain except \(k=a\) has strictly positive upper exponent. The critical gain \(k=a\) leaves the state unchanged.

The almost-sure threshold is four times lower than the **previously established** mean-square stabilizability threshold \(\lambda>2a\) for the same scalar zero-order-held model [2]. For \(a/2<\lambda\le2a\), a fixed gain yields almost-sure exponential decay even though no fixed gain yields mean-square exponential stability. The mean-square threshold itself is prior work, not an originality claim here.

## Assumptions and scope

All statements hold for every \(a>0\), \(\lambda>0\), every real \(k\), and every deterministic \(x(0)\ne0\), in exact arithmetic. The stochastic intersample gaps are independent with exponential law of rate \(\lambda\) and are independent of the initial state. Sampling is instantaneous and control is constant on each holding interval; there is no process or observation noise. Throughout, the natural logarithm of zero is interpreted as \(-\infty\) when taking the upper exponent.

At isolated intersample times the state can cross exactly through zero and subsequently become nonzero. Thus the claimed continuous-time limit is a **limsup**, not an ordinary limit; the ordinary logarithmic limit need not exist. Along sampling times \(T_n\), the ordinary logarithmic exponent does exist almost surely.

## Proof

**1. Exact regenerative multiplier and exponent.** Solving the affine ODE on one holding interval gives
\[
X_{n+1}=M(H_n)X_n,\quad
M(h)=\frac{k}{a}+\left(1-\frac{k}{a}\right)e^{ah},
\quad X_n=x(T_n).
\]
For \(k\ne a\), \(\mathbb E|\log|M(H)||<\infty\): the only possible finite singularity, at the unique zero of \(M\) when \(k>a\), is logarithmic and has a continuous positive gap density, while the tail grows no faster than a constant plus \(aH\). At \(k=a\), \(M=1\). A sampling-time multiplier is zero with probability zero, hence all \(X_n\ne0\) almost surely. The strong law yields
\[
\frac{\log|X_n|}{T_n}\longrightarrow
\lambda\,\mathbb E\log|M(H)|\quad\text{almost surely},
\]
since \(T_n/n\to1/\lambda\). Inside each interval, the absolute multiplier at elapsed age \(h\) is at most \(C_k e^{ah}\) for a finite constant \(C_k\). The exponential holding tails imply \(H_n/T_n\to0\) almost surely (e.g. by Borel--Cantelli). Therefore the intersample upper excursion changes the normalized logarithm by at most \(o(1)\), while sample times attain the sample-limit value. This proves the asserted **upper** physical-time exponent. Its strict negativity is equivalent to pathwise exponential decay; its positivity excludes such decay.

**2. Eliminate non-overcompensating feedback.** If \(k<a\), then \(M(h)>1\) for each \(h>0\), so \(\mathbb E\log M(H)>0\). If \(k=a\), \(M=1\). Thus any stabilizing gain must have \(k>a\).

**3. A beta-integral parameterization.** For \(k>a\), write
\[
\alpha=\lambda/a>0,\qquad \theta=1-a/k\in(0,1),
\qquad Y=e^{-aH}\sim\operatorname{Beta}(\alpha,1).
\]
Then
\[
M(H)=\frac{Y-\theta}{(1-\theta)Y},\qquad
F_\alpha(\theta)=\mathbb E\log|M(H)|
=-\log(1-\theta)+
\alpha\int_0^1y^{\alpha-1}\log|1-\theta/y|\,dy.
\]
The integrals are finite for all stated parameters, and \(F_\alpha(0+)=0\).

**4. The sharp obstruction for \(0<\alpha\le1/2\).** For \(0<\alpha<1\), differentiation of the logarithmic potential in the principal-value sense, justified by splitting symmetrically about the interior singularity, gives
\[
F_\alpha'(\theta)=\frac1{1-\theta}+
\alpha\theta^{\alpha-1}\operatorname{PV}
\int_0^{1/\theta}\frac{z^{\alpha-1}}{1-z}\,dz.
\]
For \(0<\alpha<1\), the principal-value integral equals
\[
\pi\cot(\pi\alpha)
+\int_{1/\theta}^{\infty}\frac{z^{\alpha-1}}{z-1}\,dz.
\]
Indeed, split the whole-line principal value at one, replace \(z>1\) by \(1/z\), expand the resulting nonsingular paired integrand in a geometric series, and use the digamma reflection identity:
\[
\operatorname{PV}\int_0^\infty
\frac{z^{\alpha-1}}{1-z}\,dz
=\sum_{j=0}^{\infty}\left(\frac1{j+\alpha}-\frac1{j+1-\alpha}\right)
=\pi\cot(\pi\alpha).
\]
For \(0<\alpha\le1/2\), the cotangent and the remaining tail integral are both nonnegative, and the term \(1/(1-\theta)\) is strictly positive. Therefore \(F_\alpha'(\theta)>0\) on \((0,1)\), so \(F_\alpha(\theta)>0\) for every overcompensating gain. In the boundary case \(\alpha=1/2\), substitution \(Y=U^2\) with \(U\) uniform on \((0,1)\) also gives the independent exact check
\[
F_{1/2}(\theta)=\sqrt\theta\,
\log\!\left(\frac{1+\sqrt\theta}{1-\sqrt\theta}\right)>0.
\]

**5. Construct stabilizing gains for \(\alpha>1/2\).** The derivative representation gives, for \(1/2<\alpha<1\),
\[
F_\alpha(\theta)=\pi\cot(\pi\alpha)\,\theta^\alpha+O_\alpha(\theta)
\quad(\theta\downarrow0).
\]
Its leading coefficient is negative. At \(\alpha=1\), the logarithmic-potential derivative simplifies to
\[
F_1'(\theta)=\frac1{1-\theta}+
\log\!\left(\frac\theta{1-\theta}\right),
\quad F_1(\theta)=\theta\log\!\left(\frac\theta{1-\theta}\right),
\]
so it is again negative for sufficiently small positive \(\theta\). For \(\alpha>1\), the finite negative first inverse moment yields
\[
F_\alpha(\theta)= -\frac{\theta}{\alpha-1}+o_\alpha(\theta).
\]
Therefore for every \(\alpha>1/2\), choosing sufficiently small \(\theta>0\), equivalently choosing \(k=a/(1-\theta)>a\) sufficiently close to \(a\), yields \(F_\alpha(\theta)<0\). Together with Step 4 this proves the exact threshold.

**6. Context of the known second-moment boundary.** If \(k>a\) and \(\lambda\le2a\), the term \(e^{aH}\) gives \(\mathbb E M(H)^2=\infty\), so already the first sampled-state second moment is infinite. For \(\lambda>2a\), elementary exponential moments give
\[
\mathbb EM(H)^2=1-2s\frac{a}{\lambda-a}
+s^2\frac{2a^2}{(\lambda-a)(\lambda-2a)},
\qquad s=(k-a)/a.
\]
The sampled-state expression is minimized by \(k=\lambda/2\), with minimum \(\lambda/[2(\lambda-a)]<1\). The previously established continuous-time mean-square stabilizability boundary is \(\lambda>2a\) [2,3]; the new contribution is the pathwise **sharp** boundary and its strict separation from mean square.

## Verification

Run `python verify_poisson_threshold.py` after installing `requirements.txt`. The program checks exact rational versions of the interval multiplier, numerically compares two independently derived logarithmic-integral representations at 21 parameter points, checks the critical-half closed form, samples both sides of the threshold, checks noncritical small-parameter coefficients, verifies the second-moment optimum, and performs one illustrative finite sample-path comparison with the strong-law prediction. These finite computations are corroboration only; the sharp threshold for all parameters follows from the analytic steps above.

## Relationship to prior work

Basu, Ferrante, and Fiacchini [1] address output regulation with stochastically sampled measurements, motivating the model class but working with mean exponential stability, hybrid observers, and LMIs rather than the sharp fixed-gain pathwise scalar threshold here. Tanwani, Chatterjee, and Liberzon [2, Section 6.3, Proposition 6.2] study **the same scalar plant and zero-order hold** and establish the mean-square stabilizability boundary \(\lambda>2a\); this earlier threshold is explicitly **not** new. Huff, Fiacchini, and Gomes da Silva Jr. [3] prove necessary and sufficient convex conditions for *mean exponential* stability under Poisson sampling, a different stability notion. Beutler [4] establishes a general logarithmic sufficient condition for almost-sure stochastic operator stability, conceptually encompassing the multiplier method; the abstract available for comparison does not state the exact scalar Poisson intensity frontier \(\lambda>a/2\). The complete text of [4] could not be inspected and remains a priority risk. No claim of a general new log-stability principle is made.

## Limitations

The result is restricted to a single unstable real scalar, a fixed real memoryless sampled-state feedback gain, independent exponential intersample gaps, and exact continuous-time dynamics. It does not address multidimensional plants, state delays, random/optimized feedback gains, dropout, or other renewal laws. The full-time ordinary logarithmic limit can fail because the trajectory crosses zero within holding intervals: only the upper exponent and the sampling-time ordinary limit are claimed. An inaccessible older article [4] may contain an equivalent scalar calculation; independent priority review has not been performed.

## References

1. H. Basu, F. Ferrante, and M. Fiacchini, *Output Regulation of Stochastic Sampled-Data Systems with Post-processing Internal Model*, arXiv:2306.15317v1, first submitted June 27, 2023. https://arxiv.org/abs/2306.15317.
2. A. Tanwani, D. Chatterjee, and D. Liberzon, *Stabilization of Deterministic Control Systems Under Random Sampling: Overview and Recent Developments*, 2018, Section 6.3, Proposition 6.2. https://liberzon.csl.illinois.edu/research/Tanwani2018_Chapter_StabilizationOfDeterministicCo.pdf.
3. D. Denardi Huff, M. Fiacchini, and J. M. Gomes da Silva Jr., *Necessary and Sufficient Convex Condition for the Stabilization of Linear Sampled-data Systems under Poisson Sampling Process*, IEEE Control Systems Letters, 2022, DOI 10.1109/LCSYS.2022.3184902. https://www.gipsa-lab.grenoble-inp.fr/~mirko.fiacchini/files/22_HuffLCSS_Poisson.pdf.
4. F. J. Beutler, *Almost Sure Exponential Bounds for Stochastic Operator Systems, with Applications to Randomly Sampled Control*, SIAM Journal on Applied Mathematics 23 (1972), 164–170, DOI 10.1137/0123017. Full text unavailable for this comparison; abstract inspected.
