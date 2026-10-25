# Fixed-prefix rigidity of one-location stopping sets on finite atomic Poisson spaces

## Finding

**Theorem (complete finite-atomic classification).** Fix an integer \(n\geq0\), the finite labeled space \(E=\{1,\ldots,n\}\), and arbitrary intensities \(\lambda_i\in(0,\infty)\). Let \(N_i\) be independent Poisson variables of means \(\lambda_i\). A map \(Z:\mathbb N_0^n\to2^E\) is a **stopping set** when it satisfies the restriction property
\[
\bigl[a_i=b_i\text{ for every }i\in Z(a)\bigr]\quad\Longrightarrow\quad Z(b)=Z(a)
\qquad(a,b\in\mathbb N_0^n).
\]
If
\[
\sum_{i\in Z(N)}\mathbf1_{\{N_i>0\}}\leq1\quad\text{almost surely},
\]
then there is a **unique** ordered list of distinct sites \(\pi=(i_1,\ldots,i_r)\) of some length \(0\leq r\leq n\) such that the following describes \(Z\) on *every* count configuration \(a\): inspect \(i_1,i_2,\ldots\) in this fixed order, and stop immediately on the first positive count or when the list is exhausted; the returned set is the inspected prefix. The empty list gives the constant empty map.

Conversely, every such partial permutation defines a stopping set satisfying the restriction property and one-occupied-site condition. Every one of these maps is **exactly** obtained at a stopping time of a deterministic, one-atom-at-a-time, \(\mu\)-continuous continuous-time decision tree, where \(\mu=\sum_i\lambda_i\delta_i\). In particular, exact equality holds for every configuration, not only modulo intensity-null sets.

The number of such maps on \(n\) labeled atoms is
\[
A_n=\sum_{r=0}^n\frac{n!}{(n-r)!}.
\]
For \(n=0,1,2,3,4\), these values are \(1,2,5,16,65\). This rigidity fails for a budget of **two** occupied sites: on three sites one can inspect site \(1\) and then inspect site \(2\) or \(3\) according to the parity of its observed count, producing a stopping set whose second query genuinely depends on observations.

## Assumptions and scope

The intensities are strictly positive and finite, and the complete finite count vector is the underlying sample space. Multiplicities matter: the budget concerns the **number of occupied locations revealed**, not the total point multiplicity. All stopping-set axioms hold pointwise on \(\mathbb N_0^n\); the occupancy budget is initially probabilistic, but positivity of the joint Poisson mass at every count vector makes it equivalent to a pointwise restriction. No randomization of the stopping rule is allowed. The result is about finite purely atomic spaces, not diffuse or countably infinite configurations.

For an ordered list \(\pi\) of length \(r>0\), write
\[
K(a)=\min\bigl(\{k\in\{1,\ldots,r\}:a_{i_k}>0\}\cup\{r\}\bigr),
\qquad Z(a)=\{i_1,\ldots,i_{K(a)}\}.
\]
For \(r=0\), define \(Z(a)=\varnothing\).

## Proof

**1. Replace the almost-sure budget by a pointwise budget.** The joint Poisson distribution assigns strictly positive probability to every \(a\in\mathbb N_0^n\), because all \(\lambda_i\) are strictly positive and finite. Thus the failure of the occupied-location bound at even one configuration would have positive probability. Hence the bound holds for every configuration.

**2. Identify the forced first atom.** If \(Z(a)=\varnothing\) for some configuration, every configuration agrees with \(a\) on that empty set; the stopping property therefore makes \(Z\) identically empty. Otherwise put \(u=(1,\ldots,1)\). Every coordinate of \(u\) is positive, so the pointwise budget implies that \(Z(u)=\{j\}\) for one atom \(j\). The stopping property then gives
\[
a_j=1\quad\Longrightarrow\quad Z(a)=\{j\}.
\]
For arbitrary \(a\), suppose \(j\notin Z(a)\). Change only its \(j\)-th coordinate to \(1\), obtaining \(b\). The two configurations agree on \(Z(a)\), so \(Z(b)=Z(a)\) and \(j\notin Z(b)\), contrary to the preceding implication. Therefore \(j\in Z(a)\) for every \(a\).

**3. Any positive count at the first atom forces immediate stopping.** Fix \(c\geq1\), and let \(v_j=c\) with all other coordinates of \(v\) equal to \(1\). Since every coordinate of \(v\) is positive and \(j\in Z(v)\), the pointwise budget gives \(Z(v)=\{j\}\). Every configuration \(a\) with \(a_j=c\) agrees with \(v\) on this stopping set, hence \(Z(a)=\{j\}\). Thus \(Z(a)=\{j\}\) whenever \(a_j>0\), irrespective of other counts.

**4. Restrict to the zero fiber and iterate.** On configurations with \(a_j=0\), define the residual map \(Z'\) on the remaining \(n-1\) coordinates by \(Z'(a_{-j})=Z(0,a_{-j})\setminus\{j\}\). Since \(j\) belongs to every returned set, agreement on \(Z'(a_{-j})\), together with the fixed value \(a_j=0\), entails agreement on \(Z(0,a_{-j})\). Thus \(Z'\) is again a stopping set, with at most one occupied residual coordinate. Induction on \(n\), with the empty-space base case, yields a fixed partial permutation of the residual atoms. Prepending \(j\) gives the claimed prefix rule for \(Z\). The first element \(j\) is recovered uniquely from \(Z(u)\), and the entire remaining list is recovered uniquely by applying the same construction on the zero fiber; hence the representation is unique.

**5. Converse and exact exploration.** A prefix rule is determined by the counts on its returned prefix, so it satisfies the restriction property. It stops at the first positive count, hence sees at most one occupied site. For \(r>0\), reveal atom \(i_1\) at time \(0\), then atom \(i_k\) at integer time \(k-1\); keep the explored set fixed between those instants and after the final query. Each increment introduces at most one atom of \(\mu\), so this deterministic nested right-continuous family is \(\mu\)-continuous in the atomic sense. Stop the family on the first positive observed count, or at time \(r-1\) if none appeared before. This is a stopping time for the observed filtration and produces exactly \(Z(a)\) for every \(a\). The constant-empty rule is obtained by an empty exploration stopped at time \(0\).

**6. Count and sharpness.** There are \(n!/(n-r)!\) partial permutations of length \(r\), and Step 4 proves that they correspond bijectively to stopping sets under the budget, giving the displayed formula for \(A_n\). For the two-occupied-site counterexample with \(n=3\), always reveal site \(1\). If \(a_1\) is even return \(\{1,2\}\); otherwise return \(\{1,3\}\). Each result is determined by observed counts, and each contains at most two occupied sites. The second inspected site depends on the observed parity, so it is not a fixed-prefix first-positive rule. This shows the budget of one is the structural threshold for the classification.

## Verification

A standalone exact finite verifier, `verify_atomic_stopping.py`, enumerates **all** stopping-set maps on products of finite count alphabets by partitioning the configuration cube into compatible observed-coordinate cylinders. It independently enumerates the fixed-prefix constructions and checks equality of the two sets. It passed for binary alphabets on \(0\leq n\leq4\) and for the ternary alphabet \(\{0,1,2\}\) on \(1\leq n\leq3\). The resulting counts are \(1,2,5,16,65\) and \(2,5,16\), respectively. This finite calculation is corroboration; the induction above proves the statement for arbitrary \(n\) and unbounded integer multiplicities.

For a list \(\pi\) of length \(r>0\), its output length has the explicitly computable law
\[
\Pr(K=k)=\exp\Bigl(-\sum_{h<k}\lambda_{i_h}\Bigr)(1-e^{-\lambda_{i_k}}),\quad1\leq k<r,
\]
and \(\Pr(K=r)=\exp(-\sum_{h<r}\lambda_{i_h})\). In particular, the class of admissible maps and its size are independent of the intensities, while their observed-prefix distributions retain intensity dependence.

## Relationship to prior work

Khezeli, *On Stopping Sets and Continuous-Time Decision Trees* (arXiv:2610.22011v1, publicly submitted 2026-10-15), proves in Theorem 1.3 that locally bounded stopping sets revealing at most one **point** are attainable when the intensity is **diffuse**. Its Definition 3.1 explicitly permits atomic one-location jumps, but the attainability theorem retains the diffuse assumption; Remark 4.2 additionally leaves stronger exact equality open in that setting. The present finite-atomic theorem is not a consequence of the diffuse hypothesis: a positive Poisson atom can carry multiple points, and the relevant criterion here counts occupied **locations**. Its added conclusions are a pointwise partial-permutation classification, unique representation, exact cardinality, and pointwise realization without null-set modifications.

Last, Peccati, and Yogeshwaran, *Phase transitions and noise sensitivity on the Poisson space via stopping sets and decision trees* (arXiv:2101.07180v3), provide the restriction-determination stopping-set framework and construct more general non-attainable stopping sets in Appendix B. Those constructions do not give the one-occupied-atomic-location classification. The proof here is elementary once the exact finite-atomic condition is isolated; no claim is made to the general diffuse classification or to new general decision-tree machinery.

## Limitations

The full-support argument requires every intensity to be strictly positive. Vanishing intensities create configurations of zero probability and need a different pointwise classification. The theorem does not classify arbitrary stopping sets, randomized rules, or two-location-bounded rules, beyond the explicit sharpness counterexample. It does not settle exact attainability on diffuse spaces or on infinite atomic spaces. The comparison with possible implicit classical finite decision-tree normal forms remains an originality risk; no independent literature audit has been performed.

## References

1. Ali Khezeli, *On Stopping Sets and Continuous-Time Decision Trees*, arXiv:2610.22011v1 (first submitted 2026-10-15), Sections 2–4, especially Definition 3.1, Theorem 1.3 and Remark 4.2. https://arxiv.org/html/2610.22011v1
2. Günter Last, Giovanni Peccati and D. Yogeshwaran, *Phase transitions and noise sensitivity on the Poisson space via stopping sets and decision trees*, arXiv:2101.07180v3 (first submitted 2021-01-18), Appendices A–B. https://arxiv.org/html/2101.07180v3
