# A parity law for sparse two-frame observation of separated symbolic sensors

## Finding
For every integer \(d\geq1\), the binary two-sided full shift can be presented through paired, separated sensors as
\[
X_d=\bigl\{y\in(\{0,1\}^2)^{\mathbb Z}:\exists x\in\{0,1\}^{\mathbb Z},\ y_j=(x_j,x_{j+d})\text{ for all }j\in\mathbb Z\bigr\}.
\]
Write \(\sigma\) for the left shift on \(X_d\), and put
\[
\rho(y,z)=\max_{j\in\mathbb Z}w_j\mathbf 1_{\{y_j\ne z_j\}},\qquad
w_0=w_1=1,\qquad w_j=2^{-|j|-2}\ (j\notin\{0,1\}).
\]
At resolution \(\delta=1/2\), define a winning observation schedule \(A\subseteq\mathbb Z\) by the property that for every two distinct configurations \(y,z\in X_d\), some \(n\in A\) satisfies \(\rho(\sigma^ny,\sigma^nz)>\delta\). With lower Banach density
\[
\underline d_{\mathrm B}(A)=\lim_{N\to\infty}\inf_{t\in\mathbb Z}\frac{|A\cap[t,t+N-1]|}{N},
\]
let \(\beta_d\) be the infimum of this density over winning schedules. Then
\[
\boxed{\displaystyle\beta_d=\begin{cases}
\frac14,&d\ \text{even},\\[3pt]
\frac{d+1}{4d+2},&d\ \text{odd}.
\end{cases}}
\]
Both bounds are attained by explicit periodic schedules. Thus \(\beta_1=1/3\), \(\beta_2=1/4\), \(\beta_3=2/7\), and the positive parity penalty at every odd separation decays to zero with \(d\).

## Assumptions and scope
All indices are in \(\mathbb Z\). The observation records two consecutive time frames of two binary sensors separated by \(d\) symbolic sites. The subshift \(X_d\) is topologically conjugate to the binary full shift via \(x\mapsto((x_j,x_{j+d}))_j\), whose inverse reads the first sensor. The displayed compatible ultrametric is part of the theorem: its threshold tests exactly the two frames with indices \(0,1\), and \(\delta=1/2\) is an expansive constant. This is not a claim of metric-independent or conjugacy-invariant observation cost.

## Proof
**Step 1 (exact reduction).** Let \(F_d=\{0,1,d,d+1\}\). From the weights, \(\rho(\sigma^ny,\sigma^nz)>1/2\) if and only if \(y_n\ne z_n\) or \(y_{n+1}\ne z_{n+1}\), which under the conjugacy holds precisely when the two underlying binary sequences differ at some coordinate in \(n+F_d\). Consequently,
\[
A\text{ is winning}\quad\Longleftrightarrow\quad A+F_d=\mathbb Z.
\]
For necessity, if a coordinate \(k\notin A+F_d\), take two full-shift sequences differing only at \(k\); their coded trajectories are not distinguished. Sufficiency follows because any distinct sequences differ somewhere. This also establishes that the dynamical cost is the exact translate-covering density of \(F_d\), not merely a lower bound.

**Step 2 (universal lower bound).** Suppose \(A+F_d=\mathbb Z\). For any integer \(t\) and \(N>d+1\), each coordinate in \([t+d+1,t+N-1]\) must be covered by a translate with its starting point inside \([t,t+N-1]\). As each translate contains at most four coordinates, 
\[
|A\cap[t,t+N-1]|\geq\frac{N-d-1}{4}.
\]
Therefore \(\underline d_{\mathrm B}(A)\geq1/4\).

**Step 3 (odd-separation obstruction).** In a translated block \(I=[t,t+2d]\), look at its interior tail \(J=[t+d+1,t+2d]\), containing \(d\) integers. Every translate covering a member of \(J\) begins in \(I\), since the smallest and largest elements of \(F_d\) are \(0\) and \(d+1\). Any three distinct positions of \(F_d\) have span at least \(d\) (including the degenerate \(d=1\) case), whereas \(J\) has diameter \(d-1\). Thus one translate meets \(J\) in at most two points. Hence every \(2d+1\) consecutive positions contain at least \(\lceil d/2\rceil\) elements of \(A\). Partitioning arbitrary long intervals into such blocks yields
\[
\underline d_{\mathrm B}(A)\geq\frac{\lceil d/2\rceil}{2d+1}.
\]
For odd \(d\), this is \((d+1)/(4d+2)\), strictly larger than \(1/4\).

**Step 4 (optimal schedules).** For even \(d\), let \(P=2d\) and choose the observation residues \(0,2,\ldots,d-2\pmod P\). Each residue together with \(F_d\) covers two adjacent sites in \([0,d-1]\) and two sites displaced by \(d\); their union covers every residue modulo \(P\). The density is \((d/2)/(2d)=1/4\). For odd \(d\), let \(P=2d+1\) and choose residues \(0,2,\ldots,d-1\pmod P\). Their translates by \(\{0,1\}\) cover \([0,d]\), while their translates by \(\{d,d+1\}\) cover \([d,2d]\). This covers every residue modulo \(P\) and has density \(((d+1)/2)/(2d+1)\). The two constructions attain the preceding lower bounds. \(\square\)

## Verification
The standalone file `check_observation.py` constructs both periodic schedules and checks their exact residue coverage and the crucial two-incidence bound for every integer separation from \(1\) through \(500\), using integer arithmetic. Run `python3 check_observation.py`; expected final output is `PASS: 500 periodic covers and interval-incidence bounds checked.` These checks illustrate the formulas; Steps 1–4 prove the result for every integer \(d\geq1\) without relying on finite enumeration.

## Relationship to prior work
Ferrari's *Observer–hider games for expansive dynamical systems* (2026) introduces the lower Banach-density observation cost, its witness-set cover obstruction, exact results for the usual contiguous-window full shift, and finite graph methods for shifts of finite type. Here the observation window in underlying binary coordinates is the disconnected four-position pattern \(F_d=\{0,1,d,d+1\}\), and an explicit infinite parity-dependent formula replaces a general finite-pattern calculation. The formula is not asserted to be absent from the inaccessible portions of that source.

Bollobás, Janson and Riordan study covering by translates of finite subsets of groups in a substantially more general framework; the present problem evaluates a particular structured infinite family of translate-covering densities with a direct sharp local incidence certificate. Their general covering theory is not claimed to be new here.

## Limitations
The answer is specific to the stated paired symbolic representation, two-frame threshold metric, and unconstrained binary full shift. It gives no analogue for arbitrary subshifts, arbitrary camera windows, stochastic noise, or metric-independent sampling. General covering methods may yield alternative proofs; the complete body of Ferrari's paper was not available for definitive statement-level exclusion, so independent literature verification remains warranted.

## References
1. L. Ferrari, *Observer–hider games for expansive dynamical systems*, Journal of Dynamics and Games, 2026, DOI: 10.3934/jdg.2026045. Public online date: 2026-06-29. https://doi.org/10.3934/jdg.2026045
2. B. Bollobás, S. Janson, O. Riordan, *On covering by translates of a set*, Random Structures & Algorithms 38 (2011), 33–67, arXiv:0910.3815. https://arxiv.org/abs/0910.3815
3. C. Li, D. Offner, I. Ye, *Minimum packing density for sets of four integers*, arXiv:2501.01571 (2025). This addresses packing, not the present minimum translate-covering cost. https://arxiv.org/abs/2501.01571
