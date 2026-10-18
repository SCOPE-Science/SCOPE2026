# Eight vertices are sharp for a transmissibility-dependent vaccination target on trees

## Finding

**Theorem (sharp vaccination-target switch).** Let \(T\) be a finite, simple, unweighted tree on \(2\le n\le7\) vertices. Perfectly vaccinate one vertex \(v\), select a single initial infected vertex uniformly from the remaining \(n-1\) vertices, and run a one-generation-per-infection SIR process in which each contact independently transmits with probability \(p\in(0,1)\). There exists **one fixed vertex** \(v_T\), independent of \(p\), that minimizes the expected final outbreak size simultaneously for **all** \(0<p<1\).

The bound is sharp: an explicit eight-vertex tree has a unique optimal vaccine target \(2\) at low transmissibility and a different unique optimal target \(1\) at high transmissibility. There is one interior tie at the unique \(p_*\in(0,1)\) satisfying

\[
p_*^3+p_*^2=1,\qquad p_*\approx0.7548776662466927.
\]

This is a minimal-order statement specifically for **trees, one vaccinated vertex, one uniformly selected remaining seed, homogeneous independent transmission, and expected final case count**. It is not a statement about arbitrary connected graphs, a fixed initial seed, the largest component, or continuous-time correlated transmission from a random recovery duration.

## Assumptions and scope

Every tree edge represents one symmetric contact between two initially susceptible individuals. Vaccination completely removes its target and adjacent edges *before* an infection seed is selected. Each newly infected individual has one infectious generation, transmitting independently to each still-susceptible neighbor with common probability \(p\), then recovers permanently. All attempts are independent. The objective is the unconditional expectation of the final number of ever-infected, nonvaccinated individuals over the uniformly random seed and transmission events.

For each candidate vaccinee \(v\), write \(T-v\) for the resulting forest and let

\[
F_v(p)=\sum_{\substack{\{x,y\}\subseteq V(T)\setminus\{v\}\\x,y\text{ connected in }T-v}}p^{\operatorname{dist}_T(x,y)}
=\sum_{k=1}^{n-2}c_{v,k}p^k.
\]

Here \(c_{v,k}\) is the nonnegative integer count of unordered surviving vertex pairs at graph distance \(k\) within the same component of \(T-v\). An empty range means the zero polynomial. Write \(E_v(p)\) for the expected final number infected under vaccination of \(v\).

## Proof

**Exact objective.** The unique path between any two unvaccinated vertices \(x,y\) in a tree remains entirely within \(T-v\) or is broken by deleting \(v\). If it survives, transmission from seed \(x\) reaches \(y\) exactly when all \(\operatorname{dist}_T(x,y)\) path contacts transmit. Its probability is \(p^{\operatorname{dist}_T(x,y)}\). Summing infection probabilities over targets and averaging the seed gives

\[
\boxed{E_v(p)=1+\frac{2}{n-1}F_v(p).}
\]

Consequently, minimizing expected outbreak size is exactly minimizing the integer-coefficient polynomial \(F_v\).

**Finite lower bound and an integer certificate.** For two coefficient vectors \(a=(a_1,\ldots,a_{n-2})\) and \(b=(b_1,\ldots,b_{n-2})\), define \(S_k=\sum_{j=1}^{k}(b_j-a_j)\). If \(S_k\ge0\) for every \(k\), then summation by parts gives the exact identity

\[
\sum_{k=1}^{n-2}(b_k-a_k)p^k
=(1-p)\sum_{k=1}^{n-3}S_kp^k+S_{n-2}p^{n-2}\ge0
\quad(0\le p\le1).
\]

Thus it suffices to exhibit a vertex \(v_T\) whose coefficient-vector partial sums are no larger than the corresponding partial sums for any competing vaccinee.

The included standalone program `verification/tree_vaccine_verifier.py` proves this finite statement exhaustively as follows. For each \(n=2,3,4,5,6,7\), it enumerates all \(n^{n-2}\) labelled trees using every Prüfer sequence of length \(n-2\). For each candidate vaccinee it deletes that vertex, computes the component-wise pair-distance counts with breadth-first traversal, and tests all the exact integer inequalities \(S_k\ge0\). On every tree the program finds at least one qualifying vertex. The respective exact numbers of labelled trees examined are

| Vertices | Labelled trees certified |
|:--:|--:|
| 2 | 1 |
| 3 | 3 |
| 4 | 16 |
| 5 | 125 |
| 6 | 1,296 |
| 7 | 16,807 |

The total is **18,248** labelled trees; these cover all isomorphism classes by Prüfer's bijection. This enumeration is a finite proof because the construction visits every labelled tree, makes no random choices, computes the coefficients exactly, and tests a sufficient analytic inequality. No claim is made about the same property for arbitrary \(n>7\).

**Sharp eight-vertex witness.** Let \(T\) have vertices \(0,1,2,3,4,5,6,7\) and edges

\[
\{0\! -\!5,\;0\! -\!1,\;1\! -\!2,\;2\! -\!3,\;2\! -\!4,\;5\! -\!6,\;6\! -\!7\}.
\]

The pair-distance polynomials for vaccinating vertices \(1\) and \(2\) are

\[
F_1(p)=5p+3p^2+p^3,\qquad
F_2(p)=4p+3p^2+2p^3+p^4.
\]

The exact vectors \((c_{v,1},\ldots,c_{v,6})\) for the other vaccinees are

| Vaccine vertex | Pair-distance coefficient vector |
|:--:|:--|
| \(0\) | \((5,4,0,0,0,0)\) |
| \(3\), \(4\) | \((6,5,4,3,2,1)\) |
| \(5\) | \((5,4,2,0,0,0)\) |
| \(6\) | \((5,5,3,2,0,0)\) |
| \(7\) | \((6,6,4,3,2,0)\) |

For **each** one of these other vaccinees \(w\), every partial sum of the coefficient vector for \(F_w-F_1\) is nonnegative. The same summation-by-parts certificate therefore proves \(F_1(p)\le F_w(p)\) for all \(0\le p\le1\). The inequalities are strict in \(0<p<1\). The only possible minimizing vaccinees are \(1\) and \(2\). Their difference is

\[
\boxed{F_2(p)-F_1(p)=p(p^2+p^3-1).}
\]

Since \(p^2+p^3\) increases strictly from zero to two on \((0,1)\), its level one is crossed exactly once. Thus \(2\) uniquely minimizes \(E_v\) for \(0<p<p_*\), both \(1\) and \(2\) tie at \(p_*\), and \(1\) uniquely minimizes \(E_v\) for \(p_*<p<1\). This concludes both the bound and its sharpness.

## Verification

The standalone Python 3 program uses only the standard library and is executable with `python3 verification/tree_vaccine_verifier.py`. It enumerates all 18,248 labelled trees through order seven, checks the universal partial-sum certificate, verifies all eight witness coefficient vectors and their global comparisons, and checks exact rational outcomes at two transmission probabilities.

An independent second implementation checked all 24 unlabelled trees through order seven using graph-isomorphism generation and a separate shortest-path routine. Direct enumeration of every retained-edge state of the eight-vertex witness, without using the pair-distance identity, gives at \(p=1/2\)

\[
E_1(1/2)=\frac{55}{28},\qquad E_2(1/2)=\frac{15}{8},
\]

and at \(p=9/10\)

\[
E_1(9/10)=\frac{11159}{3500},\qquad E_2(9/10)=\frac{116441}{35000}.
\]

These exact evaluations are consistent with the proved crossover. The supplied Prüfer enumeration, integer certificate, and analytic witness argument—not Monte Carlo estimates—establish the theorem.

## Relationship to prior work

Schneider, Mihaljev, Havlin, and Herrmann (arXiv:1102.1929v1, public 2011-02-09) optimize susceptible-cluster fragmentation and sequential immunization, motivated by disease control on large empirical networks. Their inspected full preprint does not state the sharp one-vaccine, random-seed, tree-specific crossover result.

Altarelli, Braunstein, Dall'Asta, Wakeling, and Zecchina (arXiv:1309.2805v1, public 2013-09-11) formulate the targeted network immunization problem and develop message-passing strategies. Their inspected full preprint derives epidemic branch equations and immunization optimization, but not the above minimal tree-order classification or the explicit exact crossover.

Holme (arXiv:1708.06456v1, public 2017-08-22) calculates exact node importance in SIR processes on all connected graphs through seven vertices. Its inspected full preprint uses a continuous-time infection/recovery process with shared random infectious duration rather than independent pre-sampled edge transmission, and does not classify this eight-vertex tree witness. Consequently its results do not imply the present statement through a direct substitution. Related small-network targeting and centrality phenomena are established prior knowledge; the claim here is the specified sharp boundary and exact target switch.

Holme (arXiv:q-bio/0403021, public 2004-03-16) studies locally informed vaccination heuristics. Only the accessible preprint abstract was inspected; its complete text was not available through the attempted route. This remains a limited bibliographic comparison rather than a full-text negative assertion.

## Limitations

The theorem uses homogeneous independent edge transmissibility and perfect vaccination; vaccination is chosen before, and the unique seed is chosen uniformly after, deletion. Correlated transmission, heterogeneous contacts, epidemiological timing, degree-weighted seed risks, partial vaccine efficacy, multiple vaccines, and non-trees are outside the claim. The finite lower bound is a verified exhaustive computation for \(n\le7\), not an inference that the same prefix-dominance property extends to all trees. The difference between the present minimality assertion and analogous continuous-time SIR models is substantive. No independent scholarly review or external certification is asserted.

## References

1. C. M. Schneider, T. Mihaljev, S. Havlin and H. J. Herrmann, *Suppressing Epidemics with a Limited Amount of Immunization Units*, arXiv:1102.1929v1 (2011-02-09), https://arxiv.org/abs/1102.1929.
2. F. Altarelli, A. Braunstein, L. Dall'Asta, J. R. Wakeling and R. Zecchina, *Containing epidemic outbreaks by message-passing techniques*, arXiv:1309.2805v1 (2013-09-11), https://arxiv.org/html/1309.2805v1.
3. P. Holme, *Three faces of node importance in network epidemiology: Exact results for small graphs*, arXiv:1708.06456v1 (2017-08-22), https://arxiv.org/abs/1708.06456.
4. P. Holme, *Efficient local strategies for vaccination and network attack*, arXiv:q-bio/0403021 (2004-03-16), https://arxiv.org/abs/q-bio/0403021.
