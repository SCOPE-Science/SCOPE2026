# Unique activity threshold and exactly two trapping crossovers for a completely reset active Brownian particle

## Finding
For the two-dimensional active Brownian particle with joint Poisson resetting of position and orientation, the stationary radial excess kurtosis has one and only one activity threshold at each positive reset rate. Below threshold it is strictly positive at every positive harmonic-trap strength; at threshold it has one double zero; above threshold it has **exactly two simple positive trapping zeros** and is strictly negative only between them. The two zeros open with a square-root law. The weak-reset and strong-reset thresholds have explicit universal scaling constants. This is a classification of the sign of a fourth-moment statistic, **not** a claim that a zero-kurtosis position law is exactly Gaussian.

## Assumptions and scope
Let \(r>0\), \(\beta>0\), \(\mathrm{Pe}\ge0\), with dimensionless position \(X_t\in\mathbb R^2\) and orientation \(U_t=(\cos\Theta_t,\sin\Theta_t)\). Between independent rate-\(r\) Poisson events,
\[
 dX_t=(-\beta X_t+\mathrm{Pe}\,U_t)\,dt+\sqrt2\,dW_t,\qquad d\Theta_t=\sqrt2\,dB_t.
\]
At each event, \((X_t,\Theta_t)\mapsto(0,0)\). The Brownian drivers and resets are independent; the stationary law is selected by this complete reset. Let \(S=\mathbb E|X|^2\), \(M_4=\mathbb E|X|^4\) under that stationary law, and set \(p=\mathrm{Pe}^2\) and \(\mathcal K=M_4/(2S^2)-1\).

Define the following polynomials, whose arguments are \((\beta,r)\):
\[
\begin{aligned}
 A&=r(r+1)(r+2)+r(1+3r)\beta-(14+r)\beta^2-6\beta^3,\\
 B&=2r(\beta+r+1)(2\beta+r+4)(5\beta+2r+1),\\
 C&=2r(\beta+r+1)^2(2\beta+r+4)(3\beta+r+1),\\
 F(\beta;r,p)&=A p^2+B p+C.
\end{aligned}
\]
There is exactly one \(b_0(r)>0\) satisfying \(A(b_0(r),r)=0\). For \(\beta>b_0(r)\), put
\[
 P_r(\beta)=\frac{B+\sqrt{B^2-4AC}}{-2A}>0,
 \quad p_c(r)=\min_{\beta>b_0(r)}P_r(\beta),
 \quad \beta_c(r)=\mathop{\rm argmin}_{\beta>b_0(r)}P_r(\beta).
\]
The minimum exists and its minimizer is unique. For every \(r>0\):

* If \(0\le p<p_c(r)\), then \(\mathcal K(\beta;r,p)>0\) at every \(\beta>0\).
* If \(p=p_c(r)\), then \(\mathcal K\ge0\) and has precisely one positive zero, a double zero at \(\beta=\beta_c(r)\).
* If \(p>p_c(r)\), exactly two simple zeros \(0<\beta_-(r,p)<\beta_+(r,p)\) occur; \(\mathcal K<0\) precisely on \((\beta_-,\beta_+)\), and \(\mathcal K>0\) elsewhere in \((0,\infty)\).

There is no negative-kurtosis state for any activity at \(\beta\le b_0(r)\); for \(\beta>b_0(r)\), it occurs exactly when \(p>P_r(\beta)\). In particular, the curve of negative-kurtosis onset has a **single global fold** for each \(r>0\).

Writing derivatives of \(F\) with respect to \(p\) and \(\beta\) at the fold, the opening is
\[
 \beta_\pm(r,p)=\beta_c(r)\pm
 \sqrt{\frac{-2\,\partial_p F}{\partial_{\beta\beta}F}}
 \sqrt{p-p_c(r)}+O(p-p_c(r))\quad(p\downarrow p_c(r)),
\]
where \(\partial_pF<0\) and \(\partial_{\beta\beta}F>0\) at the fold.

There are sharp limiting fold laws. For weak resetting,
\[
 \beta_c(r)\longrightarrow b_w=1.376278054074389\ldots,
 \qquad \frac{p_c(r)}{\sqrt r}\longrightarrow c_w=3.045858096262309\ldots\quad(r\downarrow0),
\]
where \(b_w\) is the unique positive root of
\[
 9b^4+33b^3+b^2-67b-28=0,
 \qquad c_w^2=\frac{2(b_w+1)^2(b_w+2)(3b_w+1)}{b_w^2(3b_w+7)}.
\]
For strong resetting,
\[
 \frac{\beta_c(r)}r\longrightarrow t_\infty=5.579967751134424\ldots,
 \qquad \frac{p_c(r)}r\longrightarrow z_\infty=7.043484018621282\ldots\quad(r\to\infty).
\]
Here \((t_\infty,z_\infty)\) is the unique positive critical pair with \(t>(1+\sqrt{13})/6\), \(z>0\), of
\[
 \Phi(t,z)=\underbrace{(1+3t-t^2-6t^3)}_{a(t)}z^2
 +2(t+1)(2t+1)(5t+2)z+2(t+1)^2(2t+1)(3t+1)=0,
 \quad \partial_t\Phi(t,z)=0.
\]

## Proof
**Independent moment derivation.** Write \(q=\mathbb E[X\cdot U]\), \(w=\mathbb E[(X\cdot U)^2]\), and \(h=\mathbb E[|X|^2(X\cdot U)]\). Apply the diffusion-plus-reset generator to the five observables \(X\cdot U\), \(|X|^2\), \((X\cdot U)^2\), \(|X|^2(X\cdot U)\), and \(|X|^4\). Since every one vanishes at the reset state \(X=0\), the resetting contribution is its negative multiplied by \(r\). The stationary equations are
\[
\begin{aligned}
 (1+\beta+r)q&=\mathrm{Pe},\\
 (2\beta+r)S&=4+2\mathrm{Pe}\,q,\\
 (4+2\beta+r)w&=2+2S+2\mathrm{Pe}\,q,\\
 (1+3\beta+r)h&=\mathrm{Pe}(2w+S)+8q,\\
 (4\beta+r)M_4&=16S+4\mathrm{Pe}\,h.
\end{aligned}
\]
For example, the orientation generator contributes \(-X\cdot U\) to the first observable and \(2(|X|^2-2(X\cdot U)^2)\) to the third. The positional Laplacian contributes \(8X\cdot U\) to the fourth and \(16|X|^2\) to the fifth. The system is triangular and all denominators are strictly positive. Substitution yields
\[
 \mathcal K(\beta;r,p)=\frac{2F(\beta;r,p)}{
 (4\beta+r)(2\beta+r+4)(3\beta+r+1)(2\beta+p+2r+2)^2}.
\]
This identity also agrees with the independent second- and fourth-moment expressions reported in the source paper. Therefore the sign of \(\mathcal K\) is exactly the sign of \(F\).

**One activity threshold at each trap.** The cubic \(A\), viewed in descending powers of \(\beta\), has coefficient signs \((-,-,+,+)\), so Descartes' rule gives at most one positive root counted with multiplicity. Because \(A(0,r)>0\) and \(A\to-\infty\) at infinity, exactly one exists and is simple. For all \(\beta>0\), both \(B\) and \(C\) are positive. Thus if \(\beta\le b_0(r)\), \(F>0\) for every \(p\ge0\). For \(\beta>b_0(r)\), \(A<0\); the quadratic \(F=A p^2+Bp+C\) starts positive and crosses zero at the unique positive value \(P_r(\beta)\), becoming negative thereafter. Its positive root is the formula in the finding. As \(\beta\downarrow b_0(r)\), the negative coefficient \(-A\) vanishes while \(B,C>0\), hence \(P_r\to\infty\). As \(\beta\to\infty\), \(A\sim-6\beta^3\), \(B\sim20r\beta^3\), \(C\sim12r\beta^4\), hence \(P_r(\beta)\sim\sqrt{2r\beta}\to\infty\). A positive interior minimizer exists.

**Global uniqueness and the two-crossing dichotomy.** Regard \(F\) as a quartic polynomial in \(\beta\) at fixed positive \(r,p\). Its leading coefficient is \(12r>0\), the coefficients of \(\beta\) and the constant term are strictly positive, and only the \(\beta^3\) and \(\beta^2\) coefficients are of unrestricted sign. Hence its ordered coefficient signs have at most **two** changes, so Descartes' rule permits at most two positive roots, counting multiplicity. If \(P_r\) had two distinct global minimizers, then at the minimum activity both would be nonnegative local minima of \(F\), necessarily roots of even multiplicity at least two; this would give at least four positive roots counted with multiplicity, a contradiction. Thus the minimizer is unique. At the critical activity, \(F\) has one positive double root and no other; higher multiplicity is also excluded. For strictly greater activity, \(F\) is negative at the minimizer (because the activity quadratic has passed its unique positive root) and positive at \(\beta=0\) and for sufficiently large \(\beta\). It must have two distinct positive crossing roots and, by the same bound, no others. Both crossings are simple. At smaller activity \(F>0\) everywhere. This proves the exhaustive classification.

**Square-root opening.** At the fold \(F=F_\beta=0\); exact double multiplicity with a strict positive local minimum implies \(F_{\beta\beta}>0\). Also
\[
 F_p=2A p_c+B=-\sqrt{B^2-4AC}<0
\]
at the positive activity root. The Taylor expansion \(F=F_p(p-p_c)+(F_{\beta\beta}/2)(\beta-\beta_c)^2+\text{higher order}\) and the implicit roots away from the double point give the claimed two-sided square-root expansion.

**Weak/strong resetting.** For \(r\downarrow0\), substitute \(p=z\sqrt r\) into \(F\) and divide by \(r\); uniformly for \(\beta\) in compact subsets of \((0,\infty)\), the zero equation becomes
\[
 -2\beta^2(3\beta+7)z^2+4(\beta+1)^2(\beta+2)(3\beta+1)=o(1).
\]
Its positive zero branch is \(z=\sqrt{G(\beta)}\), with \(G(\beta)=2(\beta+1)^2(\beta+2)(3\beta+1)/(\beta^2(3\beta+7))\). Differentiating gives
\[
 G'(\beta)=\frac{2(\beta+1)(9\beta^4+33\beta^3+\beta^2-67\beta-28)}{\beta^3(3\beta+7)^2}.
\]
The quartic factor has exactly one positive root by Descartes' rule and opposite signs at zero and infinity. Moreover, \(P_r^2\ge C/(-A)\) on its domain, and for \(0<r\le1\)
\[
 \frac{C}{r(-A)}\ge
 \frac{4(\beta+1)^2(\beta+2)(3\beta+1)}{\beta^2(15+6\beta)},
\]
which diverges as \(\beta\downarrow0\) and \(\beta\to\infty\), uniformly in small \(r\). Thus minimizers cannot escape compact sets, and the unique minimizer of \(G\) gives both weak-reset limits.

For \(r\to\infty\), substitute \(\beta=rt\), \(p=rz\), and divide \(F\) by \(r^5\); the limit is \(\Phi(t,z)\) displayed above. Its coefficient of \(z^2\) changes sign exactly at \(t=(1+\sqrt{13})/6\). The positive-zero branch on the larger-\(t\) side diverges both at that endpoint and as \(t\to\infty\). Its unique minimum follows by the same positive-root-count argument: at fixed \(z\), \(\Phi\) is a quartic in \(t\) whose leading, linear and constant coefficients are positive, so it has at most two positive zeros. The bounding inequality \(P_r^2\ge C/(-A)\), rescaled by \(r\), excludes escape of the minimizers to \(t=\infty\) or to the moving coefficient-zero boundary, establishing convergence of the unique minima. Numerically solving \(\Phi=\Phi_t=0\) gives the constants specified above. The numerical values are approximations; existence, uniqueness and limits are analytical conclusions.

## Verification
The complete standalone `verify.py` implements the independent triangular stationary-generator recurrence and the factored quartic identity using exact rational arithmetic at 80 parameter triples. It reconstructs the critical activity for \(r=1\) as \(p_c\approx7.94071433834\) at \(\beta_c\approx7.16190748\); for \(r=1\) and \(\mathrm{Pe}=10\), it brackets the two zeros near \(\beta_-=0.768947514\) and \(\beta_+=4828.575391\), consistent with the original source's approximate plot. It also checks the small- and large-reset asymptotic constants numerically. Run `python verify.py` with Python 3. These finite computations corroborate exact identities and numerical values; the continuum root-count proof is the analytic argument above.

## Relationship to prior work
Shee, arXiv:2409.06920 (first posted September 11, 2024), derived the forward stationary moments and displayed numerical phase diagrams with two trap-strength zero crossings in an example. This result **does not** claim those moments or observed sample crossings as new. It establishes an all-parameter upper bound of two crossings, an existence/uniqueness threshold for every positive reset rate, the exact fold characterization and square-root unfolding, and weak/strong resetting asymptotics. Chaudhuri and Dhar, arXiv:2005.14234 (first posted May 28, 2020), treated an active Brownian particle in a harmonic trap without complete Poisson resetting; their negative-kurtosis reentrant crossover cannot establish the positive-reset fold classification. Published formulas logically permit further algebraic deductions, so the priority and scope of this derived structural theorem warrant independent literature review.

## Limitations
The word 'phase' refers exclusively to sign regions of a stationary normalized fourth moment; it is not a thermodynamic singularity, and zero excess kurtosis does not assert exact Gaussianity. The claim assumes two spatial dimensions, independent translational and rotational Brownian noises, a fixed orientation and origin at **every** complete Poisson reset, and strictly positive resetting and confinement rates. No finite-time, partial-reset, chirality, or finite-sample inference result is proved. The supplied finite verifier is not an infinite proof. Broader, possibly unlocated, algebraic classification results could imply some assertions; no independent scientific audit or definitive publication-priority determination has occurred.

## References
1. A. Shee, *Active Brownian particle under stochastic position and orientation resetting in a harmonic trap*, arXiv:2409.06920v1 (2024-09-11), revised v2 (2025-01-14). https://arxiv.org/html/2409.06920v2
2. D. Chaudhuri and A. Dhar, *Active Brownian particle in harmonic trap: exact computation of moments, and re-entrant transition*, arXiv:2005.14234 (2020-05-28). https://arxiv.org/pdf/2005.14234
