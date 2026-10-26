# Sharp finite-jet completeness and false rank plateaux for quadratic-penciled solution families

## Finding
Let \(n\geq1\), let \(P(z)=A_0+zA_1+z^2A_2\) be a regular \(n\times n\) matrix polynomial over \(\mathbb F\in\{\mathbb R,\mathbb C\}\), let \(b\in\mathbb F^n\), and let \(\xi\ne0\) satisfy \(\det P(\xi)\ne0\). Define \(x(z)=zP(z)^{-1}b\), and let \(\mathcal S\) be the span of the solution vectors on any nonempty open parameter neighborhood of \(\xi\) on which the pencil is invertible. Then

\[
\mathcal S=\operatorname{span}\{x(\xi),x'(\xi),\ldots,x^{(2n-2)}(\xi)\}.
\]

The bound \(2n-2\) is **universally sharp**, even for real diagonal pencils that are symmetric positive definite for every real parameter. For any \(n\ge2\) and real \(\xi>0\), take \(K=\operatorname{diag}(1,2,\ldots,n)\), \(b=(1,\ldots,1)^T\), and

\[
P(z)=I+(z-\xi)^2K.
\]

For this family, with \(\mathcal V_m=\operatorname{span}\{x^{(j)}(\xi):0\le j\le m\}\), the exact jet-rank staircase is

\[
\dim\mathcal V_m=\min\{n,1+\lfloor m/2\rfloor\}\quad(m\ge0).
\]

Hence orders \(1,3,5,\ldots\) add no new direction, while the even order \(2n-2\) is necessary for a complete solution subspace. A single rank plateau therefore does not certify completeness.

## Assumptions and scope
All linear spans are over \(\mathbb F\). In the real case take \(\xi\in\mathbb R\setminus\{0\}\); in the complex case \(\xi\in\mathbb C\setminus\{0\}\). "Regular" means \(\det P\) is not the zero polynomial. The neighborhood can be any open real interval or complex disk containing \(\xi\), sufficiently small that \(P(z)\) remains invertible. Equality of solution spans also holds over any larger invertibility domain. The result concerns exact algebraic spans, not floating-point termination, error tolerance, condition numbers, or optimal reduced-model dimensions under approximation.

## Proof
Put \(q(z)=\det P(z)\) and \(p(z)=\operatorname{adj}(P(z))b\). Every coordinate of \(p\) is a sum of determinants of \((n-1)\times(n-1)\) submatrices, so \(\deg p_i\le2(n-1)\). The adjugate identity gives \(x(z)=zp(z)/q(z)\) wherever \(q(z)\ne0\). Write \(M=2n-2\).

Each derivative \(x^{(j)}(\xi)\) lies in the finite-dimensional span \(\mathcal S\): divided differences formed from values in any neighborhood converge to that derivative, and a finite-dimensional subspace is closed. Thus \(\mathcal V_M\subseteq\mathcal S\).

For the reverse inclusion, let a linear functional \(\ell:\mathbb F^n\to\mathbb F\) vanish on \(\mathcal V_M\). The analytic scalar function \(\ell(x(z))=z\ell(p(z))/q(z)\) then has a zero of order at least \(M+1=2n-1\) at \(\xi\). Since \(\xi\ne0\) and \(q(\xi)\ne0\), the polynomial \(\ell(p(z))\) also has a zero there of order at least \(2n-1\). Its degree is at most \(2n-2\); hence it vanishes identically. Consequently \(\ell(x(z))=0\) at every nonsingular parameter, and \(\ell\) annihilates \(\mathcal S\). Finite-dimensional annihilator duality proves \(\mathcal S\subseteq\mathcal V_M\), hence equality. For \(n=1\) the same argument yields \(M=0\).

To prove sharpness, fix real \(\xi>0\) and the diagonal example in the Finding. Set \(t=z-\xi\). For \(|t|<1/\sqrt n\), the convergent expansion is

\[
P(\xi+t)^{-1}b=\sum_{j=0}^\infty(-1)^jt^{2j}K^jb,
\qquad x(\xi+t)=(\xi+t)\sum_{j=0}^\infty(-1)^jt^{2j}K^jb.
\]

Thus, for each \(j\ge0\), the Taylor coefficients at orders \(2j\) and \(2j+1\) are respectively \(\xi(-1)^jK^jb\) and \((-1)^jK^jb\). Taylor coefficients and derivatives differ by nonzero factorials, so \(\mathcal V_m=\operatorname{span}\{b,Kb,\ldots,K^{\lfloor m/2\rfloor}b\}\). The first \(n\) Krylov vectors are linearly independent: their coordinate matrix is a Vandermonde matrix on the pairwise distinct nodes \(1,2,\ldots,n\), with determinant \(\prod_{1\le i<j\le n}(j-i)\ne0\). All higher powers lie in their span by finite dimensionality. This gives the claimed staircase. Moreover \(P(z)=I+(z-\xi)^2K\) is real symmetric positive definite for every real \(z\), since its diagonal entries are \(1+k(z-\xi)^2>0\). The step at \(m=2n-2\) raises the rank from \(n-1\) to \(n\), proving that no smaller universal derivative-order bound is possible, even in this positive definite class.

## Verification
The universal statement is established by the adjugate-degree and annihilator argument, independently of finite experiments. The standalone `verify.py` uses exact rational row reduction to reconstruct the diagonal-example Taylor coefficients and tests the complete rank staircase in dimensions \(1\) through \(8\), for three positive centers, across derivative orders extending beyond \(2n-2\). The output file `verification_output.txt` records successful checks. These experiments are sanity checks only, not an exhaustive or infinite proof.

## Relationship to prior work
Botchev, Knizhnerman, Zamarashkin and Zheltkov (2026) introduce an orthonormal derivative basis for \((A_0+zA_1+z^2A_2)x=zb\), obtain derivative recurrences and a companion-like \(2n\)-dimensional iteration, and discuss approximation and numerical stability (Section 4 and Appendix A). The present statement supplies an exact, worst-case **finite derivative-order completeness guarantee** and a positive definite family exhibiting arbitrarily long alternating rank plateaux; it does not modify their method. Tisseur and Meerbergen (2001) survey companion linearizations of quadratic eigenvalue problems; these provide relevant background but are not themselves the stated parameter-solution derivative rank profile. The adjugate proof is elementary and may be derivable from familiar rational realization theory; no assertion of universal novelty in all realization literature is made.

## Limitations
The theorem is about linear span in exact arithmetic, not a guaranteed useful low-rank approximation before completeness. The positive definite example is a diagonal parametric family, not the electromagnetic coefficient subclass of the motivating paper. A numerical implementation may be adversely affected by ill conditioning long before order \(2n-2\). Classical transfer-function and moment-matching literature could contain equivalent finite-jet statements under different terminology; comparison with those broader results remains an originality risk. No independent audit is claimed.

## References
1. M. A. Botchev, L. Knizhnerman, N. L. Zamarashkin and D. A. Zheltkov, *A single LU factorization approach to model reduction for linear system families with a quadratic matrix pencil*, arXiv:2610.14902v1, first submitted 10 October 2026, especially Section 4 and Appendix A. https://arxiv.org/abs/2610.14902
2. F. Tisseur and K. Meerbergen, *The quadratic eigenvalue problem*, SIAM Review **43** (2001), 235–286, DOI 10.1137/S0036144500381988. https://eprints.maths.manchester.ac.uk/466/
