# Reentrant finite-gain leader separation on paths: a sharp ten-vertex onset and an infinite reversal family

## Finding

For a unit-weight path with exactly two equally pinned, noise-corrupted leaders, the optimal distance between leaders need not increase with the feedback gain. The first path order permitting a decrease is ten, and its complete positive-gain optimum has four phases. Furthermore, the decrease occurs in infinitely many path orders.

**Exact ten-vertex phase diagram.** For the path \(P_{10}\), with vertices numbered \(1,\ldots,10\), let \(d(\kappa)\) denote the separation between the two leaders in a globally optimal placement at gain \(\kappa>0\). Put
\[
\alpha=\frac{\sqrt{59}-7}{5},\qquad
\beta_- = \frac{5-\sqrt{11}}7,\qquad
\beta_+=\frac{5+\sqrt{11}}7.
\]
Then \(0<\alpha<\beta_-<\beta_+\), and the optimal leader sets are exactly

| Gain | All globally optimal leader sets | Separation |
|---|---|---|
| \(0<\kappa<\alpha\) | \(\{3,8\}\) | \(5\) |
| \(\kappa=\alpha\) | \(\{3,8\},\{2,8\},\{3,9\}\) | \(5,6\) |
| \(\alpha<\kappa<\beta_-\) | \(\{2,8\},\{3,9\}\) | \(6\) |
| \(\kappa=\beta_-\) | \(\{2,8\},\{3,9\},\{2,9\}\) | \(6,7\) |
| \(\beta_-<\kappa<\beta_+\) | \(\{2,9\}\) | \(7\) |
| \(\kappa=\beta_+\) | \(\{2,8\},\{3,9\},\{2,9\}\) | \(6,7\) |
| \(\kappa>\beta_+\) | \(\{2,8\},\{3,9\}\) | \(6\) |

Every path of order \(3\le n\le9\) has a nondecreasing optimal leader separation as gain increases; the exact small-order classification is proved below.

**Infinite reversal family.** For every integer \(m\ge2\), on \(P_{5m}\) the unique optimal leader set at gain \(\kappa=1\) is \(\{m,4m+1\}\), with distance \(3m+1\). At the higher gain \(\kappa=2\), the only optimal leader sets are \(\{m,4m\}\) and \(\{m+1,4m+1\}\), with strictly smaller distance \(3m\). The optimal distance therefore shrinks as gain rises from one to two in arbitrarily large path networks.

## Assumptions and scope

Let \(n\ge3\). The Laplacian \(L_n\) of the unweighted path \(1-2-\cdots-n\) has diagonal entries equal to the vertex degrees and off-diagonal entries \(-1\) across consecutive vertices. Choose **exactly two distinct** leaders \(a<b\) and a common gain \(\kappa>0\). Define
\[
M_{a,b}(\kappa)=L_n+\kappa(e_ae_a^{\mathsf T}+e_be_b^{\mathsf T}),\qquad
J_{a,b}(\kappa)=\operatorname{tr}(M_{a,b}(\kappa)^{-1}).
\]
The matrix \(M_{a,b}(\kappa)\) is positive definite. With independent unit Brownian perturbations on every node and feedback dynamics \(dX=-M_{a,b}(\kappa)X\,dt+dW\), the total stationary variance equals \(J_{a,b}(\kappa)/2\). Thus minimizing \(J\) and minimizing stationary variance are equivalent. The leader-set optimum allows arbitrary placements but not heterogeneous leader gains. All inequalities refer to exact real arithmetic and positive gain.

## Proof

**1. Exact inverse-trace reduction.** Put \(d=b-a\), \(A=a-1\), \(B=n-b\), and \(s=1/\kappa\). Regard each unit path edge as an electrical resistor and each leader's grounding feedback as a shunt resistor \(s\) to ground. The diagonal of \(M_{a,b}(\kappa)^{-1}\) is the corresponding effective resistance to ground. The graph is a tree away from the two grounding shunts. At a leader the two available routes to ground are a direct resistor \(s\) and a series resistor \(d+s\), so the grounding resistance at either leader is
\[
\rho=\frac{s(d+s)}{d+2s}=\frac{d\kappa+1}{\kappa(d\kappa+2)}.
\]
A node \(x\) edges from the left leader, for \(0\le x\le d\), has effective resistance \((x+s)(d-x+s)/(d+2s)\). Every node in a tail has its distance to the nearer leader plus \(\rho\). Summing both tails and the middle region gives the **exact** identity
\[
J_{a,b}(\kappa)=\frac{A(A+1)+B(B+1)}2
+(A+B)\frac{d\kappa+1}{\kappa(d\kappa+2)}
+\frac{(d+1)\{d(d-1)\kappa^2+6d\kappa+6\}}{6\kappa(d\kappa+2)}. \tag{1}
\]
In particular, for a fixed separation \(d\), the dependence on \(A,B\) occurs only through \(A(A+1)+B(B+1)\), with \(A+B=n-1-d\) fixed. The minimum is attained precisely by balanced tails \(|A-B|\le1\), giving one or two reflected leader sets.

Set \(t=n-1-d\), \(A=\lfloor t/2\rfloor\), \(B=\lceil t/2\rceil\), and \(T_d=A(A+1)+B(B+1)\). The minimal trace for separation \(d\) is therefore
\[
F_{n,d}(\kappa)=\frac{6n+6(T_d+dn)\kappa+[3dT_d+d(d^2-1)]\kappa^2}{6\kappa(d\kappa+2)}. \tag{2}
\]
This is globally exact: \(\min_{a<b}J_{a,b}(\kappa)=\min_{1\le d\le n-1}F_{n,d}(\kappa)\).

**2. Finite-size all-gain classification and sharp onset.** Let \((c_0,c_1,c_2)\) be the coefficients of the numerator of (2), in increasing powers of \(\kappa\). For any two separations \(d,e\), direct subtraction yields
\[
F_{n,d}-F_{n,e}
=\frac{Q_0+Q_1\kappa+Q_2\kappa^2}{6(d\kappa+2)(e\kappa+2)}, \tag{3}
\]
with \(Q_0=e c_{0,d}+2c_{1,d}-d c_{0,e}-2c_{1,e}\), \(Q_1=e c_{1,d}+2c_{2,d}-d c_{1,e}-2c_{2,e}\), and \(Q_2=e c_{2,d}-d c_{2,e}\). For \(n=3,\ldots,10\), every separation outside the following sets is strictly dominated for **all** \(\kappa>0\) by at least one separation inside the corresponding set:

| Order \(n\) | Undominated candidate separations |
|---|---|
| 3 | 2 |
| 4 | 3 |
| 5 | 2, 3 |
| 6 | 3 |
| 7 | 4 |
| 8 | 5 |
| 9 | 4, 5, 6 |
| 10 | 5, 6, 7 |

This is an exact, finite polynomial sign certificate, not a sampled gain scan. Substitution in (3) produces thirty-one domination certificates. Each numerator has nonnegative coefficients and is positive on \((0,\infty)\), except for a few strictly positive quadratics with negative linear coefficient whose discriminant is negative. The standard-library executable `verify.py` generates all thirty-one coefficient triples from (2) and checks these exact sign conditions. No numerical root solving enters this exclusion.

For \(n=5\), the only change is an increase from separation two to three at \(\kappa=\sqrt5-2\). For \(n=9\), the only changes are increases from four to five at \(\kappa=(\sqrt{74}-8)/10\), and from five to six at \(\kappa=(3\sqrt6-7)/5\). Their order is strict; the remaining orders \(3,4,6,7,8\) have a constant unique optimal separation. Thus no order at most nine admits a decrease.

For ten vertices, (3) reduces to the three factorizations
\[
F_{10,5}-F_{10,6}=\frac{5\kappa^2+14\kappa-2}{2(3\kappa+1)(5\kappa+2)},\qquad
F_{10,6}-F_{10,7}=\frac{-7\kappa^2+10\kappa-2}{2(3\kappa+1)(7\kappa+2)},
\]
\[
F_{10,5}-F_{10,7}=\frac{4(6\kappa-1)}{(5\kappa+2)(7\kappa+2)}. \tag{4}
\]
Their roots satisfy \(0<\alpha<1/6<\beta_-<\beta_+\). The signs of (4), together with the strictly dominated other six separations, give exactly the seven gain regimes in the Finding. The strict balanced-tail condition identifies the listed leader sets, including ties. Therefore ten is the first path size with a decreasing optimal separation.

**3. Infinite family.** Write \(n=5m\), where \(m\ge2\), and replace the parity-dependent integer quantity \(T_d\) in (2) by its smooth relaxation \(t(t+2)/2\), with \(t=5m-1-d\). The resulting function \(f(d,\kappa)\) differs from the exact balanced integer value by \(1/4\) when \(t\) is odd and by zero when \(t\) is even. Its derivative is
\[
\frac{\partial f}{\partial d}
=\frac{P(d,\kappa,m)}{6(d\kappa+2)^2},\qquad
P=5\kappa^2d^3+(18\kappa-15m\kappa^2)d^2+(12-60m\kappa)d-2\kappa-30m. \tag{5}
\]
At \(\kappa=1\) or \(2\), the coefficients of \(P\) in descending degree have signs \((+,-,-,-)\), so Descartes' rule of signs and the signs at zero/infinity give exactly one positive root. Direct evaluation gives
\[
P(3m,1)=-2(9m^2-3m+1)<0,\quad
P(3m+1,1)=3(9m^2+28m+11)>0,
\]
\[
P(3m,2)=-2(18m^2-3m+2)<0,\quad
P(3m+1,2)=2(72m^2+111m+32)>0. \tag{6}
\]
Thus \(f\) strictly decreases up through \(d=3m\) and strictly increases from \(d=3m+1\) onward. Since \(t\) is even at the two odd-offset distances \(3m-1\) and \(3m+1\), their parity corrections vanish, while every other correction is nonnegative. Therefore the global integer minimum at each of these two gains lies among \(3m-1,3m,3m+1\).

Exact differences of (2), at gain one, are
\[
F_{5m,3m-1}(1)-F_{5m,3m+1}(1)
=\frac{2m(3m-1)}{3(m+1)(3m+1)}>0,
\]
\[
F_{5m,3m}(1)-F_{5m,3m+1}(1)
=\frac{m(3m-5)}{6(m+1)(3m+2)}>0. \tag{7}
\]
At gain two they are
\[
F_{5m,3m-1}(2)-F_{5m,3m}(2)=\frac{12m-1}{12(3m+1)}>0,
\]
\[
F_{5m,3m+1}(2)-F_{5m,3m}(2)
=\frac{5m}{4(3m+1)(3m+2)}>0. \tag{8}
\]
All inequalities are strict for integer \(m\ge2\). Balanced tails then give the unique \(\{m,4m+1\}\) placement at gain one and exactly the two reflected placements \(\{m,4m\}\), \(\{m+1,4m+1\}\) at gain two. This proves the infinite family without extrapolation from finite experiments.

## Verification

The included `verify.py` uses only Python's standard library. Executing `python3 verify.py` reproduces all thirty-one universal-gain quadratic domination certificates for path sizes three through ten; checks all six displayed phase-difference polynomials; compares exact rational matrix inverses with (1) in 656 direct cases; and checks the infinite-family candidate optima on 118 sampled size/gain combinations. Expected output begins with `VERIFY_OK`. The sign certificates and identities in the proof, not numerical sampling, support the all-gain and infinite-order statements. The inverse calculations are independent checks of the resistance derivation, and the coefficient tests are exact integer arithmetic.

## Relationship to prior work

Lin, Fardad and Jovanović (arXiv:1302.0450, 2013) formulate finite-gain noisy leader selection through trace-inverse network performance and present general optimization approaches; the objective and grounded-Laplacian formulation are not new here. Fitch and Leonard (arXiv:1407.1569, 2014), particularly Theorem 3 and Section V-D, provide the general two-noisy-leader joint-centrality criterion and numerical path examples for 51 and 101 nodes. Their Corollary 3 and Appendix B treat **two noise-free** path leaders; the finite-gain path discussion supplies examples, not the present all-gain ten-node phase diagram, smallest-size boundary, or infinite gain-reversal family. Patterson, McGlohon and Dyagilev (arXiv:1412.6595, 2014) solve noise-free path/ring leader placement computationally using segment decompositions, a different grounding regime. Patterson, Yi and Zhang (arXiv:1708.06873, 2017) formulate the resistance-grounding equivalence for noisy leaders but in their explicit special-graph results solve noise-free paths and noisy cycles, not the noisy finite-gain path optimum considered here; this later literature is only supporting comparative evidence, not the dated primary basis. The exact comparison and model distinction are essential: a general computable pair objective does not explicitly imply the present globally compared thresholds without the stated minimization and sign analysis.

## Limitations

The theorem assumes an unweighted path, exactly two pinned vertices, identical finite gains, and independent equal-intensity perturbations. It does not classify all possible gains on \(P_n\) for \(n>10\), optimize heterogeneous pinning strengths, or quantify arbitrary temporal mixing performance. The statements concern stationary covariance trace (not leader control energy). The all-size finding compares two specified positive gains, while the full all-gain classification is restricted to ten vertices. The provided self-contained arithmetic checks are not independent peer validation. A historically equivalent specialization of a broader published formula cannot be ruled out solely by the consulted sources.

## References

1. F. Lin, M. Fardad, and M. R. Jovanović, *Algorithms for leader selection in stochastically forced consensus networks*, arXiv:1302.0450, first submitted February 3, 2013. https://arxiv.org/abs/1302.0450
2. K. E. Fitch and N. E. Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, arXiv:1407.1569, first submitted July 7, 2014. https://arxiv.org/abs/1407.1569
3. S. Patterson, N. McGlohon, and K. Dyagilev, *Efficient, Optimal \(k\)-Leader Selection for Coherent, One-Dimensional Formations*, arXiv:1412.6595, first submitted December 20, 2014. https://arxiv.org/abs/1412.6595
4. S. Patterson, Y. Yi, and Z. Zhang, *A Resistance Distance-Based Approach for Optimal Leader Selection in Noisy Consensus Networks*, arXiv:1708.06873, first submitted August 23, 2017. https://arxiv.org/abs/1708.06873
