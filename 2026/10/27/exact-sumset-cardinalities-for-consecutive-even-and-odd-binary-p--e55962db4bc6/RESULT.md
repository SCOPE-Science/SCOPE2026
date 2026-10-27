# Exact sumset cardinalities for consecutive even and odd binary-palindrome lengths

## Finding
For an integer \(r\ge1\), let \(P_r\) be the set of positive integers whose standard base-two representation is a palindrome of exactly \(r\) digits. For every \(m\ge1\) set
\[
A_m=|P_{2m}+P_{2m+1}|, \qquad P_a+P_b=\{x+y:x\in P_a,\ y\in P_b\}.
\]
The complete counting generating function is
\[
\boxed{\sum_{m\ge1}A_mz^{m-1}=\frac{2-7z+6z^2-4z^3-14z^4+24z^5-8z^6}{1-7z+14z^2-4z^3-22z^4+56z^5-36z^6-16z^7+16z^8}.}
\]
In particular, the initial values for \(m=1,2,\ldots,8\) are \(2,7,27,95,345,1259,4629,17019\). Equivalently, for every \(m\ge1\),
\[
\boxed{A_{m+8}=7A_{m+7}-14A_{m+6}+4A_{m+5}+22A_{m+4}-56A_{m+3}+36A_{m+2}+16A_{m+1}-16A_m.}
\]
Thus a fixed recurrence exactly counts the distinct sums for arbitrarily long, adjacent even and odd palindrome lengths, without enumerating the exponentially many pairs of summands.

## Assumptions and scope
Binary palindromes are ordinary positive integers, without leading zeros. For \(P_{2m}\) and \(P_{2m+1}\), the initial and terminal digits of each summand equal one. The sumset counts *distinct integer values*, not representations with multiplicity. The argument includes all integers \(m\ge1\), without size cutoff or primality assumption.

## Proof
Write a length-\(2m\) palindrome by its low-to-high digits \(a_i\), where its digit in position \(2m-1-i\) also equals \(a_i\), for \(0\le i<m\). Similarly write the length-\(2m+1\) palindrome with low digits \(b_i\), where the digit in position \(2m-i\) equals \(b_i\), for \(0\le i\le m\). The outer-digit constraints are \(a_0=b_0=1\).

At digit position zero, the two ones sum to two: the result bit is zero and the carry to position one is one. At position \(2m\), the longer palindrome contributes a one and the carry from position \(2m-1\) is some \(t\in\{0,1\}\). Its result bit is \(1-t\) and the possible overflow at position \(2m+1\) is \(t\). Hence these two choices of \(t\) give disjoint sets of integer sums.

Process positions \(i\) and \(2m-i\) together, for \(1\le i<m\), and let a state \((\ell,h,c)\in\{0,1\}^3\) store the low incoming carry, high outgoing carry, and previous digit \(c=a_{i-1}\). For guessed digits \(a=a_i\), \(b=b_i\), and guessed high incoming carry \(h'\), define
\[
L=a+b+\ell,\qquad H=c+b+h'.
\]
The resulting low and high observed bits are respectively \(L\bmod2\) and \(H\bmod2\). The compatibility condition for the known high outgoing carry is \(\lfloor H/2\rfloor=h\); the successor state is \((\lfloor L/2\rfloor,h',a)\). Consequently each of the four observed bit-pairs induces an explicit nondeterministic transition on the eight possible carry/digit states.

Determinize this transition by tracking the nonempty subset \(S\) of possible carry/digit states. The two disjoint initial classes start from \(\{(1,0,1)\}\) and \(\{(1,1,1)\}\). After the \(m-1\) interior bit-pair transitions, the middle position \(m\) has a possible result bit \(u\in\{0,1\}\) exactly if there are a state \((\ell,h,c)\in S\) and a center digit \(b\in\{0,1\}\) such that
\[
\lfloor(c+b+\ell)/2\rfloor=h,\qquad u=(c+b+\ell)\bmod2.
\]
Let \(w(S)\) be the number of distinct possible middle bits, not the number of witnessing states. This last distinction removes all representation multiplicities.

Perform breadth-first enumeration of every nonempty reachable subset from the two initial classes. Exactly \(37\) different subsets occur. Index these states and let \(M\) be the resulting nonnegative integer transition matrix, whose \((S,T)\)-entry counts the observed bit-pairs taking \(S\) to \(T\). Let \(v\) put weight one at each initial singleton and \(w\) be the column of middle-bit counts. Each complete accepted output word determines exactly one integer sum, and conversely every such sum is accepted. We therefore have the exact identity
\[
A_m=vM^{m-1}w.
\]
This transfer identity is independent of any recurrence guess.

Put
\[
Q(X)=X^8-7X^7+14X^6-4X^5-22X^4+56X^3-36X^2-16X+16.
\]
The supplied, executable integer-arithmetic certificate constructs all \(37\) reachable subset states and verifies each of the \(37\) equalities
\[
vM^kQ(M)w=0\quad(0\le k<37).
\]
This finite check is sufficient for *all* \(k\ge0\): by Cayley–Hamilton, the scalar sequence \(vM^kQ(M)w\) obeys the characteristic recurrence of the \(37\)-dimensional matrix \(M\), so \(37\) consecutive initial zeros force all later values to vanish. Substituting the transfer identity proves the displayed order-eight recurrence for every \(m\ge1\). The same exact certificate verifies its eight stated initial values. Routine multiplication of the recurrence by the power series gives the asserted rational generating function and numerator.

## Verification
The standalone `verify.py` uses only the Python 3 standard library. It generates all reachable determinized states from the eight-state digit/carry rule, forms the matrix, confirms its dimension is \(37\), checks the first eight values by a separate direct enumeration of the two palindrome sets, and evaluates the \(37\) Cayley–Hamilton certificates using unbounded integers. Run `python3 verify.py`; the expected success prefix is `VERIFY_OK`. The full finite certificate, not a bounded sample, establishes the infinite recurrence once the carry-state correspondence is proved as above.

## Relationship to prior work
OEIS A264964 (2015) records the closed formula \(3^{\lfloor(r-1)/2\rfloor}\) for sums of two binary palindromes of the *same* length \(r\), rather than the adjacent even/odd lengths studied here. Rajasekaran, Shallit and Smith (2017) develop automata for additive representations by binary palindromes and give a same-length counting theorem for generalized binary palindromes; they do not present this exact mixed-length count. Zakharov (2024) considers \(P_n+P_{n-d}\) for general length differences and proves upper bounds sufficient for global density estimates, but does not determine the present exact generating function. These broader representability and bounding results do not imply the explicit count. The related literature supplies the motivation for quantifying collisions between two prescribed lengths.

## Limitations
Only the exact adjacent even/odd length pattern \((2m,2m+1)\) is classified. There is no claim about arbitrary base, arbitrary length difference, or the number of representations of each sum. The rational formula rests on the explicit, reproducible \(37\)-state finite calculation; independent mathematical validation has not been performed. Equivalent formulas in literature not located by the stated searches remain a possibility.

## References
- N. J. A. Sloane, OEIS A264964, “Numbers that are the sum of two binary palindromes of the same (binary) length,” first posted 2015-11-29. https://oeis.org/A264964
- A. Rajasekaran, J. Shallit and T. Smith, “Sums of Palindromes: an Approach via Automata,” arXiv:1706.10206 (2017), especially Theorem 9 and Sections 2 and 7. https://arxiv.org/abs/1706.10206
- D. Zakharov, “Most integers are not a sum of two palindromes,” arXiv:2402.10808 (2024), especially Sections 1–2 and the sumset estimates. https://arxiv.org/abs/2402.10808
