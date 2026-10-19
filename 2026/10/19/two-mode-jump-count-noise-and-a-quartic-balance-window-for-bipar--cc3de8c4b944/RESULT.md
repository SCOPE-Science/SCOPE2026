# Two-mode jump-count noise and a quartic balance window for bipartite exclusion

## Finding

Take integers \(a,b\ge1\), \(N=a+b\ge4\), and \(1\le k<N\). On the complete bipartite graph \(K_{a,b}\), place exactly \(k\) indistinguishable exclusion particles. Each occupied--vacant edge exchanges its endpoints at rate one, independently of other available exchanges. Start in the uniform stationary law on \(k\)-element occupied sets, and let \(C_T\) count **all actual particle jumps** during \([0,T]\), regardless of direction. Write
\[
\mu=\lim_{T\to\infty}\frac{\mathbb E C_T}{T},\qquad
F=\frac{\lim_{T\to\infty}\operatorname{Var}(C_T)/T}{\mu}.
\]
Then the exact activity rate and Fano ratio are
\[
\boxed{\mu=\frac{2abk(N-k)}{N(N-1)}}
\]
and
\[
\boxed{F=1+
\frac{(a-b)^2(N-2k)^2}{N^2(N-2)^2}
+\frac{4(a-1)(b-1)(k-1)(N-k-1)}{(N-3)(N-2)^2(N-1)^2}.}
\]
Both corrections are nonnegative. In particular, \(F=1\) **if and only if** either (i) \(a=b\) and \(k\in\{1,N-1\}\), or (ii) \(\min(a,b)=1\) and \(N=2k\). On precisely those cases the total jump count is in fact a homogeneous Poisson process, because the exit rate is constant over every accessible configuration. All other admissible parameters give \(F>1\).

For sequences \(N\to\infty\) with \(a/N\to\alpha\in(0,1)\) and \(k/N\to\rho\in(0,1)\),
\[
\boxed{F\longrightarrow 1+(1-2\alpha)^2(1-2\rho)^2.}
\]
The generic positive macroscopic excess disappears if either the partition or the particle inventory approaches one-half. At the **joint balance boundary**
\[
\frac{a}{N}=\frac12+uN^{-1/4}+o(N^{-1/4}),\qquad
\frac{k}{N}=\frac12+vN^{-1/4}+o(N^{-1/4}),
\]
for fixed real \(u,v\), the two noise contributions compete on the same scale, giving
\[
\boxed{\lim_{N\to\infty}N(F-1)=\frac14+16u^2v^2.}
\]
These are Fano-ratio statements: \(F\to1\) does not, by itself, show convergence of the entire rescaled jump-count law to a Poisson process.

## Assumptions and scope

The graph is finite, simple and completely bipartite. Each *undirected* occupied--empty edge has rate one for the allowed exchange; there is no independent per-vertex degree normalization, no external birth/death or reservoir, and no unsuccessful attempt counted. Every \(k\)-set of occupied vertices has equal stationary probability, because forward and backward rates coincide. Irreducibility holds for \(1\le k<N\). In the formulas the symbol \(k\) is the conserved particle number and \(C_T\) is the accumulated count; no limit in \(k\) is implicit in the finite-size theorem. The restriction \(N\ge4\) removes singular low-order factorial-moment denominators; small two- and three-vertex graphs are not claimed by the displayed rational formula.

## Proof

**1. Symmetry reduction and stationary moments.** Let \(J_t\) be the number of occupied vertices in the size-\(a\) part. Its birth and death rates, for each feasible integer \(j\), are respectively
\[
u_j=(a-j)(k-j),\qquad d_j=j(b-k+j).
\]
The lumped generator \(Q\) acts by \((Qf)(j)=u_j[f(j+1)-f(j)]+d_j[f(j-1)-f(j)]\), omitting transitions outside its feasible range. Its reversible stationary law is hypergeometric:
\[
\pi_j=\frac{\binom aj\binom b{k-j}}{\binom Nk}.
\]
The instantaneous total rate of **successful jumps** is
\[
\lambda(j)=u_j+d_j=ak+(b-a-2k)j+2j^2.
\]
Uniformity of the original configuration law or direct counting gives \(\mu=\mathbb E_\pi\lambda=2abk(N-k)/[N(N-1)]\). Set \(m=ak/N\), \(X=j-m\), and \(v=\mathbb E_\pi X^2=abk(N-k)/[N^2(N-1)]\). Hypergeometric falling-factorial moments satisfy
\[
\mathbb E_\pi[(J)_r]=\frac{(a)_r(k)_r}{(N)_r}
\quad(0\le r\le4),
\]
with \((z)_r=z(z-1)\cdots(z-r+1)\), and terms with impossible ranks interpreted as zero. They imply
\[
\frac{\mathbb E_\pi X^3}{v}=c=\frac{(b-a)(N-2k)}{N(N-2)}.
\]
Define the degree-two centered mode \(H_2=X^2-cX-v\). It is orthogonal to \(1\) and \(X\) in \(L^2(\pi)\). The fourth-moment identity gives
\[
\mathbb E_\pi H_2^2=
\frac{2abk(a-1)(b-1)(k-1)(N-k)(N-k-1)}
{N(N-3)(N-2)^2(N-1)^2}.
\]
The identity includes zero-norm cases by continuity of the displayed polynomial expression, without division by a zero variance: \(v>0\) throughout the hypotheses.

**2. Exactly two relaxation modes.** Direct use of \(u_j-d_j=ak-Nj\) shows
\[
QX=-NX,\qquad QH_2=-2(N-1)H_2.
\]
Since \(\lambda\) is quadratic and \(X^2=H_2+cX+v\), its centered decomposition is
\[
\lambda-\mu=c_1X+2H_2,\qquad
c_1=\frac{(b-a)(N-2k)}{N-2}.
\]
Consequently the unique mean-zero solution of the Poisson equation \(-Qh=\lambda-\mu\) is
\[
h=\frac{c_1}{N}X+\frac{1}{N-1}H_2.
\]
This eigenmode argument remains valid when \(H_2\equiv0\) on a two-state lumped chain.

**3. Counted-jump cumulants.** Let \(B\) be the off-diagonal jump operator, \((Bf)(j)=u_jf(j+1)+d_jf(j-1)\). Counting every real hop tilts the generator to \(Q_s=Q+(e^s-1)B\). Its principal eigenvalue \(g(s)\) is analytic near zero by finite-state irreducibility; \(g'(0)=\mu\), and differentiating the stationary eigenvector equation gives
\[
g''(0)=\mu+2\mathbb E_\pi[(Bh)(J)]=\mu+2\mathbb E_\pi[\lambda h].
\]
The second equality uses \(B=Q+\operatorname{diag}(\lambda)\) and stationarity \(\mathbb E_\pi Qh=0\). Orthogonality of \(X\) and \(H_2\) yields
\[
F-1=\frac2\mu\left[\frac{c_1^2v}{N}+\frac{2\mathbb E_\pi H_2^2}{N-1}\right].
\]
Substitution of the exact moment identities gives the two displayed nonnegative rational corrections. The finite-state counting-cumulant limits exist and equal \(g'(0),g''(0)\); the stationary initial law removes transient normalization issues.

**4. Equality, classification, and scaling.** The first correction vanishes precisely if \(a=b\) or \(N=2k\). The second vanishes precisely if at least one of \(a,b,k,N-k\) equals one. Under \(N\ge4\) these conditions combine exactly into cases (i) and (ii) in the finding. In each, \(\lambda(j)\) is constant across the feasible states, and its exponential holding-time clock makes \(C_T\) a homogeneous Poisson process. Otherwise \(F>1\).

Write \(\alpha_N=a/N\), \(\rho_N=k/N\). The first correction is \((1-2\alpha_N)^2(1-2\rho_N)^2[1+O(N^{-1})]\), and the second is \(4\alpha_N(1-\alpha_N)\rho_N(1-\rho_N)/N+o(N^{-1})\) when the two proportions remain bounded away from zero and one. These give the generic limit. Under the jointly tuned \(N^{-1/4}\) deviations, multiplying by \(N\) gives \(16u^2v^2\) and \(1/4\) respectively, proving the quartic balance law. All asymptotic assertions refer to integer sequences satisfying the displayed convergence assumptions.

## Verification

The standalone command \(python verification/verify.py\) (SymPy dependency listed in \(verification/requirements.txt\)) reconstructs independent full configuration generators, solves their Poisson equations over the rationals, and compares the resulting counting Fano ratios with the theorem for **59** admissible \((a,b,k)\) triples with \(1\le a,b\le4\) and \(N\ge4\). It also verifies symbolically the hypergeometric degree-two norm identity and evaluates five increasing-size examples inside the joint balance window. The code uses no unstated inputs. The exact 59-state-family comparisons and the generic symbolic identity are reproducibility checks; the proof above, not finite enumeration, establishes the all-size claim.

## Relationship to prior work

Mendonça, arXiv:1207.4106 (first posted 2012-07-17), Section 4, already identifies the generator structure and complete-bipartite exclusion spectrum. The rates, stationary symmetry, and the existence of the first two relaxation modes are not claimed as new. The present statement instead evaluates the **long-time second cumulant of every actual exchange**, separates it into two positive hypergeometric modes, classifies precisely Poisson jump counts, and derives a jointly balanced \(N^{-1/4}\) window. These cumulant and scaling conclusions were not identified in the inspected full-text sections.

Stinchcombe and de Queiroz, arXiv:1202.0774 (first posted 2012-02-03), study *instantaneous* static activity distributions in a one-dimensional **totally asymmetric** exclusion process; their definitions in the Introduction explicitly distinguish that snapshot variable from integrated event counts. Their static cumulants do not imply the present integrated-jump Fano ratio on complete bipartite graphs. More general spectral/orthogonal-polynomial and current-counting approaches can, in principle, imply the result; no claim of invention of those methods is made. Targeted comparisons are described in the accompanying review.

## Limitations

The result requires the complete bipartite topology, identical unit exchange rates for every edge, strict exclusion and fixed particle number. It provides only the first two **long-time jump-count cumulants**, not a finite-time distribution or all higher cumulants. A limiting Fano ratio equal to one is not a Poisson-process convergence theorem. Novelty remains contingent on historical comparison: an unlocated equivalent formula in the Bernoulli--Laplace or activity large-deviation literature could supersede the present evaluation, although no such exact formula was found in the inspected primary materials.

## References

1. J. R. G. Mendonça, *Exact eigenspectrum of the symmetric simple exclusion process on the complete, complete bipartite, and related graphs*, arXiv:1207.4106, first public version 17 July 2012; https://arxiv.org/html/1207.4106v4 ; https://arxiv.org/abs/1207.4106 .
2. R. B. Stinchcombe and S. L. A. de Queiroz, *Statistics of current activity fluctuations in asymmetric flow with exclusion*, arXiv:1202.0774, first public version 3 February 2012; https://arxiv.org/abs/1202.0774 .
3. P.-E. Roche, B. Derrida, and B. Douçot, *Mesoscopic Full Counting Statistics and Exclusion Models*, arXiv:cond-mat/0312659, first posted 27 December 2003; https://arxiv.org/abs/cond-mat/0312659 . A general counted-current framework, not a claim of a completed complete-bipartite activity calculation.
