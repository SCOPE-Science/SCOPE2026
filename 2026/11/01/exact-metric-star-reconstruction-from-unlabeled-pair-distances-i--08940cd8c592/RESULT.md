# Exact metric-star reconstruction from unlabeled pair distances, including invisible curvature knots

## Finding

Let \(T\) be a compact metric star with \(n\geq3\) arms of strictly positive lengths \(a_1,\ldots,a_n\). Give \(T\) its intrinsic shortest-path metric and normalized one-dimensional arclength measure. If \(X,Y\) are independent samples from that measure and \(D=d_T(X,Y)\), then **the law of \(D\) determines \(n\) and the entire multiset of arm lengths, with no generic-position assumptions**. Thus the law determines \(T\) up to metric isometry, including absolute scale. An explicit signed-atomic peeling algorithm recovers the arm lengths even when an arm-length singularity cancels exactly against a pair-sum singularity.

Write \(L=\sum_i a_i\), \((u)_+=\max\{u,0\}\), and let \(f\) be the continuous probability density of \(D\) on the nonnegative half-line. Then for every \(t\geq0\),
\[
\frac{L^2}{2}f(t)= L+\frac{n(n-3)}2t -(n-2)\sum_{i=1}^n(t-a_i)_+ +\sum_{1\leq i<j\leq n}(t-a_i-a_j)_+ .
\]
In particular, the degree and total length are intrinsic to the law:
\[
L=\frac2{f(0)},\qquad \frac{L^2f'(0+)}1=n(n-3).
\]
For \(n\geq3\), the right-hand side strictly increases with \(n\). The distributional second derivative on \((0,\infty)\) is the finite signed measure
\[
\nu:=\frac{L^2}{2}f''= -(n-2)\sum_{i=1}^n\delta_{a_i}+\sum_{1\leq i<j\leq n}\delta_{a_i+a_j}.
\]
The arm multiset is uniquely determined by \(\nu\), even if some coefficients cancel.

## Assumptions and scope

A metric star is the quotient of \(n\) closed intervals \([0,a_i]\), with their zero endpoints identified and no further identifications. All \(a_i>0\) are arbitrary real numbers, and \(n\) is finite but not assumed known. Every point is sampled with probability proportional to arclength, independently and with replacement. On the same arm at coordinates \(u,v\), the distance is \(|u-v|\); on different arms it is \(u+v\). The central junction has arclength measure zero. Density derivatives are right derivatives at zero or distributional derivatives on the positive half-line, as explicitly specified. No embedding of the graph in Euclidean space is assumed.

## Proof

**1. Exact density.** For an ordered pair of positions on a single arm of length \(a\), the unnormalized density of their absolute difference at \(t\geq0\) is \(2(a-t)_+\). For a fixed ordered pair of distinct arms of lengths \(a,b\), convolution of uniform arclength on their coordinate intervals gives the unnormalized sum-density \(t_+-(t-a)_+-(t-b)_++(t-a-b)_+\). Adding both orders of each unordered pair and dividing by \(L^2\) yields
\[
\frac{L^2}{2}f(t)=\sum_i(a_i-t)_++\sum_{i<j}\bigl[t-(t-a_i)_+-(t-a_j)_++(t-a_i-a_j)_+\bigr].
\]
The identity \((a-t)_+=a-t+(t-a)_+\) for \(t\geq0\) gives the stated hinge formula. This formula is continuous and nonnegative, integrates to one by its sampling derivation, and vanishes above the diameter \(\max_{i<j}(a_i+a_j)\). Its value and right slope at the origin give \(f(0)=2/L\) and \(f'(0+)=n(n-3)/L^2\). Because \(n\mapsto n(n-3)\) is strictly increasing on the integers \(n\geq3\), the law identifies both \(L\) and \(n\).

**2. Exact signed curvature.** On \((0,\infty)\), the second distributional derivative of \((t-c)_+\) is \(\delta_c\) for each \(c>0\). Applying this to the hinge expression proves the formula for \(\nu\). All its atoms, including signed multiplicities and exact locations, are determined by the density law. There is no atom at zero because each arm length is strictly positive.

**3. Global injectivity despite cancellation.** Suppose two multisets \(A\) and \(B\), both with \(n\geq3\) positive members, give the same \(\nu\). If they differ, let \(s>0\) be their smallest value at which the multiplicity differs. For any two positive arm lengths summing to \(s\), each summand is strictly below \(s\), so the total pair-sum coefficient at \(s\) depends only on multiplicities at smaller values. These coefficients therefore agree for \(A\) and \(B\). The coefficient of \(\delta_s\) in \(\nu_A-\nu_B\) is thus \(-(n-2)(m_A(s)-m_B(s))\), nonzero, contradiction. Hence the entire arm multiset is recovered uniquely. Since a metric star with \(n\geq3\) has a unique branch vertex of valence \(n\), equality of arm multisets is equivalent to isometry.

**4. Constructive recovery.** Begin with the signed measure \(R=\nu\) and no recovered arms. At every stage subtract from \(\nu\) the terms contributed entirely by recovered arms: the negative single-arm atoms and all pair-sum atoms whose two arms have already been recovered. If any arms remain, write \(b\) for the shortest remaining arm length. Every pair sum containing an unrecovered arm exceeds \(b\) strictly, whereas the unrecovered single-arm contribution at \(b\) is negative with mass \(-(n-2)m_b\). Thus the smallest atom of the residual lies at \(b\), is strictly negative, and its mass identifies \(m_b\). Add all \(m_b\) copies of \(b\), subtract the newly accounted terms, and repeat until \(n\) arms have been recovered. This algorithm remains valid for ties and exact coincidences between individual lengths and pairwise sums.

**5. A hidden arm.** For lengths \((1,2,3)\) the single-arm curvature atom at \(3\) cancels with the sum \(1+2\). In fact \(\nu=-\delta_1-\delta_2+\delta_4+\delta_5\); the third arm length is invisible as an individual density kink. Peeling first removes \(-\delta_1\) and \(-\delta_2\), then subtracts the known pair-sum contribution \(+\delta_3\). The residual has a negative atom at \(3\), recovering the hidden length exactly. Therefore simply reading off negative atoms of the observed curvature is *not* a valid reconstruction method, while the stated algorithm is.

## Verification

Run `python verify.py` (Python 3 standard library). It checks the independent same-arm/different-arm convolution against the collapsed hinge identity using exact rational arithmetic; integrates the piecewise-linear density exactly to one; recovers tied and colliding lengths with the signed peeling algorithm; checks the invisible-arm example; and independently samples uniform arclength points, comparing empirical distance bins with analytic probabilities. The exact argument in the proof, not the finite checks or random sampling, establishes the universal assertion.

## Relationship to prior work

Mémoli and Needham, *Distance distributions and inverse problems for metric measure spaces* (first publicly posted October 23, 2018, arXiv:1810.09646; subsequently published in 2022), study distance-histogram rigidity and state local injectivity for metric graphs. A local or generic graph-rigidity result alone does not imply the global, all-positive-arm-length statement, particularly at complete knot cancellations. The relevant complete manuscript could not be inspected through available lawful full-text routes, so an undiscovered stronger statement in that source remains a priority risk.

Aldous, Blanc and Curien, *The distance problem on measured metric spaces* (arXiv:2403.10926, March 16, 2024), construct metric trees with designated probability measures, often concentrated on leaves, to realize or approximate prescribed distance laws. Their statements and tree-construction proofs address realizability, not identification of the uniform-arclength metric star. A related published mathematical result concerning configuration spaces of separated particles on metric stars determines persistence barcodes from pairwise arm-length sums; those barcodes are not the two-point arclength distance histogram, and neither result directly implies the present inverse theorem.

## Limitations

The statement applies to finite stars with at least three strictly positive arms and normalized length measure; it does not claim global rigidity among *all* metric graphs or trees, nor under nonuniform sampling, or stability from finitely many noisy pair measurements. Degree-two subdivisions are metrically indistinguishable and deliberately excluded. This is a proof of an exact population inverse statement, not a numerical inference procedure. Historical priority is provisional because the Mémoli–Needham full manuscript and all older equivalent formulations were not exhaustively verified. An independent mathematical audit has not been performed.

## References

1. F. Mémoli and T. Needham, *Distance distributions and inverse problems for metric measure spaces*, arXiv:1810.09646 (first version 2018); *Studies in Applied Mathematics* **149** (2022), 943–1001. DOI: 10.1111/sapm.12526.
2. D. Aldous, G. Blanc, and N. Curien, *The distance problem on measured metric spaces*, arXiv:2403.10926 (first version March 16, 2024); *Annales de la Faculté des sciences de Toulouse* **34** (2025), 1345–1365.
3. *Exact persistence of two unordered separated particles on metric stars*, publicly indexed mathematical result, 2026/10/11, identifier ce01bbf73bfa; distinct persistence invariant used for implication comparison.
