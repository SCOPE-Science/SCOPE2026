# Binomial cell enumeration for oriented-triangle Hom complexes of cyclic tournaments

## Finding
For every integer \(m\geq 1\), put \(n=2m+1\) and let \(R_n\) be the standard cyclic tournament on \(\mathbb Z/n\mathbb Z\), oriented by \(a\to b\) exactly when \(1\leq(b-a)\bmod n\leq m\). Let
\[
X_m=\operatorname{Hom}(\overrightarrow C_3,R_n)
\]
be the **directed regular polyhedral Hom complex**, not a directed flag complex. Its cells are triples of nonempty vertex sets \((A,B,C)\) such that \(A\times B\), \(B\times C\), and \(C\times A\) all consist of directed arcs; the cell is \(\Delta^A\times\Delta^B\times\Delta^C\) and has dimension \(|A|+|B|+|C|-3\).

The **complete cellular face polynomial** is
\[
\boxed{\sum_{q\geq0}f_q(X_m)t^q
=(2m+1)\binom{m+1}{2}(1+t)^{m-1}.}
\]
Consequently \(\dim X_m=m-1\), and for \(0\leq q\leq m-1\),
\[
f_q(X_m)=(2m+1)\binom{m+1}{2}\binom{m-1}{q}.
\]
The target-translation group \(C_n\) acts freely on the **set of cells**, hence the quotient has exactly \(\binom{m+1}{2}\binom{m-1}{q}\) cells of dimension \(q\). For \(m\geq2\), \(\chi(X_m)=\chi(X_m/C_n)=0\), and therefore neither complex is contractible. At \(m=1\), \(X_1\) consists of three points, and its quotient consists of one point.

## Assumptions and scope
All graphs are finite loopless digraphs. The source is the oriented triangle with arcs \(A\to B\to C\to A\), where the displayed letters refer to its three **ordered** vertices. Distinct cells are not identified under source rotation. The \(f\)-polynomial counts cells of the original product-of-simplices CW structure, **not simplices in its barycentric subdivision**. The quotient cell count refers to the cellular orbit decomposition; no claim is made that this quotient decomposition is a regular CW structure.

## Proof
**1. Unique cyclic block order.** For any allowed triple of individual vertices \(a\in A,b\in B,c\in C\), the positive clockwise arc lengths \(p=b-a\), \(q=c-b\), and \(r=a-c\), each taken modulo \(n\), are all in \(\{1,\ldots,m\}\). Their sum is a positive multiple of \(n\), but is at most \(3m<2n\); hence it equals \(n\). Thus the cyclic order of every triple of labels is \(A,B,C\), and the three sets are disjoint. Fixing one \(a\in A\), all \(B\)-labels precede all \(C\)-labels in a clockwise scan starting at \(a\). The cyclic-order condition on triples with other \(A\)-labels prevents any \(A\)-label from lying strictly between a \(B\)-label and a \(C\)-label. It follows that, allowing unused vertices, all selected labels occur in a unique cyclic sequence of an \(A\)-block, a \(B\)-block, and a \(C\)-block. In particular there is a unique *anchor*, the first selected \(A\)-vertex encountered immediately after the \(C\)-block when scanning clockwise. There are exactly \(n\) possible anchors.

**2. Six nonnegative parameters.** Let \(u,v,w\geq0\) be the clockwise widths, in edges, from first to last selected vertices of the \(A,B,C\) blocks. Let \(p,q,r\geq1\) be the clockwise distances from last \(A\) to first \(B\), last \(B\) to first \(C\), and last \(C\) back to first \(A\). Then
\[
u+v+w+p+q+r=2m+1.
\]
The defining *all-to-all* arcs are equivalent to
\[
u+v+p\leq m,\quad v+w+q\leq m,\quad w+u+r\leq m.
\]
Define the three nonnegative slacks
\[
i=m-u-v-p,\quad j=m-v-w-q,\quad k=m-w-u-r.
\]
Adding gives
\[
\boxed{u+v+w+i+j+k=m-1.}
\]
Conversely **every** six-tuple of nonnegative integers satisfying this equation gives positive cyclic gaps
\[
p=1+w+j+k,\quad q=1+u+i+k,\quad r=1+v+i+j,
\]
so reconstructs unique extremal block positions from the anchor. The only remaining choices are whether each interior vertex of a nontrivial block is selected. This establishes a bijection for all \(m\geq1\), including the boundary case \(m=1\).

**3. Weighted enumeration.** Assign a variable \(s\) to each selected target vertex. A block of width zero has weight \(s\). A block of width \(u\geq1\) has two mandatory selected endpoints and \(u-1\) optional interiors, so weight \(s^2(1+s)^{u-1}\). The width generating function is therefore
\[
W(z,s)=s+\sum_{u\geq1}s^2(1+s)^{u-1}z^u
=\frac{s(1-z)}{1-(1+s)z}.
\]
The three independent nonnegative slacks contribute \((1-z)^{-3}\). Dividing by \(s^3\) changes selected-vertex degree to cellular dimension. Hence
\[
\begin{aligned}
\sum_{q\geq0} f_q(X_m)s^q
&=n s^{-3}[z^{m-1}]\,W(z,s)^3(1-z)^{-3}\\
&=n[z^{m-1}](1-(1+s)z)^{-3}\\
&=n\binom{m+1}{2}(1+s)^{m-1}.
\end{aligned}
\]
All coefficients are nonnegative, and the top coefficient is positive, establishing the dimension formula.

**4. Target rotations and Euler characteristic.** Rotating all three sets by any target translation rotates the unique anchor by the same amount. A nonidentity translation cannot fix an anchor, so the group action has no stabilizer on any cell. Every orbit has \(n\) cells, proving the quotient formula. For \(m\geq2\), substituting \(s=-1\) in the proved polynomial gives \(\chi(X_m)=0\); the quotient likewise has Euler characteristic zero. A nonempty finite contractible CW complex has Euler characteristic one, proving noncontractibility. For \(m=1\), the polynomial is three, agreeing with the three cyclic automorphisms of \(\overrightarrow C_3\).

## Verification
The self-contained standard-library program `verify.py` enumerates the defining triples of nonempty subsets directly by bitmasks, without using the six-parameter counting formula. For each odd target size from three through nineteen it independently compares the exact cell counts against (i) the binomial closed formula and (ii) a separate enumeration of the six-parameter model. For orders through fifteen it verifies uniqueness of the cyclic anchor for every enumerated cell and checks every nonidentity target translation against every cell. All tested cases passed. Actual output appears in `verify_output.txt`, ending `CYCLIC_TOURNAMENT_HOM_CELL_POLYNOMIAL_VERIFIED`. These finite tests cross-check the proof; **the all-order assertion follows from the symbolic bijection**, not extrapolation.

## Relationship to prior work
Dochtermann and Singh introduced the directed Hom construction and studied tournament targets, including examples of oriented-triangle Hom complexes and a general contractibility result for **transitive** target tournaments. Their Section 7.2 explains why the dimension of \(\operatorname{Hom}(\overrightarrow C_3,H)\) matters for equivariant obstruction arguments. The present theorem gives an exact formula for **all cellular dimensions** in the standard cyclic targets, and in particular demonstrates noncontractibility uniformly for those nontransitive targets. Their general transitive-target theorem does not imply this formula.

The previously published exact computation of \(\operatorname{Hom}(\overrightarrow C_3,R_9)\) gives its specific cell vector \((90,270,270,90)\) and homotopy type \(S^1\). The cell vector is recovered by setting \(m=4\), and is acknowledged as **covered prior numerical information**, not presented as novel here. That finite computation explicitly does not give a formula for all cyclic tournaments. The new result is the universal six-parameter correspondence, binomial polynomial, and free cellular target-rotation orbit counts. Research on the cyclic tournament's directed-path homology concerns a different chain complex and does not imply these regular-cell counts.

## Limitations
The theorem is an exact all-order **cell enumeration and Euler-characteristic classification**, not a homotopy or homology classification. Euler characteristic zero alone does not prove the space has the homotopy type of a circle, nor determine its fundamental group or torsion. In particular the known circle homotopy type for the nine-vertex target is not generalized here. The quotient's cell counts do not assert a regular quotient CW structure. Literature searching and comparison with an accessible closest published record found no all-order covering formula; independently unindexed equivalent results remain possible and no independent audit has been performed.

## References
1. A. Dochtermann and A. Singh, *Homomorphism complexes, reconfiguration, and homotopy for directed graphs*, European Journal of Combinatorics 110 (2023), article 103704; first public version arXiv:2108.10948v1 (24 August 2021); full open text https://arxiv.org/html/2108.10948v2, especially Sections 2.4, 5 and 7.2.
2. *The directed Hom complex \(\operatorname{Hom}(\overrightarrow C_3,R_9)\) has the homotopy type of a circle*, public mathematical record (2026), https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-the-directed-hom-complex-operatorname-hom-overrightarrow-c-3-r-9--879b51cbdd1a ; the finite cell vector and proof were read in its `RESULT.md`.
3. S. Savchenko, *On the number of 8-cycles for two particular regular tournaments of order N with diametrically opposite local properties*, arXiv:2403.07629 (2024); background for the alternative name *regular locally transitive tournament*, not a statement about directed Hom complexes.
