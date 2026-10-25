# Proof of the weight-three binary three-deck enumeration conjecture

## Finding

For every integer \(n\ge 3\), let \(D_{3,3}(n)\) be the number of distinct multiplicity vectors of all scattered binary subsequences of length three, among words of length \(n\) having exactly three ones. Then

\[
\boxed{\sum_{n\ge3}D_{3,3}(n)z^n
=\frac{z^3}{(1-z)^4}-\frac{z^7}{(1-z)^2(1-z^2)(1-z^4)}.}
\]

This proves the precise generating-function identity proposed as Conjecture 1 by Chrisnata, Kiah, Karingula, Vardy, Yaakobi, and Yao (first openly available by 2021). Every three-deck equivalence class in this fixed-weight family has size at most two. All nonsingleton classes are explicitly classified below.

For each \(n\), write \(C_n\) for the number of size-two classes. Then

\[
\sum_{n\ge3}C_nz^n=\frac{z^7}{(1-z)^2(1-z^2)(1-z^4)},
\qquad
D_{3,3}(n)=\binom n3-C_n.
\]

The first collision occurs at length seven, between `1000110` and `0110001`. Moreover, among weight-three words the limiting proportion uniquely determined by their three-deck is \(3/4\), and the number of distinct decks is asymptotic to \(7n^3/48\).

## Assumptions and scope

A length-three *scattered subsequence* of a word \(w=w_1\cdots w_n\) is \(w_iw_jw_k\) for indices \(1\le i<j<k\le n\). Its three-deck is the eight-component vector of multiplicities, indexed by the patterns `000`, `001`, `010`, `011`, `100`, `101`, `110`, `111`. Distinct words are equivalent precisely when these entire vectors agree; neither deletion outputs as sets nor contiguous substring counts are meant.

We restrict to the binary alphabet and words with exactly three ones, and assume \(n\ge3\). Represent a word uniquely by its four zero gaps:

\[
w=0^{x_0}1\,0^{x_1}1\,0^{x_2}1\,0^{x_3},\qquad
x_i\in\mathbb Z_{\ge0},\quad x_0+x_1+x_2+x_3=N:=n-3.
\]

All generating functions are formal power series over the integers. A coefficient statement therefore makes no analytic convergence assumption.

## Proof

**Step 1: A complete four-statistic description of the deck.** Write \(T_{abc}\) for the number of scattered occurrences of the displayed three-bit pattern. Define

\[
A:=T_{011}=3x_0+x_1,\qquad
B:=T_{110}=x_2+3x_3,\qquad
F:=T_{001}.
\]

There are exactly three ones and \(N\) zeros, so \(T_{111}=1\) and \(T_{000}=\binom N3\). The remaining pattern with two ones is determined by

\[
T_{101}=2(x_1+x_2)=3N-A-B.
\]

Put \(p_1=x_0\), \(p_2=x_0+x_1\), and \(p_3=x_0+x_1+x_2\), the numbers of zeros preceding successive ones. Then

\[
T_{001}=\sum_{i=1}^3\binom{p_i}{2},\quad
T_{010}=\sum_{i=1}^3p_i(N-p_i),\quad
T_{100}=\sum_{i=1}^3\binom{N-p_i}{2}.
\]

Because

\[
S:=\sum_i p_i=3x_0+2x_1+x_2=\frac{A+3N-B}{2},
\qquad \sum_i p_i^2=2F+S,
\]

all three one-one pattern counts are determined by \(N,A,B,F\). Conversely, these four values are visible in the full deck (with \(N=n-3\) fixed). Therefore two words with three ones and the same length have the same three-deck **if and only if** their triples \((A,B,F)\) agree.

**Step 2: Exact collision involution.** Let \(x=(x_0,x_1,x_2,x_3)\) and \(x'\) have equal \(N,A,B\). The three independent linear equations give, for an integer \(t\),

\[
x'=x+t(1,-3,3,-1).
\]

For these two gap vectors, substituting \(p'_i=p_i+(t,-2t,t)_i\) into the displayed formula for \(F\) gives the exact identity

\[
F(x')-F(x)=t(x_2-x_1+3t).
\]

If \(x\ne x'\), then \(t\ne0\), so their decks agree precisely when

\[
t=\frac{x_1-x_2}{3}\in\mathbb Z\setminus\{0\},\qquad
x'=\left(x_0+t,\,x_2,\,x_1,\,x_3-t\right)
\]

is coordinatewise nonnegative. This is a fixed-point-free involution on its domain: applying it twice recovers \(x\). The equation for \(F\) is quadratic in \(t\) with at most two integer roots, one of which is zero, so **no equivalence class has more than two words**.

**Step 3: Unique parametrization and enumeration.** Orient each two-element class so the first representative has \(x_1>x_2\). Then \(t=(x_1-x_2)/3\ge1\), and nonnegativity of the partner requires \(x_3\ge t\). Consequently every pair is represented exactly once, and without additional constraints, by

\[
x=(r,s+3t,s,t+u),\qquad
x'=(r+t,s,s+3t,u),\qquad
r,s,u\ge0,\quad t\ge1.
\]

Both words have length \(n=3+r+2s+4t+u\). Taking the product of the four independent geometric series yields

\[
\sum_{n\ge3}C_nz^n
=z^3\left(\sum_{r\ge0}z^r\right)
\left(\sum_{s\ge0}z^{2s}\right)
\left(\sum_{u\ge0}z^u\right)
\left(\sum_{t\ge1}z^{4t}\right)
=\frac{z^7}{(1-z)^2(1-z^2)(1-z^4)}.
\]

There are \(\binom n3\) binary length-\(n\) words with three ones. Every nonsingleton deck class has size exactly two, hence the number of classes equals \(\binom n3-C_n\). Since

\[
\sum_{n\ge3}\binom n3z^n=\frac{z^3}{(1-z)^4},
\]

the claimed generating function follows. This is an all-length proof, not extrapolation from a finite table.

**Step 4: Asymptotics and reconstruction fraction.** At \(z=1\), the denominator of the second generating function has leading term \(8(1-z)^4\); all other poles are roots of unity and have smaller order. Thus \(C_n=n^3/48+O(n^2)\) and \(\binom n3=n^3/6+O(n^2)\). It follows that \(D_{3,3}(n)=7n^3/48+O(n^2)\). Exactly \(2C_n\) of the \(\binom n3\) words belong to two-word classes, so the uniquely reconstructible proportion tends to \(1-2(1/8)=3/4\).

## Verification

The standalone file `verify_three_deck.py` uses a direct dynamic program to count all scattered length-three subsequences in each weight-three word. It exhaustively groups all such words at lengths \(3\) through \(24\), checks the collision involution on every non-singleton group, confirms that no group has size above two, and matches the rational generating-function coefficients. Its independent second counting route enumerates valid zero-gap configurations for all lengths \(3\) through \(100\). Run with `python3 verify_three_deck.py`; the expected final output is `VERIFY_OK`.

The finite checks are corroboration; correctness for every \(n\) follows from the preceding algebraic proof. No software package other than Python's standard library is required.

## Relationship to prior work

Chrisnata, Kiah, Karingula, Vardy, Yaakobi, and Yao derived the relevant zero-gap linear constraints and exhibited a collision pair; importantly, their *Conjecture 1* states exactly the generating function proved here. Their reported verification of twenty coefficients is not an all-length proof. This result explicitly credits the earlier conjectured formula and claims novelty for its proof and complete involutive classification, not for the conjecture's original proposal.

Nilforoushan and Parvaresh's 2026 study of degrees of freedom in length-\(k\) decks and the associated zero-error reconstruction question gives a current motivation for exact fixed-composition fibers. Their conclusions are asymptotic for unrestricted compositions and do not entail this exact weight-three formula or pairwise-fiber structure.

Other results on two-decks, contiguous profiles, and deletion-set reconstruction concern different observations and do not imply equality of the full length-three *scattered-multiplicity* vectors.

## Limitations

The theorem concerns exactly three ones and length-three subsequence multiplicities, not the unrestricted binary three-deck count, nor weights four or greater. It does not solve the 2026 conjecture on the exponent of unrestricted \(k\)-deck counts. An unindexed earlier proof of the 2021 conjecture cannot be excluded solely by the sources searched; mathematical priority needs independent checking. The included verification is finite, while the infinite statement is supported by the displayed proof.

## References

1. Arman Nilforoushan and Farzad Parvaresh, *Improved upper bound on the number of distinct k-decks for any k and alphabet size by counting the independent parameters*, arXiv:2609.23106, first submitted 2026-09-19. https://arxiv.org/abs/2609.23106
2. Johan Chrisnata, Han Mao Kiah, Sankeerth Rao Karingula, Alexander Vardy, Eitan Yaakobi, and Hanwen Yao, *On the number of distinct k-decks: Enumeration and bounds*, Advances in Mathematics of Communications 17 (2023), 960–978; published online 2021-08-30, DOI:10.3934/amc.2021032, Conjecture 1 and Section 5.3. https://doi.org/10.3934/amc.2021032
