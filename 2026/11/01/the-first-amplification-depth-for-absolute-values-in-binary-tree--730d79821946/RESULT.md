# The first amplification depth for absolute values in binary tree BMO

## Finding
Let a rooted binary tree have depth \(m\), with equal mass on its \(2^m\) leaves. For a real leaf vector \(a\), define the mean-centered \(L^1\)-BMO seminorm
\[
 F_m(a)=\max_{J}\frac1{|J|}\sum_{i\in J}|a_i-\bar a_J|,
 \qquad \bar a_J=\frac1{|J|}\sum_{i\in J}a_i,
\]
where \(J\) ranges over every descendant leaf block (including the root). Write \(|a|\) for coordinatewise absolute value, and define the optimal folding constant
\[
 c_m(2)=\sup_{F_m(a)>0}\frac{F_m(|a|)}{F_m(a)}.
\]
**Theorem.** For every real vector on the depth-three binary tree, \(F_3(|a|)\le F_3(a)\), and the sharp constant is \(c_3(2)=1\). Combining this with the exact depth-one and depth-two contraction and an explicit depth-four counterexample gives
\[
 c_1(2)=c_2(2)=c_3(2)=1,\qquad c_4(2)\ge\frac{41}{40}>1.
\]
Consequently, **the least binary-tree depth at which taking absolute values can increase mean-centered \(L^1\)-BMO is exactly four.** The depth-three upper bound is established by a finite, exact rational dual certificate covering all real eight-leaf vectors, not by a numerical sample.

## Assumptions and scope
The leaves are lexicographically ordered; at depth three the nontrivial node blocks are \(\{1,\ldots,8\}\), \(\{1,\ldots,4\}\), \(\{5,\ldots,8\}\), and the four consecutive pairs. Every node uses equal leaf weights. The input is real-valued; there is no centering condition at the root. The map under consideration is the pointwise absolute-value map, not a complex modulus or a median-centered oscillation. Constant input vectors have zero input and output seminorm and satisfy the inequality trivially.

## Proof
**1. Reduction to the root.** On a node containing two or four equally weighted leaves, folding by absolute value does not increase mean-centered absolute deviation. This follows from the sharp equal-atom folding inequality of Mohajer, Theorem 4.1, which gives \(\max\{1,2-4/n\}=1\) for \(n=2,4\). Thus for the eight-leaf assertion it suffices to establish contraction at the root, using the input BMO seminorm as its right-hand side.

**2. The finite set of input linear constraints.** For every node \(J\) of size \(n\in\{8,4,2\}\) and every sign vector \(\epsilon\in\{-1,1\}^{J}\), define the linear row
\[
 L_{J,\epsilon}(a)=\frac1n\sum_{i\in J}(\epsilon_i-\bar\epsilon_J)a_i,
 \qquad\bar\epsilon_J=\frac1n\sum_{i\in J}\epsilon_i.
\]
The identity \(n^{-1}\sum_{i\in J}|a_i-\bar a_J|=\max_{\epsilon}L_{J,\epsilon}(a)\) is exact. Deleting zero and duplicate rows leaves exactly 290 distinct nonzero rows \(L_j\). Therefore \(L_j(a)\le F_3(a)\) for all such rows and every real \(a\).

**3. Sign cells and output linear forms.** Fix a sign vector \(s\in\{-1,1\}^8\) with \(s_i a_i\ge0\); on this closed orthant, \(|a_i|=s_i a_i\). For each proper nonempty subset \(T\subset\{1,\ldots,8\}\), set
\[
 Q_{s,T}(a)=\frac14\sum_{i=1}^8 s_i\left(\mathbf1_T(i)-\frac{|T|}{8}\right)a_i.
\]
A direct dual expansion of mean absolute deviation gives
\[
 \frac18\sum_{i=1}^8\left||a_i|-\overline{|a|}\right|
 =\max_T Q_{s,T}(a),
\]
where empty and full subsets contribute zero. Hence it suffices to bound every displayed linear form by \(F_3(a)\).

**4. Exact, exhaustive rational dual certificate.** For each required pair \((s,T)\), the attached `certificate.json` supplies nonnegative rational coefficients \(\lambda_j\) and \(\mu_i\) satisfying the eight exact coordinate identities
\[
 Q_{s,T}(a)=\sum_{j=1}^{290}\lambda_jL_j(a)
 -\sum_{i=1}^{8}\mu_i s_i a_i,
 \qquad \sum_j\lambda_j\le1.
\]
All inequalities follow at once: \(s_i a_i\ge0\), and \(L_j(a)\le F_3(a)\), so \(Q_{s,T}(a)\le F_3(a)\). The source file `verify.py` reconstructs these identities using Python exact fractions, without calling a numerical solver. It also constructs the full 128-element automorphism group of the binary rooted tree. Up to this group and simultaneous sign inversion, the 256 input sign patterns form 13 classes, including the trivial constant-sign class. Within each of the 12 nontrivial classes, the stabilizer action on nonempty proper subsets leaves exactly 910 joint representative cases. The certificate contains one exact dual identity for **every** such representative. Permuting leaves or negating all inputs preserves the conclusion, so the verified cases cover every sign cell and every subset. Zero coordinates belong to at least one closed sign cell and cause no exception. This proves \(F_3(|a|)\le F_3(a)\) for **all** real eight-leaf vectors.

**5. Sharpness and minimal depth.** Every nonconstant vector with nonnegative coordinates satisfies \(F_m(|a|)=F_m(a)>0\), so the depth-three sharp constant is exactly one. The lower-depth constants are one by the same two- and four-atom inequality. At depth four, the explicit vector from Mohajer, Theorem 4.2,
\[
 a=(0,-8,-12,-12,\;0,0,0,0,\;6,1,1,1,\;1,10,14,14)
\]
satisfies \(F_4(a)=5\) and \(F_4(|a|)=41/8\); both equalities were independently recomputed by the exact checker. Therefore depth four is the first amplification depth.

## Verification
Run `python3 verify.py certificate.json` with Python 3's standard library. A successful run prints `EXACT_CERTIFICATE_OK cases=910 constraints=290 automorphisms=128 dual_terms=4739 max_bound=1 depth4_ratio=41/40`. The verifier constructs the constraint rows and tree automorphisms afresh, enumerates every representative pair, checks that each appears exactly once, checks nonnegative rational weights and their total bound, and checks all eight coordinate equations by exact fraction arithmetic. It also recomputes both seminorms of the depth-four vector. No floating-point optimization, approximate tolerance, or randomly sampled vector is used for the final certificate validation. The separate verification document describes the proof coverage and reproducibility boundary.

## Relationship to prior work
Mohajer, *Sharp Constants and Extremizers in Homogeneous Tree BMO*, arXiv:2610.14459v1, first posted October 10, 2026, developed the finite-tree rational linear-programming framework. Its Theorem 4.1 establishes exact one-generation folding bounds and its Corollary 4.1 establishes contraction at binary depths one and two. Its Theorem 4.2 exhibits depth-four amplification. Crucially, Section 6 explicitly leaves the exact depth-three binary constant and the first amplification depth unresolved. The present result closes precisely that gap by proving the intervening depth-three contraction; the published depth-four example then makes the depth threshold exact. Earlier alpha-tree BMO work of Slavin and Vasyunin concerns John–Nirenberg and comparisons of oscillation exponents, not this finite-depth folding threshold. Broader BMO-on-shapes work supplies context, without the asserted binary eight-leaf classification.

## Limitations
The proof is computer-assisted finite rational arithmetic: its completeness rests on the plainly specified combinatorial orbit enumeration and 910 explicit dual identities, each fully replayable from standalone files. It does **not** determine the sharp binary constant at depth four, the global infinite-depth constant, or any analogous transition on nonbinary, unequal-mass, or complex-valued trees. The cited October 2026 manuscript is a preprint, and independent mathematical audit of this new result has not been performed.

## References
1. M. Mohajer, *Sharp Constants and Extremizers in Homogeneous Tree BMO*, arXiv:2610.14459v1, October 10, 2026, especially Theorem 4.1, Corollary 4.1, Theorem 4.2, and Section 6. https://arxiv.org/html/2610.14459v1
2. L. Slavin and V. Vasyunin, *Inequalities for BMO on alpha-trees*, arXiv:1501.00097, initial posting December 31, 2014. https://arxiv.org/abs/1501.00097
3. R. Gibara, *Geometric Inequalities and Bounded Mean Oscillation*, PhD thesis, Concordia University, 2020. https://spectrum.library.concordia.ca/id/eprint/987220/
