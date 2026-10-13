# Sharp crossing of projective-plane coupon-coverage tails

## Finding

Fix an integer \(q\in\{2,3\}\), and set \(n=q^2+q+1\) and \(r=q+1\). In the *projective-plane mechanism*, each draw independently selects one of the \(n\) lines of the Desarguesian plane \(\mathrm{PG}(2,q)\), uniformly, and reveals its \(r\) points. In the *full mechanism*, each draw independently selects one of the \(\binom nr\) subsets of \(r\) points, uniformly. Let \(T_{\mathrm P,q}\) and \(T_{\mathrm F,q}\) be their respective first full-coverage times, counting draws starting from an empty collection. For every integer \(t\ge0\), put
\[
\Delta_q(t)=\Pr(T_{\mathrm P,q}>t)-\Pr(T_{\mathrm F,q}>t).
\]

The two smallest projective planes have *different exact time-dependent comparisons*:
\[
\begin{array}{c|ccc}
q & \Delta_q(t)=0 & \Delta_q(t)<0 & \Delta_q(t)>0\\ \hline
2 & 0\le t\le2 & \text{never} & t\ge3\\
3 & 0\le t\le3 & t=4 & t\ge5.
\end{array}
\]
Thus the Fano mechanism is slower in the usual stochastic order, whereas the order-three projective-plane mechanism is *not* stochastically comparable with the full mechanism: it has *more* four-draw completions but *fewer* completions at every horizon of at least five draws. This distinction persists although both projective-plane mechanisms have larger mean coverage times than their full-model counterparts, as already established by Barak-Pelleg and Berend.

## Assumptions and scope

All draws are independent with replacement. Points are the one-dimensional subspaces of \(\mathbf F_q^3\); lines are the two-dimensional subspaces; a draw reveals every point on its line. The full mechanism samples uniformly from *all* \(r\)-point subsets on the same labeled point set. The comparison is for **every integer horizon** \(t\ge0\), with strictness exactly as indicated. No claim is made for projective planes of other orders, dependent draws, unequal line weights, or other fair hypergraph mechanisms.

## Proof

**1. A complete survival-time identity.** More generally let \(V\) be a finite coupon set, \(\mathcal B\) a nonempty family of nonempty blocks, and let each draw select one block independently and uniformly. For every nonempty \(S\subseteq V\) define the avoidance number
\[
 e_{\mathcal B}(S)=|\{B\in\mathcal B:B\cap S=\varnothing\}|.
\]
Inclusion-exclusion applied to the events that an individual point has not yet been seen gives, for every integer \(t\ge1\),
\[
\Pr(T_{\mathcal B}>t)
=\sum_{\varnothing\ne S\subseteq V}(-1)^{|S|+1}
 \left(\frac{e_{\mathcal B}(S)}{|\mathcal B|}\right)^t.
\tag{1}
\]
Set \(c_j=\sum_{S\ne\varnothing,\ e_{\mathcal B}(S)=j}(-1)^{|S|+1}\). For a projective plane, the avoidance numbers and coefficients are finite integers and the sum in (1) is \(\sum_j c_j(j/n)^t\). For the full mechanism of \(r\)-subsets, \(e(S)=\binom{n-|S|}{r}\) if \(n-|S|\ge r\), and zero otherwise, so that
\[
\Pr(T_{\mathrm F,q}>t)=\sum_{s=1}^n(-1)^{s+1}\binom ns
\left(\frac{\binom{n-s}{r}}{\binom nr}\right)^t,
\tag{2}
\]
with the numerator interpreted as zero when \(n-s<r\).

**2. Exhaustive projective-line coefficient calculation.** Canonical representatives for points are obtained by taking each nonzero vector in \(\mathbf F_q^3\) modulo nonzero scalar multiples; distinct point pairs generate all lines. The following signed avoidance coefficient table is the *complete* result of grouping all \(2^n-1\) nonempty point subsets \(S\) by \(e(S)\):

| Plane | \(j\mapsto c_j\), including \(j=0\) |
|---|---|
| \(\mathrm{PG}(2,2)\) | \(0\mapsto-6,\ 1\mapsto21,\ 2\mapsto-21,\ 4\mapsto7\) |
| \(\mathrm{PG}(2,3)\) | \(0\mapsto-38,\ 1\mapsto130,\ 2\mapsto-78,\ 3\mapsto-182,\ 4\mapsto234,\ 6\mapsto-78,\ 9\mapsto13\) |

This is a **finite exhaustive identity**, not a probabilistic experiment: the accompanying `verify_coverage.py` constructs all lines from field coordinates, visits each of the \(127\) or \(8191\) nonempty point subsets exactly once, and checks every table coefficient using integer arithmetic. Formula (2) similarly determines the full-model coefficients without any sampling. The code contains all formulas and constants used below and requires only the Python standard library.

**3. The Fano case.** Substitution of the \(q=2\) coefficients into (1)--(2), cancelling the two common bases, gives for every integer \(t\ge1\)
\[
\Delta_2(t)=\frac{21-35(4/5)^t+35(1/5)^t}{7^t}.
\tag{3}
\]
For \(t=1,2\) the numerator is zero. If \(f(t)=(4/5)^t-(1/5)^t\), then \(f(2)=3/5\) and
\[
 f(t+1)-f(t)=\frac{4-4^t}{5^{t+1}}<0\quad(t\ge2).
\]
Consequently \(\Delta_2(t)>0\) for every integer \(t\ge3\). Both coverage times exceed zero with probability one, so \(\Delta_2(0)=0\).

**4. The order-three case and its exact crossing.** The projective-plane coefficients and (2), with \(\binom{13}{4}=715\), give the *exact finite exponential sum*
\[
\begin{aligned}
715^t\Delta_3(t)={}&234\,220^t-286\,210^t-182\,165^t\\
&+715\,126^t-78\,110^t-1287\,70^t\\
&+130\,55^t+1716\,35^t-1716\,15^t\\
&+1287\,5^t-715,
\end{aligned}
\tag{4}
\]
valid for every integer \(t\ge1\). By the number of points, at least four draws are needed to cover all thirteen points, so \(\Delta_3(0)=\Delta_3(1)=\Delta_3(2)=\Delta_3(3)=0\). Exact rational substitution in (4) gives
\[
\begin{aligned}
\Delta_3(4)&=-\frac{15480}{2924207}<0,\\
\Delta_3(5)&=\frac{2178216}{418161601}>0,\\
\Delta_3(6)&=\frac{10152590256}{1494927723575}>0.
\end{aligned}
\tag{5}
\]
To prove the sign for **all remaining integers**, partition the right side of (4) into three terms:
\[
\begin{aligned}
G_1(t)&=234\,220^t-286\,210^t-182\,165^t,\\
G_2(t)&=715\,126^t-78\,110^t-1287\,70^t,\\
G_3(t)&=130\,55^t+1716(35^t-15^t)+1287\,5^t-715.
\end{aligned}
\]
For integer \(t\ge7\), division by \(220^t\) and comparison of decreasing powers show
\[
\frac{G_1(t)}{220^t}
\ge234-286(21/22)^7-182(3/4)^7
=\frac{46372796847}{14512627712}>0.
\]
For every integer \(t\ge5\), similarly,
\[
\frac{G_2(t)}{126^t}
\ge715-78(55/63)^5-1287(5/9)^5
=\frac{200913431290}{330812181}>0.
\]
Finally \(G_3(t)>0\) for every integer \(t\ge1\): the first summand is positive, \(35^t-15^t>0\), and \(1287\,5^t-715>0\). Therefore \(\Delta_3(t)>0\) for all \(t\ge7\); together with (5) and the initial zero region, this proves the full classification. \(\square\)

## Verification

Run `python3 verify_coverage.py` from the directory containing this result and the included checker. The program builds \(\mathrm{PG}(2,2)\) and \(\mathrm{PG}(2,3)\) from coordinate subspaces, independently verifies line-incidence axioms, exhaustively evaluates every nonempty missing-point subset, checks both avoidance tables and the complete-model binomial formula, and reproduces (3)--(5) using exact fractions. It verifies the two positive rational thresholds governing all later integer horizons. This is an exhaustive finite certificate for the finite input tables combined with an analytical proof for the infinite range of horizons; testing finitely many horizons alone would not prove the theorem.

## Relationship to prior work

Barak-Pelleg and Berend, *Fano Geometry and Slow Coupon Collecting* (arXiv:2606.28216v1), establish that projective-plane mechanisms for \(q=2,3,4\) have **larger expected coverage times** than the corresponding full models, and report exact rational mean values for \(q=2,3\). Their Sections 2--3 and table do **not state** the present pointwise survival-time comparison, and their proof for \(q=3\) computes mean coverage time via recovery-set enumeration. Grunbaum and Yaakobi (arXiv:2510.25305) provide the general fair-coverage setting, recovery-set formula and an expectation-level conjecture. Berend and Sher (arXiv:2509.17201) consider a different extremality question for general package distributions. All underlying projective incidence facts, coupon models, and standard inclusion-exclusion formulas are credited to their classical sources; the contribution here is the precise **single-horizon sign reversal at \(q=3\)**, its all-horizon proof, and its contrast with the complete \(q=2\) usual-stochastic-order comparison.

## Limitations

This is a complete comparison for two specific natural finite projective planes; it is **not** a classification for larger projective planes or all fair block systems. The finite avoidance coefficients can be produced by standard incidence enumeration. The novelty claimed is the *uniform-in-time sign theorem and its sharp crossing*, not the underlying enumerative techniques, known expectation inequality, or general inclusion-exclusion identity. Equivalent unstated formulations or prior distribution-level calculations may exist; independent literature review and scientific audit remain outstanding.

## References

1. D. Barak-Pelleg and D. Berend, *Fano Geometry and Slow Coupon Collecting*, arXiv:2606.28216v1 (first submitted 26 June 2026), especially Theorem 2.1 and Section 3.
2. Y. Grunbaum and E. Yaakobi, *General Coverage Models: Structure, Monotonicity, and Shotgun Sequencing*, arXiv:2510.25305 (2025).
3. D. Berend and T. Sher, *On a Conjecture on Uniform Group Drawings in the Coupon Collector Problem*, arXiv:2509.17201 (2025 preprint; later published).
4. G. Pólya, *Sur quelques points de la théorie des probabilités*, Ann. Inst. Henri Poincaré 1 (1930), 117--161 (historical inclusion-exclusion coverage methods).
