# A rare-corner law for first-chaos projections on biased Boolean products

## Finding
Let \(\Omega=\{0,1\}^n\) for an arbitrary integer \(n\ge1\). Give it the product probability measure \(\mu=\bigotimes_{i=1}^n\operatorname{Bernoulli}(p_i)\), with each \(0<p_i<1\). Define the centered first-chaos orthogonal projector \(P\) by
\[
(Pf)(x)=\sum_{i=1}^n\frac{x_i-p_i}{p_i(1-p_i)}\,\mathbb E_\mu[(Y_i-p_i)f(Y)].
\]
As an operator on the real Banach space \(C(\Omega)\) equipped with the supremum norm, its exact norm is
\[
\boxed{\|P\|_{\infty\to\infty}=\mathbb E\left|\sum_{i=1}^n\left(\frac{B_i}{r_i}-1\right)\right|,\quad r_i=\min\{p_i,1-p_i\},\quad B_i\sim\operatorname{Bernoulli}(r_i)\text{ independent}.}
\]
In particular the norm is attained by a kernel row at the *rare corner*: choose \(x_i=1\) when \(p_i\le1/2\), and \(x_i=0\) when \(p_i\ge1/2\). A coordinate with \(p_i=1/2\) admits either choice.

For the homogeneous product \(p_i=p\), write \(q=1-p\) and \(m=\lfloor np\rfloor\). Then the exact closed formula is
\[
\boxed{\|P\|_{\infty\to\infty}=2n\max(p,q)\binom{n-1}{m}p^m q^{n-1-m}.}
\]
For any fixed \(p\in(0,1)\),
\[
\|P\|_{\infty\to\infty}\sim\sqrt{\frac{2n}{\pi}}\frac{\max(p,q)}{\sqrt{pq}}\qquad(n\to\infty).
\]
At a sparse bias \(p=c/n\), for each fixed \(c>0\),
\[
\boxed{\lim_{n\to\infty}\frac{\|P\|_{\infty\to\infty}}{n}=2e^{-c}\frac{c^{\lfloor c\rfloor}}{\lfloor c\rfloor!}.}
\]
The passage from order \(\sqrt n\) at fixed bias to order \(n\) at sparse bias is sharp, and follows from the same exact finite formula.

## Assumptions and scope
The probability measure is a full-support product measure with independent, not necessarily identically distributed Bernoulli coordinates. All functions and operator norms are real, and \(P\) is specifically the orthogonal projection onto \(\operatorname{span}\{x\mapsto x_i-p_i:1\le i\le n\}\) in \(L^2(\mu)\), subsequently regarded as a map of \(C(\Omega)\). There is **no** additional constant term in its range. Since \(p_i\in(0,1)\), the input supremum norm equals the \(L^\infty(\mu)\) norm.

## Proof
**1. Kernel and row norm.** Orthogonality and the variances \(\mathbb E(Y_i-p_i)^2=p_i(1-p_i)\) give the displayed formula for \(P\). Its kernel is
\[
K(x,y)=\sum_{i=1}^n\frac{(x_i-p_i)(y_i-p_i)}{p_i(1-p_i)}.
\]
For a linear operator on a finite supremum-norm function space, the norm is the maximum absolute row sum. Thus
\[
\|P\|_{\infty\to\infty}=\max_{x\in\Omega}\mathbb E_\mu|K(x,Y)|.
\]
This is exact: for a maximizing row \(x\), set \(f(y)=\operatorname{sgn}K(x,y)\), choosing either sign at a zero, to attain its absolute row sum.

**2. Coordinatewise convex order.** Fix a coordinate with rare-event probability \(r_i=\min(p_i,1-p_i)\le1/2\). Its kernel summand at the rare value of \(x_i\) has law \(U_i\) supported on \(\{-1,(1-r_i)/r_i\}\) and equals \(-1\) with probability \(1-r_i\), and \((1-r_i)/r_i\) with probability \(r_i\). At the common value of \(x_i\), the summand has law \(V_i\) supported on \(\{-1,r_i/(1-r_i)\}\), taking \(-1\) with probability \(r_i\), and \(r_i/(1-r_i)\) with probability \(1-r_i\). Both laws have mean zero, and the support of \(V_i\) is contained in the interval between the two values of \(U_i\).

For every convex function \(\varphi\) on that interval, the chord joining its endpoint values bounds \(\varphi\) from above. Because both laws have mean zero, averaging the chord shows \(\mathbb E\varphi(V_i)\le\mathbb E\varphi(U_i)\). Consequently \(V_i\preceq_{\mathrm{cx}}U_i\). For an independent sum \(S\) of other kernel summands, the function \(t\mapsto\mathbb E|S+t|\) is convex. Replacing a common-corner summand by its rare-corner counterpart therefore cannot decrease the absolute first moment. Repeating over all coordinates shows that a rare corner maximizes \(\mathbb E|K(x,Y)|\), without assuming equal biases.

**3. The exact heterogeneous expression.** At the rare corner, each summand is distributed as \(B_i/r_i-1\), with independent \(B_i\sim\operatorname{Bernoulli}(r_i)\). Combining this observation with step 1 gives the main formula.

**4. Homogeneous reduction.** With \(p_i=p\), the rare-corner row is distributed as \((J-np)/p\) when \(p\le1/2\), and as \(-(J-np)/q\) when \(p\ge1/2\), where \(J\sim\operatorname{Binomial}(n,p)\). Hence
\[
\|P\|_{\infty\to\infty}=\frac{\mathbb E|J-np|}{\min(p,q)}.
\]
For \(m=\lfloor np\rfloor\), use the identity
\[
(k-np)\Pr(J=k)=npq\{\Pr(J'=k-1)-\Pr(J'=k)\},
\]
where \(J'\sim\operatorname{Binomial}(n-1,p)\), together with \(\mathbb E(J-np)=0\). Summing over \(k\ge m+1\) telescopes, yielding
\[
\mathbb E|J-np|=2npq\Pr(J'=m).
\]
This establishes the finite binomial formula, including integer values of \(np\).

**5. Sharp asymptotics.** When \(p\) is fixed in \((0,1)\), the local binomial central limit theorem gives \(\Pr(J'=\lfloor np\rfloor)\sim(2\pi npq)^{-1/2}\). Substitution proves the square-root law. When \(p=c/n\), the binomial law of \(J'\) converges at each fixed integer to \(\operatorname{Poisson}(c)\). Since the boundary index is \(\lfloor c\rfloor\), the finite formula gives the stated sparse limit. At integer \(c\), the adjacent Poisson masses are equal, so the expression remains continuous in \(c\).

## Verification
The accompanying standalone standard-library script `biased_first_chaos_checker.py` independently forms the full kernel and computes exact rational absolute row sums. It checked 2,286 homogeneous rows in dimensions one through seven, 4,455 two-binomial support cases in dimensions one through thirty, and 1,860 heterogeneous rows across 150 independent-bias profiles. Every test agreed with the formulas and rare-corner maximization. The proof above, not these finite checks, establishes all-dimensional validity; the two limits use standard binomial local-limit and Poisson-limit theorems.

## Relationship to prior work
The 2022 study by Defant, Galicer, Mansilla, Mastyło and Muro gives the Walsh spectral projection/minimum projection-constant formula for the **uniform** Boolean cube, notably its Chapter 8. The fair-bias case of the present formula is consequently not asserted as new. The present statement concerns the operator norm of a specified \(L^2(\mu)\)-orthogonal projector with arbitrary independent nonuniform biases, including unequal biases, rather than the smallest norm among all projections. The uniform-group averaging theorem does not determine this biased operator norm. Filmus's 2022 notes give the standard normalized biased Fourier basis, without the rare-corner extremal norm law in the inspected material.

## Limitations
The theorem does not evaluate the *minimum* relative or absolute projection constant of the corresponding function subspace. It does not apply to dependent coordinates, degenerate endpoint biases, or higher homogeneous chaos. The closed binomial boundary expression assumes one common bias; the heterogeneous expression is an exact expectation of a weighted Poisson-binomial sum. The search of published sources and mathematical records cannot rule out an unindexed earlier equivalent convex-order statement or Hoeffding-decomposition norm identity; independent assessment has not been performed.

## References
1. A. Defant, D. Galicer, M. Mansilla, M. Mastyło, S. Muro, *Projection constants for spaces of multivariate polynomials*, arXiv:2208.06467, initial public version 12 August 2022, particularly Chapter 8, Sections 8.1–8.2. https://arxiv.org/abs/2208.06467
2. Y. Filmus, *Boolean Function Analysis*, lecture notes dated 2 June 2022, Chapter 8 on biased Fourier analysis. https://yuvalfilmus.cs.technion.ac.il/Courses/BooleanFunctionAnalysis/2021/LectureNotes.pdf
