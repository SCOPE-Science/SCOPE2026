# The degree-ten case of the reduced-degree Mori dream conjecture

## Finding

Let \(s_1<s_2<s_3\) be rational numbers and set
\[
w=\frac{1}{s_2-s_1}+\frac{1}{s_3-s_2}.
\]
Assume \(w<1\). Let \(X\) be the projective toric surface of Picard number one determined by these slopes, let \(e\) be the identity of its dense torus, and put \(X'=\operatorname{Bl}_e X\).

Let \(\Delta_1\) be the smallest good lattice triangle with these slopes. The minimal degree \(d'\) is the smallest positive integer for which exactly \(d'\) columns of \(\Delta_1\) contain at most \(d'\) lattice points; if no such positive integer exists, set \(d'=0\).

**Claim.** If \(d'=10\) and \(10s_2\notin\mathbb Z\), then \(X'\) is not a Mori dream space.

## Assumptions and scope

The ground field is \(\mathbb C\). The slopes are rational, the toric surface has Picard number one, and the width satisfies \(w<1\). The conclusion concerns only the boundary case \(d'=10\) under the nonintegrality condition \(10s_2\notin\mathbb Z\). It does not assert the full reduced-degree conjecture for \(d'\ge 11\), nor make a claim when \(10s_2\in\mathbb Z\).

For \(k\ge1\), write
\[
l_k=\lfloor ks_2\rfloor-\lceil ks_1\rceil+1,\qquad
r_k=\lfloor ks_3\rfloor-\lceil ks_2\rceil+1.
\]
These are the lattice-point counts in the successive columns from the left and right vertices of the triangle. Adding an integer to all three slopes is an integral shear, so we may normalize \(0\le s_2<1\). The condition \(10s_2\notin\mathbb Z\) then implies \(s_2>0\).

## Proof

We use the column-count lemma of He: for either column-count sequence \(c_k\in\{l_k\},\{r_k\}\), if there are at least \(nk\) columns on that side, then
\[
c_{nk}\ge k c_n-(k-1).
\]
Indeed, the floor/ceiling formulas give \(c_j-c_{j-1}\ge c_1-1\); applying the same inequality to the sequence \(c_n,c_{2n},c_{3n},\ldots\) and summing proves the displayed bound. The width hypothesis gives \(s_2-s_1>1\) and \(s_3-s_2>1\), so the column sequences are strictly increasing in the range used below.

For \(d'=10\), the ten columns containing at most ten lattice points have counts \(2,3,\ldots,9,10,10\). Partition \(\{2,3,\ldots,9\}\) into a set \(S\) assigned to the left side and its complement \(T\) assigned to the right side. The two column-count lists are therefore the elements of \(S\) in increasing order followed by \(10\), and the elements of \(T\) in increasing order followed by \(10\). Reflection interchanges the two sides and preserves the nonintegrality hypothesis, so we may assume \(|S|\le4\).

Applying the column-count inequality for every pair of positive integers \((n,k)\) with \(nk\) no larger than the length of the relevant list leaves exactly three possible subsets:
\[
S=\varnothing,\qquad S=\{4,7\},\qquad S=\{4,8\}.
\]
The exhaustive check is a short integer-only enumeration over all \(163\) subsets with \(|S|\le4\); its complete source is included as `verification/degree10_shape_check.py`. The mathematical elimination of the two nonempty survivors is as follows.

If \(S=\{4,8\}\), then \(l_1=4\), \(l_2=8\), and \(l_3=10\). From \(0\le s_2<1\), the first equality gives \(-4<s_1\le-3\). The second forces either \(-4<s_1\le-7/2\) with \(s_2<1/2\), or \(-7/2<s_1\le-3\) with \(s_2\ge1/2\). In the first case, \(\lfloor3s_2\rfloor\in\{0,1\}\) and \(\lceil3s_1\rceil\in\{-11,-10\}\); in the second, \(\lfloor3s_2\rfloor\in\{1,2\}\) and \(\lceil3s_1\rceil\in\{-10,-9\}\). Neither case satisfies \(l_3=\lfloor3s_2\rfloor-\lceil3s_1\rceil+1=10\). Thus \(S=\{4,8\}\) is impossible.

If \(S=\{4,7\}\), then \(l_1=4\) gives \(-4<s_1\le-3\). The equality \(l_2=7\) forces \(\lfloor2s_2\rfloor=0\) and \(\lceil2s_1\rceil=-6\), hence \(-7/2<s_1\le-3\) and \(s_2<1/2\). The equality \(l_3=10\) then forces \(\lfloor3s_2\rfloor=0\) and \(\lceil3s_1\rceil=-9\), so \(s_2<1/3\). Since \(s_2>0\), the right-hand equality \(r_1=2\) gives \(s_3\in[2,3)\), whereas \(r_2=3\), together with \(0<s_2<1/3\), gives \(s_3\in[3/2,2)\). This is a contradiction. Therefore any slope triple satisfying the claim's hypotheses must have \(S=\varnothing\).

When \(S=\varnothing\), the left side has a single low-count column with ten points and the right side has successive column counts \(2,3,\ldots,10\). This is exactly the González–Karu interpolation configuration with parameter \(n=10\). Their theorem implies that \(X'\) is not a Mori dream space whenever \(ns_2\notin\mathbb Z\). Taking \(n=10\) proves the claim. \(\square\)

## Verification

The included checker uses only the Python standard library and integer arithmetic. Running `python verification/degree10_shape_check.py` reports `tested_shapes=163`, the three survivor subsets listed above, and `CHECK_OK`. The subsequent exclusions of \(S=\{4,7\}\) and \(S=\{4,8\}\) are given explicitly in the proof; the last step is the published González–Karu theorem for the remaining configuration. No numerical approximation is used. The argument is conditional on the stated definition of minimal degree and on the cited column-count lemma.

## Relationship to prior work

He formulated the reduced-degree conjecture for these blow-ups and proved it for \(d'\le9\); his classification of the cases up to nine does not include \(d'=10\). The present argument supplies the next boundary case by showing that, under \(10s_2\notin\mathbb Z\), every admissible degree-ten triangle reduces to the González–Karu configuration. González and Karu already prove non-Mori-dreamness for that configuration for arbitrary positive parameter \(n\), so the contribution here is the exhaustive degree-ten shape reduction, not a new proof of their interpolation theorem.

Later work on blow-ups of weighted projective planes gives additional criteria and examples in that subclass. It does not state the degree-ten classification for all rational-slope toric surfaces of Picard number one. The result is compatible with that work and does not claim to classify all degree-ten cases with \(10s_2\in\mathbb Z\).

## Limitations

This is a single finite case of a published conjecture. The enumeration checks the necessary inequalities from the cited column-count lemma, not an unrestricted search over all rational slopes; the two surviving nonempty patterns are then excluded by exact floor/ceiling arguments. The proof does not establish the conjecture for \(d'\ge11\), and it leaves the integral case \(10s_2\in\mathbb Z\) open. A related 2021 paper on extremal curves in weighted-projective-plane blow-ups was available only through its abstract during this comparison; it is recorded as a residual literature risk for that subclass, not as evidence that the all-toric-surface claim is covered.

## References

1. Z. He, *New Examples and Non-examples of Mori Dream Spaces when Blowing up Toric Surfaces*, arXiv:1703.00819 (first public version 2017-03-02), especially Conjecture 2.10, Theorem 2.13, Lemma 9.1, and the proof of Theorems 2.13–2.14.
2. J. L. González and K. Karu, *Some non-finitely generated Cox rings*, Compositio Mathematica 152 (2016), 984–996; arXiv:1407.6344, especially Theorem 1.2.
3. S. Zhou, *Mori dreamness of blowups of weighted projective planes*, Archiv der Mathematik 117 (2021), 267–276, DOI 10.1007/s00013-021-01621-0.
4. J. González-Anaya, J. L. González, and K. Karu, *Curves generating extremal rays in blowups of weighted projective planes*, Journal of the London Mathematical Society 104 (2021), 1342–1362; arXiv:2002.07123.
