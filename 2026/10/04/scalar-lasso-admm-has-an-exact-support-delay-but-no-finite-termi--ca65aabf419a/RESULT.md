# Scalar Lasso ADMM has an exact support delay but no finite termination
## Finding
Consider the scalar Lasso splitting
\[
\min_{x,z\in\mathbb R} \frac12(x-b)^2+\lambda|z| \quad\text{subject to}\quad x=z,
\]
where \(b>\lambda>0\). Apply standard unrelaxed scaled ADMM with a fixed finite penalty \(\rho>0\), initialized by \(z^0=u^0=0\). Then the first index at which the split variable is positive is
\[
j_*=\left\lfloor\frac{\log(b/(b-\lambda))}{\log(1+\rho)}\right\rfloor+1.
\]
After that index, \(u^k=\lambda/\rho\) and, for every integer \(n\ge0\),
\[
z^{j_*+n}-(b-\lambda)=\left(\frac{\rho}{1+\rho}\right)^n\bigl(z^{j_*}-(b-\lambda)\bigr),
\]
with \(0<z^{j_*}<b-\lambda\). Consequently the support is identified after finitely many steps, but the ADMM state does not reach its fixed point in any finite number of iterations for any finite \(\rho>0\). The exact post-identification spectral radius is \(\rho/(1+\rho)\), which approaches \(1\) as \(\rho\to\infty\).

This supplies a one-coordinate counterexample to the finite-termination statement for the \(K=I\), anisotropic Lasso case in Dohmatob, Eickenberg, Thirion, and Varoquaux (2016, Theorem 1(c3)) as stated. It does not challenge finite active-set identification.
## Assumptions and scope
The loss is the scalar least-squares loss \(\tfrac12(x-b)^2\), the regularizer is \(\lambda|z|\), and \(b>\lambda>0\), so the unique primal solution is \(x^*=z^*=b-\lambda>0\). The scaled dual solution is \(u^*=\lambda/\rho\). The iteration is standard unrelaxed scaled ADMM with fixed finite \(\rho>0\):
\[
 x^{k+1}=\frac{b+\rho(z^k-u^k)}{1+\rho},\qquad
 z^{k+1}=S_{\lambda/\rho}(x^{k+1}+u^k),\qquad
 u^{k+1}=u^k+x^{k+1}-z^{k+1},
\]
where \(S_t(r)=\operatorname{sign}(r)\max\{|r|-t,0\}\), and \(z^0=u^0=0\). No assertion is made here about arbitrary initialization, over-relaxation, adaptive penalties, or general multivariate design matrices.
## Proof
Set \(q=(1+\rho)^{-1}\). As long as the soft-thresholding output remains zero, define the threshold input \(r^j=x^j+u^{j-1}\). Because \(z^0=u^0=0\) and all pre-activation quantities are nonnegative, the inactive recurrence is
\[
 r^j=\frac b\rho(1-q^j),\qquad z^j=0\quad\text{whenever}\quad r^j\le\frac\lambda\rho.
\]
Thus the first positive split variable occurs at the smallest positive integer \(j\) satisfying
\[
 b(1-q^j)>\lambda,
\]
or equivalently \(q^j<(b-\lambda)/b\). Since the inequality is strict, the least such integer is
\[
 j_*=\left\lfloor\frac{\log(b/(b-\lambda))}{\log(1+\rho)}\right\rfloor+1.
\]
At that step soft thresholding gives
\[
 z^{j_*}=\frac{b(1-q^{j_*})-\lambda}\rho>0,\qquad u^{j_*}=\frac\lambda\rho.
\]
Let \(c=(b-\lambda)/b\). Minimality of \(j_*\) gives \(q^{j_*-1}\ge c\), hence \(q^{j_*}\ge c/(1+\rho)\). Therefore
\[
 0<z^{j_*}=\frac{b(c-q^{j_*})}\rho\le\frac{bc}{1+\rho}<bc=b-\lambda.
\]
Once \(u^k=\lambda/\rho\) and \(0<z^k<b-\lambda\), the next threshold input is strictly above \(\lambda/\rho\), so the active sign persists. The ADMM update then reduces exactly to
\[
 z^{k+1}=\frac{b-\lambda+\rho z^k}{1+\rho},\qquad u^{k+1}=\frac\lambda\rho.
\]
Subtracting \(z^*=b-\lambda\) yields
\[
 z^{k+1}-z^*=\frac\rho{1+\rho}(z^k-z^*).
\]
Induction proves the displayed geometric formula for every \(n\ge0\). Since \(0<\rho/(1+\rho)<1\) and \(z^{j_*}-z^*\ne0\), the split variable is unequal to its solution at every finite subsequent iteration. Hence the full ADMM state cannot terminate finitely.

On the active cell, the state map in variables \((z,u)\) has Jacobian
\[
 T'_\rho=\begin{pmatrix}\rho/(1+\rho)&1/(1+\rho)\\0&0\end{pmatrix},
\]
whose eigenvalues are \(\rho/(1+\rho)\) and \(0\). This proves the exact post-identification rate. Also, \(j_*=1\) exactly when \(\rho>\lambda/(b-\lambda)\); at equality the strict threshold makes \(j_*=2\). Thus increasing \(\rho\) can shorten support-identification delay while simultaneously worsening the active linear factor toward \(1\).
## Verification
The proof is symbolic and covers every \(b>\lambda>0\) and finite \(\rho>0\) under the stated initialization. The accompanying `verify.py` uses exact rational arithmetic on several parameter choices to replay the inactive recurrence, the strict threshold index, the active recurrence, and the nontermination witness. Those finite computations are consistency checks, not substitutes for the quantified proof.

For the exact witness \(b=2\), \(\lambda=1\), \(\rho=1\), the first step lands exactly on the soft threshold, so \(z^1=0\). The second step gives \(z^2=1/2\), and thereafter
\[
 z^{2+n}=1-2^{-(n+1)}
\]
for every \(n\ge0\). Thus the iterates converge to \(z^*=1\) but never equal it at a finite index.
## Relationship to prior work
Liang, Fadili, Peyré, and Luke prove finite activity identification for Douglas–Rachford/ADMM under partial smoothness, with identification asserted for sufficiently large iteration index; their result does not give the scalar onset formula above or imply finite convergence of the complete ADMM state. Dohmatob, Eickenberg, Thirion, and Varoquaux give the same standard scaled ADMM update for penalized regression and prove finite support identification. Their Theorem 1(c3) additionally states that, in the anisotropic case and for \(K=I\), the whole algorithm converges in finite time. The scalar recurrence above is an instance of exactly that Lasso setting and shows that this last finite-termination statement is false as written for every finite \(\rho>0\) from the stated zero split/dual initialization.

A later analysis by Liang, Fadili, and Peyré separates finite activity identification and local linear convergence from a finite-convergence result for Douglas–Rachford under additional local hypotheses. That distinction is consistent with the scalar calculation here. The present result therefore sharpens the support-identification picture by giving an exact onset index and isolates a simple penalty tradeoff that is invisible in an asymptotic large-penalty projection approximation.
## Limitations
The result is deliberately one-dimensional: it is a minimal counterexample and an exact timing law, not a classification of multivariate Lasso ADMM. It assumes \(b>\lambda>0\), fixed finite \(\rho>0\), standard unrelaxed scaled ADMM, and \(z^0=u^0=0\). Different initializations can hit the solution exactly, and no claim is made about adaptive or infinite-penalty limits. The literature comparison targets the finite-termination statement as written; an unindexed correction, author note, or thesis could contain the same scalar observation.
## References
1. J. Liang, J. Fadili, G. Peyré, and R. Luke, *Activity Identification and Local Linear Convergence of Douglas–Rachford/ADMM under Partial Smoothness*, arXiv:1412.6858, first public version 2014-12-22.
2. E. Dohmatob, M. Eickenberg, B. Thirion, and G. Varoquaux, *Local Q-Linear Convergence and Finite-time Active Set Identification of ADMM on a Class of Penalized Regression Problems*, ICASSP 2016, DOI: 10.1109/ICASSP.2016.7472579.
3. J. Liang, J. Fadili, and G. Peyré, *Local Convergence Properties of Douglas–Rachford and ADMM*, arXiv:1606.02116, first public version 2016-06-07.
