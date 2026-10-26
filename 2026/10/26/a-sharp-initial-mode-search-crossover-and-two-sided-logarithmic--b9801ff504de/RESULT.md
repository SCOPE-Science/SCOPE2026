# A sharp initial-mode search crossover and two-sided logarithmic reset-rate reentrance

## Finding

In the symmetric diffusion–ballistic intermittent search model of Flaquer-Galmés, Campos and Méndez [1], the ballistic-start strategy can beat the diffusion-start strategy at a sufficiently distant absorbing target **if and only if**
\[
v^2>D(q+r),
\]
where \(D\) is diffusivity, \(v\) ballistic speed, \(q\) the ballistic-to-diffusive switching rate and \(r\) the Poisson resetting rate. The boundary does not depend on the diffusive-to-ballistic switching rate \(p\). When the inequality holds, there is exactly one target distance \(x_*(r)>0\) at which the two mean first-arrival times coincide: diffusion-start is better for \(0<x<x_*(r)\), and ballistic-start is better for \(x>x_*(r)\). When the inequality fails, diffusion-start is strictly better at every positive distance.

More precisely, fix \(D,p,q,r,v>0\), and define
\[
B=\frac{r+p}{D}+\frac{(r+q)^2}{v^2},\qquad
C=\frac{r(r+q)(r+p+q)}{Dv^2},\qquad
\lambda_\pm=\sqrt{\frac{B\pm\sqrt{B^2-4C}}2},\qquad
K=\frac{r(r+q)}{v^2}.
\]
These satisfy \(0<\lambda_-<\lambda_+\). In the ballistic-advantage regime, the unique crossover is
\[
x_*(r)=\frac{1}{\lambda_+-\lambda_-}
\log\!\left(\frac{\lambda_-(\lambda_+^2-K)}{\lambda_+(\lambda_-^2-K)}\right).
\]

For fixed \(D,p,q,v\) with \(v^2>Dq\), set \(r_c=v^2/D-q>0\) and \(\lambda_0=\sqrt{p/D+q^2/v^2}\). The crossover exists exactly for \(0<r<r_c\), and **diverges logarithmically at both ends**:
\[
\lim_{r\downarrow0}\frac{x_*(r)}{\log(q/r)}=\frac1{2\lambda_0},\qquad
\lim_{r\uparrow r_c}\frac{x_*(r)}{\log(r_c/(r_c-r))}
=\frac{1}{\sqrt{(r_c+p+q)/D}-\sqrt{r_c/D}}.
\]
Consequently, for every sufficiently large fixed target distance, ballistic-start outperforms diffusion-start for some intermediate reset rates but not for sufficiently small or sufficiently large ones. No claim of uniqueness of the optimal rate or of connectedness of the advantageous-rate set is made.

## Assumptions and scope

The state space is \(\mathbb R\times\{\mathrm D,+,-\}\). In state \(\mathrm D\) the position evolves by Brownian diffusion with generator \(D\partial_{xx}\). In states \(+\) and \(-\) it moves at fixed velocities \(+v\) and \(-v\), respectively. Transitions \(\mathrm D\to\pm\) each occur at rate \(p/2\), and \(\pm\to\mathrm D\) at rate \(q\). A target sits at the origin and captures the particle only in the diffusive state; passing through it during a ballistic relocation does not count as detection. The particle starts at position \(x>0\), either in diffusion or in an equiprobable mixture of the two ballistic headings. Independently, Poisson events of rate \(r>0\) reset **both the position and the internal state** to this respective initial configuration. We compare the two finite mean capture times \(T_{\mathrm D}(x;r)\) and \(T_{\mathrm B}(x;r)\), without optimizing \(p,q,v\) between strategies. All parameters are strictly positive; the zero-rate or infinitely fast limits are not asserted as separate model cases.

## Proof

For a search attempt *without* resetting, let \(F_{\mathrm D}(x;s)\) and \(F_{\mathrm B}(x;s)\) be the Laplace transforms of target-detection time from diffusion and an equally mixed ballistic initial state, respectively. The published solution [1, equations (22) and (25)] supplies, at \(s=r\),
\[
\phi_\pm=\frac{(r+q)^2}{v^2\lambda_\pm}-\lambda_\pm,
\qquad A_0=\frac{q(r+q)}{v^2},
\]
\[
F_{\mathrm D}(x;r)=\frac{\phi_-e^{-\lambda_-x}-\phi_+e^{-\lambda_+x}}{\phi_--\phi_+},\quad
F_{\mathrm B}(x;r)=\frac{A_0(e^{-\lambda_-x}/\lambda_--e^{-\lambda_+x}/\lambda_+)}{\phi_--\phi_+}.
\]
Here the formulas have been rewritten using \(p=1/\tau_D\) and \(q=1/\tau_v\). Renewal at complete Poisson resets [1, equations (35)–(38)] gives
\[
T_j(x;r)=\frac{1-F_j(x;r)}{rF_j(x;r)},\qquad j\in\{\mathrm D,\mathrm B\},
\]
so smaller mean is equivalent to larger \(F_j\). Both transforms are strictly positive because there is positive probability of detection before the next reset.

First establish that the two decay parameters are real and distinct without relying on numerical roots. For \(P(z)=z^2-Bz+C\) and \(h=(r+q)^2/v^2\), direct algebra yields
\[
P(h)=-\frac{pq(r+q)}{Dv^2}<0.
\]
Since \(B,C>0\), this entails \(0<\lambda_-^2<h<\lambda_+^2\). In particular
\(\phi_--\phi_+=(\lambda_+-\lambda_-)[1+h/(\lambda_-\lambda_+)]>0\).

Set \(c_\pm=(\lambda_\pm^2-K)/\lambda_\pm\). Subtraction and \(h-A_0=K\) produce the exact sign identity
\[
F_{\mathrm B}(x;r)-F_{\mathrm D}(x;r)=
\frac{c_-e^{-\lambda_-x}-c_+e^{-\lambda_+x}}{\phi_--\phi_+}.
\]
Because \(K<h<\lambda_+^2\), one has \(c_+>0\), and
\(c_+-c_-=(\lambda_+-\lambda_-)[1+K/(\lambda_+\lambda_-)]>0\). A second polynomial evaluation gives
\[
P(K)=\frac{qr(r+q)}{Dv^4}\,[v^2-D(r+q)].
\]
Since \(K<\lambda_+^2\), this implies \(c_->0\) exactly when \(v^2>D(r+q)\), and \(c_-\le0\) otherwise. If \(c_-\le0\), the difference of transforms is negative at every \(x\ge0\). If \(c_->0\), the ratio of the two positive exponential terms is
\(\frac{c_-}{c_+}e^{(\lambda_+-\lambda_-)x}\), which increases strictly from a value below one to infinity. Hence there is precisely one sign change at the stated \(x_*(r)\), proving the complete comparison.

For the two logarithmic laws, suppose \(v^2>Dq\) and keep \(D,p,q,v\) fixed. As \(r\downarrow0\),
\[
\lambda_-^2\sim \frac{rq(p+q)}{pv^2+Dq^2},\qquad
\lambda_+\longrightarrow\lambda_0,\qquad
\lambda_-^2-K\sim\frac{rq^2(v^2-Dq)}{v^2(pv^2+Dq^2)}.
\]
Consequently \(c_-\) is a positive constant times \(\sqrt r\), whereas \(c_+\to\lambda_0\). Substitution into the logarithmic formula yields the first limit. At \(r=r_c\), \(\lambda_-^2=K=r_c/D\) and \(\lambda_+^2=(r_c+p+q)/D\); the previous factorization shows \(\lambda_-^2-K\) vanishes to first order in \(r_c-r\), whereas \(c_+\) stays positive. This proves the second limit. Continuity and divergence at the two ends imply that \(x_*(r)\) has an attained finite positive minimum on \((0,r_c)\). Every target beyond that minimum has at least one intermediate resetting-rate interval of ballistic superiority, while it has none near either endpoint. These are statements about the full stationary-reset first-arrival mean, not about sample paths under a shared coupling.

## Verification

The standalone script `verify_mode_crossing.py` verifies both polynomial identities symbolically with SymPy, independently evaluates the original two first-passage formulas and the factored sign identity at several positive parameter choices, tests the strict inequalities on both sides of calculated crossover distances, and checks the two logarithmic limits numerically. The script also gives an explicit fixed-distance, reentrant-rate example with \(D=p=q=1\), \(v=2\), and \(x=4\). Run `python verify_mode_crossing.py` in a Python environment with SymPy installed. The proof above, not the finite numerical checks, establishes the statements for all admitted real parameters.

## Relationship to prior work

The source [1] supplies the exact no-reset first-arrival transforms and the resetting renewal expression for both initial modes, including their large-distance mean-time ratio. These formulas are prior work; they are not claimed here. The present result is the global *relative-order theorem*: a necessary-and-sufficient simple speed/reset threshold independent of \(p\), strict uniqueness of the distance where the preferred starting mode changes, and the two logarithmically diverging boundaries in reset rate. Figures 6–11 of [1] treat first-arrival behavior and optimize switching parameters for each initial mode separately, but do not state this comparative theorem. General intermittent-search [2] and resetting [3] results motivate the setting but do not provide this three-state threshold. As all comparisons derive from the exact source formulas, independent priority checking should specifically scrutinize whether an equivalent interpretation of those formulas has previously been stated elsewhere.

## Limitations

This is a mathematically derived comparative property of the exact one-dimensional, exponential-switching, complete-reset model. Resetting only position without restoring the initial internal mode, biased choices of ballistic direction, finite target width, non-Poisson resets, and spatially heterogeneous motion are not covered. The existence of a reentrant reset-rate advantage does not establish a single connected advantageous interval or a unique optimal reset rate. The first-passage transform formulas belong to [1]; the new assertion is their global, parameter-sharp comparison and endpoint scaling.

## References

[1] R. Flaquer-Galmés, D. Campos, and V. Méndez, *Intermittent random walks under stochastic resetting*, Physical Review E **109**, 034103 (2024). First public preprint 2024-01-30, arXiv:2401.16849, https://arxiv.org/abs/2401.16849 ; full publisher article DOI:10.1103/PhysRevE.109.034103.

[2] O. Bénichou, C. Loverdo, M. Moreau, and R. Voituriez, *Intermittent search strategies*, Reviews of Modern Physics **83**, 81 (2011), DOI:10.1103/RevModPhys.83.81.

[3] M. R. Evans, S. N. Majumdar, and G. Schehr, *Stochastic Resetting and Applications*, Journal of Physics A **53**, 193001 (2020), DOI:10.1088/1751-8121/ab7cfe.
