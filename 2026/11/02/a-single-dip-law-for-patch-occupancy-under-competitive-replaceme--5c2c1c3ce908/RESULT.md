# A single-dip law for patch occupancy under competitive replacement

## Finding

A competitively superior invader can **reduce total habitat occupancy** even while its own occupancy rises. For a homogeneous patch with an arbitrary finite, irreducible, reversible resident ecological process, there is a complete sharp dichotomy: total occupancy either increases strictly with the invader's arrival pressure, or falls to **exactly one** minimum and then rises. The dividing parameter is one integrated resident return-time statistic.

Let \(0\) designate the empty patch and let \(\pi_0\) be its resident-only stationary probability. Define
\[
T=\int_0^\infty \bigl(\Pr_0\{X_t=0\}-\pi_0\bigr)\,dt,
\qquad v_c=\frac{\pi_0}{T}.
\]
The integral is finite and strictly positive. If the invader has local extinction rate \(v\), and its pressure is \(b>0\), the equilibrium total occupancy \(O(b)\) obeys:

- For \(0<v\le v_c\), \(O(b)\) is strictly increasing on \((0,\infty)\).
- For \(v>v_c\), there is exactly one \(b_*>0\) such that \(O(b)\) strictly decreases on \((0,b_*)\) and strictly increases on \((b_*,\infty)\). This is a strict global minimum.

The invader's own stationary occupancy, \(b/(b+v)\), is strictly increasing in both regimes. Thus the nonmonotonicity comes from replacement of longer-persisting resident occupation by a shorter-persisting invader, not from declining invader establishment.

## Assumptions and scope

Consider a single ecological patch. Its resident-state space \(S\) is finite with at least two states, one of which is empty, labeled \(0\). A conservative continuous-time generator \(Q=(q_{ij})\) acts on the states \(S\). It is irreducible and reversible for its unique strictly positive stationary distribution \(\pi\): \(\pi_iq_{ij}=\pi_jq_{ji}\) for all states. All nonempty resident states count as habitat occupied; they need not encode only one species.

Append a state \(I\) in which a superior invader occupies the patch and excludes all residents. At independent Poisson rate \(b>0\), the invader arrives and replaces any resident state by \(I\); at rate \(v>0\) it becomes locally extinct and returns the patch to \(0\). The baseline generator \(Q\) operates only outside \(I\); no resident transitions occur inside \(I\). These assumptions define a finite irreducible continuous-time Markov chain and its unique stationary distribution. The scalar \(b\) is external pressure, not endogenously determined by a spatial metacommunity.

Write \(p_0(b)\) for stationary probability of an empty patch, \(p_I(b)\) for invader occupancy, and \(O(b)=1-p_0(b)\) for **total** (resident-or-invader) occupancy. All conclusions concern \(b>0\), with endpoints interpreted as limits.

## Proof

**1. Exact stationary occupation by a reset resolvent.** Balance between the invader and resident subsets gives
\[
p_I(b)=\frac{b}{b+v},\qquad \sum_{j\in S}p_j(b)=\frac{v}{b+v}.
\]
In row-vector notation, the resident stationary balance is
\[
p_S(b)(bI-Q)=vp_I(b)e_0^{\top},
\]
where \(e_0\) selects the empty state. The matrix \(bI-Q\) is invertible for every \(b>0\). Hence, with
\[
h(b)=b[(bI-Q)^{-1}]_{00}
=b\int_0^\infty e^{-bt}(e^{Qt})_{00}\,dt,
\]
we have the exact identities
\[
p_0(b)=\frac{v}{b+v}h(b),\qquad
O(b)=1-\frac{v}{b+v}h(b).
\]
This proves the formula without approximation or time-scale separation.

**2. A strictly concave spectral mixture.** Reversibility makes \(Q\) self-adjoint in \(L^2(\pi)\). Since the finite chain is irreducible, its nonzero eigenvalues are strictly negative. The diagonal return probability therefore has a spectral expansion
\[
(e^{Qt})_{00}=\pi_0+\sum_{j=1}^{m}c_j e^{-\lambda_jt},
\qquad c_j\ge0,\quad \lambda_j>0,\quad
\sum_jc_j=1-\pi_0>0.
\]
Repeated eigenvalues may be combined. The coefficients are nonnegative **because the same empty-state indicator occurs on both sides of a reversible spectral projection**; this positivity is the substantive hypothesis behind the conclusion. Integrating yields
\[
h(b)=\pi_0+\sum_j c_j\frac{b}{b+\lambda_j},\qquad
T=\sum_j\frac{c_j}{\lambda_j}>0.
\]
In particular,
\[
h'(b)=\sum_j\frac{c_j\lambda_j}{(b+\lambda_j)^2}>0,
\qquad h''(b)=-2\sum_j\frac{c_j\lambda_j}{(b+\lambda_j)^3}<0.
\]
These derivatives and all displayed integrals are finite. Moreover, \(h(0+)=\pi_0\), \(h'(0+)=T\), and \(h(b)\to1\) as \(b\to\infty\).

**3. Exactly zero or one turning point.** Differentiate the empty probability to obtain
\[
p_0'(b)=\frac{v}{(b+v)^2}F(b),
\quad F(b)=(b+v)h'(b)-h(b).
\]
The central monotonicity identity is
\[
F'(b)=(b+v)h''(b)<0\qquad(b>0).
\]
Its endpoint values are \(F(0+)=vT-\pi_0\) and \(F(\infty)=-1\). When \(vT\le\pi_0\), strict decrease makes \(F(b)<0\) for every positive \(b\), so \(p_0\) decreases and \(O\) increases strictly. When \(vT>\pi_0\), continuity, strict decrease, and the endpoint signs give **exactly one** zero \(b_*\); \(p_0\) rises then falls, so \(O\) falls then rises with its unique strict global minimum at \(b_*\). This proves both alternatives, including the critical equality case.

**4. Exact ecological counterexample.** Take just two resident states, empty \(0\) and occupied \(1\), with resident colonization and extinction rates both one:
\[
Q=\begin{pmatrix}-1&1\\1&-1\end{pmatrix},\qquad
\pi_0=\frac12,\qquad T=\frac14,\qquad v_c=2.
\]
For invader extinction rate \(v=10\), direct inversion gives
\[
p_0(b)=\frac{10(1+b)}{(10+b)(2+b)},
\qquad O(b)=1-\frac{10(1+b)}{(10+b)(2+b)}.
\]
The unique stationary occupancy minimum occurs at \(b_*=2\), with
\[
O(2)=\frac38<\frac12=\lim_{b\downarrow0}O(b),
\qquad \lim_{b\to\infty}O(b)=1.
\]
The intruding competitor's own occupancy \(b/(b+10)\) rises monotonically. Both the threshold and the interior minimum therefore occur even in the smallest nontrivial resident process.

## Verification

The accompanying self-contained `CHECK.py` uses exact rational arithmetic for irreducible reversible generators constructed from symmetric conductances and positive stationary masses. It compares the augmented chain's directly solved stationary probability against the resolvent formula, and verifies the derivative signs and threshold identities for many finite examples. It also checks the exact two-state minimum and general two-state stationary formula. Run `python3 CHECK.py` from the directory containing this document. These finite computations test implementations and boundary examples; they are **not** substituted for the all-finite-state spectral proof above.

## Relationship to prior work

The competition-colonization literature describes replacement of inferior resident competitors by superior propagules, including the classical hierarchical model and its stochastic local-community refinements; see Orrock and Watling (2010). Its state descriptions, feedback and propagation assumptions differ from the single-patch reversible-background model here. General renewal and resolvent formulas for Markov processes with killing and resurrection appear in Pakes (1997, accessible publication record 2007); more recent resetting analyses include Meylahn, Sabhapandit and Touchette (2015), and the spectral-resetting study of Rose and colleagues (2018). The resolvent identity used here is **not itself new**. The assessed specific addition is the sharp all-finite-state ecological occupancy classification by \(vT/\pi_0\), including its strict one-minimum conclusion and explicit ecological inversion example. The accessible literature inspections did not establish the same classification. This is not a proof of historical priority, particularly because the complete Pakes text was not available for comparison.

## Limitations

The theorem does not address nonreversible resident dynamics, time-varying invader arrivals, multiple invaders, partial displacement, spatially coupled patches, delayed recovery, or competition feedback on invader pressure. Strict reversibility is important: without the nonnegative diagonal spectral coefficients, strict concavity of \(h\) need not follow. The result concerns exact stationary probabilities rather than finite observation horizons, field data, or a calibrated management intervention. No claim is made that all ecological communities have a single-dip response.

## References

- Pakes, A. G., *Killing and resurrection of Markov processes*, Communications in Statistics—Stochastic Models 13 (1997), 255–269. DOI: https://doi.org/10.1080/15326349708807425 . Public online record dated 21 March 2007.
- Orrock, J. L. and Watling, J. I., *Local community size mediates ecological drift and competition in metacommunities*, Proceedings of the Royal Society B (2010). https://pmc.ncbi.nlm.nih.gov/articles/PMC2880146/
- Meylahn, J. M., Sabhapandit, S. and Touchette, H., *Large deviations for Markov processes with resetting*, Physical Review E 92 (2015). https://arxiv.org/abs/1510.02431
- Rose, D. C., Touchette, H., Lesanovsky, I. and Garrahan, J. P., *Spectral properties of simple classical and quantum reset processes*, Physical Review E 98 (2018). https://doi.org/10.1103/PhysRevE.98.022129
