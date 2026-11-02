# A five-eighths parking threshold and Poisson overflow law on two-level trees

## Finding

Let \(T_b\) be the full rooted \(b\)-ary tree of height two, with one root, \(b\) intermediate vertices, and \(b^2\) leaves, where \(b\ge2\). There are \(N_b=b^2+b+1\) parking spaces, one per vertex. Independently for each of \(m_b\) cars, draw a uniformly random preferred vertex. The cars park sequentially; upon finding a site occupied, a car travels along its unique upward path to the root, taking the first available site, or exits if there is none. Denote the number of exiting cars by \(F_b(m_b)\).

**Theorem (the full critical escape-count law).** For every fixed \(t\ge0\), if \(m_b/b^{5/4}\to t\), then
\[
 F_b(m_b)\ \xrightarrow{\mathrm d}\ (Z_t-1)_+,
 \qquad Z_t\sim\operatorname{Poisson}(t^4/8),
 \qquad (x)_+=\max\{x,0\}.
\]
In particular,
\[
 \Pr\{F_b(m_b)=0\}\ \longrightarrow\
 \exp(-t^4/8)\left(1+\frac{t^4}{8}\right).
\]
This yields a sharp threshold in terms of the total number \(N_b\) of spaces: \(m_b=o(N_b^{5/8})\) implies that all cars park with probability tending to one, whereas \(m_b/N_b^{5/8}\to\infty\) implies that the probability all cars park tends to zero. At the critical scale, the complete number of failed cars, not just the success indicator, has a shifted-Poisson limit.

**Quantitative Poissonized version.** Let instead the total number of cars be Poisson with mean \(t b^{5/4}\), independently assigning each car a uniform vertex. For each fixed \(t\ge0\), the total-variation distance between the law of the exiting count and that of \((Z_t-1)_+\) is \(O_t(b^{-1/4})\).

## Assumptions and scope

The tree is deterministic and exactly two edges deep, with the same increasing number \(b\) of children at every non-leaf vertex. Preferences are independent, uniform on **all** \(b^2+b+1\) vertices, and cars are processed once under the usual upward parking rule. A car leaving the root is counted as failed. The integer sequence \(m_b\ge0\) is unrestricted except for the asymptotic condition. The distributional statement is for \(b\to\infty\); no finite-tree independence between parking subtrees is assumed under fixed \(m_b\).

## Proof

**1. Order-free tree recursion.** Write \(A_v\) for the number of initial preferences at vertex \(v\). For any vertex \(v\), let \(R_v\) be the number of cars leaving its rooted subtree upward. Then, proceeding from leaves upward,
\[
 R_v=\left(A_v+\sum_{w:\ w\text{ child of }v}R_w-1\right)_+.
\]
The formula follows because all cars within the subtree first occupy its available vertices along upward paths, and any excess crosses the edge to the parent. It is independent of processing order (the standard Abelian property for rooted tree parking). At the root \(o\), \(F_b=R_o\). Adding one extra car cannot decrease \(F_b\), which will justify de-Poissonization.

**2. Poissonize.** Fix \(t>0\) and set \(\mu_b=t b^{5/4}/N_b=t b^{-3/4}(1+O(b^{-1}))\). Take independent \(A_v\sim\operatorname{Poisson}(\mu_b)\) at every vertex. The total number of cars has mean exactly \(N_b\mu_b=t b^{5/4}\). For a leaf \(v\), its upward contribution is \((A_v-1)_+\). Put \(J_v=\mathbf1\{A_v=2\}\), and for each intermediate parent \(i\) let \(B_i\) count its children with \(J_v=1\). The independent variables \(B_i\) are binomial with parameters \(b\) and
\[
 q_b=\Pr\{A_v=2\}=\frac{\mu_b^2 e^{-\mu_b}}2.
\]

**3. Isolate the only critical overflow mechanism.** Let \(G_b\) be the event that (i) no leaf has three or more preferred cars; (ii) no intermediate parent has two or more direct arrivals; (iii) no intermediate parent has both a direct arrival and a leaf with exactly two arrivals; (iv) no intermediate parent has three or more leaves with exactly two arrivals; and (v) the root has no direct arrival. Union bounds and independence give
\[
 \Pr(G_b^c)
 \le O(b^2\mu_b^3)+O(b\mu_b^2)
     +O(b^4q_b^3)+O(\mu_b)
 =O_t(b^{-1/4}).
\]
On \(G_b\), every intermediate subtree sends either zero cars upward if \(B_i\le1\), or exactly one if \(B_i=2\); the direct arrivals permitted at a parent cannot create another overflow. Hence, with
\[
 Z_b=\sum_{i=1}^b\mathbf1\{B_i\ge2\},
\]
we have the exact identity \(F_b=(Z_b-1)_+\) on \(G_b\).

**4. Rare-parent Poisson limit.** Since \(bq_b\to0\), for \(p_b=\Pr\{B_i\ge2\}\),
\[
 p_b=\binom b2 q_b^2+O((bq_b)^3),
 \qquad b p_b\longrightarrow\frac{t^4}{8}.
\]
The parent blocks are independent under Poissonization, so \(Z_b\sim\operatorname{Binomial}(b,p_b)\). Standard binomial-to-Poisson coupling, together with the displayed bad-event bound, proves the quantitative total-variation statement for \(F_b\).

**5. Return to a fixed number of cars.** For any \(0<t_-<t<t_+\), couple the preference sequences for \(\operatorname{Poisson}(t_-b^{5/4})\), \(m_b\), and \(\operatorname{Poisson}(t_+b^{5/4})\) cars by using one infinite sequence of independent uniform vertices. Poisson concentration ensures the three sample sizes are ordered with probability tending to one. Since the number of failed cars is nondecreasing with the number of processed cars, their integer-valued distribution functions are squeezed between the corresponding Poissonized limits. Let \(t_-\uparrow t\) and \(t_+\downarrow t\). For \(t=0\), compare with any fixed \(t_+>0\). This proves the fixed-count limit.

**6. Sharp threshold.** The subcritical assertion follows from the \(t=0\) case. For any sequence \(m_b/b^{5/4}\to\infty\) and any fixed \(T>0\), monotonicity bounds its success probability by that at \(\lfloor Tb^{5/4}\rfloor\), whose limit is \(e^{-T^4/8}(1+T^4/8)\). Let \(T\to\infty\) to obtain zero. As \(N_b\sim b^2\), the load exponent expressed in \(N_b\) is \(5/8\).

## Verification

The accompanying standalone Python program `CHECKER.py` independently simulates cars in their prescribed order and compares the exact resulting number of exits with the bottom-up subtree recursion. It checked all \(50{,}549\) preference sequences for \(b=2\), up to five cars, and \(b=3\), up to four cars, without a mismatch. Independent seeded Monte Carlo diagnostics for moderate \(b\) are also printed. Because the principal error term is only of order \(b^{-1/4}\), these small- and moderate-size simulations are not expected to closely match the eventual limit; they are not used as proof of asymptotics.

Run `python CHECKER.py` using Python 3. The exact checks require only the standard library and complete in ordinary seconds. The infinite-size conclusion rests on the Poissonization, union bound, and monotone de-Poissonization above, not on finite numerical experiments.

## Relationship to prior work

Rooted-tree parking functions and the order-independent property were established well before this theorem; in particular Bruner and Panholzer (2015) study universal characterizations and bounds for fixed rooted trees and aggregate enumeration over Cayley trees. Their extremal star and chain bounds do not give the critical escape-count distribution for a deterministic complete height-two tree. Panholzer (2020) studies tree-family enumeration in regimes with fixed positive load fraction, unlike the vanishing load here. Contat and Curien (2021), the motivating source, study parking on random Cayley trees, where the transition is at a positive load fraction. Aldous, Contat, Curien and Hénard (2022) study an infinite binary tree with fixed degree and an independent car-arrival law, and Contat (2023) studies random trees with prescribed degree sequences and their frozen configuration-model coupling. Those models and results do not assert the high-degree, two-level Poisson overflow law above.

The novel assertion assessed here is **only** the \(b^{5/4}\) / \(N_b^{5/8}\) threshold and the explicit shifted-Poisson distribution of failures, with the quantitative Poissonized approximation. Basic parking definitions, Abelian recursion, and generic Poisson approximation techniques are prior background, not claimed new. No exhaustive historical-priority certification is asserted.

## Limitations

The result is proved for a deterministic, balanced, height-two rooted tree; the argument does not establish the same exponent for arbitrary irregular or random trees, trees of larger height, different parking capacities, or nonuniform preference distributions. The fixed-\(m_b\) limit is qualitative; the \(O_t(b^{-1/4})\) error bound is stated only for Poissonized arrivals. Independent mathematical validation has not been performed.

## References

- M.-L. Bruner and A. Panholzer, *Parking functions for trees and mappings*, arXiv:1504.04972, first posted 20 April 2015. https://arxiv.org/abs/1504.04972
- A. Panholzer, *Parking function varieties for combinatorial tree models*, arXiv:2007.14676, first posted 29 July 2020. https://arxiv.org/abs/2007.14676
- A. Contat and N. Curien, *Parking on Cayley trees & Frozen Erdős–Rényi*, arXiv:2107.02116, first posted 5 July 2021. https://arxiv.org/abs/2107.02116
- D. Aldous, A. Contat, N. Curien and O. Hénard, *Parking on the infinite binary tree*, arXiv:2205.15932, first posted 31 May 2022. https://arxiv.org/abs/2205.15932
- A. Contat, *Parking on trees with a (random) given degree sequence and the Frozen configuration model*, arXiv:2312.04472, first posted 7 December 2023. https://arxiv.org/abs/2312.04472
