# Sharp equal-singular-value rank-one Schatten comparison below exponent two

## Finding
For every real exponent \(1<p<2\), let \(\mathcal R_p\) be the supremum of
\[
\frac{\|A+B\|_{S_p}}{\||A|+|B|\|_{S_p}}
\]
over nonzero rank-one complex square matrices \(A,B\) of any common size at least two having **equal** nonzero singular values. Write
\[
\gamma_p=\frac{p}{2-p},\qquad
F_p(u)=\frac{1}{p}\left[\frac p2\log\cosh u+
  \left(1-\frac p2\right)\log\cosh(\gamma_pu)
  -\log\cosh(pu)\right].
\]
There exists exactly one \(u_p>0\) such that
\[
\tanh u_p+\tanh(\gamma_pu_p)=2\tanh(pu_p),
\]
and the **sharp restricted constant** is
\[
\boxed{\mathcal R_p=\exp F_p(u_p)>1.}
\]
Every maximizing pair, after normalization of its singular values, has input-line overlap \(c_p=\tanh u_p\), output-line overlap \(d_p=\tanh(\gamma_pu_p)\), with a phase alignment maximizing the real trace cross term. Conversely every such pair is extremizing. Thus \(0<c_p<d_p<1\). The restricted constant is attained by \(2\times2\) rank-one matrices and is independent of ambient size.

Let \(u_0\) denote the unique positive root of \(u_0\tanh u_0=1\), and put \(\kappa=(u_0^2-1)/2\). Then
\[
\boxed{u_p=u_0-u_0(p-1)+O((p-1)^2),}
\]
\[
\boxed{\mathcal R_p=1+\kappa(p-1)^2-\kappa(p-1)^3+O((p-1)^4)}
\qquad(p\downarrow1),
\]
where \(u_0=1.1996786402577338\ldots\) and \(\kappa=0.2196144199453225\ldots\).
In particular, \(\mathcal R_p\) gives an explicit sharp rank-one *lower bound* for the unrestricted two-summand Schatten comparison constant, whose exact value for \(1<p<2\) is **not** asserted.

## Assumptions and scope
The matrices have complex entries, are square of arbitrary finite order at least two, each has rank exactly one, and have identical positive sole singular value. Scaling both simultaneously does not change the quotient. For \(T\), its modulus is \(|T|=(T^*T)^{1/2}\) and its Schatten norm is the \(\ell_p\)-norm of its singular values. Input and output overlaps are absolute inner products between the corresponding one-dimensional subspaces. All uniqueness claims concern the scalar overlap parameters and aligned relative phase, not unique labeled matrices.

## Proof
**1. Two-Gram reduction.** Scale the common nonzero singular value to one. Express \(A=a\,x^*\) and \(B=b\,y^*\), with all four vectors unit. Set \(c=|\langle x,y\rangle|\in[0,1]\) and \(d=|\langle a,b\rangle|\in[0,1]\). The positive matrix \(|A|+|B|=xx^*+yy^*\) has nonzero eigenvalues \(1+c\) and \(1-c\), including a possible zero endpoint. Thus its Schatten \(p\)-power is \((1+c)^p+(1-c)^p\).

The matrix \((A+B)^*(A+B)\) has at most two nonzero eigenvalues. Their product is \((1-c^2)(1-d^2)\), independent of the relative phase, and their sum is
\[
2+2\operatorname{Re}(\langle a,b\rangle\langle y,x\rangle)\le2+2cd.
\]
At fixed eigenvalue product, the sum of their \(p/2\)-powers strictly increases with their sum when the eigenvalues are not both zero: write the eigenvalues as \(r e^v,r e^{-v}\) and use the monotonicity of \(\cosh(pv/2)\); the zero-product endpoint follows directly. The maximum therefore requires cross-phase alignment whenever \(cd>0\). At alignment, the two squared singular values are \((1+c)(1+d)\) and \((1-c)(1-d)\). Hence every pair is bounded by, and every feasible \(c,d\) attains,
\[
Q_p(c,d)^p=
\frac{(1+c)^{p/2}(1+d)^{p/2}+(1-c)^{p/2}(1-d)^{p/2}}
 {(1+c)^p+(1-c)^p}.
\]
The same formula holds in arbitrary larger dimensions, because the rank-one sum has rank at most two.

**2. Optimal output overlap.** For fixed \(0<c<1\), the numerator is strictly concave as a function of \(d\in[0,1]\) since \(p/2\in(1/2,1)\). Its derivative vanishes exactly at
\[
\left(\frac{1+d}{1-d}\right)^{(2-p)/2}
=\left(\frac{1+c}{1-c}\right)^{p/2},
\qquad d=\tanh\!\left(\gamma_p\operatorname{arctanh}c\right).
\]
This is the unique maximum over \(d\in[0,1]\). Substituting \(c=\tanh u\) gives \(\log\max_d Q_p(c,d)=F_p(u)\). Both endpoint regimes \(c=0\) and \(c=1\) have optimal quotient one. Furthermore \(F_p(0)=0\) and \(\lim_{u\to\infty}F_p(u)=0\).

**3. Exactly one interior global maximum.** Differentiation gives
\[
2F_p'(u)=\tanh u+\tanh(\gamma_pu)-2\tanh(pu).
\]
For \(a=p-1\in(0,1)\), set
\[
L_p(u)=\frac{\sinh(\gamma_p a u)}{\sinh(a u)}
\frac{\cosh u}{\cosh(\gamma_p u)}.
\]
Since \(\gamma_p-p=\gamma_pa\), the sign of \(F_p'(u)\) is exactly the sign of \(L_p(u)-1\). Notice \(L_p(0+)=\gamma_p>1\), while \(L_p(\infty)=0\).

To establish strict monotonicity, introduce \(q(s)=s\coth s\). For \(s>0\), \(q'(s)>0\), and
\[
q''(s)=2\operatorname{csch}^2s\,[s\coth s-1]>0.
\]
Consequently \(q(\gamma_p s)-q(s)\) strictly increases in \(s>0\). Since \(a<1\),
\[
\begin{aligned}
\frac{d}{du}\log L_p(u)
&=\frac{q(\gamma_pau)-q(au)}{u}
   +\tanh u-\gamma_p\tanh(\gamma_pu)\\
&<\gamma_p\coth(\gamma_pu)-\coth u
   +\tanh u-\gamma_p\tanh(\gamma_pu)\\
&=\frac{2\gamma_p}{\sinh(2\gamma_pu)}-\frac2{\sinh(2u)}<0.
\end{aligned}
\]
The last strict inequality follows because \(\sinh s/s\) strictly increases for \(s>0\). Thus \(L_p\) crosses one exactly once. This gives a unique positive critical point \(u_p\), strict increase followed by strict decrease, and hence an attained global optimum greater than one. Strict concavity in step 2 and phase alignment in step 1 give the complete equality classification.

**4. Sharp trace-endpoint expansion.** Set \(\varepsilon=p-1\). For fixed \(u\), a direct fourth-order Taylor expansion (uniform on compact intervals of \(u\)) yields
\[
F_{1+\varepsilon}(u)=\varepsilon^2 H(u)+\varepsilon^3 J(u)+O(\varepsilon^4),
\]
where
\[
H(u)=\tfrac12u^2\operatorname{sech}^2u,
\qquad J(u)=H(u)(1-2u\tanh u).
\]
Since \(H'(u)=u\operatorname{sech}^2u(1-u\tanh u)\), \(H\) has its unique positive maximizer at \(u_0\), where \(u_0\tanh u_0=1\), and \(H(u_0)=\kappa\), \(H''(u_0)=-2\kappa\), \(J(u_0)=-\kappa\), \(J'(u_0)=-2u_0\kappa\).

For completeness, the scalar critical equation can be divided by \(\varepsilon^2\) and expanded locally: near \(\varepsilon=0\) it has the simple root \(u_0\), so the implicit-function theorem gives the unique nearby root \(u_0-J'(u_0)\varepsilon/H''(u_0)+O(\varepsilon^2)=u_0-u_0\varepsilon+O(\varepsilon^2)\). To identify it with the global \(u_p\), the strict decrease of \(L_p\) from step 3, together with the sign of \(H'\) on fixed points on both sides of \(u_0\), traps the unique root in every neighborhood of \(u_0\) as \(\varepsilon\downarrow0\). Substitution gives \(\log\mathcal R_p=\kappa\varepsilon^2-\kappa\varepsilon^3+O(\varepsilon^4)\). Exponentiating yields the displayed expansion.

## Verification
The standalone file `checker.py` uses only the Python standard library. Running `python checker.py` executes 2,991 deterministic assertions. These compare the two-by-two singular-value calculation with the Gram formula, verify scalar derivative roots and bounded-grid maximization, check stationary choices against randomized overlap pairs, and test convergence of the trace-endpoint coefficients. The exact root uniqueness and asymptotic quantifiers follow from the preceding proof, not from finite checks.

## Relationship to prior work
Tang and Zhang initiated the multi-summand quasi-reverse Minkowski Schatten constant problem and proposed an all-exponent sharp formula [1]. Pang, Zeng–Liu–Ratnavelu and Qiu established counterexamples to that proposed formula below exponent two [2–4]. In particular, Qiu's rank-one calculation reduces the problem to two overlap variables and optimizes one variable [4]. The contribution here is **the remaining global optimization**, proof of a **unique full interior extremizer at every exponent** in the equal-singular-value rank-one subfamily, and the **sharp second- and third-order trace-endpoint behavior**. These are a restricted-family statement and an unrestricted lower bound, not a determination of the unrestricted comparison constant. Teng Zhang's matrix norm bounds [5] supply distinct general estimates rather than the restricted exact optimum.

## Limitations
Equal nonzero singular values and rank-one summands are essential hypotheses. Nothing here establishes the unrestricted sharp two-summand constant for \(1<p<2\), nor the optimal constant with more than two summands, non-rank-one summands, or unequal singular values. The results are finite-dimensional (dimension-free through rank reduction). Publication priority has not been independently certified; an equivalent optimization under alternate matrix norm terminology cannot be ruled out completely. The checker is diagnostic, not a formal proof or independent mathematical audit.

## References
[1] Q. Tang and S. Zhang, *Generalizing Lee's conjecture on the sum of absolute values of matrices*, arXiv:2510.16846, first submitted 2025-10-19.

[2] Z. Pang, *Counterexamples to a conjectured Schatten norm inequality*, arXiv:2608.18112.

[3] Z. Zeng, H. Liu, and K. Ratnavelu, *A Counterexample to the Tang Zhang Schatten Norm Conjecture and Sharp Positive Results*, arXiv:2608.15558.

[4] H. Qiu, *Sharp Quasi-Reverse Minkowski Inequality for Schatten Norms*, arXiv:2608.17565, first submitted 2026-08-18.

[5] T. Zhang, *Operator symmetric moduli and sharp triangle inequalities*, arXiv:2603.01046.
