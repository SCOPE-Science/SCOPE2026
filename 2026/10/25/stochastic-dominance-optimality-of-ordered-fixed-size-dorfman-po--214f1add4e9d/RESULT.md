# Stochastic-dominance optimality of ordered fixed-size Dorfman pools and a variance reversal

## Finding

Consider independent infection indicators for a finite set of people with known, potentially different infection probabilities. In the classical two-stage Dorfman procedure, one test is given to every nonoverlapping pool; after a positive pool test, **every** member of that pool receives an individual retest. Every test is perfect. Fix the common pool size and the number of pools.

**Theorem (distributional ordered-pooling optimum).** Let integers \(m\ge1\), \(k\ge2\), and \(N=mk\) be given. For each person \(i\in\{1,\ldots,N\}\), independently let the infection indicator have probability \(p_i\in[0,1)\). Sort people by increasing \(p_i\) and put consecutive blocks of \(k\) people in pools; call this partition \(\mathcal P_*\). If \(\mathcal P\) is *any* other partition into \(m\) pools of size \(k\), and \(T_{\mathcal P}\) denotes the total number of first-stage and second-stage assays, then, for every real threshold \(t\),

\[
 \Pr\{T_{\mathcal P_*}\ge t\}\le\Pr\{T_{\mathcal P}\ge t\}.
\]

Thus the same ordered partition minimizes every test-count upper tail, each quantile under the usual lower-quantile convention, and the expectation of every increasing test-capacity penalty with finite expectation. Equality of the **entire distributions** occurs precisely when the multisets of negative-pool probabilities \(\{\prod_{i\in G}(1-p_i):G\in\mathcal P\}\) and \(\{\prod_{i\in G}(1-p_i):G\in\mathcal P_*\}\) agree; tied risk values may permit many equivalent partitions. The conclusion extends to \(p_i=1\) by continuity, without asserting this equality characterization at that boundary.

**Variance boundary for paired screening.** Specialize to \(k=2\), write \(a_i=1-p_i\), and suppose at least two pools exist. If all \(p_i\le1/2\), ordered adjacent pairing *minimizes* \(\operatorname{Var}(T)\) among pairings. If all \(p_i\ge1/2\), the same pairing *maximizes* \(\operatorname{Var}(T)\). Opposite-extreme pairing of the smallest with the largest \(a_i\), the next smallest with the next largest, and so on gives the opposite extremum. Strict inequalities hold for strictly ordered nondegenerate risks on the appropriate open side of the half-risk boundary. Hence optimal upper-tail probabilities do not imply optimal variance. The sign boundary is sharp for the pairwise-exchange argument.

## Assumptions and scope

A partition \(\mathcal P=(G_1,\ldots,G_m)\) consists of \(m\) disjoint subsets of equal size \(k\) whose union is \(\{1,\ldots,N\}\). All \(N\) individual infection statuses are mutually independent. Pool \(G\) is negative exactly when every member of \(G\) is uninfected. Tests are perfect, always available, and have equal unit cost. All \(m\) initial tests are counted, and a positive pool contributes exactly \(k\) more tests, even if a later individual assay is positive. No adaptive stopping or inference of an untested last member is permitted. For a pool \(G\) set \(u_G=\prod_{i\in G}(1-p_i)\). Because pools contain disjoint individuals, their positive indicators are independent Bernoulli variables with success probabilities \(1-u_G\). If \(Y_{\mathcal P}\) is the number of positive pools, then \(T_{\mathcal P}=m+kY_{\mathcal P}\) and

\[
 \mathbb E[z^{Y_{\mathcal P}}]=\prod_{G\in\mathcal P}\bigl(u_G+(1-u_G)z\bigr).
\]

The stochastic comparison is only over partitions with the **same** \(m\) and \(k\); it does not optimize the number or size of pools. Its natural application is allocating batches to independent heterogeneous public-health screening subjects when laboratory capacity must accommodate the realized, rather than merely expected, assay count.

## Proof

**1. Logarithmic majorization.** Put \(a_i=1-p_i>0\), and reorder indices so that \(0<a_1\le\cdots\le a_N\). Define \(b_i=\log a_i\) and, for each pool \(G\), let \(x_G=\log u_G=\sum_{i\in G}b_i\). Write \(x(\mathcal P)\) for the vector of the \(m\) pool log-negative-probabilities. For any \(r\in\{1,\ldots,m\}\), the sum of its \(r\) largest coordinates is the sum of \(rk\) *distinct* entries from \((b_i)\), and hence is at most the sum of the globally largest \(rk\) entries. For the ordered-block partition \(\mathcal P_*\), those largest entries occur in its \(r\) largest blocks, giving equality. At \(r=m\) the sums coincide because each person belongs to exactly one pool. Therefore

\[
 x(\mathcal P_*)\ \text{majorizes}\ x(\mathcal P)
\]

for every equal-size partition \(\mathcal P\).

**2. A two-pool stochastic comparison.** Take any two pool log-probabilities \(x\le y\), and apply a spread \(x\mapsto x-\delta\), \(y\mapsto y+\delta\) with \(\delta\ge0\), staying in the physically admissible region \(x-\delta\le y+\delta\le0\). The negative probabilities \(u=e^x\) and \(v=e^y\) satisfy fixed product \(uv=e^{x+y}\), while their sum increases:

\[
 e^{x-\delta}+e^{y+\delta}\ge e^x+e^y.
\]

For the sum \(S\) of the two *positive*-pool indicators, the two nontrivial upper-tail probabilities are

\[
 \Pr(S\ge1)=1-uv,\qquad
 \Pr(S\ge2)=(1-u)(1-v)=1-u-v+uv.
\]

Thus the spread leaves the first probability fixed and weakly decreases the second; in symbols the more-spread pair has a stochastically smaller positive-pool count. It is independent of the other pool indicators, so convolution preserves this stochastic order. More generally, the same conclusion holds along each pairwise equal-sum mean-preserving *compression*, in the reversed direction. The finite transfer characterization of vector majorization connects any vector majorized by \(x(\mathcal P_*)\) to it via finitely many such compressions, with coordinate permutations. All intermediary log-values lie between endpoint log-values and hence remain at most zero; their exponential values are legitimate Bernoulli negative probabilities for the mathematical comparison, even if intermediate configurations need not correspond to an actual allocation. Applying the two-pool comparison at each step yields

\[
 Y_{\mathcal P_*}\le_{\mathrm{st}}Y_{\mathcal P}
\]

for every partition. The affine increasing relation \(T=m+kY\) proves the first assertion. All first-stage counts are fixed; no conclusion is being inferred just from an expected-value inequality.

**3. Whole-law equality criterion.** For every partition, \(\Pr(Y_{\mathcal P}=0)=\prod_Gu_G=\prod_ia_i\) is identical. The expected number of positive pools is \(m-\sum_Ge^{x_G}\). By strict convexity of the exponential and strict Karamata inequality, if the log-pool-probability multisets for \(\mathcal P_*\) and \(\mathcal P\) differ, then \(\sum_G e^{x_G(\mathcal P_*)}>\sum_G e^{x_G(\mathcal P)}\), so their means and entire distributions differ. Conversely, identical group-negative-probability multisets give the same probability-generating polynomial and hence the same entire distribution. If some \(p_i\to1\), both compared discrete probability-generating polynomials vary continuously, proving the asserted boundary extension.

**4. Variance reversal for pairs.** For \(k=2\), independence across pools gives

\[
 \operatorname{Var}(T_{\mathcal P})=4\sum_{\{i,j\}\in\mathcal P}h(a_i,a_j),
 \qquad h(s,t)=st(1-st).
\]

This smooth symmetric pair cost has mixed derivative \(\partial_s\partial_th(s,t)=1-4st\). When all \(a_i\ge1/2\), it is nonpositive throughout the risk domain, and when all \(a_i\le1/2\), it is nonnegative throughout. For four ordered values \(a\le b\le c\le d\), both comparisons of adjacent pairing with either alternative follow by integrating this mixed derivative over nonnegative rectangles:

\[
 h(a,b)+h(c,d)-h(a,c)-h(b,d)
 =\int_b^c\int_a^d(1-4st)\,dt\,ds,
\]
\[
 h(a,b)+h(c,d)-h(a,d)-h(b,c)
 =\int_b^d\int_a^c(1-4st)\,dt\,ds.
\]

The signs show that the adjacent pairing \((a,b),(c,d)\) locally minimizes the sum on the negative-mixed-derivative side, and maximizes it on the positive-mixed-derivative side. Repeated four-point uncrossing yields the respective global optimum over all perfect matchings (and the opposite-extreme pairing yields the opposite optimum). Strictly distinct values in the open domains make every nontrivial exchange strict. The derivative changes sign at \(st=1/4\), so perturbing four close values on opposite sides of \(1/2\) produces opposite strict preferences; the half-risk boundary cannot be uniformly moved.

**5. Exact four-person witness.** With increasing negative probabilities \(a=(1/10,1/5,3/10,2/5)\), compare adjacent pairs \(\{1,2\},\{3,4\}\) with opposite-extreme pairs \(\{1,4\},\{2,3\}\). Ordered pairing yields \(\mathbb E[Y]=93/50\), \(\operatorname{Var}(Y)=313/2500\), while opposite-extreme pairing yields \(\mathbb E[Y]=19/10\), \(\operatorname{Var}(Y)=237/2500\). In other words, ordered pooling reduces the expected count and every upper-tail probability while *increasing* the variance. With \(a=(3/5,7/10,4/5,9/10)\) the same two pairings yield \(\operatorname{Var}(Y)=1113/2500\) and \(1237/2500\), respectively, so the variance comparison reverses across the half-risk threshold. Test-count variances in both cases are four times the reported \(Y\) variances.

## Verification

The included dependency-free `verification/verify.py` evaluates the positive-pool-count law in two independently implemented ways: convolution of exact rational Bernoulli pool probabilities, and (for six-person cases) direct enumeration of independent person-level infection states. It enumerates all equal-size unlabeled partitions for sample sizes \(N\in\{4,6,8,9\}\), across pool sizes \(k\in\{2,3\}\) and multiple exact rational risk profiles. The packaged `verification/certificate.json` reports 2,478 partition evaluations, 7,986 exact upper-tail comparisons, 360 direct state-vs-convolution comparisons, and 246 pairing-variance extremality checks, all passing; it also stores the exact four-person rational examples. Run from a directory containing the `verification` folder using `python3 verification/verify.py` and compare its standard output, after JSON parsing, to the certificate. These are **finite sanity checks**, not an exhaustive check for unbounded population sizes and not the proof of the theorem; the proof above supplies the universal quantifiers.

## Relationship to prior work

Dorfman's 1943 paper introduced the two-stage pooling procedure, and explicitly derived the expected total assay count and its variance for homogeneous risk. Black, Bilder, and Tebbs (2012) analyze richer recursive-halving group tests with heterogeneous risks and their workload distributions. Aprahamian, Bish, and Bish (2019, especially Theorem 1 and Section 4.1) establish existence of an ordered partition for optimization of expected objectives under heterogeneous infection risk, allowing other pool-size designs and imperfect assays. Their ordered-optimality result does **not by itself imply** minimization of *every workload upper tail* for a fixed common pool size. Bobkova, Chen, and Eraslan (2023) modify Dorfman testing by conditionally skipping the last individual test, and identify cases where mixing risks is favorable for that different protocol; their findings are not contradicted by the present fixed-protocol result. Saraiva (2026) studies upper bounds on the expected benefit of positive assortative matching; its accessible abstract does not establish the present joint stochastic-dominance and paired-variance assertions, though the inaccessible full text remains a relevant bibliographic uncertainty. The two-pool transfer argument additionally distinguishes this result from standard Bernoulli comparisons at *fixed sums* of success probabilities: here the constant under a transfer is the **product** of negative probabilities.

## Limitations

The model assumes mutually independent and perfectly detected infection statuses, unit test costs, disjoint pools of one common size, full retesting of every positive pool, and no dilution or assay errors. For correlated infections, imperfect tests, unequal pool sizes, or alternate second-stage algorithms, the conclusion need not hold. No claim is made about optimal pool size, estimated rather than known risk probabilities, throughput with asynchronous processing, or empirical field performance. The half-risk variance statement concerns only size-two pools and parameter regimes on one side of that boundary; it does not describe the general mixed-risk variance optimizer. Although the comparisons and primary sources cited below support the stated literature distinction, exhaustively excluding a previously published equivalent formulation—especially under alternate majorization or reliability terminology—would require an independent bibliographic audit. In particular, the complete 2026 Saraiva article could not be examined here.

## References

1. R. Dorfman (1943), *The Detection of Defective Members of Large Populations*, Annals of Mathematical Statistics 14(4), 436–440. DOI: 10.1214/aoms/1177731363.
2. M. S. Black, C. R. Bilder, J. M. Tebbs (2012), *Group testing in heterogeneous populations by using halving algorithms*, Applied Statistics 61(2), 277–290. Accessible text: https://pmc.ncbi.nlm.nih.gov/articles/PMC4097341/.
3. H. Aprahamian, D. R. Bish, E. K. Bish (2019), *Optimal Risk-Based Group Testing*, Management Science 65(9), 4365–4384. DOI: 10.1287/mnsc.2018.3138. Author-accessible full PDF: https://zhanksun.github.io/files/mnsc.2018.3138.pdf.
4. N. Bobkova, Y. Chen, H. Eraslan (2023 online), *Optimal group testing with heterogeneous risks*, Economic Theory. DOI: 10.1007/s00199-023-01502-3.
5. G. Q. Saraiva (2026), *An upper bound to the benefits of implementing positive assortative matching in pooled testing*, Health Care Management Science. DOI: 10.1007/s10729-026-09759-5.
