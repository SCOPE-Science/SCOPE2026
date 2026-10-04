# Critical-damping penalty for symmetric three-block ADMM
## Finding
Consider the equality-constrained three-block quadratic
\[
\min_{x_1,x_2,x_3\in\mathbb R} \frac{a}2\left(x_1^2+x_2^2+x_3^2\right)
\quad\text{subject to}\quad x_1+x_2+x_3=0,
\]
with \(a>0\). Apply the standard direct three-block ADMM, updating \(x_1,x_2,x_3\) successively and then the multiplier, with penalty \(\rho>0\). Define
\[
t=\frac{\rho}{a+\rho}\in(0,1).
\]
The exact asymptotic spectral radius has a unique minimizer. Let \(t_*\) be the unique root in \((0,1)\) of
\[
4t^4-16t^3+12t^2-4t+1=0.
\]
Then
\[
t_*=0.5947955253657324076\ldots,
\qquad
\rho_*=a\frac{t_*}{1-t_*}=1.4678898250138705587\ldots a,
\]
and the sharp convergence factor is
\[
\rho_{\mathrm{spec},*}=t_*^{3/2}=0.4587240807118043076\ldots.
\]
For penalties below \(\rho_*\), the two active eigenvalues are positive and real and the dominant one strictly decreases as \(\rho\) increases. At \(\rho_*\) they merge into a repeated positive root. Above \(\rho_*\) they form a complex-conjugate pair whose common modulus increases with \(\rho\). Thus the unique rate optimum is exactly the real-to-complex critical-damping transition.

## Assumptions and scope
The claim concerns the unmodified direct Gauss--Seidel three-block ADMM for the displayed scalar, symmetric, strongly convex quadratic. The multiplier convention is
\[
\lambda^{k+1}=\lambda^k-\rho\left(x_1^{k+1}+x_2^{k+1}+x_3^{k+1}\right).
\]
Writing \(u^k=-\lambda^k/\rho\) converts this to the scaled update \(u^{k+1}=u^k+x_1^{k+1}+x_2^{k+1}+x_3^{k+1}\). No claim is made for unequal curvatures, nonscalar blocks, over-relaxed multiplier steps, randomized block orders, or proximal modifications.

## Proof
The three primal minimizations give
\[
\begin{aligned}
x_1^{k+1}&=-t\left(x_2^k+x_3^k+u^k\right),\\
x_2^{k+1}&=-t\left(x_1^{k+1}+x_3^k+u^k\right),\\
x_3^{k+1}&=-t\left(x_1^{k+1}+x_2^{k+1}+u^k\right).
\end{aligned}
\]
Eliminating \(x_1^{k+1}\) yields a closed recurrence for \(s^k=(x_2^k,x_3^k,u^k)^\top\):
\[
s^{k+1}=M(t)s^k,
\]
where
\[
M(t)=\begin{pmatrix}
t^2&t^2-t&t^2-t\\
-t^3+t^2&-t^3+2t^2&-t^3+2t^2-t\\
-t^3+2t^2-t&-t^3+3t^2-2t&-t^3+3t^2-3t+1
\end{pmatrix}.
\]
Direct expansion gives
\[
\det(\lambda I-M(t))
=\lambda\left(\lambda^2+A(t)\lambda+t^3\right),
\qquad
A(t)=2t^3-6t^2+3t-1.
\]
The maximum of \(A\) on \([0,1]\) occurs at \(t=1-1/\sqrt2\) and equals \(-2+\sqrt2<0\), so whenever the quadratic roots are real they are positive. Its discriminant factors as
\[
\Delta(t)=A(t)^2-4t^3=(1-t)^2P(t),
\]
with
\[
P(t)=4t^4-16t^3+12t^2-4t+1.
\]
A Sturm chain, up to positive scalar multiples, is
\[
\frac14P(t),\quad 4t^3-12t^2+6t-1,\quad \frac34t(2t-1),\quad 1-t,\quad -\frac34.
\]
The one-sided sign patterns at \(0\) and \(1\) have respectively three and two variations. Hence \(P\) has exactly one root \(t_*\) in \((0,1)\). Since \(P(0)>0\) and \(P(1)<0\), the active roots are real on \((0,t_*)\) and nonreal conjugates on \((t_*,1)\).

On \((t_*,1)\), their product is \(t^3\), so each has modulus \(t^{3/2}\), strictly increasing in \(t\). On \((0,t_*)\), let \(q(t)\) be the larger root. Then
\[
q'(t)=-\frac{A'(t)q(t)+3t^2}{2q(t)+A(t)}
=-\frac{A'(t)q(t)+3t^2}{\sqrt{\Delta(t)}}.
\]
Any stationary point with \(A'(t)\ne0\) must satisfy \(q=-3t^2/A'(t)\). Substitution into the quadratic equation gives exactly
\[
\left(\frac{-3t^2}{A'(t)}\right)^2
+A(t)\left(\frac{-3t^2}{A'(t)}\right)+t^3
=
\frac{t^2(t-1)^2(2t-1)^2}{(2t^2-4t+1)^2}.
\]
Thus the only stationary point in \((0,t_*)\) is \(t=1/2\); direct sign evaluation on either side shows \(q'(t)<0\), while \(q'(1/2)=0\). Therefore \(q\) is strictly decreasing on \((0,t_*)\). The decreasing real-root branch and increasing complex-modulus branch meet at \(t_*\), where the quadratic has the repeated root \(t_*^{3/2}\). This proves uniqueness of the stated optimum. Finally, \(\rho=a t/(1-t)\) is strictly increasing in \(t\), so the same optimizer transfers to the penalty parameter.

## Verification
The accompanying `verify.py` uses exact rational arithmetic to check the reduced matrix characteristic polynomial at enough rational parameter values to determine its coefficient identities, verifies the discriminant and stationary-point polynomial identities, checks the Sturm sign-variation count, and isolates the unique root \(t_*\) by high-precision decimal bisection. It then reproduces the numerical values of \(t_*\), \(\rho_*/a\), and \(t_*^{3/2}\). These computations support the algebraic proof; the proof does not rely on finite sampling for the infinite-parameter statement.

## Relationship to prior work
Chen, Shen, and You study the same direct three-block ADMM framework and prove convergence under penalty restrictions; their additional “optimal step size” belongs to a relaxed predictor-corrector variant, not to optimization of the penalty parameter of the unmodified direct iteration. Lin, Ma, and Zhang prove global linear convergence of standard multiblock ADMM under several scenarios and explicitly write the Gauss--Seidel multiblock recurrence; their illustrative experiment selects a penalty near a sufficient upper bound rather than minimizing an exact spectral radius. The later paper of Ke, Ma, and Zhang treats general three-block separable quadratic programs from a matrix-computation viewpoint, so it is the closest structural comparison. Its accessible abstract and introduction establish the general class and iteration but do not state the scalar symmetric penalty optimizer above; full later pages were not available through the lawful access routes checked here, which remains an originality risk rather than evidence of noncoverage.

## Limitations
The result is exact only for three identical scalar quadratic blocks with one scalar sum constraint and the standard multiplier step. A later inaccessible portion of the 2018 quadratic-programming paper could contain an implication-equivalent specialization; that risk is recorded in the review. The calculation does not establish optimal tuning for general three-block quadratic programs, and the repeated-root optimum is an asymptotic spectral statement rather than a finite-iteration monotonicity guarantee in every norm.

## References
1. C. Chen, Y. Shen, and Y. You, “On the Convergence Analysis of the Alternating Direction Method of Multipliers with Three Blocks,” *Abstract and Applied Analysis* 2013, Article 183961. DOI 10.1155/2013/183961. First published 26 October 2013.
2. T. Lin, S. Ma, and S. Zhang, “On the Global Linear Convergence of the ADMM with Multi-Block Variables,” arXiv:1408.4266; *SIAM Journal on Optimization* 25 (2015), 1478–1497. DOI 10.1137/140971178.
3. Y. Ke, C. Ma, and H. Zhang, “Convergence of ADMM for Three-Block Separable Quadratic Programming Problems with Linear Constraints,” *East Asian Journal on Applied Mathematics* 8 (2018), 498–509. DOI 10.4208/eajam.240817.010318.
