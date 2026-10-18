# Optimal phase ordering for survival and convex dispersion in a branching population

## Finding

Consider any finite multiset of constant-rate environments applied sequentially to a linear birth–death population. Reordering the environments leaves its final mean unchanged, yet **ordering the environments by nonincreasing birth-to-death ratio simultaneously maximizes finite-horizon survival and minimizes the final abundance in convex order**. Reversing this order simultaneously minimizes survival and maximizes every convex-dispersion functional. With strictly positive birth and death rates and durations, these bounds are strict whenever a sequence has an inversion between unequal ratios.

More precisely, a schedule is a permutation \(\pi\) of \(m\ge1\) phases. Phase \(i\) has length \(t_i>0\), per-individual birth rate \(b_i>0\), and per-individual death rate \(d_i>0\). Starting with \(k\ge1\) independent ancestors at time zero, every individual independently gives birth to one new individual and dies at those rates in the current phase. There is no immigration, density dependence or interaction between lineages. Write \(Z_\pi\) for the final population.

Let \(\pi_\downarrow\) order the ratios \(b_i/d_i\) nonincreasingly and let \(\pi_\uparrow\) order them nondecreasingly. Then, for every permutation \(\pi\),

\[
\Pr(Z_{\pi_\downarrow}>0)\ge\Pr(Z_\pi>0)\ge\Pr(Z_{\pi_\uparrow}>0),
\qquad
Z_{\pi_\downarrow}\le_{\rm cx}Z_\pi\le_{\rm cx}Z_{\pi_\uparrow}.
\]

Here convex order means that every real convex function \(\varphi\) whose expectations are finite satisfies \(\mathbb E\varphi(Z_{\pi_\downarrow})\le\mathbb E\varphi(Z_\pi)\le\mathbb E\varphi(Z_{\pi_\uparrow})\). All schedules share the mean

\[
\mathbb E Z_\pi=k\exp\left(\sum_{i=1}^m (b_i-d_i)t_i\right).
\]

The extremal final laws depend only on a two-parameter family defined below. Ties in \(b_i/d_i\) may be permuted without changing the entire final distribution.

## Assumptions and scope

The states are \(0,1,2,\ldots\), with state-dependent total birth rate \(nb_i\) and total death rate \(nd_i\) while phase \(i\) operates. All rates and durations are fixed and positive. Finite phase durations guarantee nonexplosion for the linear process. The ordering compares permutations of the **same multiset of rate-duration triples**, not alternative physical trajectories with changed phase durations or changed rates. The result concerns abundance at the common terminal horizon \(T=\sum_i t_i\), not the whole time-dependent survival curve or the distribution of first-extinction time. The initial \(k\) ancestors behave independently under a common deterministic schedule.

Define, for each phase,

\[
 r_i=b_i-d_i,\quad
 a_i=e^{-r_i t_i},\quad
 h_i=\begin{cases}(1-a_i)/r_i,&r_i\ne0,\\t_i,&r_i=0,\end{cases}\quad
 c_i=b_i h_i.
\]

Always \(a_i,h_i,c_i>0\). For an ordered schedule \(\pi=(\pi_1,\dots,\pi_m)\), define

\[
 A=\prod_{j=1}^m a_{\pi_j},\qquad
 B_\pi=\sum_{j=1}^m c_{\pi_j}\prod_{\ell<j}a_{\pi_\ell}.
\]

The positive parameter \(A\) is permutation invariant; only \(B_\pi\) depends on phase order.

## Proof

**Step 1: linear-fractional generating functions.** For one initial individual during phase \(i\), let \(f_i(z)=\mathbb E[z^{Z(t_i)}\mid Z(0)=1]\), with \(0\le z\le1\). The branching backward equation and initial condition are

\[
 \partial_t f=b_i f^2-(b_i+d_i)f+d_i,\qquad f(0,z)=z.
\]

Setting \(y=1/(1-f)\) gives the linear equation \(\partial_t y=-r_i y+b_i\). Hence the exact stage map satisfies

\[
 \frac1{1-f_i(z)}=\frac{a_i}{1-z}+c_i.
\]

The branching property gives the whole-schedule generating function for one founder as the chronological composition \(f_{\pi_1}\circ\cdots\circ f_{\pi_m}\). Affine maps in \(1/(1-z)\) compose, so

\[
 G_\pi(z)=1-\frac{1-z}{A+B_\pi(1-z)}.
\]

In particular the final mean is \(G_\pi'(1)=1/A\). Every initial founder has an independent copy of this law and thus the \(k\)-founder generating function is \(G_\pi(z)^k\).

**Step 2: exact comparison under one adjacent swap.** Suppose the phases \(i,j\) occur consecutively in that order following a fixed prefix. Write \(a_{\rm pre}>0\) for the product of \(a\)'s in the prefix. From the formula for \(B\), and noting that the suffix receives the same multiplier \(a_i a_j\) whichever adjacent order is used,

\[
 B_{\dots ij\dots}-B_{\dots ji\dots}
 =a_{\rm pre}\big(c_i+a_i c_j-c_j-a_j c_i\big)
 =a_{\rm pre}h_i h_j(b_jd_i-b_i d_j).
\]

Consequently, placing the **larger** birth-to-death ratio first never increases \(B\), and decreases it strictly when the ratios differ. Repeated adjacent swaps sort any permutation. Thus

\[
 B_{\pi_\downarrow}\le B_\pi\le B_{\pi_\uparrow},
\]

and equality at an extreme is possible only when the original ordering has no strict ratio inversion relative to that extreme. The argument holds also when some \(b_i=d_i\), by continuity or by the exact definition of \(h_i\).

**Step 3: survival and full convex order.** Put \(s_\pi=A+B_\pi>0\). The one-founder final distribution is

\[
 \Pr(Z_\pi=0\mid k=1)=1-\frac1{s_\pi},\qquad
 \Pr(Z_\pi=n\mid k=1)=\frac{A}{s_\pi^2}
 \left(\frac{B_\pi}{s_\pi}\right)^{n-1}\quad(n\ge1).
\]

This follows by expanding the generating function as a geometric series. Thus survival from \(k\) founders is \(1-(1-1/s_\pi)^k\), which decreases strictly with \(B_\pi\).

For every integer cutoff \(q\ge0\), the one-founder stop-loss transform is

\[
 \mathbb E[(Z_\pi-q)_+\mid k=1]
 =\frac1A\left(\frac{B_\pi}{A+B_\pi}\right)^q.
\]

At \(q=0\) it is the common mean; for \(q\ge1\) it is strictly increasing in \(B_\pi\). Since nonnegative integer-valued laws with the same finite mean are in convex order exactly when all integer-threshold stop-loss transforms are ordered, this proves the convex-order conclusion for one founder. To extend to \(k\) founders, couple by independent sums and apply preservation of convex order under addition of an independent random variable, successively to each summand. This establishes the theorem for all \(k\ge1\).

For a single founder the exact variance is

\[
 \operatorname{Var}(Z_\pi)=\frac{2B_\pi}{A^2}+\frac1A-\frac1{A^2};
\]

for \(k\) founders it is \(k\) times this expression. The variance is consequently minimized by the same ratio ordering as extinction probability.

**Step 4: an exact fixed-mean risk separation.** Take a favorable environment with \((b,d,t)=(3,1,(\log2)/2)\) and an unfavorable environment with \((b,d,t)=(1,2,\log2)\). Their \((a,c)\) pairs are respectively \((1/2,3/4)\) and \((2,1)\). Both orders have \(A=1\), so the final mean from one founder equals one. Favorable first gives \(B=5/4\), survival probability \(4/9\) and variance \(5/2\). Unfavorable first gives \(B=5/2\), survival probability \(2/7\) and variance \(5\). This is a strict difference in extinction risk and population dispersion with identical total exposure, time horizon, and final mean.

## Verification

The companion standalone `verify.py` uses Python standard-library exact fractions to test the adjacent-swap identity for 1,024 pairs of noncritical, supercritical, and critical phase cases. It checks all 360 permutations of fifteen representative four-phase selections and validates the predicted survival, variance and integer-threshold stop-loss inequalities. An independent CTMC uniformization calculation then propagates the full population distribution through the two exact witness environments and confirms the rational survival and variance values numerically. The machine-readable `verification_certificate.json` records 3,917 exact assertions and eight independent forward-solver checks. These finite computations are corroboration; unrestricted claims follow from Steps 1–3.

To reproduce, run `python3 verify.py`; output should match the certificate. No external packages or network access are needed.

## Relationship to prior work

Kendall (1948) already solved the generalized linear birth–death process with time-varying per-capita rates. Its time-inhomogeneous branching law and the associated linear-fractional transformations are established background, not claimed as discoveries. Paradis (2011), accessible in full, applies the general model to temporal speciation/extinction and phylogenetic inference, including stepwise rate changes; it does not state the finite-phase permutation optimization or convex-order envelope. Crawford and Suchard (2012, online 2011), also inspected in full, study transition probabilities and numerical computation for general birth–death chains, not ordering prescribed ecological phases. Bhattacharya and Perlman (2017) concern conditional survival asymptotics of inhomogeneous branching processes, not the finite-order extremality considered here.

The specific contribution here is the **global sorting rule**, its strict equality condition, its simultaneous ordering of **all convex abundance losses**, and the exact comparison at a fixed, order-invariant mean. Because the complete Kendall (1948) paper could not be retrieved, it remains possible that older work includes the same exchange argument or a stronger rearrangement theorem; bibliographic independence has not been externally established.

## Limitations

The model is a single-type, linear, noninteracting branching process with exogenous deterministic phase lengths and uniformly acting positive per-capita rates. Results need not hold under density dependence, immigration, random or state-responsive switching, spatial structure, multitype branching, or phase-specific catastrophes. Optimizing terminal survival is not the same as optimizing time-to-extinction or survival at each intermediate time. The conclusions require no approximation but do not assert field-data validation. No independent audit has been conducted.

## References

- D. G. Kendall (1948), “On the Generalized ‘Birth-and-Death’ Process,” *Annals of Mathematical Statistics* 19(1), 1–15. DOI: 10.1214/aoms/1177730285. Public March 1948.
- E. Paradis (2011; first online 2010-11-05), “Time-Dependent Speciation and Extinction from Phylogenies: A Least Squares Approach,” *Evolution* 65(3), 661–672. DOI: 10.1111/j.1558-5646.2010.01179.x.
- F. W. Crawford and M. A. Suchard (2012; online 2011), “Transition probabilities for general birth-death processes with applications in ecology, genetics, and evolution,” *Journal of Mathematical Biology* 65, 553–580. DOI: 10.1007/s00285-011-0471-z.
- B. Bhattacharya and M. D. Perlman (2017), “Time-Inhomogeneous Branching Processes Conditioned on Non-Extinction,” arXiv:1703.00337.
