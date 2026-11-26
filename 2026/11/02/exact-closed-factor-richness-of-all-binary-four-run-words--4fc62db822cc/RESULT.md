# Exact closed-factor richness of all binary four-run words

## Finding

A word is **closed** if it is empty, has length one, or has a nonempty proper border occurring only as its prefix and suffix. A border is a word that is both a prefix and a suffix, with no restriction on whether the two occurrences overlap. Let \(C(w)\) count distinct contiguous closed factors of \(w\), including the empty word once.

For positive integers \(a,b,c,d\), put \(w=0^a1^b0^c1^d\), \(n=a+b+c+d\), \(x=\min(a,c)\), and \(y=\min(b,d)\). Then
\[
C(w)=n+1+xy.
\]
The result is unchanged under exchanging the letters. For every \(n\ge4\), the largest count among binary words of length \(n\) with exactly four runs is
\[
n+1+\left\lfloor\frac{\lfloor n/2\rfloor^2}{4}\right\rfloor.
\]
The numbers of maximizing length-\(n\) words beginning with \(0\) are \(1,4,2,8\) for \(n\equiv0,1,2,3\pmod4\), respectively. The counts over both starting letters are twice these.

Writing \(E(w)=C(w)-n-1\), the bivariate series for words starting with \(0\) is
\[
\sum_{a,b,c,d\ge1} z^{a+b+c+d}u^{E(0^a1^b0^c1^d)}
=\left(\frac{1+z}{1-z}\right)^2\sum_{x,y\ge1}z^{2(x+y)}u^{xy}.
\]
In particular,
\[
\sum_{n\ge4}z^n\sum_{\substack{a+b+c+d=n\\a,b,c,d\ge1}} E(0^a1^b0^c1^d)
=\frac{z^4}{(1-z)^6(1+z)^2}.
\]

## Assumptions and scope

All factors are linear and contiguous, and equal words are counted only once. A border's internal occurrences are tested within the factor, not in the ambient word. All run exponents are positive. The series are formal in \(z\) with polynomial coefficients in \(u\). The extremum is restricted to binary words with exactly four maximal equal-letter runs.

## Proof

**Classifying borders.** Any non-unary prefix of a word with at least two runs includes its first transition and therefore has the full initial run length of the word. A proper suffix starting within the initial run has a shorter initial run and includes the first transition, so it cannot equal that prefix. Consequently a proper border must have its suffix occurrence start in a later run of the same letter as the first run. This applies to arbitrary positive run lengths and allows overlapping terminal occurrences.

**Classifying closed factors.** Each nonempty factor of \(w\) has one to four runs. The one-run closed factors are exactly the powers \(0^i\), \(1^j\) with \(1\le i\le\max(a,c)\) and \(1\le j\le\max(b,d)\): a power of length at least two is a first return to its prefix of length one less, and single letters are closed by definition.

A two-run word has no proper nonempty border. In fact there is no later run of its initial letter in which a border's suffix occurrence could start.

A three-run factor has form \(0^i1^b0^j\) or \(1^i0^c1^j\). Its only possible proper nonempty borders are powers of the outer letter of length at most \(\min(i,j)\), because the suffix occurrence must start in the last run. If \(i=j\), the full outer power has only the two terminal occurrences. If \(i\ne j\), such a power occurs at least twice in the longer outer run and at least once in the shorter run, so is not a closing border. The distinct three-run closed factors are therefore
\[
0^i1^b0^i\quad(1\le i\le x),\qquad 1^j0^c1^j\quad(1\le j\le y).
\]

A four-run factor has form \(0^i1^b0^c1^j\) with \(1\le i\le a\) and \(1\le j\le d\). A proper nonempty border's suffix occurrence starts in the third run, hence has two runs. Its prefix includes all \(i\) initial zeros and its suffix all \(j\) final ones, so it must be \(0^i1^j\). It exists exactly when \(i\le c\) and \(j\le b\); in that case it occurs exactly once across each of the two \(01\) transitions. The distinct closed four-run factors are thus \(0^i1^b0^c1^j\) with \(1\le i\le x\), \(1\le j\le y\).

These classes are disjoint. Adding the empty factor gives
\[
C(w)=1+\max(a,c)+\max(b,d)+x+y+xy=n+1+xy.
\]

**Maximum and equality cases.** The positive integers \(x,y\) satisfy \(x+y\le m=\lfloor n/2\rfloor\). At fixed sum \(s\) their product is maximal for balanced pairs, with value \(\lfloor s^2/4\rfloor\), strictly increasing for integers \(s\ge2\). Thus equality in the desired bound requires \(x+y=m\) and \(|x-y|\le1\). These conditions are sufficient: start with run lengths \((x,y,x,y)\); for odd \(n\) add one to any of the four runs. These are all possibilities because the residual \(n-2(x+y)\) is zero or one. There is one ordered balanced pair for even \(m\) and two for odd \(m\), giving the stated multiplicities. For example, \(0^31^30^31^3\) has count \(22\), the unique maximum at length 12 among words starting with \(0\).

**Generating series.** For a fixed minimum \(x\) of the two zero-run lengths, their length weight is \(z^{2x}(1+2z+2z^2+\cdots)\), since a positive difference can occur in either run. The same formula applies to the two runs of ones, with minimum \(y\). Taking their product and weighting by \(u^{xy}\) gives the bivariate series. Differentiating formally in \(u\) and evaluating at \(u=1\) gives
\[
\left(\frac{1+z}{1-z}\right)^2\left(\sum_{x\ge1}xz^{2x}\right)^2
=\frac{z^4}{(1-z)^6(1+z)^2}.
\]

## Verification

The supplied standard-library program `verify_closed_four_runs.py` compares the explicit factor sets with both a direct border occurrence test and a longest-border prefix-function test for all positive four-run compositions of total length at most 16. It also includes 128 seeded longer cases and checks bivariate coefficients through length 20. These are finite diagnostics; the border argument and elementary counts above prove the assertions for every allowed length.

## Relationship to prior work

Badkobeh–Fici–Lipták [1, Theorems 23 and 25] characterize binary words attaining the general lower bound of \(n+1\) factors (including the empty word) and give a quadratic lower bound using a construction with four equal blocks and a possible final residual run. That lower bound is not an exact count for arbitrary positive four-run exponents. Binary words with at most three runs are bitonic and attain \(n+1\); with four runs the excess is always positive. A separate exact count for words with exactly two occurrences of one letter [3] already covers the four-run subfamily with both runs of that letter of length one. It agrees with the present formula there after the empty factor is included. Parshina–Puzynina [2] give the unrestricted asymptotic maximum \(\sim n^2/6\), distinct from the four-run maximum with leading coefficient \(1/16\).

## Limitations

The result does not determine an exact maximum for arbitrary words, more than four runs, larger alphabets, or circular words. The comparisons above are qualified and do not claim definitive historical priority.

## References

1. G. Badkobeh, G. Fici and Z. Lipták, *On the Number of Closed Factors in a Word*, arXiv:1305.6395, https://arxiv.org/abs/1305.6395.
2. O. Parshina and S. Puzynina, *Finite and Infinite Closed-Rich Words*, arXiv:2111.00863, https://arxiv.org/abs/2111.00863.
3. *Sharp closed-factor complexity with exactly two marked positions*, Resultary record `2ab04efc05f9`, https://github.com/Resultary/2026/blob/main/2026/10/25/SCOPE-sharp-closed-factor-complexity-with-exactly-two-marked-positions--2ab04efc05f9/RESULT.md.
