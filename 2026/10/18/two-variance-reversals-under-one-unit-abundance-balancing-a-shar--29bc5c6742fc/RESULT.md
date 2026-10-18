# Two variance reversals under one-unit abundance balancing: a sharp eight-individual threshold and an unbounded family

## Finding

Consider a finite community with positive integer species abundances \(a=(a_1,\ldots,a_s)\), \(s\ge 2\), totaling \(N\). Draw \(m\) of its individuals uniformly without replacement and let \(K_m(a)\) count species present in the sample. A *one-unit balancing transfer* replaces two abundances \(x,y\), with \(x\ge y+2\), by \(x-1,y+1\); all other abundances are unchanged. For a transfer \(a\to b\), set

\[
\Delta_m(a,b)=\operatorname{Var}(K_m(b))-\operatorname{Var}(K_m(a)),\qquad 1\le m\le N.
\]

A strict sign reversal means that consecutive **nonzero** entries of \((\Delta_1,\ldots,\Delta_N)\), after zero entries have been removed, have opposite signs. Then:

1. For every one-unit balancing transfer on any community with \(N\le7\), the variance-difference sequence has at most one strict sign reversal. At \(N=8\), up to permutation of species, there is **exactly one** transfer with at least two reversals:
\[
(4,3,1)\longrightarrow(4,2,2).
\]
Its variance differences at sample sizes \(m=1,\ldots,8\) are
\[
\left(0,-\frac{11}{784},\frac{73}{3136},\frac1{245},-\frac{55}{784},-\frac{95}{784},-\frac7{64},0\right).
\]
Thus balancing decreases variance at \(m=2\), increases it at \(m=3,4\), and decreases it again at \(m=5,6,7\), even though expected sample richness rises at every \(2\le m\le7\).

2. The phenomenon persists for arbitrarily large community censuses. For every integer \(k\ge1\), the one-unit transfer
\[
A_k=(4k,3k,k)\longrightarrow B_k=(4k,3k-1,k+1)
\]
with total \(N=8k\) has
\[
\Delta_2(A_k,B_k)<0,\qquad\Delta_3(A_k,B_k)>0,\qquad\Delta_7(A_k,B_k)<0.
\]
These are two strict sign reversals along the sequence of sample sizes, regardless of \(k\). Moreover the transfer strictly raises expected observed richness at every \(2\le m\le7k\).

This is a finding about **sampling uncertainty**, not the already known formulas for mean or variance of rarefied richness.

## Assumptions and scope

An abundance profile is an unordered multiset of strictly positive integers, so species labels and the ordering of counts do not create distinct cases. A sample is a uniformly chosen \(m\)-element subset of the \(N\) distinguishable individuals: sampling is without replacement and every individual has equal inclusion probability. A transfer preserves the population census and the number of extant species and satisfies \(x-y\ge2\) before transfer. Variance is the population variance over all \(\binom Nm\) equiprobable samples. Zeros in a sign sequence do not count as reversals; the endpoints \(m=1,N\) have zero variance in every profile with fixed \(s\). For \(N\le7\), the conclusion concerns **every** positive-integer partition of \(N\) and every permissible one-unit transfer, not just three-species communities. The all-size family concerns the specified three-species abundance vectors and the three stated sample sizes; it does not claim to classify every larger transfer.

## Proof

**Exact hypergeometric second moment.** Write \(D=\binom Nm\), and for each species \(i\) write \(q_i=\binom{N-a_i}m\). For a pair \(i<j\), put \(r_{ij}=\binom{N-a_i-a_j}m\). Binomial coefficients are zero outside their natural domain. If \(J_i\) indicates that species \(i\) is *absent*, then \(K_m=s-\sum_i J_i\), and
\[
\mathbb E J_i=q_i/D,\qquad \mathbb E(J_iJ_j)=r_{ij}/D.
\]
Consequently the following integer identity is exact:
\[
D^2\operatorname{Var}(K_m(a))=
\sum_i q_i(D-q_i)+2\sum_{i<j}(D r_{ij}-q_iq_j)=:W_m(a).
\tag{1}
\]
The formula is included for derivation and checking, not asserted as a new rarefaction-variance formula: hypergeometric moment formulas have a long prior literature.

**Sharp census through eight individuals.** Enumerate partitions recursively in nonincreasing order: from a current remainder \(r\) and upper bound \(h\), choose the next part in \(\{1,\ldots,\min(r,h)\}\), then recurse on the remainder with the chosen part as bound. This lists every positive-integer partition exactly once. For each profile examine each pair of parts with difference at least two; transfer one unit and sort the resulting profile. Deduplicate the same target profile arising from different equal-sized species. Compute the integers \(W_m(b)-W_m(a)\) for every \(1\le m<N\) using (1); the denominator \(D^2\) is common and positive. Count sign changes after discarding zeros. The exhaustive certificate, implemented in the attached `verify_rarefaction.py`, gives:

| Total individuals | Unordered profiles | Distinct permitted transfers | Transfers with two or more reversals |
|---:|---:|---:|---:|
| 2 | 2 | 0 | 0 |
| 3 | 3 | 0 | 0 |
| 4 | 5 | 1 | 0 |
| 5 | 7 | 2 | 0 |
| 6 | 11 | 5 | 0 |
| 7 | 15 | 9 | 0 |
| 8 | 22 | 17 | 1 |

The sole eight-individual profile pair is the displayed witness. For that pair, the attached checker independently enumerates every sample subset at each \(m=1,\ldots,7\); the direct first and second moments reproduce (1) and all seven signed differences. Thus the minimum and uniqueness at the first occurrence are **exhaustive finite results**, not inferences from sampling or from an incomplete search. The concise verifier is part of the proof certificate and uses exact integer arithmetic. A second standalone implementation, `bruteforce_census.py`, redoes **the full finite census through eight individuals** without the moment identity, by enumerating the actual samples for every candidate profile and sample size. It reproduces all transfer counts and the unique double-reversal pair.

**All-size rational-polynomial sign certificates.** Put \(t=k-1\ge0\) and write \(D_m(k)=\binom{8k}m\). Define the integer-valued polynomial
\[
P_m(t)=D_m(t+1)^2\bigl(\operatorname{Var}(K_m(B_{t+1}))-\operatorname{Var}(K_m(A_{t+1}))\bigr).
\]
By (1), \(P_m\) is obtained by substituting \(N=8(t+1)\) and the two stated profiles into binomial-polynomial products. The exact expansions (coefficients ordered by increasing powers of \(t\)) are:
\[
P_2(t)=-\sum_{j=0}^3(11,40,42,12)_j t^j,
\]
\[
P_3(t)=\frac13\sum_{j=0}^5(219,1544,4358,6180,4408,1264)_j t^j,
\]
and
\[
P_7(t)=-\frac1{907200}\sum_{j=0}^{13}c_jt^j,
\]
where the positive integer coefficient vector is
\[
(c_0,\ldots,c_{13})=(6350400,184165920,2384168724,18228554940,91792468529,321351269036,804021318232,1453406108560,1892608259997,1744131131028,1094924372494,435143104900,94129956824,7421653616).
\]
Each coefficient has the indicated strict sign. Since \(t\ge0\) and \(D_m(k)>0\), the three variance inequalities hold for every integer \(k\ge1\). The attached checker reconstructs these coefficients by exact rational polynomial multiplication, tests their signs, and additionally evaluates them against independently computed integer binomial moments at \(k=1,2,3,10,100,1000\). It does not extrapolate the all-size claim from those sample values: the **full symbolic coefficients** certify it.

**Expected-richness direction.** For any permitted transfer \(x\to x-1\), \(y\to y+1\), the identity \(\mathbb E K_m=\sum_i(1-q_i/D)\) and Pascal's identity give
\[
\mathbb E K_m(b)-\mathbb E K_m(a)
=\frac{\binom{N-y-1}{m-1}-\binom{N-x}{m-1}}{\binom Nm}.
\tag{2}
\]
For \(A_k\to B_k\), take \(x=3k\), \(y=k\), \(N=8k\); since \(7k-1>5k\), the numerator is strictly positive for every \(2\le m\le7k\). This shows that the uncertainty reversal happens despite the standard monotone improvement in expected richness under balancing.

## Verification

Run `python3 verify_rarefaction.py` with a standard Python 3 interpreter. No third-party packages or network access are needed. The script performs a complete integer-partition enumeration through \(N=8\), checks every possible one-unit balancing transfer, and compares the hypergeometric formula with explicit uniformly weighted subsets of the eight-individual witness. The alternate `bruteforce_census.py` instead uses uniformly weighted sample combinations for the entire finite census; it agrees. The first program then expands \(P_2,P_3,P_7\) in exact \(\mathbb Q[t]\), asserts coefficient signs, and checks the symbolic/numeric identity at six integer values of \(k\). Actual execution completed with `ALL CERTIFICATES PASS`. The finite census proves only the stated lower bound and first-occurrence uniqueness; the explicitly signed polynomial coefficient certificates prove the infinite family. Neither task depends on a random seed, floating point, or a timeout-based exclusion.

## Relationship to prior work

Classical individual-based rarefaction uses hypergeometric sampling and already supplies expected-richness and variance formulas (Hurlbert 1971; Heck, van Belle and Simberloff 1975). Gotelli and Colwell (2001) discuss crossings of **mean** rarefaction curves across communities. Nipperess and Matsen (2012) derive more general phylogenetic-diversity rarefaction moments; for a star-tree specialization the underlying richness-variance formula is covered. Shimadzu (2018) analyzes distinctions between size- and coverage-based richness comparisons. None of the **inspected material** gives this sharp first two-variance-reversal threshold for a *single Robin Hood transfer*, the unique eight-individual witness, or the persistent explicit all-size coefficient certificates. The contribution concerns those comparisons, not rediscovery of hypergeometric moment formulas. Different abundance profiles may have expected-richness crossings in the prior literature, but formula (2) precludes such crossings in the present one-transfer family. Bibliographic coverage is not a proof of global novelty.

## Limitations

Only finite fixed-census rarefaction without replacement is modeled; sampling with replacement, detection biases, species dependencies and uncertainty in the underlying abundance counts are outside scope. The minimal-threshold uniqueness assertion is specific to one-unit balancing transfers, not arbitrary profile changes. The infinite-family theorem forces two reversals at the *specified* sample sizes but does not classify all sign changes for every large \(k\). The 1975 foundational variance paper was identifiable via bibliographic abstract but its publisher full text was unavailable for complete inspection, and related works outside the accessible literature could use different terminology for an equivalent sign phenomenon. No independent audit or empirical ecological validation is claimed.

## References

- Hurlbert, S. H. (1971), *The nonconcept of species diversity: a critique and alternative parameters*, Ecology 52(4), 577–586. DOI: 10.2307/1934145.
- Heck, K. L. Jr., van Belle, G., and Simberloff, D. (1975), *Explicit calculation of the rarefaction diversity measurement and the determination of sufficient sample size*, Ecology 56(6), 1459–1461. DOI: 10.2307/1934716.
- Gotelli, N. J., and Colwell, R. K. (2001), *Quantifying biodiversity: procedures and pitfalls in the measurement and comparison of species richness*, Ecology Letters 4, 379–391. DOI: 10.1046/j.1461-0248.2001.00230.x. Author-hosted full text: https://www.robertkcolwell.org/publications/7086.pdf.
- Nipperess, D. A., and Matsen, F. A. (2012), *The mean and variance of phylogenetic diversity under rarefaction*, arXiv:1208.6552, original preprint posted August 2012. https://arxiv.org/abs/1208.6552.
- Shimadzu, H. (2018), *On species richness and rarefaction: size- and coverage-based techniques quantify different characteristics of richness change in biodiversity*, Journal of Mathematical Biology. DOI: 10.1007/s00285-018-1255-5.
