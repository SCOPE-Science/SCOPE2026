# Two-block distinguishing colorings of the binary free shift

## Finding

Let \(X=F(2^{\mathbb Z})\) be the set of bi-infinite binary sequences with no nonzero shift period, and let \(G\) be the undirected graph joining each \(x\in X\) to its left and right shifts. For an integer \(k\ge1\) and any rule \(\phi:\{0,1\}^2\to\{1,\ldots,k\}\), define the continuous, hence Borel, vertex coloring \(c_\phi(x)=\phi(x_0,x_1)\). Then **\(c_\phi\) distinguishes every graph automorphism of \(G\) if and only if \(\phi\) is injective.** The least palette for a uniform two-block coloring is exactly \(4\). For a fixed palette of \(k\ge4\) named colors, exactly \(k(k-1)(k-2)(k-3)\) rules distinguish; for \(k<4\) none do.

The distinction is quantitative: Chen and Zou prove the unrestricted Borel distinguishing number of this graph is \(3\), so no optimal three-color Borel distinguishing coloring is of this two-consecutive-coordinate form.

## Assumptions and scope

The shift \(T\) is defined by \((Tx)_j=x_{j+1}\) for every integer \(j\). The free set consists of all \(x\) such that \(T^m x\ne x\) for every nonzero integer \(m\). Thus each connected component \(\{T^j x:j\in\mathbb Z\}\) of \(G\) is a two-ended simple infinite path. A distinguishing coloring means a vertex coloring preserved by no nonidentity automorphism of the **entire uncountable graph**, not merely of its individual components. No proper-coloring requirement is imposed. The theorem classifies exactly the fixed, homogeneous, forward two-block rules; it does not assert impossibility for larger finite windows or for general continuous colorings.

## Proof

**Sufficiency.** Suppose \(\phi\) is injective. Every graph automorphism sends each path component to a path component. Enumerate the source component as \(T^j x\) and the target as \(T^j x'\), where \(x,x'\in X\). An isomorphism of two bi-infinite paths has the form \(T^j x\mapsto T^{j+t}x'\) or \(T^j x\mapsto T^{t-j}x'\), for some integer \(t\).

If a color-preserving map uses the first form, then for all integers \(j\), injectivity gives \((x_j,x_{j+1})=(x'_{j+t},x'_{j+t+1})\). Consequently \(T^j x=T^{j+t}x'\) at every vertex, so the map is literally the identity on that component (and its image component is the same one).

For the reversed form, injectivity instead gives \(x_j=x'_{t-j}\) and \(x_{j+1}=x'_{t-j+1}\) for every integer \(j\). Applying the first equality with \(j+1\) shows \(x'_{t-j-1}=x'_{t-j+1}\) for all \(j\), making \(x'\) two-periodic. This contradicts \(x'\in X\). Thus every color-preserving graph automorphism fixes every component pointwise.

**Necessity.** Suppose \(\phi\) identifies two different binary pairs. The following table covers all six possible unordered collisions. The column headed \(t\) specifies a reflection of the orbit indexed by \(j\mapsto t-j\). Let \(u\) be the aperiodic sequence equal to \(1\) only at index zero; let \(v\) equal \(0\) only at index zero; let \(w_j=0\) for \(j\le0\) and \(w_j=1\) for \(j>0\). Each listed color string \(j\mapsto\phi(x_j,x_{j+1})\) is invariant under its displayed reflection, directly by the collision indicated:

| Colliding pair inputs | Witness \(x\) | Reflection \(j\mapsto t-j\) | Why the color string is symmetric |
|---|---|---|---|
| \(00,01\) | \(u\) | \(t=0\) | At most one exception, at \(j=0\). |
| \(00,10\) | \(u\) | \(t=-2\) | At most one exception, at \(j=-1\). |
| \(00,11\) | \(w\) | \(t=0\) | Constant tails agree, with only the boundary at \(j=0\). |
| \(01,10\) | \(u\) | \(t=-1\) | The two adjacent exceptions at \(j=-1,0\) agree. |
| \(01,11\) | \(v\) | \(t=-2\) | At most one exception, at \(j=-1\). |
| \(10,11\) | \(v\) | \(t=0\) | At most one exception, at \(j=0\). |

In every row, reflection of the corresponding infinite path component is nonidentity and preserves all its colors. Extending that reflection by the identity on all other components gives a color-preserving automorphism of the entire graph. (It is even a Borel automorphism: only a countable Borel subset is moved.) Hence every noninjective rule fails.

Finally a rule on the four binary ordered pairs is injective exactly if the palette has at least four labels. Choosing distinct labels yields the upper bound, and choosing four distinct labels in order yields \(k(k-1)(k-2)(k-3)\) maps for \(k\ge4\).

## Verification

The complete implication in both directions is proved symbolically above for all aperiodic input sequences and all automorphisms; it does not rely on a finite experiment. The accompanying standalone `verify_two_block.py` enumerates all \(4^4=256\) labeled four-color rules and, for each of six collision classes, verifies the specified witness symmetry on indices from \(-30\) through \(30\); it also counts injective labeled rules for palette sizes one through four, yielding respectively \(0,0,0,24\). Run `python3 verify_two_block.py`; expected final line: `VERIFY_OK`. This finite check only tests the explicit witness constructions; the proof establishes reflection symmetry at every integer.

## Relationship to prior work

Chen and Zou, *The Borel Distinguishing Number of Schreier Graphs* (first public 2026-09-14), establish the exact unrestricted value \(D_B(G)=3\) using their upper \(n+1\) and matching amenable-group lower bounds with \(n=2\) and \(\Gamma=\mathbb Z\). The present theorem instead classifies **all homogeneous two-block codes** on this same graph, including rigidity against permutations of distinct path components. An unrestricted three-color Borel construction need not be two-block, so Chen--Zou's palette minimum alone does not imply the local classification. Bilge and Kaya introduced Borel distinguishing numbers; their published abstract states general separation phenomena, not this two-block classification. Gao, Jackson, Krohne and Seward analyze continuous equivariant maps and graph colorings of free shifts, especially chromatic colorings, which are different from distinguishing colorings. Gao, Wang and Jiang study Borel and continuous *chromatic* numbers for arbitrary finite generating sets of \(\mathbb Z\); this is likewise a different invariant.

## Limitations

This is an exact result about the specified two-block class only. It does not compute the least palette for arbitrary three-block or longer-window rules, arbitrary continuous colorings on \(X\), or other groups/alphabet sizes. The critical accessible descriptions of the 2026 Chen--Zou and 2025 Bilge--Kaya papers were abstracts/secondary material, not their full proof texts, leaving a residual literature-overlap risk for implicit related lemmas.

## References

- Junhao Chen and Jie Zou, *The Borel Distinguishing Number of Schreier Graphs*, arXiv:2609.15003v1, submitted 2026-09-14, https://arxiv.org/abs/2609.15003.
- Onur Bilge and Burak Kaya, *Borel distinguishing number*, arXiv:2508.08201, submitted 2025-08-11, https://arxiv.org/abs/2508.08201.
- Su Gao, Steve Jackson, Edward Krohne, and Brandon Seward, *Continuous Combinatorics of Abelian Group Actions*, arXiv:1803.03872, submitted 2018-03-11, https://arxiv.org/abs/1803.03872.
- Su Gao, Yingying Jiang, and Tianhao Wang, *Borel Combinatorics of Schreier Graphs of \(\mathbb Z\)-actions*, arXiv:2510.27290, submitted 2025-10-31, https://arxiv.org/abs/2510.27290.
