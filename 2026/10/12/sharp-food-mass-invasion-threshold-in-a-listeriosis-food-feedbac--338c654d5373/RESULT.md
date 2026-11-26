# Exact endemic-equilibrium count on a fixed-food-mass leaf of the printed listeriosis model

## Finding

Consider the standalone listeriosis equations (4.1) of Koutou, Kouanda and Ouédraogo [1] on a fixed leaf with total food mass \(U+C=F>0\). For strictly positive rates, write \(h=\mu+\delta+\gamma\), \(k=\xi/d\), \(\Delta=p-a_4F\), and \(\widehat{\mathcal R}=\beta k\Lambda/(\mu h)\). The number of equilibria with all five coordinates strictly positive is as follows:

- If \(\Delta>0\), there is exactly one such equilibrium when \(\mathcal T_F:=\widehat{\mathcal R}(1+a_3F/\Delta)>1\), and none when \(\mathcal T_F\leq 1\), including at equality.
- If \(\Delta\leq 0\), there is exactly one such equilibrium for every strictly positive \(\beta\).

The contribution is the nonlinear equilibrium count, not the formula for the clean-food linear invasion index. On \(\Delta>0\) that index and its disease-free linear threshold were already obtained in [2]. Here it also determines whether a strictly positive equilibrium exists, and the count extends to cases where that index is not defined.

For example, take \(\Lambda=\mu=\delta=\gamma=\xi=d=p=a_3=a_4=1\), \(\beta=2\), and \(F=9/10\). Then \(\widehat{\mathcal R}=2/3\) and \(\mathcal T_F=20/3\), yet the strictly positive equilibrium is exactly
\[
(S,I,B,U,C)=(3/5,1/5,1/5,3/5,3/10).
\]
Thus the if-and-only-if criterion in [1, Proposition 4.2] does not hold on every positive fixed-food-mass leaf of the printed system.

## Assumptions and scope

The state coordinates denote susceptible and infected humans, environmental bacteria, and uncontaminated and contaminated food, respectively. With the notation above, equations (4.1) of [1] are
\[
\begin{aligned}
\dot S&=\Lambda+\gamma I-(\mu+\lambda)S, & \dot I&=\lambda S-hI,\\
\dot B&=\xi I-dB,&\lambda&=\beta(B+a_3C),\\
\dot U&=p(U+C)-(B+a_4C+p)U,&\dot C&=(B+a_4C)U-pC.
\end{aligned}
\]
The rates \(\Lambda,\mu,\delta,\gamma,\beta,\xi,d,p,a_3,a_4\) are strictly positive. The equation for \(\dot U+\dot C\) vanishes, so the leaf is invariant. We do not treat the five equations as an asserted invariant subsystem of the full co-infection system with all its parameters positive.

## Proof of the nonlinear count

Adding the human balance equations at equilibrium and imposing bacterial balance give
\[
S=\frac{\Lambda-(\mu+\delta)I}{\mu},\qquad B=kI,\qquad 0<I<I_{\max}:=\frac{\Lambda}{\mu+\delta}
\]
for any strictly positive equilibrium. The food equation reduces to
\[
q(C;B):=a_4C^2+(B+\Delta)C-BF=0,\qquad U=F-C.
\]
For \(B>0\), \(q(0;B)<0\) and \(q(F;B)=pF>0\); the product of the two roots is negative. Hence the unique positive root \(C(B)\) lies in \((0,F)\). Its derivative comes from
\[
\partial_C q(C(B);B)=\frac{BF+a_4C(B)^2}{C(B)}>0,\qquad
C'(B)=\frac{F-C(B)}{\partial_Cq(C(B);B)}>0.
\]
Writing the food balance as \(B(F-C)=C(\Delta+a_4C)\) shows that \(\Delta+a_4C>0\) on this branch and
\[
\frac{C(B)}B=\frac{F-C(B)}{\Delta+a_4C(B)}.
\]
The derivative of the right-hand expression with respect to \(C\) is \(-p/(\Delta+a_4C)^2\). Consequently \(C(B)/B\) strictly decreases with \(B\).

After substitution the remaining infected-human equation, divided by \(I>0\), is
\[
\beta\left(k+a_3\frac{C(kI)}I\right)=\frac{h\mu}{\Lambda-(\mu+\delta)I},\qquad 0<I<I_{\max}.
\]
The left side is continuous and strictly decreasing; the right side is continuous and strictly increasing. At the right endpoint the former has a finite limit and the latter diverges. Every solution reconstructs a strictly positive equilibrium and every strictly positive equilibrium is represented.

The positive food root extends continuously to \(B=0\), with value \(\max(0,-\Delta/a_4)\), as follows directly from the quadratic formula. If \(\Delta>0\), the displayed food ratio tends to \(F/\Delta\); the left limit of the human equation exceeds the right limit exactly when \(\mathcal T_F>1\). A strict crossing then exists and is unique, while equality of limits gives no crossing in the open interval. If \(\Delta\leq 0\), the denominator in the food ratio tends to zero from above, while the numerator tends to \(F\) for \(\Delta=0\) and \(p/a_4\) for \(\Delta<0\). The left limit is then infinite, and strict monotonicity gives exactly one crossing for each strictly positive \(\beta\).

In the rational example, \(\lambda=1\), \(h=3\), \(k=1\), \(\Delta=1/10\), and \(U+C=9/10\). The five printed derivatives, in the order \(S,I,B,U,C\), evaluate to
\[
1+1/5-2(3/5),\quad 3/5-3(1/5),\quad 1/5-1/5,\quad 9/10-(3/2)(3/5),\quad (1/2)(3/5)-3/10,
\]
all zero. This witness contradicts the printed equilibrium criterion rather than merely demonstrating an incorrect prediction of linear stability.

## Disease-free comparison (background)

With \(I=0\) at equilibrium one has \(B=0\), \(S=\Lambda/\mu>0\), and the infected equation then forces \(C=0\). The disease-free equilibrium on the leaf is \((\Lambda/\mu,0,0,F,0)\). In leaf coordinates the susceptible eigenvalue is \(-\mu\), and the other eigenvalues come from the block
\[
M_F=\begin{pmatrix}-h & Q & Q a_3\\ \xi &-d&0\\ 0&F&-\Delta\end{pmatrix},\qquad Q=\beta\Lambda/\mu.
\]
For \(\Delta>0\), [2] proves local asymptotic stability below \(\mathcal T_F=1\), linear instability above it, and a zero eigenvalue at equality. Equivalently, \(w=(1,k,kF/\Delta)^\mathsf{T}\) satisfies \(M_Fw=(h(\mathcal T_F-1),0,0)^\mathsf{T}\). The sign of the spectral bound follows by pairing with a strictly positive left eigenvector for that bound, available by the Perron theorem after shifting the irreducible Metzler block by a positive multiple of the identity. For \(\Delta\leq0\), the characteristic polynomial displayed in [2], evaluated at \(z=-\Delta\), equals \(-Q\xi a_3F<0\); it is monic and hence has a real root above \(-\Delta\geq0\). Thus the disease-free point is linearly unstable on those leaves as well. These linear facts are not a stability assertion about the strictly positive equilibrium.

## Reproducibility and relationship to prior work

The accompanying `verify.py` (with the dependency specified in `requirements.txt`) checks the fixed-leaf identities, the Jacobian and the rational example using exact arithmetic. The proof above, not the script, establishes the number of equilibria for all positive parameters.

Reference [1, §4, equations (4.1)–(4.6)] prints the disease-free point with zero food mass, gives the index \(\widehat{\mathcal R}\) in (4.2), and states in Proposition 4.2 that a unique endemic equilibrium exists if and only if that index exceeds one. Its bifurcation calculation in §4.1 uses the printed zero-food state. Reference [2] corrects the disease-free point and the local threshold at positive food mass and gives an instability witness. A local instability or a zero eigenvalue does not establish existence or uniqueness of a strictly positive equilibrium, including at equality or when \(\Delta\leq0\). The nonlinear argument here yields the exact count on all positive-mass leaves and a witness to the failure of Proposition 4.2. Other listeriosis models, such as [3, §3], have food-contamination thresholds, but use different equations and do not give this count for (4.1).

The statement is limited to the standalone equations, strictly positive rates, and fixed positive food mass. No global convergence, local or global stability of the positive equilibrium, full co-infection dynamics, or empirical inference is claimed. The result is a mathematical property of a specified model, not a calibrated epidemiological threshold.

## References

1. O. Koutou, C. A. K. Kouanda and A. Ouédraogo, “Mathematical Analysis of a Co-Dynamics Model of Listeriosis and Bacterial Meningitis Starting From Ready-to-Eat Foods,” *International Journal of Analysis and Applications* **24** (2026), 160. DOI: 10.28924/2291-8639-24-2026-160.
2. “The ready-to-eat food reservoir shifts the listeriosis invasion threshold,” Resultary, record [c83367963703](https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-the-ready-to-eat-food-reservoir-shifts-the-listeriosis-invasion--c83367963703), 2026-10-04, Finding and Proof.
3. C. W. Chukwu, F. Nyabadza and Fatmawati, “Modelling the Potential Role of Media Campaigns on the Control of Listeriosis,” *Mathematical Biosciences and Engineering* **18** (2021), 7580–7601. DOI: 10.3934/mbe.2021375.
