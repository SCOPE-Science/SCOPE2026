# Unimodal birth thresholds for Wigner-negative vacuum–Fock rings, with a first even-order reversal at 24

## Finding
Let \(h_n\) be the normalized \(n\)-th Hermite oscillator state and let
\[
\rho_{n,t}=(1-t)|h_0\rangle\langle h_0|+t|h_n\rangle\langle h_n|,\qquad n\ge1,\quad 0\le t\le1.
\]
Write \(L_n\) for the ordinary Laguerre polynomial and \(Q_n(s)=(-1)^nL_n(s)\). For every \(n\), the Wigner-negative set of \(\rho_{n,t}\) is a disjoint union of concentric open annuli and, for odd \(n\), possibly one central open disk. **Its entire amplitude phase diagram is exact:** place a marker at each negative local minimum of \(Q_n\) on \((0,\infty)\); for odd \(n\), also mark the endpoint \(s=0\). If the markers are \(s_1<\cdots<s_k\), let
\[
m_j=-Q_n(s_j)>0,\qquad t_j=(1+m_j)^{-1}.
\]
Then \(k=\lceil n/2\rceil\), and the number of connected negative components at \(0\le t\le1\) is precisely
\[
\boxed{\quad C_n(t)=\sum_{j=1}^{\lceil n/2\rceil}\mathbf1_{\{t>t_j\}}.\quad}
\]
All interior events are nondegenerate births of annuli at double radial zeros. The odd-order endpoint event at \(t=1/2\) births a central disk. No other changes of negative-region topology occur. Simultaneous births are permitted by the formula.

**Ordering law.** As the markers are read outward, their depths \(m_j\) first decrease and then increase, with at most one adjacent tie at the turning point; equivalently the birth thresholds \(t_j\) first increase and then decrease. A monotone segment may be empty. Thus the entire radial sequence has at most one directional reversal, at every Hermite order.

**First two-ring reversal.** For every even \(n\in\{4,6,\dots,22\}\), the second negative minimum of \(Q_n\) is strictly deeper than the first; at \(n=24\) the order reverses. Writing \(m_1,m_2\) for these minima, rigorously enclosed values are
\[
\begin{array}{c|cc}
 n&m_1&m_2\\ \hline
22&0.4375450443\ldots&0.448760675\ldots\\
24&0.4345526045\ldots&0.427347868\ldots
\end{array}
\]
Consequently, for even orders through 22, the second ring is born before the first as mixture weight increases, while at order 24 the first ring is born before the second. The assertion about a *first* reversal concerns precisely this pair of innermost rings among even orders, not arbitrary other ring pairs or higher orders.

## Assumptions and scope
The Wigner convention used here is
\[
W_f(q,p)=\frac1{2\pi}\int_{\mathbb R}f(q+y/2)\overline{f(q-y/2)}e^{-ipy}\,dy.
\]
The normalized Hermite functions are \(h_n(x)=\pi^{-1/4}(2^n n!)^{-1/2}H_n(x)e^{-x^2/2}\). All statements concern the one-mode diagonal *incoherent* vacuum–Fock mixture above, with real phase-space coordinates \((q,p)\). Laguerre normalization is
\[
L_n(s)=\sum_{j=0}^n(-1)^j\binom nj\frac{s^j}{j!}.
\]
A radial zero has multiplicity as a zero in \(s=2(q^2+p^2)\). At positive radial minima this also gives a nondegenerate local fold of the nodal circles. The central zero at \((q,p)=(0,0)\) for odd \(n\), \(t=1/2\), is quadratic in \((q,p)\), not a pair of circles.

## Proof
**1. Exact Wigner polynomial.** Mehler's generating identity for normalized Hermite functions gives, by substituting \(q\pm y/2\) and performing the Gaussian integral,
\[
\sum_{n\ge0}u^nW_{h_n}(q,p)=\frac{1}{\pi(1+u)}\exp\!\left[-\frac{1-u}{1+u}(q^2+p^2)\right],\quad |u|<1.
\]
Comparison with the Laguerre generating function yields
\[
W_{h_n}(q,p)=\frac{(-1)^n}{\pi}e^{-(q^2+p^2)}L_n(2(q^2+p^2)).
\]
By linearity in the density operator, writing \(s=2(q^2+p^2)\),
\[
W_{\rho_{n,t}}(q,p)=\frac{e^{-s/2}}{\pi}\{1-t+tQ_n(s)\}.
\]
The Gaussian multiplier never vanishes, so the negative set is determined exactly by \(Q_n(s)<-(1-t)/t\) for \(t>0\).

**2. Negative lobes and all birth thresholds.** The classical Laguerre root theorem supplies exactly \(n\) distinct positive zeros, and the derivative identity \(L_n'(s)=-L_{n-1}^{(1)}(s)\) supplies exactly one critical point between each adjacent pair, all simple. As \(s\to\infty\), \(Q_n(s)\sim s^n/n!>0\), while \(Q_n(0)=(-1)^n\). Hence \(Q_n\) has exactly \(\lceil n/2\rceil\) negative lobes on the half-line, counting the lobe adjacent to zero for odd \(n\). Every negative interior lobe has one strict minimum \(s_j\), and on that lobe the sublevel set \(\{Q_n<-c\}\), for \(c\ge0\), is one open interval if \(c<m_j\) and empty if \(c\ge m_j\). Different lobes are separated by intervals where \(Q_n>0\). Passing from \(s\) to phase space makes each such interval an open annulus, except the odd-order lobe at the origin, which becomes an open disk when \(t>1/2\). This proves the exact count for every \(n\) and \(t\), including equality cases.

At a negative interior minimum \(s_j>0\), the Laguerre equation
\[
sQ_n''+(1-s)Q_n'+nQ_n=0
\]
gives \(Q_n''(s_j)=nm_j/s_j>0\). Therefore a threshold \(t_j=(1+m_j)^{-1}\) has exactly one double radial zero at \(s_j\). Writing \(t=t_j+\delta\) with small \(\delta>0\), the two nearby boundary radii in the \(s\)-variable obey
\[
s_{\pm}=s_j\pm(1+m_j)\sqrt{\frac{2s_j}{nm_j}}\,\sqrt\delta+O(\delta).
\]
This explicitly proves the nondegenerate annular fold. For odd \(n\), \(Q_n(s)=-1+ns+O(s^2)\) at \(s=0\), giving a central disk only when \(t>1/2\). No additional critical events are possible, because every lobe has exactly one minimum.

**3. Global ordering law.** Put \(y(s)=L_n(s)\). The positive auxiliary energy
\[
E_n(s)=y(s)^2+\frac{s}{n}y'(s)^2
\]
has the exact derivative, obtained by inserting the Laguerre differential equation,
\[
\boxed{\quad E_n'(s)=\frac{2s-1}{n}\,y'(s)^2.\quad}
\]
Consequently \(E_n\) strictly decreases along every nontrivial interval below \(1/2\) and strictly increases along every nontrivial interval above \(1/2\). At each interior minimum marker, \(y'=0\), so \(E_n(s_j)=m_j^2\); at the odd-order center marker \(E_n(0)=1=m_1^2\). Reading increasing markers therefore gives an initially decreasing and subsequently increasing sequence \(m_j\). Only a consecutive pair whose intervening interval straddles \(1/2\) can tie or reverse the local trend, and such a pair occurs at most once. The strictly decreasing map \(m\mapsto1/(1+m)\) gives the asserted single-peak law for the thresholds.

**4. Exact even-degree crossover.** For each even \(n=4,6,\dots,24\), denote the first and third positive roots of \(L_n'\) by \(x_{n,1}<x_{n,3}\). These are precisely the first two negative minima of \(L_n\). The bundled standalone checker computes isolating rational intervals for *all* \(n-1\) positive derivative roots using exact polynomial root isolation, and then encloses \(-L_n(x_{n,1})\) and \(-L_n(x_{n,3})\) by rational interval Horner evaluation. Every comparison is strict: \(m_2>m_1\) for all the ten even degrees from 4 through 22, and \(m_1>m_2\) at 24. In particular, for 22 the respective depth enclosures lie within \((0.4375450443,0.4375450445)\) and \((0.4487606728,0.4487606785)\), while for 24 they lie within \((0.4345526044,0.4345526046)\) and \((0.4273478673,0.4273478704)\). Strict rational inequalities prove the claimed first even-degree reversal. No numerical root approximation is used for this finite cutoff proof.

## Verification
Run `python artifacts/check.py` from the package root. The script reproduces the exact rational root isolations and minimum-depth comparisons for all even degrees 4 through 24, independently checks the ordering sequence numerically for all degrees 1 through 64, and evaluates the defining Wigner integral against its Laguerre formula at two phase-space points in each of orders 0 through 3. The file `artifacts/check_output.txt` records successful execution. Exact rational comparisons establish the finite cutoff; the all-degree ordering law and complete topological classification are proved analytically, not inferred from a finite run.

## Relationship to prior work
Kenfack and Życzkowski (2004) introduced an integrated Wigner-negativity indicator and analyzed Fock states and coherent Gaussian cats, but not the entire negative-domain birth ordering of diagonal vacuum–higher-Fock mixtures. Miranowicz and colleagues (2015) studied mixed vacuum–single-photon states and several nonclassicality measures; their two-level order-one results cannot cover a degree-24 reversal. Van Herstraeten, Cerf, and Chabaud (2026) study Wigner positivity and entropy for finite Fock support, including a vacuum–higher-Fock coherence family; a published mathematical note develops the small-mixture maximal-coherence boundary, rather than the present whole-parameter negative-lobe topology. The energy monotonicity is an elementary classical Laguerre-ODE/Sonin-type mechanism, not claimed as a new special-function identity. The contribution is its all-order application to ring-birth thresholds together with the exact first even-order reversal.

## Limitations
The classification is restricted to diagonal mixtures with exactly vacuum and one pure number state; coherent off-diagonal perturbations and mixtures of three or more Fock levels are not included. The all-order ordering theorem allows coincident nonadjacent birth thresholds and does not classify all such simultaneous coincidences. The first-reversal cutoff refers solely to the first two negative rings among even degrees through 24. A nearby 2026 primary paper was accessible only through its abstract and a separately published mathematical note, leaving a bounded publication-priority risk; no independent external audit is claimed.

## References
1. A. Kenfack and K. Życzkowski, *Negativity of the Wigner function as an indicator of nonclassicality*, arXiv:quant-ph/0406015v1, first public 2004-06-02, https://arxiv.org/abs/quant-ph/0406015.
2. A. Miranowicz et al., *Statistical mixtures of states can be more quantum than their superpositions*, arXiv:1502.04523v1, first public 2015-02-16, https://arxiv.org/abs/1502.04523.
3. Z. Van Herstraeten, N. J. Cerf, and U. Chabaud, *Wigner-positive quantum states can have lower entropy than the vacuum*, arXiv:2609.24670v1, first public 2026-09-21, https://arxiv.org/abs/2609.24670.
4. *Sharp near-vacuum boundary layer for maximal Wigner-positive Fock coherence*, published mathematical note, https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-sharp-near-vacuum-boundary-layer-for-maximal-wigner-positive-foc--bd630ca1caac/RESULT.md.
