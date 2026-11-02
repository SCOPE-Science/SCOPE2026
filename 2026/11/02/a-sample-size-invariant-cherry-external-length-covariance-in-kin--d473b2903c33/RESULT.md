# A sample-size-invariant cherry–external-length covariance in Kingman coalescents

## Finding
For the standard Kingman coalescent on \(n\ge4\) labeled tips, denote the number of cherries by \(C_n\), the number of surviving singleton lineages when there are \(k\) lineages by \(S_k\), and total external branch length by \(L_n\). In the normalization where every unordered lineage pair coalesces at rate one, the exact levelwise dependence is

\[\operatorname{Cov}(C_n,S_k)=-\frac{k(k-1)(n-k)(n-k-1)}{3(n-1)(n-2)(n-3)},\qquad 2\le k\le n.\]

It follows that **the topology–length covariance does not depend on sample size**:

\[\boxed{\operatorname{Cov}(C_n,L_n)=-\frac29}\qquad(n\ge4).\]

For \(n=2,3\), \(C_n=1\) identically, so the covariance is zero. For \(n\ge4\), the levelwise covariance is strictly negative for \(2\le k\le n-2\) and vanishes for the top two levels. If every pair merger occurs at rate \(\lambda\), the displayed length covariance becomes \(-2/(9\lambda)\).

## Assumptions and scope
Start with \(n\) distinguishable singleton leaves. At a state with \(k\) extant ancestral lineages, choose a uniformly random unordered pair to merge; independently, remain at that state for \(T_k\sim\operatorname{Exp}\!\left(\binom{k}{2}\right)\), where exponential distributions are parameterized by rate. The variables \(T_k\), \(2\le k\le n\), are mutually independent and independent of the sequence of chosen pairs. Define a *cherry* to be one merger in which both children are singleton original leaves. Denote its total count by \(C_n\). Define \(S_k\) as the count of extant lineages containing precisely one original leaf. Define the total external branch length by \(L_n=\sum_{k=2}^nS_kT_k\). No branch above the most recent common ancestor is included.

## Proof
Fix \(n\ge4\). Write \((s)_r=s(s-1)\cdots(s-r+1)\) for falling factorials. At a level with \(k\) lineages and \(s\) singleton lineages, there are exactly \(\binom{s}{2}\) cherry-producing pairs, \(s(k-s)\) pairs joining a singleton to a composite lineage, and \(\binom{k-s}{2}\) pairs joining two composites. Their singleton-count decreases are respectively \(2,1,0\), and a cherry is created exactly in the first case.

**Singleton factorial moments.** For \(r=1,2,3\), \(r\) specified original leaves survive as singleton lineages through a merger at level \(h\) exactly if neither chosen lineage is among those \(r\) leaves. The probability of this event is \(\binom{h-r}{2}/\binom h2\). Multiplication from level \(n\) down to level \(k\) gives

\[\mathbb E[(S_k)_r]=\frac{(k)_r(k-1)_r}{(n-1)_r},\qquad r=1,2,3,\]

with the right side interpreted as zero when a numerator falling factorial vanishes. Expanding explicitly gives

\[a_k:=\mathbb E S_k=\frac{k(k-1)}{n-1},\quad b_k:=\mathbb E(S_k)_2=\frac{k(k-1)^2(k-2)}{(n-1)(n-2)},\]

\[e_k:=\mathbb E(S_k)_3=\frac{k(k-1)^2(k-2)^2(k-3)}{(n-1)(n-2)(n-3)}.\]

**Cherry counts before a level.** Let \(A_k\) be the number of cherries already created by the time the process first has \(k\) lineages; thus \(A_n=0\). The one-merger rules give

\[\mathbb E[A_{k-1}\mid A_k,S_k]=A_k+\frac{(S_k)_2}{k(k-1)}\]

and

\[\mathbb E[A_{k-1}S_{k-1}\mid A_k,S_k]=\frac{k-2}{k}A_kS_k+\frac{(S_k)_3}{k(k-1)}.\]

The second formula follows because \(\mathbb E[S_{k-1}\mid S_k=s]=(k-2)s/k\) and a newly created cherry contributes \(s-2\) singleton lineages after its merger. Iterating from \(A_n=0\), using the factorial-moment formulas and \(\sum_{r=0}^{m}r(r-1)=m(m+1)(m-1)/3\), yields

\[c_k:=\mathbb EA_k=\frac n3-\frac{k(k-1)(k-2)}{3(n-1)(n-2)},\]

\[d_k:=\mathbb E[A_kS_k]=\frac{k(k-1)}3\left(1-\frac{(k-1)(k-2)(k-3)}{(n-1)(n-2)(n-3)}\right).\]

These formulas also apply at \(k=2\); since \(n\ge3\), at most one original singleton can remain when only two lineages exist.

**Future cherries.** At a state with \(k\ge3\) lineages and \(s\) singleton lineages, the future pair-merging process is a fresh uniform \(k\)-coalescent. Any two specified singleton lineages form a cherry with probability \(2/[3(k-1)]\): by exchangeability this is \(\mathbb EC_k/\binom k2\), and the standard first-moment recurrence above with the terminal merger gives \(\mathbb EC_k=k/3\) for \(k\ge3\). Consequently

\[\mathbb E[C_n\mid\mathcal F_k]=A_k+\frac{S_k(S_k-1)}{3(k-1)}.\]

For \(k=2\) in a process initially having \(n\ge3\) lineages, \(S_2\le1\), so the same expression remains valid. Taking expectations gives \(\mathbb EC_n=n/3\). Multiplication by \(S_k\) and the identity \(s^2(s-1)=(s)_3+2(s)_2\) give

\[\mathbb E[C_nS_k]=d_k+\frac{e_k+2b_k}{3(k-1)}.\]

Subtracting \((n/3)a_k\), substituting the four expressions above and cancelling factors yields the claimed polynomial covariance profile.

**Length covariance.** Since the holding times are mutually independent and independent of all chosen merger pairs,

\[\operatorname{Cov}(C_n,L_n)=\sum_{k=2}^{n}\frac{2}{k(k-1)}\operatorname{Cov}(C_n,S_k).\]

Substituting the profile and evaluating \(\sum_{k=2}^{n}(n-k)(n-k-1)=(n-1)(n-2)(n-3)/3\) gives exactly \(-2/9\). This completes the proof.

## Verification
The standalone, dependency-free `verify.py` independently (i) enumerates every ranked labeled merger history for \(3\le n\le7\), (ii) checks every levelwise covariance against the theorem with exact rational arithmetic, (iii) computes the same moments by a separate probability-and-reward dynamic program for \(3\le n\le100\), and (iv) rechecks the finite sum producing the constant covariance. Execute `python3 verify.py`. A successful run prints `PASS` and the numbers of checks. All exhaustive and numerical computations have finite scopes; the formulas above prove the general statement.

## Relationship to prior work
The Kingman coalescent and its lineage holding-time normalization are classical. McKenzie and Steel's 1999 preprint (published in 2000) establishes the marginal cherry-count distribution and its moments under Yule-type tree topology. Dahmer and Kersting's 2013 preprint (published in 2015) develops external-branch-length and surviving-lineage statistics, including their asymptotic behavior. Frost and Volz (2013) analyze cherry and tip dynamics in phylogenetic models using rate-based transition descriptions and deterministic approximations. These provide the marginal and mechanistic context, but the inspected statements do not give the exact finite-sample mixed covariance, its quartic level profile, or the sample-size-invariant constant. A transition model alone is not being claimed as new.

## Limitations
The exact covariance depends on the standard constant pair-coalescence-rate normalization, and it need not persist for non-Kingman or population-size-varying coalescents. The result concerns covariance, not independence, conditional distribution, or a joint central limit theorem. Historical priority remains uncertain because some relevant primary materials, notably the complete text of Frost and Volz (2013), could not be inspected in full; indexed scientific sections concerning the dynamics were examined. The theorem's analytic proof is self-contained apart from elementary finite sums and the stated coalescent construction.

## References
- I. Dahmer and G. Kersting, *The internal branch lengths of the Kingman coalescent*, arXiv:1303.4562 (first posted 2013-03-19), Annals of Applied Probability 25 (2015), 1325–1348, DOI:10.1214/14-AAP1024. https://arxiv.org/abs/1303.4562
- A. McKenzie and M. Steel, *Distributions of cherries for two models of trees*, University of Canterbury Research Report 177 (May 1999); Mathematical Biosciences 164 (2000), 81–92, DOI:10.1016/S0025-5564(99)00060-7. https://ir.canterbury.ac.nz/bitstreams/246ff6f4-967f-4550-9f98-c4b3d671fe84/download
- S. D. W. Frost and E. M. Volz, *Modelling tree shape and structure in viral phylodynamics*, Philosophical Transactions of the Royal Society B 368 (2013), 20120208, DOI:10.1098/rstb.2012.0208. https://doi.org/10.1098/rstb.2012.0208
- S. Zhu, J. Degnan, M. Steel, *Clades and clans: a comparison study of two evolutionary models*, arXiv:1407.3880 (2014). https://arxiv.org/html/1407.3880v1
