# Exact finite-population cooperation-advantage peak in threshold collective action

## Finding

In the finite-population \(N\)-person threshold collective-action game defined below, a cooperator's expected payoff advantage over a defector has an **exact universal composition mode**. Let \(Z>N\ge3\) be integers, let \(2\le M\le N-1\), and let \(k\in\{1,\ldots,Z-1\}\) count the cooperators in the total population. If \(\Delta(k)\) denotes the cooperator-minus-defector expected payoff at composition \(k\), then, for every benefit multiplier \(F>0\) and contribution cost \(c>0\), the maximizers of \(\Delta\) are

\[
\operatorname*{argmax}_{1\le k\le Z-1}\Delta(k)=
\begin{cases}
\{\lceil MZ/N-1\rceil\},&N\nmid MZ,\\
\{MZ/N-1,\ MZ/N\},&N\mid MZ.
\end{cases}
\]

This mode location is independent of the benefit, cost, and positive pairwise-comparison intensity. The payoff advantage changes sign at most twice as the population's number of cooperators increases. More precisely, define the hypergeometric function \(H(k)\) below and its maximum \(H_*>1\); the exact threshold for cooperation to be advantageous in **at least one** nonabsorbing population composition is

\[
F_{\mathrm{crit}}=\frac{N(Z-1)}{(Z-N)H_*}.
\]

For \(0<F<F_{\mathrm{crit}}\), every \(\Delta(k)<0\). At equality, the only neutral compositions are the one or two maximizing compositions and all others favor defection. For \(F>F_{\mathrm{crit}}\), the compositions favoring cooperation form a nonempty consecutive interval of integers. A second threshold \(F_{\mathrm{tail}}=N(Z-1)/(Z-N)>F_{\mathrm{crit}}\) governs the all-but-one-cooperator endpoint: \(\Delta(Z-1)\) is negative, zero, or positive according as \(F<F_{\mathrm{tail}}\), \(F=F_{\mathrm{tail}}\), or \(F>F_{\mathrm{tail}}\). In particular, throughout \(F_{\mathrm{crit}}<F<F_{\mathrm{tail}}\), selection disfavors cooperation at both extremes but favors it at an intermediate consecutive band, attaining the two-sign-transition bound.

## Assumptions and scope

The population contains \(Z\) individuals, of whom \(k\) cooperate and \(Z-k\) defect, where \(1\le k\le Z-1\). Groups have fixed size \(N<Z\). To evaluate an individual's payoff, choose \(N-1\) distinct co-players uniformly without replacement from the other \(Z-1\) individuals. For a group with \(j\in\{0,\ldots,N\}\) cooperators, each group member receives benefit \(cFj/N\) if \(j\ge M\), and zero group benefit otherwise. Each cooperator also pays cost \(c>0\), irrespective of success. We require integers \(Z>N\ge3\), \(2\le M\le N-1\), and multiplier \(F>0\). These restrictions ensure a nontrivial interior action threshold and exclude degenerate boundary games.

Write \(\pi_C(k)\) and \(\pi_D(k)\) for the average payoffs to a cooperator and a defector, respectively, and \(\Delta(k)=\pi_C(k)-\pi_D(k)\). Under pairwise Fermi comparison with any intensity \(\beta>0\), the sign of the selective transition bias is the sign of \(\Delta(k)\). The result does not claim a count of fixed points of a finite-state Markov chain, fixation-probability inequalities, or behavior with mutation, spatial assortment, threshold-dependent cost, or stochastic group size.

For \(J_k\) distributed hypergeometrically with population size \(Z-2\), number of successes \(k-1\), and sample size \(N-1\), set

\[
H(k)=\Pr(J_k\ge M)+M\Pr(J_k=M-1).
\]

The precise probability mass is

\[
\Pr(J_k=j)=\frac{\binom{k-1}{j}\binom{Z-k-1}{N-1-j}}{\binom{Z-2}{N-1}},
\]

where out-of-range binomial coefficients are zero.

## Proof

**1. Reduction of both focal payoffs.** Put \(u(j)=j\mathbf1_{\{j\ge M\}}\). A focal cooperator has \(k-1\) cooperating co-players in the other \(Z-1\) individuals, whereas a focal defector has \(k\). Couple these two uniform co-player draws by replacing one defector in the cooperator's sampling pool with one cooperator in the defector's sampling pool. If the distinguished replaced individual is selected, the two groups contain the same total number of cooperators, so their benefit difference is zero. This inclusion event has probability \((N-1)/(Z-1)\). Otherwise the cooperator group has one more cooperator and the common \(N-1\) co-players come from the remaining \(Z-2\) individuals, which contain exactly \(k-1\) cooperators. The marginal benefit difference is

\[
u(j+1)-u(j)=\mathbf1_{\{j\ge M\}}+M\mathbf1_{\{j=M-1\}}.
\]

After subtracting the cooperator's certain cost, we obtain the exact identity

\[
\boxed{\Delta(k)=c\left[-1+\frac{F(Z-N)}{N(Z-1)}H(k)\right].}
\tag{1}
\]

In particular, \(F>0\) and \(c>0\) imply that \(H\) and \(\Delta\) have the same maximizing compositions.

**2. Exact adjacent-difference factorization.** Couple the hypergeometric draws defining \(H(k)\) and \(H(k+1)\) by turning one previously defective individual in the \(Z-2\) background into a cooperator. This distinguished individual occurs in the \(N-1\)-sample with probability \((N-1)/(Z-2)\). Conditioned on inclusion, the other \(N-2\) sampled individuals contain \(X\) cooperators, with

\[
X\sim\operatorname{Hypergeom}(Z-3,k-1,N-2).
\]

Writing \(h(j)=u(j+1)-u(j)\), we have

\[
h(j+1)-h(j)=M\mathbf1_{\{j=M-2\}}-(M-1)\mathbf1_{\{j=M-1\}}.
\]

Therefore

\[
H(k+1)-H(k)=\frac{N-1}{Z-2}
\left[M\Pr(X=M-2)-(M-1)\Pr(X=M-1)\right].
\]

Substitute the two hypergeometric masses. The elementary binomial ratios

\[
\frac{\binom{Z-k-2}{N-M}}{\binom{Z-k-2}{N-M-1}}
=\frac{Z-N-k+M-1}{N-M},\qquad
\frac{\binom{k-1}{M-1}}{\binom{k-1}{M-2}}
=\frac{k-M+1}{M-1}
\]

hold whenever the denominators are positive. At zero boundaries the same equality follows directly from the two masses using the out-of-range convention. Collecting terms yields the globally valid exact factorization, for all \(1\le k\le Z-2\):

\[
\boxed{
H(k+1)-H(k)=
\frac{N-1}{Z-2}
\frac{\binom{k-1}{M-2}\binom{Z-k-2}{N-M-1}}{\binom{Z-3}{N-2}}
\frac{MZ-N(k+1)}{N-M}.}
\tag{2}
\]

The nonnegative prefactor is strictly positive precisely when \(M-1\le k\le Z-N+M-1\). Put \(t=MZ/N-1\). The inequalities

\[
M-1<t<Z-N+M-1
\]

follow respectively from \(M(Z-N)>0\) and \((N-M)(Z-N)>0\). Thus, on the entire active interval, the sign of the increment is the sign of \(t-k\). Before that interval \(H\) is constantly zero, and after it \(H\) is constantly one. This proves the exact unique maximizer at \(\lceil t\rceil\) when \(t\notin\mathbb Z\), and the exact pair \(\{t,t+1\}\) when \(t\in\mathbb Z\). It also proves \(H(1)=0\), \(H(Z-1)=1\), and \(H_*>1\), because the active region has strictly positive increments before its maximum and strictly negative increments after it.

**3. Benefit thresholds and sharp sign-transition count.** Formula (1) says \(\Delta(k)>0\) exactly when \(H(k)>N(Z-1)/(F(Z-N))\). The strict one-peak behavior from (2) makes each strict upper level set of \(H\) either empty or a consecutive interval. The minimum benefit for a nonempty upper level set is exactly \(F_{\mathrm{crit}}\), with neutrality solely at the mode(s) at equality. Since \(H(1)=0\) and \(H(Z-1)=1\), the high-cooperation endpoint has the separate transition \(F_{\mathrm{tail}}\). Since \(H_*>1\), \(F_{\mathrm{crit}}<F_{\mathrm{tail}}\). All benefit multipliers strictly between them produce negative, then positive, then negative selective bias as \(k\) increases, possibly with neutral compositions at the separating boundaries. Thus two strict sign transitions are attainable and no more than two can occur. Positive pairwise-comparison intensity preserves all signs by monotonicity of the Fermi function. This completes the proof.

## Verification

The self-contained file `verify.py` independently computes focal cooperator and defector expectations using separate hypergeometric sampling pools, then compares their difference with (1). It also verifies (2) and the mode classification in every nondegenerate parameter triple with \(4\le Z\le20\). The replay reported 43,605 exact independent payoff checks and 13,566 exact adjacent-difference checks, with no failure. These finite checks are not a proof of the universally quantified theorem; the proof is the coupling argument and exact binomial factorization above.

The sharp example has \((Z,N,M,F,c)=(10,5,3,6,1)\). For \(k=1,\dots,9\), its hypergeometric levels are

\[
H(k)=\left(0,0,\frac9{14},\frac{19}{14},\frac{25}{14},\frac{25}{14},\frac{10}7,1,1\right).
\]

Its payoff differences are exactly

\[
\Delta(k)=\left(-1,-1,-\frac47,-\frac2{21},\frac4{21},\frac4{21},-\frac1{21},-\frac13,-\frac13\right).
\]

Hence cooperation is advantageous only at \(k\in\{5,6\}\) and is disadvantageous at both population-composition extremes. The independently checked benefit thresholds are \(F_{\mathrm{crit}}=126/25\) and \(F_{\mathrm{tail}}=9\).

Reproduce with `python3 verify.py` in the same directory; the standard library suffices.

## Relationship to prior work

Pacheco, Santos, Souza, and Skyrms (2008, DOI 10.1098/rspb.2008.1126) introduced this finite/infinite-population threshold stag-hunt model, analyzed the hypergeometric finite-population payoffs, and displayed numerically the rich phase structure. Their accessible full mathematical development and the follow-up Pacheco–Santos–Souza–Skyrms (2011) article do not state factorization (2), the exact universal finite-population mode, or the two sharp benefit thresholds. The underlying model and finite-population payoff equations belong to that prior work and are not claimed as new.

Peña, Lehmann, and Nöldeke (2014, arXiv:1310.0498, DOI 10.1016/j.jtbi.2013.12.016) develop the gain-from-switching/Bernstein-polynomial perspective for large, well-mixed populations. Their binomial (independent co-player) arguments illuminate the meaning of unimodality, but they do not imply the particular finite sampling-without-replacement identity (2) or its integer-valued mode location without a separate argument. Bach, Helvik, and Christiansen (2006) analyze threshold games and evolutionary equilibria in a related deterministic setting; those results do not directly specify the finite hypergeometric maximizer.

## Limitations

This is an exact characterization of the **selective drift sign at each interior finite-population composition**, not of fixation probabilities or the long-term distribution of a Markov process. With \(F=F_{\mathrm{crit}}\), neutral compositions do not become absorbing states under the ordinary stochastic update rule. The exact identity assumes uniform group sampling without replacement, group benefit proportional to the count of contributors once threshold is reached, and a constant contribution cost. Benefit nonlinearities, group-size mixtures, spatially localized meetings, or heterogeneous costs can change the location or number of modes. Although primary-source comparisons support originality in this specific formulation, undiscovered equivalent finite-population arguments remain a residual bibliographic risk, and no independent audit has been carried out.

## References

1. J. M. Pacheco, F. C. Santos, M. O. Souza, B. Skyrms, “Evolutionary dynamics of collective action in \(N\)-person stag hunt dilemmas,” *Proceedings of the Royal Society B* 276 (2009), 315–321; published online September 23, 2008. DOI: 10.1098/rspb.2008.1126. Full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC2674356/ .
2. J. M. Pacheco, F. C. Santos, M. O. Souza, B. Skyrms, “Evolutionary dynamics of collective action,” in *The Mathematics of Darwin's Legacy* (2011), accessible author manuscript: https://atpgroup.org/jmp/PDFs/130.pdf .
3. J. Peña, L. Lehmann, G. Nöldeke, “Gains from switching and evolutionary stability in multi-player matrix games,” *Journal of Theoretical Biology* (2014), arXiv:1310.0498, DOI: 10.1016/j.jtbi.2013.12.016.
4. L. A. Bach, T. Helvik, F. B. Christiansen, “The evolution of \(n\)-player cooperation—threshold games and ESS bifurcations,” *Journal of Theoretical Biology* (2006).
