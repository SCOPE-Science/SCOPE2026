# Zero-free ambiguity for a three-stage arithmetic exponential cascade and its complex-Doppler transition

## Finding
Let \(a,d>0\). Define the threefold causal-exponential convolution
\[
\eta_b(t)=e^{-bt}\mathbf1_{[0,\infty)}(t),\qquad
f_{a,d}=\eta_a*\eta_{a+d}*\eta_{a+2d}.
\]
For every real delay \(\tau\) and Doppler frequency \(\nu\), the symmetric self-ambiguity function
\[
A_{a,d}(\tau,\nu)=\int_{\mathbb R} f_{a,d}(t+\tau/2)f_{a,d}(t-\tau/2)e^{-2\pi i\nu t}\,dt
\]
**does not vanish**. More precisely, with \(T=|\tau|\), \(\rho=e^{-dT}\), \(s=(2a+2\pi i\nu)/d\), and \(D(s)=\prod_{j=0}^4(s+j)\),
\[
A_{a,d}(\tau,\nu)=\frac{e^{-aT-i\pi\nu T}}{2d^5}
\frac{P_\rho(s)}{D(s)},\quad
P_\rho(s)=(1-\rho)^2s^2+(1-\rho)(7-\rho)s+12.
\]
For every \(T>0\), the meromorphic continuation in complex \(\nu\) has exactly two zeros counted with multiplicity, and their \(s\)-coordinates satisfy \(\Re s<-3\). It has five simple poles, corresponding to \(s=0,-1,-2,-3,-4\), with no zero/pole cancellations. The two zeros are nonreal conjugates in the \(s\)-plane when \(0<dT<\log(7+4\sqrt3)\), coalesce into a double zero at \(s=-2-\sqrt3\) when
\[
dT=\log(7+4\sqrt3),
\]
and are two distinct real points in \((-4,-3)\) when \(dT>\log(7+4\sqrt3)\). At \(T=0\), the numerator is the positive constant \(12\), so no finite zeros occur in the meromorphic continuation.

## Assumptions and scope
The window is not normalized to unit \(L^2\) norm; multiplying it by any nonzero constant only rescales its ambiguity function and does not change the zero sets. Both the rate offset \(a>0\) and increment \(d>0\) are arbitrary. All real delay and frequency values, including \(\tau=0\) and \(\nu=0\), are covered. "Complex-Doppler zeros" refer solely to the meromorphic continuation of the explicit rational-exponential formula, not physical zeros at real frequencies. The theorem does not concern three arbitrary unrelated decay rates or convolutions of four or more factors.

## Proof
**Step 1 (threefold convolution).** The Laplace transform in the causal variable is
\[
\frac1{(w+a)(w+a+d)(w+a+2d)}.
\]
Partial fractions, or two elementary convolution integrations, give
\[
f_{a,d}(t)=\frac{e^{-at}(1-e^{-dt})^2}{2d^2}\,\mathbf1_{[0,\infty)}(t).
\]
The function is real and nonnegative. Consequently, the product inside the ambiguity integral is unchanged on replacing \(\tau\) by \(-\tau\); write \(T=|\tau|\). Setting \(t=u+T/2\) and using causal support, we obtain
\[
A_{a,d}(\tau,\nu)=\frac{e^{-aT-i\pi\nu T}}{4d^4}
\int_0^\infty e^{-(2a+2\pi i\nu)u}
(1-e^{-du})^2(1-e^{-dT}e^{-du})^2\,du.
\]
The substitution \(z=e^{-du}\) leads to
\[
A_{a,d}(\tau,\nu)=\frac{e^{-aT-i\pi\nu T}}{4d^5}
\int_0^1 z^{s-1}(1-z)^2(1-\rho z)^2\,dz.
\]
Here \(\Re s=2a/d>0\) for real \(\nu\), justifying the Euler integral.

**Step 2 (exact rational formula).** Expanding only the final quadratic gives
\[
\int_0^1 z^{s-1}(1-z)^2(1-\rho z)^2\,dz
=B(s,3)-2\rho B(s+1,3)+\rho^2 B(s+2,3)
=\frac{2P_\rho(s)}{D(s)}.
\]
The three beta terms are explicit rational functions because \(B(s+k,3)=2/((s+k)(s+k+1)(s+k+2))\). This proves the displayed ambiguity formula for every real \(\tau,\nu\), including \(T=0\) by continuity.

**Step 3 (global zero-freeness).** If \(0\le\rho<1\), set \(w=s+3\). Exact algebra yields
\[
P_\rho(s)=(1-\rho)^2w^2+(1-\rho)(1+5\rho)w+6\rho(1+\rho).
\]
For \(0<\rho<1\), all three real coefficients are strictly positive. The roots of a quadratic with positive real coefficients all have strictly negative real parts: if its discriminant is nonnegative both roots are negative (positive sum of their opposites and positive product), whereas if it is negative their common real part is negative. Hence every root has \(\Re s<-3\). At \(\rho=1\), the numerator is \(12\) and has no roots. At physical real \(\nu\), \(\Re s=2a/d>0\), so the numerator never vanishes. All factors of \(D(s)\) are also nonzero there. The exponential prefactor is nonvanishing. This proves the claimed real-plane zero-freeness, including the zero-delay boundary.

**Step 4 (meromorphic zero and pole census).** For \(T>0\), \(\rho\in(0,1)\) and \(P_\rho\) has degree two. The identities
\[
\begin{aligned}
P_\rho(0)&=12,&P_\rho(-1)&=6(1+\rho),\\
P_\rho(-2)&=2(1+4\rho+\rho^2),&
P_\rho(-3)&=6\rho(1+\rho),\\
P_\rho(-4)&=12\rho^2
\end{aligned}
\]
exclude cancellations with all five factors of \(D(s)\). Thus the complete meromorphic continuation has exactly two numerator zeros with multiplicity and five distinct simple poles. They are mapped bijectively by the affine transformation between \(s\) and complex \(\nu\). The discriminant is
\[
\operatorname{disc}_s P_\rho=(1-\rho)^2(\rho^2-14\rho+1).
\]
The only root of \(\rho^2-14\rho+1\) in \((0,1)\) is \(\rho_*=7-4\sqrt3\), giving the unique finite delay threshold \(dT_*=\log(7+4\sqrt3)\). Below this delay the two roots are nonreal conjugates; at the threshold they coincide at \(s=-2-\sqrt3\) (the quadratic leading coefficient remains positive), so the zero has exact order two. Above the threshold they are real, distinct, and satisfy \(s<-3\). In addition, putting \(v=s+4\) gives
\[
P_\rho(s)=(1-\rho)^2v^2+(1-\rho)(7\rho-1)v+12\rho^2.
\]
Since \(0<\rho<7-4\sqrt3<1/7\), the sum and product of the two real \(v\)-roots are positive, so both satisfy \(v>0\), or \(s>-4\). Together with \(s<-3\), this proves the claimed interval. At \(T=0\), \(\rho=1\) and there are no numerator zeros. All claims follow.

## Verification
The standalone `checker.py` uses exact symbolic identities to verify the numerator, shift, discriminant, and all five pole noncancellation values. It evaluates the original defining ambiguity integral directly at seven choices of \((a,d,\tau,\nu)\), including negative delay and zero frequency, and compares those values at high precision against the rational formula. The maximum scaled absolute discrepancy in the included run was less than \(4\times10^{-16}\). It also checks representative complex-root configurations on both sides of the threshold and at equality. These computations are corroboration only: the all-parameter result is proved above, without numerical extrapolation.

## Relationship to prior work
Kloos and Stöckler (2013, arXiv:1311.7359v1) analyze totally positive functions of finite type and exponential B-splines using Zak transforms and Gabor frames, providing the natural older window family. Gröchenig, Jaming, and Malinnikova (2018, arXiv:1811.03937v1), Section 3 Lemma 3.1, prove zero-freeness for convolutions of two causal exponentials; Section 4 proves it for equal-rate higher convolutions using Hurwitz/Bessel polynomials. Immediately following their Lemma 3.1 they explicitly identify the zeros of higher convolutions with distinct decay rates as requiring a separate investigation. The present statement treats exactly the first arithmetic-progression triple among those distinct-rate higher convolutions and adds its complete complex-Doppler numerator zero classification. The familiar two-rate and equal-rate statements do not imply the explicit three-distinct-rate formula or its sharp discriminant transition. A more general, not yet located theorem for totally positive functions or rational Laplace transforms could subsume this special family; priority beyond the inspected sources is not established.

## Limitations
Distinct rates are required to lie in a three-term arithmetic progression; the formula alone does not settle arbitrary triples. "Nonreal" refers to the auxiliary polynomial coordinate \(s\) and not to real-world Doppler measurements. The meromorphic continuation has poles away from the physical real-frequency axis, and no assertion is made about zeros at its poles. Seven numerical integration tests are not an exhaustive verification of real frequencies; unrestricted correctness comes from the displayed identities and quadratic argument. No independent mathematical audit or publication-priority determination has been performed.

## References
1. T. Kloos and J. Stöckler, *Zak transforms and Gabor frames of totally positive functions and exponential B-splines*, arXiv:1311.7359v1, publicly available 2013-11-28. https://arxiv.org/abs/1311.7359
2. K. Gröchenig, P. Jaming, and E. Malinnikova, *Zeros of the Wigner Distribution and the Short-Time Fourier Transform*, arXiv:1811.03937v1, publicly available 2018-11-09, in particular Section 3 after Lemma 3.1 and Section 4. https://arxiv.org/abs/1811.03937
