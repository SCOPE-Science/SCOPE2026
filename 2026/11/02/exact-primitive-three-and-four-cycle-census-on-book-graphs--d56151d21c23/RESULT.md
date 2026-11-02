# Exact primitive three- and four-cycle census on book graphs

## Finding
For every integer \(m\ge1\), let \(B_m=K_2\vee\overline K_m\), with two distinct labelled central vertices \(u,v\), and \(m\) distinct labelled peripheral vertices. This is the graph of \(m\) triangles sharing the edge \(uv\). Under standard loopless, synchronous degree-threshold parallel chip-firing, let \(N_q(m)\) count distinct primitive periodic orbits of least period \(q\), counted once per orbit rather than once per state. Then
\[
N_3(m)=m2^{m+1},\qquad N_4(m)=m(m-1)2^{m-1}.
\]
In particular, primitive four-cycles first appear for \(m=2\), and
\[
\frac{N_4(m)}{N_3(m)}=\frac{m-1}{4}.
\]
Thus the counts are equal exactly at \(m=5\), with three-cycles more numerous at \(1\le m\le4\) and four-cycles more numerous for \(m\ge6\). These are counts over *all* nonnegative integer periodic chip configurations, without restricting the conserved total chip count.

## Assumptions and scope
Each vertex \(w\) holds a nonnegative integer \(x_w\). At each integer time it fires if and only if \(x_w\ge d_w\), sending one chip along each incident edge simultaneously; otherwise it waits. Write \(F\) for the update. The hub degrees are \(D=m+1\); each peripheral degree is \(2\). A primitive \(q\)-cycle is an orbit of length exactly \(q\) under \(F\), so it contains \(q\) distinct chip configurations. Hub labels and all peripheral labels are fixed; graph automorphisms are *not* quotiented out. The only periods enumerated here are \(q=3\) and \(q=4\). Neither a maximal-period claim nor a claim about all transients is made.

## Proof
**Periodic firing and confinement.** For any periodic orbit of length \(q\), let \(f_w(t)\in\{0,1\}\) indicate firing at phase \(t\). Summing the update over the period gives \(L\sum_{t=0}^{q-1} f(t)=0\), where \(L\) is the connected graph Laplacian. Thus every vertex fires an identical number \(k\) of times in the period. For a primitive orbit of length greater than one, \(1\le k\le q-1\). Such a periodic configuration is confined to \(0\le x_w\le2d_w-1\): if a vertex fires at any phase, its following height is at most \(d_w-1+d_w=2d_w-1\) once its height has previously been below \(d_w\), and every vertex in a nonconstant periodic firing word has a waiting phase. This is also the confined-state lemma of Jiang [2].

For a proposed periodic binary firing word at each vertex, define \(c_w(t)=\sum_{z\sim w}f_z(t)\) and \(\Delta_w(t)=\sum_{s=0}^{t-1}(c_w(s)-d_w f_w(s))\), with \(\Delta_w(0)=0\). The number of possible initial heights realizing the proposed word is exactly
\[
\max\left(0,1+\min\left(2d_w-1,\min_{f_w(t)=0}(d_w-1-\Delta_w(t))\right)-\max\left(0,\max_{f_w(t)=1}(d_w-\Delta_w(t))\right)\right).
\]
This follows by intersecting the firing and waiting threshold inequalities. It provides an alternative completely finite recipe for all calculations below.

**One-fire phase lemma.** Suppose \(k=1\) and let \(a_w\in\mathbb Z/q\mathbb Z\) be the unique phase at which \(w\) fires. Since between consecutive firings the height increases by a nonnegative number of incoming chips, the only nonredundant constraints on its height are that it is below threshold immediately before its firing and at least threshold at its firing. The exact number of permissible heights of vertex \(w\) is therefore the number of its neighbors with firing phase \(a_w-1\). Multiplication over vertices gives the exact number of configurations with the fixed firing-phase assignment.

**Three-cycles.** For \(q=3\) and \(k=1\), the central vertices must have different firing phases: if both fire at phase \(a\), each peripheral may only fire at phase \(a+1\), leaving both centers without a neighbor firing at \(a-1\). There are six ordered assignments of two distinct central phases. For any such assignment, each labelled peripheral must fire at one of the two successor phases; let \(j\) of them take one of these phases. The phase lemma yields a product of central height choices equal to \(j\) or \(m-j\), while every peripheral has exactly one allowable height. Summing over the \(2^m\) choices gives \(\sum_{j=0}^m\binom mj j=m2^{m-1}\) (or the symmetric sum). Hence the number of three-periodic *states* in the \(k=1\) class is \(6m2^{m-1}\).

On the confined strip, the involution \(x_w\mapsto2d_w-1-x_w\) commutes with the update and exchanges firing with waiting. It bijects the \(k=1\) and \(k=2\) three-cycle states. Since a three-periodic state in either class cannot have period one, the primitive three-cycle count is
\[
N_3(m)=\frac{2\cdot6m2^{m-1}}3=m2^{m+1}.
\]

**Four-cycles with one firing per vertex.** For \(q=4\), \(k=1\), each peripheral must fire in the phase immediately after one of the central vertices. If the two central firing phases coincide or are adjacent on the four-phase clock, the one-fire phase lemma leaves at least one center without a predecessor-phase firing neighbor; therefore those assignments contribute zero. The two central phases must be antipodal. There are four ordered antipodal assignments (including temporal rotations). Assign \(j\) peripheral vertices to fire after one center and \(m-j\) after the other. Each peripheral has one possible chip height; the respective central height multiplicities are \(j\) and \(m-j\). Each antipodal assignment therefore contributes
\[
\sum_{j=0}^m\binom mj j(m-j)=m(m-1)2^{m-2}.
\]
The total \(k=1\) four-periodic state population is \(4m(m-1)2^{m-2}\), and the chip-complement involution provides the same number in the \(k=3\) class.

**No primitive four-cycles with two firings per vertex.** A two-one binary word of length four either alternates (\(1010\) or \(0101\)) or has two cyclically consecutive ones (a rotation of \(1100\)). Suppose a center has word \(1100\). Write \(c_t\) for its number of firing neighbors in phase \(t\). The constraints that it fires at phases \(0,1\) but waits at phases \(2,3\) imply that its phase-zero chip height \(h\) satisfies \(h\ge2D-c_0\) and \(h<D+c_3\). Thus \(c_0+c_3>D=m+1\) is necessary.

There are six possible two-one words of the second center. The peripheral degree-two update \(y\mapsto y+f_u+f_v-2\mathbf1_{y\ge2}\), inspected over four phases, gives: if the second-center word is respectively \(1100,1010,1001,0110,0101,0011\), the respective upper bounds on \(c_0+c_3\) are \(1,m+1,m+2,m,m+1,m+1\). Every bound is at most \(D\) except the \(1001\) case. In that exceptional case, obtaining more than \(D\) requires every peripheral to have firing word \(1100\); but then the second center has zero firing neighbors in both phases \(2\) and \(3\). The analogous necessary condition for its consecutive firings at phases \(3,0\), namely \(c'_2+c'_3>D\), fails. Therefore neither center can have consecutive firings. Both centers must alternate. Their combined drive to each peripheral is then two-periodic, and a direct degree-two update over two phases shows that every periodically driven peripheral also has a two-periodic state. All vertices therefore return after two updates. Hence no primitive four-cycle has \(k=2\).

The only primitive four-cycle states come from the \(k=1\) and \(k=3\) classes. Dividing their total by four gives
\[
N_4(m)=\frac{2\cdot4m(m-1)2^{m-2}}4=m(m-1)2^{m-1}.
\]
The formulas include \(m=1\), when the second sum vanishes. This completes the proof.

## Verification
The standalone `verify.py` reconstructs every possible central firing word of lengths three and four and both possible periodic peripheral responses, then intersects exact integer height intervals. For \(m=1,\ldots,25\) it checks the closed formulas and firing-word classifications. A separate vertex-level loop enumerates every confined labelled initial configuration for \(m=1,\ldots,6\), applies the literal simultaneous update, and checks the primitive period-three and period-four orbit counts. For \(m=6\) this covers \(4(m+1)^2 4^m=802{,}816\) confined configurations. Its recorded output is in `verifier_output.txt`. The proof above establishes the all-\(m\) statement; the finite tests do not replace that proof.

## Relationship to prior work
Jiang [2], especially Proposition 2.5 and the confined-state/complement lemmas, proves general periodic-firing restrictions and studies period possibilities on complete bipartite and multipartite graphs. Those classes do not include the book graphs with triangles meeting along one edge (except isolated small isomorphisms), and the cited results do not provide these exact orbit counts. Jiang, Scully and Zhang [3] characterize impossible periodic firing words on arbitrary connected graphs; their general prohibition on clumpy words is consistent with, and can shorten, the four-cycle exclusion argument above, but does not count the book-graph primitive cycles. Levine [1] studies complete-graph chip firing via circle rotations, not the book-graph labelled orbit census; moreover, its complete-graph convention includes self-loops. Thus the exact book-graph enumeration and crossover are distinct from those documented general restrictions.

## Limitations
No claim is made that periods other than three and four are absent, nor is a universal convergence time claimed. The formulas count labelled nonnegative periodic configurations of arbitrary conserved chip total, not graph-isomorphism classes and not all eventual attraction-basin states. Related unpublished or poorly indexed calculations of book-graph periods could exist; the literature comparison cannot prove novelty. Independent validation has not been performed.

## References
[1] L. Levine, *Parallel Chip-Firing on the Complete Graph: Devil's Staircase and Poincaré Rotation Number*, arXiv:0811.2800, first submitted 2008-11-17. https://arxiv.org/abs/0811.2800 .

[2] T.-Y. Jiang, *On the Period Lengths of the Parallel Chip-Firing Game*, arXiv:1003.0943, first submitted 2010-03-04. https://arxiv.org/abs/1003.0943 .

[3] T.-Y. Jiang, Z. Scully and Y. X. Zhang, *Motors and Impossible Firing Patterns in the Parallel Chip-Firing Game*, arXiv:1211.6786, first submitted 2012-11-29. https://arxiv.org/abs/1211.6786 .
