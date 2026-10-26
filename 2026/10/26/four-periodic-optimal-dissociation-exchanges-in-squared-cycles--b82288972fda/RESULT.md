# Four-periodic optimal dissociation exchanges in squared cycles

## Finding
For each integer \(m\ge 7\), let \(G_m=C_m^2\): vertices are elements of \(\mathbb Z_m\), and two distinct vertices are adjacent when their cyclic distance is at most two. A **dissociation set** \(D\) is a set inducing maximum degree at most one. Define \(\mathcal X_m\) to have one vertex per maximum-cardinality dissociation set, with two vertices adjacent exactly when one member of the selected set is replaced by one unselected member and the result remains a maximum dissociation set.

**Theorem.** The maximum cardinality is
\[
\operatorname{diss}(G_m)=\lfloor m/2\rfloor-\mathbf 1_{\{m\equiv 2\pmod 4\}}.
\]
The number of maxima, their exchange-graph edges, and connectivity are as follows (all displayed formulas apply to integers \(m\ge7\) in the stated residue class).

| \(m\pmod4\) | Number of maximum sets | Exchange edges | Exchange components |
| --- | ---: | ---: | --- |
| \(0\) | \(4\) | \(0\) | four isolated vertices |
| \(1\) | \(2m\) | \(3m\) | connected, the \(m\)-sun graph |
| \(2\) | \(5m(m-2)/8\) | \(m(7m-6)/4\) | connected |
| \(3\) | \(m\) | \(m\) | the cycle \(C_m\) |

Here the \(m\)-sun graph means a cycle \(C_m\) together with one new vertex adjacent to both ends of every cycle edge (the original cycle edges remain). Thus the \(m\equiv1\pmod4\) exchange graph has \(m\) degree-four and \(m\) degree-two vertices and exactly \(m\) triangles.

In the \(m\equiv2\pmod4\) case the degree distribution is additionally exact:
\[
\begin{array}{c|ccc}
\text{exchange degree}&4&6&8\\\hline
\text{multiplicity}&m(m-8)/4&m(m+2)/4&m(m+2)/8.
\end{array}
\]
All four residue classes occur arbitrarily far along the family. In particular, optimum-preserving one-token reconfiguration freezes at every multiple of four but is connected at all other sufficiently large lengths, with no extra tokens allowed.

## Assumptions and scope
All graphs are finite, simple, undirected. The square of the cycle uses the *ordinary* distance-two power, not a Cartesian square. Every exchange is a token jump, not necessarily a move along an edge of the original graph. The theorem does not address nonmaximum dissociation sets, larger powers, or the exceptional smaller cycles \(C_3^2\) through \(C_6^2\). Set cardinalities and degrees refer to labeled cycle vertices, not configurations modulo rotation.

## Proof
**1. Canonical blocks and the optimum.** In a dissociation set, every component of the induced subgraph consists of one selected vertex (a singleton) or two adjacent selected vertices (a pair). Along the underlying cycle, a pair has separation one or two. Reading clockwise from the first selected vertex of each component, the component followed by the mandatory two unselected vertices is one of

```
S = 100        (singleton, length 3)
P = 1100       (short pair, length 4)
L = 10100      (long pair, length 5).
```

Extra zeros, if any, are appended after the two mandatory terminal zeros of a block. These blocks are disjoint, cover the entire cyclic word, and are uniquely recovered from its selected components. Conversely, any cyclic concatenation of these blocks produces a dissociation set, provided \(m\ge7\). The same description works when there is just one block, because the terminal zeros enforce cyclic separation.

If \(p\) is the number of paired components, \(s\) the number of singleton components, \(\ell\) the number of long pairs, and \(e\) the total extra zeros, then
\[
|D|=2p+s,\qquad m=4p+3s+\ell+e=2|D|+s+\ell+e.
\]
In particular \(2|D|\le m\). Equality requires \(s=\ell=e=0\), which forces \(4\mid m\). In residue two modulo four, equality at \(m/2\) is thus impossible. In all four classes, the constructions described below attain the asserted maximum, completing the optimization proof.

**2. Counting all maxima.** Write \(m=4q+r\), \(r\in\{0,1,2,3\}\), where the ranges in the theorem ensure \(q\ge1\) and for \(r\in\{1,2\}\), \(q\ge2\). The preceding equality confines maxima to the following deficit types. Here \(E\) denotes a short-pair block `11000` with one extra zero, and \(F\) denotes `110000` with two extra zeros.

| Remainder | All possible component-defect descriptions | Count |
| --- | --- | --- |
| \(r=0\) | \(q\) copies of \(P\) | \(4\) |
| \(r=1\) | one \(L\) among \(q\) pair blocks, or one \(E\) among \(q\) | \(m+m\) |
| \(r=2\) | two \(S\) among \(q+1\) blocks; two \(L\) among \(q\); one \(L\) and one extra zero among \(q\); or two extra zeros among \(q\) | \(mq/2+m(q-1)/2+mq+m(q+1)/2\) |
| \(r=3\) | one \(S\) among \(q+1\) blocks | \(m\) |

For the counting rule, if the cyclic configuration has \(c\) components, count its rooted ordered block descriptions and multiply by \(m/c\): each actual configuration admits exactly \(c\) component roots out of \(m\) possible marked locations. For example, in the \(r=2\) case the two-singleton descriptions number \(m\binom{q+1}{2}/(q+1)=mq/2\); the two-long-pair descriptions number \(m\binom q2/q=m(q-1)/2\); the one-long-one-extra descriptions number \(m\cdot q^2/q=mq\); and distributing two extra zeros among \(q\) pair blocks gives \(m\binom{q+1}{2}/q=m(q+1)/2\). Summation yields \(5m(m-2)/8\).

**3. Exchanges and components.** An elementary exchange preserves the number of selected vertices and hence the tiny available defect budget \(m-2|D|\). The following are legitimate one-token replacements, wherever these strings represent consecutive full blocks; their inverses are legitimate too:

```
L  <-> E         10100        <-> 11000
SP <-> PS        1001100      <-> 1100100
SS <-> F         100100       <-> 110000
EP <-> PE        110001100    <-> 110011000
FP <-> EE        1100001100   <-> 1100011000
```

The middle two strings in each displayed substitution have the same length and the same number of ones, differ at precisely two bit positions, and satisfy all boundary conditions because each block begins with one or two selected vertices and ends with two zeros. Rotations and cyclic wraps are allowed.

For \(r=0\), the only configurations are the four rotations of \(P^q\); no two differ by one token. For \(r=3\), moving the unique \(S\) across adjacent \(P\)-blocks via `SP <-> PS` gives the entire single cycle of \(m\) rotations, with edges connecting a configuration to the rotations by four positions clockwise and counterclockwise. Since \(m\) is odd, this is \(C_m\).

For \(r=1\), each \(L\) changes to two possible \(E\)-configurations by exchanging its left or right selected vertex, and each \(E\)-configuration has two neighboring \(E\)-configurations by transporting the extra zero past one neighboring \(P\)-block. The \(E\)-configurations form a cycle under rotation by four positions: \(\gcd(4,m)=1\). Each \(L\) attaches to the endpoints of exactly one edge of this cycle, and each cycle edge gets precisely one such \(L\). Directly checking possible insertion positions in the local blocks excludes other exchanges. This is precisely the \(m\)-sun graph.

For \(r=2\), use `L <-> E` to eliminate each \(L\). For two singletons, successive applications of `SP <-> PS` bring them together, then `SS <-> F` makes a configuration with only paired components. The remaining configurations consist entirely of \(P\)-blocks with two extra zeros. More generally, write a paired block with \(a\) extra zeros as `11` followed by \(a+2\) zeros. For adjacent blocks with \(a\ge1\) and \(b\ge0\), transferring one extra zero from the first block to the second changes `11 0^(a+2) 11 0^(b+2)` to `11 0^(a+1) 11 0^(b+3)`. The two words have precisely one different selected vertex: the second pair moves one place left and overlaps itself at one vertex. It is therefore a legal one-token exchange. This elementary transfer applies across the cyclic boundary as well. The nonnegative surplus vector \((a_1,\ldots,a_q)\) has total two, and adjacent transfers connect all such vectors. Passing a marked surplus once across the cyclic boundary also changes the chosen anchor-pair phase by one position; hence the same transfers connect every labeled phase rather than only configurations rooted at one pair. The displayed `EP <-> PE` and `FP <-> EE` are the first two special cases. This proves connectedness of all paired configurations and thus of the entire \(r=2\) exchange graph.

**4. Local exchange degrees.** Here is the complete case table obtained by testing all possible replacement positions against the defining degree-at-most-one condition. Only distances at most four on the underlying cycle need to be tested: at larger distance, deleting the old token could not remove any conflict caused by inserting the new one, so the insertion would contradict maximality. Thus the test is local, independent of the number of intact \(P\)-blocks between defects. The proof is a direct comparison of the patterns surrounding the removed and inserted tokens; `verify.py` independently repeats the check on the complete labeled graphs for a substantial range.

| Maximum-set defect type | Exchange degree |
| --- | ---: |
| \(r=0\): all \(P\) | \(0\) |
| \(r=1\): one \(E\) / one \(L\) | \(4\) / \(2\) |
| \(r=3\): one \(S\) | \(2\) |
| \(r=2\): two extra zeros, no \(S,L\) | \(8\) |
| \(r=2\): one \(L\) and one extra zero | \(6\) |
| \(r=2\): two \(L\) | \(4\) |
| \(r=2\): two \(S\) in consecutive component blocks | \(6\) |
| \(r=2\): two \(S\) in nonconsecutive component blocks | \(4\) |

The counts of these last five types, in order, are \(m(q+1)/2\), \(mq\), \(m(q-1)/2\), \(m\), and \(m(q-2)/2\). The last two follow because exactly \(m\) of the \(mq/2\) two-singleton configurations have consecutive singleton blocks. Combining equal degree types gives the three multiplicities in the theorem. The handshaking lemma then gives \(m(7m-6)/4\) exchange edges. This proves all assertions.

## Verification
The included standalone `verify.py` builds the graphs from cyclic bit words and checks every relevant vertex's induced degree. For all \(7\le m\le16\) it **independently enumerates every vertex subset** and compares the complete family of maxima to the block construction. For every \(7\le m\le32\), it constructs all block configurations, regenerates every one-token exchange from set symmetric differences, and checks the optimum, vertex counts, edge counts, degree histograms, connectivity, and defect-type degree rules. Further separate tests at \(m=33,34,35,38,42,46\) agree with the formulas. `python verify.py` prints `VERIFY_OK` on success. Computations supplement the general block proof; they are not evidence of exhaustive infinite enumeration.

## Relationship to prior work
Boliac, Cameron and Lozin (2004) study computational complexity of dissociation and induced matching on bipartite graphs; their setting does not contain the triangular graph \(C_m^2\). Orlovich, Dolgui, Finke, Gordon and Werner (2011) analyze broader complexity and solvable hereditary classes for dissociation sets; the accessible main results do not give optimum-exchange graphs for the squared cycles. Bonsma, Kamiński and Wrochna (arXiv v1, March 3, 2014) analyze **independent-set** reconfiguration in claw-free graphs, with a different feasibility condition (induced degree zero rather than at most one). Existing maximum-independent-set phase results for cycle powers likewise do not imply the present four-periodic dissociation theorem or its degree distribution. The present claim is a direct solution-space classification for degree-at-most-one induced subgraphs, not a restatement of an independence-number formula.

## Limitations
The claimed theorem is restricted to ordinary squared cycles of length at least seven. It does not determine exchange diameters in the connected cases, and it does not assert any universal behavior for arbitrary claw-free graphs. The accessible literature review is not exhaustive; equivalent older results under the names **1-dependence**, **induced-degree-one sets**, or **3-path vertex-cover complements** remain a possible originality risk. Independent expert audit has not been performed.

## References
- R. Boliac, K. Cameron, V. V. Lozin, *On computing the dissociation number and the induced matching number of bipartite graphs*, Ars Combinatoria 72 (2004), 241–253. https://combinatorialpress.com/article/ars/Volume%20072/volume-72-paper-26.pdf
- Y. Orlovich, A. Dolgui, G. Finke, V. Gordon, F. Werner, *The complexity of dissociation set problems in graphs*, Discrete Applied Mathematics 159 (2011), 1352–1366. https://doi.org/10.1016/j.dam.2011.04.023
- P. Bonsma, M. Kamiński, M. Wrochna, *Reconfiguring Independent Sets in Claw-Free Graphs*, arXiv:1403.0359v1 (publicly submitted 2014-03-03). https://arxiv.org/html/1403.0359v1
