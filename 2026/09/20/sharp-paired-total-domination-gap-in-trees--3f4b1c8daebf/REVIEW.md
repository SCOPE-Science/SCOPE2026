# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** Chellali--Haynes give
\(\gamma_{\mathrm{pr}}(T)-\gamma_t(T)\le s(T)-1\), where \(s(T)\) is the
number of support vertices. Since distinct supports have distinct leaf
neighbors, \(s(T)\le\lfloor n/2\rfloor\). For odd order this already gives
the claimed bound. For even order, the only potentially larger case is
\(s=n/2\); such a tree is exactly a corona \(H\circ K_1\), and the exact
identity
\[
\gamma_{\mathrm{pr}}(H\circ K_1)=2|V(H)|-2\nu(H)
\]
forces one further unit of improvement because a connected \(H\) has a
nonempty matching.

The equality analysis was checked adversarially. In the odd case, parity
excludes an extra leaf and any edge joining two support vertices would
produce a paired-dominating set two vertices smaller; connectedness then
forces the unique subdivided star. In the even case, \(s=n/2\) reduces to a
corona and equality forces the core matching number to be one, hence a star.
When \(s=n/2-1\), parity fixes both domination parameters, edges among
supports are again excluded by a smaller paired set, and a minimum total
dominating set forces one of the two remaining vertices to be adjacent to
all supports; the other is necessarily the single extra leaf. This gives
exactly the second extremal family.

A standalone exhaustive verifier recomputes both parameters and agrees with
the theorem and the complete isomorphism classification for every
nonisomorphic tree of orders two through twelve.

## Originality

**PASS, to the best of our knowledge.** The foundational 1998 paired-
domination paper, the 2004 total-versus-paired tree paper, the 2006 equality
characterization, the 2020 survey chapter metadata/abstract, the 2022
paired-domination-in-trees paper, and recent 2026 work on algorithms and
random trees were checked at the level available from the cited sources.
Exact and synonymous searches for a fixed-order maximum of
\(\gamma_{\mathrm{pr}}-\gamma_t\), paired-versus-total domination gaps in
trees, support-vertex equality cases, subdivided-star extremizers, and corona
formulations did not locate the stated order-only formula or the odd/even
classification.

The originality risk is nonzero. The numerical upper bound is close to the
2004 support-sensitive inequality, so a short equivalent corollary may have
appeared under different terminology. The 2020 Springer survey chapter was
not inspected in full, and the 2004 article was not read end-to-end, although
its relevant support-sensitive theorem is explicitly stated in accessible
abstract/indexed material. These are the most plausible sources for prior
coverage among those identified.

## Value

**PASS.** The result turns a support-sensitive comparison into an exact
fixed-order extremum, identifies a parity effect that improves the naive
even-order consequence by one, and classifies every extremal tree. The
corona identity isolates the matching-theoretic mechanism responsible for
the even case and may be reusable in other domination comparisons.

## Scientific limitations

- The theorem concerns finite simple trees only; no corresponding extremum
  over all connected graphs is claimed.
- The main order bound builds on an established 2004 inequality; the new
  content claimed here is the exact fixed-order optimization, parity
  refinement, sharpness for every order, and complete extremal
  classification.
- The 2020 survey chapter was not inspected in full and the 2004 article was
  not read end-to-end; differently indexed prior coverage remains possible.
- Finite exhaustive verification supports but does not replace the proof.

## Sources checked

- T. W. Haynes, P. J. Slater, *Paired-domination in graphs*, Networks 32
  (1998), 199--206.
- M. Chellali, T. W. Haynes, *Total and paired-domination numbers of a tree*,
  AKCE International Journal of Graphs and Combinatorics 1(2) (2004),
  69--75.
- M. A. Henning, *Trees with equal total domination and paired-domination
  numbers*, Utilitas Mathematica 69 (2006).
- W. J. Desormeaux, T. W. Haynes, M. A. Henning, *Paired Domination in
  Graphs*, in *Topics in Domination in Graphs* (2020), 31--77.
- A. Gorzkowska, M. A. Henning, M. Kleszcz, M. Pilśniak, *Paired Domination
  in Trees*, Graphs and Combinatorics 38 (2022), 129.
- D. Ralaivaosaona, M. A. Henning, *Paired domination in trees: A linear
  algorithm and asymptotic normality* (posted 4 August 2026).
