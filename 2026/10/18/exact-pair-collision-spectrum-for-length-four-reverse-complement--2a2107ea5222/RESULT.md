# Exact pair-collision spectrum for length-four reverse-complement duplication

## Finding

Let \(\Sigma\) be a finite alphabet of even size \(q\ge 2\), with a specified fixed-point-free involution \(a\mapsto\overline a\). Given any word \(w\in\Sigma^n\), \(n\ge4\), the length-four reverse-complement duplication at start position \(i\) inserts the reverse complement of the four-letter block immediately after that block. Positions are numbered from zero. Write the resulting word as \(T_i(w)\), where \(0\le i\le n-4\).

For a uniform independent-symbol word \(W\in\Sigma^n\), the exact probability of **two distinct duplication sites producing the same descendant** depends only on their displacement \(d\):

\[
\Pr\bigl(T_i(W)=T_{i+d}(W)\bigr)=p_d=\begin{cases}
q^{-4},&d=1,2,\\
q^{-6},&d=3,\\
q^{-d-2},&d\ge4.
\end{cases}
\]

Define the number of colliding *pairs of sites*, counting each unordered pair once, by
\[
C_4(w)=\sum_{0\le i<j\le n-4}\mathbf1\{T_i(w)=T_j(w)\}.
\]
Then for every \(n\ge4\), with \((t)_+=\max\{t,0\}\),
\[
\boxed{\mathbb E C_4(W)=
\frac{(n-4)_++(n-5)_+}{q^4}
+\frac{(n-6)_+}{q^6}
+\sum_{d=4}^{n-4}\frac{n-3-d}{q^{d+2}}.}
\]
An empty sum is zero. In particular, for fixed \(q\) as \(n\to\infty\),
\[
\mathbb E C_4(W)=n\left(\frac{2}{q^4}+\frac1{q^6}+\frac{1}{q^5(q-1)}\right)+O_q(1).
\]
At \(q=2\), the coefficient of \(n\) is \(11/64\). This is a pair-collision statistic and is **not** an assertion about the number of distinct descendants.

## Assumptions and scope

The complement has no fixed points and is an involution. Word symbols are independent and uniformly distributed. Both duplication sites copy precisely four *source* symbols and insert a reversed, complemented copy directly after that block. No restriction on distinct symbols in the source is imposed. The claim concerns all valid pairs of sites and all lengths \(n\ge4\), not only binary words. The probability is invariant under which involution pairs the symbols.

## Proof

Let \(R(x_0\cdots x_{m-1})=\overline{x_{m-1}}\cdots\overline{x_0}\) denote reverse-complementation. Fix two sites \(i\) and \(i+d\) and restrict to the \(d+4\) source letters \(x_0\cdots x_{d+3}\) between the beginning of the first block and the end of the second. Let \(P=x_0x_1x_2x_3\), \(V=x_4\cdots x_{d+3}\), and \(Y=x_d\cdots x_{d+3}\). The prefixes before \(i\) and suffixes after \(i+d+4\) cancel from the equality between the two descendants. The remaining equality is exactly
\[
R(P)\,V=V\,R(Y). \tag{1}
\]
This equation has length \(d+4\) on both sides.

**Displacements below four.** Direct comparison of each of the \(d+4\) coordinates in (1), using \(\overline{\overline a}=a\), gives the following **complete** lists of solutions:

\[
\begin{array}{c|c|c}
d&x_0\cdots x_{d+3}&\text{number of choices}\\\hline
1&a\,\overline a\,a\,\overline a\,a&q\\
2&a\,b\,\overline b\,\overline a\,a\,b&q^2\\
3&a\,\overline a\,a\,\overline a\,a\,\overline a\,a&q.
\end{array}
\]
Here \(a,b\in\Sigma\) are arbitrary and independent when both appear. Each displayed family satisfies (1) by substitution; conversely, reading the coordinate equations left to right forces the displayed letters successively, with the indicated free coordinates.

**Displacements at least four.** Set \(A=R(P)\), so \(|A|=4\). In (1), the first \(d\) symbols give the recurrence \(V_r=A_r\) for \(0\le r<4\) and \(V_r=V_{r-4}\) for \(4\le r<d\); hence \(V\) is the length-\(d\) prefix of the infinite periodic word \(AAAA\cdots\). Since \(d\ge4\), the last four symbols on the left of (1) are \(Y\), while the last four on the right are \(R(Y)\). Thus (1) forces \(Y=R(Y)\), and the periodicity condition together with \(Y=R(Y)\) conversely implies (1). The word \(Y\) is the four-letter cyclic rotation of \(A\) determined by \(d\pmod4\). Any fixed four-letter cyclic rotation is a bijection on \(\Sigma^4\). A four-letter word satisfies \(Y=R(Y)\) exactly when its first two letters are chosen arbitrarily and its last two letters are their complementary reversals. There are therefore exactly \(q^2\) admissible choices of \(A\); each determines \(P=R(A)\) and the whole of \(V\). This exhausts the solutions for \(d\ge4\).

The source interval has \(d+4\) independent uniformly distributed symbols. Dividing the respective solution counts \(q,q^2,q,q^2\) by \(q^{d+4}\) proves the four probability cases. Symbols outside that interval can be arbitrary and have no effect.

For fixed \(d\in\{1,\dots,n-4\}\), there are precisely \(n-3-d\) ordered pairs of valid sites \((i,i+d)\) with \(i< i+d\). Summing their probabilities proves the displayed exact expectation. Finally, the tail for \(d\ge4\) is a convergent geometric series with linear coefficient \(\sum_{d\ge4}q^{-d-2}=q^{-5}/(q-1)\). Terms arising from \(n-3-d\) rather than \(n\), and from omitting \(d>n-4\), are uniformly bounded for each fixed \(q\), proving the asymptotic formula.

## Verification

The accompanying standalone `check_rc4.py` implements the channel directly. Exhaustive source-word enumeration checks the local collision counts for binary displacement \(1\le d\le10\) and quaternary displacement \(1\le d\le5\). It separately checks the pair-collision expectation for every binary source length \(4\le n\le12\) using rational arithmetic. Its output terminates with `PAIR_SPECTRUM_RC4_PASS`. These finite tests are cross-checks; the argument above proves the formulas for all permissible \(q,n\).

## Relationship to prior work

Lenz, Wachter-Zeh and Yaakobi's work on tandem and palindromic duplications establishes the channel context and compares one-error spheres, including exact special cases for small palindromic duplication length. Ben-Tolila and Schwartz establish structural word-equation arguments for reverse-complement duplication, particularly rigidity for odd duplication lengths. Yohananov and Schwartz investigate asymptotic coding capacity for these duplication channels. Zabokritskiy identifies a coordinate-wise equivalence between even-length reverse-complement and palindromic duplication channels, allowing the present result to be restated for the corresponding palindromic model. None of the compared statements supplies the explicit four-case length-four site-separation collision probabilities or their pair-moment consequence as stated here. The equivalence of the two channels is not claimed as new.

## Limitations

This theorem calculates equality of a *given pair* of one-step outputs, and the expected total pair multiplicity. It does not enumerate complete descendant multiplicity distributions; triple and higher collisions can occur, so subtracting this expectation from the number of sites would not give the expected number of distinct outputs. The result does not cover complement involutions with fixed points, nonuniform sources, arbitrary numbers of sequential duplications, or general block lengths. Equivalent formulas expressed in the palindromic-duplication model remain a possible literature-overlap risk. Independent mathematical assessment has not been performed.

## References

1. A. Lenz, A. Wachter-Zeh and E. Yaakobi, *Bounds on Codes Correcting Tandem and Palindromic Duplications*, arXiv:1707.00052 (first public 2017-06-30), https://arxiv.org/abs/1707.00052.
2. A. Lenz, A. Wachter-Zeh and E. Yaakobi, *Duplication-Correcting Codes*, arXiv:1712.09345 (2017), https://arxiv.org/abs/1712.09345.
3. N. Ben-Tolila and M. Schwartz, *On the Reverse-Complement String-Duplication System*, arXiv:2112.11811 (2021), https://arxiv.org/abs/2112.11811.
4. L. Yohananov and M. Schwartz, *On the Coding Capacity of Reverse-Complement and Palindromic Duplication-Correcting Codes*, arXiv:2312.00394 (2023), https://arxiv.org/abs/2312.00394.
5. A. L. Zabokritskiy, *Coding for Multiple Reverse-Complement and Palindromic Duplications*, arXiv:2609.00779 (2026), https://arxiv.org/abs/2609.00779.
