# Exact ranking inversion law for paired one-dimensional sketched Rayleigh quotients

## Finding

Let \(A\) be any real symmetric matrix with two orthonormal eigenvectors \(u,v\) of distinct eigenvalues \(a<b\). For \(0<\theta<\pi/4\), construct the two unit trial vectors
\[
x=\cos\theta\,u+\sin\theta\,v,\qquad y=\sin\theta\,u+\cos\theta\,v.
\]
Their ordinary Rayleigh quotients satisfy \(x^\mathsf T A x<y^\mathsf T A y\). With the **same** \(k\times n\) matrix \(S\) of independent \(N(0,1)\) entries, compute both one-dimensional sketched Rayleigh quotients
\[
Q_S(z)=\frac{(Sz)^\mathsf T(SAz)}{(Sz)^\mathsf T(Sz)},\qquad z\in\{x,y\}.
\]
Put \(\rho=\sin(2\theta)\in(0,1)\). The probability of the **strictly reversed** ordering is, for every integer \(k\ge1\),
\[
\boxed{\Pr\{Q_S(x)>Q_S(y)\}
=\frac{\Gamma((k+1)/2)^2\rho^k}{\pi k\,\Gamma(k)}
{}_3F_2\!\left(\begin{matrix}\frac12,\frac{k+1}2,\frac k2\\ k,\frac k2+1\end{matrix};\rho^2\right).}
\]
The probability is strictly positive, strictly increasing with \(\rho\), and **independent of both the eigenvalue gap and the ambient matrix dimension**. Two useful special cases are
\[
\Pr\{Q_S(x)>Q_S(y)\}=\frac{\arcsin\rho}{\pi}\quad(k=1),
\qquad
\Pr\{Q_S(x)>Q_S(y)\}=\frac12-\frac{E(\rho)}{\pi}\quad(k=2),
\]
where \(E(\rho)=\int_0^{\pi/2}\sqrt{1-\rho^2\sin^2 t}\,dt\) is the complete elliptic integral of the second kind (modulus convention). For each fixed \(\rho\in(0,1)\), as \(k\to\infty\),
\[
\boxed{\Pr\{Q_S(x)>Q_S(y)\}\sim
\sqrt{\frac2\pi}\,\frac{(\rho/2)^k}{\sqrt{k(1-\rho^2/2)}}.}
\]
In particular, the ratio of consecutive inversion probabilities tends to \(\rho/2\). The **joint** use of the same sketch is essential; the statement is not a result for independent sketches on the two candidates.

## Assumptions and scope

All inner products are real and unweighted. The eigenvectors \(u,v\) are orthonormal, the eigenvalues \(a,b\) are real and satisfy \(a<b\); the ambient dimension is at least two. The trial angle satisfies \(0<\theta<\pi/4\) and the sketch has any integer number \(k\ge1\) of independent standard-normal rows. The quotient denominators are almost surely positive. The theorem concerns *two separate one-dimensional sketched Ritz estimates*; it is not a theorem about the eigenvalues of a joint two-dimensional projected operator. The endpoints \(\rho=0\) and \(\rho=1\) are excluded from the statement: at \(\rho=0\) the trial vectors are exact eigenvectors and the inversion probability is zero; at \(\theta=\pi/4\) they coincide and the strict inversion event is empty, so taking \(\rho\uparrow1\) in the interior formula does not give that endpoint probability.

## Proof

**1. Exact sign reduction.** Set \(c=\cos\theta\), \(s=\sin\theta\), \(g=Su\), and \(h=Sv\). Since \(S\) is standard Gaussian and \(u,v\) are orthonormal, \(g,h\) are independent standard Gaussian vectors in \(\mathbb R^k\). Write \(U=\|g\|^2\), \(Z=\|h\|^2\), and \(V=g^\mathsf T h\). The quotient numerators and denominators are
\[
\begin{array}{ll}
N_x=ac^2U+bs^2Z+(a+b)csV,&D_x=c^2U+s^2Z+2csV,\\
N_y=as^2U+bc^2Z+(a+b)csV,&D_y=s^2U+c^2Z+2csV.
\end{array}
\]
Direct expansion, without a distributional approximation, gives
\[
N_xD_y-N_yD_x=(a-b)(c^2-s^2)\{UZ+csV(U+Z)\}.
\]
Because \((a-b)(c^2-s^2)<0\) and both denominators are almost surely positive, reversal occurs exactly when
\[
UZ+\frac\rho2 V(U+Z)<0.\tag{1}
\]
The eigenvalues cancel from the sign test.

**2. Trace-normalized Wishart coordinates.** Let \(H=U+Z\), \(r=(U-Z)/H\), and \(w=2V/H\). By Cauchy--Schwarz, \(r^2+w^2\le1\), and (1) is equivalent to
\[
1-r^2+\rho w<0.\tag{2}
\]
For \(k\ge2\), the Gram matrix of \(g,h\) is a nonsingular real Wishart matrix almost surely. Its density is proportional to \((UZ-V^2)^{(k-3)/2}e^{-(U+Z)/2}\) on the positive-definite cone. The inverse change of variables is \(U=H(1+r)/2\), \(Z=H(1-r)/2\), \(V=Hw/2\), with absolute Jacobian \(H^2/4\). Integrating out \(H\) yields the **normalized** disk density
\[
f_k(r,w)=\frac{k-1}{2\pi}(1-r^2-w^2)^{(k-3)/2},\qquad r^2+w^2<1.\tag{3}
\]
Hence \(r\) has density \((1-r^2)^{k/2-1}/B(1/2,k/2)\), and, conditional on \(r\), \(w/\sqrt{1-r^2}\) has density proportional to \((1-t^2)^{(k-3)/2}\) on \((-1,1)\).

**3. An exact one-dimensional probability integral.** Write \(I_z(\alpha,\beta)\) for the regularized incomplete beta function and \(B\) for the beta function. From (2), an inversion is possible at fixed \(r\) only if \(|r|>\sqrt{1-\rho^2}\). Conditional beta integration, using the symmetry \(r\mapsto-r\), gives
\[
p_k(\rho)=\frac1{B(1/2,k/2)}
\int_{\sqrt{1-\rho^2}}^1
(1-r^2)^{k/2-1}
I_{1-(1-r^2)/\rho^2}\!\left(\frac{k-1}2,\frac12\right)dr.\tag{4}
\]
Substitute \(t=\sqrt{1-r^2}/\rho\). This becomes
\[
p_k(\rho)=\frac{\rho^k}{B(1/2,k/2)}
\int_0^1\frac{t^{k-1}}{\sqrt{1-\rho^2t^2}}
I_{1-t^2}\!\left(\frac{k-1}2,\frac12\right)dt.\tag{5}
\]
All integrands are nonnegative. Expanding the square-root denominator and applying Tonelli's theorem, the coefficient of \((1/2)_j\rho^{2j}/j!\) is the beta integral
\[
\int_0^1 t^{k+2j-1}I_{1-t^2}\!\left(\frac{k-1}2,\frac12\right)dt
=\frac{B((k-1)/2,(k+2j+1)/2)}{(k+2j)B((k-1)/2,1/2)}.\tag{6}
\]
After gamma simplification, the ratio of the \(j\)-th coefficient to the zeroth coefficient is
\[
\frac{((k+1)/2)_j(k/2)_j}{(k)_j(k/2+1)_j}.
\]
The zeroth coefficient is \(\Gamma((k+1)/2)^2/(\pi k\Gamma(k))\); the displayed \({}_3F_2\) formula follows for \(k\ge2\).

**4. The one-row and two-row identities.** For \(k=1\), write the two independent scalar Gaussians in polar coordinates. Then \((r,w)\) is uniform on the unit circle, so (2) becomes \(w(w+\rho)<0\). The fraction of the circle with \(-\rho<w<0\) is \(\arcsin\rho/\pi\). The hypergeometric series above reduces to this same function when \(k=1\), by the classical power series for \(\arcsin\). For \(k=2\), the conditional beta law in (5) has \(I_{1-t^2}(1/2,1/2)=2\arccos(t)/\pi\). Therefore
\[
p_2(\rho)=\frac{\rho^2}{\pi}\int_0^1\frac{t\arccos t}{\sqrt{1-\rho^2t^2}}dt
=\frac12-\frac1\pi\int_0^1\frac{\sqrt{1-\rho^2t^2}}{\sqrt{1-t^2}}dt
=\frac12-\frac{E(\rho)}\pi,
\]
where the middle equality is integration by parts.

**5. Strict dependence on overlap and sharp asymptotics.** In (2), inversion requires \(w<0\), and increasing \(\rho\) strictly enlarges the event region of positive disk (or circle) measure; this proves strict increase. The gamma duplication formula and Stirling's ratio give
\[
\frac{\Gamma((k+1)/2)^2}{\pi k\Gamma(k)}
\sim\sqrt{\frac2{\pi k}}\,2^{-k}.
\]
For each fixed series index \(j\), the hypergeometric coefficient ratio tends to \(2^{-j}\). Each ratio is bounded by one for \(k\ge1\), so for \(0<\rho<1\) the series is dominated by \(\sum_{j\ge0}(1/2)_j\rho^{2j}/j!\), which converges. Dominated convergence shows that the \({}_3F_2\) factor tends to \((1-\rho^2/2)^{-1/2}\). Multiplication proves the claimed equivalence and the limiting consecutive-row ratio.

## Verification

Execute `python verify.py` with the dependencies in `requirements.txt`. The verifier reconstructs the cross-multiplication identity symbolically, compares the hypergeometric formula against its **independently evaluated beta integral** for multiple row counts and overlaps, tests both closed-form cases, checks large-row asymptotics, and runs direct Gaussian experiments with a fixed seed. The recorded execution passed 700,113 exact/numerical/sample checks. The proof above establishes the infinite-dimensional parameter ranges and exact asymptotic statement; computational tests alone do not prove them.

## Relationship to prior work

Nakatsukasa and Tropp (2021 preprint; 2024 journal) introduce sketching into Rayleigh--Ritz and explain how the sketch can destroy symmetry and classical eigenvalue safeguards. Balabanov and Grigori (2021 preprint) explicitly define a sketched Rayleigh quotient and discuss numerical eigenvalue approximation. Neither of the inspected relevant full-text sections specifies the **joint strict-order inversion probability for a common Gaussian sketch**, its exact special-function formula, or the sharp \((\rho/2)^k/\sqrt{k}\) rate. These previous methods and the two-dimensional Wishart distribution are foundational ingredients, not claimed inventions. A standard one-quotient spectral-envelope escape probability and prior single-quotient distributional results do not imply this two-candidate joint event without additional covariance analysis.

## Limitations

The theorem treats symmetric two-eigenvector mixtures, equal-magnitude swapped trial coefficients, a single Gaussian sketch shared between the two estimates, and **separate** one-dimensional Ritz quotients. It does not analyze eigenvalue sorting of a joint projected matrix, arbitrary trial-vector pairs, non-Gaussian sketches, or sketch-dependent trial selection. It does not imply numerical conditioning bounds for an implemented eigensolver. The large-row equivalent fixes \(\rho\in(0,1)\). At \(\rho=1\), the candidate vectors coincide and the strict event is empty, so a discontinuity from interior limits is expected. Independent publication-priority verification and independent scientific audit have not been performed.

## References

1. Y. Nakatsukasa and J. A. Tropp, *Fast & Accurate Randomized Algorithms for Linear Systems and Eigenvalue Problems*, publicly posted October 29, 2021, arXiv:2111.00113. https://arxiv.org/abs/2111.00113 ; https://ar5iv.labs.arxiv.org/html/2111.00113 .
2. O. Balabanov and L. Grigori, *Randomized Block Gram-Schmidt Process for the Solution of Linear Systems and Eigenvalue Problems*, arXiv:2111.14641 (2021), especially the sketched Rayleigh quotient formulation. https://arxiv.org/abs/2111.14641 .
3. Classical real Wishart density and beta/gamma integral identities, used explicitly and derived where necessary above; these distributions and identities are not claimed as new.
