# Arithmetic resonance and sharp frame degeneration for a one-sided Poisson shift flow

## Finding

For every integer \(q\ge2\), let \(S\) be the bilateral shift \((Sf)(n)=f(n-1)\) on \(\ell^2(\mathbb Z)\), and let the one-sided Poisson shift flow be \(R_t=\exp(t(S-I))\), for real \(t>0\). Consider the critical-density measurements
\[
\mathcal M_{q,t}f=\big(\{(R_t^k f)(qm)\}_{m\in\mathbb Z}\big)_{k=0}^{q-1}.
\]
The measurement operator is injective for every \(t>0\), but it is bounded below (hence gives stable recovery) **if and only if**
\[
t\notin\mathcal R_q:=\bigcup_{d=1}^{\lfloor q/2\rfloor}\left\{\frac{\pi m}{\sin(\pi d/q)}:m\in\mathbb N\right\}.
\]
The exceptional times are locally finite. At each exceptional time the reconstruction is unique but unstable.

The optimal squared lower frame bound
\[
A_q(t):=\inf_{\|f\|_2=1}\sum_{k=0}^{q-1}\sum_{m\in\mathbb Z}|(R_t^kf)(qm)|^2
\]
obeys the **sharp small-time law**
\[
\lim_{t\downarrow0}\frac{A_q(t)}{t^{2(q-1)}}=\binom{2q-2}{q-1}^{-1}.
\]
For every \(t_0\in\mathcal R_q\) there are positive constants \(c,C,\delta\), depending on \(q,t_0\), such that
\[
c|t-t_0|^2\le A_q(t)\le C|t-t_0|^2\quad(0<|t-t_0|<\delta).
\]
For \(q=2\), the leading constant at **every** exceptional time \(t_0=m\pi\), \(m\ge1\), is also exact:
\[
A_2(t)=\frac{|t-m\pi|^2}{1+e^{2m\pi}}+o(|t-m\pi|^2).
\]

## Assumptions and scope

All sequences are complex, with the usual \(\ell^2\)-norm. We use \(\widehat f(\theta)=\sum_{n\in\mathbb Z}f(n)e^{-in\theta}\) and normalized torus measure \(d\theta/(2\pi)\). The shift is unitary; \(R_t\) is a bounded convolution operator for all \(t\ge0\). The data use temporal powers \(R_t^k=R_{kt}\), including the time-zero sample, at the spatial sublattice \(q\mathbb Z\), with exactly \(q\) time channels. \(\sigma_{\min}\) denotes the smallest ordinary singular value of a complex matrix.

## Proof

**1. Exact direct-integral normalization.** The Fourier multiplier of \(R_t\) is
\[
a_t(\theta)=\exp\big(t(e^{-i\theta}-1)\big).
\]
For \(\phi\in[0,2\pi)\) define the \(q\) aliases \(\theta_j=(\phi+2\pi j)/q\) and \(w_j=\exp(t(e^{-i\theta_j}-1))\). Decimation by \(q\) gives the data Fourier transform
\[
G_k(\phi)=\frac1q\sum_{j=0}^{q-1}w_j^k\widehat f(\theta_j).
\]
Writing \(V_{kj}=w_j^k\), \(0\le k,j<q\), Parseval and the change of variables for the aliases yield
\[
\|\mathcal M_{q,t}f\|^2=\frac1{2\pi q^2}\int_0^{2\pi}\!\|V(\phi)F(\phi)\|_2^2\,d\phi,
\quad
\|f\|_2^2=\frac1{2\pi q}\int_0^{2\pi}\!\|F(\phi)\|_2^2\,d\phi.
\]
Here \(F_j(\phi)=\widehat f(\theta_j)\). Every square-integrable fiber vector is realized by some \(f\), and the eigenvalues depend continuously on the circle fiber (at the seam merely up to a column permutation). Consequently the **exact** sharp bound is
\[
A_q(t)=\frac1q\min_{\phi\in[0,2\pi]}\sigma_{\min}(V(\phi))^2.
\]
The corresponding optimal upper bound is given by the maximum of the largest singular value squared divided by \(q\), and is always finite.

**2. All resonance times.** A Vandermonde matrix is singular exactly when two nodes \(w_j,w_l\) coincide. Write \(z_j=e^{-i\theta_j}\). The collision condition is
\[
t(z_j-z_l)=2\pi i m,\qquad m\in\mathbb Z\setminus\{0\}.
\]
For circularly separated aliases by the shorter index distance \(d\in\{1,\ldots,\lfloor q/2\rfloor\}\), their chord length is \(2\sin(\pi d/q)\); varying \(\phi\) rotates that chord through every direction. Thus the collision is possible precisely at the displayed times \(\pi |m|/\sin(\pi d/q)\). At a fixed positive \(t\), each pair can collide at only finitely many fiber phases, since the chord direction equation has finitely many solutions. Hence the fiber matrix is invertible almost everywhere for **every** \(t>0\), which proves global injectivity, while a collision at even one phase makes the continuous essential infimum of its least singular value zero. This proves the stability classification.

**3. Exact small-time coefficient.** Put \(\eta=e^{-i\phi/q}\), \(\zeta=e^{-2\pi i/q}\), and \(z_j=\eta\zeta^j\). Right-multiply \(V\) by the unitary finite Fourier matrix \(U_{jr}=q^{-1/2}\zeta^{-jr}\). Expanding the exponential gives, for \(0\le r<q\),
\[
(VU)_{kr}=\sqrt q\,e^{-kt}\sum_{h\ge0}\frac{(kt\eta)^{r+hq}}{(r+hq)!}
=t^r\eta^r C_{kr}(t,\eta),
\]
where \(C(t,\eta)\to C_0\) uniformly over all unit-modulus \(\eta\) as \(t\downarrow0\), and \((C_0)_{kr}=\sqrt q\,k^r/r!\). Because \(C_0\) is the invertible polynomial-evaluation matrix on \(0,1,\ldots,q-1\), the inverse factorization is valid uniformly for small positive \(t\). After multiplication by \(t^{q-1}\), its only surviving row is the final row of \(C_0^{-1}\), up to a unit-modulus factor. Finite differences of degree \(q-1\) show that this row has entries
\[
\frac{(-1)^{q-1-k}}{\sqrt q}\binom{q-1}{k},\qquad 0\le k<q.
\]
The square of its Euclidean norm is \(q^{-1}\sum_k\binom{q-1}{k}^2=q^{-1}\binom{2q-2}{q-1}\). Therefore
\[
\lim_{t\downarrow0}t^{q-1}\|V(t,\phi)^{-1}\|=\sqrt{\frac1q\binom{2q-2}{q-1}}
\]
uniformly over all fibers. Inserting this into the exact frame-bound formula proves the asserted coefficient, not merely its exponent.

**4. Quadratic loss at every resonance.** Fix \(t_0\in\mathcal R_q\). The resonant set is discrete because every \(\sin(\pi d/q)\) is positive and there are only finitely many index gaps. Shrink a time neighborhood so that no other resonance occurs. If \(w_j=w_l=w_h\) for three distinct aliases at the same time and fiber, the differences \(t(z_j-z_l)\) and \(t(z_j-z_h)\) are imaginary. This would give three different points on the unit circle having the same real part, impossible. Thus each collision class has at most two nodes.

For a fixed pair of indices and nearby \(t\), the difference \(|t(z_j-z_l)|=2t\sin(\pi d/q)\) is at least a fixed multiple of \(|t-t_0|\) away from every nonzero integer multiple of \(2\pi i\) when approaching a possible collision at \(t_0\). Since complex exponentiation has simple zeros when subtracting one at \(2\pi i\mathbb Z\), a uniform local estimate gives \(|w_j-w_l|\ge c|t-t_0|\) near potential collision fibers. Away from collision fibers the differences are bounded below by compactness. The standard Lagrange interpolation formula for the inverse Vandermonde matrix has denominators \(\prod_{l\ne j}(w_j-w_l)\). In a neighborhood of a collision, no node belongs to more than one colliding pair, and every other factor remains bounded below. A finite compact cover of the fiber circle therefore gives
\[
\sup_\phi\|V(t,\phi)^{-1}\|\le \frac{C}{|t-t_0|}.
\]
This proves the required positive multiple **lower bound** for \(A_q(t)\). Conversely, at an actual collision phase \(\phi_0\), the unit vector supported on the two coinciding columns with opposite coefficients has image norm \(O(|t-t_0|)\) at nearby time. Evaluating the Rayleigh quotient there gives the matching **upper bound** for \(A_q(t)\). These arguments include simultaneous *disjoint* pair collisions.

**5. The sharp two-channel coefficient.** In the case \(q=2\), the fiber matrix has rows \((1,1)\) and \((e^{-t}e^{tz},e^{-t}e^{-tz})\), with \(z\) ranging over one half of the unit circle, and its determinant equals \(2e^{-t}\sinh(tz)\) up to sign. At \(t_0=m\pi\) the only collision phase has \(z=\pm i\); parametrizing a nearby phase by real \(u\), one has
\[
|\det V|^2=4e^{-2t_0}\big((t-t_0)^2+t_0^2u^2\big)+o((t-t_0)^2+u^2).
\]
The square of the *larger* singular value approaches \(2(1+e^{-2t_0})\), and the small singular value squared is the determinant squared divided by that large singular value squared. Minimizing over \(u\) and including the factor \(1/q=1/2\) gives the stated constant \((1+e^{2t_0})^{-1}\). Both sides of the collision phase seam give the same value.

## Verification

The accompanying standalone Python script `check_poisson_sampling.py` runs with Python 3 and NumPy. It performs 197 numerical consistency checks: exact predicted resonance phases for dimensions \(2\) through \(8\); Vandermonde determinant formulas; an independently implemented finite-cycle Fourier decimation identity; the small-time sharp coefficient for four dimensions across 21 fibers; and the sharp two-channel resonance coefficient at the first three resonances. The finite tests are not an infinite proof; all infinite quantifiers and constants follow analytically from the five proof steps above.

## Relationship to prior work

General dynamical-sampling frame and interpolation criteria based on fiber matrices and eigenvalue separation are established by Aguilera--Cabrelli--Carbajal--Paternostro (2019/2020) and, for Fourier multiplier observation families, Gardeazabal-Gutiérrez--Sousa (2025). Those criteria account for the general matrix-invertibility mechanism; neither inspected text gives the present global *arithmetic set* of exceptional Poisson times or the precise binomial small-time and quadratic near-resonance frame losses. The recent graph Paley--Wiener work of Bulai and coauthors (2026) provides the lattice graph dynamical-sampling motivation with a different, selfadjoint Laplacian evolution. Aldroubi and coauthors (2020) investigate heat-flow blind spots for real-line bandlimited signals, a different symmetric real-multiplier problem. No claim is made that generic Vandermonde inversion or abstract frame criteria are new.

## Limitations

This is a specific one-sided, nonselfadjoint shift-Poisson semigroup with exactly the critical number of consecutive temporal channels and a uniform sampling lattice. The result makes no assertion about arbitrary graph Laplacians, arbitrary shift-preserving operators, more or fewer channels, different spatial patterns, or discretization of continuous-time samples. For \(q>2\), the resonance collapse is proved to have **order two**, not an explicit leading coefficient. A previously unindexed specialization of abstract dynamical-sampling theorems is a residual priority risk. The separate literature assessment is not an independent audit.

## References

1. I. M. Bulai, C. Cabrelli, E. Cordero, U. Molter, S. Saliani, *Dynamical Sampling in Graph Paley--Wiener Spaces* (first public 2026-09-21), arXiv:2609.25472v1. https://arxiv.org/abs/2609.25472
2. I. Gardeazabal-Gutiérrez and M. Sousa, *Dynamical sampling, derivatives, and interpolation formulas in the Paley--Wiener space* (2025), arXiv:2506.16195. https://arxiv.org/abs/2506.16195
3. A. Aguilera, C. Cabrelli, D. Carbajal, V. Paternostro, *Dynamical Sampling for Shift-preserving Operators* (2019/2020), arXiv:1912.10348. https://arxiv.org/abs/1912.10348
4. A. Aldroubi, K. Gröchenig, L. Huang, P. Jaming, I. Krishtal, J. L. Romero, *Sampling the flow of a bandlimited function* (2020/2021), arXiv:2004.14032. https://arxiv.org/abs/2004.14032
