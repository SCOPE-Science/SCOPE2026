# Every rational occurs as a first-order limit probability in the Fibonacci layered-permutation class

## Finding
Let \(\mathcal F=\operatorname{Av}(231,312,321)\). Draw a permutation uniformly from \(\mathcal F_n\) and interpret first-order logic in the language of two strict linear orders: position and value. For every rational \(a/b\in[0,1]\), there is an explicit first-order sentence \(\Phi_{a,b}\) such that
\[
\lim_{n\to\infty}\Pr_{\pi\in\mathcal F_n}(\pi\models\Phi_{a,b})=\frac ab.
\]
In fact the construction has the exact finite-size symmetry
\[
\Pr(\Phi_{a,b})=\frac ab\Pr(H_b),
\]
where \(H_b\) is the event that at least one of the designated patterns occurs; this holds at every finite size, not only asymptotically. Thus the set of first-order limiting probabilities contains \(\mathbb Q\cap[0,1]\), a stronger assertion for this concrete Fibonacci class than mere density.

## Assumptions and scope
The probability measure is uniform over permutations of size \(n\) belonging to \(\operatorname{Av}(231,312,321)\); it is not the uniform measure on unrestricted permutations. The logic is first-order with the two intrinsic linear orders, and formulas can depend on the fixed integers \(a,b\), but not on \(n\). Avoiding \(231\) and \(312\) makes a permutation a direct sum of decreasing layers, while avoiding \(321\) restricts the layer sizes to \(1\) and \(2\). Hence members correspond bijectively to compositions of \(n\) with parts \(1,2\). Write their word of layer sizes over the alphabet \(\{1,2\}\), and let \(C_n=F_{n+1}\) be the number of such compositions, with \(F_1=F_2=1\).

For integers \(b\ge2\) and \(1\le j\le b\), define a word
\[
W_j=112(22)^{j-1}12(22)^{b-j}22.
\]
An exponent on a parenthesized word means ordinary word repetition. Each word has exactly \(3\) letters \(1\), exactly \(2b+2\) letters \(2\), \(2b+5\) layer symbols, and total layer-size weight \(4b+7\). The words are distinct. The cases \(a=0\) and \(a=b\) can be handled by the same construction or by always-false and always-true formulas.

## Proof
**1. Non-overlap and equal size.** Each \(W_j\) starts with \(11\), ends with \(2\), and has no occurrence of \(11\) after its first two symbols. Thus no nonempty proper suffix of any \(W_i\) equals a prefix of any \(W_j\): a suffix of length one ends in \(2\) rather than \(1\), while a suffix of length at least two cannot begin with \(11\). This is a *cross-bifix-free* family. All words have the same number of occurrences of each layer size and hence have the same total permutation weight.

**2. Exact bijection of first-occurrence classes.** Fix any total size \(n\ge0\). If a composition has a marked occurrence, let \(t\) be the least starting position (in the sequence of layers) of any \(W_j\). Its unique word of length \(2b+5\) beginning at \(t\) is \(W_i\) for exactly one \(i\). For any \(j\), replace those \(2b+5\) symbols by \(W_j\). The total size remains \(n\) because the words have equal weight. No new marked occurrence can start strictly before \(t\): an occurrence that overlaps the replacement from the left would force a nonempty proper suffix of a marked word to equal a prefix of \(W_j\), contradicting step 1. An occurrence fully to the left was absent already. Consequently the earliest marked occurrence is now \(W_j\) at \(t\). Replacing it again by \(W_i\) is the inverse. So if \(N_i(n)\) is the number of compositions with earliest marked pattern \(W_i\), then
\[
N_1(n)=N_2(n)=\cdots=N_b(n)
\]
for every \(n\), including those with no possible occurrence (when all counts are zero). Let \(H_b\) denote the event that some marked word occurs. Summing gives the exact equality \(\Pr(\text{earliest word is one of }W_1,\ldots,W_a)=(a/b)\Pr(H_b)\).

**3. First-order definability.** In a layered permutation with layer sizes at most two, the inversion relation \(I(x,y)\) defined by \(x<_{\mathrm{pos}}y\) and \(y<_{\mathrm{val}}x\) holds precisely for the ordered pair of points in a size-two layer. Define the layer representative predicate \(R(x)\) by saying that there is no \(y\) with \(I(y,x)\). For a representative \(x\), its layer has size two iff \(\exists y\,I(x,y)\), otherwise size one. The relation \(\operatorname{NextR}(x,y)\) means that \(x,y\) are representatives, \(x<_{\mathrm{pos}}y\), and no other representative lies strictly between them in the position order. These are all first-order formulas. For each fixed finite layer word \(W_j\), a first-order formula \(\operatorname{Occ}_j(x)\) asserts that \(x\) begins a chain of \(2b+5\) successive representatives with the prescribed singleton/doubleton predicates. The sentence \(\Phi_{a,b}\) says that some \(\operatorname{Occ}_i(x)\), with \(1\le i\le a\), holds and that no \(\operatorname{Occ}_j(y)\), with \(1\le j\le b\), starts strictly before \(x\). This is a single first-order two-order sentence for each fixed \(a,b\).

**4. Occurrence tends to certainty.** For a prescribed prefix of \(k\) layer symbols with total size \(s\), its probability under the uniform composition of \(n\) (for \(n\ge2k\)) equals \(C_{n-s}/C_n\). Using the Fibonacci asymptotics, the probability tends to \(\varphi^{-s}\), where \(\varphi=(1+\sqrt5)/2\). Thus every fixed number of initial layer sizes converges jointly to independent letters with probabilities \(p=\varphi^{-1}\) for \(1\) and \(q=\varphi^{-2}\) for \(2\), and \(p+q=1\). Under this limiting product measure, the probability that \(W_1\) occurs in none of the first \(m\) disjoint blocks of \(2b+5\) layer symbols is exactly
\[
\left(1-p^3q^{2b+2}\right)^m\xrightarrow[m\to\infty]{}0.
\]
The same upper bound follows for \(\limsup_{n\to\infty}\Pr(\neg H_b)\) for each fixed \(m\). Letting \(m\to\infty\) proves \(\Pr(H_b)\to1\). Together with steps 2 and 3 this gives \(\lim\Pr(\Phi_{a,b})=a/b\). The endpoints \(0,1\) are trivially first-order realizable, completing the claim for all rationals in \([0,1]\).

## Verification
The standalone standard-library `checker.py` constructs the cross-bifix-free word families and checks their equal letter counts for every \(2\le b\le10\). It independently enumerates all compositions for \(b=2\), \(15\le n\le22\); \(b=3\), \(19\le n\le24\); and \(b=4\), \(23\le n\le26\), confirming equal earliest-occurrence counts for each of the \(b\) marked words. It additionally verifies the pattern-avoidance characterization on all compositions of orders at most \(10\). Execution prints `ALL_CHECKS_OK`. These finite checks supplement, but do not replace, the universal bijection and limiting argument above.

## Relationship to prior work
Braunfeld and Kukla established a first-order convergence law for layered permutations and related structures (2021/2022), but did not describe a full spectrum of limiting probabilities. Markström and Räty established general logical convergence for small classes by regular-language methods (2026). Falgas-Ravry, Markström, Räty and Skerman proved that every small permutation class with exponential growth has a *dense* set of first-order limiting probabilities (2026). The present theorem establishes exact containment of **every rational** in the limit spectrum of the specific Fibonacci class \(\operatorname{Av}(231,312,321)\), together with a finite-size equinumerosity mechanism. Density does not imply exact rational attainment; a rational generating function for each sentence does not imply that all rational values are attained.

## Limitations
The assertion is a lower inclusion, not a complete description of the limit spectrum. It does not claim that every real or every algebraic number is attainable. The construction needs two intrinsic linear orders and specifically the bounded-layer Fibonacci class. The first-order formulas grow with the prescribed denominator. No independently performed mathematical audit is claimed. Earlier equivalent exact-rational results under coding or first-hit pattern terminology remain a possible priority risk.

## References
1. V. Falgas-Ravry, K. Markström, E. Räty, F. Skerman, *On first-order limiting probabilities for small permutation classes*, arXiv:2610.34328v1, first posted 2026-10-25, especially Theorem 1.4 and §4, https://arxiv.org/abs/2610.34328.
2. K. Markström, E. Räty, *Logical isomorphism and logical limit laws for small permutation classes and regular languages*, arXiv:2610.22218v1, 2026, https://arxiv.org/abs/2610.22218.
3. S. Braunfeld, M. Kukla, *Logical Limit Laws for Layered Permutations and Related Structures*, Enumerative Combinatorics and Applications 2(4) (2022), #S4PP2, first publicly available 2021, https://doi.org/10.54550/ECA2022V2S4PP2.
