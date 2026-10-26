# The sharp dimension-dependent true-residual frontier for single-row DEIM–GMRES

## Finding

Consider the one-dimensional, non-oversampled, deterministically row-sketched GMRES step in dimension \(n\ge2\), with a row selected by the discrete empirical interpolation method (DEIM). Let \(0<\mu\le L\), \(\kappa=L/\mu\), and
\[
q=\frac{\kappa-1}{2\sqrt\kappa}, \qquad q_{\mathrm{pole}}=\frac1{\sqrt{n-1}}.
\]
Over all real symmetric matrices \(A\) with \(\mu I\preceq A\preceq LI\), and all nonzero initial residual vectors \(r\), with the one sampled value \((Ar)_i\ne0\), the **exact** supremum of the ratio of the *true* residual norms is
\[
\boxed{
\sup_{A,r}\frac{\|r_+\|_2}{\|r\|_2}=
\begin{cases}
\displaystyle\frac{\sqrt n\,q}{1-\sqrt{n-1}\,q},&0\le q<1/\sqrt{n-1},\\[5pt]
+\infty,&q\ge1/\sqrt{n-1}.
\end{cases}}
\]
In the finite branch, the maximum is **attained** (including with a deterministic tie convention for DEIM), and is approachable with a unique maximum-magnitude sampled coordinate. The infinite branch means that nonsingular sampled least-squares problems have arbitrarily large true residuals, not that a pseudoinverse returns infinity at exact singularity.

Put \(\tau_n=\sqrt n-\sqrt{n-1}\). Consequently, the update is universally nonexpansive in the original Euclidean residual norm **if and only if**
\[
q\le\tau_n
\quad\Longleftrightarrow\quad
\kappa\le\bigl(\tau_n+\sqrt{1+\tau_n^2}\bigr)^2.
\]
For every fixed \(\kappa>1\), sufficiently large \(n\) falls into the infinite branch. This is a worst-case obstruction specific to the one-row, unoversampled sketch, not to conventional GMRES or a sketch embedding the full residual search space.

## Assumptions and scope

Let \(n\ge2\), \(0<\mu\le L\), \(A=A^{\mathsf T}\in\mathbb R^{n\times n}\), and \(\mu I\preceq A\preceq LI\). Let \(r\ne0\) be the initial residual of a consistent nonsingular linear system; any such vector is realizable by choosing an appropriate right-hand side and initial iterate. Set \(m=s=1\) in the DEIM variant of the deterministically sketched GMRES algorithm. The Krylov basis is proportional to \(r\), so DEIM picks any coordinate \(i\) attaining \(\max_j|r_j|\). The sampled least-squares problem minimizes \(|(r-\alpha Ar)_i|\). Whenever \((Ar)_i\ne0\), the unique coefficient and the true residual are
\[
\alpha=\frac{r_i}{(Ar)_i},\qquad r_+=r-\alpha Ar.
\]
The bound is a supremum over the specified spectral interval (and is sharp even with the smallest and largest eigenvalues exactly \(\mu\) and \(L\)). A tie between maximal coordinates can be resolved by any fixed deterministic convention after reindexing coordinates. Strictly unique pivots approximate sharpness. Statements concern a single exact-arithmetic update and do not assert stability under repeated restarting, other sketches, or floating-point errors. A singular sampled operator invokes a separate pseudoinverse convention; the finite/infinite dichotomy concerns nonsingular samples.

## Proof

**1. Exact residual identity.** Scale \(r\) to \(u=r/\|r\|_2\). Replace the selected coordinate vector by \(e=\operatorname{sgn}(u_i)e_i\), so \(c=e^{\mathsf T}u=|u_i|\in[1/\sqrt n,1]\). When \(c<1\) let \(s=\sqrt{1-c^2}\) and \(w=(e-cu)/s\), a unit vector perpendicular to \(u\). Write \(Au=a u+v\), where \(a=u^{\mathsf T}Au>0\), \(v\perp u\), \(p=\|v\|_2\), and \(h=w^{\mathsf T}v\in[-p,p]\). Then \(e^{\mathsf T}Au=ca+sh\) and
\[
\frac{r_+}{\|r\|_2}=\frac{s h\,u-cv}{ca+sh},\qquad
\frac{\|r_+\|_2^2}{\|r\|_2^2}=
\frac{s^2h^2+c^2p^2}{(ca+sh)^2}.
\]
If \(c=1\), the same bound follows directly from \(\|r_+\|_2/\|r\|_2=p/a\), with \(s=0\).

**2. Exact spectral angular bound.** The matrix polynomial \((A-\mu I)(LI-A)\) is positive semidefinite. Taking its quadratic form on \(u\) yields \(p^2\le(a-\mu)(L-a)\). Elementary maximization for \(a\in[\mu,L]\) gives
\[
\frac pa\le \max_{a\in[\mu,L]}\frac{\sqrt{(a-\mu)(L-a)}}a
=\frac{L-\mu}{2\sqrt{\mu L}}=q,
\]
with equality at \(a=2\mu L/(\mu+L)\). The case \(\mu=L\) gives \(v=0\) and exact elimination.

**3. Finite supremum and sharpness.** Suppose \(\sqrt{n-1}\,q<1\). Since \(s/c\le\sqrt{n-1}\), the sampled denominator satisfies \(ca+sh\ge a(c-sq)>0\), and the exact numerator is at most \(p\), because \(|h|\le p\). Therefore
\[
\frac{\|r_+\|_2}{\|r\|_2}
\le\frac{p}{ca-sp}
\le\frac{q}{c-sq}
\le\frac{\sqrt n\,q}{1-\sqrt{n-1}\,q}.
\]
The last step follows since \(c\ge1/\sqrt n\) makes \(c-q\sqrt{1-c^2}\) strictly increasing in \(c\).

For equality put \(u=\mathbf1/\sqrt n\), choose \(e=e_1\), set \(c=1/\sqrt n\), \(s=\sqrt{1-1/n}\), and \(w=(e-cu)/s\). Define \(\rho=\mu/(\mu+L)\) and
\[
z=\sqrt\rho\,u-\sqrt{1-\rho}\,w,\qquad A=\mu I+(L-\mu)zz^{\mathsf T}.
\]
Then \(\|z\|_2=1\), \(A\) has extremal eigenvalues exactly \(\mu,L\), and \(Au=au-pw\), with
\[
a=\frac{2\mu L}{\mu+L},\qquad
p=\frac{(L-\mu)\sqrt{\mu L}}{\mu+L},\qquad p/a=q.
\]
Thus \(h=-p\), each numerator and denominator inequality is an equality, and coordinate one is a permissible DEIM maximizer. Small perturbations of \(r\) give a unique pivot and approximate the same supremum.

**4. Blow-up at and above the pole.** In the same construction keep \(u,w\) fixed and vary \(\rho\in(0,1)\). The ratio \(p/a\), now depending continuously on \(\rho\), ranges from \(0\) to the maximum \(q\). If \(q\ge c/s=1/\sqrt{n-1}\), select a sequence of \(\rho\)'s such that \(0<p/a<c/s\) and \(p/a\to c/s\). With \(h=-p\), the ratio \(p/(ca-sp)\) tends to \(+\infty\), and every sampled value remains nonzero. At the boundary \(q=c/s\), approach the maximizing \(\rho\) from one side. The same conclusion holds for uniquely maximal pivots by sufficiently small perturbations of \(r\) for each point in the sequence. Singular limiting samples are not used as algorithmic updates.

**5. Exact nonexpansion frontier.** In the finite branch the sharp factor is at most one precisely when \(q\le1/(\sqrt n+\sqrt{n-1})=\tau_n\). Since the finite branch is sharp and the other branch is unbounded, this is necessary and sufficient. Solving \((\kappa-1)/(2\sqrt\kappa)\le\tau_n\) for \(\sqrt\kappa\ge1\) gives the displayed equivalent condition-number threshold. In particular, for fixed \(\kappa>1\) the pole occurs once \(n\ge1+q^{-2}\) (with the correct integer interpretation).

**An exact two-dimensional illustration.** With \(\mu=1\), \(L=4\), \(r=(1,1)^{\mathsf T}\) and
\[
A=\begin{pmatrix}13/10&-9/10\\-9/10&37/10\end{pmatrix},
\]
the spectrum is \(\{1,4\}\). Selecting coordinate one gives \(Ar=(2/5,14/5)^{\mathsf T}\), \(\alpha=5/2\), and \(r_+=(0,-6)^{\mathsf T}\). Hence \(\|r_+\|_2/\|r\|_2=3\sqrt2\), which is exactly the theorem's finite worst-case factor at \(n=2\), \(\kappa=4\). The ordinary full-residual GMRES coefficient would instead minimize \(\|r-\alpha Ar\|_2\) and cannot increase the residual.

## Verification

Execute the self-contained Python script `verify.py` using a standard Python 3 interpreter. It checks a complete exact-rational sharpness example; exact rank-one extremizers in six dimension/condition-number pairs; blow-up sequences in dimensions two, three and five; perturbed unique-pivot cases; and 2,000 pseudorandom rank-one SPD tests against the finite sharp bound. It terminates with a `PASS` count. Numerical tests do not constitute the universal proof, supplied above.

## Relationship to prior work

Bergermann (2026), Algorithm 5.2 and Sections 2.3, 4.1 and 5.2, defines the deterministic DEIM row sketch and the relevant least-squares solve. For the one-dimensional Krylov basis, its pivot rule selects the largest-magnitude residual component. That paper analyzes basis embeddings and numerical examples rather than the precise **true residual norm** for the one-row extremal regime. Nakatsukasa and Tropp (2024) analyze randomized sGMRES under subspace-embedding assumptions; such an embedding cannot hold on the two-dimensional space \(\operatorname{span}\{r,Ar\}\) with a single sampled coordinate except when the vectors are dependent. The 2025 flexible-GMRES stabilization uses an outer minimization and therefore describes a different algorithm. Burke, Carson and Ma (2026) examine floating-point backward stability, not this exact-arithmetic worst-case row-selection frontier.

The Kantorovich-type bound \(p/a\le q\) is classical; it is not asserted as new. The contribution is its tight interaction with the **data-dependent DEIM row choice**, producing an attained rational-function dimension threshold, a sharp nonexpansion condition, and an actual singular-approach obstruction. General sketch bounds alone do not imply the exact result because they require hypotheses violated by the chosen single-row sketch. Exact historical priority outside inspected sources remains uncertain.

## Limitations

This is an exact-arithmetic, real SPD, **one-update** statement with one selected row and Krylov dimension one. It does not claim performance for larger sketch size, oversampling, other selection rules, indefinite matrices, preconditioning, finite-precision regularization or restarted multi-step convergence. The unbounded branch is about limiting nonsingular least-squares solves; the Moore–Penrose pseudoinverse at exactly zero sampled operator produces a finite output and is not being described as infinite. Although equality in the finite branch may use tied DEIM entries, the same supremum is approached with unique maximum-magnitude coordinates. Overlap with an uninspected historical special-case theorem remains possible.

## References

1. Kai Bergermann, *Deterministic sketching for Krylov subspace methods*, arXiv:2604.07158 (first public 8 April 2026), §§2.3, 4.1, 5.2, Algorithm 5.2. https://arxiv.org/abs/2604.07158
2. Yuji Nakatsukasa and Joel A. Tropp, *Fast and Accurate Randomized Algorithms for Linear Systems and Eigenvalue Problems*, SIAM J. Matrix Anal. Appl. **45** (2024), 1183–1214, doi:10.1137/23M1565413.
3. Stefan Güttel and John W. Pearson, *Stabilizing randomized GMRES through flexible GMRES*, arXiv:2506.18408 (2025).
4. Liam Burke, Erin Carson and Yuxin Ma, *On the Numerical Stability of Sketched GMRES*, SIAM J. Matrix Anal. Appl. (2026), doi:10.1137/25M1744629.
