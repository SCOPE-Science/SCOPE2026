# A five-vertex threshold for polarization-increasing links in anchored opinion networks

## Finding

For the homogeneous-anchoring Friedkin–Johnsen opinion model on a finite connected simple undirected unweighted graph, with binary innate opinions, adding one missing edge cannot increase equilibrium polarization if the graph has at most four vertices, for **any** positive common anchoring weight. The bound is sharp at five vertices, even when the original graph is a path.

More precisely, let \(P_G(a)\) be the sum of squared deviations of equilibrium expressed opinions from their mean, for a common anchoring weight \(a>0\), and let \(\Delta(a)=P_{G+e}(a)-P_G(a)\) for one nonedge \(e\). Then \(\Delta(a)\leq 0\) whenever \(|V(G)|\leq4\) and innate opinions belong to \(\{0,1\}^{V(G)}\).

For five vertices \(V=\{0,1,2,3,4\}\), take the path with edge set
\[
E(G)=\{01,04,12,23\},\qquad e=02,\qquad s=(0,0,1,0,1)^{\mathsf T}.
\]
Here \(01\) denotes the undirected edge joining vertices \(0\) and \(1\), and similarly for the other edge labels. The polarization difference is exactly
\[
\boxed{\Delta(a)=\frac{-2a^3(a^4+4a^3-7a-3)}{(a^2+3a+1)^2(a^2+5a+3)^2}.}
\]
There is a **unique** crossover \(a_*\in(1,2)\), the positive root of \(a^4+4a^3-7a-3=0\), with \(a_*\approx 1.32018042507931\). The new edge **increases** polarization for \(0<a<a_*\), has no effect at \(a=a_*\), and **decreases** polarization for \(a>a_*\). In particular,
\[
\Delta(1)=\frac{2}{405}>0,\qquad \Delta(2)=-\frac{496}{34969}<0.
\]
Thus an added positive social tie need not make equilibrated opinions less dispersed, and the direction of its effect can reverse as the relative strength of innate anchoring changes.

## Assumptions and scope

All graphs here are finite, simple, connected, undirected and unweighted. Every vertex has one fixed innate opinion \(s_i\in\{0,1\}\), unchanged when the edge is added. Each vertex simultaneously updates its expressed opinion by
\[
x_i(t+1)=\frac{a s_i+\sum_{j\sim_G i}x_j(t)}{a+\deg_G(i)},\qquad a>0.
\]
Because every denominator is positive and each row has strictly positive innate weight, the dynamics have a unique attracting equilibrium \(z_G(a)\). Writing \(L_G\) for the combinatorial Laplacian and \(I\) for the identity, the equilibrium solves
\[
(aI+L_G)z_G(a)=a s,\quad z_G(a)=a(aI+L_G)^{-1}s.
\]
The equilibrium mean is the innate mean: \(\overline z=\overline s\), because \(\mathbf1^{\mathsf T}L_G=0\). Defining \(C=I-\mathbf1\mathbf1^{\mathsf T}/n\), polarization is
\[
P_G(a)=z_G(a)^{\mathsf T}Cz_G(a).
\]
Polarization is the **sum**, not the average, of squared deviations; dividing by \(n\) leaves every sign unchanged. We compare two graphs at the same \(a\) and with the same innate vector. We make no claim for arbitrary real-valued innate opinions, unequal anchoring weights, directed or signed networks, or multiple link changes.

## Proof

**Step 1: exact rational certificate.** Set \(M=aI+L_G\), \(N=aI+L_{G+e}\), \(k=\det M\), \(h=\det N\), and \(u=\operatorname{adj}(M)s\), \(v=\operatorname{adj}(N)s\). Substitution gives
\[
\Delta(a)=\frac{a^2}{k^2h^2}\bigl(k^2v^{\mathsf T}Cv-h^2u^{\mathsf T}Cu\bigr).
\]
The bracket is a polynomial in \(a\) with rational coefficients. Since \(L_G\) and \(L_{G+e}\) are positive semidefinite and \(a>0\), both determinants are strictly positive; hence the sign of \(\Delta\) is the sign of the bracket. A polynomial all of whose coefficients are nonpositive is nonpositive on the positive half-line.

**Step 2: exhaustive lower bound, with reproducible exact finite proof.** The accompanying `verify.py` enumerates every connected unlabeled simple graph on \(n=2,3,4\) vertices by examining every labeled edge mask and taking the minimum relabeled mask under all vertex permutations. For each graph it examines every missing edge and every binary innate assignment up to complementation. Complementation is valid because \(z_G(a;\mathbf1-s)=\mathbf1-z_G(a;s)\), and consequently both polarizations and their difference are unchanged. Thus it suffices to set the zeroth innate bit to zero; the all-zero assignment is trivial.

For each nontrivial decorated case the verifier calculates the bracket polynomial in Step 1 using exact symbolic adjugates and determinants and asserts that **every** coefficient is nonpositive. It covers one connected unlabeled graph at \(n=2\), two at \(n=3\), and six at \(n=4\); the respective nontrivial graph–edge–opinion comparisons number \(0,3,77\). Among the \(80\) comparisons, \(58\) certificates are nonzero and \(22\) vanish identically. At \(n=1\) or connected \(n=2\), no missing edge exists. The complete enumeration and strictly algebraic coefficient tests establish the bound **for all real \(a>0\)** rather than at sampled values. The executable source is the finite proof certificate; numerical test output alone is not relied on as proof.

**Step 3: sharp witness and unique crossover.** Apply the same matrix formula to the specified five-vertex path and shortcut. Exact symbolic simplification yields the displayed rational expression for \(\Delta\). Each denominator factor is strictly positive for \(a>0\), so the sign is the opposite of
\[
F(a)=a^4+4a^3-7a-3.
\]
The descending nonzero coefficient signs of \(F\) are \(+,+,-,-\); Descartes' rule of signs gives **at most one positive root**. Because \(F(1)=-5<0\) and \(F(2)=31>0\), there is exactly one positive root \(a_*\in(1,2)\). Continuity and the absence of further positive roots prove all asserted strict intervals and the values at \(a=1,2\). The limiting responses \(\Delta(a)/a^3\to2/3\) as \(a\downarrow0\) and \(a\Delta(a)\to-2\) as \(a\to\infty\) also follow from the exact formula.

## Verification

Run `python verify.py` with Python 3 and SymPy 1.10 or later. The program constructs every enumerated graph internally, forms exact integer or rational matrices, checks the sign of every coefficient in the \(80\) finite certificates, reconstructs the five-vertex rational identity independently from matrix inverses, verifies two rational test points, and counts positive roots exactly. A successful run ends with `PASS` and prints the graph and comparison counts. No downloaded tables, data files, numerical tolerances, or external services are needed. The calculation of the root approximation is not needed for the proof.

## Relationship to prior work

The anchored opinion update is a specialization of the established Friedkin–Johnsen framework; convergence and multidimensional variants are studied by Parsegov, Proskurnikov, Tempo and Friedkin (2015, arXiv:1505.04920). Zhu, Bao and Zhang (2021) analyze minimizing **polarization plus graph disagreement** by link addition. Their monotonicity statement for the combined objective does **not** imply monotonicity of polarization alone, which is the quantity studied here.

Bhalla, Lechowicz and Musco (arXiv:2111.14020, initially public in 2021) develop edge-update analyses for polarization; their readily accessible abstract establishes that broad single-edge changes are prior knowledge. The full text could not be examined sufficiently to rule out an equivalent minimal-order statement, so a covering theorem under different terminology remains a bibliographic risk. The present claim is specifically the **sharp five-vertex threshold under binary innate opinions and a common positive anchoring weight**, plus an exact path witness with a **unique** anchoring-dependent reversal; it does not claim novelty for the FJ equilibrium formula or the qualitative possibility of edge-induced polarization in larger networks.

## Limitations

The lower bound is a finite, exhaustive certificate in the specified mathematical model; it is not a general graph-theoretic monotonicity theorem beyond four vertices. The five-vertex construction establishes existence, not a classification of all five-vertex witnesses. Results depend on homogeneous positive anchoring, binary innate opinions, simple unweighted undirected graphs, and the centered squared-deviation statistic. They do not validate empirical social behavior. Literature access was incomplete for a particularly relevant edge-dynamics paper, and an equivalent earlier theorem cannot be categorically excluded without further independent bibliographic examination. No independent scientific audit has been performed.

## References

1. S. E. Parsegov, A. V. Proskurnikov, R. Tempo and N. E. Friedkin, *Novel Multidimensional Models of Opinion Dynamics in Social Networks*, arXiv:1505.04920, first submitted 19 May 2015. https://arxiv.org/abs/1505.04920
2. L. Zhu, Q. Bao and Z. Zhang, *Minimizing Polarization and Disagreement in Social Networks via Link Recommendation*, NeurIPS 2021. https://papers.nips.cc/paper_files/paper/2021/file/101951fe7ebe7bd8c77d14f75746b4bc-Paper.pdf
3. N. Bhalla, A. Lechowicz and C. Musco, *Local Edge Dynamics and Opinion Polarization*, arXiv:2111.14020, first submitted 28 November 2021. https://arxiv.org/abs/2111.14020
4. F. Biondi and collaborators, *Dynamics of Opinion Polarization*, arXiv:2206.06134 (2022). https://arxiv.org/abs/2206.06134
