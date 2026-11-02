# A sharp four-vertex fitness crossover for edge additions in the birth–death Moran process

## Finding
Fix the standard birth–death Moran process on a connected, simple, undirected graph, with one mutant of relative fitness \(r>1\), all other vertices of fitness one, and its starting vertex uniform. Every insertion of one missing edge in a connected graph of order at most four belongs, up to isomorphism, to the classes in the following table. The signs refer to the change in the mutant's fixation probability \(\rho\) after edge insertion.

| Edge insertion | Change for \(r>1\) |
|---|---|
| Four-vertex star \(\to\) paw (triangle with a leaf) | Strictly negative |
| Four-vertex path \(\to\) paw | Negative for \(1<r<r_c\), zero for \(r=r_c\), positive for \(r>r_c\) |
| Four-vertex path \(\to\) four-cycle | Strictly negative |
| Paw \(\to\) diamond (complete graph minus one edge) | Strictly negative |
| Four-cycle \(\to\) diamond | Strictly positive |
| Diamond \(\to\) complete four-vertex graph | Strictly negative |

The critical fitness \(r_c\) is the **unique positive root** of
\[
P(r)=12780r^9+14805r^8-177144r^7-665280r^6-1193573r^5-1412701r^4-1179232r^3-667896r^2-206727r-19404,
\]
with \(4.887<r_c<4.888\) (numerically \(r_c\approx4.8875341047\)). Thus four vertices are necessary and sufficient for an added undirected edge to reverse its effect on uniform-single-mutant fixation as fitness increases. The **qualitative ranking reversal** was observed numerically in earlier work; the finding is the exact cutoff, rigorous uniqueness for all \(r>1\), and the complete classification of all graph-type edge additions through four vertices.

## Assumptions and scope
For each configuration of mutant sites \(S\subseteq V\), a vertex reproduces with probability proportional to fitness, and its offspring replaces one of its neighbors chosen uniformly. All sites are initially residents except one uniformly random mutant. Mutants have constant relative fitness \(r>1\); neither mutation nor migration outside graph edges occurs. Fixation means eventual absorption at the all-mutant state. Only connected simple undirected graphs with two, three, or four vertices and addition of one previously absent edge are classified. The discrete-time selection-normalization common to all transitions cancels from the harmonic equations below.

## Proof
For a nonabsorbing subset \(S\), write \(h(S)\) for its mutant fixation probability and \(d_i\) for the degree of vertex \(i\). The boundary conditions are \(h(\varnothing)=0\) and \(h(V)=1\). Conditioning on a reproduction–replacement step, multiplying by the common total fitness, and cancelling self-transition terms gives the exact finite harmonic equation
\[
\sum_{i\in S,\,j\notin S,\,ij\in E}\frac{r}{d_i}\,[h(S\cup\{j\})-h(S)]
+\sum_{i\notin S,\,j\in S,\,ij\in E}\frac{1}{d_i}\,[h(S\setminus\{j\})-h(S)]=0.
\]
Connectivity makes the fourteen transient equations (for four vertices) uniquely solvable, because both absorbing states are reachable. The required average is \(\rho_G(r)=\tfrac14\sum_{i\in V}h(\{i\})\). Exact rational-function elimination yields, for the path and paw,
\[
\rho_{\mathrm{path}}=\frac{r^3(8r^2+16r+15)}{2(r+1)(2r^2-r+2)(2r^2+5r+6)},
\]
\[
\rho_{\mathrm{paw}}=\frac{r^3 A(r)}{2B(r)},
\]
where the coefficients of \(A\), in descending order, are
\(45360,201204,387108,479847,478953,374117,173451,31584\), and those of \(B\) are
\(22680,123282,310806,530223,751386,866494,751386,530223,310806,123282,22680\).
The other four graph formulas are
\[
\rho_{\mathrm{star}}=\frac{r^3(3r+1)(3r+7)}{(r+3)(3r^2-2r+3)(3r^2+4r+3)},
\]
\[
\rho_{C_4}=\rho_{K_4}=\frac{r^3}{(r+1)(r^2+1)},
\]
\[
\rho_{\mathrm{diamond}}=\frac{r^3(126r^4+447r^3+643r^2+429r+115)}{(r+1)(126r^6+447r^5+761r^4+852r^3+761r^2+447r+126)}.
\]

All six edge-difference rational functions have strictly positive denominators on \(r>1\) (the accompanying exact-arithmetic certificate verifies positivity via coefficient tests after shifting \(r\) by one). Their signed numerators, after removal of positive scalar and \(r^3(r-1)\), are respectively: negative a polynomial \(Q_8\) with strictly positive coefficients; \(P(r)\) as displayed above; \(-(r+9)\); negative a polynomial \(Q_{11}\) with strictly positive coefficients; \(8r^3+32r^2+29r+11\); and its negative. The complete integer coefficient lists for \(Q_8\) and \(Q_{11}\) appear and are checked in `verify.py`; they contain respectively nine and twelve strictly positive coefficients. Therefore the five noncrossover signs in the table are strict.

The polynomial \(P\) has precisely one sign change in its descending coefficient sequence. Descartes' rule of signs gives **at most one** positive zero; \(P(1)<0\), whereas the leading coefficient is positive, so by continuity **exactly one** occurs. Direct exact rational substitution at \(4887/1000\) and \(4888/1000\) proves the stated bracket. Since the difference sign equals the sign of \(P\) for \(r>1\), the crossover is unique and transverse.

There are exactly six connected four-vertex isomorphism classes; considering all missing-edge additions yields exactly the six rows of the table, as established by exhaustive permutation canonicalization and edge enumeration. For three vertices the only edge addition is path \(P_3\) to triangle \(K_3\), whose exact difference is
\[
\rho_{K_3}-\rho_{P_3}=-\frac{r^2(r-1)}{(r+2)(r^2+r+1)(2r^2+r+2)}<0
\qquad(r>1).
\]
On two vertices no connected graph admits an added simple edge. This proves sharp minimality.

## Verification
The standalone `verify.py` (Python 3, SymPy) constructs and independently checks all finite harmonic systems, verifies the six rational functions and sign factorizations with exact symbolic arithmetic, enumerates all connected labeled graph edge additions and canonical isomorphism types for orders two through four, checks all shifted denominator coefficients, and confirms uniqueness and a rational interval for the critical root. The verification program executed successfully. The analytic harmonic equations, positivity factors, Descartes' rule, and graph enumeration yield a proof for every real \(r>1\); finite numerical sampling alone would not.

## Relationship to prior work
Lieberman, Hauert and Nowak (2005) introduced evolutionary graph fixation under the birth–death mechanism. Broom and Rychtář (2008) analyzed special graph families. **Broom, Rychtář and Stadler (2009) explicitly reported a numerical fitness-dependent rank reversal between the four-vertex path (their star with a tail) and paw (their star with an additional leaf–leaf edge). That qualitative observation is prior art, not this finding's novelty.** Their published comparisons use a finite collection of fitness values, not an explicit algebraic fitness boundary and a proof of uniqueness over all \(r>1\). Hindersin and Traulsen (2015) further compare small evolutionary graphs numerically against the complete graph at specified fitnesses. Those comparisons do not themselves imply the complete six-transition all-fitness theorem. Searches and inspection found no established statement of this exact classification; the priority assessment remains provisional, not a claim of exhaustive literature coverage.

## Limitations
This is a finite-network theorem restricted to order at most four, a uniform **single** mutant, **birth–death** (not death–birth) updating, unweighted edges, equal resident fitness, and no mutation. It does not assert a general monotonicity or universal crossover law at larger graph orders. Older literature describing numerical reversals means that the *existence* of qualitative reversals is not new. Some relevant historical full texts were not fully available; an unlocated exact calculation could overlap this classification. No independent audit has been performed.

## References
1. Lieberman, E., Hauert, C., and Nowak, M. A. (2005). Evolutionary dynamics on graphs. *Nature* 433, 312–316. https://doi.org/10.1038/nature03204 (first published 2005-01-20).
2. Broom, M., Rychtář, J. (2008). An analysis of the fixation probability of a mutant on special classes of non-directed graphs. *Proc. R. Soc. A*. https://doi.org/10.1098/rspa.2008.0058 (bibliographic/abstract comparison; complete text not inspected).
3. Broom, M., Rychtář, J., Stadler, B. T. (2009). Evolutionary dynamics on small-order graphs. *Journal of Interdisciplinary Mathematics*. https://doi.org/10.1080/09720502.2009.10700618 (open-access full text inspected).
4. Hindersin, L., and Traulsen, A. (2015). Most undirected random graphs are amplifiers of selection for birth-death dynamics, but suppressors of selection for death-birth dynamics. *PLOS Computational Biology*. https://doi.org/10.1371/journal.pcbi.1004437 (full-text methods/results inspected).
