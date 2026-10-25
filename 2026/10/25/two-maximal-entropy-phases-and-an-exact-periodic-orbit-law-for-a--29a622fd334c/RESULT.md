# Two maximal-entropy phases and an exact periodic-orbit law for antisquare-good binary shifts

## Finding
Let \(X\subseteq\{0,1\}^{\mathbb Z}\) be the bi-infinite binary configurations having no factor \(u\overline u\) with \(|u|\ge2\), where \(\overline u\) exchanges zeros and ones. Equivalently, their only permitted antisquares are `01` and `10`. Let \(\sigma\) denote the left shift and \(P_n=|\{x\in X:\sigma^n x=x\}|\), for integers \(n\ge1\).

The complete periodic-orbit generating function is
\[
\boxed{\zeta_X(z)=\exp\!\left(\sum_{n\ge1}\frac{P_n}{n}z^n\right)=\frac{1}{(1+z^3)^2(1-z-z^3)^2}.}
\]
In particular, if \(S_0=3,S_1=S_2=1\), and \(S_n=S_{n-1}+S_{n-3}\) for \(n\ge3\), then
\[
\boxed{P_n=2S_n+6\mathbf1_{3\mid n}(-1)^{n/3}.}
\]
The number of primitive periodic shift-orbits of least period \(n\) is exactly \(n^{-1}\sum_{d\mid n}\mu(d)P_{n/d}\), where \(\mu\) is the number-theoretic Möbius function.

The space \(X\) has exactly **two ergodic invariant probability measures of maximal entropy**. They are exchanged by bit complementation, each has entropy \(\log\psi\), and all maximizing measures are their convex combinations; here \(\psi>1\) is the real root of \(\psi^3-\psi^2-1=0\). Their respective frequencies of the digit `1` are
\[
\boxed{\delta=\frac{1}{\psi^2(3\psi-2)}=0.1942540040\ldots,
\qquad1-\delta=0.8057459960\ldots .}
\]
This supplies a pair of complementary, digit-density-distinct entropy phases for a bit-complement-invariant pattern-avoidance condition.

## Assumptions and scope
A factor means a finite contiguous block. An antisquare is a word of the form \(u\overline u\) with nonempty \(u\). The forbidden orders are \(|u|\ge2\), with no bound on order. Periods refer to **labeled bi-infinite configurations** fixed by \(\sigma^n\), not necklaces, and all logarithms are natural. Periodic-point counts include points of least period dividing \(n\). The assertions concern the full good shift \(X\), including exceptional nonperiodic points, rather than only a finite-type approximation.

## Proof
**1. Reduction using established antisquare theory.** The minimal-antisquare classification of Baranwal–Currie–Mol–Ochem–Rampersad–Shallit (Theorem 11, [1]) lists `0011`, `1100`, `0110`, `1001` at order two and `010101`, `101010` at order three. Their Section 7 establishes that every higher-order minimal antisquare contains `001011` or `110100`. Thus, with

`F = {0011, 1100, 0110, 1001, 010101, 101010, 001011, 110100}`,

let \(Y\) be the two-sided shift avoiding all factors from `F`. Then \(Y\subseteq X\). If \(x\in X\setminus Y\), it must contain `001011` or `110100`. Proposition 18 of [1], together with complementation, forces such a configuration to be a shift of the heteroclinic word \({}^{\omega}0\,1\,0\,1^{\omega}\), or of its complement. In particular, no such configuration is periodic. The exceptional configurations comprise at most two countable, nonperiodic shift-orbits, so every shift-invariant probability measure gives them mass zero. Hence \(X\) and \(Y\) have exactly the same periodic points and invariant probability measures (identified by extension with zero mass to the exceptional orbits).

**2. Complete 20-state presentation and two phases.** Form the order-five de Bruijn graph with as vertices the binary length-five words not containing a member of `F`, and an edge \(v\to v_2v_3v_4v_5b\) for \(b\in\{0,1\}\) precisely when the six-letter word \(vb\) avoids `F`. Its 20 vertices split into exactly two disjoint strongly connected 10-vertex graphs. The zero-rich component has vertices

`00000 00001 00010 00100 00101 01000 01010 10000 10001 10100`

and its complete edge list, written as adjacency, is:

```
00000 : 00000 00001
00001 : 00010
00010 : 00100 00101
00100 : 01000
00101 : 01010
01000 : 10000 10001
01010 : 10100
10000 : 00000 00001
10001 : 00010
10100 : 01000
```

The other component is its letterwise complement. These lists have 14 edges per component, give all 20 admissible states, and have no cross-component edges. Each component is strongly connected and has a fixed-vertex loop (`00000` or `11111`); hence each is primitive and defines a topologically mixing subshift of finite type. Since the length-five block presentation is conjugate to the original shift, \(Y\) is the disjoint union of these two systems.

**3. Exact determinants, zeta function, and periodic points.** Let \(A\) be the \(10\times10\) zero-one adjacency matrix of the displayed component, in lexicographic state order. Row elimination, or the standalone exact-integer checker, gives
\[
\det(tI-A)=t^4(t^3+1)(t^3-t^2-1),\qquad
\det(I-zA)=(1+z^3)(1-z-z^3).
\]
The complement component has a permutation-similar matrix. A period-\(n\) point corresponds bijectively to a closed walk of length \(n\) in the five-block graph, so \(P_n=2\operatorname{tr}(A^n)\). The matrix identity \(\exp(\sum_{n\ge1}\operatorname{tr}(A^n)z^n/n)=1/\det(I-zA)\) proves the stated zeta formula. Newton sums for \(t^3-t^2-1\) are the sequence \(S_n\); the sum of the \(n\)-th powers of the three roots of \(t^3+1\) equals \(3(-1)^{n/3}\) when \(3\mid n\) and zero otherwise. This proves the formula for \(P_n\), and Möbius inversion gives the primitive-orbit count.

**4. Maximal entropy and quantitative symmetry breaking.** Both components have the same Perron eigenvalue \(\psi\), the unique positive real root above one of \(t^3-t^2-1\); all other characteristic roots have smaller absolute value. The primitive finite-state Perron–Frobenius theorem therefore gives one and only one entropy-maximizing ergodic measure per component, each with entropy \(\log\psi\). Every invariant probability measure on \(X\) gives the exceptional shift-orbits zero mass, so no additional maximizing measure exists. The full set of maximizing measures is the segment joining the two component measures.

To compute the digit density, weight each directed edge in the displayed component by \(y\) if it appends `1`, and by \(1\) otherwise; call the matrix \(A(y)\). The explicit edge list gives the **polynomial identity**
\[
\det(tI-A(y))=t^4(t^3+y)(t^3-t^2-y).
\]
For \(y=e^s\) near one, the maximal eigenvalue \(\lambda(s)\) therefore solves \(\lambda^3-\lambda^2-e^s=0\). Differentiating the finite-state pressure \(\log\lambda(s)\) at \(s=0\) yields the expected digit-one frequency in the Parry measure:
\[
\delta=\left.\frac{d}{ds}\log\lambda(s)\right|_{s=0}
=\frac{1}{\psi^2(3\psi-2)}.
\]
Bit complementation interchanges the phases and the digit-one/digit-zero frequencies.

## Verification
Run the included `verify.py` with Python 3 (standard library only). It regenerates the 20 states and 28 edges, verifies exactly two complementary strongly connected 10-state components, proves the unweighted characteristic polynomials by exact Faddeev–LeVerrier arithmetic, and proves the weighted polynomial identity by checking 11 integer values of \(y\). Each polynomial coefficient has degree at most 10 in \(y\), so 11 exact evaluations are an identity certificate, not a numerical fit.

The checker also directly enumerates all labeled period-\(n\) binary configurations for \(1\le n\le14\), checks all possible forbidden antisquare orders using periodic reduction, compares against the eight finite forbidden patterns, and verifies adjacency-matrix traces and the closed recurrence. The counts are

`2, 2, 2, 10, 12, 26, 30, 42, 56, 92, 134, 202, 288, 422`.

## Relationship to prior work
Theorem 11, Proposition 18, and Theorem 19 of [1] supply the crucial minimal-antisquare and exceptional-word classifications, plus the **already known** good-word growth constant \(\psi\). The growth constant and finite forbidden-pattern reduction are not claimed as new. The contribution here is the explicitly evaluated full bi-infinite **periodic-point zeta function**, the proof of exactly **two** ergodic maximal-entropy phases, and their different exact symbol densities. The finite-state proof relies on, and goes quantitatively beyond, that earlier combinatorial classification. Generic Perron–Frobenius and matrix-zeta identities are standard mathematical tools, not new lemmas.

## Limitations
The theorem is restricted to binary words permitting only antisquares of order one, with two-sided symbolic dynamics. It does not classify periodic orbits under arbitrary larger allowable antisquare sets, nor does it determine a complete list of all invariant measures. Its originality assessment is literature-based rather than an independent certification; the published finite forbidden-pattern description makes some of the calculations accessible to standard finite-state methods. The companion checker verifies the finite certificates, not the published minimal-antisquare or exceptional-word theorems from scratch.

## References
[1] A. Baranwal, J. Currie, L. Mol, P. Ochem, N. Rampersad, and J. Shallit, *Antisquares and Critical Exponents*, Discrete Mathematics & Theoretical Computer Science 25:2 (2023), Article 11; earliest public preprint 2022-09-20, arXiv:2209.09223, DOI:10.46298/dmtcs.10063. Theorem 11, Proposition 18, and Theorem 19, especially Sections 6–7.
[2] S. Baker and A. Ghenciu, *Dynamical properties of S-gap shifts and other shift spaces*, Journal of Mathematical Analysis and Applications 430 (2015), 633–647, DOI:10.1016/j.jmaa.2015.04.092 (general dynamical context; not the source of the present specific orbit formulas).
