# Sharp six-phase Walsh peak and its exact optimizer count on an affine six-circuit

## Finding
For the six Walsh characters with frequency support
\[
S=\{0,e_1,e_2,e_3,e_4,e_1+e_2+e_3+e_4\}\subseteq\mathbb F_2^4,
\]
consider coefficient vectors with all entries in the sixth roots of unity \(\mu_6\). The sharp peak is
\[
\min_{c\in\mu_6^6}\max_{x\in\mathbb F_2^4}\left|\sum_{\gamma\in S}c_\gamma(-1)^{\gamma\cdot x}\right|^2=12.
\]
The mean squared modulus of every such sum is \(6\), so the sharp peak-to-average power ratio is \(2\). Exactly \(480\) normalized coefficient vectors attain the bound when vectors are identified only under a common sixth-root scalar factor. No other equivalences are imposed.

## Assumptions and scope
The ambient group is \(\mathbb F_2^4\); the six frequencies are ordered as displayed. Write \(\zeta=\exp(\pi i/3)\), so \(\mu_6=\{\zeta^j:0\le j\le5\}\). Every coefficient has modulus one, and phases outside \(\mu_6\) are excluded. Haar averages mean normalized counting measure. The support is an affine circuit: its six Walsh evaluations have sign product \(+1\). Optimizer counting is over coefficient tuples modulo the six possible common rotations, not coordinate permutations, Walsh modulations, conjugation or other symmetries.

## Proof
Write \(z_0,\ldots,z_5\) for the six complex coefficients. Across \(\mathbb F_2^4\), the Walsh evaluations realize exactly the sixteen sign patterns \(\varepsilon\in\{\pm1\}^6\) with \(\varepsilon_0=1\) and \(\prod_i\varepsilon_i=1\). Every even-parity pattern is either one of these or its overall negative; since six is even, both have even parity and their signed sums have equal modulus. Consequently, maxima and every even absolute moment agree with those over all thirty-two even-parity sign patterns.

Under the uniform distribution on those thirty-two patterns, every nonconstant sign monomial of degree at most four has mean zero. Since \(\sum_i|z_i|^2=6\), expansion yields
\[
\mathbb E\left|\sum_i\varepsilon_i z_i\right|^2=6,
\qquad
\mathbb E\left|\sum_i\varepsilon_i z_i\right|^4=60+\left|\sum_i z_i^2\right|^2\ge60.
\]
Every signed sum belongs to the Eisenstein integer lattice \(\mathbb Z[\zeta]\), where \(\zeta^2=\zeta-1\). Thus for integers \(a,b\), its squared modulus is the integer \(a^2+ab+b^2\). The possible values of that positive quadratic form strictly below \(12\) are exactly \(0,1,3,4,7,9\). This follows directly by writing \(4(a^2+ab+b^2)=(2a+b)^2+3b^2\) and considering \(|b|\le3\). Therefore, if every squared Walsh magnitude were less than \(12\), each would be at most \(9\). Pointwise \(Y^2\le9Y\), where \(Y\) is the squared magnitude, would then imply \(\mathbb E Y^2\le9\mathbb E Y=54\), contradicting the preceding exact fourth-moment lower bound \(60\). Hence the sharp peak is at least \(12\).

For attainment take \(z_j=\zeta^j\) in the displayed frequency order. Direct evaluation of the thirty-two even sign patterns gives squared magnitudes \(0,4,12\) with multiplicities \(8,12,12\); the corresponding physical sixteen Walsh sample multiplicities are \(4,6,6\). Thus the peak is exactly \(12\).

Finally, divide out a common sixth-root rotation by setting \(z_0=1\). There are exactly \(6^5=7776\) remaining tuples. The standalone integer checker examines all sixteen physical Walsh evaluations for each tuple, using the exact norm formula \(a^2+ab+b^2\). It determines the sharp value \(12\) for exactly \(480\) normalized tuples, and the complete frequency distribution of the remaining peak values. This exhausts the stated finite class without tolerance, sampling or symmetry assumptions beyond the explicitly stated common rotation.

## Verification
Run `python3 checker.py` using Python 3's standard library. It asserts the exact average-moment identities for all \(7776\) normalized tuples, the sharp lower bound and explicit attaining construction, and counts exactly \(480\) normalized minimizers. The proof of the lower bound is symbolic and does not depend on the computation; enumeration is necessary for the exact optimizer count, and covers all possibilities rather than a subset.

## Relationship to prior work
Large signed-sum inequalities over general planar unit vectors are studied by Ambrus and González Merino (2020) and Grundbacher (2025). Those works allow every independent sign pattern, whereas the affine Walsh circuit accesses only even-parity patterns; their unrestricted signed-sum extremal statements do not imply a sharp bound after discarding half of the signs. Previously studied sparse Fourier phase-minimax problems include a four-character affine Walsh basis and a three-frequency cyclic problem (published records cited below); neither fixes both the present six-circuit and six-phase alphabet, nor gives its optimum and exact count of normalized optimizers.

## Limitations
This is a finite-alphabet, fixed-six-character result. The continuous-phase minimum and a classification of all continuous-phase extremizers are not established. The count \(480\) relies on a short exact exhaustive checker; it is not an independently verified closed-form orbit theorem. Possible older polyphase or coding-theoretic tables not indexed under these terms remain a bibliographic risk. No assertion of independent audit is made.

## References
- G. Ambrus and B. González Merino, *Large signed subset sums*, arXiv:2012.13164, first public 2020-12-24, especially the general signed-sum definition and planar framework.
- F. Grundbacher, *A Sharp Bound on Large Planar Signed Vector Sums*, arXiv:2502.13752v1, first public 2025-02-19; unrestricted planar signed-sum comparison.
- Published mathematical research record, *Sharp phase flatness of the four-character Walsh affine basis*, 2026, identifier `2026/10/4/SCOPE-sharp-phase-flatness-of-the-four-character-walsh-affine-basis--cd44a812cc6a`.
- Published mathematical research record, *Exact seven-sample phase minimax for the Fano frequency triple*, 2026, identifier `2026/10/4/SCOPE-exact-seven-sample-phase-minimax-for-the-fano-frequency-triple--d1f94e9a8add`.
