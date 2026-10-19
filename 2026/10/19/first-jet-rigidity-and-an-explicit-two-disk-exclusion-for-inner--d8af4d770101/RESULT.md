# First-jet rigidity and an explicit two-disk exclusion for inner Hardy \(H^4\) approximants

## Finding
Let \(f\) be an inner function on the unit disk, and let \(q\) be the unique polynomial of degree at most one minimizing \(\|1-fq\|_{H^4}\). The entire optimization problem, its minimum value and its unique minimizer depend only on \(f(0)\) and \(f'(0)\). Moreover, if \(q\) has degree one, its unique zero \(w\) satisfies the explicit **strict** bound \(|w|>2\). Thus all degree-one optimal approximants for all inner functions are zero-free in the closed radius-two disk. Neither the bound nor its optimality is asserted to be sharp.

## Assumptions and scope
An inner function is a bounded analytic function on the open unit disk whose radial boundary values have modulus one almost everywhere. Normalize the Hardy norm by \(\|g\|_{H^4}^4=(2\pi)^{-1}\int_0^{2\pi}|g(e^{it})|^4dt\). The zero assertion concerns a nonconstant optimal polynomial. For \(f(0)=0\), the optimizer is zero; for \(f'(0)=0\) or \(f\) constant, the optimizer has degree zero. In the nonconstant case with \(f(0)\ne0\) and \(f'(0)\ne0\), the optimizer has degree one.

## Proof
Write \(q(z)=A+Bz\), \(c=f(0)\), and \(d=f'(0)\). Since \(|f|=1\) almost everywhere on the boundary, direct multiplication of \((1-fq)^2(1-\overline{fq})^2\), followed by extracting the constant Laurent coefficient, yields the **exact** quartic objective
\[
\begin{aligned}
\|1-fq\|_4^4={}&1+4(|A|^2+|B|^2)+|A|^4+4|AB|^2+|B|^4\\
&-4\operatorname{Re}(cA)-4\operatorname{Re}\big(cA(|A|^2+2|B|^2)+dA^2\overline B\big)
+2\operatorname{Re}(c^2A^2).
\end{aligned}
\]
This identity proves the first-jet assertion for the objective. Since \(q\mapsto fq\) is injective and the \(L^4\) norm is strictly convex, the minimizer exists uniquely, hence also depends only on \((c,d)\).

If \(c=0\), every \(fq\) has zero constant term and the mean-value inequality \(\|1-fq\|_4\ge |(1-fq)(0)|=1\) gives the unique minimizer \(q=0\). If \(c\ne0\), multiply \(f\) by a unimodular constant and rotate its argument to arrange \(c=u\in(0,1)\) and \(d=v\in[0,1-u^2]\). These changes preserve the modulus of the zero of the optimal polynomial. The upper bound on \(v\) is the Schwarz–Pick derivative bound. The endpoint \(u=1\) makes \(f\) constant.

Conjugation invariance of the displayed quartic and uniqueness force the optimizing \(A=a\) and \(B=b\) to be real. At \(a=0\), the partial derivative in \(a\) is \(-4u(1+2b^2)<0\), so \(a>0\). If \(v=0\), uniqueness and invariance under rotations of \(B\) give \(b=0\). If \(v>0\), the objective is smaller at \(b\) than at \(-b\) for \(b>0\), and its partial derivative at \(b=0\) equals \(-4va^2<0\); hence the minimizer has \(b>0\).

For real \(a,b\), denote the displayed quartic by \(F(a,b)\). Its derivative at \(a=1\) has the exact decomposition
\[
\partial_aF(1,b)= (1-u)\left[2(1-u)(5+u)+8\left(b-\frac{1+u}{2}\right)^2\right]
+8b(1-u^2-v)>0.
\]
As \(F\) is strictly convex separately in \(a\), this implies \(0<a<1\) at the minimizer. The other stationarity equation is
\[
b\,[2(1-u^2)+2(a-u)^2+b^2]=va^2.
\]
Since \(0<v\le1-u^2\), its positive solution satisfies \(0<b<a^2/2\). Hence the zero of \(q(z)=a+bz\) obeys
\[
|w|=a/b>2/a>2.
\]
This exhausts the cases.

## Verification
The accompanying `verify.py` uses symbolic differentiation to check the stationarity identity and the exact positive decomposition of \(\partial_aF(1,b)\). It evaluates the quartic both by its closed formula and by Fourier-grid integration for two distinct finite Blaschke products with the same \((c,d)\), and computes sample minimizers. The symbolic checks validate algebra only; the infinite-family conclusion follows from the analytic proof, not from the finite samples. Reproduce with `python verify.py` using SymPy, NumPy and SciPy.

## Relationship to prior work
Centner–Cheng–Felder's 2023 paper *Optimal Polynomial Approximants in \(H^p\)* (arXiv:2305.16068v1, Theorem 5.13) proves existence of a positive inner-function-dependent-exponent root exclusion constant, but does not specify radius two or the first-jet identity. Cheng–Felder (arXiv:2310.16010v1, Section 3.2) examines global possible OPA roots and Section 3.3 presents fixed-point iteration, not this explicit inner \(H^4\) uniform bound. Bénéteau et al. (arXiv:2511.08000v1, Section 4.1) give root estimates through approximation errors and inner factors; these do not imply a uniform disk of radius two for degree-one inner \(H^4\) approximants. Earlier \(H^2\) inner results are linear projections and do not imply the \(H^4\) quartic assertion.

## Limitations
The number two is a rigorously valid exclusion radius, not a claimed best constant. Nothing is claimed for general non-inner \(f\), for degrees above one, or for exponents other than four. The finite tests do not certify an optimal radius. The literature assessment is best-knowledge and does not constitute an independent priority certification.

## References
- R. Centner, R. Cheng, C. Felder, *Optimal Polynomial Approximants in \(H^p\)*, arXiv:2305.16068v1, first posted 2023-05-25, especially Theorem 5.13. https://arxiv.org/abs/2305.16068
- R. Cheng, C. Felder, *More properties of optimal polynomial approximants in Hardy spaces*, arXiv:2310.16010v1, first posted 2023-10-24, Sections 3.2–3.3. https://arxiv.org/abs/2310.16010
- C. Bénéteau et al., *Metric projections, zeros of optimal polynomial approximants, and some extremal problems in Hardy spaces*, arXiv:2511.08000v1, first posted 2025-11-11, Section 4.1. https://arxiv.org/abs/2511.08000
