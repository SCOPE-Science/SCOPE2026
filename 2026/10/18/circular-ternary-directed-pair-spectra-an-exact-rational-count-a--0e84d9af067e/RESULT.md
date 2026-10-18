# Circular ternary directed-pair spectra: an exact rational count and connectivity deficit

## Finding
Let \(\Sigma=\{0,1,2\}\). For a nonempty circular word \(w=(w_0,\ldots,w_{n-1})\in\Sigma^n\), read indices modulo \(n\), and set
\[
M_{ab}(w)=\#\{i\in\{0,\ldots,n-1\}: w_i=a,\ w_{i+1}=b\},\quad a,b\in\Sigma.
\]
Define \(T(n)\) as the number of distinct nine-entry matrices \(M(w)\), where \(w\) ranges over all ternary circular words of length \(n\). Words differing by cyclic rotation have the same observation, but no identification of symbols or reversal is made. Periodic words are included; in particular a circular word of length one records a single loop.

For every \(n\ge1\), the exact counting series is
\[
\boxed{\begin{aligned}
\sum_{n\ge1}T(n)z^n={}&\frac{1+z^3}{(1-z)^3(1-z^2)^3(1-z^3)}-1\\
&-\frac{3z^2}{(1-z)^2}
-\frac{3z^3}{(1-z)^3(1-z^2)}
-\frac{z^3}{(1-z)^3}.
\end{aligned}}
\]
The first values, for \(n=1,\ldots,13\), are \(3,6,11,24,48,95,174,306,510,819,1266,1901,2775\). The counting function is eventually quasipolynomial of exact period \(6\) and degree \(6\), with
\[
T(n)=\frac{n^6}{8640}+O(n^5).
\]
In particular \(T(n)\) is the maximum size of a zero-error code of circular length-\(n\) ternary words when the observation channel reveals precisely the directed adjacent-pair multiplicities, without noise.

A sharper realization statement holds. Let \(B(n)\) count all \(3\times3\) matrices of nonnegative integers with total sum \(n\) and with each row sum equal to the corresponding column sum. These are the *balanced candidate spectra*, whether or not they are realizable by a single circular word. Then
\[
B(n)-T(n)=\frac{n^3}{4}+O(n^2),\qquad
1-\frac{T(n)}{B(n)}=\frac{2160}{n^3}+O(n^{-4}).
\]
Thus almost every balanced candidate is realizable, and the excluded proportion has a sharp cubic-order decay.

## Assumptions and scope
All claims concern a fixed **labeled three-letter alphabet**, all lengths \(n\ge1\), cyclic ordered pairs including the closing pair, and multiplicities rather than just distinct pair types. No restrictions on word primitivity or occurrence counts are imposed. The symbol \(z\) is a formal indeterminate; asymptotic estimates concern positive integer \(n\) tending to infinity. Balanced matrices include disconnected directed multigraphs and are not required to be spectra of a word.

## Proof
**Realizability criterion.** Interpret a nonnegative matrix \(M=(m_{ab})\) as a directed multigraph on \(\Sigma\), with \(m_{ab}\) edges from \(a\) to \(b\), loops permitted. The cyclic consecutive pairs of a word traverse every edge exactly once, giving an Euler circuit; the graph is balanced and its nonisolated vertices lie in a single weakly connected component. Conversely, a finite directed multigraph with these conditions has an Euler circuit, whose successive vertex labels form a circular word of length \(\sum m_{ab}\). Hence a nonzero matrix is realizable precisely when it is balanced and its active vertices (vertices incident to edges, including loops) are connected after directions are forgotten.

**Counting every balanced matrix.** The three diagonal entries are arbitrary and contribute \((1-z)^{-3}\). For off-diagonal entries, balance implies
\[
h=m_{01}-m_{10}=m_{12}-m_{21}=m_{20}-m_{02}\in\mathbb Z.
\]
When \(h\ge0\), the six entries are uniquely parametrized by \(u,v,w\ge0\) as
\[
(m_{01},m_{10})=(u+h,u),\quad
(m_{12},m_{21})=(v+h,v),\quad
(m_{20},m_{02})=(w+h,w).
\]
For \(h\le0\), reverse the orientation. The contributions from the two orientations coincide, and the \(h=0\) slice must be counted only once. Consequently the series for *all* balanced matrices, including the zero matrix, is
\[
F(z)=\frac{1}{(1-z)^3(1-z^2)^3}
\left(1+2\sum_{h\ge1}z^{3h}\right)
=\frac{1+z^3}{(1-z)^3(1-z^2)^3(1-z^3)}.
\]
This parametrization is bijective, not just a decomposition with possible multiplicities.

**Removing disconnected active supports.** Let \(S(z)=z/(1-z)\) count a nonempty loop-only component on one specified vertex. On two specified vertices, any balanced connected graph must have equal positive multiplicities on the two oppositely directed edges, and arbitrary loops. Its generating function is
\[
P(z)=\frac{z^2}{(1-z)^2(1-z^2)}.
\]
Every disconnected nonzero balanced matrix on three labeled vertices has exactly one of the following disjoint component types: two loop-only components and one inactive vertex (\(3S(z)^2\)); one connected two-vertex component plus one loop-only component (\(3P(z)S(z)\)); or three loop-only components (\(S(z)^3\)). There are no other cases: all nontrivial components have at least two vertices and three vertices cannot contain two such components. Removing the zero matrix and these three types gives
\[
\sum_{n\ge1}T(n)z^n=F(z)-1-3S(z)^2-3P(z)S(z)-S(z)^3,
\]
which is the asserted exact rational expression. A maximum zero-error code consists of one representative for each attainable matrix; two representatives with the same matrix are indistinguishable, proving the code-size statement.

**Quasipolynomial and asymptotic.** The reduced denominator divides \((1-z)^7(1+z)^2(1+z+z^2)\). Non-cancellation at primitive third roots of unity follows from the \(F(z)\) summand, while the pole of order \(2\) at \(z=-1\) also persists; therefore the eventual quasipolynomial has exact period \(6\). At \(z=1\),
\[
F(z)=\frac{1}{12(1-z)^7}+O((1-z)^{-6}),
\quad 3P(z)S(z)=\frac{3}{2(1-z)^4}+O((1-z)^{-3}).
\]
The other disconnected corrections are of pole order at most \(3\). Taking coefficients of these rational functions yields
\[
B(n)=\frac{n^6}{8640}+O(n^5),\quad
B(n)-T(n)=\frac{n^3}{4}+O(n^2),
\]
and division of these two estimates gives the stated \(2160/n^3+O(n^{-4})\) deficit fraction. The pole orders of the rational generating functions also justify the claimed error terms, including their oscillatory contributions. This completes the proof.

## Verification
The accompanying `verify.py` uses only the Python standard library. Running `python3 verify.py` checks the first fourteen rational-series coefficients, enumerates all \(3^n\) linear presentations of length-\(n\) circular words for \(1\le n\le9\), and independently enumerates connected balanced integer matrices using signed flows for \(1\le n\le14\). All checks passed. These finite checks corroborate the algebra; they do not substitute for the preceding all-\(n\) proof.

## Relationship to prior work
Bernardini et al. [1] study strings sharing a **set** of fixed-length substrings, with reductions and algorithms based on Eulerian walks; they explicitly distinguish the **multiset** observation and discuss its Euler-trail interpretation (their introduction, related-work discussion and flow preliminaries). They do not count possible ternary circular length-two multiset observations. Ota and Manada [2] consider exact substring frequencies for circular **binary** strings and give uniqueness/reconstruction criteria; their full paper is about reconstruction of a supplied instance rather than the cardinality of all ternary directed two-factor spectra. The Euler-circuit criterion is classical and is not claimed as new. The specific connected-circulation generating function and sharp asymptotic deficit are the contribution here.

## Limitations
The formula is restricted to directed length-two observations, circular words, and three labeled letters. It counts possible observation profiles, not the number of words realizing an individual profile and not error-correcting codes under a noisy channel. General alphabet sizes and longer reads are not classified. Relevant unpublished, unindexed, or differently described prior enumerations of connected balanced integer matrices might contain an equivalent formula; no uniqueness of discovery is claimed.

## References
[1] G. Bernardini, A. Conte, E. Gabory, R. Grossi, G. Loukides, S. P. Pissis, G. Punzi and M. Sweering, “On Strings Having the Same Length-k Substrings,” *CPM 2022*, LIPIcs 223, article 16, DOI: 10.4230/LIPIcs.CPM.2022.16 (publicly released June 22, 2022). Full open-access text: https://drops.dagstuhl.de/storage/00lipics/lipics-vol223-cpm2022/LIPIcs.CPM.2022.16/LIPIcs.CPM.2022.16.pdf.

[2] T. Ota and A. Manada, “A Reconstruction of Circular Binary String Using Substrings and Minimal Absent Words,” *IEICE Transactions on Fundamentals*, advance publication September 5, 2023, DOI: 10.1587/transfun.2023TAP0015. Full open-access text: https://www.jstage.jst.go.jp/article/transfun/advpub/0/advpub_2023TAP0015/_pdf/-char/en.
