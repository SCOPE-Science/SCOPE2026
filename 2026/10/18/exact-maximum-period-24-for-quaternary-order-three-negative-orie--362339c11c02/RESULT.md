# Exact maximum period 24 for quaternary order-three negative orientable sequences

## Finding
Let the alphabet be \(\mathbb Z_4=\{0,1,2,3\}\), with negation modulo four. A cyclic word of period \(m\) is *negative orientable of order three* if its \(m\) cyclic length-three windows are pairwise distinct and, for any two of those windows \(u,v\), \(u\ne -v^R\), where the superscript denotes reversal. Both indices may coincide, so self-negative-reversal windows are excluded. Then
\[
\boxed{\max m=24.}
\]
One attaining word, read cyclically, is `001201322330323133102111`.

## Assumptions and scope
Only the alphabet \(\mathbb Z_4\) and length-three cyclic windows are considered. Negative reversal is the involution \(J_3(a,b,c)=(-c,-b,-a)\) modulo four, not ordinary reversal and not coordinatewise negation alone. A cyclic word is permitted to wrap across its final and first symbols. Period means the number of cyclic positions; distinct windows guarantee that it is the least period. No assertion is made for other alphabet sizes or window orders.

## Proof
**1. Triple classes.** There are \(4^3=64\) length-three triples. Exactly eight satisfy \(J_3(t)=t\): the middle coordinate is one of \(0,2\), and the last coordinate is the negative of the first. These eight are forbidden. The remaining \(56\) triples form \(28\) two-element classes \(\{t,J_3(t)\}\). Thus every admissible cyclic word uses at most \(28\) triple classes. A triple \(t=(a,b,c)\) defines a directed edge from \((a,b)\) to \((b,c)\) in the order-two de Bruijn digraph. The edges of the cyclic word have equal in- and out-degree at every vertex.

**2. The ten-vertex quotient.** Put \(J_2(a,b)=(-b,-a)\) and identify each two-symbol vertex \(v\) with \(J_2(v)\). There are ten such vertex classes. For every nonfixed triple class choose either member \((a,b,c)\) and add one undirected quotient edge between \([(a,b)]\) and \([(b,c)]\). This is independent of the chosen member, since the other member reverses the endpoints. Loops count twice toward degrees. The full \(28\)-edge quotient multigraph has the following canonical-representative degree table:

| Vertex representative | Degree |
|---|---:|
| `00` | 3 |
| `01` | 7 |
| `02` | 6 |
| `03` | 7 |
| `11` | 8 |
| `12` | 7 |
| `13` | 4 |
| `21` | 7 |
| `22` | 3 |
| `31` | 4 |

These numbers follow by checking the \(28\) nonfixed triple classes (the complete, reproducible enumeration is included in `verify.py`). Exactly six quotient vertices have odd degree: `00`, `01`, `03`, `12`, `21`, and `22`.

For any cyclic word, its selected quotient edges have **even degree at every quotient vertex**. Indeed, collect the ordinary incoming and outgoing incidences of the selected directed edges at the original vertices in one quotient class. Their total is even because the directed edge set is balanced there: total indegree equals total outdegree. This is precisely the number of undirected quotient incidences, including twice for a loop. Hence the omitted quotient edges must have odd degrees at all six odd-degree vertices. At least three quotient edges must be omitted, giving \(m\le25\).

**3. Exclusion of period \(25\).** If exactly three edges are omitted, they must pair off the six odd-degree vertices in a perfect matching. List each triple class using the lexicographically smaller of its two members. A direct inspection of the quotient multigraph gives precisely two possible perfect matchings, with omitted triple representatives

`001,032,122` and `003,012,221`.

Both are impossible even without imposing connectivity. For a two-symbol vertex \(v\), define the divergence of a triple \(t\) by
\[
d_v(t)=\mathbf1_{\mathrm{prefix}_2(t)=v}-\mathbf1_{\mathrm{suffix}_2(t)=v},\qquad
\Phi_v(t)=d_v(t)-d_{J_2(v)}(t).
\]
The negative reversal sends the source of an edge to the negative reversal of its target. Consequently \(d_v(J_3(t))=-d_{J_2(v)}(t)\), and **\(\Phi_v(J_3(t))=\Phi_v(t)\)**. Therefore the sum of \(\Phi_v\) over selected triple classes is independent of choosing one or the other representative. But balanced directed edges require that sum to be zero.

For \(v=12\), the sum over the complete \(28\) nonfixed triple classes is \(-1\), and the contributions of omitted `001,032,122` are respectively \(0,0,1\). Thus selecting the other \(25\) classes forces \(\sum\Phi_{12}=-2\), impossible. For \(v=03\), the complete sum is \(1\), and omitted `003,012,221` contribute respectively \(-1,0,0\); the remaining sum is \(2\), again impossible. Both sums and the exact two-matchings enumeration are independently reproduced in `verify.py`. Consequently \(m\le24\).

**4. Attainment.** For the cyclic word

`001201322330323133102111`

the \(24\) cyclic triples, beginning at consecutive positions, are

`001,012,120,201,013,132,322,223,233,330,303,032,323,231,313,133,331,310,102,021,211,111,110,100`.

They are pairwise distinct, none is fixed by negative reversal, and no two are paired by negative reversal. These checks are performed directly and exhaustively by the bundled standalone verifier. Thus \(m\ge24\), proving equality.

## Verification
Execute `python3 verify.py`, using Python 3 and no third-party packages. It enumerates all \(64\) triples, the \(28\) nonfixed negative-reversal classes, the quotient degrees, *all* three-edge matchings among six odd vertices, the two invariant contradictions, and the \(24\) cyclic windows of the proposed construction. `verification_output.txt` records a successful execution. The upper bound is the finite analytic argument above; the enumerations reproduce its small explicit incidence tables. No numerical optimization or heuristic search is needed for the proof.

## Relationship to prior work
Mitchell and Wild, *New upper bounds for the period of a negative orientable sequence* (first arXiv submission 2026-02-04, arXiv:2602.04433), establish a general upper bound giving \(25\) for alphabet four and order three (Theorem 3.11 and Table 1, row three, column four). Their earlier upper bound in the same table is \(27\). The present result adds a quotient parity and invariant obstruction that forbids the last candidate length \(25\).

Mitchell and Wild, *Constructing orientable and negative orientable sequences with asymptotically optimal period* (arXiv:2603.18646, 2026-03-19), give a construction lower bound \(22\) for the same parameter (Table 2, row three, column four) rather than this exact optimum. Their general constructions do not assert a period-\(24\) witness or the matching upper bound. Their *Negative Avoiding Sequences* (arXiv:2603.25286, 2026-03-26) concerns excluding \(-t\), not excluding \(-t^R\); the objects differ. Previous binary, ternary, or ordinary-orientable special cases do not imply this statement.

## Limitations
Only the exact quaternary order-three extremum is determined. It neither supplies a general formula for all alphabets/orders nor proves a classification or count of all period-\(24\) extremizers. The checks are reproducible, but no independent external scientific audit has been performed. The primary literature was examined for coverage; unindexed earlier computations or differently formulated equivalent results remain possible.

## References
1. Chris J. Mitchell and Peter R. Wild, *New upper bounds for the period of a negative orientable sequence*, arXiv:2602.04433 (initial submission 2026-02-04), https://arxiv.org/abs/2602.04433.
2. Chris J. Mitchell and Peter R. Wild, *Constructing orientable and negative orientable sequences with asymptotically optimal period*, arXiv:2603.18646 (initial submission 2026-03-19), https://arxiv.org/abs/2603.18646.
3. Chris J. Mitchell and Peter R. Wild, *Negative Avoiding Sequences*, arXiv:2603.25286 (initial submission 2026-03-26), https://arxiv.org/abs/2603.25286.
