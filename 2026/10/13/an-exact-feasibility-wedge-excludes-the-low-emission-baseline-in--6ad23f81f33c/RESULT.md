# An exact feasibility wedge excludes the low-emission baseline in a green supply-chain game
## Finding
The supply-chain game of Ahsan and He imposes, in Assumption 4, a two-sided restriction on the carbon-abatement cost coefficient:
\[
L<k<U,
\]
with
\[
L=
\frac{(m+(1-\alpha)\delta)(\delta\theta+\varphi)}
{2\theta\varphi},
\qquad
U=
\frac{(m+(1-\alpha)\delta)^2}
{4m\theta-2(1-\alpha)\varphi}.
\]

The interval is not automatically meaningful. For positive \(m,\theta,\delta,\varphi\) and \(0<\alpha<1\), it is nonempty exactly when
\[
\frac{(1-\alpha)\varphi}{2}<m\theta<(1-\alpha)\varphi.
\]
Thus Assumption 4 contains an unspoken lower feasibility boundary.

At the numerical baseline stated in the paper,
\[
m=0.4,\qquad \alpha=0.2,
\]
this exact condition reduces to
\[
\varphi<\theta<2\varphi.
\]
Consequently, the entire low-emission baseline
\[
\theta=0.7
\]
is outside the stated feasible domain for both listed values
\[
\varphi=0.75,\qquad \varphi=0.90.
\]
No positive value of \(k\) can repair this.

The mismatch is not confined to the low-emission branch. At
\[
(\theta,\varphi)=(1.45,0.75),
\]
the admissible interval is only
\[
0.984413793\ldots<k<1.041428571\ldots,
\]
so neither of the paper's baseline values \(k=1.1\) and \(k=1.3\) satisfies the stated restriction. At
\[
(\theta,\varphi)=(1.45,0.90),
\]
the second Assumption-4 restriction becomes
\[
0.882413793\ldots<k<1.325454545\ldots,
\]
which does admit both baseline \(k\)-values.

Therefore the baseline simulation grid is not contained in the feasibility region under which the paper presents its closed-form Stackelberg payoffs and evolutionary stability conditions. In particular, every numerical experiment using \(\theta=0.7\) is outside the stated Assumption-4 domain.

## Assumptions and scope
The source assumes
\[
m>0,\quad \theta>0,\quad \delta>0,\quad \varphi>0,\quad 0<\alpha<1,
\]
and takes \(k>0\).

Only the second restriction in Assumption 4 is analyzed:
\[
\frac{(m+\delta-\alpha\delta)(\delta\theta+\varphi)}
{2\theta\varphi}
<
k
<
\frac{(m+\delta-\alpha\delta)^2}
{4m\theta+2(-1+\alpha)\varphi}.
\]
Since
\[
m+\delta-\alpha\delta=m+(1-\alpha)\delta>0,
\]
the sign analysis is unambiguous.

The finding is a domain-of-validity statement. It does not assert that every trajectory plotted outside Assumption 4 is numerically false. Instead, those runs require an independent justification because the source presents its equilibrium payoffs and evolutionary analysis after imposing Assumption 4 to ensure economic and mathematical feasibility, including the bound on the optimal abatement level.

The paper's third Assumption-4 condition involving \(s\) and \(t\) can only shrink the admissible set further; it is not needed for the exclusion proved here.

## Proof
Set
\[
A=m+(1-\alpha)\delta>0
\]
and
\[
D=4m\theta-2(1-\alpha)\varphi.
\]
Then
\[
L=\frac{A(\delta\theta+\varphi)}{2\theta\varphi},
\qquad
U=\frac{A^2}{D}.
\]

Because \(L>0\) and \(k>0\), a nonempty interval \(L<k<U\) requires \(U>0\). Since \(A^2>0\),
\[
U>0
\quad\Longleftrightarrow\quad
D>0
\quad\Longleftrightarrow\quad
m\theta>\frac{(1-\alpha)\varphi}{2}.
\]

Assume this necessary inequality. Direct subtraction and factorization give
\[
U-L=
-\frac{(2\delta\theta+\varphi)A
(m\theta+\alpha\varphi-\varphi)}
{2\theta\varphi\,[\,2m\theta-(1-\alpha)\varphi\,]}.
\]
Under the present assumptions every factor in the denominator is positive, and so are
\[
2\delta\theta+\varphi
\quad\text{and}\quad
A.
\]
Therefore
\[
U-L>0
\quad\Longleftrightarrow\quad
m\theta+\alpha\varphi-\varphi<0,
\]
or equivalently
\[
m\theta<(1-\alpha)\varphi.
\]
Combining the two inequalities proves the exact feasibility wedge
\[
\frac{(1-\alpha)\varphi}{2}<m\theta<(1-\alpha)\varphi.
\]

For the paper's values
\[
m=\frac25,\qquad \alpha=\frac15,
\]
the wedge becomes
\[
\varphi<\theta<2\varphi.
\]
Thus \(\theta=7/10\) fails whenever \(\varphi\) equals \(3/4\) or \(9/10\).

Using the paper's baseline
\[
\delta=\frac{17}{20},
\]
the exact bounds are:
\[
(\theta,\varphi)=\left(\frac7{10},\frac34\right):
\quad
L=\frac{2421}{1750},
\quad
U=-\frac{729}{50},
\]
\[
(\theta,\varphi)=\left(\frac7{10},\frac9{10}\right):
\quad
L=\frac{897}{700},
\quad
U=-\frac{729}{200},
\]
\[
(\theta,\varphi)=\left(\frac{29}{20},\frac34\right):
\quad
L=\frac{7137}{7250},
\quad
U=\frac{729}{700},
\]
and
\[
(\theta,\varphi)=\left(\frac{29}{20},\frac9{10}\right):
\quad
L=\frac{2559}{2900},
\quad
U=\frac{729}{550}.
\]
These exact fractions yield the decimal intervals stated above.

## Verification
The bundled script `verification/verify.py` uses exact rational arithmetic to factor the interval condition, evaluate all four announced \((\theta,\varphi)\) baseline pairs, and test the two baseline choices
\[
k=1.1,\qquad k=1.3.
\]
It verifies that no positive \(k\) exists in either low-emission branch, that neither baseline \(k\) fits the high-emission \(\varphi=0.75\) branch, and that both fit the second Assumption-4 bound in the high-emission \(\varphi=0.90\) branch.

The key wedge is analytic and independent of numerical sampling.

## Relationship to prior work
The motivating article explicitly imposes Assumption 4 to make its Stackelberg equilibria economically and mathematically feasible, including a two-sided bound on the abatement cost coefficient \(k\). It later announces the baseline values
\[
\alpha=0.20,\quad
\varphi\in\{0.75,0.90\},\quad
\delta=0.85,\quad
k\in\{1.1,1.3\},\quad
m=0.4,\quad
\theta\in\{0.7,1.45\},
\]
and uses those baselines to motivate its evolutionary sensitivity results.

Earlier green-supply-chain evolutionary-game studies, including Sun et al. (2019) and Sun, Wang, and Du (2025), analyze how subsidy, carbon price, emission-reduction cost, and initial strategy proportions alter evolutionary outcomes. They concern different payoff systems and do not contain the 2026 paper's two-sided \(k\)-restriction. They therefore do not imply the exact wedge
\[
\frac{(1-\alpha)\varphi}{2}<m\theta<(1-\alpha)\varphi
\]
or the exclusion of the 2026 low-emission baseline.

Searches using the exact DOI, the Assumption-4 formula, baseline values, and aliases such as feasibility, abatement-cost bound, and carbon-intensity restriction did not locate a published correction of this source-specific compatibility issue.

## Limitations
The result does not recompute the full constrained Stackelberg game outside Assumption 4. In particular, it does not determine which boundary solution would replace any closed-form interior solution when an abatement constraint becomes active.

The result also does not invalidate numerical integration of the replicator equations as an abstract dynamical system. It establishes that the excluded parameter runs are outside the feasible parameter domain stated by the paper itself, so they cannot by themselves validate the theory that was derived under that domain.

No claim is made that Assumption 4 is the only possible economically meaningful domain. A corrected or piecewise KKT analysis could enlarge the valid parameter region.

## References
1. A. Ahsan, Y. He, “An Evolutionary Game-Theoretic Analysis of Dual-Channel Encroachment and Green Fulfillment in Platform-Based Supply Chains,” Mathematics 14 (2026), 172. DOI: 10.3390/math14010172.
2. H. Sun, Y. Wan, L. Zhang, Z. Zhou, “Evolutionary game of the green investment in a two-echelon supply chain under a government subsidy mechanism,” Journal of Cleaner Production 235 (2019), 1315–1326. DOI: 10.1016/j.jclepro.2019.06.329.
3. H. Sun, K. Wang, X. Du, “Cooperative emission reduction behaviour of supply chain enterprises under cap-and-trade and government subsidies,” Environment, Development and Sustainability 27 (2025), 2549–2579. DOI: 10.1007/s10668-023-03980-w.
