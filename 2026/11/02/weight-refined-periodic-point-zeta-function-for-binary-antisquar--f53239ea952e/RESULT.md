# Weight-refined periodic-point zeta function for binary antisquare avoidance

## Finding

A binary *antisquare* is a word \(v\overline v\), where \(\overline v\) exchanges zero and one. A binary bi-infinite word is *good* if it has no antisquare with \(|v|\ge2\). Let \(\mathcal G_n\) be the set of indexed binary strings \(w\) of length \(n\ge1\) whose bi-infinite periodic extension \(w^{\mathbb Z}\) is good. Put
\[
P_n(u)=\sum_{w\in\mathcal G_n}u^{|w|_1}.
\]
Here indexed strings are counted separately, but rotations with identical strings are not artificially distinguished.

**Theorem.** As a formal power series in \(z\) with polynomial coefficients in \(u\),
\[
\boxed{\exp\left(\sum_{n\ge1}\frac{P_n(u)}{n}z^n\right)=
\frac{1}{(1-z-uz^4-u^2z^6)(1-uz-u^3z^4-u^4z^6)}.}
\]
Every nonconstant periodic good word has either exclusively long zero-runs or exclusively long one-runs, where *long* means length at least three. In the former case it has, cyclically, a unique decomposition into blocks \(0^k1\) and \(0^k101\) with \(k\ge3\); the latter case is its bitwise complement. Consequently its relative number of ones lies in \([0,1/3]\) or \([2/3,1]\). Equality at either nonconstant boundary is possible precisely if \(6\mid n\): the indexed words at the \(1/3\) boundary are the six rotations of \((000101)^{n/6}\), and those at the \(2/3\) boundary are their six complements.

Putting \(u=1\), the number \(C_n=|\mathcal G_n|\) satisfies
\[
\sum_{n\ge1}\frac{C_n}{n}z^n=-2\log(1-z-z^4-z^6),
\qquad C_n=C_{n-1}+C_{n-4}+C_{n-6}\quad(n\ge7),
\]
with \((C_1,\ldots,C_6)=(2,2,2,10,12,26)\). The first sixteen values are \(2,2,2,10,12,26,30,42,56,92,134,202,288,422,612,906\).

Let \(\mu\) denote the Möbius function. The weight enumerator \(L_n(u)\) of *primitive rotation necklaces* (least period exactly \(n\)) is exactly
\[
\boxed{L_n(u)=\frac1n\sum_{d\mid n}\mu(d)P_{n/d}(u^d).}
\]
The coefficient of \(u^j\) counts primitive necklaces of length \(n\) and weight \(j\), without identifying bitwise complements or reversals.

## Assumptions and scope

All lengths \(n\) are positive integers. The alphabet is labeled \(\{0,1\}\); antisquares of order one, \(01\) and \(10\), are permitted. The forbidden pattern condition is imposed on the entire bi-infinite periodic extension, so factors are allowed to cross the length-\(n\) boundary or repeat around it. The variable \(u\) records the number of ones in the indexed period, not the number of cyclic rotations. A rational dynamical zeta function here means the displayed formal exponential, with no analytic convergence assertion needed.

## Proof

**1. Reduction to eight forbidden factors.** Baranwal–Currie–Mol–Ochem–Rampersad–Shallit [1, Theorem 11] determine the minimal antisquares. In particular, every minimal forbidden antisquare of order at least four has the factor \(001011\) or its complement \(110100\); those of orders two and three are respectively \(0011,0110,1001,1100\) and \(010101,101010\). Their Proposition 18 states that a bi-infinite good word containing \(001011\) must have a nonperiodic one-sided-constant form. Its bitwise complement gives the same conclusion for \(110100\). Consequently, for a periodic bi-infinite binary word, goodness is **equivalent** to avoidance of the finite set
\[
\mathcal F=\{0011,0110,1001,1100,010101,101010,001011,110100\}.
\]
The forward implication uses the periodicity obstruction in Proposition 18; the reverse implication uses the complete minimal-antisquare classification. It would not be valid to impose those last two non-antisquare patterns on arbitrary finite good words.

**2. Complete periodic run grammar.** The all-zero and all-one periods are good. Consider a nonconstant period \(w\), so every maximal cyclic run is bounded on both sides by the other symbol. A run of exactly two zeros would yield \(1001\), and a run of exactly two ones would yield \(0110\); both are forbidden. Thus all cyclic runs have length one or at least three. Consider two consecutive long runs in cyclic order (meaning there is no long run between them). If their symbols differ, there are an even number of intervening singleton runs. With zero singleton runs one gets \(0011\) or \(1100\); with two one gets \(001011\) or \(110100\); with four or more one gets a forbidden length-six alternating factor. Therefore no two consecutive long runs can differ in symbol, and hence all long runs have the same symbol. If there were no long run, the sequence would be alternating and hence contain a forbidden length-six alternating word. Thus there is at least one long run, and all long runs have the same symbol.

Assume the long runs consist of zeros. Every one-run is then a singleton. Between consecutive long zero-runs the intermediate singleton runs alternate, beginning and ending with one-runs, so there is an odd number of them. Five or more intermediate singleton runs would contain a length-six alternating factor. Therefore there are exactly one or three intermediate singleton runs. Starting each block at a long zero-run gives the unique cyclic block grammar \(0^k1\) and \(0^k101\), \(k\ge3\), with the long run fixing each block boundary. The complementary long-one class is disjoint.

Conversely, each such cyclic concatenation avoids \(\mathcal F\): it has no adjacent ones, no zero-run of length two, no six alternating consecutive symbols, and therefore avoids the first six patterns. The last two patterns contain \(11\), so they too are absent. Thus every word in these classes is good. The constants exhaust the remaining words.

**3. Rooted-block enumeration.** A block in the long-zero class has length-and-weight generating series
\[
f_0(z,u)=\sum_{k\ge3}\bigl(u z^{k+1}+u^2z^{k+3}\bigr)
=\frac{uz^4+u^2z^6}{1-z}.
\]
The complement class has
\[
f_1(z,u)=\sum_{k\ge3}\bigl(u^k z^{k+1}+u^{k+1}z^{k+3}\bigr)
=\frac{u^3z^4+u^4z^6}{1-uz}.
\]
For a fixed number \(r\ge1\) of long runs, an indexed word counted in \(P_n(u)\) has exactly \(r\) choices of a marked long-run start among its \(n\) positions. On the other hand, an ordered \(r\)-tuple of blocks together with a choice of the marked start position determines one such marked indexed word. This is a bijection, including for words with nontrivial rotational period. Therefore the contribution to \(\sum_{n\ge1}P_n(u)z^n/n\) with exactly \(r\) long runs is \((f_0^r+f_1^r)/r\). Summing \(r\) and adding the two constant words at every length gives
\[
\begin{aligned}
\sum_{n\ge1}\frac{P_n(u)}{n}z^n
&=-\log(1-z)-\log(1-uz)\\
&\quad-\log(1-f_0(z,u))-\log(1-f_1(z,u))\\
&=-\log(1-z-uz^4-u^2z^6)\\
&\quad-\log(1-uz-u^3z^4-u^4z^6).
\end{aligned}
\]
Exponentiation proves the stated rational zeta identity.

**4. Counts, primitive necklaces, and sharp density boundary.** At \(u=1\) both denominator factors coincide. Differentiating the logarithmic identity in \(z\) (or expanding the roots of the reciprocal denominator) gives the order-six recurrence and listed initial values. Every periodic word with least period \(e\mid n\) is an \((n/e)\)-fold repetition of a primitive period-\(e\) word, multiplying its Hamming weight by \(n/e\). Möbius inversion, with each primitive necklace contributing exactly \(e\) indexed words, gives \(L_n(u)=n^{-1}\sum_{d\mid n}\mu(d)P_{n/d}(u^d)\).

A long-zero block \(0^k1\) contains one one in at least four positions; a long-zero block \(0^k101\) contains two ones in at least six positions. Hence every weighted average of their densities is at most \(1/3\). Equality forces every block to have the latter form with \(k=3\), so the period is a repetition of \(000101\) and \(6\mid n\). That length-six word has least period six, producing exactly six indexed rotations for each multiple of six. Bitwise complementation gives the other side. The constants have densities zero or one. This proves both the forbidden central density interval and its sharp boundary.

## Verification

The standalone Python 3 standard-library program `verify.py` computes the bivariate coefficients directly from the two rational denominator factors. Independently, it enumerates every indexed binary string for \(1\le n\le14\) and compares (i) direct antisquare testing for orders \(2\) through \(n+1\), (ii) all eight forbidden factors, (iii) the cyclic run grammar, and (iv) each weight-enumerator coefficient. It further compares primitive necklace weight profiles with a direct rotation-orbit enumeration for \(1\le n\le12\), and checks count recurrence and support constraints through \(n=80\). It reports `VERIFY_OK` and `SOURCE_WORDS_CHECKED 32766`. Direct finite testing does not attempt arbitrarily large antisquare orders: the published minimal-antisquare theorem and Proposition 18 prove the all-order equivalence. The infinite-length result rests on the mathematical proof above, not these finite checks.

To reproduce: run `python3 verify.py` in the directory containing the supplied file. The program needs no network or nonstandard dependencies.

## Relationship to prior work

[1, Theorems 11 and 19, Proposition 18] gives the complete minimal-antisquare list, a periodicity obstruction and the exponential growth rate of arbitrary *linear* good words; its Pansiot-word proof already exhibits the unweighted recurrence characteristic polynomial. This result uses that groundwork and does **not** claim a new growth rate or recurrence polynomial. The present contribution is the exact **cyclic**, Hamming-weight-refined periodic-point zeta, the corresponding exact primitive rotation-necklace polynomials and the sharp achievable-density boundary.

[2] classifies small numbers of square/antisquare factors and provides infinite avoidance constructions, without this cyclic weight-resolved enumeration. [3] studies avoidance of complementary factors, a different constraint from antisquare avoidance. [4] studies circular binary words with only three permitted *squares*, and asks a counting question for that different language; it does not count antisquare-free periodic points. Standard block-cycle/necklace methods are used explicitly here rather than claimed new.

## Limitations

This theorem concerns *periodic* extensions only, not arbitrary finite words or nonperiodic infinite good words. It does not assert a formula for the number of linear good strings, identify reflection or complement necklaces, or improve the known growth exponent. The weighted rational formula could in principle be implicit in a different previously published finite-state presentation; the relevant works inspected do not explicitly supply its statement or implications. Novelty remains subject to independent literature review. Verification through finite lengths does not establish infinite correctness; the proof uses the published antisquare characterization and the demonstrated block bijection.

## References

[1] A. Baranwal, J. Currie, L. Mol, P. Ochem, N. Rampersad, J. Shallit, “Antisquares and Critical Exponents,” *Discrete Mathematics & Theoretical Computer Science* 25:2 (2023), arXiv:2209.09223, first publicly posted 2022-09-19, https://arxiv.org/abs/2209.09223, DOI:10.46298/dmtcs.10063. Especially Sections 6–7, Theorem 11, Proposition 18 and Theorem 19.

[2] T. Ng, P. Ochem, N. Rampersad, J. Shallit, “New Results on Pseudosquare Avoidance,” arXiv:1904.09157 (2019), https://arxiv.org/abs/1904.09157.

[3] J. Currie, Ľ. Dvořáková, P. Ochem, D. Opočenská, N. Rampersad, J. Shallit, “Complement Avoidance in Binary Words,” arXiv:2209.09598 (2022), https://arxiv.org/abs/2209.09598.

[4] J. D. Currie, J. T. Johnson, “Characterization of the lengths of binary circular words containing no squares other than 00, 11, and 0101,” arXiv:2005.09742 (2020), https://arxiv.org/abs/2005.09742.
