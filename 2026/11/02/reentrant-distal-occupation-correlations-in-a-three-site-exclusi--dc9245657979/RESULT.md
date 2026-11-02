# Reentrant distal occupation correlations in a three-site exclusion chain with local resetting

## Finding

Consider the open, continuous-time totally asymmetric simple exclusion process with independent local resetting to its entry site, described precisely below. At the boundary rates \(\alpha=1/2\) and \(\beta=1/6\), and with unit forward hopping rate, the stationary covariance between occupations of sites 1 and 3 is

\[
C_{13}(r)=\frac{3(54r^4+18r^3-231r^2-125r+125)}{(3r+5)^2(6r^2+44r+55)^2},\qquad r\geq0.
\]

There are exactly two positive zeros \(r_-\) and \(r_+\), uniquely specified as the positive roots of \(54r^4+18r^3-231r^2-125r+125=0\), and isolated by

\[
0.532<r_-<0.533,\qquad 2.043<r_+<2.044.
\]

Consequently \(C_{13}(r)>0\) for \(0\leq r<r_-\), \(C_{13}(r)<0\) for \(r_-<r<r_+\), and \(C_{13}(r)>0\) for \(r>r_+\), with equality exactly at the two thresholds. Furthermore, **both adjacent-site covariances are strictly negative for every \(r\geq1\)**. Thus for every \(r>r_+\), the two nonadjacent occupations are positively correlated even as each adjacent pair is negatively correlated. The late positive covariance satisfies \(C_{13}(r)\sim1/(2r^2)\) as \(r\to\infty\).

This sign reentrance is not confined to a single isolated choice of boundary rates: there is an open neighborhood of \((\alpha,\beta)=(1/2,1/6)\) in the positive quadrant for which the distal covariance exhibits at least two sign changes as the resetting rate increases, and both adjacent covariances are negative at a resetting rate where the distal covariance is positive. This open-neighborhood statement asserts **at least** two crossings, not exactly two for every nearby boundary-rate pair.

## Assumptions and scope

Sites are \(1,2,3\), with occupation variables \(n_i\in\{0,1\}\). Each particle at site \(i=1,2\) attempts to move to site \(i+1\) at rate 1 if that destination is vacant. If site 1 is vacant, an external particle is injected at rate \(\alpha>0\); a particle at site 3 exits at rate \(\beta>0\). Independently for **each occupied** site \(j\in\{2,3\}\), its particle jumps directly to site 1 at rate \(r\geq0\) when site 1 is vacant. In particular, from configuration \((n_1,n_2,n_3)=(0,1,1)\), the two different donor particles each offer a distinct rate-\(r\) transition. All clocks are independent. These are *local* particle-specific resets, not a simultaneous replacement of the entire configuration.

Because \(\alpha,\beta>0\), the finite-state chain is irreducible even at \(r=0\), so its stationary law is unique. We write \(C_{ij}=\mathbb E_\pi[n_i n_j]-\mathbb E_\pi[n_i]\mathbb E_\pi[n_j]\). The exact two-threshold classification holds for the stated rational boundary rates, with only the robust-existence extension claimed for nearby positive rates. No thermodynamic-limit conclusion is asserted.

## Proof

**1. Generator and exact stationary law.** Index states by binary labels \(n_3n_2n_1\) in the order \(000,001,010,011,100,101,110,111\). Define

\[
H(r)=(3r+5)(6r^2+44r+55)>0.
\]

The stationary probabilities are \(\pi_m=w_m/(2H(r))\), where the eight unnormalized weights are

| State \(n_3n_2n_1\) | Weight \(w_m\) |
|---|---|
| \(000\) | \(2(6r+5)\) |
| \(001\) | \(36r^3+108r^2+92r+15\) |
| \(010\) | \(2(3r+2)(6r+5)\) |
| \(011\) | \(72r^2+144r+55\) |
| \(100\) | \(6(6r+5)\) |
| \(101\) | \(12(3r+1)(3r+5)\) |
| \(110\) | \(18(3r+5)\) |
| \(111\) | \(54(3r+5)\) |

These weights are strictly positive for \(r\geq0\), and their sum is exactly \(2H(r)\). To check stationarity, form the eight-state generator \(Q\). Its nonzero off-diagonal rates are obtained from the four event rules in the preceding section: entry, exit, two rightward hops, and each eligible donor-to-site-1 reset. Direct substitution of the displayed \(w_m\) into every of the eight polynomial balance equations gives \(\sum_m w_m Q_{m,j}=0\) identically in \(r\). The complete construction and exact symbolic identities, independent of any numerical optimization, are reproduced by the standalone checker.

**2. Exact pair covariances.** Summing the eight probabilities over the appropriate occupied configurations and putting them over the common positive denominator gives

\[
\begin{aligned}
C_{13}(r)&=\frac{3F(r)}{H(r)^2},\\
C_{12}(r)&=-\frac{A(r)}{2H(r)^2},\\
C_{23}(r)&=-\frac{9B(r)}{2H(r)^2},
\end{aligned}
\]

where

\[
\begin{aligned}
F(r)&=54r^4+18r^3-231r^2-125r+125,\\
A(r)&=648r^5+5832r^4+17460r^3+21078r^2+7070r-2375,\\
B(r)&=216r^4+684r^3+354r^2-340r-125.
\end{aligned}
\]

These are algebraic identities, not fitted curves. For example, writing \(W_i=\sum_{m:n_i=1}w_m\) and \(W_{ij}=\sum_{m:n_i=n_j=1}w_m\), one has \(C_{ij}=[2H W_{ij}-W_iW_j]/(4H^2)\). Expanding for \(i,j=1,3\) yields \(2H W_{13}-W_1W_3=12F\), which gives the displayed formula.

**3. Two and only two positive zeros.** The coefficient signs of \(F\), from highest to lowest power, are \(+,+,-,-,+\). Descartes' rule of signs gives at most two positive roots, counted with multiplicities. Yet \(F(0)=125>0\), \(F(1)=-159<0\), and \(F(3)=2531>0\), so continuity supplies distinct positive roots in \((0,1)\) and \((1,3)\). These are therefore all positive roots; they are simple and force the complete sign classification. Exact rational evaluation improves their isolation to the intervals quoted in the finding. Since \(H(r)>0\), \(C_{13}\) has precisely the same signs as \(F\).

**4. Adjacent anticorrelation at sufficiently rapid resetting.** For \(r\geq1\), \(A(r)>0\) because the sum of its nonconstant positive terms contains \(7070r\geq7070>2375\). Also

\[
B(r)=216r^4+684r^3+r(354r-340)-125>0
\]

since \(r\geq1\) makes the first two terms at least \(216+684\), and the third at least 14. Thus \(C_{12},C_{23}<0\) for all \(r\geq1\). The leading terms of \(F\) and \(H^2\) give \(C_{13}(r)\sim1/(2r^2)\).

**5. Persistence under boundary-rate perturbations.** For every positive \(\alpha,\beta\), and \(r\geq0\), the irreducible eight-state chain has a unique invariant vector depending continuously on its rates. The three strict signs of \(C_{13}\) at \(r=0,1,3\), and strict signs of \(C_{12},C_{23}\) at \(r=3\), persist in some open neighborhood of \((1/2,1/6)\). The intermediate-value theorem therefore forces at least two distal sign changes there. These observations establish the open-set counterexample without making an unsupported global statement about all boundary rates.

## Verification

The included `verify.py` uses only Python's standard library and carries out polynomial arithmetic over the rationals. It independently constructs the event generator, verifies its row sums, all eight stationary balance identities, exact normalization and all three covariance numerator identities. It evaluates the quartic at rational isolation boundaries and proves the adjacent covariance sign conditions. Separately, it solves eight rational stationary linear systems by Gaussian elimination at reset rates \(0,1/5,1/2,1,2,3,10,100\), checking the answers against the displayed formula; these samples are checks, not a substitute for the universal polynomial proof. Run with `python3 verify.py` in the extracted package directory.

## Relationship to prior work

Pelizzola and Pretti, *Totally asymmetric simple exclusion process with local resetting and open boundary conditions* (published November 11, 2022; arXiv distribution February 21, 2024), introduce exactly this open-boundary local-resetting mechanism and investigate continuum mean-field densities, phases, finite-size simulation and **nearest-neighbor** covariances. Their equations define the model; this work does not claim that definition or those mean-field conclusions as new. Their mean-field closure explicitly discards correlations and cannot imply the finite-chain sign changes. The present claim concerns the exact **nonadjacent** occupation covariance for the minimal lattice on which it exists, with exact resetting-rate thresholds and coexistence of positive distal and negative neighboring correlations.

Pelizzola, Pretti and Zamparo (2020 preprint, 2021 publication) study local resetting with **periodic** rather than open boundaries, including the conserved-particle TASEP; the stationary processes and available covariance implications differ. Miron and Reuveni (2020 preprint, 2021 publication) study **symmetric** diffusion with local resetting, predominantly through mean-field and simulations. Classical exact open-boundary TASEP methods at zero resetting do not directly classify these signs over positive \(r\). General finite-state stationary linear algebra makes computation possible but does not itself supply the exhibited reentrant correlation theorem. No priority claim is made beyond the inspected literature.

## Limitations

The exact polynomial formula and *exactly two* positive zeros are established at \(\alpha=1/2\), \(\beta=1/6\), for **three sites only**. The open-neighborhood result provides at least two sign changes, not a complete two-parameter phase diagram. This result does not establish that the same reentrance persists in long chains or in the thermodynamic limit. Its novelty relative to every possible unindexed finite-state specialization is not independently certified. Numerical checks establish reproducibility, not a separate infinite-dimensional or asymptotic claim.

## References

1. A. Pelizzola and M. Pretti, *Totally asymmetric simple exclusion process with local resetting and open boundary conditions*, Journal of Physics A: Mathematical and Theoretical **55** (2022), 454001; published November 11, 2022. DOI: https://doi.org/10.1088/1751-8121/ac9d72 . Public full-text preprint: https://arxiv.org/abs/2402.13698 .
2. A. Pelizzola, M. Pretti and M. Zamparo, *Simple Exclusion Processes with Local Resetting*, EPL **133** (2021), 60003. Preprint: https://arxiv.org/abs/2012.10993 .
3. A. Miron and S. Reuveni, *Diffusion with Local Resetting and Exclusion*, Physical Review Research **3** (2021), L012023. Preprint: https://arxiv.org/abs/2011.08241 .
