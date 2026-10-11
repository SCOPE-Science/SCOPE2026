# Sharp energy-norm stability for two-periodic recurrences

## Finding
Let \(a,b\in\mathbb C\). On \(\ell_2(\mathbb Z;\mathbb C)\), define the two-periodic first-difference operator
\[
(L_{a,b}x)_n=x_{n+1}-a_nx_n,\qquad a_{2k}=a,\quad a_{2k+1}=b.
\]
Put \(r=|ab|\), \(S=2+|a|^2+|b|^2\), and \(\delta=|r-1|\). The operator is boundedly invertible exactly when \(\delta>0\), and its exact inverse norm is
\[
\boxed{\|L_{a,b}^{-1}\|=K(a,b)=\frac{\sqrt{S+\sqrt{S^2-4\delta^2}}}{\sqrt2\,\delta}.}
\]
For every \(g,y\in\ell_2(\mathbb Z)\) with \(\delta>0\), there is a unique \(x\in\ell_2(\mathbb Z)\) satisfying \(L_{a,b}x=g\); the smallest uniform residual-error constant is exactly \(K(a,b)\):
\[
\|x-y\|_2\le K(a,b)\|L_{a,b}y-g\|_2.
\]
If \(r=1\), no finite universal constant exists, even for homogeneous forcing \(g=0\).

At fixed \(r>0\), \(r\ne1\), the optimal constant is uniquely minimized (as a function of coefficient moduli) by \(|a|=|b|=\sqrt r\); it then equals \(1/|\sqrt r-1|\). Holding \(r\) fixed while the moduli become increasingly unequal makes \(K(a,b)\) arbitrarily large. A nonzero residual realizes equality in the sharp estimate if and only if \(ab=0\); otherwise extremizing residual sequences exist but no nonzero extremizer does.

## Assumptions and scope
All sequences are indexed by all integers, not by a half-line, and stability is measured in the global Hilbert energy norm \(\ell_2\), not the pointwise supremum norm. Complex coefficients are unrestricted, including zero. The same numerical operator norm and assertions hold for real coefficients on the real sequence space by equality of real Hilbert-operator norms and their complexifications. The normalization has unit forward shift and no step-size multiplier. The statement does not concern pointwise Ulam stability on nonnegative indices.

## Proof
**Fiberization.** Group parity by setting \(u_k=x_{2k}\) and \(v_k=x_{2k+1}\). This is a unitary identification with \(\ell_2(\mathbb Z;\mathbb C^2)\). Apply its Fourier transform, with \(z\) on the unit circle. Because
\[
(Lx)_{2k}=v_k-au_k,\qquad (Lx)_{2k+1}=u_{k+1}-bv_k,
\]
\(L\) becomes multiplication by the continuous matrix symbol
\[
A(z)=\begin{pmatrix}-a&1\\z&-b\end{pmatrix},\qquad |z|=1.
\]
The characteristic roots of the positive Hermitian matrix \(A(z)^*A(z)\) are
\[
\lambda_\pm(z)=\frac{S\pm\sqrt{S^2-4|ab-z|^2}}2,
\]
since its trace is \(S\) and its determinant is \(|ab-z|^2\). The square root is real because these are actual singular-value squares.

**Sharp inverse bound.** On the unit circle, \(\min_{|z|=1}|ab-z|=||ab|-1|=\delta\). The least singular value of \(A(z)\) is minimized at that distance. If \(\delta>0\), the inverse matrix field is continuous and uniformly bounded. Its multiplication-operator norm is its essential-supremum norm, which, by continuity, is its maximum. Rationalization gives
\[
\|L^{-1}\|^2=\frac{S+\sqrt{S^2-4\delta^2}}{2\delta^2}.
\]
For \(x=L^{-1}g\), one has \(x-y=-L^{-1}(Ly-g)\), proving the residual estimate and its optimality. Concentrating normalized Fourier data on successively smaller arcs near the minimizing phase makes the quotient tend to the asserted constant.

If \(\delta=0\), then \(ab\) lies on the unit circle and \(A(ab)\) is singular. Its zero eigenvalue occurs at only one point of the circle. Hence the multiplication operator has trivial kernel on \(\ell_2\) but is not bounded below: choose Fourier data supported on narrowing arcs and nearly in its zero-singular direction. Thus a uniform correction inequality cannot hold.

**Fixed Floquet-product profile.** For fixed \(r>0\), \(\delta>0\), the displayed formula is strictly increasing as a function of \(S\). The arithmetic-geometric mean inequality gives \(|a|^2+|b|^2\ge2|ab|=2r\), with equality precisely when \(|a|=|b|=\sqrt r\). The equality-case symbol has constant coefficient moduli and \(S=2+2r\), giving \(K=1/|\sqrt r-1|\). As \(|a|\to\infty\) and \(|b|=r/|a|\), \(S\to\infty\), so \(K\to\infty\). In fact \(K\sim\max\{|a|,|b|\}/\delta\) in that limit.

**Equality versus approximation.** If \(ab\ne0\), the minimizing phase \(z=ab/|ab|\) is the unique point where the fiber inverse norm reaches its maximum. That singleton has zero Haar measure, so no nonzero \(L^2\) Fourier field can attain the multiplication-operator norm. If \(ab=0\), \(|ab-z|=1\) for every unit \(z\), so the largest singular value of \(A(z)^{-1}\) is constant almost everywhere. A measurable unit singular-vector field multiplied by a nonzero square-integrable scalar gives an actual extremizer. This completes the classification.

## Verification
Run `python verify.py` in an environment with Python 3 and NumPy. The deterministic verifier tests finite circular approximations and direct singular values of the two-by-two symbol against the analytic formula; the captured run completed 6,746 checks. Such tests are finite corroboration, not an infinite-dimensional proof. The preceding fiberization and singular-value argument establish the exact theorem without computational assumptions.

For example, \((|a|,|b|)=(2,2)\) gives \(K=1\), whereas \((8,1/2)\) has the same two-step product modulus \(4\) but \(K\approx2.710347891355\). This demonstrates sharp sensitivity to within-period imbalance despite identical Floquet multiplier magnitude.

## Relationship to prior work
Xu and Brzdęk (2015) establish Hyers–Ulam stability for first-order recurrences with **constant** matrix coefficients and pointwise bounded-error norms; their statement does not give a sharp two-periodic bilateral \(\ell_2\) inverse norm. Jung (2015) studies constant-matrix difference equations on integer indices using pointwise bounds. Anderson, Onitsuka, and Rassias (2020) give periodic-coefficient stability bounds on the **nonnegative** grid under **uniform pointwise** residual and error control, including a sharp constant in the growing-product regime. Their period-two formula depends on the coefficient magnitudes via a maximum of linear expressions, rather than the Hilbert-space singular-value expression here. Its overlap in stability threshold does not imply the present energy-norm constant, fixed-product minimum, or nonattainment classification. Fourier block decomposition and singular-value calculus are classical methods; the claim is the exact quantified energy stability profile for this recurrence, not invention of those methods.

## Limitations
The result is restricted to the first-order bilateral two-periodic scalar recurrence and the \(\ell_2\) error norm. It does not assert pointwise Ulam constants, finite-interval constants, or optimal profiles for longer periods. It is not an independent bibliographic certification: an equivalent formula may exist in general weighted-shift resolvent literature under another name. Nonattainment refers to a nonzero residual in the Hilbert space, not to formal Bloch waves or finite cyclic approximants.

## References
1. B. Xu and J. Brzdęk, “Hyers-Ulam Stability of a System of First Order Linear Recurrences with Constant Coefficients,” *Discrete Dynamics in Nature and Society* (2015), DOI 10.1155/2015/269356. First public version verified 2015-03-02.
2. S.-M. Jung, “Hyers-Ulam stability of the first-order matrix difference equations,” *Advances in Difference Equations* (2015), DOI 10.1186/s13662-015-0507-6. Published 2015-06-05.
3. D. R. Anderson, M. Onitsuka and J. M. Rassias, “Best constant for Ulam stability of first-order h-difference equations with periodic coefficient,” arXiv:2004.03465v1 (submitted 2020-04-06), especially Sections 2 and 4.
