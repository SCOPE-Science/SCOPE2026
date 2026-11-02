# Sharp three-to-four-alternative boundary for input-only pairwise proportional ranking compression

## Finding

**Theorem (quota-preserving subsampling and the first obstruction).** Let \(m,n\ge 1\) and \(1\le k\le n\). Given \(n\) voters' strict complete rankings of the same \(m\) alternatives, choose \(k\) *distinct voters* without modifying their rankings. Write \(N_{ab}\) for the number of all voters ranking \(a\) above \(b\), and \(S_{ab}\) for the corresponding count among the chosen voters.

1. If \(m\le 3\), for every profile and every \(k\), there is a choice of the \(k\) voters such that **simultaneously for every ordered pair** of distinct alternatives,
   \[
   \left\lfloor\frac{kN_{ab}}n\right\rfloor
   \le S_{ab}\le
   \left\lceil\frac{kN_{ab}}n\right\rceil.
   \]
   In particular, their rankings meet the pairwise proportionality axiom of Halpern, Liu, Micha, Ng, and Suksompong; no synthesized or repeated voter is necessary.
2. The alternative bound is sharp. With four alternatives and \((n,k)=(4,2)\), some profiles have **no** pairwise-proportional selection of two input voters. Among the \(\binom{27}{4}=17{,}550\) multisets of four rankings on four *labeled alternatives* (voters unlabeled), precisely \(690\) are obstructions. All obstructions have four distinct rankings and form exactly \(30\) equivalence classes under alternative relabeling: \(28\) classes of size \(24\), one of size \(12\), and one of size \(6\). Under four independent uniform strict rankings the exact obstruction probability is \(115/2304\).

The qualifier **input-only** is essential in the second part. The four-alternative witness below *does* admit pairwise-proportional synthetic output rankings, as may be permitted by the unrestricted ranking-compression model.

## Assumptions and scope

Every voter supplies a strict linear order, with no missing alternatives or ties. Voters may share the same ranking but are distinct individuals; the output is a subset of size \(k\) of these individuals. The axiom requires for every ordered \((a,b)\) and integer \(1\le t\le k\) that \(N_{ab}\ge tn/k\) implies \(S_{ab}\ge t\). Applying this to both orientations gives precisely the floor/ceiling quotas displayed above. Candidate relabeling does not permute voter identities in the stated anonymous-profile census. There are no single-peakedness, single-crossing, or probabilistic restrictions.

## Proof

**Three alternatives.** Label them \(A,B,C\). Aggregate the input into a multiplicity vector \(c\in\mathbb Z_{\ge0}^{6}\), indexed in the order \(ABC,ACB,BAC,BCA,CAB,CBA\). The comparison-incidence matrix, with the first row counting the number selected and the other rows counting \(A\succ B\), \(B\succ C\), and \(A\succ C\), is
\[
M=\begin{pmatrix}
1&1&1&1&1&1\\
1&1&0&0&1&0\\
1&0&1&1&0&0\\
1&1&1&0&0&0
\end{pmatrix}.
\]

This matrix is **totally unimodular**. Here is a complete Ghouila-Houri row-signing certificate. Label its rows \(0,1,2,3\). For each nonempty subset of rows, the displayed signed combination has every one of its six entries in \(\{-1,0,1\}\):

| Row subset | Signing |
|---|---|
| \(\{0\},\{1\},\{2\},\{3\}\) | \(r_0,r_1,r_2,r_3\), respectively |
| \(\{0,1\},\{0,2\},\{0,3\}\) | \(r_0-r_1,\ r_0-r_2,\ r_0-r_3\) |
| \(\{1,2\},\{1,3\},\{2,3\}\) | \(r_1-r_2,\ r_1-r_3,\ r_2-r_3\) |
| \(\{0,1,2\}\) | \(r_0-r_1-r_2\) |
| \(\{0,1,3\}\) | \(r_0-r_1-r_3\) |
| \(\{0,2,3\}\) | \(r_0-r_2-r_3\) |
| \(\{1,2,3\}\) | \(r_1+r_2-r_3\) |
| \(\{0,1,2,3\}\) | \(r_0-r_1-r_2+r_3\) |

The Ghouila-Houri criterion therefore gives total unimodularity. The accompanying checker independently computes **all 209 nonempty square minors**, each in \(\{-1,0,1\}\), and checks all 15 row subsets.

Consider the bounded polytope
\[
P=\left\{z\in\mathbb R^{6}:0\le z\le c,\quad
\left\lfloor\frac{k}{n}Mc\right\rfloor\le Mz\le
\left\lceil\frac{k}{n}Mc\right\rceil\right\},
\]
where floors and ceilings are componentwise. It contains the fractional point \(z=(k/n)c\). Its constraint matrix is obtained from \(M\) by sign reversal of rows and adjoining unit rows, and so remains totally unimodular. All right-hand sides are integers. The standard integrality theorem for bounded polyhedra with totally unimodular constraints therefore gives an integral point \(z\in P\). Its first matrix-coordinate is exactly \(k\), so \(\sum_j z_j=k\), and \(0\le z_j\le c_j\) lets us choose distinct input voters with those six ranking multiplicities. The remaining coordinates impose the quotas for three unordered alternative pairs; their complementary orientations automatically inherit their floor/ceiling quotas. The cases \(m=1,2\) follow directly by restricting any three-alternative construction or by one comparison. A polynomial-time algorithm follows from solving the fixed-dimension integral linear system, or directly by enumerating at most \((n+1)^5\) count vectors.

**Four-alternative witness.** Take these four input ballots, top to bottom:
\[
\begin{array}{c|c}
1&A\succ B\succ C\succ D\\
2&A\succ C\succ D\succ B\\
3&C\succ A\succ B\succ D\\
4&D\succ B\succ C\succ A
\end{array}.
\]
The comparisons \(A\) versus \(C\), \(B\) versus \(C\), and \(B\) versus \(D\) each split exactly \(2:2\), so any two-voter representative set must contain one vote favoring each orientation on each of these three comparisons. Yet all six pairs of input voters fail as follows:

| Selected voters | Balanced comparison on which they agree |
|---|---|
| \(\{1,2\}\) | \(A\succ C\) |
| \(\{1,3\}\) | \(B\succ D\) |
| \(\{1,4\}\) | \(B\succ C\) |
| \(\{2,3\}\) | \(C\succ B\) |
| \(\{2,4\}\) | \(D\succ B\) |
| \(\{3,4\}\) | \(C\succ A\) |

Hence no input-only pair works (not even allowing a repeated copy of one ballot). Synthetic ballots \(A\succ B\succ C\succ D\) and \(C\succ A\succ D\succ B\), by contrast, satisfy all six comparisons' quotas for this profile. This distinction prevents confusing the result with a failure of unrestricted pairwise proportionality.

**Exact first-obstruction census.** For \(n=4,k=2\), selecting two *distinct input voters* automatically respects all comparisons with support \(0,1,3,4\): a \(3:1\) preference is present in at least one of the two voters, while a \(4:0\) preference is unanimous. Only \(2:2\) comparisons constrain selection: the two voters must disagree on every such comparison. If any input ranking occurs twice, either remaining distinct voter has the opposite orientation on every \(2:2\) comparison, so one copy of the repeated ranking paired with that voter is admissible. Consequently every failure consists of four distinct orders.

There are exactly \(\binom{24}{4}=10{,}626\) sets of four distinct orders on four labeled alternatives. Enumerating all of these, forming the set of tied comparisons for each, and checking the six input pairs produces exactly \(690\) failures. A second enumeration independently checks the literal floor/ceiling quotas on all \(\binom{27}{4}=17{,}550\) ranking multisets, obtaining \(690\) failures, all distinct. Canonicalizing each failure under all \(24\) alternative relabelings yields the \(30\)-class distribution stated above. Each of the \(690\) distinct-ballot multisets has \(4!\) ordered voter presentations among the \(24^4\) equally likely labeled profiles, giving \(690\cdot24/24^4=115/2304\). Every finite operation and its independent check are implemented in the accompanying Python file.

## Verification

From the same directory run `python3 ranking_quota_verifier.py` (Python 3 standard library only). The reproduced results are: 209 total-unimodularity minor checks and 15 independent row-sign tests; 5,004 anonymous input profiles and 38,610 profile/committee-size checks for three alternatives through nine voters; 690 obstructions among 17,550 four-alternative multisets from direct quota testing; 690 from the structurally independent tied-pair test; 30 alternative-relabeling classes with orbit sizes \(28\times24,12,6\); and the six explicitly named witness failures. The proof for arbitrary \(n,k\) is the integral-polyhedron argument, **not** an extrapolation from the finite tests. The finite census is exhaustive because it iterates each member of the explicitly specified finite domain.

## Relationship to prior work

Halpern, Liu, Micha, Ng, and Suksompong (2026) define pairwise proportionality and establish unrestricted impossibility for large candidate sets (Theorem 3), while their Proposition 1 shows that requiring input rankings can defeat several axioms using a six-alternative construction. Their positive theorems for single-peaked and single-crossing input apply to structured profiles, not arbitrary profiles of three alternatives; their unrestricted small-instance search through seven alternatives is also a different requirement. The present theorem identifies the **sharp input-only candidate boundary**, guarantees *selection without replacement* while preserving every exact floor/ceiling pairwise quota for three alternatives, and enumerates the first failure layer. Restricting the earlier six-alternative Proposition 1 example to any four alternatives does not produce a pairwise-proportionality failure, so this specific four-alternative witness is not obtained by that direct restriction.

Procaccia, Schiffer, Wang, and Zhang (2025) study subset selection with positional representation and approximate positional proportionality, rather than exact simultaneous quotas on pairwise comparisons. Ghouila-Houri's criterion and integral-polyhedron theory are established ingredients, not newly claimed mathematical facts.

## Limitations

The universal positive theorem is specific to at most three alternatives and to strict complete rankings. The negative example uses input-only selection; it does not prove that four alternatives defeat arbitrary synthetic output rankings. The reported exact census is only for four input voters compressed to two; no enumeration of other electorate sizes is asserted. Novelty relative to unindexed balanced-selection and discrepancy literature cannot be proved by a finite search.

## References

- Daniel Halpern, Xinyu Liu, Evi Micha, Yu Peng Ng, and Warut Suksompong. *Proportionality in Ranking Compression*. arXiv:2610.23193v1 (first posted 2026-10-16). https://arxiv.org/html/2610.23193
- Ariel D. Procaccia, Benjamin Schiffer, Serena Wang, and Shirley Zhang. *Metritocracy: Representative Metrics for Lite Benchmarks*. NeurIPS 2025. https://papers.nips.cc/paper_files/paper/2025/hash/01d64478381c33e29ed611f1719f5a37-Abstract-Conference.html
- A. Ghouila-Houri. *Caractérisation des matrices totalement unimodulaires*. C. R. Acad. Sci. Paris 254 (1962), 1192–1194. See bibliographic reference in https://doi.org/10.1002/net.3230060406
