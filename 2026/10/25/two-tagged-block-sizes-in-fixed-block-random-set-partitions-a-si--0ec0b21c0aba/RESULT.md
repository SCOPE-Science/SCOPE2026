# Two tagged block sizes in fixed-block random set partitions: a six-element covariance crossover

## Finding

Let \(\Pi_{n,k}\) be a uniformly chosen partition of \([n]\) into exactly \(k\) nonempty blocks. Let \(X\) and \(Y\) be the cardinalities of the blocks containing labels \(1\) and \(2\), respectively. Write \(S(n,k)\) for a Stirling number of the second kind, with \(S(0,0)=1\) and zero outside its natural range, and put
\[
 a_{n,k}=\frac{S(n-1,k)}{S(n,k)},\qquad b_{n,k}=\frac{S(n-2,k)}{S(n,k)}.
\]
For all integers \(n\ge 2\) and \(1\le k\le n\), the complete covariance is
\[
 \operatorname{Cov}(X,Y)=a_{n,k}+n(n-2)b_{n,k}-(n-1)^2a_{n,k}^2. \tag{1}
\]
For two blocks and \(n\ge3\), this specializes to
\[
 \operatorname{Cov}(X,Y\mid k=2)=\frac{2^{n-3}\bigl(2^{n-1}-n(n-2)-2\bigr)}{(2^{n-1}-1)^2}, \tag{2}
\]
which is strictly negative for \(3\le n\le5\) and strictly positive for every \(n\ge6\). In contrast, for exactly one two-element block and all other blocks singleton (\(k=n-1\)),
\[
 \operatorname{Cov}(X,Y\mid k=n-1)=-\frac{2(n-2)}{n^2(n-1)}<0\qquad(n\ge3). \tag{3}
\]
Consequently, for **each** \(n\ge6\), two natural nondegenerate choices of the prescribed block count produce opposite signs of dependence for the same two tagged cluster sizes. For each fixed integer \(k\ge2\),
\[
 \operatorname{Cov}(X,Y)=\frac{k-1}{k^2}+O_k\!\left(n^2(1-1/k)^n\right)\quad\text{as } n\to\infty. \tag{4}
\]
Thus positive covariance is eventually forced at every fixed nontrivial block count, whereas a near-discrete partition has negative covariance. Equations (2)–(4), rather than classical Stirling enumeration alone, describe the crossover phenomenon.

## Assumptions and scope

The random partition is uniformly distributed on the \(S(n,k)\) **unlabeled** partitions; blocks are not weighted by size and there is no conditioning on either tag's block size. The two tags are distinct fixed labels. For \(k=1\) or \(k=n\), the two sizes are deterministic and their covariance vanishes. Both sizes can coincide without the two tags belonging to the same block. The result compares only the displayed block counts: it does **not** assert monotonicity in \(k\) for arbitrary intermediate values.

The full joint count, for given integer sizes \(x,y\) and event \(H\) that the two tags belong to the same block, is
\[
 \begin{aligned}
 S(n,k)\Pr\{X=x,Y=y,H\}&=\mathbf1_{x=y}\binom{n-2}{x-2}S(n-x,k-1),\\
 S(n,k)\Pr\{X=x,Y=y,H^c\}&=\binom{n-2}{x-1}\binom{n-x-1}{y-1}S(n-x-y,k-2).
 \end{aligned} \tag{5}
\]
Each expression is defined to be zero for infeasible sizes, and binomial coefficients are zero when the lower index lies outside \([0,m]\). In the second line \(x,y\ge1\), \(x+y\le n\); the first line requires \(2\le x=y\le n\). These two disjoint cases sum to \(S(n,k)\).

## Proof

**Joint law.** If the tags share a block of size \(x\), select its \(x-2\) other labels from the remaining \(n-2\), and partition the complement into \(k-1\) blocks. If the tags occupy different blocks of sizes \(x,y\), select the first block's \(x-1\) other labels, then the second block's \(y-1\) other labels, then partition the remaining \(n-x-y\) labels into \(k-2\) blocks. This gives equation (5) with no block-ordering overcount, because the two tagged blocks are distinguished by their tags.

**Covariance.** Let \(I_{ij}\) indicate that labels \(i\) and \(j\) share a block. Collapsing a specified pair of labels induces a bijection between partitions in which the pair is together and partitions of \(n-1\) labels into \(k\) blocks. Hence \(\mathbb EI_{ij}=a_{n,k}\). For two distinct pair constraints (even if they share one vertex), collapsing their induced equivalence components decreases the number of labels by two, so their joint expectation is \(b_{n,k}\). Since
\[
 X=1+\sum_{j=2}^n I_{1j},\qquad Y=1+I_{12}+\sum_{j=3}^n I_{2j},
\]
we obtain \(\mathbb EX=\mathbb EY=1+(n-1)a_{n,k}\), and
\[
 \mathbb E(XY)=1+(2n-1)a_{n,k}+n(n-2)b_{n,k}.
\]
Among the \((n-1)^2\) products of pair indicators, exactly one squares the same indicator; this contributes \(a_{n,k}\), with each other product contributing \(b_{n,k}\). Subtracting the product of expectations gives (1).

**The six-element crossover.** For \(k=2\), \(S(n,2)=2^{n-1}-1\). Substituting these elementary Stirling values into (1) and factoring yields (2). Put \(F_n=2^{n-1}-n(n-2)-2\). Direct evaluation gives \(F_3=-1\), \(F_4=-2\), \(F_5=-1\), and \(F_6=6\). The identity
\[
 F_{n+1}-2F_n=(n-1)(n-3)>0\qquad(n\ge4)
\]
proves \(F_n>0\) for every \(n\ge6\), establishing the sharp threshold.

**Near-discrete partitions.** For \(k=n-1\), precisely one unordered pair of labels forms the unique nonsingleton block, uniformly among \(\binom n2\) pairs. Set \(Z_1=X-1\) and \(Z_2=Y-1\). Then \(\mathbb EZ_i=2/n\) and \(\mathbb E(Z_1Z_2)=1/\binom n2=2/[n(n-1)]\), giving equation (3).

**Fixed-block limit.** Allocate \(n\) labeled elements independently to \(k\) labeled boxes with probability \(1/k\) each; forget the box labels and condition on every box being nonempty. Because each unlabeled \(k\)-block partition admits exactly \(k!\) box labelings, this construction gives precisely \(\Pi_{n,k}\). Without conditioning, the two sizes \(U,V\) of the boxes containing tags \(1,2\) have \(\operatorname{Cov}(U,V)=(k-1)/k^2\): the probability that any two labels share a box is \(1/k\), and any two distinct pair-coincidence constraints have joint probability \(1/k^2\). Let \(p=\Pr\{\text{some box is empty}\}\). The union bound gives \(p\le k(1-1/k)^n\). Since \(1\le U,V\le n\), conditioning on all boxes being used changes \(\mathbb E(UV)\) by at most \(n^2p\) and each marginal mean by at most \(np\). The resulting covariance change is at most \(3n^2p\). This proves (4) and eventual positivity.

## Verification

Run `python verify.py` with a standard Python 3 interpreter. The verifier independently generates every restricted-growth-string partition of \([n]\) for \(2\le n\le9\), compares each joint cell in (5), recomputes covariance from raw counts, and tests the exact formulas for \(3\le n<150\). It also checks the fixed-block asymptotic error against a conservative explicit bound. Its recorded output was `PASS: exact independent assertions: 4746`.

This finite check is not a proof for arbitrary \(n,k\); the enumerative bijections, elementary recurrence, and occupancy-conditioning estimate above establish the general conclusions.

## Relationship to prior work

Classical Stirling enumeration and the labeled-box sampling representation are established facts. Pitman (1997) discusses probabilistic constructions for set partitions; Timashev (2003) studies uniform fixed-block partitions, block-size counts, and tagged-block marginal asymptotics. Neither source in the inspected material states the two-tag finite covariance crossover (2)–(3) or the fixed-block covariance limit (4). Pittel (2000) studies the meet/join of independently chosen partitions, a different joint object. Goh and Schmutz (1994) study maximal block sizes and their multiplicities rather than the covariance of the two tagged block sizes. The present claim is the specific sharp conditional dependence comparison, not the known general representation or Stirling formulas.

## Limitations

The study concerns uniform partitions with fixed block number, not exchangeable partitions with general Gibbs or Ewens weights. It does not classify covariance signs at *all* intermediate block counts, derive an asymptotic law when \(k\) grows with \(n\), or imply independence when covariance vanishes. Some older general allocation and set-partition literature remains a priority risk; no independent historical-priority assessment has been conducted.

## References

1. J. Pitman, “Some Probabilistic Aspects of Set Partitions,” *American Mathematical Monthly* **104** (1997), 201–209; DOI: 10.1080/00029890.1997.11990624. Author-hosted full text: https://www.stat.berkeley.edu/~pitman/452.pdf.
2. A. N. Timashev, “Random partitions of a set with given number of blocks,” *Discrete Mathematics and Applications* **13** (2003), 307–317; DOI: 10.1515/156939203322385919. Original-language full text: https://www.mathnet.ru/php/getFT.phtml?jrnid=dm&option_lang=eng&paperid=201&what=fullt.
3. B. Pittel, “Where the Typical Set Partitions Meet and Join,” *Electronic Journal of Combinatorics* **7** (2000), R5; DOI: 10.37236/1483, published 2000-01-15.
4. W. M. Y. Goh and E. Schmutz, “Random Set Partitions,” *SIAM Journal on Discrete Mathematics* **7** (1994), 419–436; DOI: 10.1137/S0895480190186974.
