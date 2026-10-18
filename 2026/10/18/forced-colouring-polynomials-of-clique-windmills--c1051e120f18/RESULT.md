# Forced-colouring polynomials of clique windmills

## Finding
For all integers \(k,m\ge2\), consider the clique windmill (or generalized friendship graph)
\[
W_{k,m}=K_1\vee(kK_m),
\]
where the lone vertex is the *hub* and the \(k\) disjoint cliques of size \(m\) are *blades*. Fix the named palette \(\{1,\ldots,q\}\), with \(q=m+1=\chi(W_{k,m})\). A partial vertex colouring is **forced** when repeatedly colouring any blank vertex whose coloured neighbours exhibit exactly \(q-1\) distinct colours eventually colours all vertices properly. Let \(f_s(W_{k,m};q)\) count all initially forced partial assignments with exactly \(s\) precoloured vertices. Then
\[
\boxed{\sum_{s=0}^{km+1}f_s(W_{k,m};q)x^s
=(m+1)(m!)^k x^{k(m-1)}\left((1+x)(m+x)^k-m\right).}
\]
In particular, the minimum successful seed size and its exact multiplicity are
\[
\boxed{k(m-1)\quad\text{and}\quad(m+1)(m!)^k(m^k-m),}
\]
respectively. With independent initial vertex labels, a particular named colour has probability \(p\) and an uncoloured vertex has probability \(u=1-(m+1)p\). The associated forced-colouring probability polynomial is
\[
\boxed{\mathrm{FC}_{m+1}(W_{k,m};p)
=(m+1)(m!)^k p^{k(m-1)}\left((p+u)(mu+p)^k-mu^{k+1}\right),\quad 0\le p\le\frac1{m+1}.}
\]

## Assumptions and scope
All graphs are finite, simple, and undirected; \(k,m\) are arbitrary integers at least two. A partial assignment consists of either one of the \(q\) named colours or a blank at each vertex. Initially adjacent nonblank vertices must have different colours. At any stage a blank vertex can be forced only if the set of colours on its already coloured neighbours has cardinality exactly \(q-1\); the forced colour is the unique missing one. A successful partial assignment is one that can be completed by such steps. This notion is distinguished from ordinary zero forcing and from the existence of a unique proper-colouring extension without a local forcing sequence. The cardinality enumerator counts assignments, not colour-isomorphism classes.

## Proof
**1. Mandatory local seeds.** If a blade begins with at least two blank vertices, neither can ever be forced, regardless of what happens at the hub or in the other blades. Indeed, each sees at most \(m-2\) initially coloured neighbours in its own blade and at most one hub neighbour. So it sees at most \(m-1=q-2\) colours, strictly fewer than the requisite \(q-1=m\). No vertex in that blade can be the first of its initially blank vertices to be forced. Consequently every successful initial configuration has at least \(m-1\) coloured vertices in each blade.

**2. Characterization with a coloured hub.** Suppose the hub is initially coloured and every blade has at most one blank vertex. For an initially proper partial assignment extending to a proper full colouring, any blank blade vertex sees its coloured hub and the \(m-1\) coloured neighbours in that blade in \(m\) distinct colours, so it is forced immediately. Conversely, the necessity proved above excludes all configurations with fewer coloured blade vertices.

**3. Characterization with a blank hub.** Before the hub is coloured no blank blade vertex can be forced: it sees at most its \(m-1\) blade neighbours, fewer than the \(m\) required distinct colours. Hence the first forcing step must colour the hub. Given an extension to a full proper \(q\)-colouring, the hub can be forced precisely when its initially coloured neighbours display all the \(m\) colours different from its eventual colour. If this holds, forcing the hub then forces all remaining blade vertices by step 2. If it does not hold, no first move exists, and forcing fails.

For each fixed full proper colouring, a blade has exactly \(m\) colours among its vertices, one occurrence of each colour other than the hub colour. If the hub starts blank, the only failing seed patterns *among patterns with at most one blank per blade* are those where every blade has exactly one blank, and all these omitted leaves carry the same colour. There are exactly \(m\) such patterns for each full proper colouring.

**4. Enumeration without multiple-counting.** The hub has \(m+1\) possible full colours, and conditional on the hub colour each blade admits an independent permutation of the remaining \(m\) colours, so there are exactly \((m+1)(m!)^k\) full proper colourings. For a fixed one, the possible seed sets preserving at least \(m-1\) coloured vertices per blade contribute the blade polynomial \(mx^{m-1}+x^m\). A coloured hub contributes
\[
x(mx^{m-1}+x^m)^k.
\]
A blank hub contributes
\[
(mx^{m-1}+x^m)^k-mx^{k(m-1)},
\]
because the last term counts the \(m\) simultaneous same-colour omissions just identified. Every successful initial partial assignment has exactly one full colouring obtainable by forcing: each step chooses a uniquely determined colour. Thus each successful partial assignment is counted once when summing over full proper colourings, even though failing partial assignments might have several proper extensions. Multiplying by \((m+1)(m!)^k\) and factoring gives the claimed cardinality enumerator.

**5. Probability and minimum.** In the independent initial-label model, an assignment on \(s\) vertices with total graph order \(km+1\) has probability \(p^su^{km+1-s}\). Substitute this into the cardinality enumerator, or repeat the seed-set count with weights \(p\) for coloured and \(u\) for blank, to obtain the stated probability polynomial. The smallest possible power in the enumerator is \(k(m-1)\), whose coefficient is
\[
(m+1)(m!)^k(m^k-m)>0
\]
for every \(k,m\ge2\). This proves sharpness. More explicitly, let the hub initially be blank, omit one vertex per blade, and choose the omitted full-colour classes to differ in at least two blades; the hub is then forced and the remaining vertices follow.

For completeness, writing \(s=k(m-1)+r\), the coefficient for \(0\le r\le k+1\) equals
\[
f_s=(m+1)(m!)^k\left(\binom{k}{r}m^{k-r}
+\binom{k}{r-1}m^{k-r+1}-m\mathbf1_{\{r=0\}}\right),
\]
where out-of-range binomial coefficients are zero; for all other \(s\) it vanishes.

## Verification
The dependency-free Python file `windmill_forcing_verify.py` independently enumerates every partial assignment, tests the local forcing process using graph adjacency, and compares the resulting cardinality counts with the closed formula. It has exhaustively checked seven small parameter pairs, including \((k,m)=(4,2)\) and \((2,3)\), totalling \(366142\) distinct initial assignments, without discrepancies. It additionally verifies explicit minimal-size forcing configurations for all \(2\le k,m\le7\). For example, the polynomial for \((k,m)=(2,2)\) is
\[
24x^2+96x^3+60x^4+12x^5,
\]
and for \((k,m)=(2,3)\) it is
\[
864x^4+2160x^5+1008x^6+144x^7.
\]
Run `python windmill_forcing_verify.py` from a directory containing the standalone file. These finite checks are corroboration only; the proof above establishes all integer parameters.

## Relationship to prior work
Farr introduced and developed the forced-colouring function in *The forced colouring function of a graph* (first public preprint September 15, 2026), including a complete-graph evaluation, simple-graph examples, and general complexity results [1]. Farr and Morgan previously proposed the forced-colouring polynomial framework and studied general polynomial representations [2]. The theorem here specializes the same forcing rule to the infinite clique-windmill family, for which the globally shared hub introduces cross-blade constraints not captured by multiplying isolated clique formulas. Ordinary graph zero-forcing polynomials and geometric/dissociation polynomials on windmills use different definitions and do not establish this enumeration.

## Limitations
The theorem concerns only the chromatic palette size \(q=m+1\), not arbitrary larger palettes, and only clique windmills with at least two blades and at least two vertices per blade. It counts labelled initial assignments and associated forcing probabilities; it does not describe independent computational hardness reductions, robustness to nonstandard forcing rules, or minimum-length forcing sequences. The originality comparison is necessarily limited to material inspected and discoverable bibliographic records; an unindexed equivalent may exist.

## References
[1] G. E. Farr, *The forced colouring function of a graph*, arXiv:2609.17108v1 (first public September 15, 2026), https://arxiv.org/abs/2609.17108 .

[2] G. E. Farr and K. Morgan, *Graph polynomials: some questions on the edge*, arXiv:2406.15746v1 (2024), https://arxiv.org/abs/2406.15746 .
