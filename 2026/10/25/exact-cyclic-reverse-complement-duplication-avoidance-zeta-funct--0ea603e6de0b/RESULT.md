# Exact cyclic reverse-complement-duplication avoidance zeta function for the DNA alphabet

## Finding
For the four-letter alphabet \(\Sigma=\{0,1,2,3\}\) with complement \(\overline a=3-a\), count circular words of every length whose periodic extension avoids the length-four reverse-complement duplication blocks \(ab\overline b\overline a\). Such blocks are precisely the outputs of a length-two reverse-complement duplication of \(ab\). Denote by \(a_n\) the number of **labeled** length-\(n\) words satisfying this condition; rotations remain separate when they give distinct strings.

Define the integer polynomial
\[
\begin{aligned}
Q(z)={}&(1-z)^3(1+z)^3(1+z^2)^2\\
&\cdot(1-3z-2z^2-3z^3)\\
&\cdot(1-z+z^2-4z^3+2z^4-3z^5)^2\\
&\cdot(1+z+z^2+4z^3+2z^4+3z^5).
\end{aligned}
\]
The **exact all-length circular-avoidance result** is
\[
\boxed{\exp\!\left(\sum_{n\ge1}\frac{a_n}{n}z^n\right)=\frac1{Q(z)},\qquad
\sum_{n\ge1}a_nz^n=-\frac{zQ'(z)}{Q(z)}.}
\]
The first ten \(a_n\) are
\[
4,12,64,228,744,2904,10420,39012,145900,546792.
\]
The corresponding counts \(N_n\) of cyclic rotation classes are
\[
4,8,24,62,152,500,1492,4910,16228,54760.
\]
For every positive length \(n\), both the total and primitive necklace counts are explicitly
\[
\boxed{N_n=\frac1n\sum_{d\mid n}\varphi(d)a_{n/d},\qquad
P_n=\frac1n\sum_{d\mid n}\mu(d)a_{n/d}.}
\]
Thus the entire circular and aperiodic-cycle census is determined with no cutoff. The dominant exponential growth is governed by the unique positive root \(\alpha\) of \(x^3-3x^2-2x-3=0\), approximately \(3.7473465403\). More precisely \(a_n=\alpha^n+O(1.721^n)\), and \(N_n\sim\alpha^n/n\). The dominant root itself is shared with the pre-existing linear irreducible-word enumeration; the new content is the **complete periodic trace and rotation-orbit census**, including the additional spectral factors.

## Assumptions and scope
The complement must be an involution without fixed letters on four symbols. Every such involution is equivalent by a permutation of the alphabet to \(0\leftrightarrow3\), \(1\leftrightarrow2\); therefore these counts are complement-label independent. For \(n\ge1\), evaluate a cyclic factor of length four in the bi-infinite repetition \(w^\mathbb{Z}\), with indices modulo \(n\), even when \(n<4\). When \(n\ge4\), absence of the forbidden factors is equivalent to absence of a cyclic inverse of a genuine length-two reverse-complement duplication. For shorter periods this is a **periodic-extension avoidance** definition, not a claim about physically deleting four symbols from a shorter word. The objects are circular strings, not error-correcting codebooks and not the general set of all reachable duplication descendants.

## Proof
For every state \((a,b,c)\in\Sigma^3\), create a directed edge to \((b,c,d)\) exactly when \((a,b,c,d)\ne (a,b,\overline b,\overline a)\). Equivalently the edge is present unless \(c=\overline b\) and \(d=\overline a\). Let \(A\) be this completely explicit \(64\)-by-\(64\) zero-one adjacency matrix, with states indexed by \(16a+4b+c\). Each admissible periodic word of length \(n\) corresponds bijectively to a closed walk of length \(n\) in this graph, **with a labeled starting coordinate**: the state at coordinate \(i\) consists of the three cyclic symbols starting there. This bijection holds also for \(n=1,2,3\) using periodic extension. Therefore \(a_n=\operatorname{tr}(A^n)\) for every \(n\ge1\).

Exact integer-matrix arithmetic gives the characteristic polynomial
\[
\begin{aligned}
\det(xI-A)={}&x^{36}(x-1)^3(x+1)^3(x^2+1)^2\\
&\cdot(x^3-3x^2-2x-3)\\
&\cdot(x^5-x^4+x^3-4x^2+2x-3)^2\\
&\cdot(x^5+x^4+x^3+4x^2+2x+3).
\end{aligned}
\]
This identity is not an assumed factorization: the included standalone checker derives all \(64\) traces by exact sparse matrix multiplication, reconstructs **every** characteristic-polynomial coefficient using Newton identities, and compares all coefficients to the displayed factorization. Newton's identity for monic coefficients \(c_0=1\) is
\[
c_k=-\frac1k\sum_{j=1}^k c_{k-j}\operatorname{tr}(A^j),\qquad 1\le k\le64.
\]
All divisions are exact and checked. Replacing \(x\) with \(1/z\) and multiplying by \(z^{64}\) yields \(\det(I-zA)=Q(z)\): the zero eigenvalues do not contribute. Formally, \(-\log\det(I-zA)=\sum_{n\ge1}\operatorname{tr}(A^n)z^n/n\). Differentiation proves both generating-function identities for all \(n\).

Every length-\(n\) admissible word of least period \(m\mid n\) is an \(n/m\)-fold repetition of a unique primitive length-\(m\) word. Möbius inversion on the divisor lattice yields the primitive labeled count \(\sum_{d\mid n}\mu(d)a_{n/d}\); every primitive orbit has \(n\) members. Burnside's rotation lemma gives \(N_n=n^{-1}\sum_{d\mid n}\varphi(d)a_{n/d}\). Both count formulas therefore follow independently of any finite cutoff.

The spectral factors show that the cubic's positive root \(\alpha\) has larger modulus than the other nonzero eigenvalues; those have moduli at most \(1.720177\), as can be checked by isolating the roots of the displayed degree-five and lower factors. The coefficient of \(\alpha^n\) in the trace is one. Hence the stated exponential estimates; the nonprimitive rotation terms contribute \(O(n\alpha^{n/2})\), negligible relative to \(\alpha^n\).

## Verification
Run \(\texttt{python3 rc2_periodic_checker.py}\) in a standard Python 3 environment. The program uses no third-party packages. It constructs the graph directly from the forbidden-factor definition; calculates \(\operatorname{tr}(A^n)\) for all \(1\le n\le64\); reconstructs the exact characteristic polynomial by Newton identities; and checks every coefficient of the explicit product. It separately enumerates every four-letter word through length seven, testing cyclic length-four factors directly. It verifies necklace-integrality identities through length twenty-four. All checks completed successfully with the printed marker `RC2_Q4_CYCLIC_PASS`. Finite direct word enumeration corroborates the graph model; **the infinite-length proof comes from the verified matrix identity and formal trace and orbit identities**, not from checking only finite initial terms.

## Relationship to prior work
Ben-Tolila and Schwartz introduced and analyzed the reverse-complement string-duplication system and characterized the **binary linear** irreducibles for block length two; that is the central motivating source, not a claim of a new duplication operator. The exact **linear**, all-even-alphabet irreducible-word generating function is also known and has dominant denominator \(1-(q-1)z-(q-2)z^2-(q-1)z^3\). Counting paths with open boundaries does **not** yield the trace enumeration of periodic points: it omits the cyclic boundary conditions and the extra degree-five and cyclotomic factors displayed here. For example, at four symbols and length four, the ordinary linear-avoidance count is \(240\), whereas the exact periodic-avoidance count is \(228\). Yohananov and Schwartz subsequently treated duplication-correcting **code capacity**, not these periodic orbit multiplicities. Yu and Schwartz studied duplication-free codes under **tandem**, rather than reverse-complement, duplication rules. The finite-state and Burnside techniques are standard; the explicit quaternary cyclic characteristic factorization and resulting all-length periodic and necklace census are the result asserted here.

## Limitations
This work is restricted to a four-letter alphabet and reverse-complement duplication length two. The result does not imply an optimal duplication-correcting code size, a root-uniqueness theorem for arbitrary descendants, or estimates for actual biological mutation rates. The fully periodic convention at lengths below four differs from operational reducibility for short circular molecules. The Perron cubic and its growth constant are not claimed as new, since linear enumerations already exhibit that root. The novelty comparison is best-knowledge rather than proof of worldwide uniqueness; equivalent unindexed periodic-point counts may exist.

## References
1. E. Ben-Tolila and M. Schwartz, *On the Reverse-Complement String-Duplication System*, arXiv:2112.11811v1 (first public version 2021-12-22), https://arxiv.org/pdf/2112.11811 . Section IV.A, especially Lemma 5, discusses binary linear irreducibles; Section IV.B discusses cyclic factor statistics but not this periodic census.
2. L. Yohananov and M. Schwartz, *On the Coding Capacity of Reverse-Complement and Palindromic Duplication-Correcting Codes*, arXiv:2312.00394v1 (2023-12-01), https://arxiv.org/pdf/2312.00394 .
3. W. Yu and M. Schwartz, *On Duplication-Free Codes for Disjoint or Equal-Length Errors*, arXiv:2401.04675v1 (2024-01-09), https://arxiv.org/pdf/2401.04675 .
