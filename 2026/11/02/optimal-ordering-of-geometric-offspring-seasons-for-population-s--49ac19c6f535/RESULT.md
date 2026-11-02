# Optimal ordering of geometric-offspring seasons for population survival

## Finding

A calendar of a fixed multiset of distinct reproductive seasons can have the same expected final abundance but different probabilities of extinction. In the finite, density-independent population model below, **one scalar score per season gives an exact global ordering for every calendar length**. The score uses both the season's expected reproduction and its geometric-offspring scale; ordering solely by expected reproduction need not be optimal.

For season \(i\) with offspring mean \(m_i\) and geometric scale \(a_i\), define
\[
\theta_i=\frac{m_i-1}{a_i}.
\]
Among all permutations of a prescribed multiset of \(n\ge2\) seasons, placing the scores in **nonincreasing** order maximizes the chance of at least one descendant after \(n\) generations, minimizes final population size in convex order, and minimizes its variance. Nondecreasing score order simultaneously gives the opposite extrema. A swap of adjacent unequal-score seasons is strictly improving in the indicated direction; tied scores can be freely interchanged. These statements compare calendar arrangements using the same offspring laws, not different individual reproductive budgets.

If the ordered seasonal calendar is repeated indefinitely and the product of its mean offspring counts exceeds one, the same nonincreasing-score order also maximizes the founder lineage's probability of permanent survival. This does not assert persistence when the product is at most one.

## Assumptions and scope

Consider a discrete-generation branching population starting from \(Z_0=1\). Individuals reproduce independently, offspring follow the law of the current season, and all individuals within a given generation have that season's offspring law. There is no immigration, density dependence or environmental feedback. Choose \(n\ge2\) reproductive seasons with pairs \((m_i,a_i)\) satisfying
\[
 a_i>0,\qquad 0<m_i\le1+a_i.
\]
Their probability-generating functions are
\[
 f_i(s)=1-\frac{m_i(1-s)}{1+a_i(1-s)},\qquad 0\le s\le1.
\]
Equivalently, \(\Pr(X_i=0)=1-m_i/(1+a_i)\) and, for integers \(k\ge1\),
\[
 \Pr(X_i=k)=\frac{m_i}{(1+a_i)^2}\left(\frac{a_i}{1+a_i}\right)^{k-1}.
\]
The upper bound on \(m_i\) makes these probabilities nonnegative. A calendar \(\pi\) uses season \(\pi(1)\) first and \(\pi(n)\) last. Comparisons are made at the common horizon of exactly \(n\) generations. In the periodic statement the *whole* calendar is repeated in the same order ad infinitum.

## Proof

**1. Closed composition.** Direct substitution shows that the functions \(F_{M,C}(s)=1-M(1-s)/(1+C(1-s))\) satisfy
\[
 F_{M_1,C_1}\bigl(F_{M_2,C_2}(s)\bigr)
 =F_{M_1M_2,\,C_2+C_1M_2}(s).
\]
Induction gives the \(n\)-generation generating function
\[
 G_\pi(s)=f_{\pi(1)}\circ\cdots\circ f_{\pi(n)}(s)
 =1-\frac{M(1-s)}{1+C_\pi(1-s)},
\]
where
\[
 M=\prod_{i=1}^n m_i>0,\qquad
 C_\pi=\sum_{i=1}^n a_{\pi(i)}\prod_{j=i+1}^{n}m_{\pi(j)}>0.
\]
Thus \(M=\mathbb E[Z_n]\) is independent of ordering and
\[
 \Pr_\pi(Z_n>0)=\frac{M}{1+C_\pi}.
\]

**2. Exact adjacent-interchange law.** Suppose seasons \(i,j\) occupy consecutive calendar positions, with all remaining seasons held fixed. Write \(T>0\) for the product of the means of the seasons *after* this pair, taking \(T=1\) if the pair comes last. All other terms in \(C_\pi\) are unaffected by their interchange. Therefore
\[
 C_{\ldots,i,j,\ldots}-C_{\ldots,j,i,\ldots}
 =T\{a_i(m_j-1)-a_j(m_i-1)\}
 =Ta_ia_j(\theta_j-\theta_i).
\]
An inversion relative to nonincreasing score order can be exchanged to strictly decrease \(C_\pi\) when the scores differ. Successive adjacent exchanges sort any finite calendar and attain the global minimum. Reversing them attains the global maximum. Equality under exchanging a pair occurs exactly when its scores tie. The ordering for final-generation survival follows because \(M/(1+C)\) is strictly decreasing in \(C>0\).

**3. Complete distribution and risk ordering.** Expanding the composite generating function yields
\[
 \Pr_\pi(Z_n=0)=1-\frac{M}{1+C_\pi},\qquad
 \Pr_\pi(Z_n=k)=\frac{M}{(1+C_\pi)^2}
 \left(\frac{C_\pi}{1+C_\pi}\right)^{k-1}\quad(k\ge1).
\]
For each integer \(t\ge0\), summing the geometric tail gives the exact stop-loss expectation
\[
 \mathbb E_\pi[(Z_n-t)_+]
 =M\left(\frac{C_\pi}{1+C_\pi}\right)^t.
\]
For noninteger \(t\ge0\) the stop-loss expression is the linear interpolation of its two neighboring integer values, since \(Z_n\) is integer-valued. For \(t<0\), it is simply \(M-t\). Hence smaller \(C_\pi\) gives smaller stop-loss expectations for every real \(t\), with equal means. This is exactly the usual convex-order comparison, and also gives
\[
 \operatorname{Var}_\pi(Z_n)=M(1+2C_\pi-M).
\]
The existence of ties does not affect the extremal ordering.

**4. Repeated seasonal cycles.** If the calendar repeats, the population at the ends of successive full cycles is an ordinary Galton–Watson process with offspring PGF \(G_\pi\), mean \(M\), and coefficient \(C_\pi\). Extinction is almost sure for \(M\le1\). When \(M>1\), the positive fixed-point solution of \(G_\pi(s)=s\) is the founder's permanent survival probability
\[
 \Pr_\pi(Z_t>0\text{ for all }t\ge0)
 =\frac{M-1}{C_\pi}.
\]
Because every full cycle has the same \(M\), the score-sorted extremizers remain optimal. Survival at cycle boundaries is equivalent to survival at all intermediate generations because zero is absorbing.

**5. Why sorting by mean can be wrong.** Take two legitimate seasons \((m,a)=(3,7)\) and \((2,2)\). Their scores are respectively \(2/7\) and \(1/2\). The *lower-mean* season must come first: its calendar has \((M,C)=(6,13)\), giving two-generation survival \(3/7\) and repeated-cycle permanent survival \(5/13\). Putting the higher-mean season first gives \((M,C)=(6,16)\), survival \(6/17\), and repeated-cycle survival \(5/16\). In both calendars the expected two-generation population equals six.

## Verification

Run `python3 CHECK.py` using Python's standard library. Its deterministic exact-rational test suite verifies composition formulas, adjacent-commutator signs, all permutations of 150 randomly generated admissible rational season multisets of sizes two through six, stop-loss comparisons, supercritical periodic-survival formulas, and both explicitly stated examples. The packaged suite passed **152,229 exact-rational assertions**. These finite checks corroborate the formulas; the adjacent-exchange and PGF arguments above establish the theorem for all admissible real parameters and every finite calendar length.

## Relationship to prior work

Finite-population survival in variable environments was studied by Mountford (1971). Keiding and Nielsen's 1973 report and 1975 article explicitly develop linear-fractional offspring generating functions in varying and random environments: the closure family and general extinction formulas are **established prior machinery**. Jagers (1974) gives the general varying-environment branching framework. Pellerey (2007) compares populations across different dependence structures of *random environmental sequences* using supermodular and related orders. None of the inspected accessible material states the exact deterministic permutation score, the sharp adjacent-interchange equality criterion, or the combined finite and periodic ecological calendar extrema. The relevant Keiding–Nielsen full technical text could not be independently inspected in full; therefore historical priority remains provisional. The new claim is the ecological calendar optimization and sharp ordering characterization, not the branching-process construction, fractional-linear closure, or general comparison-order methods.

## Limitations

The theorem assumes a prescribed, deterministic multiset of seasons, independent individual reproduction, zero-inflated geometric offspring, and exact parameter knowledge. It concerns founder lineage survival and final-population dispersion, not density-regulated persistence, optimal weather control, random calendar feedback or empirical field populations. The variance and convex-order consequences should not be construed as new general stochastic-order principles. Earlier literature in a closely matching offspring family remains a material historical-priority risk; no claim of independent peer validation is made.

## References

1. Mountford, M. D. (1971), *Population survival in a variable environment*, Journal of Theoretical Biology 32(1), 75–79. DOI: https://doi.org/10.1016/0022-5193(71)90136-6. OpenAlex first-publication index: https://openalex.org/W2058118050 (date recorded 1971-07-01; original day within July not otherwise verified).
2. Keiding, N. and Nielsen, J. E. (1973), *Branching Processes with Varying and Random Geometric Offspring Distributions*, Stanford Department of Statistics report COV NSF 6 (November 1973). https://statistics.stanford.edu/technical-reports/branching-processes-varying-and-random-geometric-offspring-distributions. Journal version (1975), Journal of Applied Probability 12(1), 135–141, https://doi.org/10.2307/3212415.
3. Jagers, P. (1974), *Galton–Watson processes in varying environments*, Journal of Applied Probability 11(1), 174–178. https://doi.org/10.2307/3212594.
4. Pellerey, F. (2007), *Comparison results for branching processes in random environments*, Journal of Applied Probability 44(1), 142–150. https://doi.org/10.1239/jap/1175267168.
5. Kersting, G. (2020), *A unifying approach to branching processes in a varying environment*, Journal of Applied Probability 57(1), 196–220. Preprint: https://arxiv.org/abs/1703.01960.
