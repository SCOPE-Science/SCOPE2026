# Sharp rank-one type diversity in finite permutation structures

## Finding
Consider a finite nonempty structure with **two named strict linear orders**. Its elements may be plotted as the points \((i,\pi(i))\) of a permutation \(\pi\), where the first order ranks positions and the second ranks values. For an element \(a\), let its **pointed rank-one type** be the set of all first-order formulas with sole free variable \(x\) and quantifier rank at most one that hold at \(a\). Distinct types are counted *within the same finite structure*.

**Theorem.** Every such finite structure realizes at most **10 distinct pointed rank-one types**. This is sharp, and 10 points are the smallest number that can realize 10 types. Among the \(10!=3,628,800\) permutations of order 10, exactly **328** realize 10 types. They have exactly **two** possible sets of quadrant codes, each realized by 164 permutations. Under reversal of either order and interchange of the orders (the order-eight square symmetry group), the 328 permutations comprise exactly **46 orbits**: 10 of size four and 36 of size eight.

## Assumptions and scope
The language is \(\{<_1,<_2\}\) with equality, and each \(<_i\) is a strict total order on the same finite set. There are no unary colours, parameters, counting quantifiers, or other relations. Both orders are **named**; their reversal/interchange is used only to count symmetry orbits, not to identify structures in the logical statement. The universe is nonempty and may have any finite size. Quantifier rank counts nesting of first-order quantifiers, not total occurrences. One-variable types may contain Boolean combinations of formulas of quantifier rank at most one.

For each point \(a=(i,\pi(i))\), encode four nonempty quadrants by a four-bit mask \(m(a)\): bit \(1\) means a point strictly left and below; bit \(2\), strictly left and above; bit \(4\), strictly right and below; bit \(8\), strictly right and above. The **type spectrum** \(S(\pi)=\{m(a):a\in\pi\}\) is a set of integers in \(\{0,\ldots,15\}\). A 16-bit integer \(\sum_{m\in S(\pi)}2^m\) records it without multiplicity. The 10-point maximizers have spectrum integers `0xfce8` and `0xfea8`, namely

\[\{3,5,6,7,10,11,12,13,14,15\}\quad\text{or}\quad\{3,5,7,9,10,11,12,13,14,15\}.\]

## Proof
**1. Rank-one formulas are exactly the quadrant masks.** A quantifier-free formula with free variables among \(x,y\), over two total orders and equality, is a Boolean combination of the five mutually exclusive cases \(y=x\) and the four strict quadrant relations. Thus a formula of quantifier rank one with free variable \(x\) can test whether each quadrant contains a witness, using \(\exists y\), and cannot distinguish anything beyond the four truth values: quantifier-free formulas with only \(x\) are constant, and outer Boolean operations do not add information. Conversely, the four quadrant-existence formulas distinguish all different masks. Hence counting distinct pointed rank-one types equals counting distinct masks.

**2. At most ten masks.** If the structure has one point, only mask \(0\) occurs. Otherwise, the first and last elements of \(<_1\) contribute at most two types. Every other point has some point strictly to its left and some point strictly to its right. Its mask therefore chooses a nonempty subset of bits \(\{1,2\}\) and a nonempty subset of \(\{4,8\}\): there are only \(3\cdot3=9\) possible interior masks. But the two masks \(9=1+8\) and \(6=2+4\) cannot both occur. Indeed, a point of mask \(9\) lies above every point to its left and below every point to its right, whereas a point of mask \(6\) lies below every point to its left and above every point to its right. If the first of those two points comes before the second, their value comparison must simultaneously go in both directions; the opposite positional ordering gives the same contradiction. Thus there are at most eight distinct interior masks, plus at most two endpoint masks. Hence \(|S(\pi)|\le10\) for all sizes.

**3. Sharpness.** The 10-point permutation
\[\pi=(3,2,1,4,6,5,10,8,9,7)\]
has masks, in positional order, \((12,14,10,9,13,11,5,15,7,3)\), all different. A structure with \(n\) points cannot realize more than \(n\) types, so ten points are necessary.

**4. Exact extremal layer.** `verify.cpp` enumerates all permutations of \(\{0,\ldots,9\}\) lexicographically (there are exactly \(10!\)), computes every point mask by direct pair comparisons, and selects those whose spectrum has cardinality ten. It obtains exactly 164 occurrences of each of the two 16-bit spectra `0xfce8` and `0xfea8`, hence 328 maximizers. It then applies all eight coordinate symmetries (reversing the positional and/or value order and exchanging coordinates), removes each full orbit and finds ten size-four and 36 size-eight orbits. A separately implemented verifier, `verify_independent.py`, obtains the same two signature counts using prefix and suffix extrema rather than pair comparisons. As the enumeration covers every 10-point permutation, this finite certificate is exhaustive; it is not being used to infer the upper bound for arbitrary size.

## Verification
From the directory containing the embedded standalone files, run:

```sh
g++ -O2 -std=c++17 verify.cpp -o verify
./verify
python3 verify_independent.py
```

The first program prints `permutations_checked=3628800`, `extremizers=328`, `dihedral_orbits=46`, and orbit-size counts \(10,36\). The independent program prints the two 164-entry signature counts. Both were executed from the enclosed sources. The analytic upper bound is independent of enumeration. `verify.cpp` uses only C++17 standard headers; the independent script uses only the Python standard library.

## Relationship to prior work
Linman and Pinsker (2014) treat finite permutations as structures with two orders and classify the reducts of their countable homogeneous limit. In particular their discussion of row-column cells over named points motivates using the four quadrants relative to a point. Their reduct classification does **not state** the finite within-structure maximum of ten pointed rank-one types or the 328-permutation extremal layer. Albert, Bouvel and Féray (2018 preprint) study the first-order theory of permutations in the same two-order language, including Ehrenfeucht–Fraïssé games, without stating these extremal counts in the inspected material. A separately indexed result on complete one-types **over parameter sets in a fixed infinite homogeneous two-order structure** addresses a different quantification: it does not provide the number of rank-one types simultaneously realized by points of one finite two-order structure. These differences are implication comparisons, not claims that all related literature has been exhaustively ruled out.

## Limitations
The claim concerns exactly one free variable and quantifier rank at most one; it does not classify rank-two **sentences**, arbitrary parameter types, or structures with more than two orders. The 328 count and 46-orbit refinement depend on the disclosed finite exhaustive programs, while the universal upper bound has a short mathematical proof. Priority among unindexed earlier notes or tabulations remains uncertain.

## References
1. J. Linman and M. Pinsker, *Permutations on the Random Permutation*, arXiv:1405.4297 (first public version 2014-05-16); especially introduction and Section 4.
2. M. Albert, M. Bouvel and V. Féray, *Two First-Order Logics of Permutations*, arXiv:1808.05459 (first public version 2018-08-16), published in *Journal of Combinatorial Theory, Series A* 171 (2020), Article 105158; Sections 2 and 4.
