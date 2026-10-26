# Exact jump-activity noise for two-particle exclusion on Hamming graphs

## Finding

Let \(q\ge2\) and \(d\ge2\) be integers. On the Hamming graph \(H(d,q)=K_q^{\square d}\), place two indistinguishable hard-core particles, initially in the uniform stationary law on unordered pairs of distinct vertices. Each particle attempts, at rate one for each incident edge, to jump to its neighbor; attempts into the other occupied vertex are suppressed and are **not counted**. Let \(C_T\) count all successful jumps up to time \(T\), including those that leave the particles' Hamming separation unchanged. Define
\[
 N=q^d-1,\qquad w_j=\binom dj(q-1)^j,\qquad S_j=\sum_{h=j+1}^d w_h.
\]
Then the mean successful-jump rate and the stationary long-time count Fano ratio are exactly
\[
 \lim_{T\to\infty}\frac{\mathbb E C_T}{T}
 =\mu_{d,q}=2d(q-1)\frac{N-1}{N},
\]
\[
 F_{d,q}:=\lim_{T\to\infty}\frac{\operatorname{Var}(C_T)}{\mathbb E C_T}
 =1+\frac{2d}{N^2(N-1)}\sum_{j=1}^{d-1}\frac{S_j^2}{(d-j)w_j}.
\]
The sum is strictly positive: \(F_{d,q}>1\) for every \(q,d\ge2\). For the one-factor boundary \(H(1,q)=K_q\), \(q\ge3\), the successful-jump count is instead exactly Poisson with rate \(2(q-2)\), hence its Fano ratio is one. The fully occupied graph \(H(1,2)\) has no successful jumps, so a Fano ratio is not defined there.

For each **fixed** alphabet size \(q\ge2\), the excess noise has the sharp dimension-dependent asymptotic law
\[
 \boxed{\displaystyle \lim_{d\to\infty} \frac{d(q-1)q^d}{2}\,(F_{d,q}-1)=1.}
\]
Thus the first non-Poisson correction of this canonical two-particle interacting system is of order \(1/[d(q-1)q^d]\), with an evaluated coefficient. For example, \(F_{2,2}=10/9\), \(F_{3,2}=52/49\), and \(F_{2,3}=29/28\). No convergence in distribution of the full counting process to a Poisson process is asserted.

## Assumptions and scope

The graph's vertices are words of length \(d\) over an alphabet of cardinality \(q\). An edge changes exactly one coordinate to a different alphabet symbol. Hopping rates are one per oriented edge, so an isolated particle has total escape rate \(d(q-1)\). Time is continuous; rejected attempts are not counted; the particle number is exactly two. The uniform probability measure on unordered distinct-vertex pairs is stationary because every allowed transition has its reverse at the same rate. The finite chain is irreducible for \(d\ge2\). The limits defining the first two asymptotic count cumulants exist by finite-state Markov perturbation theory. The asymptotic limit in the finding keeps \(q\) fixed as \(d\) grows.

## Proof

**1. Radial reduction.** Let \(J\in\{1,\ldots,d\}\) be the Hamming distance between the two occupied vertices. Its stationary distribution is
\[
 \pi_j=\frac{w_j}{N},\qquad N=\sum_{j=1}^d w_j=q^d-1.
\]
For a radial test function \(g\), the induced birth-death generator \(L\) has upward rate
\[
 a_j=2(d-j)(q-1),\quad 1\le j<d,
\]
and downward rate \(b_j=2j\) when \(j\ge2\), with \(b_1=0\). For \(q>2\) there are also legal changes of alphabet letter leaving \(J\) fixed; those are **successful counted jumps**, but not jumps of \(J\). They disappear from \(L g\), not from the full counting observable. The detailed balance relation \(\pi_j a_j=\pi_{j+1}b_{j+1}\) is immediate.

**2. Exact jump intensity and its variance.** For \(D=d(q-1)\), the full two-particle chain's instantaneous total successful-hop intensity is
\[
 \lambda_j=2D-2\mathbf1_{\{j=1\}}.
\]
Only an adjacent pair blocks the two directed attempts along its common edge. Since \(\pi_1=D/N\), the stationary intensity is \(\mu=2D-2D/N\), proving the mean formula. Write \(P\) for the full uniform stationary law and \(Q\) for its generator. Its marked-jump tilted matrix has diagonal \(Q_{xx}\) and off-diagonal \(e^sQ_{xy}\). Differentiating its simple principal eigenvalue twice at zero gives
\[
 \lim_{T\to\infty}\frac{\operatorname{Var}(C_T)}{T}
 =\mu+2\langle \lambda-\mu,(-Q)^{-1}_{0}(\lambda-\mu)\rangle_P.
\]
Here the inverse is the Poisson inverse on mean-zero functions. This identity follows directly from the first two differentiated right-eigenvector equations: the first derivative is \(\mu\), the first right-eigenvector derivative solves \((-Q)u=\lambda-\mu\), and stationarity gives \(\langle 1,Q'_0u\rangle_P=\langle\lambda,u\rangle_P\). No assumption that the clock is a Cox or externally modulated Poisson process is made. Because \(\lambda-\mu=-2(\mathbf1_{\{J=1\}}-\pi_1)\), the Poisson equation is radial and can be solved with \(L\).

**3. Exact radial Green form.** Set \(f_j=\mathbf1_{\{j=1\}}-\pi_1\) and solve \((-L)g=f\), with \(\sum_j\pi_jg_j=0\). Summing the stationary-weighted Poisson equation over states \(1,\ldots,j\) yields the exact edge flux identity
\[
 \pi_ja_j(g_{j+1}-g_j)=-\pi_1\sum_{h=j+1}^d\pi_h.
\]
The Dirichlet energy gives
\[
 \langle f,(-L)^{-1}f\rangle_{\pi}
 =\sum_{j=1}^{d-1}\pi_ja_j(g_{j+1}-g_j)^2
 =\frac{D^2}{2(q-1)N^3}\sum_{j=1}^{d-1}\frac{S_j^2}{(d-j)w_j}.
\]
The variance-rate correction is eight times this energy. Divide by \(\mu=2D(N-1)/N\) to obtain precisely the displayed Fano formula. Every summand is positive, establishing strict super-Poissonian count noise for \(d\ge2\). In contrast, on a complete graph with two particles every configuration has constant rate \(2(q-2)\), so the jump-time process is homogeneous Poisson for \(q\ge3\).

**4. Fixed-alphabet asymptotics.** Write \(W=q^d-1=N\). The first term in the sum is
\[
 \frac{S_1^2}{(d-1)w_1}=\frac{(W-d(q-1))^2}{d(d-1)(q-1)}
 =\frac{W^2}{d^2(q-1)}\bigl(1+O_q(d^{-1})\bigr).
\]
To control all other terms rather than assume first-term dominance, use unimodality of \(w_j=\binom dj(q-1)^j\): its mode is at \(j\) near \(d(q-1)/q\). For sufficiently large \(d\), the contributions from \(j=2,3\) are at most \(O_q(W^2/d^3)\). For \(4\le j\) up to a mode, \(w_j\ge w_4\asymp_q d^4\) and \(d-j\ge c_qd\), so those terms sum to \(O_q(W^2/d^4)\). Above a mode, the weights are nonincreasing; hence
\[
 S_j\le(d-j)w_j,
\]
and their remaining contribution is at most \(\sum_j(d-j)w_j\le d q^d\), exponentially smaller than \(W^2/d^3\). Therefore the whole finite sum is
\[
 \frac{W^2}{d^2(q-1)}\bigl(1+O_q(d^{-1})\bigr).
\]
Substitution into the exact Fano formula proves
\[
 F_{d,q}-1=\frac{2}{d(q-1)q^d}\bigl(1+O_q(d^{-1})\bigr),
\]
which includes the exact limiting coefficient. Every estimate is for fixed integer \(q\ge2\), without claiming uniformity in growing \(q\).

## Verification

The supplied program `verify_hamming.py` constructs the original two-particle full configuration-space generator independently from vertex coordinates, including all transitions that preserve Hamming distance. It solves that full-generator Poisson equation numerically and compares both count cumulants with the exact rational formula. Nine cases pass: \((q,d)=(2,2),(2,3),(2,4),(2,5),(3,2),(3,3),(4,2),(4,3),(5,2)\). The program also prints nine large-d normalized-ratio checks for \(q=2,3,4\) and \(d=20,50,100\). Run using Python 3 with NumPy and SciPy; set `OPENBLAS_NUM_THREADS=1` if desired. Finite checks are not used as a proof of the all-dimensional formulas or the asymptotic law.

## Relationship to prior work

Exclusion dynamics and the activity observable were already established and studied in earlier literature. Lecomte, Garrahan and van Wijland (arXiv:1203.1600, first public March 7, 2012) treat low-activity biased ensembles of nearest-neighbor SSEP on one-dimensional rings. Arita, Krapivsky and Mallick (arXiv:1407.3228, first public July 11, 2014) develop hydrodynamic diffusion coefficients for generalized exclusion on infinite hypercubic lattices. de Queiroz (arXiv:1207.3044) addresses activity and current statistics of one-dimensional totally asymmetric exclusion, distinguishing instantaneous activity from integrated current. These established methods and phenomena are not claimed as new. The result here evaluates the long-time **total accepted-transition count** cumulant on finite \(q\)-ary Hamming graphs, including its exact binomial-tail Green function and the sharp fixed-alphabet dimension scaling. The ordinary two-particle square \(H(2,2)=K_{2,2}\) is covered by the known complete-bipartite special case and is included only as a consistency check, not as an independent contribution.

## Limitations

The result is restricted to two conserved indistinguishable particles, identical symmetric unit edge rates, uniform equilibrium initialization, all-successful-hop counting, and homogeneous Hamming graphs. It does not establish other particle densities, higher counting cumulants, a full Poisson-process limit, graph-uniform bounds, or the joint limit where alphabet size and dimension diverge. The exact Green identity relies on standard Markov perturbation theory; despite targeted comparisons, an equivalent evaluated Hamming-graph specialization in less accessible literature cannot be excluded without independent historical assessment.

## References

1. V. Lecomte, J. P. Garrahan and F. van Wijland, *Inactive dynamical phase of a symmetric exclusion process on a ring*, arXiv:1203.1600 (first posted 2012-03-07); https://arxiv.org/abs/1203.1600.
2. C. Arita, P. L. Krapivsky and K. Mallick, *Generalized Exclusion Processes: Transport Coefficients*, arXiv:1407.3228 (first posted 2014-07-11); https://arxiv.org/abs/1407.3228.
3. S. L. A. de Queiroz, *Current-activity versus local-current fluctuations in driven flow with exclusion*, arXiv:1207.3044 (first posted 2012-07-12); https://arxiv.org/abs/1207.3044.
