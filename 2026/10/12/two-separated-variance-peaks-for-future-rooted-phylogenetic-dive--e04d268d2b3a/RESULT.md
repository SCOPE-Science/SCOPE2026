# Two separated variance peaks for future rooted phylogenetic diversity under uniform extinction

## Finding

In a ten-species rooted ultrametric phylogeny, the variance of future rooted phylogenetic diversity under **independent, identical extinction risks** can have two separated strict local maxima as the extinction probability increases from zero to one. More strongly, this happens throughout an entire interval of crown-stem lengths, with exactly two maxima in the explicit unresolved-crown family. A fully resolved strictly bifurcating ten-tip tree with positive rational edge lengths also has at least two such maxima; the four strict derivative inequalities below persist under small perturbations.

Let \(q\in[0,1]\) be the common extinction probability, and let \(P_q\) be the sum of lengths of edges on paths from the root to at least one surviving tip, with \(P_q=0\) if all tips die. Put \(V(q)=\operatorname{Var}(P_q)\). The assertion is about the number of local maxima of \(V\), **not** about modes of the distribution of \(P_q\).

**Unresolved-crown theorem.** For each \(a\in[7/10,4/5]\), attach an outgroup tip to the root by an edge of length \(1\); attach a crown node by an edge of length \(a\), then attach nine tips to that node by edges of length \(1-a\). Every root-to-tip distance equals one. For this tree,

\[
V_a(q)=\bigl(1+9(1-a)^2\bigr)q(1-q)+a^2q^9(1-q^9)+18a(1-a)(1-q)q^9.
\]

The derivative has the strictly alternating signs \((+,-,+,-)\) at \(q=1/2,3/5,3/4,9/10\), respectively, for *every* stem length in the closed stated interval. There are exactly three critical points in \((0,1)\), one in each intervening interval; the first and third are strict local maxima and the middle one is a strict local minimum. The case \(a=3/4\) reduces to

\[
V_{3/4}(q)=\frac{25}{16}q(1-q)+\frac9{16}q^9(1-q^9)+\frac{27}{8}(1-q)q^9,
\]

\[
16V'_{3/4}(q)=25-50q+567q^8-540q^9-162q^{17}.
\]

**Fully resolved witness.** The same derivative-sign pattern occurs on the following strictly bifurcating tree. The root has two children: tip \(0\) at length \(1\), and the first of eight crown internal nodes \(C_0,\ldots,C_7\), with root-to-\(C_0\) length \(3/4\). For \(j=0,\ldots,6\), node \(C_j\) has a leaf child \(j+1\) connected by an edge of length \(1-(3/4+j/1000)\), and a child \(C_{j+1}\) connected by length \(1/1000\). Finally, \(C_7\) has the two leaf children \(8,9\), both attached by length \(1-(3/4+7/1000)\). All \(18\) edges are positive and every root-to-tip distance is \(1\). Writing the resulting variance as \(V_B(q)\), exact rational calculation gives

\[
V'_B(1/2)>\frac1{20},\qquad V'_B(3/5)<-\frac1{20},\qquad
V'_B(3/4)>\frac1{10},\qquad V'_B(9/10)<-\frac12.
\]

Thus this binary tree has at least two strict local maxima, in \((1/2,3/5)\) and \((3/4,9/10)\), separated by at least one local minimum in \((3/5,3/4)\). These inequalities hold on a nonempty open neighborhood of the displayed positive edge-length vector; likewise on sufficiently small perturbations within the ultrametric subspace.

## Assumptions and scope

Every species survives independently with probability \(1-q\); each tip has the same risk and shares no extinction dependence with other tips. The tree is fixed, with positive edge lengths. The branch lengths above are measured in units of the common root-to-tip height. Rooted phylogenetic diversity includes the root-to-tip path even if only one tip survives. No stochastic time dynamics or phylogenetic covariance of extinction indicators are imposed. The unresolved family permits a nine-way crown split; the separate binary construction establishes that nonbinary branching is not necessary.

## Proof

For the unresolved-crown tree, let \(Z\) indicate outgroup survival, and let \(S\) count crown survivors. Independence gives \(Z\sim\operatorname{Bernoulli}(1-q)\), \(S\sim\operatorname{Binomial}(9,1-q)\), and \(Z\perp S\). Define \(I=\mathbf1_{\{S>0\}}\). Then

\[
P_q=Z+aI+(1-a)S.
\]

Directly, \(\operatorname{Var}(Z)=q(1-q)\), \(\operatorname{Var}(S)=9q(1-q)\), \(\operatorname{Var}(I)=q^9(1-q^9)\), and \(\operatorname{Cov}(I,S)=9(1-q)q^9\). Expanding the variance proves the formula in the Finding section.

Write \(B(a)=1+9(1-a)^2>0\). Differentiation yields

\[
V'_a(q)=B(a)(1-2q)+9a^2q^8(1-2q^9)+18a(1-a)q^8(9-10q).
\]

To certify signs *uniformly in the real interval* \(a\in[7/10,4/5]\), set \(a=7/10+t/10\) with \(t\in[0,1]\). At each of the four test probabilities, \(\sigma V'_a(q)\), with respective target signs \(\sigma=+1,-1,+1,-1\), is quadratic in \(t\). Expand it in the quadratic Bernstein basis

\[
\sigma V'_a(q)=\beta_0(1-t)^2+2\beta_1t(1-t)+\beta_2t^2.
\]

Exact rational expansion (reproduced in the standalone verifier) establishes these **strict lower bounds on every one of the three coefficients**:

| \(q\) | \(\sigma\) | Proven lower bound for \(\min_i\beta_i\) |
|---|---|---|
| \(1/2\) | \(+\) | \(3/50\) |
| \(3/5\) | \(-\) | \(3/100\) |
| \(3/4\) | \(+\) | \(3/100\) |
| \(9/10\) | \(-\) | \(1/2\) |

Because the Bernstein basis terms are nonnegative and sum to one, these bounds prove every claimed sign for every real \(a\) in the closed interval, not merely for sampled stem lengths.

For positive \(a<1\), the nonzero coefficients of \(V'_a\), in descending powers of \(q\), have signs

\[
\operatorname{sgn}\bigl(-18a^2,\;-180a(1-a),\;9a^2+162a(1-a),\;-2B(a),\;B(a)\bigr)=(-,-,+,-,+).
\]

There are precisely three sign changes. Descartes' rule of signs bounds the number of positive roots, counted with multiplicity, by three. The four certified signs force at least one positive root in each of the three disjoint intervals, so there are **exactly three**, all simple, and the sign order makes the first and third strict maxima and the second a strict minimum.

For the fully resolved tree, index the leaf set by \(\{0,\ldots,9\}\). For each directed edge \(e\) let \(S_e\) be its nonempty set of descendant leaves and \(\ell_e>0\) its length. The edge indicator \(Y_e\) is one when at least one descendant survives. Independence implies

\[
\operatorname{Cov}(Y_e,Y_f)=q^{|S_e\cup S_f|}-q^{|S_e|+|S_f|},
\quad
V_B(q)=\sum_{e,f}\ell_e\ell_f\left(q^{|S_e\cup S_f|}-q^{|S_e|+|S_f|}\right).
\]

This is the familiar exact edge-covariance identity of Faller, Pardi, and Steel (their Lemma 2.1, specialized to identical risks); **the identity itself is not claimed as new**. Inserting the explicit edge lengths and descendant sets above, differentiating this polynomial, and comparing exact fractions gives the four displayed strict rational margins. The included complete Python 3 verifier constructs these very edges, checks all the claimed margins, and independently reconstructs the variance via all survivor states. Continuity of the derivative in the finite edge lengths preserves the strict inequalities in a nonempty open set. This finishes the proof.

## Verification

Run `python3 verify_pd_variance.py` using only Python 3 standard-library modules. It prints `VERIFY_OK` when all checks pass. It verifies the analytic variance and derivative polynomials at \(a=3/4\), four exact interval-wide Bernstein sign certificates, all positive branch lengths and ultrametric root-to-leaf paths for the binary witness, four exact binary derivative inequalities, and agreement of the edge-covariance and direct survivor-state variance calculations at four independent probabilities on each of two tree profiles. The last comparison covers \(2\times4\times2^{10}=8192\) survivor-state contributions. Finite enumeration is a cross-check; the statements for every real \(a\) in the interval and every \(q\) in \((0,1)\) follow from the algebraic proof.

## Relationship to prior work

Faller, Pardi, and Steel (2008; publicly available as arXiv:0708.0425 on 2 August 2007) introduced the stochastic future-PD setting and established a general exact variance formula (Lemma 2.1), together with asymptotic distribution and exact-computation results. The present theorem uses that formula but proves a **qualitative variation law** not stated there: two separated local maxima in the risk-dependent variance, uniformly over a nontrivial continuous parameter interval, and their persistence on fully bifurcating ultrametric trees. O'Dwyer, Kembel, and Green (2012) derive analytic PD sampling means and variances in ecological metacommunities; their paper treats sampling schemes and phylogenetic edge-length abundance, not this three-critical-point extinction-probability theorem. Nipperess and Matsen (2013) derive PD mean/variance under fixed-size rarefaction, a different sampling law. Existing exact variance formulas are acknowledged rather than presented as new.

## Limitations

The proof does **not** assert that ten leaves are minimal, classify all trees exhibiting this behavior, or give exact numbers of critical points for the fully bifurcating witness (only at least three critical points and at least two maxima are established there). It does not cover dependent extinctions or heterogeneous probabilities, nor make empirical predictions for realistic extinction regimes. The fully resolved witness has very short internal edges, chosen to maintain the strict sign pattern; the existence of a larger perturbation neighborhood is qualitative, not quantified. Although relevant primary papers and a published research-index search were compared, unindexed or unpublished analyses of variance shapes could exist.

## References

1. B. Faller, F. Pardi, M. Steel, *Distribution of phylogenetic diversity under random extinction*, Journal of Theoretical Biology 251 (2008), 286–296, doi:10.1016/j.jtbi.2007.11.034; initial public arXiv manuscript arxiv:0708.0425 (2007-08-02). Lawful author full text: https://www.math.canterbury.ac.nz/~m.steel/Non_UC/files/research/arxiv-1.pdf .
2. J. P. O'Dwyer, S. W. Kembel, J. L. Green, *Phylogenetic diversity theory sheds light on the structure of microbial communities*, PLOS Computational Biology 8 (2012), e1002832, doi:10.1371/journal.pcbi.1002832 .
3. D. A. Nipperess, F. A. Matsen IV, *The mean and variance of phylogenetic diversity under rarefaction*, Methods in Ecology and Evolution 4 (2013), 566–572, doi:10.1111/2041-210X.12042; preprint arxiv:1208.6552 .
