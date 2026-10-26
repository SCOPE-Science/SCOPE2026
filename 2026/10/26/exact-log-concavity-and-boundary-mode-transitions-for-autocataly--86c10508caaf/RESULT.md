# Exact log-concavity and boundary-mode transitions for autocatalytic count laws

## Finding
For a reversible two-species autocatalytic count process, a sharp stationary log-concavity classification reduces the infinitely many population sizes and, at each size, almost all index tests to a pair of boundary inequalities. The population-uniform threshold in the ratios of mutation to autocatalytic rates is exactly \(1/3\), independent of the relative autocatalytic speeds. In the symmetric system, the boundary-local-mode transition and log-concavity transition are distinct, with a quantifiable intervening regime that is unimodal but fails log-concavity.

## Assumptions and scope
Fix an integer \(n\ge2\), positive parameters \(\kappa_1,\kappa_2,\iota_1,\iota_2\), and a continuous-time birth–death chain \(K\in\{0,1,\ldots,n\}\) whose nonzero transition rates are
\[
q(k,k+1)=\frac{(n-k)^2}{n^2}(\kappa_1k+\iota_1),\qquad
q(k,k-1)=\frac{k^2}{n^2}(\kappa_2(n-k)+\iota_2).
\]
These formulas apply only when the indicated destination lies in the state space. Put \(a=\iota_1/\kappa_1>0\), \(b=\iota_2/\kappa_2>0\), and \(r=\kappa_1/\kappa_2>0\). The rising factorial is \((u)_0=1\) and \((u)_j=u(u+1)\cdots(u+j-1)\). A positive finite sequence \(w_0,\dots,w_n\) is *log-concave* when \(w_k^2\ge w_{k-1}w_{k+1}\) for every \(1\le k\le n-1\). A strict endpoint local peak has weight strictly exceeding its single neighboring weight. A central plateau of two equally high adjacent weights counts as a single peak region.

The unique stationary probability is
\[
\pi_n(k)=\frac{1}{Z_n}\,\kappa_1^k\kappa_2^{n-k}\binom nk^{\!2}(a)_k(b)_{n-k},\qquad 0\le k\le n,
\]
where \(Z_n\) is the sum of the displayed positive weights. Define for integers \(j\ge1\) and \(u>0\)
\[
F_j(u)=\frac{j^2(j+u)}{(j+1)^2(j-1+u)}.
\]

**Exact finite-size criterion.** If \(n=2\), stationarity is log-concave exactly when \(F_1(a)F_1(b)\le1\). If \(n\ge3\), it is log-concave exactly when BOTH
\[
F_1(a)F_{n-1}(b)\le1,\qquad F_{n-1}(a)F_1(b)\le1.
\]
Every interior concavity inequality indexed by \(2\le k\le n-2\) is strict whenever that range is nonempty. Thus the condition does not depend on \(r\). For any fixed \(a,b>0\), the laws are log-concave for **every** integer \(n\ge2\) if and only if \(a\ge1/3\) and \(b\ge1/3\).

**Symmetric shape thresholds.** Suppose also \(\kappa_1=\kappa_2\), \(a=b=u>0\), and \(n\ge4\). For \(0<u<1/(n+1)\), both boundary cells are strict local peaks in addition to the central peak region (a single middle cell if \(n\) is even, a two-cell middle plateau if \(n\) is odd). For \(u>1/(n+1)\), the central region is the only local-peak region; at equality the endpoints tie their immediate neighbors but are not strict peaks. At and above equality, the sequence is centrally unimodal (nondecreasing to its center and then nonincreasing). Its log-concavity has a later, sharp transition \(u_n\), uniquely determined by
\[
(1+u_n)(n-1)^2(n-1+u_n)=4u_n n^2(n-2+u_n),\qquad \frac1{n+1}<u_n<\frac13.
\]
The stationary sequence is log-concave if and only if \(u\ge u_n\), and the critical mutation ratio obeys
\[
u_n=\frac13-\frac4{9n}+O(n^{-2})\quad(n\to\infty).
\]
Consequently \(1/(n+1)\le u<u_n\) is a genuine unimodal, non-log-concave regime.

## Proof
**Stationary weights.** All nearest-neighbor rates are positive in the interior and on allowed boundary edges, so the finite chain is irreducible. The detailed-balance ratio is
\[
\frac{\pi_n(k+1)}{\pi_n(k)}
=r\frac{(n-k)^2}{(k+1)^2}\frac{k+a}{n-k-1+b}
=\frac{q(k,k+1)}{q(k+1,k)}\quad(0\le k<n).
\]
Taking successive products from the zero cell gives exactly the normalized stationary weights displayed above.

**Reduction to boundaries.** Write \(R_k=\pi_n(k+1)/\pi_n(k)\). For \(1\le k<n\), the successive-ratio quotient factorizes exactly as
\[
\frac{R_k}{R_{k-1}}=F_k(a)F_{n-k}(b).
\]
Log-concavity at index \(k\) is equivalent to this quotient being at most one. For every integer \(j\ge2\), expansion gives
\[
(j+1)^2(j-1+u)-j^2(j+u)=j^2-j-1+(2j+1)u>0,
\]
so \(0<F_j(u)<1\) for all \(u>0\). Also \(F_1(u)=(1+u)/(4u)\), which is at most one exactly when \(u\ge1/3\). At every index \(2\le k\le n-2\), both factors are strictly less than one; only \(k=1\) and \(k=n-1\) remain. This proves the finite-size tests, with the one-cell interpretation for \(n=2\). If \(a,b\ge1/3\), every factor is at most one, proving uniform log-concavity. If \(a<1/3\), then \(F_1(a)>1\) and \(F_{n-1}(b)\to1\) as \(n\to\infty\), so the \(k=1\) inequality eventually fails. Interchange \(a,b\) for the other necessity. Relative speed \(r\) cancels identically in the second ratios.

**Symmetric modes.** For \(r=1\) and \(a=b=u\), symmetry gives \(\pi_n(k)=\pi_n(n-k)\). The initial two successive ratios are
\[
R_0=\frac{n^2u}{n-1+u},\qquad
R_1=\frac{(n-1)^2(1+u)}{4(n-2+u)}.
\]
The first ratio is less than one, equal to one, or greater than one according as \(u\) is less than, equal to, or greater than \(1/(n+1)\). For every \(n\ge4\) and \(u>0\), \(R_1>1\); indeed multiplying the inequality by its positive denominator leaves \((n-3)^2+((n-1)^2-4)u>0\). By the strict interior concavity just proved, \(R_1>R_2>\cdots>R_{n-2}\). Symmetry entails \(R_{n-1-k}=R_k^{-1}\), so these monotone ratios cross level one only at the center, with a middle plateau for odd \(n\). If \(R_0<1\), the two endpoints are additional strict local peaks. If \(R_0\ge1\), the whole positive sequence is centrally unimodal.

**Sharp symmetric concavity boundary.** The two endpoint log-concavity tests now coincide and become \(F_1(u)F_{n-1}(u)\le1\). Both factors are strictly decreasing in \(u>0\); their product tends to infinity at zero and is strictly below one at \(u=1/3\), because \(F_1(1/3)=1\) and \(F_{n-1}(1/3)<1\). Therefore its equality has exactly one positive solution \(u_n\) below \(1/3\). At \(u=1/(n+1)\), the equal first masses give \(R_0=1<R_1\), so log-concavity fails and \(u_n>1/(n+1)\). Expanding the equality yields the displayed polynomial equation. Finally, uniformly for bounded \(u\), \(F_{n-1}(u)=1-1/n+O(n^{-2})\), while \(F_1(1/3)=1\) and \(F_1'(1/3)=-9/4\). The unique root tends to \(1/3\) and its Taylor expansion gives \(u_n=1/3-4/(9n)+O(n^{-2})\). These arguments prove every asserted range and boundary condition.

## Verification
The accompanying `verify.py` uses only Python's standard library. It reconstructs unnormalized weights as exact rational numbers and tests each nearest-neighbor detailed-balance ratio, all interior log-concavity inequalities, and their equivalence with the boundary-only criterion for \(2\le n\le24\), eight mutation ratios in each coordinate and three speed ratios. It also checks endpoint and center behavior for \(4\le n\le31\), including odd-length central plateaus, then numerically brackets critical roots and checks the first-order asymptotic at two large sizes. The recorded result is `PASS: 114964 exact finite checks and root/asymptotic spot checks`. These finite checks corroborate, but do not replace, the all-parameter analytical argument.

## Relationship to prior work
Xiang and KhudaBukhsh (2026, first version October 13) investigate the quadratic-rate autocatalytic count chain and prove cutoff behavior. Their derivation of the stationary mass function and the associated count ratios is the input here. The current result asks a different question: exact finite-size discrete shape, not mixing-time asymptotics. Existing work on mutation-perturbed Togashi–Kaneko processes and Moran-type models considers related stationary laws, sometimes weighted beta-binomial forms with a *single* binomial factor, whose transition-rate convention differs from the quadratic-rate count process considered here. Their shape statements therefore do not immediately imply the displayed \(1/3\) criterion. The possible coverage of these sharp inequalities by a general theorem on hypergeometric coefficient sequences has not been fully excluded.

## Limitations
The theorem concerns the stationary **count marginal**, not mixing cutoff profiles, transient count distributions or multitype extensions. The stationary law depends on all positive rates, but the symmetric mode classification assumes equality of both autocatalysis rates and both mutation/autocatalysis ratios. Strict local maxima are distinguished from global maxima; coexistence of three local-peak regions does not assert that all are globally maximizing. Boundary and middle ties are included explicitly. Independent validation has not been conducted; finite numerical tests are not exhaustive. A residual priority risk remains for broad shape theorems for finite hypergeometric coefficient products.

## References
1. Xiang and KhudaBukhsh (2026), *Cutoff profiles and boundary effects in the Togashi–Kaneko model of autocatalytic reactions with weak mutations*, arXiv:2610.17775, version 1 first public October 13, 2026. https://arxiv.org/abs/2610.17775
2. *Fragility in a Togashi–Kaneko Stochastic Model with Mutations* (2026), SIAM Journal on Life Sciences, full article https://epubs.siam.org/eprint/SD2DDMET5TJ6KJXCDECC/full ; compare the different Moran/weighted-beta-binomial stationary convention in Section 4.
3. Saito and Kaneko (2014), *Theoretical Analysis of Discreteness-Induced Transition in Autocatalytic Reaction Dynamics*, arXiv:1403.6222; compare the different linear-in-species count rates for its bimodality discussion.
