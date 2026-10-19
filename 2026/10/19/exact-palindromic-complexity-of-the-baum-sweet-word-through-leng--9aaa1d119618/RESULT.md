# Exact palindromic complexity of the Baum–Sweet word through length \(8192\)

## Finding

Let \(B=b_0b_1\cdots\) be the binary Baum–Sweet word defined below, and let \(P_B(n)\) be the number of distinct palindromic contiguous factors of \(B\) having length \(n\). This result determines \(P_B(n)\) **for every integer \(1\le n\le8192\)**.

For \(1\le n\le44\), the values in increasing length order are

\[
\begin{split}
(P_B(1),\ldots,P_B(44)) = (&2,2,3,3,4,3,4,3,4,4,4,4,4,3,4,2,\\
&4,2,4,2,4,1,4,1,3,1,2,1,2,1,2,1,\\
&2,2,2,2,2,2,2,2,2,2,1,2).
\end{split}
\]

For all integers \(45\le n\le8192\), the complete answer is

\[
P_B(n)=\begin{cases}
2,&n=2^j+d,\quad j\in\{6,8,10,12\},\quad d\in\{3,5,7,9,11,13,15,17,19,21,23,25\};\\
2,&n=2^j+d,\quad j\in\{7,9,11\},\quad d\in\{2,4,6,8,10,12\};\\
1,&\text{otherwise.}
\end{cases}
\]

The two exceptional families do not overlap. There are exactly \(66\) exceptional lengths in this range and \(8082\) lengths with a single palindrome, namely the all-zero word \(0^n\). At each exceptional length, exactly one palindrome other than \(0^n\) occurs. No assertion is made for \(n>8192\).

## Assumptions and scope

The Baum–Sweet word is normalized by \(b_0=1\); for every positive integer \(m\), \(b_m=1\) if and only if every maximal run of consecutive zero digits in the ordinary base-two expansion of \(m\) has even length. Otherwise \(b_m=0\). A *factor* is a finite, contiguous subword, and a *palindrome* is identical to its reversal. Factors are counted by distinct literal strings, not occurrences or positions.

Define a four-letter, length-two morphism \(\mu\) and binary coding \(\tau\) by

\[
\mu(A)=AB,\qquad\mu(B)=CB,\qquad\mu(C)=BD,\qquad\mu(D)=DD,
\]
\[
\tau(A)=\tau(B)=1,\qquad\tau(C)=\tau(D)=0.
\]

Then \(B=\tau(\mu^\omega(A))\), with the fixed point starting at \(A\). The dyadic block size is \(L=2^{13}=8192\).

## Proof

**(1) Exact automaton presentation.** Reading a binary integer from its most significant bit, use states \(A,B,C,D\), start at \(A\), and move under a bit \(e\in\{0,1\}\) to position \(e\) of \(\mu\) of the current state (positions numbered from zero). The start state ignores a leading zero, state \(B\) records a completed even zero-run, state \(C\) records a currently odd zero-run, and \(D\) is a rejecting sink. The accepting states, whose \(\tau\)-value is one, are \(A,B\). Thus the digit transition computes precisely the Baum–Sweet definition, and the standard uniform-morphism indexing gives \(B=\tau(\mu^\omega(A))\).

**(2) Finite complete covering of all factors in scope.** In the four-letter fixed point, the distinct adjacent pairs are exactly

\[
\mathcal Q=\{AB,BB,BC,BD,CB,DB,DC,DD\}.
\]

This follows by starting with \(AB\), then repeatedly adding the length-two factors of \(\mu(XY)\) for every already available adjacent pair \(XY\); the closure stabilizes at the displayed eight pairs. Each new pair appears in a substituted occurrence of an earlier pair, proving its actual occurrence in the fixed point. Conversely, every adjacent pair in a sufficiently long substituted prefix appears through this closure, proving completeness.

Cut the coded fixed point into aligned blocks \(\tau(\mu^{13}(X))\), each of length \(L\). Every factor of length at most \(L\) lies wholly within one block or crosses just one boundary. Thus it occurs in at least one of the eight concrete words

\[
W_{XY}=\tau\bigl(\mu^{13}(XY)\bigr),\qquad XY\in\mathcal Q,
\]

each of length \(2L\). Conversely, every factor of every \(W_{XY}\) occurs in \(B\). Hence this finite set is an **exact** factor cover, not a prefix sample. Since \(DD\in\mathcal Q\) and \(\mu(D)=DD\), the factor \(0^n\) occurs for every \(1\le n\le L\).

**(3) Exhaustive exact distinct-palindrome enumeration.** The companion standalone program constructs all eight \(W_{XY}\) and enumerates each distinct palindrome containing a \(1\), using a palindromic suffix tree (eertree). At each input position, a new distinct palindrome, when it appears, must be the longest palindromic suffix; the usual suffix-link search therefore finds every distinct palindrome without omitted lengths or approximate string hashes. Full literal strings are used as set keys, deduplicating occurrences across the eight cover words. Let \(e(n)\) be the cardinality of the resulting set at length \(n\). Then the previous factor-cover argument proves \(P_B(n)=1+e(n)\) for every \(1\le n\le8192\).

The code compares the full computed length profile with both the \(44\) initial values and the two dyadic exceptional families in the theorem, for **every** integer length in the range. The assertions are exhaustive finite checks over a proven complete factor cover, so no extrapolation from a prefix or a finite length sample is involved.

## Verification

Run `python3 verify.py` using Python 3 and only its standard library. The program independently checks the first \(8192\) Baum–Sweet symbols against the binary zero-run definition, constructs and verifies all eight adjacent-pair blocks, enumerates the entire palindrome profile through length \(8192\), and matches the expected profile and its SHA-256 digest. A separate direct center-expansion algorithm computes the literal palindrome sets independently for every length through \(128\).

Expected final line: `VERIFY_OK`. The SHA-256 of the UTF-8 table with rows `n,count` followed by a newline, for lengths \(1\) through \(8192\), is `c94eac15fdef31d2b90ccd14121e0782788a316c05a5c80f9d7bde100ff05e55`.

## Relationship to prior work

Allouche, Baake, Cassaigne and Damanik (2001) study palindromic complexity of several automatic and substitution words, including paperfolding, period-doubling and Rudin–Shapiro; their inspected discussion does not give this Baum–Sweet table. Charlier, Rampersad and Shallit (2011), Theorem 9.7, show generally that the palindrome complexity of an automatic sequence is a regular sequence; this does not determine the particular \(8192\)-length spectrum above. Pelantová and Starosta (2011) discuss palindromic and generalized complexity of other symbolic dynamical languages, including the Thue–Morse word; their explicit examples do not imply this finite Baum–Sweet classification. The present result is a concrete, fully enumerated instance, not a strengthening of the general regularity theorem.

## Limitations

The conclusion concerns only \(1\le n\le8192\). Its dyadic exceptional pattern is not asserted for larger lengths, and the verification program is not an infinite theorem for this pattern. The verification uses finite exhaustive enumeration over a mathematically proved complete factor cover; it is not a separately machine-formalized proof. An unindexed prior calculation for this precise Baum–Sweet invariant may exist. Independent audit has not been performed.

## References

- J.-P. Allouche, M. Baake, J. Cassaigne and D. Damanik, *Palindrome Complexity*, arXiv:math/0106121, first submitted 14 June 2001, https://arxiv.org/html/math/0106121v1.
- É. Charlier, N. Rampersad and J. Shallit, *Enumeration and Decidable Properties of Automatic Sequences*, arXiv:1102.3698, first submitted 17 February 2011, https://arxiv.org/html/1102.3698v1.
- E. Pelantová and Š. Starosta, *Languages invariant under more symmetries: overlapping factors versus palindromic richness*, arXiv:1103.4051, first submitted 21 March 2011, https://arxiv.org/html/1103.4051v1.
