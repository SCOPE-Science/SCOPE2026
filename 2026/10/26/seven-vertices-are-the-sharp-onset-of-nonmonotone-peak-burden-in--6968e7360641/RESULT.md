# Seven vertices are the sharp onset of nonmonotone peak burden in rooted tree epidemics

## Finding

Consider synchronous Reed–Frost SIR transmission on a finite rooted tree: each infected vertex can transmit to each still-susceptible neighbor once, independently with probability \(p\), and is then removed. The sole initially infected vertex is the designated root. Let \(I_j\) be the number newly infected in generation \(j\), including \(I_0=1\). Let \(\tau\) be the **first** generation at which \(I_j\) attains its maximum over the epidemic, and set \(H_T(p)=\mathbb E[\sum_{j=0}^{\tau}I_j]/|V(T)|\).

**Theorem (sharp rooted-tree cutoff and complete first exception census).** For every rooted tree with at most six vertices, \(H_T(p)\) is nondecreasing on \([0,1]\). Among the 48 root-preserving isomorphism types on seven vertices, exactly two have a nonmonotone \(H_T\). Both have a unique strict interior maximum and are strictly decreasing sufficiently near \(p=1\). They are precisely the following rooted trees:

- **Type A:** the root has a leaf neighbor and a second neighbor followed by a chain of two further edges ending in a fork with two leaf children; its level populations when all edges are open are \((1,2,1,1,2)\). An unambiguous edge list is \(\{(0,1),(0,6),(1,2),(2,3),(3,4),(3,5)\}\).
- **Type B:** the root has two leaf neighbors and a third neighbor that itself has three leaf neighbors; its level populations with all edges open are \((1,3,3)\). An edge-list realization is \(\{(0,1),(0,2),(0,3),(3,4),(3,5),(3,6)\}\), rooted at \(0\).

For these two types the **expected cumulative case counts** (before dividing by seven) are exactly

\[
7H_A(p)=1+2p^2+5p^5-5p^6,\qquad
7H_B(p)=1+6p^2+6p^3-23p^4+25p^5-11p^6.
\]

Type A peaks at the unique \(p\in(0,1)\) solving \(30p^4-25p^3-4=0\), approximately \(0.9765183354\). Type B peaks at the unique \(p\in(0,1)\) solving \(66p^4-125p^3+92p^2-18p-12=0\), approximately \(0.9381828767\). At full transmissibility \(H_A(1)=3/7\) and \(H_B(1)=4/7\). All claims are for the explicitly stated first-maximum tie convention.

## Assumptions and scope

All graphs in the theorem are finite, simple, connected, undirected **trees** \(T=(V,E)\), with a specified root \(r\), and \(1\le |V|\le7\). Edges transmit independently with common \(p\in[0,1]\). Infection lasts exactly one generation; a newly infected node is infectious in the next generation and removed afterwards. The initial infectious set is exactly \(\{r\}\); no importation, reinfection, or additional seed occurs. A source at generation \(j\) transmits only to susceptible neighbors in generation \(j+1\). In ties for largest active-infection count, the **earliest** generation is used. The statistic is **cumulative infected up to that peak**, not the final attack rate, expected peak incidence, peak time, or an expectation taken before choosing the peak.

We use the term *peak burden* as a precisely defined peak-indexed proxy inspired by the empirical 'herd immunity threshold at the peak' statistic in the motivating literature, not as a claim that this finite-tree quantity is a classical herd-immunity threshold.

## Proof

**1. Percolation representation.** Preassign independent Bernoulli open/closed marks to all edges. Because a tree has a unique root-to-vertex path, a vertex is infected at time \(j\) exactly when every edge on its root path is open and that path has length \(j\). Thus a realization is completely encoded by a subset \(F\subseteq E\): let \(a_j(F)\) be the number of vertices in the root component of \((V,F)\) at distance \(j\) from the root; choose \(t(F)=\min\{j:a_j(F)=\max_k a_k(F)\}\), and define \(C(F)=\sum_{j\le t(F)}a_j(F)\). The exact finite expectation is

\[
|V|H_T(p)=\sum_{F\subseteq E} C(F)p^{|F|}(1-p)^{|E|-|F|}.
\]

This is a finite identity for the actual stochastic SIR process, not an approximation or a simulation formula.

**2. Bernstein monotonicity certificate.** Write \(m=|E|=|V|-1\) and

\[
h_k=\sum_{\substack{F\subseteq E\\|F|=k}}C(F),\quad
b_k=\frac{h_k}{\binom mk},\qquad 0\le k\le m.
\]

Then \(|V|H_T(p)=\sum_{k=0}^m\binom mk b_kp^k(1-p)^{m-k}\), so direct differentiation yields

\[
|V|H'_T(p)=m\sum_{k=0}^{m-1}\binom{m-1}k(b_{k+1}-b_k)p^k(1-p)^{m-1-k}.
\]

Hence all nonnegative adjacent differences \(b_{k+1}-b_k\) guarantee nondecreasing \(H_T\) throughout \([0,1]\).

**3. Complete finite cutoff classification.** The packaged `verify.py` constructs **every** labeled tree on \(n\le7\) vertices using the Prüfer-code bijection, canonically identifies rooted isomorphism classes by recursively sorting child-tree codes, and enumerates every one of the \(2^{n-1}\) possible open-edge sets of each representative. It calculates all \(h_k\) as integers and all \(b_{k+1}-b_k\) as exact rational numbers. The complete 85-row `rooted_tree_certificate.tsv` gives the reproducible data. The numbers of distinct rooted trees for \(n=1,2,3,4,5,6,7\) are \(1,1,2,4,9,20,48\), respectively.

For **every** rooted type with \(n\le6\), every adjacent Bernstein difference is nonnegative. For \(n=7\), the same is true for 46 of the 48 types. The two remaining types have respective exact Bernstein difference vectors

\[
A:\quad(0,\tfrac{2}{15},\tfrac{4}{15},\tfrac25,\tfrac{41}{30},-\tfrac16),
\qquad
B:\quad(0,\tfrac25,\tfrac{11}{10},\tfrac{17}{30},\tfrac{43}{30},-\tfrac12).
\]

Their final negative entries prove \(|V|H'_A(1)=-1\) and \(|V|H'_B(1)=-3\), so both are nonmonotone. Rooted Prüfer enumeration and canonical rooted codes ensure that no tree or rooting of the stated orders is omitted; the argument makes **no** claim about orders eight and above.

**4. Analytical formulas for the two exceptions.** For Type A, let \(w\) indicate that the root-to-leaf edge is open, and let \(x\) indicate the first edge of the length-four arm. When \(w=x=1\), the peak is first achieved in generation one, so \(C=3\), regardless of the later edges. If \(w=0\) and all five other edges are open, the two-terminal-leaf generation is the unique maximum and \(C=6\). In every other configuration \(C=1\). Thus \(C=1+2\mathbf1_{\{w=x=1\}}+5\mathbf1_{\{w=0,\text{all other edges open}\}}\), yielding the displayed formula for \(7H_A\).

For Type B, let \(X\) indicate opening of the root-to-hub edge, \(J\sim\operatorname{Bin}(2,p)\) count open root-to-leaf edges, and \(K\sim\operatorname{Bin}(3,p)\) count open hub-to-leaf edges; these variables are independent. If \(X=0\), then \(C=1+2\mathbf1_{\{J=2\}}\). If \(X=1\), then \(C=1,4,5\) for \(J=0\) and \(K\le1,K=2,K=3\), respectively; \(C=3,6\) for \(J=1\) and \(K\le2,K=3\), respectively; and \(C=4\) for \(J=2\). Taking these elementary binomial expectations gives the polynomial for \(7H_B\).

Their derivatives factor as

\[
7H'_A(p)=-p(30p^4-25p^3-4),\qquad
7H'_B(p)=-p(66p^4-125p^3+92p^2-18p-12).
\]

Under the bijection \(p=t/(1+t)\) from \((0,1)\) to \((0,\infty)\), the respective quartic factors, multiplied by \((1+t)^4\), become \(t^4-41t^3-24t^2-16t-4\) and \(3t^4-43t^3-34t^2-66t-12\). Each has exactly one positive root by Descartes' sign rule and the sign change between \(t=0\) and sufficiently large \(t\). Since the quartic factor is negative at \(p=0\) and positive at \(p=1\), each expected-burden curve strictly increases to its unique maximum and then strictly decreases.

## Verification

Run `python3 verify.py` in the directory containing `rooted_tree_certificate.tsv`. The only dependency is Python's standard library. The verification rebuilds every labeled tree through seven vertices by the Prüfer correspondence, reduces root-preserving duplicates by canonical child-tree encodings, enumerates all bond states, reconstructs the exact Bernstein profiles, checks the entire attached certificate byte for byte, verifies every nonnegative difference outside the two named exceptions, checks their exact polynomial coefficients and endpoint derivatives, and checks the positive-root Descartes transformations. Expected ending: `EXACT_CERTIFICATE_OK rooted_types_checked 85 seven_vertex_exception_types 2`.

The independent first-principles calculations for Types A and B in Step 4 provide a separate algebraic check on the two reported polynomials. All numerical decimal thresholds are illustrations of the uniquely specified exact algebraic roots; no numerical root search is used to certify monotonicity or exhaustive classification.

## Relationship to prior work

Ozbay, Nielsen and Nguyen (arXiv:2212.06995; original submission 14 December 2022) document nonmonotonic peak-defined cumulative infection statistics in discrete-time network SIR simulations and identify shifts in the generation of peak infection as the mechanism. That nonmonotonic phenomenon and the peak-defined statistic are **not** claimed as new. Their article studies larger simulated networks and does not supply the sharp seven-vertex rooted-tree onset, the exact census of two rooted exceptions, or their polynomial thresholds. The present calculation treats a precisely specified single-seed, one-generation-infectious special case.

Sharkey, Kiss, Wilkinson and Simon (DOI:10.1007/s11538-013-9923-5) derive exact expected infectious-time equations for **continuous-time Markovian** SIR on tree networks. Exact first moments at fixed times do not themselves evaluate an expectation whose stopping time is the random sample-path peak; their model and stated results do not imply the discrete peak-burden classification. Curran-Sebastian, Pellis, Hall and House (arXiv:2301.07058) study epidemic first-passage and peak-time uncertainty using continuous-time branching and deterministic approximations, not a finite rooted-tree earliest-peak polynomial census.

Known rooted-tree counts used to cross-check enumeration are background combinatorics, not the claimed new epidemic content. The publication-priority comparison is best-knowledge rather than an exhaustive proof of uniqueness in all literature.

## Limitations

The sharp minimality applies **only within rooted trees** with a single predetermined seed and synchronous one-generation infectiousness. Other graphs (including cycles), random or multiple seeds, different recovery laws, and different conventions for ties between peak generations may have different minimal orders and exceptional families. Neither classical infinite-population herd immunity nor cumulative final outbreak size is covered. The code is an exhaustive *finite* computation for seven vertices or fewer, not an infinite-order theorem. The small expected-burden decrease for Type A is mathematically exact but may have little direct public-health magnitude; the structural first-onset result, not a quantitative policy prediction, is the value asserted.

## References

1. S. A. Ozbay, B. F. Nielsen, M. M. Nguyen, *Bifurcations in the Herd Immunity Threshold for Discrete-Time Models of Epidemic Spread*, arXiv:2212.06995 (first submitted 14 December 2022), https://arxiv.org/abs/2212.06995.
2. K. J. Sharkey, I. Z. Kiss, R. R. Wilkinson, P. L. Simon, *Exact Equations for SIR Epidemics on Tree Graphs*, Bulletin of Mathematical Biology 77 (2015), 614–645, DOI:10.1007/s11538-013-9923-5; accessible version https://researchonline.ljmu.ac.uk/id/eprint/10968/.
3. J. Curran-Sebastian, L. Pellis, I. Hall, T. House, *Calculation of Epidemic First Passage and Peak Time Probability Distributions*, arXiv:2301.07058, https://arxiv.org/abs/2301.07058.
