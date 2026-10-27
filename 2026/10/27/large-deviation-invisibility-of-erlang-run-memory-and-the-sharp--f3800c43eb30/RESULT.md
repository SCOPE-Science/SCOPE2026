# Large-deviation invisibility of Erlang run memory and the sharp asymmetric phase-ratio boundary

## Finding
An alternating-velocity run-and-tumble particle can have nonexponential holding times and nevertheless possess **exactly the same complete long-time displacement large-deviation rate function** as a memoryless two-state telegraph process. Within the family of unequal Erlang stage counts, this happens **if and only if the two stage counts are equal**. Unequal stage counts are detectable from the two distinct fractional-power corrections to the extreme tilted pressures.

Precisely, let \(p,q\in\{1,2,\ldots\}\), \(\lambda_+,\lambda_->0\), and \(v>0\). Set \(X_t=v\int_0^t S_s\,ds\), where \(S_s\in\{-1,+1\}\) alternates and independent successive positive and negative run durations have Erlang distributions with shape/rate \((p,\lambda_+)\) and \((q,\lambda_-)\), respectively. For any initial phase state, the scaled cumulant generating function is
\[
\Lambda(\theta)=\lim_{t\to\infty}\frac1t\log\mathbb E[e^{\theta X_t}],
\quad
(\Lambda+\lambda_+-v\theta)^p(\Lambda+\lambda_-+v\theta)^q=\lambda_+^p\lambda_-^q,
\]
where the defining root is the unique real root satisfying \(\Lambda>\max\{v\theta-\lambda_+,-v\theta-\lambda_-\}\). The laws of \(X_t/t\) satisfy the full large-deviation principle with good convex rate \(I(x)=\sup_{\theta\in\mathbb R}\{\theta x-\Lambda(\theta)\}\).

In particular, the exact positive and negative pressure-edge laws are
\[
\Lambda(\theta)=v\theta-\lambda_+
+\lambda_+\lambda_-^{q/p}(2v\theta)^{-q/p}(1+o(1)),\qquad\theta\to+\infty,
\]
\[
\Lambda(\theta)=-v\theta-\lambda_-
+\lambda_-\lambda_+^{p/q}(2v|\theta|)^{-p/q}(1+o(1)),\qquad\theta\to-\infty.
\]
Thus their powers identify the ratio of Erlang stage counts. The entire large-deviation rate coincides with some two-state exponential-run telegraph rate **precisely when** \(p=q\). If \(p=q\), the only matching Markov switching rates are \(\lambda_+,\lambda_-\), and for \(-1\le z\le1\),
\[
I(vz)=\frac{\lambda_+(1+z)+\lambda_-(1-z)}2
-\sqrt{\lambda_+\lambda_-}\sqrt{1-z^2}.
\]
It equals \(+\infty\) outside \([-v,v]\). At the two endpoints \(I(v)=\lambda_+\) and \(I(-v)=\lambda_-\) for every \(p,q\).

## Assumptions and scope
All run times are independent across completed sojourns, with deterministic alternating sign. Each Erlang law has a strictly positive finite integer shape and strictly positive phase rate. The process may begin in any of the finitely many Erlang stages, possibly randomized. No reflecting walls, absorbing boundary, potential, thermal white noise, or resetting are included. The large-deviation scaling is \(t\to\infty\) with all microscopic parameters fixed; it is not a uniform joint limit in stage counts or rates.

## Proof
**1. Phase embedding.** Replace a \(+\) run by \(p\) successive exponential stages with rate \(\lambda_+\), and a \(-\) run by \(q\) successive exponential stages with rate \(\lambda_-\). Cycling through all \(p+q\) stages produces an irreducible continuous-time Markov chain with generator \(Q\); each stage transition advances one step, and the final negative stage returns to the first positive stage. Let \(V\) be the diagonal matrix whose first \(p\) entries equal \(v\) and last \(q\) entries equal \(-v\). Feynman–Kac yields \(\mathbb E_i[e^{\theta X_t}]=[e^{t(Q+\theta V)}\mathbf1]_i\). The irreducible Metzler matrix has a simple real dominant eigenvalue \(\Lambda(\theta)\), analytic in \(\theta\), and this eigenvalue determines the above logarithmic limit for every starting phase.

**2. Exact pressure equation.** The eigenvector recursion around the unique stage cycle multiplies successive ratios. Writing \(A_+=\Lambda+\lambda_+-v\theta\) and \(A_-=\Lambda+\lambda_-+v\theta\), it gives \(A_+^p A_-^q=\lambda_+^p\lambda_-^q\). Positivity of the Perron eigenvector requires \(A_+>0,A_->0\). On this region the left side is strictly increasing in \(\Lambda\), from zero at the larger diagonal threshold to infinity, proving existence and uniqueness.

**3. Entire large-deviation principle.** The pressure is finite and differentiable on the whole real line. Since \(X_t/t\in[-v,v]\), exponential tightness is automatic. Gärtner–Ellis gives the good convex Legendre rate and the lower bound on its exposed interior; smooth strict convexity follows from the nonzero asymptotic fluctuation variance of the additive velocity functional of the irreducible finite-state chain (or by differentiating the strictly monotone pressure equation). The rate function is continuous on the closed attainable interval, with endpoint values derived in Step 4. Open sets meeting either edge also contain attainable interior points arbitrarily near that edge, which extends the lower bound to the full interval. Sets outside are impossible. Hence the full upper and lower large-deviation bounds hold.

**4. Ballistic edges.** At \(\theta\to+\infty\), write \(\Lambda=v\theta-\lambda_++\delta\), \(\delta>0\). Then
\[
\delta^p(\delta+2v\theta+\lambda_--\lambda_+)^q=\lambda_+^p\lambda_-^q.
\]
Because the second factor diverges, \(\delta\to0\); dividing by its leading power gives the stated coefficient and exponent. At negative tilt exchange the signs and shapes. The intercepts \(\Lambda(\theta)-v|\theta|\to-\lambda_{\operatorname{edge}}\) give \(I(\pm v)=\lambda_\pm\), since the Legendre supremum is attained in the respective infinite-tilt limit.

**5. Complete Markov-alias classification.** If \(p=q=m\), positivity permits taking the positive \(m\)-th root, leaving \(A_+A_-=\lambda_+\lambda_-\), exactly the quadratic eigenvalue equation of a two-state telegraph process with transition rates \(\lambda_+,\lambda_-\). Therefore their pressures, and Legendre rates, coincide at every argument. Solving this quadratic and taking the Legendre transform gives the displayed closed form of \(I\). Conversely, suppose the pressure equals that of *some* two-state telegraph chain with the same velocities and positive rates \(a,b\). Its positive/negative infinite-tilt intercepts must be \(-a,-b\), so \(a=\lambda_+\), \(b=\lambda_-\). Its corrections at both edges are proportional to \(|\theta|^{-1}\), while the Erlang corrections have positive nonzero coefficients and powers \(q/p\), \(p/q\). Equality therefore forces \(p=q\). Equality of rate functions implies equality of pressures by convex biconjugation, completing the if-and-only-if classification.

**6. Finite-time inequivalence.** Start in the first positive stage. The ballistic atom at \(X_t=vt\) is exactly the event of no complete positive run before time \(t\):
\[
\Pr(X_t=vt)=e^{-\lambda_+t}\sum_{j=0}^{p-1}\frac{(\lambda_+t)^j}{j!}.
\]
For the Markov comparator the atom is \(e^{-\lambda_+t}\). They differ for every \(t>0\) when \(p=q>1\); hence matching the full displacement large-deviation function does not imply matching the finite-time distributions.

## Verification
A standalone Python program `verify_pressure.py` reconstructs the phase generators and computes their eigenvalues independently of the scalar characteristic-root method. It tests \(p,q\in\{1,2,3,4\}\), independent pseudorandom rates, speeds and tilts, the equal-shape Markov identity, and asymptotic edge corrections across five asymmetric/symmetric examples. The program currently passes 140 deterministic comparisons; the worst absolute spectral/root discrepancy was below \(1.3\times10^{-11}\). Numerical checks corroborate the finite-matrix steps but are not substitutes for the proof above. Run `python verify_pressure.py` with NumPy and SciPy installed.

## Relationship to prior work
Singh and Aghion (2026) study the bistable potential, constant-rate tumbling, thermal noise and first passage; they explicitly identify non-Markovian tumbling as a next direction. The present theorem concerns the *unconfined, zero-thermal-noise benchmark*, not that paper's bistable escape problem. Di Crescenzo (2001) studies alternating Erlang telegraph motion and derives finite-time densities, establishing the underlying model. De Gregorio and Macci (2012) and Macci (2016) establish large-deviation results for classical and more general telegraph processes. Hu, Pozdnyakov and Yan (2022) derive finite-time occupation distributions for a different multistate on–off model. Those density, model and general-theory results are not claimed here. The narrower assessed contribution is the **exact if-and-only-if matching of the entire large-deviation rate within the two-sided Erlang family**, together with its asymmetric edge-ratio discrimination. Broader finite-time formulas and general renewal large-deviation theorems may implicitly contain this equivalence; a complete priority determination requires further expert comparison of the inaccessible 2001 and 2016 full texts.

## Limitations
No first-passage, confinement, reset, entropy-production, central-time scaling uniformity, or multidimensional active motion is proved. The equality concerns the leading speed-\(t\) large-deviation *rate only*, not all subexponential prefactors or finite-dimensional temporal statistics. Neither external independent validation nor a priority guarantee has been obtained.

## References
1. R. K. Singh and E. Aghion, *Spatial density, first passage times, and entropy of run and tumble particles in a bistable potential* (2026), arXiv:2610.08029v1, https://arxiv.org/html/2610.08029v1; posted October 6, 2026.
2. A. Di Crescenzo, *On random motions with velocities alternating at Erlang-distributed random times*, Adv. Appl. Probab. **33** (2001), 690–701, doi:10.1239/aap/1005091360.
3. A. De Gregorio and C. Macci, *Large deviation principles for telegraph processes*, Statist. Probab. Lett. **82** (2012), 1874–1882, doi:10.1016/j.spl.2012.06.023.
4. C. Macci, *Large deviations for some non-standard telegraph processes*, Statist. Probab. Lett. **110** (2016), 119–127, doi:10.1016/j.spl.2015.12.016.
5. C. Hu, V. Pozdnyakov and J. Yan, *On occupation time for on-off processes with multiple off-states*, Modern Stochastics Theory and Applications **9** (2022), 413–430, https://doi.org/10.15559/22-VMSTA210.
