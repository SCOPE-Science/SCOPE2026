# Reciprocal ghost limits of the unrelaxed scalar auxiliary-variable optimizer on strongly convex quadratics

## Finding
For every \(a\in\mathbb R\setminus\{0\}\) and \(C>0\), there is \(H(a,C)>0\) such that all fixed steps \(h>H(a,C)\) in the **unrelaxed** scalar auxiliary-variable (SAV) minimization scheme converge to a **nonstationary** point on the strongly convex objective \(f(x)=x^2/2\), even as the scheme's modified energy tends to zero. The precise limit is
\[
 x_\infty(h)=-\frac{2C}{a}+\frac{(a^2+2C)^2}{a^3h}\left(1+\frac{|a|}{\sqrt{2C}}\right)+O_{a,C}(h^{-2}),\qquad h\to+\infty.
\]
Thus the leading ghost limit has the opposite sign from the initial point and magnitude \(2C/|a|\). The conclusion concerns the original unrelaxed update, not the relaxed, restarted, or line-search variants.

## Assumptions and scope
Work in exact real arithmetic. Let \(f(x)=x^2/2\), \(x_0=a\ne0\), \(C>0\), and \(r_0=\sqrt{f(a)+C}\). Apply equations (2.3) and (2.5) of Liu--Shen--Zhang with zero linear operator \(L=0\), fixed \(h>0\), and with **no relaxation or reinitialization**. In explicit form, for every integer \(k\ge0\),
\[
 r_{k+1}=\frac{r_k}{1+h x_k^2/(x_k^2+2C)},\qquad
 x_{k+1}=x_k-\frac{h r_{k+1}x_k}{\sqrt{x_k^2/2+C}}.
\]
All denominators are strictly positive and \(r_k>0\) at every finite step. The unique minimizer and only stationary point is zero. The symbol \(O_{a,C}(h^{-2})\) means a bound uniform as \(h\to\infty\) with \(a,C\) fixed.

## Proof
Put \(t=1/h\), \(A(x)=x^2+2C\), and \(s(x)=\sqrt{A(x)/2}\). The exactly equivalent rationalized equations are
\[
 r_{k+1}=r_k\frac{tA(x_k)}{x_k^2+tA(x_k)},\qquad
 x_{k+1}=x_k-\frac{2r_k s(x_k)x_k}{x_k^2+tA(x_k)}.
\]
Write \(A=a^2+2C\). The first step is obtained without approximation:
\[
 x_1=a\frac{tA-2C}{a^2+tA},\qquad
 r_1=s(a)\frac{tA}{a^2+tA}.
\]
Consequently \(x_1=-2C/a+tA^2/a^3+O_{a,C}(t^2)\) and \(r_1=t s(a)A/a^2+O_{a,C}(t^2)\). Define \(b=-2C/a\ne0\) and \(B=b^2+2C\). On the second step, substitute the exact first-step formulas and expand at \(t=0^+\); the denominators converge to \(b^2>0\). This yields
\[
 r_2=O_{a,C}(t^2),\qquad
 x_2=b+t\left(\frac{A^2}{a^3}-\frac{A\sqrt{AB}}{a^2b}\right)+O_{a,C}(t^2).
\]
Since \(b=-2C/a\) and \(B=2CA/a^2\), the coefficient in parentheses simplifies exactly to
\[
 K(a,C)=\frac{A^2}{a^3}\left(1+\frac{|a|}{\sqrt{2C}}\right).
\]
To control **all** later steps, choose the closed interval \(I=[b-|b|/2,b+|b|/2]\), which is disjoint from zero. Let
\[
 R=\max_{x\in I}\frac{A(x)}{x^2}<\infty,\qquad
 L_*=\max_{x\in I}\frac{2s(x)}{|x|}<\infty.
\]
For \(t\) sufficiently small, \(x_2\) lies within \(|b|/4\) of \(b\), \(tR<1/2\), and \(L_*r_2/(1-tR)<|b|/4\). As long as \(x_k\in I\), the update implies
\[
 0<r_{k+1}\le tRr_k,\qquad |x_{k+1}-x_k|\le L_*r_k.
\]
Induction from \(k=2\) and the geometric tail bound \(\sum_{j=2}^\infty L_*r_j\le L_*r_2/(1-tR)<|b|/4\) show that every later \(x_k\) stays in \(I\). Hence \(r_k\to0\) geometrically, \(x_k\) converges, and \(|x_\infty-x_2|=O_{a,C}(t^2)\). In particular, \(|x_\infty|\ge|b|/2>0\). Combining this uniform tail estimate with the second-step expansion proves the claimed two-term expansion. Finally, \(r_{k+1}<r_k\) on \(I\) and at the finite initial steps for sufficiently large \(h\), so \(r_k^2\downarrow0\), whereas \(f(x_k)\to x_\infty^2/2>0\).

**Explicit finite-step witness.** For \(a=C=1\), \(h=20\), the first two steps are exact:
\[
 x_1=-\frac{37}{23},\qquad
 r_1=\frac3{23}\sqrt{\frac32},\qquad
 r_2=\frac{7281}{685561}\sqrt{\frac32}<\frac1{75},
\]
\[
 x_2=-\frac{37}{23}\left(1-\frac{145620}{29807\sqrt{809}}\right),\qquad -1.34<x_2<-1.32.
\]
The last enclosure follows from \(28<\sqrt{809}<29\). On \(-1.6\le x\le-1\), the auxiliary contraction factor is at most \(3/23\), while \(|x_{k+1}-x_k|\le20\sqrt2\,r_{k+1}\). Therefore the post-second-step tail is at most \(3\sqrt2\,r_2<3\sqrt2/75<0.06\), which closes the invariant interval and gives \(-1.40<x_\infty<-1.26\), together with \(r_k\to0\). This is a rigorous infinite-iteration assertion, not an inference from truncating numerical trajectories.

## Verification
The accompanying self-contained `VERIFY.py` checks the source recurrence against its rationalized form; exact rational identities and rigorous square-root bounds for the \(h=20\) trapping witness; and floating-point trajectories at multiple starting signs, shifts, and large steps. It tests the asymptotic coefficient numerically but does not mistake finite trajectories for an infinite proof. The theorem's infinite-time limit and the \(h\to\infty\) error estimate follow from the invariant-interval and geometric-tail argument above.

## Relationship to prior work
Liu, Shen, and Zhang (2023), equations (2.3)–(2.5), introduced and analyzed this unrelaxed SAV optimization step and the relaxed/adaptive alternatives. Their Theorem 1 gives unconditional decay of modified energy. Their Section 2.4 identifies a small auxiliary-to-physical-energy ratio as a **slow-convergence risk**, while their Section 4 convergence argument for a reinitialized line-search variant imposes Wolfe-type safeguards. These results are not claimed as new. The present exact characterization shows something strictly stronger on the unrelaxed fixed-step recurrence: a sequence converges to a demonstrably **noncritical** point with the sharp reciprocal leading limit and first correction. The formal stationary-point inference from the update requires excluding a vanishing auxiliary variable, a possibility realized here.

Jiang, Zhang, and Zhao (2021) study consistency correction using relaxation; Ma, Mao, and Shen (2024) study SAV-based training and report altered solutions for a baseline SAV scheme. They motivate the importance of auxiliary-variable consistency but do not state the two-step reciprocal asymptotics for the specific unrelaxed modified optimization rule in the material examined. No universal uniqueness or publication-priority guarantee is inferred from searches.

## Limitations
The theorem concerns the unrelaxed, fixed-step, zero-linear-operator scheme on one strongly convex scalar quadratic. It does not assert nonconvergence for relaxed/restarted variants, Wolfe line searches, all starting steps, arbitrary strongly convex objectives, or floating-point implementations. The threshold \(H(a,C)\) is proved to exist but is not optimized; a separate exact rational witness covers \(h=20\) for \(a=C=1\). Prior specialized literature could contain equivalent observations; independent publication-priority and scientific audit have not been performed.

## References
1. X. Liu, J. Shen, X. Zhang, *An Efficient and Robust Scalar Auxiliary Variable Based Algorithm for Discrete Gradient Systems Arising from Optimizations*, arXiv:2301.02942v1 (first public posting 2023-01-07), SIAM J. Sci. Comput. 45 (2023), A2304–A2324, DOI: 10.1137/23M1545744. https://arxiv.org/pdf/2301.02942
2. M. Jiang, Z. Zhang, and J. Zhao, *Improving the Accuracy and Consistency of the Scalar Auxiliary Variable (SAV) Method with Relaxation*, arXiv:2104.06620 (2021). https://arxiv.org/abs/2104.06620
3. Z. Ma, Z. Mao, J. Shen, *Efficient and stable SAV-based methods for gradient flows arising from deep learning*, J. Comput. Phys. 505 (2024), 112911, DOI: 10.1016/j.jcp.2024.112911. https://www.math.purdue.edu/~shen7/pub/MMS_JCP24.pdf
