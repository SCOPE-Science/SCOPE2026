# Exact weight-three binary three-deck equivalence and a conjectured generating function

## Finding
Let \(D_{3,3}(n)\) denote the number of distinct **three-decks**, i.e. multisets of scattered subsequences of length three including multiplicities, among binary words of length \(n\) containing exactly three ones. Then, for every integer \(n\geq3\),

\[
\sum_{n\geq3}D_{3,3}(n)z^n=\frac{z^3}{(1-z)^4}-\frac{z^7}{(1-z)^2(1-z^2)(1-z^4)}.
\]

This proves Conjecture 1 in Chrisnata, Kiah, Karingula, Vardy, Yaakobi and Yao, *On the number of distinct \(k\)-decks: Enumeration and bounds* (2021 online; 2023 volume), whose authors reported checking the first twenty coefficients.

A stronger structural assertion determines every ambiguity class. For nonnegative integers \(a,b,c,d\), let
\[
w(a,b,c,d)=0^a1\,0^b1\,0^c1\,0^d.\]
Its three-deck equivalence class has size at most two. A distinct partner exists **if and only if**
\[
b\ne c,\qquad b-c\in3\mathbb Z,\qquad a+\frac{b-c}{3}\geq0,\qquad d+\frac{c-b}{3}\geq0.
\]
When it exists, that partner is uniquely
\[
w\!\left(a+\frac{b-c}{3},\;c,\;b,\;d+\frac{c-b}{3}\right).
\]
The number \(P_n\) of two-word ambiguity classes, and hence of word pairs with identical three-decks, satisfies
\[
\sum_{n\geq3}P_nz^n=\frac{z^7}{(1-z)^2(1-z^2)(1-z^4)},\qquad
D_{3,3}(n)=\binom n3-P_n.
\]
There are exactly \(\binom n3-2P_n\) singleton classes and \(P_n\) doubleton classes. No larger class occurs. The first collision occurs at length seven, between `1000110` and `0110001`. Furthermore \(P_n=\frac{n^3}{48}+O(n^2)\); thus an asymptotic proportion \(1/4\) of fixed-weight-three words have a distinct three-deck-equivalent mate.

## Assumptions and scope
The alphabet is exactly \(\{0,1\}\). Every word considered in the theorem has exactly three positions marked \(1\), and four nonnegative **ordered** zero gaps. A scattered occurrence of pattern \(u=u_1\cdots u_j\) is an increasing tuple of indices of letters spelling \(u\), with multiplicities counted. Let \(\binom wu\) be its number of scattered occurrences. Equality of three-decks is equality of all eight numbers \(\binom wu\), \(u\in\{0,1\}^3\). Throughout \(n\) is an integer at least three. The generating function is a formal power series in \(z\); no analytic convergence assumption is used. For \(n<3\), there are no binary words of weight three and the coefficient is zero.

## Proof
**1. Necessary linear constraints.** Equality of three-decks at fixed \(n\) implies equality of each shorter scattered-pattern count: for a pattern of length \(j<3\), sum over all patterns of length three the occurrence multiplicity of the shorter pattern. Every chosen \(j\)-tuple lies in exactly \(\binom{n-j}{3-j}\) three-tuples, so the resulting sum is \(\binom{n-j}{3-j}\binom wu\). All denominators are positive since \(n\ge3\).

For \(w=w(a,b,c,d)\), direct selection of marked positions and zeros gives
\[
\binom w{01}=3a+2b+c,\qquad
\binom w{011}=3a+b,\qquad
\binom w{110}=c+3d.
\]
The total number of zeros is \(N=n-3=a+b+c+d\). Solving these equations, any other four-gap vector with the same deck must have the form
\[
(a',b',c',d')=(a-t,b+3t,c-3t,d+t)
\]
for an integer \(t\), constrained by nonnegativity. This is the complete one-dimensional integer kernel; the \(01\) equation is redundant, since \(2\binom w{01}=3N+\binom w{011}-\binom w{110}\).

**2. Exact nonlinear collision test.** The count of the scattered pattern \(001\) is
\[
F(a,b,c,d)=\binom a2+\binom{a+b}2+\binom{a+b+c}2.
\]
Under the displayed kernel shift, elementary expansion yields exactly
\[
F(a-t,b+3t,c-3t,d+t)-F(a,b,c,d)=t(b-c+3t).
\]
Thus matching three-decks requires \(t=0\) or \(t=(c-b)/3\). The latter gives the unique candidate in the statement, which must have nonnegative integral gaps.

The candidate is also *sufficient*: along the kernel, counts of \(011,110,101\) are unchanged (in particular \(\binom w{101}=2(b+c)\)). The remaining two-zero patterns satisfy the exact shift identities
\[
\Delta\binom w{100}=t(b-c+3t),\qquad
\Delta\binom w{010}=-2t(b-c+3t).
\]
They follow directly from
\[
\binom w{100}=\binom{b+c+d}2+\binom{c+d}2+\binom d2,
\]
and
\[
\binom w{010}=a(b+c+d)+(a+b)(c+d)+(a+b+c)d.
\]
Finally \(\binom w{000}=\binom N3\) and \(\binom w{111}=1\) depend only on composition. All eight length-three counts therefore agree when \(t=(c-b)/3\), and there are no other possible partners. Applying the partner map a second time restores the original vector. Thus every class has cardinality at most two.

**3. Exact pair counting.** Every nontrivial pair has exactly one representative with \(b>c\). For that representative put \(b=c+3s\), with integer \(s\ge1\). The candidate partner has final gap \(d-s\), so feasibility is exactly \(d=s+e\) for some integer \(e\ge0\). There are no other restrictions: \(a,c,e\ge0\), \(s\ge1\), and the total number of zeros is
\[
N=a+(c+3s)+c+(e+s)=a+e+2c+4s.
\]
Consequently, counting one representative per unordered pair gives the rational generating function
\[
\sum_{n\ge3}P_nz^n
=z^3\left(\sum_{a\ge0}z^a\right)
\left(\sum_{e\ge0}z^e\right)
\left(\sum_{c\ge0}z^{2c}\right)
\left(\sum_{s\ge1}z^{4s}\right)
=\frac{z^7}{(1-z)^2(1-z^2)(1-z^4)}.
\]
There are \(\binom n3\) words of length \(n\) with three ones. Every two-word class reduces the number of distinct decks by one, yielding the claimed difference of generating functions. The pole at \(z=1\) in the pair series has leading term \(1/(8(1-z)^4)\), so coefficient extraction gives \(P_n=n^3/48+O(n^2)\). Dividing twice this by \(\binom n3=n^3/6+O(n^2)\) gives limiting proportion \(1/4\).

## Verification
The accompanying standard-library `checker.py` independently constructs the exact three-deck via dynamic programming on scattered occurrences, rather than by using the four-gap closed formulas. It groups all \(52{,}360\) weight-three binary words of lengths three through thirty-four, checks that all classes have size one or two and that the specified partner map describes exactly every collision, then checks the rational-generating-function coefficients. A second direct index-triple enumeration checks \(495\) words at lengths three through eleven, and the checker tests four-deck separation for \(2{,}170\) directed collision instances as a consistency check. The all-length proof above, not these finite experiments, establishes the theorem.

To reproduce: run `python3 checker.py` from the same directory as this document. Expected final line: `VERIFIED_OK`. The checker uses only the Python standard library.

## Relationship to prior work
Rigo and Salimov introduced and studied \(m\)-binomial equivalence, the language equivalent to equality of scattered-subsequence decks, in 2013. Their work is primarily about infinite-word complexity, not this fixed-weight-three enumeration.

Lejeune, Rigo and Rosenfeld (2020) study binomial equivalence classes of finite words, proving structural results mainly for binary 2-binomial equivalence and general language growth. Their full manuscript does not state the weight-three 3-binomial collision classes or this conjectured series.

Chrisnata et al. explicitly study three-decks of weight-three binary words. Their Lemma 24 supplies the relevant affine kernel and comparison of the \(001\) count; Theorem 27 gives a lower bound. They state the exact generating function proved here as **Conjecture 1**, and report its first twenty verified coefficients (original paper pp. 15–17). These existing linear-algebra and experimental observations are credited, not presented as new. The new claim is the full necessary-and-sufficient collision classification and the resulting all-length proof of the conjectured generating function and class-size distribution.

The result is about **scattered subsequences counted with multiplicity**, not contiguous factors, unordered Parikh profiles, deletion balls counted without multiplicity, or the unrestricted-weight number of three-decks.

## Limitations
The theorem does not enumerate three-decks across all weights, prove general \(k\)-deck reconstruction bounds, or establish any result for arbitrary alphabets or weights above three. The originality assessment is based on the cited primary full texts, overlap searches and relevant existing records; a previously unindexed proof cannot be excluded. The proof is complete within the stated binary weight-three domain, but no independent mathematical audit has been performed.

## References
1. Michel Rigo and Pavel Salimov, *Another Generalization of Abelian Equivalence: Binomial Complexity of Infinite Words*, WORDS 2013, LNCS 8079, 217–228. DOI: 10.1007/978-3-642-40579-2_23. Author long-version manuscript: https://orbi.uliege.be/bitstream/2268/149313/2/binomial_final_long.pdf. Public repository availability dated 2013-05-27: https://orbi.uliege.be/handle/2268/149313.
2. Marie Lejeune, Michel Rigo and Matthieu Rosenfeld, *On the Binomial Equivalence Classes of Finite Words*, *International Journal of Algebra and Computation* 30 (2020), 1375–1397, doi:10.1142/S0218196720500459. Author full text: https://www.lirmm.fr/~mrosenfeld/LejeuneRigoRosenfeld.pdf.
3. Johan Chrisnata, Han Mao Kiah, Sankeerth Rao Karingula, Alexander Vardy, Eitan Yaakobi and Hanwen Yao, *On the Number of Distinct \(k\)-Decks: Enumeration and Bounds*, *Advances in Mathematics of Communications* 17(4), 960–978. DOI: 10.3934/amc.2021032. Published online 2021; author-hosted full text: https://yaakobi.net.technion.ac.il/files/2022/08/60_k_Decks_Disc_Math21.pdf (especially Lemma 24, Theorem 27, Conjecture 1).
