# Sharp Carathéodory floors for the polylogarithmic Bergman-type kernel scale

## Finding
For a real parameter \(\alpha\ge0\), let
\[
F_\alpha(t)=\sum_{n=0}^{\infty}(n+1)^\alpha t^n
=\frac{\operatorname{Li}_{-\alpha}(t)}{t},\qquad |t|<1,
\]
where the quotient at \(t=0\) has value one. Define the normalized function \(H_\alpha(t)=(1-t)^2F_\alpha(t)\). Its **exact sharp Carathéodory lower envelope** is
\[
\boxed{\inf_{|t|<1}\operatorname{Re} H_\alpha(t)=
\begin{cases}
0,&0\le\alpha<1,\\
1,&\alpha=1,\\
4\eta(-\alpha),&1<\alpha<2,\\
0,&\alpha=2,\\
-\infty,&\alpha>2,
\end{cases}}
\]
with \(\eta(s)=(1-2^{1-s})\zeta(s)\) the entire Dirichlet eta function. In particular, \(4\eta(-\alpha)>0\) for \(1<\alpha<2\). The indicated infima are sharp: for \(0\le\alpha<1\), approach \(t=1\) on the real radius; for \(1<\alpha\le2\), approach \(t=-1\); at \(\alpha=1\), the function is identically one; for \(\alpha>2\), approach \(t=1\) along a suitable interior complex ray in logarithmic coordinates.

Consequently, \(\operatorname{Re}H_\alpha(t)>0\) throughout the disk exactly for \(0\le\alpha\le2\). The reproducing kernel \(F_\alpha(z\overline w)\) is zero-free on the bidisk exactly in this parameter range. For every \(\alpha>2\), it has a zero corresponding to a negative real product \(z\overline w\in(-1,0)\). The precise real-part envelope, rather than a zero count by itself, is the principal assertion.

## Assumptions and scope
Let \(\mathcal B_\alpha\) be the space of analytic \(f(z)=\sum_{n\ge0}a_nz^n\) on the open unit disk with norm \(\|f\|_\alpha^2=\sum_{n\ge0}|a_n|^2/(n+1)^\alpha\). Its reproducing kernel is \(K_\alpha(z,w)=F_\alpha(z\overline w)\); \(\alpha=0\) is the Hardy space and \(\alpha=1\) is the standard unweighted Bergman space. No statement is made for negative \(\alpha\), for other coefficient normalizations, or about the complete number of zeros beyond the sharp threshold. All infima are taken over the **open** unit disk, not its boundary. The eta and zeta functions in the formula are their standard analytic continuations.

## Proof
**1. Reduction to second differences.** For \(\alpha>0\), the power-series identity gives
\[
H_\alpha(t)=1+\sum_{n=1}^{\infty} \big((n+1)^\alpha-2n^\alpha+(n-1)^\alpha\big)t^n,
\]
with \(0^\alpha=0\). We use the elementary disk inequality, valid for every \(u\in[0,1)\) and \(|t|<1\),
\[
-\frac{1}{1+u}<\operatorname{Re}\frac{t}{1-ut}<\frac{1}{1-u}.
\]
This follows from the boundary formula \(\operatorname{Re}(t/(1-ut))=(\cos\theta-u)/(1-2u\cos\theta+u^2)\), whose derivative in \(\cos\theta\) is positive. The upper and lower boundary extrema are attained in radial limits to \(1\) and \(-1\), respectively.

**2. Sublinear powers.** Suppose \(0<\alpha<1\), and put \(c_\alpha=\alpha/\Gamma(1-\alpha)>0\). The absolutely convergent fractional-power formula
\[
x^\alpha=c_\alpha\int_0^\infty(1-e^{-xs})s^{-1-\alpha}\,ds
\]
yields, after taking second differences and summing the geometric series,
\[
H_\alpha(t)=1-c_\alpha\int_0^\infty
(1-e^{-s})^2\frac{t}{1-te^{-s}}s^{-1-\alpha}\,ds.
\]
The disk upper bound in step 1 implies
\[
\operatorname{Re}H_\alpha(t)>1-c_\alpha\int_0^\infty(1-e^{-s})s^{-1-\alpha}\,ds=0.
\]
For \(t\uparrow1\), dominated convergence applies with dominating integrand \(c_\alpha(1-e^{-s})s^{-1-\alpha}\), and gives \(H_\alpha(t)\to0\). Hence the sharp infimum is zero.

**3. Superlinear powers below two.** Suppose \(1<\alpha<2\). Now \(c_\alpha=1/\Gamma(-\alpha)>0\), and
\[
x^\alpha=c_\alpha\int_0^\infty(e^{-xs}-1+xs)s^{-1-\alpha}\,ds.
\]
Second differences yield instead
\[
H_\alpha(t)=1+c_\alpha\int_0^\infty
(1-e^{-s})^2\frac{t}{1-te^{-s}}s^{-1-\alpha}\,ds.
\]
By the disk lower bound in step 1,
\[
\operatorname{Re}H_\alpha(t)>
1-c_\alpha\int_0^\infty\frac{(1-e^{-s})^2}{1+e^{-s}}s^{-1-\alpha}\,ds
=H_\alpha(-1).
\]
The integral is finite because its integrand is \(O(s^{1-\alpha})\) at zero. Dominated convergence along \(t\downarrow-1\) proves sharpness. The standard polylogarithm continuation at \(-1\) gives \(F_\alpha(-1)=\eta(-\alpha)\) and hence \(H_\alpha(-1)=4\eta(-\alpha)\). The zeta functional equation gives \(\zeta(-\alpha)<0\) for \(1<\alpha<2\), while \(1-2^{1+\alpha}<0\), so this sharp floor is strictly positive.

**4. Three integer endpoints.** The elementary rational generating functions imply \(H_0(t)=1-t\), \(H_1(t)=1\), and \(H_2(t)=(1+t)/(1-t)\). These have sharp real-part infima \(0,1,0\), respectively, and have positive real part throughout the open disk.

**5. Blow-up beyond two.** Fix any \(\alpha>2\). Set \(t=e^{-s}\) with \(s=\rho e^{i\theta}\), where \(\rho\downarrow0\) and \(0<\theta<\pi/2\). A dominated complex Riemann-sum limit shows
\[
\operatorname{Li}_{-\alpha}(e^{-s})
\sim\Gamma(\alpha+1)s^{-\alpha-1},
\qquad H_\alpha(e^{-s})\sim\Gamma(\alpha+1)s^{1-\alpha}.
\]
Here the asymptotic holds at every fixed angle with \(\operatorname{Re}s>0\); it follows by comparing \(\sum_{n\ge1}n^\alpha e^{-ns}\) with \(\int_0^\infty x^\alpha e^{-sx}\,dx\), whose relative error tends to zero. Because \(\alpha-1>1\), we may choose \(\theta\in(0,\pi/2)\) with \(\cos((\alpha-1)\theta)<0\). Thus \(\operatorname{Re}H_\alpha(e^{-\rho e^{i\theta}})\to-\infty\), proving both failure of positive real part and the sharp value \(-\infty\).

**6. Negative-real kernel zeros above two.** For \(2<\beta\le3\), the zeta functional equation yields \(\eta(-\beta)<0\), so \(F_\beta(-1)=\eta(-\beta)<0<F_\beta(0)\). Continuity supplies \(r\in(0,1)\) with \(\operatorname{Li}_{-\beta}(-r)=0\). If \(\operatorname{Li}_{-\gamma}(-r)=0\) for some \(\gamma>0\), then Rolle's theorem applied to \(x\mapsto\operatorname{Li}_{-\gamma}(-x)\), which vanishes at both \(0\) and \(r\), gives \(r'\in(0,r)\) such that \(\operatorname{Li}_{-(\gamma+1)}(-r')=0\), by the differential identity \(d\operatorname{Li}_{s}(-x)/dx=\operatorname{Li}_{s-1}(-x)/x\). Every \(\alpha>2\) differs by a nonnegative integer from some \(\beta\in(2,3]\), proving the assertion for all \(\alpha>2\). Every \(t\in\mathbb D\) is realizable as \(z\overline w\) with \(z,w\in\mathbb D\). This finishes the kernel claim.

## Verification
The proof is analytic for **all real parameters** in the indicated ranges. A standalone numerical sanity script, `CHECK.py`, evaluates the exact polylogarithm, samples interior points against the asserted sharp envelopes, checks the complex-sector blow-up sign, and observes negative-real sign changes for representative supercritical orders. Running `python CHECK.py` with `mpmath` prints three `POLYLOG_..._OK` markers. Its finite numerical tests are not relied upon for the continuum proof. The critical steps are the two fractional-power integral identities, the sharp Möbius disk inequalities, the zeta sign, and the fixed-sector complex Riemann-sum asymptotic.

## Relationship to prior work
Classical work describes polylogarithm zeros and their integer-order Eulerian structure; see Wood's *The Computation of Polylogarithms*, especially §21, and Savage–Visontai for general Eulerian real-rootedness. In particular, qualitative zeros of negative-order polylogarithms are **not** claimed to be newly discovered. Bénéteau–Khavinson–Liaw–Seco–Sola study Dirichlet-type spaces and zeros of *optimal approximants* and their associated finite-section kernels, a different question from the full kernel's exact real-part envelope. A comparison with the general literature on special radial Bergman kernels did not find the present all-real-order, sharp Carathéodory infimum formula. The central novel candidate is the complete real-part phase diagram and its boundary-location switch at the Hardy-to-Bergman exponent, not classical polylogarithm identities themselves.

## Limitations
This result concerns the particular coefficient norms \((n+1)^{-\alpha}\) and the full scalar reproducing kernel; it does not assert a universal theorem for all weighted Bergman measures, nor count all supercritical zeros. Earlier literature may contain an equivalent sharp real-part estimate under a different name, and independent review has not been performed. The cited 1975 polylogarithm zero study could not be read completely, although its known subject is zeros in the order variable. The proof is mathematically self-contained apart from standard gamma/zeta/polylogarithm identities, and the finite test is illustrative rather than an infinite certificate.

## References
1. C. D. Savage and M. Visontai, *The s-Eulerian polynomials have only real roots*, arXiv:1208.3831 (first publicly submitted 2012-08-19); classical Eulerian-root background.
2. C. Bénéteau, D. Khavinson, C. Liaw, D. Seco and A. A. Sola, *Orthogonal polynomials, reproducing kernels, and zeros of optimal approximants*, arXiv:1509.04807 (first submitted 2015-09-16); full Dirichlet-type space framework and a distinct kernel-zero problem.
3. D. C. Wood, *The Computation of Polylogarithms*, 1992, University of Kent repository, https://kar.kent.ac.uk/21052/1/ThecompD.pdf, especially §§6, 21; established polylogarithm zero counts, special values and continuation.
4. B. Fornberg and K. S. Kölbig, *Complex zeros of the Jonquière or polylogarithm function*, Mathematics of Computation 29 (1975), 582–599, DOI 10.1090/S0025-5718-1975-0369278-0; relevant earlier zero literature, full text not inspected.
