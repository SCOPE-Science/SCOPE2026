# Sharp first-surplus approximation ratio for the Product-Gap facility mechanism

## Finding

For every integer \(k\ge 2\), the Product-Gap mechanism with \(k\) facilities and exactly \(k+1\) agents on the real line has sharp worst-case expected-social-cost approximation ratio
\[
\sup_{\operatorname{OPT}_k>0}
\frac{\mathbb E[\operatorname{SC}(\operatorname{PG}_k)]}{\operatorname{OPT}_k}
=k-\frac12.
\]
The supremum is not attained by a positive-optimum profile. This is the exact first-surplus specialization of the mechanism introduced in Jia [1] and independently in Chan--Lin--Wang [2]; those works establish the unrestricted ratio \(2k\). The statement is solely a performance guarantee for that specified mechanism, not an optimality theorem over all mechanisms or a claim of strategyproofness for \(k\ge4\).

## Assumptions and scope

The \(k+1\) agents report locations \(x_1\le\dots\le x_{k+1}\) on the real line. A facility arrangement is a multiset of \(k\) freely located real points; an agent's cost is her distance to the nearest facility, and social cost is the sum of individual costs. The social optimum \(\operatorname{OPT}_k\) minimizes this sum over all such arrangements. Product-Gap selects a \(k\)-element subset of agents with probability proportional to the product of the \(k-1\) gaps between their selected, ordered locations, then locates facilities there [1, Definition 3.1; 2, Section 5]. If at most \(k\) distinct occupied positions occur, the mechanism covers them and both social costs are zero. Accordingly a positive denominator requires strictly ordered \(x_1<\cdots<x_{k+1}\). Write \(g_j=x_{j+1}-x_j>0\) for \(1\le j\le k\), and let \(m=\min_j g_j\).

## Proof

**Step 1: The optimum.** Since there are \(k+1\) distinct occupied positions and only \(k\) facilities, two agents have the same nearest facility. By the triangle inequality their combined costs are at least the distance between their positions, which is at least \(m\). Conversely one facility at an endpoint of a closest adjacent pair and one facility at each other agent position gives social cost \(m\). Thus \(\operatorname{OPT}_k=m\). This argument does not assume facilities must be located at reports.

**Step 2: An exact omission law.** Every selection omits exactly one report. Set
\[
P=\prod_{j=1}^{k}g_j,\qquad S=\sum_{j=1}^{k}\frac1{g_j}.
\]
The unnormalized selection weights when omitting report \(i\) are
\[
 w_1=\frac P{g_1},\quad
 w_{k+1}=\frac P{g_k},\quad
 w_i=P\left(\frac1{g_{i-1}}+\frac1{g_i}\right)
 \quad(2\le i\le k).
\]
For an interior omission, the new gap between retained neighbors is \(g_{i-1}+g_i\), giving exactly the displayed formula. Every reciprocal gap occurs twice in the sum of these weights, so the normalization is \(Z=2PS>0\). All retained agents incur zero cost, while the omitted agent incurs \(g_1\) at the left endpoint, \(g_k\) at the right endpoint, and \(\min(g_{i-1},g_i)\) at an interior position. Therefore
\[
 \mathbb E[\operatorname{SC}(\operatorname{PG}_k)]
 =\frac{k+1+\displaystyle\sum_{j=1}^{k-1}
 \frac{\min(g_j,g_{j+1})}{\max(g_j,g_{j+1})}}
 {2\displaystyle\sum_{j=1}^k1/g_j}.
 \tag{1}
\]
This identity is valid for every positive real gap vector, not just integer or experimentally tested vectors.

**Step 3: The universal upper bound.** Choose an index \(t\) such that \(g_t=m\), and set \(h_j=m/g_j\) and \(A=\sum_{j\ne t}h_j>0\). In equation (1), write \(\rho_j=\min(g_j,g_{j+1})/\max(g_j,g_{j+1})\). Each \(\rho_j\le1\); if \(j=t-1\), then \(\rho_j=h_{t-1}\), and if \(j=t\), then \(\rho_j=h_{t+1}\), where indices outside \(\{1,\ldots,k\}\) are ignored. Hence the one or two adjacent \(\rho\)-terms sum to at most \(A\), while the number of remaining terms is at most \(k-2\). Consequently
\[
 k+1+\sum_{j=1}^{k-1}\rho_j\le 2k-1+A.
\]
Since \(m\sum_j 1/g_j=1+A\), equation (1) gives
\[
 \frac{\mathbb E[\operatorname{SC}(\operatorname{PG}_k)]}{\operatorname{OPT}_k}
 \le\frac{2k-1+A}{2(1+A)}<\frac{2k-1}{2},
\]
where strictness follows from \(A>0\) and \(k\ge2\).

**Step 4: Sharpness.** For \(0<\varepsilon<1\), choose \(g_1=\varepsilon\) and \(g_2=\cdots=g_k=1\). Equation (1) becomes
\[
 \frac{\mathbb E[\operatorname{SC}(\operatorname{PG}_k)]}{\operatorname{OPT}_k}
 =\frac{2k-1+\varepsilon}{2\bigl(1+(k-1)\varepsilon\bigr)}
 \longrightarrow k-\frac12
 \quad(\varepsilon\downarrow0).
\]
Thus the bound is sharp for every integer \(k\ge2\), although no distinct-position input attains it. The degenerate limit \(\varepsilon=0\) is excluded because then \(\operatorname{OPT}_k=0\), so no positive-cost approximation ratio is defined.

## Verification

The accompanying standard-library checker `verify_gap_product.py` independently computes the \(k+1\) omission probabilities from the defining products of selected spacings, rather than from equation (1). It compares the exact rational expected cost to equation (1), checks the sharp upper bound and the claimed endpoint family, over 3,119 finite strictly ordered profiles: every \(k\)-gap tuple from \(\{1,2,3\}^k\) for \(2\le k\le6\), 200 reproducible rational gap tuples for each \(2\le k\le11\), and 30 members of the sharpness family. This is a finite consistency check, not an exhaustive proof over real inputs; Steps 1--4 establish the theorem for all real configurations.

To replay: `python3 verify_gap_product.py` from the extracted package directory.

## Relationship to prior work

Jia [1, Definition 3.1 and Section 4] introduces Product-Gap and proves a tight \(2k\) guarantee across unrestricted population sizes, using a cut decomposition and many-agent sharpness example. Chan, Lin and Wang [2, Section 5 and Lemma 5] independently define the same rule and establish the same unrestricted worst-case factor. Neither inspected approximation proof gives the exact first-surplus value \(k-1/2\); their many-agent sharpness profiles have population greater than \(k+1\). Both works discuss other mechanisms or bounds for the \(k=n-1\) setting, without identifying the present precise worst-case performance of Product-Gap on exactly \(k+1\) reports. The new proof supplies the omission law (1) and the sharp first-surplus bound.

## Limitations

The domain is the real line, exactly \(k+1\) agents, social cost under truthful reported positions, and the specified Product-Gap rule. For \(k\ge4\), existing work shows the rule is not strategyproof in general; no contrary incentive assertion is made. The tight upper bound is a nonattained supremum over distinct locations, not the behavior of zero-optimum profiles or an improvement of the known unrestricted \(2k\) factor. No assertion is made for more than \(k+1\) agents, higher dimensions, arbitrary metrics, or uniqueness of the approximation-optimal mechanism. An equivalent unindexed prior specialization cannot be ruled out by a finite literature search.

## References

[1] J. Jia, *Product Gap Mechanisms for Multi-Facility Location*, arXiv:2608.19633v1 (first public 2026-08-20), https://arxiv.org/abs/2608.19633 . See Definition 3.1, Section 4 and Theorem 3.

[2] H. Chan, J. Lin and C. Wang, *Randomized Strategyproof Facility Location: Two Facilities and Beyond*, arXiv:2608.22484 (first public 2026-08-23; current version inspected), https://arxiv.org/abs/2608.22484 . See Section 5, Lemma 5 and the unrestricted tightness construction.
