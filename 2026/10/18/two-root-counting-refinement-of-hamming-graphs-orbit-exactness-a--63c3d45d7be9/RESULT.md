# Two-root counting refinement of Hamming graphs: orbit exactness and the sharp metric-pair defect

## Finding

**Theorem.** Fix integers \(q\ge2\), \(d\ge1\), and \(1\le t\le d\). In the Hamming graph \(H(d,q)\), individually distinguish two vertices \(a,b\) at Hamming distance \(t\) by different initial colours, and give every other vertex a common initial colour. The stable partition of ordinary one-dimensional counting colour refinement is **exactly** the orbit partition of graph automorphisms fixing \(a\) and \(b\) pointwise.

After a graph automorphism we may take \(a=(0,\ldots,0)\) and \(b=(1,\ldots,1,0,\ldots,0)\), with precisely \(t\) initial ones. For any vertex \(x\), let \(\alpha\), \(\beta\), and \(\gamma\) count, in the first \(t\) coordinates, entries equal to \(0\), equal to \(1\), and different from both; let \(\delta\) count nonzero entries in the remaining \(d-t\) coordinates. Thus \(\alpha+\beta+\gamma=t\) and \(0\le\delta\le d-t\). The stable classes are precisely the nonempty sets with fixed \((\alpha,\beta,\gamma,\delta)\). Their number is

\[
N(q,d,t)=\begin{cases}(t+1)(d-t+1),&q=2,\\ \binom{t+2}{2}(d-t+1),&q\ge3.\end{cases}
\]

The class indexed by \((\alpha,\beta,\gamma,\delta)\) contains exactly

\[
\frac{t!}{\alpha!\,\beta!\,\gamma!}(q-2)^\gamma
\binom{d-t}{\delta}(q-1)^\delta
\]

vertices, with \(0^0=1\). For \(q=2\), necessarily \(\gamma=0\).

A second, sharp assertion concerns the **two-root metric partition** according to the ordered distance pair \((\operatorname{dist}(x,a),\operatorname{dist}(x,b))\). This partition equals the automorphism-orbit partition (and hence is equitable) if and only if \(q=2\), or \(t=1\), or \(t=d\). In every other case (\(q\ge3\) and \(2\le t<d\)), it is non-equitable, but exactly **one counting-refinement round, started from that distance-pair partition**, produces the orbit partition.

## Assumptions and scope

The graph \(H(d,q)\) is the Cartesian product of \(d\) copies of the complete graph on \(q\) letters; two words are adjacent if they differ in exactly one coordinate. The two roots are distinct and individually assigned distinct colours that differ from the common colour of all other vertices. Counting colour refinement repeatedly recolours a vertex by its old colour together with the multiset of colours of its neighbours. An equitable partition is one in which every vertex in a cell has the same number of neighbours in each cell. Distances throughout are ordinary unweighted graph distances, which equal Hamming distances.

The assertion about one refinement round applies to the explicitly given two-root **distance-pair** starting partition, not to an unspecified number of rounds from the original three-colour initialization. No exact number of rounds from that initial colouring is claimed.

## Proof

**1. Two-root orbits.** Coordinate permutations among the first \(t\) positions and among the last \(d-t\) positions preserve both roots. Independently at each of the first positions, an arbitrary permutation of the \(q-2\) letters other than \(0,1\) preserves both roots; at each later position one may arbitrarily permute the \(q-1\) nonzero letters. These are graph automorphisms. Their action is transitive on all words with any prescribed feasible tuple \((\alpha,\beta,\gamma,\delta)\). The orbit size follows by first choosing coordinate categories and then assigning allowed letters. It remains to show distinct tuples never fall in one full pointwise-stabilizer orbit, and that refinement distinguishes them.

**2. A local invariant that reconstructs the tuple.** Write \(u=\operatorname{dist}(x,a)\) and \(v=\operatorname{dist}(x,b)\). Directly from the four categories,

\[
u=\beta+\gamma+\delta,\qquad v=\alpha+\gamma+\delta.
\]

Let \(f(x)\) be the number of graph neighbours \(y\) of \(x\) for which both \(\operatorname{dist}(y,a)=u-1\) and \(\operatorname{dist}(y,b)=v-1\). For a last-coordinate nonzero letter, replacing that letter by zero decreases both distances by one and contributes exactly one such neighbour. No other coordinate change decreases both distances: in an initial coordinate, changing among \(0\), \(1\), and a third letter can decrease at most one of the distances, and changing a zero later-coordinate letter increases at least one. Therefore \(f(x)=\delta\). (If either distance would become negative, the defining neighbour count is zero.) It follows that

\[
\delta=f,\qquad \alpha=t+f-u,\qquad \beta=t+f-v,\qquad\gamma=u+v-t-2f.
\]

Thus \((u,v,f)\) determines the tuple. Since distances to the roots and adjacency are preserved by every automorphism fixing both roots, each tuple is also a union of full pointwise-stabilizer orbits. Together with the transitivity in step 1, the tuples are precisely those orbits.

**3. Why counting refinement sees the invariant.** The stable colouring is equitable and retains each initial singleton as a singleton. In any equitable partition with a singleton \(\{a\}\), distance from \(a\) is constant within every cell: induct on the radius \(r\), since the union of cells at distance at most \(r\) is preserved by equitability, and having a neighbour in this union is cellwise constant; the distance at most \(r+1\) set is exactly that union together with all its neighbours. The same argument applies to \(\{b\}\). Hence \((u,v)\) is constant within every stable colour class. Because the union of stable cells with distance pair \((u-1,v-1)\) is itself a union of colour classes, equitability also makes \(f(x)\) constant within any stable colour class. By step 2, every stable cell lies in one orbit tuple. Conversely, all counting-refinement rounds are automorphism invariant under the pointwise stabilizer, since the initial colouring is. Hence no orbit tuple can split between stable classes. Therefore stable colour classes and stabilizer orbits coincide.

**4. Exact metric-partition boundary.** If \(q=2\), \(\gamma=0\) and \(u+v=t+2\delta\), so \((u,v)\) determines \(\delta\) and then \(\alpha,\beta\). If \(t=d\), \(\delta=0\) and the displayed reconstruction formulas use only \((u,v)\). If \(t=1\), \(v-u=\alpha-\beta\) is \(1\), \(-1\), or \(0\), distinguishing the three possible initial-coordinate categories (where permitted); then \(\delta\) follows from \(u\). In all three cases distance pairs equal orbit tuples, yielding an equitable partition.

Suppose instead \(q\ge3\) and \(2\le t<d\). Both tuples \((t-2,0,2,0)\) and \((t-1,1,0,1)\) are feasible, and both have distance pair \((u,v)=(2,t)\), yet their \(f\)-values are respectively \(0\) and \(1\). The distance-pair cell \((1,t-1)\) contains exactly the neighbours counted by \(f\) for these words, so the metric partition is not equitable. In a single colour-refinement round from the distance-pair partition, its neighbour-colour multiset records \(f\); hence the refined cells lie within orbit tuples. They cannot split tuples by automorphism invariance, proving equality after one round. This completes both assertions.

**Smallest displayed example.** In \(H(3,3)\), let \(a=000\), \(b=110\). The vertices \(220\) and \(012\) both have distances \((2,2)\) from \((a,b)\), but have respectively \(0\) and \(1\) neighbours whose distance pair is \((1,1)\). Thus the metric partition fails here, whereas stable counting refinement distinguishes their orbits.

## Verification

The scripts `verify_direct.py`, `verify_quotient.py`, and `verify_metric_boundary.py` use only the Python standard library. Execute with `python3 verify_direct.py`, `python3 verify_quotient.py`, and `python3 verify_metric_boundary.py` respectively. The corresponding `direct_run.txt`, `quotient_run.txt`, and `metric_run.txt` contain the observed standard outputs.

`verify_direct.py` constructs the actual graph, refines its individualised three-colour partition to stabilization, and compares stable colours to the orbit types, the distance-pair criterion and the local formula \(f=\delta\), in 82 configurations containing a total of 18,903 vertices. `verify_quotient.py` independently constructs the exact weighted transition network among the orbit types and verifies that their initial colouring eventually separates all types for 1,026 parameter configurations. `verify_metric_boundary.py` independently enumerates feasible four-parameter types and tests the necessary-and-sufficient distance-pair criterion in 2,646 parameter configurations. All three completed successfully; no computation is used as a substitute for the all-parameter proof above.

## Relationship to prior work

Krotov's 2009 work develops weight distributions and equitable partitions (perfect colourings) on Hamming graphs; the general survey of distance-regular graphs by van Dam, Koolen and Tanaka discusses equitable distance partitions and two-point homogeneity; Mirafzal and Ziaee describe the Hamming-graph automorphism group. These provide context and established structural vocabulary. The contribution here is the coarsest equitable partition from **two distinctly marked vertices**, its precise recovery of the pointwise stabilizer's orbit partition, and the sharp distance-pair defect criterion with a one-round repair. The automorphism transitivity used in the proof is verified directly and does not assume the cited group classification.

## Limitations

This theorem concerns ordinary vertex counting colour refinement on **uniform** Hamming graphs and two different singleton colours, not arbitrary Cartesian products with unequal alphabet sizes, two unlabelled vertices assigned the same colour, or the two-dimensional Weisfeiler–Leman algorithm. The proof gives orbit equality at stabilization but no sharp stabilization-round formula. Literature comparison was non-exhaustive: a specialized earlier result on individualized Hamming schemes or two-root equitable partitions might overlap. No independent scientific audit or publication-priority certification has been performed.

## References

1. D. S. Krotov, *On weight distributions of perfect colorings and completely regular codes*, arXiv:0907.0001 (first public version, 2009-06-30), https://arxiv.org/abs/0907.0001.
2. E. R. van Dam, J. H. Koolen and H. Tanaka, *Distance-regular graphs*, arXiv:1410.6294 (2014), https://arxiv.org/abs/1410.6294.
3. M. Mirafzal and M. Ziaee, *A note on the automorphism group of the Hamming graph*, arXiv:1901.07784 (2019), https://arxiv.org/abs/1901.07784.
