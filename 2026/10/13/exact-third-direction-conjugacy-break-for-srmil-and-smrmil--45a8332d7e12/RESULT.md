# Exact third-direction conjugacy break for SRMIL and SMRMIL
## Finding
For the SRMIL and SMRMIL methods introduced by Cai, Yue, and Mo, exact line search makes the RMIL and MRMIL coefficients coincide and removes the spectral correction in the sufficient-descent direction. On every strictly convex quadratic
\[
f(x)=\tfrac12 x^{\mathsf T}Ax-b^{\mathsf T}x,\qquad A\succ0,
\]
the resulting recurrence is
\[
d_0=-g_0,\qquad d_{k+1}=-g_{k+1}+\beta_{k+1}d_k,
\qquad
\beta_{k+1}=\frac{g_{k+1}^{\mathsf T}(g_{k+1}-g_k)}{\lVert d_k\rVert^2}.
\]
If \(g_1\ne0\) and \(g_2\ne0\), then \(d_0\) and \(d_1\) are \(A\)-conjugate, but the next pair is never \(A\)-conjugate. In fact,
\[
d_2^{\mathsf T}Ad_1=(d_1^{\mathsf T}Ad_1)\lVert g_2\rVert^2
\left(\frac1{\lVert d_1\rVert^2}-\frac1{\lVert g_1\rVert^2}\right)<0.
\]
Thus dimensions one and two still terminate in at most their dimension many exact line searches, whereas dimension three is the smallest dimension in which the method can fail the classical finite-termination property. The exact witness
\[
A=\operatorname{diag}(1,2,3),\qquad b=0,\qquad x_0=(1,1,1)^{\mathsf T}
\]
has
\[
d_2^{\mathsf T}Ad_1=-\frac{38}{4067}
\]
and after the third exact line search
\[
g_3=\frac1{9769349}(32871,52536,-45981)^{\mathsf T}\ne0.
\]

## Assumptions and scope
The statement concerns exact arithmetic, symmetric positive definite \(A\), and exact line search for the exact-line branch of SRMIL/SMRMIL. The source indexes its first direction by one; indices are shifted here so that the initial direction is \(d_0=-g_0\). The strict conjugacy defect requires that the problem has not already been solved after either of the first two searches, namely \(g_1\ne0\) and \(g_2\ne0\).

The finding does not claim that SRMIL or SMRMIL fails global convergence under the Wolfe or Armijo searches analyzed in the source. It isolates the exact-line quadratic structure inherited from RMIL/MRMIL.

## Proof
Exact line search gives \(g_{k+1}^{\mathsf T}d_k=0\). Hence the extra factor in the source sufficient-descent direction equals one, and the source RMIL and MRMIL coefficients agree. At the first step, \(d_0=-g_0\), so \(g_1^{\mathsf T}g_0=0\) and
\[
\beta_1=\frac{\lVert g_1\rVert^2}{\lVert g_0\rVert^2}.
\]
Writing \(g_1-g_0=\alpha_0Ad_0\), we have
\[
d_1^{\mathsf T}Ad_0
=\frac1{\alpha_0}
\left[-g_1^{\mathsf T}(g_1-g_0)+\beta_1d_0^{\mathsf T}(g_1-g_0)\right]=0.
\]
Thus the first two search directions are \(A\)-conjugate.

After the second exact line search, \(g_2^{\mathsf T}d_1=0\). Since \(g_2-g_1=\alpha_1Ad_1\) and \(d_0^{\mathsf T}Ad_1=0\), while \(d_0^{\mathsf T}g_1=0\), it follows that \(d_0^{\mathsf T}g_2=0\). From \(d_1=-g_1+\beta_1d_0\) we then obtain \(g_2^{\mathsf T}g_1=0\). Therefore
\[
\beta_2=\frac{\lVert g_2\rVert^2}{\lVert d_1\rVert^2}.
\]
Moreover, exact line search and \(g_2-g_1=\alpha_1Ad_1\) give
\[
\alpha_1d_1^{\mathsf T}Ad_1=\lVert g_1\rVert^2,
\qquad
g_2^{\mathsf T}Ad_1=\frac{\lVert g_2\rVert^2}{\alpha_1}.
\]
Substituting these identities into \(d_2=-g_2+\beta_2d_1\) yields
\[
d_2^{\mathsf T}Ad_1=(d_1^{\mathsf T}Ad_1)\lVert g_2\rVert^2
\left(\frac1{\lVert d_1\rVert^2}-\frac1{\lVert g_1\rVert^2}\right).
\]
Finally, \(g_1\perp d_0\) and \(d_1=-g_1+\beta_1d_0\) imply
\[
\lVert d_1\rVert^2=\lVert g_1\rVert^2+\beta_1^2\lVert d_0\rVert^2>\lVert g_1\rVert^2
\]
when \(g_1\ne0\). With \(A\succ0\) and \(g_2\ne0\), every remaining factor is positive, proving the strict negative defect.

In one dimension the first exact line search solves the problem. In two dimensions, if the first line search does not already solve it, the two nonzero \(A\)-conjugate directions \(d_0,d_1\) form a basis; exact minimization along them therefore reaches the minimizer after the second search. The displayed three-dimensional witness remains nonstationary after its third exact line search, establishing minimality.

## Verification
The accompanying `verify.py` uses exact rational arithmetic. It reconstructs the three-dimensional witness, verifies the first two exact step lengths and coefficients, checks \(d_1^{\mathsf T}Ad_0=0\), checks \(d_2^{\mathsf T}Ad_1=-38/4067\), performs the third exact line search, and verifies
\[
\lVert g_3\rVert^2=\frac{5954786298}{95440179883801}>0.
\]
The universal inequality is analytic and does not rely on this finite computation.

## Relationship to prior work
Cai--Yue--Mo define the RMIL coefficient with denominator \(\lVert d_{k-1}\rVert^2\), define the sufficient-descent spectral direction, and state that under exact line search their SRMIL and SMRMIL constructions reduce to RMIL and that RMIL/MRMIL coincide. Their paper proves descent and global convergence properties but does not state the exact third-direction \(A\)-conjugacy defect or a minimal-dimension finite-termination result.

Classical linear and nonlinear conjugate-gradient theory supplies the comparator: the standard HS, FR, PRP, and DY formulas coincide on strictly convex quadratics under exact line search and generate the familiar conjugate-direction finite-termination mechanism. A later 2026 RMIL paper by Salihu, Kumam, Ibrahim, and Phiangsungnoen explicitly motivates revised spectral parameters by conjugacy conditions, so the broad issue that RMIL variants may not encode the desired conjugacy structure is prior motivation. Its inspected full text develops revised parameters, descent, global convergence, and numerical tests; it does not give the exact universal defect above, the dimension-two termination statement, or the three-dimensional exact witness.

## Limitations
The theorem is about the exact-line branch. It does not rank practical performance under inexact Wolfe or Armijo searches, and it does not assert divergence. Loss of \(A\)-conjugacy does not by itself imply failure on every three-dimensional quadratic; the explicit witness proves that dimension-step termination can fail and that dimension three is minimal for such failure.

A specialized older source could contain the same finite-termination observation under different terminology. Targeted searches for RMIL, exact line search, conjugacy, quadratic finite termination, and the denominator \(\lVert d_k\rVert^2\) did not locate an implication-equivalent statement.

## References
1. Yu Cai, Hong Yue, Chenyun Mo, *Applications of two sufficient descent spectral conjugate gradient methods in image denoising*, AIMS Mathematics 11 (2026), 8635--8654, DOI: 10.3934/math.2026355.
2. Nasiru Salihu, Poom Kumam, Sulaiman Mohammed Ibrahim, Supak Phiangsungnoen, *An Adaptive Spectral Conjugate Gradient Method With Integrated Conjugacy Conditions and Its Application*, Mathematical Methods in the Applied Sciences 49 (2026), 16163--16183, DOI: 10.1002/mma.70858.
3. M. Rivaie, M. Mamat, L. W. June, M. Ismail, *A new class of nonlinear conjugate gradient coefficients with global convergence properties*, Applied Mathematics and Computation 218 (2012), 11323--11332, DOI: 10.1016/j.amc.2012.05.030.
4. M. Rivaie, M. Mamat, A. Abashar, *A new class of nonlinear conjugate gradient coefficients with exact and inexact line searches*, Applied Mathematics and Computation 268 (2015), 1152--1163, DOI: 10.1016/j.amc.2015.07.019.
