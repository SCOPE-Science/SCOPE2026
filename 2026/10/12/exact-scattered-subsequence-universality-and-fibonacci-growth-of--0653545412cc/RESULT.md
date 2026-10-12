# Exact scattered-subsequence universality and Fibonacci growth of Baum–Sweet prefixes

## Finding

Write \(b(0)=1\), and for every integer \(n\ge1\), define \(b(n)\) to equal \(1\) precisely when all maximal runs of zero digits in its ordinary binary representation have **even** length; otherwise set \(b(n)=0\). The first symbols are `1101100101001001`.

For \(N\ge0\), set \(W_N=b(0)b(1)\cdots b(N-1)\), with \(W_0\) empty, and define \(U(N)\) as the largest integer \(k\ge0\) such that each binary word of length \(k\) occurs as an order-preserving (not necessarily contiguous) subsequence of \(W_N\). Let \(B(N)=\sum_{0\le n<N}b(n)\).

**Theorem.** The initial values are \(U(0)=U(1)=U(2)=0\) and \(U(3)=1\). For **all** integers \(N\ge4\),
\[
 U(N)=B(N)-2-\mathbf{1}_{\{N=4^t+1\text{ for some }t\in\mathbb Z,\ t\ge1\}}.
\]
With Fibonacci numbers \(F_0=0\), \(F_1=1\), \(F_{j+2}=F_{j+1}+F_j\), we have, for every \(m\ge0\),
\[
 B(2^m)=F_{m+2};
\]
and, for every \(m\ge2\),
\[
 U(2^m)=F_{m+2}-2.
\]
Putting \(\varphi=(1+\sqrt5)/2\) and \(\alpha=\log_2\varphi\), it follows that
\[
 U(N)=\Theta(N^\alpha),\quad
 \lim_{m\to\infty}\frac{U(2^m)}{(2^m)^\alpha}=\frac{\varphi^2}{\sqrt5},\quad
 \lim_{N\to\infty}\frac{U(N)}N=0.
\]
The formula evaluates in \(O(\log N)\) integer-arithmetic operations by the digit DP below (arithmetic bit-cost depends on \(N\)).

## Assumptions and scope

Subsequence positions are strictly increasing; no contiguity requirement is imposed. The prefix starts at index zero and uses the **accepted empty-run convention** \(b(0)=1\). All formulae concern finite prefixes, not arbitrary factors or circular subsequences. For the empty prefix the only universally present word has length zero.

## Proof

**1. Adjacent-one classification.** For all \(n\ge0\),
\[
 b(n)=b(n+1)=1\quad\Longleftrightarrow\quad n=4^t-1\text{ for some integer }t\ge0.
\]
Indeed \(n=0\) gives the first adjacent pair. If \(n>0\) is even and accepted, its binary expansion ends in a positive even-length run of zeros. Adding one shortens that final run by one and creates an odd zero-run, so \(n+1\) is rejected. If \(n\) is odd but not a string of all ones, its final nonempty zero-run lies immediately before the trailing ones and has even length \(2s\). Adding one decreases that run to length \(2s-1\), again forcing rejection. Hence an odd accepted \(n\) followed by another accepted value must be all ones, of some bit length \(h\). Its successor is a one followed by \(h\) zeros and is accepted exactly when \(h\) is even. Thus \(n=2^{2t}-1=4^t-1\), as asserted. In particular, no three consecutive entries equal one, and the consecutive-one pairs start precisely at \(0,3,15,63,\ldots\).

**2. Greedy-arch lemma.** For any binary word, greedily divide it into the shortest successive blocks each containing both symbols, leaving a final suffix containing at most one distinct symbol. If there are \(a\) completed blocks, its subsequence universality index equals \(a\). To prove the lower bound, realize each of the \(a\) prescribed target letters in its own completed block. For the reverse bound, in the \(i\)-th completed block choose its last letter \(x_i\). The block contains no previous occurrence of \(x_i\), by greedy minimality. Choose a letter \(c\) absent from the final suffix. A greedy match of \(x_1\cdots x_a c\) is forced to reach the last position of each completed block in turn and then cannot match \(c\). No alternative matching exists because greedy leftmost matching succeeds whenever any matching does. Therefore not all words of length \(a+1\) are subsequences.

**3. Complete arch count.** The first six Baum–Sweet symbols, `110110`, form exactly two arches and contain four ones. From index six onward, every isolated one is preceded by a zero; each pair of adjacent ones starts at \(4^t-1\) for \(t\ge2\), is preceded by a zero, and is followed by a zero. Beginning immediately after the first six symbols, each isolated one adds exactly one completed arch, closing at that one. In each adjacent pair, the first one closes an arch, while the second one initiates the following arch, which closes at the next zero. Thus each one contributes exactly one new arch, except that the second member of an adjacent pair remains temporarily unfinished if the prefix ends there. Such a trailing pair ends a prefix precisely at \(N=4^t+1\), \(t\ge2\). The same counting identity is checked directly for \(N=4,5,6\); note that \(N=5=4^1+1\) has the same one-arch deficit. Together with the first-six-symbol offset of two, this yields the displayed all-prefix formula, and the four exceptional initial prefix values follow by inspection. This is an infinite structural argument, not an inference from finite enumeration.

**4. Fibonacci count.** Every accepted positive integer of binary length \(\ell\ge1\) is written uniquely as a leading `1` followed by a concatenation of tokens `1` and `00`. The number of token strings of total length \(\ell-1\) is \(F_\ell\) by the usual two-term recurrence. Counting the accepted zero and all positive numbers below \(2^m\) gives
\[
 B(2^m)=1+\sum_{\ell=1}^m F_\ell=F_{m+2}.
\]
If \(m\ge2\), \(2^m\) is not of the form \(4^t+1\), proving the dyadic formula. For arbitrary \(N\), take consecutive powers of two bracketing \(N\) and apply monotonicity of \(B\). The dyadic Fibonacci estimates and \(U(N)=B(N)+O(1)\) imply the sharp growth exponent \(\alpha\). Finally Binet's formula \(F_{m+2}=\big(\varphi^{m+2}-(1-\varphi)^{m+2}\big)/\sqrt5\) gives the dyadic constant.

**5. Explicit logarithmic digit DP.** For \(N\ge1\), let \(s\) be the standard binary representation of \(N\), of length \(L\). The count of accepted integers with fewer than \(L\) digits, **including zero**, is \(F_{L+1}\). When inspecting the \(L-1\) digits after the leading one, maintain a state \(E\) or \(O\) according to whether the current zero-run has even or odd length. From \(E\), digit `0` enters \(O\), and digit `1` stays at \(E\); from \(O\), digit `0` enters \(E\), while digit `1` invalidates that branch. With \(r\) remaining digits, the number of valid completions from states \(E\) and \(O\) equals \(F_{r+1}\) and \(F_r\), respectively. For each next actual digit `1`, first count numbers obtained by choosing smaller digit `0`: add \(F_r\) if the current state is \(E\), and \(F_{r+1}\) if it is \(O\). Then follow the actual digit `1`, stopping if the previous state was \(O\). At an actual `0` just toggle the state. Starting from \(F_{L+1}\), this yields exactly \(B(N)\), since all counted numbers are less than \(N\). Apply the indicator correction to obtain \(U(N)\). There are \(L-1=O(\log N)\) iterations.

## Verification

The accompanying standalone `verify.py` regenerates the word directly from its digit definition; compares the greedy arch count against the exact all-prefix theorem for every \(N\) from one to \(2^{20}\); checks adjacency and no-triple constraints; checks the Fibonacci formula for dyadic sizes through exponent twenty; and independently tests universal-subsequence coverage by exhaustive binary target words for all prefixes of length at most 29. It prints `PREFIX_OK` and `BRUTE_OK` on success. These are finite consistency tests. The infinite proof is the digit-run/arch/Fibonacci argument above; neither sampling nor the checker alone proves it.

## Relationship to prior work

Schnoebelen and Veron's 2023 work develops greedy arch factorizations, circular universality, signatures, and compressed-word algorithms [1]. Their general arch correspondence is not claimed as new here. Adamson and coauthors study subsequence universality of regular languages [2], rather than the exact prefix index for this fixed automatic sequence. The Baum–Sweet word itself is classical [3]. The additional statement is a **closed all-prefix Baum–Sweet formula**, sharp Fibonacci values, and its sublinear power-law exponent. Generic universality algorithms applied to an explicitly given finite word do not themselves state this formula.

## Limitations

The result does not classify all absent subsequences, arbitrary interior factors, or circular universality. The logarithmic complexity counts arithmetic operations on Fibonacci-sized integers; bit complexity is larger. The novelty assessment depends on accessible and indexed literature and cannot exclude an earlier unpublished or unindexed equivalent identity. Independent external validation has not been performed.

## References

[1] P. Schnoebelen and J. Veron, *On arch factorization and subword universality for words and compressed words*, arXiv:2304.11932v1, first public 2023-04-24, https://arxiv.org/abs/2304.11932.

[2] D. Adamson, P. Fleischmann, A. Huch, T. Koß, F. Manea, and D. Nowotka, *k-Universality of Regular Languages*, arXiv:2311.10658v1, first public 2023-11-17, https://arxiv.org/abs/2311.10658.

[3] L. E. Baum and M. M. Sweet, *Continued Fractions of Algebraic Power Series in Characteristic 2*, Annals of Mathematics 103 (1976), 593–610. Used solely for historical attribution of the sequence, not for the present universality assertion.
