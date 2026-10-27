# A correlation threshold and two ridge-escape exponents in singular total least squares

## Finding
Consider genuine overdetermined total least squares with a rank-one Tikhonov penalty. A correlation between the penalized and unpenalized columns creates an exact attainment threshold and changes the escape exponent of the solution when a vanishing isotropic ridge is added. For the model below, the threshold is \(\beta=1+\gamma^2\). Above it the regularized solution norm grows like \(\varepsilon^{-1/4}\); precisely at it the growth is \(\varepsilon^{-1/6}\). Below it the unregularized minimum is attained and the regularized minimizers stay bounded.

Specifically, writing \(K=\beta-1-\gamma^2\), the value and escape laws in the two nonattaining cases are
\[
\begin{array}{ll}
K>0: & \min F_\varepsilon=1+2\sqrt{K\varepsilon}+o(\sqrt\varepsilon),\quad
\varepsilon^{1/4}|v_\varepsilon|\longrightarrow K^{1/4},\\[3pt]
K=0: & \min F_\varepsilon=1+3(\gamma^2/4)^{1/3}\varepsilon^{2/3}+o(\varepsilon^{2/3}),\quad
\varepsilon^{1/6}|v_\varepsilon|\longrightarrow(2\gamma^2)^{1/6}.
\end{array}
\]
In both nonattaining cases, \(u_\varepsilon v_\varepsilon\to-\gamma\) for **every** global minimizer. The limiting constants and exponents are sharp.

## Assumptions and scope
Fix any real \(0<\gamma<1\) and \(\beta>0\). Let the \(3\times2\) data matrix, observed vector, and singular regularization row be
\[
A=\begin{pmatrix}1&\gamma\\0&\sqrt{1-\gamma^2}\\0&0\end{pmatrix},\qquad
b=\begin{pmatrix}0\\0\\\sqrt\beta\end{pmatrix},\qquad L=\begin{pmatrix}1&0\end{pmatrix}.
\]
The columns of \(A\) have unit norm and correlation \(\gamma\); \(A\) has full column rank, and \(b\) is orthogonal to its range. The regularization is genuinely singular since the second coordinate is unpenalized. For \((u,v)\in\mathbb R^2\), define
\[
F_0(u,v)=\frac{\|A(u,v)^{\mathsf T}-b\|_2^2}{1+u^2+v^2}+\|L(u,v)^{\mathsf T}\|_2^2,
\qquad F_\varepsilon(u,v)=F_0(u,v)+\varepsilon(u^2+v^2),\quad\varepsilon>0.
\]
The first expression is the standard reduced Tikhonov-regularized total-least-squares objective, with unit penalty coefficient. The added ridge is a separate, **vanishing** regularizer; it is not an observational noise model. For every \(\varepsilon>0\), continuity and coercivity ensure at least one global minimizer. No uniqueness is asserted: sign symmetry can produce two minimizers.

## Proof
**1. Exact cancellation identity.** Since \(A^{\mathsf T}A=\begin{psmallmatrix}1&\gamma\\\gamma&1\end{psmallmatrix}\) and \(A^{\mathsf T}b=0\), set \(w=1+u^2+v^2\) and \(K=\beta-1-\gamma^2\). Direct expansion and completion of the square give the identity, valid for every real \(u,v\),
\[
\boxed{\quad F_0(u,v)-1=\frac{K+(uv+\gamma)^2+u^2+u^4}{w}.\quad}\tag{1}
\]
This identity is the basis of the complete classification.

**2. Attainment threshold.** If \(K\ge0\), the right side of (1) is strictly positive at every finite point: for \(u\ne0\) the term \(u^2\) is positive; for \(u=0\) the term \((uv+\gamma)^2=\gamma^2\) is positive. Along \(v\to+\infty\) with \(u=-\gamma/v\), (1) tends to zero. Hence \(\inf F_0=1\), never attained. If \(K<0\), use the same path and take finite \(|v|\) sufficiently large. Its numerator in (1) equals \(K+\gamma^2/v^2+\gamma^4/v^4<0\), so \(\inf F_0<1\). All strict sublevels \(\{F_0\le c\}\) for \(c<1\) are bounded: the nonnegative fractional term gives \(F_0\ge u^2\), bounding \(u\); as \(|v|\to\infty\) uniformly over bounded \(u\), the fractional term tends to \(1\), whence \(F_0\to1+u^2\ge1\). Such sublevels are closed, hence compact. Therefore the infimum is attained. A fixed test point below \(1\) also confines every minimizer of \(F_\varepsilon\) to a common compact strict sublevel for sufficiently small \(\varepsilon\). Uniform convergence on that compact set shows that all accumulation points minimize \(F_0\).

**3. Escape preliminaries.** Assume \(K\ge0\). Trial points from step 2 give \(\min F_\varepsilon\to1\), whereas \(F_\varepsilon\ge F_0>1\) at every finite point. Thus global minimizers leave each compact set. Since \(F_0\ge u^2\), their \(u\)-coordinates stay bounded, so \(|v|\to\infty\). The fractional term tends uniformly to \(1\) for bounded \(u\) as \(|v|\to\infty\); comparison with the optimal value forces \(u\to0\). Consequently \(w/v^2\to1\) at every minimizing sequence.

**4. Generic nonattainment \(K>0\).** From (1), for every minimizer,
\[
F_\varepsilon-1\ge\frac{K}{w}+\varepsilon v^2
=\frac{K}{v^2}(1+o(1))+\varepsilon v^2.
\]
Take the explicit trial point \(v=(K/\varepsilon)^{1/4}\), \(u=-\gamma/v\). Then \((uv+\gamma)^2=0\), and substitution into (1) gives
\(\min F_\varepsilon\le1+2\sqrt{K\varepsilon}+o(\sqrt\varepsilon)\).
The arithmetic-geometric-mean inequality gives the matching lower bound. Further, with \(q=\sqrt\varepsilon v^2\), the normalized lower bound is \(K/q+q+o(1)\); the upper bound confines \(q\) to a compact positive interval, and \(K/q+q\) has the unique minimizer \(q=\sqrt K\). Hence \(\varepsilon^{1/4}|v|\to K^{1/4}\). The unused nonnegative square term in (1), divided by \(w\), would contribute a positive amount at the leading \(\sqrt\varepsilon\) scale unless \((uv+\gamma)^2\to0\). Therefore \(uv\to-\gamma\).

**5. Critical nonattainment \(K=0\).** For each fixed \(v\), completing the square in \(u\) yields
\[
(uv+\gamma)^2+u^2
=(1+v^2)\left(u+\frac{\gamma v}{1+v^2}\right)^2
+\frac{\gamma^2}{1+v^2}.
\]
Consequently, at every minimizing point,
\[
F_\varepsilon-1\ge\frac{\gamma^2}{(1+v^2)w}+\varepsilon v^2
=\frac{\gamma^2}{v^4}(1+o(1))+\varepsilon v^2.
\]
Use \(v=(2\gamma^2/\varepsilon)^{1/6}\), \(u=-\gamma/v\) as a trial point. Its value is
\(1+3(\gamma^2/4)^{1/3}\varepsilon^{2/3}+o(\varepsilon^{2/3})\).
The lower bound is sharp because the minimum over positive \(r\) of \(\gamma^2/r^4+\varepsilon r^2\) equals exactly \(3(\gamma^2/4)^{1/3}\varepsilon^{2/3}\). Writing \(q=\varepsilon^{1/3}v^2\), comparison of upper and lower bounds confines \(q\) to a compact positive interval; the limiting objective \(\gamma^2/q^2+q\) has its unique minimum at \(q=(2\gamma^2)^{1/3}\). This establishes \(\varepsilon^{1/6}|v|\to(2\gamma^2)^{1/6}\). At such minimizers, \(w=O(\varepsilon^{-1/3})\) and \(F_\varepsilon-1=O(\varepsilon^{2/3})\); (1) then implies \((uv+\gamma)^2\le w(F_\varepsilon-1)=O(\varepsilon^{1/3})\), so \(uv\to-\gamma\). All limits were obtained for arbitrary global minimizers, not for a selected optimizer branch.

## Verification
The self-contained mathematical proof is analytical. For a reproducible check, run `python CHECK.py` in an environment with NumPy, SciPy and SymPy. It verifies the exact Gram identity symbolically, the rational completion identity, and numerical optimum values for \(\gamma=1/2\), \(K\in\{-1/4,0,1/4\}\) over decreasing ridge weights. These finite tests corroborate the constants and boundary behavior but do not certify infinite-parameter statements.

For the critical data with \(\gamma=1/2\), \(\beta=5/4\), the sharp value law is \(\min F_\varepsilon=1+(3/2^{4/3})\varepsilon^{2/3}+o(\varepsilon^{2/3})\). For the supercritical data \(\gamma=1/2\), \(\beta=3/2\), it is \(1+\sqrt\varepsilon+o(\sqrt\varepsilon)\). The case \(\beta=1\) has a finite minimizer of value strictly below \(1\).

## Relationship to prior work
Nguyen and Nguyen (2026, arXiv:2610.22880v1) analyze the attainment of singular-penalty fractional-quadratic programs by simultaneous diagonalization and give a nonattainment example (Theorem 4, Corollary 1, Example 1). Their first public arXiv version was submitted on 2026-10-16. That paper does not give the added-ridge escape laws or the correlation-controlled distinction between fourth-root and sixth-root behavior. Its illustrative nonattainment example lacks the correlated cross term that causes the critical cancellation here.

Beck and Ben-Tal (2006) give a sufficient finite-attainment condition and a trust-region reduction; Xia, Wang and Yang (2018, arXiv:1810.11972) use that condition for a global solution method. In the present family, the nullspace compression and its augmented data block have smallest eigenvalue \(1\) whenever \(\beta\ge1\), so their strict sufficient condition does not distinguish, for instance, \(\beta=1\) (finite attainment) from \(\beta=1+\gamma^2\) (nonattainment). The new statement characterizes the actual threshold in this minimal correlated model and quantifies how a small full-rank ridge approaches it. General singular perturbation theory may imply the existence of fractional exponents; the exact application-specific boundary and constants are the contribution, not a claimed new general perturbation method.

## Limitations
Only the displayed minimal rank-one-penalty TLS family is classified. The exponents are not claimed to hold for arbitrary matrices, higher-dimensional nullspaces, other regularizers, or stochastic perturbations. The ridge parameter is positive and approaches zero with \(\gamma,\beta\) fixed; no uniform double-parameter transition is asserted. Existence is guaranteed but uniqueness of global minimizers is not asserted. This result does not supply a finite-precision solver or a universal selection rule for all singular TRTLS problems. Some older specialized TLS literature was not available in full text, so historical equivalence cannot be categorically excluded.

## References
1. V.-B. Nguyen and T. N. Nguyen, *Solving the Tikhonov Regularization of the Total Least Squares Problem by matrix simultaneous diagonalization via congruence*, arXiv:2610.22880v1 (first submitted 2026-10-16). https://arxiv.org/abs/2610.22880
2. Y. Xia, L. Wang and M. Yang, *A fast algorithm for globally solving Tikhonov regularized total least squares problem*, arXiv:1810.11972 (2018). https://arxiv.org/abs/1810.11972
3. A. Beck and A. Ben-Tal, *On the Solution of the Tikhonov Regularization of the Total Least Squares Problem*, SIAM Journal on Optimization 17 (2006), 98–118, doi:10.1137/050624418.
4. G. H. Golub, P. C. Hansen and D. P. O'Leary, *Tikhonov Regularization and Total Least Squares*, SIAM Journal on Matrix Analysis and Applications 21 (1999), 185–194, doi:10.1137/S0895479897326432.
