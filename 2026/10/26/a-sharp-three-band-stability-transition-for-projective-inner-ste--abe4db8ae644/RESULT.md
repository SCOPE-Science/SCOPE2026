# A sharp three-band stability transition for projective inner-step variation

## Finding
For the original three-stage projective inner-step-size-variation (PISV) scheme of Koellermeier and Samaey, the real negative stability domain changes from **three disjoint intervals to one interval** at the exact inner-to-outer-step ratio \(\lambda=1/9\). This gives a sharp spectral-gap threshold for the method's ability to damp all modes in the inner forward-Euler stability interval.

Specifically, set \(\lambda=\delta t/\Delta t\in(0,1/2]\), \(x=\kappa\Delta t\ge0\), and
\[
 s_\lambda=\sqrt{\frac{1-9\lambda}{1-\lambda}}\quad(0<\lambda<1/9).
\]
The complete weak real-axis stability set \(\mathcal S_\lambda=\{x\ge0:|R_\lambda(-x)|\le1\}\) is
\[
\mathcal S_\lambda=\begin{cases}
[0,\frac{1-s_\lambda}{2\lambda}]\ \cup\
[\frac{1+s_\lambda}{2\lambda},\frac{3-s_\lambda}{2\lambda}]\ \cup\
[\frac{3+s_\lambda}{2\lambda},\frac2\lambda],&0<\lambda<\frac19,\\[2mm]
[0,\frac2\lambda],&\frac19\le\lambda\le\frac12.
\end{cases}
\]
No further stable points occur at \(x>2/\lambda\). At the critical ratio \(\lambda=1/9\), \(|R_\lambda(-x)|=1\) also at the **interior** points \(x=9/2\) (amplification \(-1\)) and \(x=27/2\) (amplification \(+1\)); hence gap-free *weak* stability does not imply strict decay there. For \(\lambda>1/9\), every \(0<x<2/\lambda\) is strictly stable.

For \(0<\lambda<1/9\) the first and third stability bands both have length \(a_\lambda=(1-s_\lambda)/(2\lambda)\), the middle one has length \(2a_\lambda\), and both instability gaps have length \(s_\lambda/\lambda\). In the stiff separation limit \(\lambda\downarrow0\), the band lengths tend to \(2,4,2\), while both gaps grow like \(1/\lambda\).

## Assumptions and scope
Take \(\Delta t>0\), \(\delta t>0\), and \(0<\lambda=\delta t/\Delta t\le1/2\), so that the inner PISV steps fit into the outer-step interval without a negative remaining extrapolation time. Let \(f(y)=-\kappa y\) with \(\kappa\ge0\). The published three-stage scheme, in ordinary stage notation, reads
\[
\begin{aligned}
U_1&=y_n,\\
U_2&=y_n+\delta t\,f(U_1),\\
U_3&=y_n+\delta t\,f(U_1)+\frac{\delta t}{2}f(U_2),\\
y_{n+1}&=y_n+\delta t\,f(U_1)+(\Delta t-\delta t)f(U_3).
\end{aligned}
\]
This is the tableau in Eq. (96) of the cited PISV paper. Here absolute stability means bounded repeated scalar multiplication, \(|R_\lambda(-x)|\le1\); strict contraction means \(|R_\lambda(-x)|<1\). The claim concerns the real negative axis only, not general complex eigenvalues or nonnormal matrices.

## Proof
Set \(x=\kappa\Delta t\) and use the preceding stages. Direct substitution gives the exact polynomial
\[
R_\lambda(-x)=1-x+\frac32\lambda(1-\lambda)x^2-\frac12\lambda^2(1-\lambda)x^3
=(1-\lambda x)\left[1-(1-\lambda)x+\frac12\lambda(1-\lambda)x^2\right].
\]
The two stability inequalities factor **independently**:
\[
\begin{aligned}
R_\lambda(-x)+1&=(2-\lambda x)\left[1-\frac{1-\lambda}{2}x+\frac{\lambda(1-\lambda)}2x^2\right],\\
R_\lambda(-x)-1&=-x\left[1-\frac{3\lambda(1-\lambda)}2x+\frac{\lambda^2(1-\lambda)}2x^2\right].
\end{aligned}
\]
Both bracketed quadratic polynomials have positive leading coefficients. Their respective discriminants have the common sign of \(1-9\lambda\): they equal \((1-\lambda)(1-9\lambda)/4\) and \(\lambda^2(1-\lambda)(1-9\lambda)/4\).

If \(\lambda>1/9\), neither quadratic vanishes and both are strictly positive, giving \(-1<R_\lambda(-x)<1\) for \(0<x<2/\lambda\). At \(\lambda=1/9\), each quadratic has one double root, at \(x=9/2\) and \(x=27/2\), respectively, giving the two stated interior neutral points but no gap. If \(0<\lambda<1/9\), their positive roots, in increasing order, are
\[
\frac{1-s_\lambda}{2\lambda}<\frac{1+s_\lambda}{2\lambda}<\frac{3-s_\lambda}{2\lambda}<\frac{3+s_\lambda}{2\lambda}<\frac2\lambda.
\]
The first quadratic is negative exactly between the first pair (so \(R_\lambda(-x)<-1\) there), while the second is negative exactly between the second pair (so \(R_\lambda(-x)>1\) there). This yields the three claimed intervals and only those intervals on \([0,2/\lambda]\). For \(x>2/\lambda\), the first quadratic is strictly positive because it is increasing beyond that point and equals \(1/\lambda\) at \(x=2/\lambda\); the prefactor \(2-\lambda x\) is negative. Thus \(R_\lambda(-x)<-1\) and no stable points occur beyond the stated endpoint.

The band and gap lengths follow by subtraction of endpoints. Lastly,
\[
 s_\lambda=1-4\lambda+O(\lambda^2),\qquad
\frac{1-s_\lambda}{2\lambda}=2+O(\lambda),\qquad
\frac{s_\lambda}{\lambda}=\frac1\lambda-4+O(\lambda),
\]
which proves the claimed stiff-separation lengths.

## Verification
The standalone standard-library checker `verify_pisv.py` carries out exact bivariate polynomial-ring multiplication for the amplification polynomial and its two factorizations, exact checks of the critical neutral points and rational three-band endpoints at \(\lambda=1/10\), and 50,000 additional rational-amplification checks spanning both sides of the transition. It is auxiliary: the preceding factorization and discriminant argument is the complete infinite-domain proof.

As an exact example, at \(\lambda=1/10\) the stable intervals are
\[
[0,10/3]\ \cup\ [20/3,40/3]\ \cup\ [50/3,20].
\]
For a diagonal symmetric dissipative system, a mode lying strictly within either intervening gap amplifies in magnitude, even though its individual inner Euler step satisfies \(0<\delta t\,\kappa<2\).

## Relationship to prior work
Koellermeier and Samaey introduced PISV and provided its Runge--Kutta tableau (their Eq. (96)). Their real/complex stability discussion in Section 6.2 and Fig. 9(c) illustrates stability regions qualitatively, but does not state the parameter-sharp three-band formula or the critical interior neutral points. This work takes that scheme as given and supplies an exact complete **negative-real-axis** classification, rather than claiming invention of the algorithm or its stability function.

Classical projective-forward-Euler and projective-Runge--Kutta studies analyze amplification on separated fast/slow spectral clusters. Their general criteria do not themselves give these explicit PISV stability boundaries. Subsequent numerical projective integration for degenerate parabolic systems addresses different projective integrators and PDE applications, not the three-stage PISV stability phase diagram. Exact equivalent statements elsewhere remain possible.

## Limitations
The theorem is confined to the three-stage PISV scheme, scalar real nonpositive eigenvalues, and \(0<\lambda\le1/2\). It does not assert complex-plane stability, global nonlinear stability, positivity, or error estimation quality. Endpoints in the weak-stability bands may have amplification \(\pm1\) and therefore do not guarantee convergence to zero; in particular the critical ratio has two extra interior nondecaying modes. Claims of publication priority are subject to literature-coverage limits, and no independent scientific audit has been performed.

## References
1. J. Koellermeier and G. Samaey, *Projective Integration Methods in the Runge-Kutta Framework and the Extension to Adaptivity in Time*, arXiv:2210.08302, first submission 2022-10-15, revised 2024-01-19, especially Eq. (96), Section 6.2, and Figure 9(c). https://arxiv.org/abs/2210.08302
2. *Projective Integration Schemes for Nonlinear Degenerate Parabolic Systems*, Journal of Scientific Computing (2026), DOI:10.1007/s10915-026-03286-9, relevant background on fast/slow spectral stability regions; does not supply the PISV classification. https://doi.org/10.1007/s10915-026-03286-9
