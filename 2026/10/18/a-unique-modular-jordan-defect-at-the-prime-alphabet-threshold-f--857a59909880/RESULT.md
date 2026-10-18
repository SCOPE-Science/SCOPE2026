# A unique modular Jordan defect at the prime-alphabet threshold for the free left-regular band

## Finding
Let \(p\) be any prime, \(k\) any field of characteristic \(p\), and \(F_p\) the free left-regular band on the alphabet \(\{1,\ldots,p\}\), including the empty word. In its monoid algebra \(A=kF_p\), put \(x=\sum_{a=1}^{p}(a)\), and let \(L_x:A\to A\) be left multiplication by \(x\). Then its complete Jordan form over \(k\) is
\[
J_2(0)\ \oplus\ J_1(0)^{\oplus(p!-1)}\ \oplus\ \bigoplus_{j=1}^{p-1}J_1(j)^{\oplus p!/j!}.
\]
Here \(J_s(\lambda)\) denotes one size-\(s\) Jordan block of eigenvalue \(\lambda\), and each integer eigenvalue is understood as its image in \(k\). In particular, exactly **one** Jordan block is nonsimple, and it has size two and eigenvalue zero. An explicit rank-one, square-zero obstruction is
\[
L_x^{\,p}-L_x=L_{b_p},\qquad b_p=\sum_{w\in S_p}w,\qquad \operatorname{rank}L_{b_p}=1,\qquad L_{b_p}^{\,2}=0.
\]
This is the first characteristic-\(p\) alphabet size at which the uniform single-letter operator ceases to be semisimple; for smaller alphabets it is semisimple.

## Assumptions and scope
The free left-regular band on \(n\) symbols consists of every word with no repeated symbol, including the empty word. Multiplication is concatenation followed by deletion of letters in the second word already present in the first. The algebra has the words as an independent \(k\)-basis. All statements about the modular Jordan decomposition above concern **left multiplication on the full monoid algebra**, not the restriction to full-length permutations, an averaging operator over real probabilities, or multiplication solely within the symmetric invariant subalgebra. No algebraic closure is needed: all eigenvalues and blocks occur over the ground field.

## Proof
For an alphabet of size \(n\), denote by \(b_r\) the sum of all injective words of length \(r\), with \(b_0\) the empty word. Directly from the multiplication rule, for \(0\le r\le n\),
\[
xb_r=r b_r+b_{r+1},\qquad b_{n+1}=0.
\]
Indeed, for a fixed word of length \(r\), its coefficient in \(xb_r\) is \(r\), one contribution for each possible placement of its first letter within the right factor. Each word of length \(r+1\) appears exactly once. Induction gives the integral identity
\[
b_r=x(x-1)\cdots(x-r+1).
\]
Now set \(n=p=\operatorname{char}(k)\). By the polynomial identity \(T^p-T=\prod_{a\in\mathbb F_p}(T-a)\),
\[
b_p=x^p-x.
\]
Every word of length \(p\) contains all letters and absorbs every word on its right. Consequently, for every basis word \(w\),
\[
b_pw=b_p.
\]
The coefficient vector \(b_p\) is nonzero (its \(p!\) full words are distinct basis vectors), so \(L_{b_p}\) has exactly rank one. Moreover,
\[
b_p^2=p!\,b_p=0
\]
in characteristic \(p\). This proves the displayed rank and square-zero identities without any finite experiment.

The same recurrence with \(r=p\) yields \((x-p)b_p=b_{p+1}=0\), hence \(xb_p=0\). Therefore
\[
(L_x^p-L_x)L_x=0,
\]
so the minimal polynomial of \(L_x\) divides
\[
T^2\prod_{j=1}^{p-1}(T-j).
\]
All nonzero eigenvalues consequently have only size-one Jordan blocks, and zero has blocks of size at most two. On a size-two zero block, the polynomial \(T^p-T\) acts with rank one, while on any size-one block it acts as zero; thus \(\operatorname{rank}(L_x^p-L_x)=1\) forces exactly one size-two zero block.

For completeness, the algebraic multiplicities can be obtained integrally from the characteristic-zero decomposition of the same integer matrix. Brauner, Commins and Reiner's eigenmodule formula [3, Theorem 4.11] gives, in characteristic zero, for eigenvalue \(j\in\{0,\ldots,n\}\), multiplicity
\[
\sum_{r=0}^{n-j}\frac{n!}{(n-j-r)!j!r!}\,!r
=\frac{n!}{j!},
\]
where \(!r\) counts derangements of \(r\) letters. The equality uses \(\sum_{r=0}^{m}\binom mr\,!r=m!\), obtained by classifying permutations by their nonfixed-point set. The characteristic polynomial of an integral matrix reduces coefficientwise in every characteristic. With \(n=p\), only the eigenvalues \(0\) and \(p\) collide modulo \(p\); their combined multiplicity is \(p!+1\). The one size-two zero block leaves \(p!-1\) size-one zero blocks. Every eigenvalue \(j\) for \(1\le j<p\) remains distinct with multiplicity \(p!/j!\), proving the formula.

For any smaller alphabet \(n<p\), the integral relation \(\prod_{j=0}^{n}(L_x-jI)=0\) has distinct roots in \(k\), hence \(L_x\) is semisimple. At \(n=p\), the nonzero square-zero map above proves nonsemisimplicity; the boundary is sharp.

## Verification
A standalone program `verify.py` constructs all injective words, multiplies them literally, builds the left-multiplication matrices, and performs finite-field Gaussian elimination. It checks the complete eigen-kernel and generalized-zero-kernel dimensions for primes \(p=2,3,5\), as well as \(\operatorname{rank}(L_x^p-L_x)=1\), \((L_x^p-L_x)^2=0\), and \((L_x^p-L_x)L_x=0\). It prints `VERIFY_OK_MODULAR_FIRST_COLLISION` on success. The largest tested matrix has dimension \(326\). These finite checks do **not** supply the uniform prime proof.

## Relationship to prior work
Brown [1] treats left-regular-band random walks and their ordinary-field diagonalizable spectra. Saliola [2] identifies the quiver and path-algebra structure of free left-regular-band algebras. Brauner, Commins and Reiner [3, Theorems 2.9 and 4.11] identify the invariant polynomial relation over arbitrary coefficients and the complete eigenspace decomposition when the symmetry-group order is invertible in the coefficient field. The integral identity for \(b_p\) and the characteristic-zero multiplicities are therefore antecedents, not presented as new. The claim here addresses the **modular action on the full monoid algebra** at \(n=\operatorname{char}(k)\), resolving the Jordan extensions left indeterminate by the ordinary eigenspace decomposition. In particular, the invariant-ring polynomial relation alone does not determine Jordan multiplicities on this much larger regular module.

## Limitations
This statement determines the first collision \(n=p\); it does not determine the complete Jordan structure for \(n>p\), nonuniform letter weights, other left-regular bands, or the separate full-length permutation module. It establishes mathematical identities under explicit hypotheses, not historical uniqueness. Potential earlier modular shuffle analyses under different terminology remain a priority risk.

## References
[1] Kenneth S. Brown, *Semigroups, Rings, and Markov Chains*, arXiv:math/0006145, initial public preprint 2000-06-20; especially left-regular-band spectral analysis. https://arxiv.org/abs/math/0006145

[2] Franco V. Saliola, *The Quiver of the Semigroup Algebra of a Left Regular Band*, arXiv:math/0608698, initial public preprint 2006-08-28. https://arxiv.org/abs/math/0608698

[3] Sarah Brauner, Patricia Commins, Victor Reiner, *Invariant Theory for the free left-regular band and a q-analogue*, arXiv:2206.11406, initial public preprint 2022-06-22; Theorems 2.9 and 4.11. https://arxiv.org/abs/2206.11406
