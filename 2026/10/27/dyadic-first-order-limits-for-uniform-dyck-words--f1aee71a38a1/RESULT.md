# Dyadic First-Order Limits for Uniform Dyck Words

## Finding
Let \(D_n\) be uniformly distributed over all Dyck words of length \(2n\), with up-step `U`, down-step `D`, and nonnegative height at each prefix. Represent the word as a finite relational structure with its directed immediate-successor relation and one unary predicate identifying `U` positions. Then every first-order sentence \(\varphi\) has a limiting probability \(p_\varphi\), effectively computable from \(\varphi\), and
\[
\{p_\varphi:\varphi\text{ a first-order sentence}\}
=\mathbb Z[1/2]\cap[0,1].
\]
Moreover \(\Pr(D_n\models\varphi)=p_\varphi+O_\varphi(n^{-1})\). If \(p_\varphi=0\), the probability is \(O_\varphi(e^{-c_\varphi n})\) for some \(c_\varphi>0\); if \(p_\varphi=1\), the same exponential bound holds for the failure probability. In particular the model has a convergence law but not a zero-one law: the sentence asserting that the first two symbols are `UD` has limit \(1/4\).

The mechanism is an explicit product law for finite endpoint windows. If \(u\) is a nonnegative up/down prefix of length \(a\) and height \(h(u)\), and \(v\) is a suffix of length \(b\) whose reversed, up/down-swapped word is nonnegative of height \(h^*(v)\), then
\[
\lim_{n\to\infty}\Pr(D_n\text{ begins with }u\text{ and ends with }v)
=\frac{(h(u)+1)(h^*(v)+1)}{2^{a+b}}.
\]
Thus the two boundary windows become independent, although the full word is globally balanced and conditioned to remain nonnegative.

## Assumptions and scope
A Dyck word is a word \(w=w_1\cdots w_{2n}\in\{U,D\}^{2n}\) with \(\#U=\#D=n\) and nonnegative prefix heights \(\sum_{i\le j}(\mathbf1_{\{w_i=U\}}-\mathbf1_{\{w_i=D\}})\). Each of the Catalan number \(C_n=\binom{2n}{n}/(n+1)\) admissible words receives probability \(1/C_n\).

The signature is \(\{S,P\}\), where \(S(i,j)\) means \(j=i+1\) and \(P(i)\) means position \(i\) contains `U`. There is equality, but no total order predicate, matching relation, height, arithmetic, or counting quantifier. The first and last positions are first-order definable using \(S\). All assertions concern fixed first-order sentences as \(n\to\infty\), with even word length \(2n\); constants in error bounds depend on the sentence.

## Proof
**1. Boundary counts.** For nonnegative integers \(x,y\) and an integer \(t\ge0\) of compatible parity, the reflection principle gives the number of nonnegative nearest-neighbour walks of length \(t\) from height \(x\) to height \(y\):
\[
B_t(x,y)=\binom{t}{(t+y-x)/2}-\binom{t}{(t+y+x+2)/2},
\]
where a binomial coefficient with nonintegral or out-of-range lower index is zero. For a fixed admissible prefix \(u\) and suffix \(v\) as above, the exact number of Dyck words with these boundaries is \(B_{2n-a-b}(h(u),h^*(v))\), once their windows are disjoint. Reflection plus the central-binomial Stirling expansion at fixed offsets gives
\[
\frac{B_{2n-a-b}(h(u),h^*(v))}{C_n}
=\frac{(h(u)+1)(h^*(v)+1)}{2^{a+b}}+O_{u,v}(n^{-1}).
\]
All these limiting cylinder probabilities are strictly positive. Summing over all allowed windows confirms that they form probability distributions; the two factors separately sum to one.

**2. Abundance of every finite interior pattern.** Fix a binary word \(t\) of length \(\ell\) and an integer multiplicity threshold \(T\). Under an *unconditioned* uniform binary word of length \(2n\), choose \(\Theta(n)\) disjoint \(\ell\)-letter blocks at distance at least any prescribed fixed \(K\) from either endpoint. The number equal to \(t\) is binomial with success probability \(2^{-\ell}\). Hence its chance of being less than \(T\) is \(O(e^{-cn})\). The Dyck conditioning event has unconditioned probability \(C_n/2^{2n}=\Theta(n^{-3/2})\), so after conditioning the failure probability remains \(O(e^{-c'n})\). A union bound handles every binary \(\ell\)-word simultaneously. Consequently, for each fixed neighbourhood radius and threshold, every full-radius interior neighbourhood type occurs at least that threshold with exponentially high probability.

**3. Reduction of first-order truth to boundary windows.** The Gaifman graph of \(S\) is a path of degree at most two. Effective bounded-degree Hanf locality supplies, for each \(\varphi\), a finite radius \(r\) and integer threshold \(T\): two sufficiently long coloured paths whose counts of every radius-\(r\) pointed neighbourhood agree below \(T\), or are both at least \(T\), satisfy exactly the same \(\varphi\). Choose \(K>2r\). Full-radius interior types have counts at least \(T\) with exponentially high probability by Step 2; all truncated endpoint neighbourhood types are determined by the first and last \(K\) letters. Thus, outside an exponentially rare event, the truth of \(\varphi\) is a Boolean function of those two endpoint words. This Boolean function is effective: compute the Hanf parameters, enumerate the finitely many admissible endpoint pairs, search for a finite Dyck completion that realizes both boundaries and saturates the finite set of interior types, and evaluate \(\varphi\) on it. Positive boundary-cylinder limits and Step 2 ensure each search terminates.

**4. Convergence and upper spectrum inclusion.** There is a finite set \(A_\varphi\) of admissible endpoint pairs such that, up to exponentially rare exceptions, \(\varphi\) holds precisely on their cylinder union. Consequently
\[
p_\varphi=\sum_{(u,v)\in A_\varphi}
\frac{(h(u)+1)(h^*(v)+1)}{2^{2K}}
\in\mathbb Z[1/2]\cap[0,1].
\]
The exact boundary expansion yields the claimed \(O_\varphi(n^{-1})\) rate. If the limit is zero, the sum contains no admissible pair because each summand is positive; the sentence can then hold only on the exponentially rare exceptional set. The analogous argument for its negation handles limiting probability one.

**5. Constructive converse: no dyadic number is missing.** Consider nonnegative prefixes \(u\) of any even length \(2m\), with \(m\ge2\). By Step 1 (with empty suffix), the limiting probability of an individual prefix is \((h(u)+1)/2^{2m}\). Their integer numerator weights total \(2^{2m}\). Every weight is odd, the weight \(1\) appears at least twice (the Catalan paths ending at zero), and each weight \(3,5,\ldots,2m+1\) occurs at least once. Sort the weights. Each weight is no greater than one plus the sum of its predecessors: for \(2j+1\), the preceding sum is at least \(2+3+5+\cdots+(2j-1)=j^2+1\ge2j\). The elementary subset-sum interval lemma then shows that every integer from \(0\) through \(2^{2m}\) is the sum of weights from a subset of the prefixes. A finite union of these prefix cylinders is definable in first-order logic using \(S\) and \(P\), and has the desired limiting mass. Given any dyadic number \(a/2^d\in[0,1]\), choose \(2m\ge d\), \(m\ge2\), and take a subset with numerator \(a2^{2m-d}\). This establishes the reverse inclusion and effective realization.

## Verification
The standalone `check_dyck_fo.py` independently enumerates all Dyck words through semilength nine, compares exact joint endpoint counts with the reflection formula, verifies the complete subset-sum property at six even prefix lengths, and checks 121 two-boundary asymptotics using exact binomial coefficients at semilength 5000. Executing it with Python 3 produces:

`DYCK_FO_EXACT_OK 6917 1083 4704 121`

The four integers are the number of enumerated Dyck words, exact cylinder equalities, total numerator weights examined, and large-size boundary comparisons. These finite tests are not a substitute for the reflection/Stirling, conditional concentration, Hanf locality and all-length subset-sum arguments in the proof.

## Relationship to prior work
Markström and Räty (arXiv:2610.22218v1, 2026) prove logical convergence for small permutation classes via regular-language encodings and discuss applications to regular words. Dyck words form a nonregular language, and the present theorem is for the successor-and-letter signature on Dyck words, not the two-order logic of a pattern-avoiding permutation. Their discussion of Dyck bijections does not identify the present exact arithmetic spectrum.

Albert, Bouvel, Féray and Noy (arXiv:2210.05537, first public 2022) prove a first-order limit law and density of limiting probabilities for 231-avoiding permutations in the **two-order** language. A bijection with Dyck paths by itself does not preserve first-order definability in the binary successor/letter language; this is a different claim. Koponen (arXiv:2610.16163v1, 2026) discusses constraints relevant to first-order convergence laws for random expansions; this paper motivates examining a concrete conditioned finite-model family but is not invoked as a covering result.

The reflection principle, Catalan asymptotics, classical conditioning of random-walk excursions, and Hanf locality are standard ingredients, not claimed as discoveries. The distinct contribution assessed here is their combination into a complete effective first-order probability classification and sharp zero-limit dichotomy for the globally constrained Dyck-word model. The same numerical set of dyadic probabilities occurs in simpler unrestricted-word examples; equality of this set is not itself claimed as a novel abstract arithmetic discovery.

## Limitations
No statement is made for signatures containing the full order \(<\), matching-parenthesis edges, arithmetic on positions, height functions or monadic second-order quantifiers; these can observe much more of the path. The error constants are sentence-dependent and the effective procedure may be impractically expensive. No uniqueness or historical-priority certification is asserted: a more general unpublished or unlocated theorem on random conditioned words might imply the result. The mathematical review is not independent validation.

## References
- K. Markström and E. Räty, *Logical isomorphism and logical limit laws for small permutation classes and regular languages*, arXiv:2610.22218v1, first public 2026-10-15, especially Introduction and Theorem 1.
- V. Koponen, *A characterization of the finite model property for \(\omega\)-categorical theories*, arXiv:2610.16163v1, first public 2026-10-12, mathematical classification 03C13.
- M. Albert, M. Bouvel, V. Féray, M. Noy, *A logical limit law for 231-avoiding permutations*, arXiv:2210.05537, first public 2022-10-11, *Discrete Mathematics & Theoretical Computer Science* 26 (2024).
- D. Kuske and N. Schweikardt, *First-Order Logic with Counting: At Least, Weak Hanf Normal Forms Always Exist and Can Be Computed!*, arXiv:1703.01122 (2017), for effective bounded-degree locality.
- Classical reflection principle and Stirling asymptotics for Catalan/Dyck excursions (standard combinatorics).
