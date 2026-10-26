# Sharp 21-block surjectivity threshold for radius-two endomorphisms of the golden-mean shift

## Finding

Let \(X=\{x\in\{0,1\}^{\mathbb Z}:x_i x_{i+1}=0\text{ for every }i\in\mathbb Z\}\) be the two-sided golden-mean shift. Consider **all** centered radius-two sliding block maps \(F:X\to\{0,1\}^{\mathbb Z}\), with \((Fx)_i=f(x_{i-2}x_{i-1}x_ix_{i+1}x_{i+2})\). There are \(2^{13}=8192\) different such maps, since exactly thirteen length-five input words are admissible.

**Theorem (complete census and sharp observation threshold).** Exactly \(229\) of these maps are endomorphisms \(F:X\to X\). Exactly \(11\) of the \(229\) are onto \(X\). Among the onto maps, exactly five are reversible, namely the shifts \(x\mapsto\sigma^k x\) for \(-2\le k\le2\); the other six are noninjective. For every non-onto endomorphism in this class, a legal output word of length at most \(21\) has no input predecessor. The bound \(21\) is **best possible**, attained by exactly one of the \(229\) endomorphisms.

The extremal endomorphism has the local rule
\[
f(w)=1\quad\Longleftrightarrow\quad w\in\{00010,01000,10101\}.
\]
All \(X\)-admissible words of length at most \(20\) occur in its image, while at length \(21\) precisely the following two admissible words do not occur:

```
100010010001010010001
100010010100010010001
```

They are reversals of one another. Thus no observation of length \(20\) can certify failure of surjectivity for all radius-two endomorphisms of this canonical shift of finite type, whereas length \(21\) always suffices.

For a complete numerical rule list, order the admissible five-blocks lexicographically as

```
00000 00001 00010 00100 00101 01000 01001
01010 10000 10001 10010 10100 10101
```

and encode \(f\) by the integer \(m=\sum_{j=0}^{12} 2^j f(w_j)\), where \(w_j\) is the block at zero-based index \(j\) in this list. The onto codes are exactly

```
100 162 224 388 792 1060 1156 2570 4690 6168 7936
```

The shift codes for \(k=-2,-1,0,1,2\) are, respectively,

```
7936 224 6168 1156 4690
```

The six noninjective onto codes are `100`, `162`, `388`, `792`, `1060`, and `2570`.

In contrast, among centered radius-one rules on \(X\), exactly seven map \(X\) into itself, and only the three shifts \(\sigma^{-1},\mathrm{id},\sigma\) are onto. Hence **radius two is the first centered neighborhood radius admitting a noninjective surjective endomorphism** of \(X\).

## Assumptions and scope

All configurations are bi-infinite, all local rules are binary, and the output is assessed relative to the **same** golden-mean shift \(X\). Rule codes identify values only on words that actually occur in \(X\); arbitrary extensions to forbidden five-blocks are not counted as distinct maps. Since every legal five-block has a bi-infinite extension with zeroes on both sides, the thirteen rule values are independent choices and determine distinct global maps.

A word of length \(n\) occurs in \(F(X)\) if it is a contiguous length-\(n\) factor of some image configuration. Surjectivity means equality of the two bi-infinite shifts \(F(X)=X\), not surjectivity on each finite periodic ring.

## Proof

**1. Exact endomorphism condition.** There are exactly \(21\) legal six-blocks. For a rule of radius two, adjacent output symbols are the values on the overlapping first and last five-blocks of one legal six-block. Therefore \(F(X)\subseteq X\) if and only if for every admissible six-block \(a_0\cdots a_5\),
\[
f(a_0\cdots a_4)f(a_1\cdots a_5)=0.
\]
Every such six-block extends to a point of \(X\), so this criterion is necessary as well as sufficient. Treating the thirteen rule values as binary variables gives an independence-set enumeration on a thirteen-vertex graph, with one loop. Its exact counting polynomial is
\[
1+12t+49t^2+85t^3+63t^4+17t^5+2t^6.
\]
The coefficient sum is \(229\). The accompanying program enumerates all \(8192\) rules against all \(21\) constraints, reproducing every coefficient, not merely the sum.

**2. Exact surjectivity test.** Construct the predecessor graph with one vertex for each of the eight admissible four-blocks and one edge for each of the thirteen admissible five-blocks. An edge \(u_0\cdots u_4\) goes from \(u_0\cdots u_3\) to \(u_1\cdots u_4\) and carries label \(f(u_0\cdots u_4)\). All vertices are initial and terminal. A word labels a path if and only if it has a legal finite predecessor: overlapping edges concatenate, and every finite golden-mean predecessor block extends to a bi-infinite input by zero-padding.

For a subset \(S\) of vertices, define \(T_b(S)\) to be the vertices reachable by a labeled \(b\)-edge starting in \(S\). Begin with the full vertex set \(V\). A legal word \(y_1\cdots y_n\) occurs in the image exactly when
\[
T_{y_n}\cdots T_{y_1}(V)\ne\varnothing.
\]
Search the finite state graph of pairs \((S,b)\), where \(S\subseteq V\) and \(b\) is the last output bit; extend by \(0\) or by \(1\) unless \(b=1\). Its at most \(2^8\cdot2\) states include every possible continuation class. A path reaches the empty set if and only if some legal output word is missing. If no empty transition is reachable, every legal word occurs; because \(F(X)\) is compact and shift invariant, equality of finite languages gives \(F(X)=X\). Breadth-first search gives the shortest omitted legal word when one exists.

Exhaustive application to all \(229\) candidate endomorphisms gives precisely the eleven codes above. The first-missing-word length distribution among the remaining \(218\) is:

| Shortest missing length | Number of maps |
| ---: | ---: |
| 1 | 1 |
| 3 | 30 |
| 4 | 23 |
| 5 | 39 |
| 6 | 45 |
| 7 | 42 |
| 8 | 27 |
| 9 | 5 |
| 10 | 4 |
| 15 | 1 |
| 21 | 1 |

No rule is discarded by a preset word-length cutoff; closure is exact on the full reachable subset graph. The complete code-to-witness catalog is in `classification.csv`.

**3. Sharpness and the two length-21 defects.** Exactly one candidate has its first missing word at length \(21\): code `4132`, equivalently \(f=1\) on the three five-blocks displayed above. For an independent direct check, enumerate all \(196418\) legal input blocks of length \(25\) and apply this rule to their \(21\) centered windows. Exactly \(28655\) distinct output blocks arise, whereas \(X\) has exactly \(28657\) legal length-\(21\) blocks. Their exact set difference consists of the two displayed reversals. The set of length-\(20\) prefixes of the enumerated outputs coincides with the complete legal length-\(20\) language, and therefore every shorter legal word also occurs. This proves the sharp threshold independently of the subset BFS for this extremizer.

**4. Reversible versus nonreversible onto rules.** Reading the leftmost, second, middle, fourth, or rightmost input bit gives the five shift masks above, which are bijections of \(X\). The remaining six onto codes are not injective: each maps both \(0^{\mathbb Z}\) and one of the distinct periodic inputs \((01)^{\mathbb Z}\) or \((001)^{\mathbb Z}\) to \(0^{\mathbb Z}\). For codes `100`, `792`, `1060`, `2570`, take \((01)^{\mathbb Z}\); for codes `162`, `388`, take \((001)^{\mathbb Z}\). The explicit local-rule test in `verify.py` checks these six collisions.

**5. Sharp minimal radius.** For radius one there are five legal three-blocks and eight legal four-blocks. Repeating the same exhaustive preservation and subset-language test over the \(32\) possible rules gives seven self-maps and exactly three onto masks (in lexicographic three-block order): `4`, `18`, `24`. They read, respectively, the middle, right, and left input bit. Radius zero has only the identity as an onto map. Thus no smaller centered radius realizes a noninjective onto endomorphism.

## Verification

Run `python verify.py` with `classification.csv` in the same directory, using standard Python only. It checks every preserving rule, every surjectivity decision, the full shortest-witness distribution, the complete radius-one baseline, all six periodic noninjectivity witnesses, and independently generates all legal length-\(25\) inputs for code `4132`. The direct language-generation routine is separate from the predecessor subset transition test. No sampled experiment is used to infer an infinite-language statement: the infinite claims follow from complete closure of a finite automaton, and the finite enumerations are exhaustive.

## Relationship to prior work

Hedlund's sliding-block representation underpins the finite-window model. Schüle–Stoop classified dynamical properties of elementary rules on the full binary shift; their unrestricted-domain classification does not imply the present exact counts for rules defined solely on the golden-mean constraint. Kari–Taati explicitly discuss the hard-core/golden-mean shift and general properties of surjective endomorphisms of strongly irreducible shifts of finite type, but do not enumerate the centered five-block rule space or compute the exact surjectivity-detection length. Salo's study of von Neumann regularity addresses elementary rules on the full shift and uses the golden-mean shift in a different argument; it does not give this classification.

Adler–Kitchens–Marcus establish general equivalences between onto, finite-to-one, and equal entropy for maps of irreducible shifts of finite type; their almost-topological classification does not supply this exact constrained-radius census or the sharp observation threshold. Generic finite-automaton decision methods are known. The contribution here is the exact complete classification of the first radius at which proper onto endomorphisms occur, together with the unexpectedly long and **sharp** \(21\)-block detection horizon. Earlier unindexed specialized enumerations could exist; this does not certify historical priority.

## Limitations

The theorem is restricted to the two-sided binary golden-mean shift, centered radii at most two, and unrestricted deterministic local values on the admissible windows. It does not classify endomorphisms of larger radius, preimage degrees of the six noninjective maps, noisy observations, or maps on a full binary shift. The finite automaton computations are completely replayable but have not received independent human mathematical audit. No assertion of unique historical priority is made.

## References

1. J. Kari and S. Taati, *Statistical Mechanics of Surjective Cellular Automata*, arXiv:1311.2319v1 (first posted 2013-11-10), *Journal of Statistical Physics* **160** (2015), 1198–1243. The article's sections on symbolic shifts, the hard-core shift, and surjective endomorphisms provide the motivating setting.
2. M. Schüle and R. Stoop, *A Full Computation-relevant Topological Dynamics Classification of Elementary Cellular Automata*, arXiv:1107.2080v1 (first posted 2011-07-11). The full text treats elementary rules on the full binary shift.
3. V. Salo, *On von Neumann regularity of cellular automata*, arXiv:2209.13373v1 (2022), *Natural Computing* **22** (2023), 527–538. The full text treats regularity and predecessor automata, with a different golden-mean example.
4. G. A. Hedlund, *Endomorphisms and automorphisms of the shift dynamical system*, *Mathematical Systems Theory* **3** (1969), 320–375, doi:10.1007/BF01691062.
5. R. Adler, B. Kitchens and B. Marcus, *Almost topological classification of finite-to-one factor maps between shifts of finite type*, *Ergodic Theory and Dynamical Systems* **5** (1985), 485–500, doi:10.1017/S0143385700003114. Primary full PDF inspected for the factor-map implications.
