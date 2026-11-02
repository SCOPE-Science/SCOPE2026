# The four-site Markov screening law: four optimal pooling regimes and an alternating-pair phase

## Finding

**Theorem.** For four consecutively indexed screening specimens with stationary binary Markov infection status and a perfect two-stage Dorfman test, define the positive-status prevalence \(p\in(0,1)\), one-step infection-status correlation \(\rho\), \(u=1-p\), \(a=u+p\rho\), and \(b=u+p\rho^2\). Assume
\[
-\min\left\{\frac{p}{1-p},\frac{1-p}{p}\right\}<\rho<1.
\]
The minimum expected number of tests across **every set partition** of the four specimens is exactly
\[
\min\left\{5-4ua^3,\quad 5-3uA_3,\quad 6-4uA_2,\quad4\right\},
\]
where
\[
A_3=\begin{cases}a^2,&\rho\geq0,\\ab,&\rho<0,\end{cases}
\qquad
A_2=\begin{cases}a,&\rho\geq0,\\b,&\rho<0.\end{cases}
\]
These four candidate values are respectively attained by one four-person pool, an optimized triple plus a singleton, two optimized pairs, and four individual tests. For strictly positive correlation the two-pair option is **never** globally optimal. For strictly negative correlation each of the four structures is uniquely optimal *as a pool-size structure* on a nonempty open set of feasible parameters. In the negative-correlation two-pair regime the optimal pools are exactly \(\{1,3\}\) and \(\{2,4\}\), even though these are noncontiguous. For a triple, the optimal negative-correlation choices are \(\{1,2,4\}\) or \(\{1,3,4\}\), rather than either contiguous triple. For zero correlation placements of a fixed size are tied.

More generally, for \(h\geq2\) specimens selected from a stationary chain of \(n\geq 2h-1\) sites with strictly feasible \(\rho\), the highest all-negative probability among size-\(h\) subsets is attained exactly by consecutive sites when \(\rho>0\), and by subsets with every consecutive selected-index gap equal to two when \(\rho<0\). This is a single-pool structure theorem, not an assertion that parity pools always form the globally best multi-pool partition for larger \(n\).

## Assumptions and scope

Let \(X_i=1\) indicate disease-positive specimen \(i\), for \(i=1,2,3,4\). The joint law is a stationary first-order two-state Markov chain with \(\Pr(X_i=1)=p\) and \(\mathrm{Corr}(X_i,X_{i+1})=\rho\). Its transition matrix, with states in the order zero, one, is
\[
M=\begin{pmatrix}u+p\rho&p(1-\rho)\\u(1-\rho)&p+u\rho\end{pmatrix}.
\]
The strict range in the theorem ensures nonnegative (indeed strictly positive) transition entries and \(|\rho|<1\). A pool test detects at least one positive specimen without false positives, false negatives, dilution, or additional pooling constraints. Every specimen must be resolved. A singleton receives one individual test. For each larger pool, test the pool once, and retest *all* its members individually if and only if it tests positive. The objective is the expected total number of tests, without extra weighting of laboratory time or assay cost. All set partitions, including noncontiguous groupings, are allowed.

## Proof

**1. Exact all-negative law.** Since the nonconstant eigenvalue of \(M\) is \(\rho\), the \(d\)-step conditional probability \(\Pr(X_{i+d}=0\mid X_i=0)\) is \(u+p\rho^d\). Therefore for any nonempty selected index set \(H=\{i_1<\cdots<i_h\}\),
\[
q(H):=\Pr(X_i=0\text{ for all }i\in H)
=u\prod_{j=1}^{h-1}\bigl(u+p\rho^{i_{j+1}-i_j}\bigr).
\]
By conditioning on the pool outcome, the number of tests assigned to a nonsingleton \(H\) has expectation \(1+|H|(1-q(H))\); for a singleton it is \(1\). The sum of those expectations over a partition is the objective.

**2. Exact best geometry within each pool structure.** Put \(c=u+p\rho^3\). For \(0<\rho<1\), \(a>b>c>0\); for negative feasible \(\rho\), \(b>c>a>0\). All four pooled give \(q(\{1,2,3,4\})=ua^3\), hence expected cost \(5-4ua^3\). For a three-person pool, the possible gap patterns are \((1,1)\) and \((1,2)\) or \((2,1)\). Their probabilities are \(ua^2\) and \(uab\); thus the optimized triple cost is \(5-3uA_3\), with the claimed choices.

For two pairs, the only pairings are \(12|34\), \(13|24\), and \(14|23\). The sum of their two all-negative probabilities is respectively \(2ua\), \(2ub\), and \(u(a+c)\). If \(\rho>0\), \(a>b\) and \(a>c\), making \(12|34\) best. If \(\rho<0\), \(b>a\) and
\[
2b-a-c=-p\rho(1-\rho)^2>0,
\]
so the unique best pairing is \(13|24\). The best cost of two pairs is consequently \(6-4uA_2\).

For a structure of one pair and two singletons the minimum cost is \(5-2uA_2\). Set \(z=uA_2\). If \(z\leq1/2\), this is at least four individual tests; if \(z\geq1/2\), the optimized two-pair cost \(6-4z\) is no higher. Hence no \(2+1+1\) partition lowers the displayed four-way minimum. These are all five integer partitions of four and all their corresponding set partitions; thus the minimum formula holds globally, including ties and boundary comparisons.

**3. Positive correlation forbids a globally optimal two-pair partition.** Suppose \(\rho\geq0\), and write \(z=ua\). We have \(a\geq u\), hence \(z\leq a^2\). If \(z<1/2\), the two-pair cost \(6-4z\) is strictly greater than the four-singleton cost. If \(z>1/2\), then \(a^2>1/2\) and
\[
(5-4ua^3)-(6-4ua)=-1+4z(1-a^2)
\leq-1+4a^2(1-a^2)<0,
\]
so the four-person pool is strictly cheaper. Finally if \(z=1/2\), then \(a^2\geq1/2\). For \(a^2>1/2\), the four-person pool costs \(5-2a^2<4\), whereas the two-pair cost is four. When \(a^2=1/2\), we must have \(a=u=1/\sqrt2\), thus \(\rho=0\), and the three-plus-one cost is \(5-3/(2\sqrt2)<4\). In every case, two pairs are strictly dominated by an available alternative.

**4. Every negative-correlation structure really wins.** The following rational choices are strictly feasible; the indicated candidate is strictly below the other three:

| Optimal structure | \(p\) | \(\rho\) | Exact minimum | Positive margin to next-best structure |
|---|---:|---:|---:|---:|
| One four-person pool | \(1/10\) | \(-1/10\) | \(6155279/2500000\) | \(735721/2500000\) |
| Three plus one (gapped triple) | \(2/7\) | \(-1/10\) | \(33839/8575\) | \(41/8575\) |
| Two alternating pairs | \(1/4\) | \(-1/4\) | \(237/64\) | \(461/4096\) |
| Four singletons | \(1/2\) | \(-1/2\) | \(4\) | \(3/4\) |

These are strict rational inequalities in continuous functions of \(p,\rho\), so each persists on a nonempty feasible open neighborhood. The two gapped triples are tied by reflection, and strict optimality refers to the *integer pool-size structure*, not necessarily a single labeled partition.

**5. General fixed-size single-pool geometry.** In the strict feasible range with \(\rho>0\), each \(\rho^d\) for a positive integer \(d\) is maximized uniquely at \(d=1\). For \(\rho<0\), the sequence \(\rho^d\) has its largest value uniquely at \(d=2\): odd powers are negative and even powers decrease as their exponent increases. Since all factors \(u+p\rho^d\) are strictly positive, the product for a selected size-\(h\) subset is maximized by all gaps being one or two, respectively. The hypothesis \(n\geq2h-1\) makes gap-two subsets possible. This proves the stated exact characterizations.

## Verification

Run `python3 verify_markov_pool.py` with Python and SymPy installed. The checker independently enumerates all \(2^4=16\) binary Markov states to verify the algebraic all-negative law for every nonempty subset, then tests all \(15\) four-item set partitions at \(132\) exact-rational feasible parameter points. It evaluates expected test counts directly from the full distribution, separately from the candidate formula, and checks all four rational witnesses. A completed replay produced **2,223 exact assertions passed**. Finite grid checks are supplementary: Steps 1–5 are the infinite-parameter proof.

## Relationship to prior work

Dorfman's 1943 work introduced two-stage group tests. Hong and Scaglione (2008) analyze one-dimensional Markov binary sources using adaptive sensor data-retrieval queries, explicitly restricting their proposed recursive and binary-tree algorithms to contiguous groups. Lendle, Hudgens, and Qaqish (first publicly available as a technical report in 2010; online journal release September 27, 2011) derive test-efficiency formulas under exchangeable-cluster assumptions. Landolfi and Lall (first publicly available August 21, 2023) optimize Dorfman partitions for globally exchangeable specimen statuses, in which placement of same-size pools has no meaning. None of these inspected results states the exhaustive stationary four-site, possibly negatively correlated, noncontiguous-pooling classification proved here. The general expected-testing cost functional is classical, not claimed as new.

## Limitations

This is a mathematical decision benchmark for spatially indexed screening, not a model fitted to a real transmission mechanism. Negative infection-status autocorrelation may be inappropriate for some contagious diseases; the result identifies what such dependence *would* imply under the assumptions. Imperfect sensitivity, dilution, sample-processing time, pooled-test costs varying with size, and restrictions on which specimens can be mixed may change the optimum. The general single-pool gap law does not imply a full optimal partition classification for an arbitrary number of sites. Historical equivalences under alternative group-testing notation remain possible; originality has not been independently certified.

## References

1. R. Dorfman, *The Detection of Defective Members of Large Populations*, Annals of Mathematical Statistics **14** (1943), 436–440. DOI: https://doi.org/10.1214/aoms/1177731363 .
2. Y.-W. P. Hong and A. Scaglione, *Group Testing for Binary Markov Sources: Data-Driven Group Queries for Cooperative Sensor Networks*, IEEE Transactions on Information Theory **54** (2008), 3538–3551. DOI: https://doi.org/10.1109/TIT.2008.926363 .
3. S. D. Lendle, M. G. Hudgens, and B. F. Qaqish, *Group Testing for Case Identification with Correlated Responses*, Biometrics **68** (2012), 532–540, online September 27, 2011. https://pmc.ncbi.nlm.nih.gov/articles/PMC3384753/ .
4. N. C. Landolfi and S. Lall, *Optimal Dorfman Group Testing for Symmetric Distributions*, arXiv:2308.11050 (2023); SIAM Journal on Mathematics of Data Science **6** (2024), 731–760. https://arxiv.org/abs/2308.11050 .
