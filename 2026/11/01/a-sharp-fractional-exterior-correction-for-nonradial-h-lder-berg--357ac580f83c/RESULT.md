# A sharp fractional exterior correction for nonradial Hölder Bergman polynomials

## Finding

Let \(0<\alpha<1\), \(\tau\in\mathbb R\), and \(0<|\varepsilon|<1/2\), with \(\varepsilon\) real. On the unit disk set
\[
 \omega(z)=1+2\varepsilon\operatorname{Re}\!\left[z(1-|z|)^{\alpha-i\tau}\right].
\]
Let \(P_n(z)=\kappa_n z^n+\cdots\) be its degree-\(n\) planar orthonormal polynomial for normalized area measure \(dA=dx\,dy/\pi\), with \(\kappa_n>0\). Define
\[
 A=\varepsilon\,2^{-\alpha-i\tau}\Gamma(1+\alpha+i\tau).
\]
Uniformly over the entire exterior \(|z|\ge1\),
\[
 \frac{P_n(z)}{\sqrt{n+1}\,z^n}
 =1-\frac{A}{z}\,n^{-\alpha-i\tau}+O(n^{-2\alpha}). \tag{1}
\]
The optimal normalization has the distinct, quadratic scale
\[
 \frac{\kappa_n}{\sqrt{n+1}}
 =1+\frac{|A|^2}{2}n^{-2\alpha}+o(n^{-2\alpha}). \tag{2}
\]
For each fixed \(|z|\ge1\),
\[
 \lim_{n\to\infty}n^\alpha\left|\frac{P_n(z)}{\sqrt{n+1}z^n}-1\right|=\frac{|A|}{|z|}>0. \tag{3}
\]
When \(\tau\ne0\), the cluster set of the complex sequence \(n^\alpha(P_n(z)/(\sqrt{n+1}z^n)-1)\) is exactly the circle centered at zero with radius \(|A|/|z|\); when \(\tau=0\), it converges to \(-A/z\). In particular, Hölder regularity \(C^{0,\alpha}\) alone does not permit a uniform \(o(n^{-\alpha})\) exterior approximation for this natural unit-disk class, even though the boundary weight is the constant one.

## Assumptions and scope

The disk is \(\mathbb D=\{z\in\mathbb C:|z|<1\}\). The power \((1-r)^{\alpha-i\tau}\) for \(0\le r<1\) uses the real logarithm. The weight is strictly positive because \(|2\varepsilon z(1-|z|)^{\alpha-i\tau}|<1\); it extends as a positive \(C^{0,\alpha}\) weight to a neighborhood of the closed disk by setting the perturbation to zero for \(|z|\ge1\). The exterior expression divides by \(z^n\) only for \(|z|\ge1\). Every limit is as positive integer \(n\to\infty\), with the four parameters and \(z\) fixed except for the uniformity in (1). The frequency \(\tau\) may be zero.

## Proof

**Step 1: exact moment matrix.** Use the inner product linear in its first argument, \(\langle f,g\rangle=\int_{\mathbb D}f\overline g\,\omega\,dA\). Angular integration gives
\[
 \langle z^j,z^k\rangle=
 \begin{cases}
 1/(j+1),&j=k,\\
 \gamma_j,&j=k+1,\\
 \overline{\gamma_k},&k=j+1,\\
 0,&|j-k|\ge2,
 \end{cases}
 \qquad
 \gamma_n=2\varepsilon B(2n+2,1+\alpha+i\tau).
 \tag{4}
\]
Indeed, in the first off-diagonal only the conjugate angular Fourier mode contributes; the radial integral is \(2\varepsilon\int_0^1r^{2n+1}(1-r)^{\alpha+i\tau}\,dr\). All diagonal perturbations vanish by angular averaging.

**Step 2: exact orthogonalization and normalization.** Let \(q_n=P_n/\kappa_n\) be monic and \(h_n=\|q_n\|_\omega^2=\kappa_n^{-2}\). Since \(z^n\) is orthogonal to every polynomial of degree at most \(n-2\), Gram–Schmidt gives the identities, for every \(n\ge1\),
\[
 q_0=1,\quad h_0=1,\qquad
 q_n(z)=z^n-\frac{\gamma_n}{h_{n-1}}q_{n-1}(z),\qquad
 h_n=\frac1{n+1}-\frac{|\gamma_n|^2}{h_{n-1}}.
 \tag{5}
\]
The last formula follows from the Pythagorean theorem after projection onto the immediately preceding orthogonal polynomial. All \(h_n\) are strictly positive because \(\omega>0\).

**Step 3: gamma asymptotics and the two response scales.** Put \(s=1+\alpha+i\tau\). The classical gamma-ratio expansion gives
\[
 \gamma_n=2\varepsilon\Gamma(s)\frac{\Gamma(2n+2)}{\Gamma(2n+2+s)}
 =2\varepsilon\Gamma(s)(2n)^{-s}(1+O(n^{-1})).
 \tag{6}
\]
Set \(t_n=(n+1)h_n\) and \(b_n=n(n+1)|\gamma_n|^2\). Then (5) is exactly \(t_n=1-b_n/t_{n-1}\). The lower bound \(\omega\ge1-2|\varepsilon|>0\) and the extremal definition of monic norms imply \(1-2|\varepsilon|\le t_n\le1\) (use the unweighted monic minimum \(1/(n+1)\), and the trial monomial for the upper bound). Since
\[
 b_n=|A|^2n^{-2\alpha}(1+O(n^{-1})),
 \tag{7}
\]
we have \(t_n\to1\) and hence \(t_n=1-|A|^2n^{-2\alpha}+o(n^{-2\alpha})\). Taking inverse square roots proves (2). In addition, the coefficient
\[
 a_n=\frac{\gamma_n}{h_{n-1}}
 =A\,n^{-\alpha-i\tau}\left(1+O(n^{-\min\{1,2\alpha\}})\right).
 \tag{8}
\]
The coefficient of \(z^{n-1}\) in \(q_n\) is exactly \(-a_n\).

**Step 4: exterior estimate.** Let \(R_n(z)=q_n(z)/z^n\) for \(|z|\ge1\). Formula (5) becomes \(R_n(z)=1-(a_n/z)R_{n-1}(z)\). By (8), \(|a_n|=O(n^{-\alpha})\). Choosing an index beyond which \(|a_n|\le1/2\), the recursion makes \(R_n\) uniformly bounded on the whole exterior. Substitution back gives \(R_n=1+O(n^{-\alpha})\) uniformly and then
\[
 R_n(z)=1-\frac{a_n}{z}+O(n^{-2\alpha})
 =1-\frac{A}{z}n^{-\alpha-i\tau}+O(n^{-2\alpha}),
\]
where the replacement error \(O(n^{-\alpha-1})\) is absorbed since \(\alpha<1\). Multiplication by \(\kappa_n/\sqrt{n+1}=1+O(n^{-2\alpha})\) proves (1). Formula (3) follows because \(|n^{-i\tau}|=1\) and \(A\ne0\). For nonzero \(\tau\), the increasing or decreasing sequence \(\tau\log n\) has unbounded range and successive absolute increments tending to zero, so its phases are dense on the unit circle; the vanishing remainder in (1) proves the stated exact cluster circle.

**Step 5: Hölder regularity.** The map \(x\mapsto x^{\alpha-i\tau}\) on \(x\ge0\), extended by zero at \(0\), is \(\alpha\)-Hölder: homogeneity reduces the quotient \(|s^{\alpha-i\tau}-t^{\alpha-i\tau}|/|s-t|^\alpha\) to \(t/s\in[0,1]\), where it is bounded at both endpoints. Composing with \(1-|z|\), multiplying by \(z\), and extending beyond the circle gives the asserted \(C^{0,\alpha}\) weight. The nonzero limit (3) proves sharpness of the rate.

## Verification

The accompanying `verify.py` independently computes the finite tridiagonal Gram matrix and beta moments, checks the monic recurrence by direct Gram inner products for degrees one through thirteen, and evaluates the scaled asymptotic constants through degree 1500. Run `python verify.py` with the dependency in `requirements.txt`. Its output includes `CHECK_OK: Gram orthogonality, beta moments, monic recurrence, fractional asymptotics`. These finite checks do not certify the all-degree formulas; the proof above does.

## Relationship to prior work

Hübner, *Asymptotics of Weighted Bergman Polynomials under Finite Regularity* (first public 2026-10-17, arXiv:2610.24693), gives uniform exterior asymptotics for positive \(C^{0,\alpha}\) weights, with error \(O(n^{-\beta})\) for every \(\beta<\alpha\) on a fixed exterior compact set. Its Theorem A and proof do not state an explicit gamma-valued fractional correction or the two-scale response (1)–(2) for the oscillatory one-angular-mode weight. The boundary value of the present weight equals one, so its leading exterior factor specializes to \(\sqrt{n+1}z^n\). The exact leading error in (1) proves that an \(o(n^{-\alpha})\) uniform generalization is impossible even in this smooth-domain, nonradial-weight subfamily.

Hedenmalm and Wennman, *Riemann–Hilbert hierarchies for hard edge planar orthogonal polynomials* (arXiv:2008.02682), construct all-order expansions for real-analytic weights. Their analytic-weight hypotheses exclude the present nonanalytic boundary perturbation. Classical area-orthogonal-polynomial theory (Suetin) and ordinary banded Gram–Schmidt provide general methods rather than the particular asymptotic response stated here. The elementary beta/gamma and orthogonalization steps are not themselves claimed novel; the new claim is their exact nonradial Hölder exterior-response law and sharpness mechanism.

## Limitations

The result concerns a single nontrivial angular Fourier mode of a positive disk weight; it is not a global characterization of all Hölder weights, and it does not establish an upper \(O(n^{-\alpha})\) estimate for every weight. The constants in big-O may depend on \(\alpha,\tau,\varepsilon\). Results on more general oscillatory moment matrices might imply this particular example indirectly; historical priority beyond the inspected sources requires independent checking. No independent mathematical audit has been performed.

## References

1. L. A. Hübner, *Asymptotics of Weighted Bergman Polynomials under Finite Regularity*, arXiv:2610.24693, first submitted 2026-10-17, https://arxiv.org/html/2610.24693v1.
2. H. Hedenmalm and A. Wennman, *Riemann–Hilbert hierarchies for hard edge planar orthogonal polynomials*, arXiv:2008.02682, first submitted 2020-08-06, https://arxiv.org/abs/2008.02682.
3. P. K. Suetin, *Polynomials Orthogonal over a Region and Bieberbach Polynomials*, Proceedings of the Steklov Institute of Mathematics 100 (1971); English translation 1974.
4. P. Kevei, *Regularly log-periodic functions and some applications*, arXiv:1709.01996. Provides a general log-periodic Laplace–Tauberian setting, but not a planar nonradial orthogonal-polynomial analysis.
