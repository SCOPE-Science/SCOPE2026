# Parallel-class rigidity and full lean-colouring spectrum of finite affine planes

## Finding

**Theorem.** Let \(\mathcal A\) be any finite affine plane of order \(q\ge3\), including a non-Desarguesian plane when one exists. Let \(H_{\mathcal A}\) have the \(q^2\) points as vertices and all affine lines as hyperedges. A lean colouring assigns at least two colours to the points such that every line is monochromatic or rainbow. Every such colouring, up to renaming colours, is **uniquely** of exactly one of these forms:

1. All \(q^2\) points have distinct colours.
2. Choose one of the \(q+1\) parallel classes and a nonempty set of \(k\) of its \(q\) lines, with \(1\le k\le q\). Make each selected line monochromatic, with a separate colour for each such line, and give every point outside the selected lines a distinct fresh colour.

Consequently, the attainable colour counts are exactly
\[
\mathscr S(H_{\mathcal A})=\{q^2-k(q-1):k=0,1,\ldots,q\},
\qquad \operatorname{Lean}(H_{\mathcal A})=q.
\]
For \(k\ge1\), precisely \((q+1)\binom qk\) colour partitions use \(q^2-k(q-1)\) colours; one colour partition uses \(q^2\) colours. Therefore there are exactly \(1+(q+1)(2^q-1)\) lean partitions and exactly \(q(q-2)\) absent integer colour counts between the minimum and maximum. If \(t\) colours are available as named labels, with unused labels allowed, the number of lean colourings is the polynomial
\[
L_{\mathcal A}(t)=(t)_{q^2}+(q+1)\sum_{k=1}^{q}\binom qk(t)_{q^2-k(q-1)},
\quad (t)_r=\prod_{j=0}^{r-1}(t-j).
\]

At order \(q=2\), the exception is complete: every nonconstant point colouring is lean because the lines have only two points. It follows that \(L_{\mathcal A}(t)=t^4-t\), and its lean spectrum is \(\{2,3,4\}\).

## Assumptions and scope

A finite affine plane of order \(q\) has \(q^2\) points, \(q(q+1)\) lines of size \(q\), and \(q+1\) parallel classes of \(q\) pairwise-disjoint lines. Distinct points determine a unique line; nonparallel lines meet once; through any point there is one line of each direction. The theorem requires only these axioms and no field representation. A colour partition identifies colourings that differ only by permuting the names of their used colours. The polynomial instead counts functions from the point set into a fixed named palette of size \(t\), provided the image contains at least two colours.

## Proof

**1. Repeated colours force an entire line.** Assume \(q\ge3\). Given distinct same-coloured points \(u,v\), their unique connecting line \(L\) contains two equal colours, so it is not rainbow and must therefore be monochromatic. This implication uses the full lean condition, not merely a forbidden-rainbow convention.

**2. Two intersecting monochromatic lines are impossible in a nonconstant lean colouring.** Suppose distinct monochromatic lines \(L,M\) meet at \(O\). Both have the same colour \(c\), because they share \(O\). Take a point \(P\notin L\cup M\). Among the \(q+1\ge4\) directions through \(P\), exclude those parallel to \(L\) and to \(M\), and the direction of \(PO\). At least one direction remains. The line \(K\) through \(P\) in such a direction meets both \(L\) and \(M\) in distinct points (otherwise \(K\) would pass through \(O\)). Both intersection points have colour \(c\), so \(K\) must be monochromatic and \(P\) has colour \(c\). Every point on \(L\cup M\) already has colour \(c\), and every outside point is handled in the same way; hence the entire plane has one colour, contradicting the requirement of at least two. Thus any distinct monochromatic lines in a lean colouring must be disjoint and therefore parallel.

**3. Monochromatic lines in a parallel class have distinct colours.** If two distinct, disjoint monochromatic lines \(L,M\) shared colour \(c\), choose \(u\in L\), \(v\in M\). Their joining line \(K\) meets both and contains repeated colour \(c\). Step 1 makes \(K\) monochromatic, contradicting Step 2 because \(K\) intersects \(L\) and is different from it. Hence these line colours are distinct.

**4. No colour repeats outside the selected lines.** Every repeated-colour pair lies on a monochromatic line by Step 1. Steps 2 and 3 show that all such lines belong to a single parallel class and have distinct colours. If a point outside their union shared a colour with a point on any selected line, Step 1 would create a second monochromatic line crossing the selected line; this contradicts Step 2. If two outside points shared a colour, Step 1 would create another monochromatic line, so it would be included among the selected lines. Thus all remaining points are distinctly and freshly coloured. If there is no repeated pair, all points have distinct colours.

**5. Every described partition is valid.** In a selected parallel class, each selected line is monochromatic and each unselected line is rainbow because all its points have fresh distinct colours. Every line in another direction meets each selected line in at most one point. Since different selected lines have different colours and all other point colours are unique, such a transversal is rainbow. At least two colours occur: \(q\ge3\) and even selecting all \(q\) parallel lines gives \(q\) colours. Hence all patterns are lean.

**6. Enumerate.** Selecting \(k\) lines in one of \(q+1\) parallel classes produces \((q+1)\binom qk\) different partitions. Their selected class is unique when \(k\ge1\), so there is no double count; the injective partition contributes one more. The selected \(k\) disjoint lines use \(k\) colours in place of \(kq\) singleton colours, reducing the total to \(q^2-k(q-1)\). Each such partition having \(r\) blocks has exactly \((t)_r\) injective assignments of names to blocks, giving the polynomial. Its smallest admissible colour count is attained at \(k=q\), namely \(q\), which is the lean number. There are \(q+1\) realised counts in the inclusive interval from \(q\) to \(q^2\), so the number missing is \(q^2-q+1-(q+1)=q(q-2)\). For \(q=2\), any colouring automatically makes each two-point line monochromatic or rainbow; requiring two colours excludes exactly the \(t\) constant colourings from \(t^4\). This proves every claim.

## Verification

The supplied standard-library Python program `verify_affine_lean.py` builds affine planes of orders \(2,3,4,5,7\), using \(\mathbf F_4\) at order \(4\). It verifies the incidence axioms, generates all partitions asserted by the classification, and tests the lean condition and stated coefficient counts for each order at least \(3\). It independently enumerates **all** set partitions of the \(4\)-point and \(9\)-point affine planes; these yield respectively \(14\) and \(29\) valid partitions and agree exactly with the special case and theorem. For \(q=3\), the spectrum with multiplicities is \((3:4),(5:12),(7:12),(9:1)\). The checks at \(q=4,5,7\) verify validity and count of constructed partitions, not completeness by exhaustion. The proof above establishes unrestricted completeness.

Run from the directory containing the program with `python verify_affine_lean.py`; the program ends with `PASS` only after all assertions succeed.

## Relationship to prior work

Piehowski [1] introduced lean colourings and proved general bounds for uniform, partite, wide-path-connected and other hypergraphs. Its uniform-edge lower bound implies only the scalar lower estimate \(\operatorname{Lean}(H_{\mathcal A})\ge q\), while its wide-path-connectivity result does not apply: distinct affine lines meet in at most one point. The novel content here is the complete partition classification, exact chromatic spectrum and named-palette polynomial, which do not follow from those general theorems. The \(q\)-colour construction also achieves Piehowski's lower bound.

Tuza [2] surveys C- and bi-hypergraph colourings, including gap phenomena. These notions respectively forbid rainbow hyperedges or forbid both rainbow and monochromatic hyperedges; their admissible-colouring conditions differ from the present one, which **permits exactly those two edge types**. Thus results on C-colouring spectra or WORM colourings are not statements of this theorem. An affine plane is not the same incidence structure as a projective plane: affine planes have parallel disjoint lines, permitting several simultaneously monochromatic lines; the counting theorem is not a specialization of projective-plane line-colouring classifications.

## Limitations

The result assumes a finite affine plane exists for the chosen order and says nothing about existence of planes of non-prime-power order. It counts arbitrary point-colourings subject to the lean condition, not proper graph colourings. The program's finite checks do not certify the result for untested orders or non-Desarguesian planes; the axiomatic proof does. Although targeted comparisons found no published equivalent, other terminology or unindexed prior literature could contain an independent earlier classification. No independent scientific audit is represented here.

## References

[1] Harrison Piehowski, *The Lean Number of a Hypergraph*, arXiv:2607.14015v1 (first publicly posted 15 July 2026), https://arxiv.org/abs/2607.14015 ; accessible full text: https://www.researchgate.net/publication/410158181_The_Lean_Number_of_a_Hypergraph .

[2] Zsolt Tuza, *Mixed hypergraphs and beyond*, survey (2019), https://www.researchgate.net/publication/334329458_Mixed_hypergraphs_and_beyond .
