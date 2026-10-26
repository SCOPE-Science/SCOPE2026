# Exact nonuniqueness counts for even–odd \(g\)-adic bases in every base \(g\ge4\)

## Finding
For an integer \(g\ge4\), let \(E_g\) consist of all positive integers whose nonzero base-\(g\) digits occur only at even exponent positions, and let \(O_g\) consist of those whose nonzero digits occur only at odd exponent positions. Put \(A_g=E_g\cup O_g\). For every integer \(n\ge0\), let
\[
R_g(n)=\#\{(a,b)\in A_g^2:a\le b,\ a+b=n\}.
\]
Then, for every integer \(k\ge1\), the exact number of integers below the complete two-position-block cutoff with nonunique representations is
\[
\boxed{\#\{0\le n<g^{2k}:R_g(n)\ge2\}
=(3g-1)(2g-1)^{k-1}-2^{2k-1}-5k-1.}
\]
In the same interval the only integers with no representation are \(0\) and \(1\). Hence the number with exactly one representation is
\[
\boxed{g^{2k}-(3g-1)(2g-1)^{k-1}+2^{2k-1}+5k-1.}
\]
For each fixed \(g\ge4\), the nonuniqueness count is asymptotic to
\[
\frac{3g-1}{2g-1}(2g-1)^k,
\]
and its sharp exponent along these cutoffs is \(\log_{g^2}(2g-1)\).

## Assumptions and scope
The base \(g\) is an arbitrary **integer**, not necessarily prime. The base expansion of every \(n\in\mathbb Z_{\ge0}\) is unique, with digits in \(\{0,\ldots,g-1\}\) and the unit digit at exponent zero. All elements of \(A_g\) are strictly positive. Repetition of the same summand is allowed, but summand order is disregarded. The cutoff is strict: \(0\le n<g^{2k}\). The result does not assert an exact constant for arbitrary real cutoffs.

## Proof
**Step 1: separate three representation types.** A representation either has one summand in each of \(E_g,O_g\), both in \(E_g\), or both in \(O_g\). Because base-\(g\) digits of an even-supported and an odd-supported integer never overlap, the mixed representation exists precisely when \(n\) has at least one nonzero even-position digit and one nonzero odd-position digit, and is unique among mixed representations. Call such an integer *mixed*. Integers with digits supported on just one parity (including zero) are *pure*.

Let \(\widetilde E\), respectively \(\widetilde O\), be the integers below \(g^{2k}\) representable by two **nonnegative** numbers supported on even, respectively odd, digit positions. When an element of \(\widetilde E\) is mixed, some odd-position digit equals one and arises by carrying from two digits in the preceding even position; both summands are then automatically positive. Similarly, any mixed element of \(\widetilde O\) has a positive even-position digit produced by a carry from two odd-position digits, so both odd-supported summands are positive. Thus a mixed integer has at least two positive unordered representations exactly when it lies in \(\widetilde E\cup\widetilde O\).

**Step 2: exact digit counts for the two carry families.** For an even–even sum, each consecutive base-\(g\) digit pair \((d_{2j},d_{2j+1})\) can have either \(d_{2j+1}=0\) and any \(d_{2j}\in\{0,\ldots,g-1\}\), or \(d_{2j+1}=1\) and \(d_{2j}\in\{0,\ldots,g-2\}\). The second case corresponds to a carry; the two even-supported digit summands have sum \(g+d_{2j}\le 2g-2\). Consequently
\[
|\widetilde E|=(2g-1)^k.
\]
The pure-even portion has \(g^k\) possibilities, the pure-odd portion has \(2^k\), and their intersection is just zero, giving
\[
|\widetilde E\cap\{\text{mixed integers}\}|=(2g-1)^k-g^k-2^k+1.
\]
For an odd–odd sum, the units digit is zero. Each pair consisting of odd digit \(d_{2j+1}\) and next even digit \(d_{2j+2}\), for \(0\le j<k-1\), has \(2g-1\) admissible values by the same carry argument; the top odd digit has \(g\) admissible values, because a final carry beyond the cutoff is forbidden. Thus
\[
|\widetilde O|=g(2g-1)^{k-1},
\]
and its mixed portion has size
\[
g(2g-1)^{k-1}-g^k-2^{k-1}+1.
\]
The common portion \(\widetilde E\cap\widetilde O\) has units digit zero and every other digit either zero or one. Indeed the odd–odd condition bounds every higher even digit by one, while the even–even condition bounds each odd digit by one. Conversely, all these binary choices satisfy both local carry criteria when \(g\ge4\). Its mixed portion therefore has size
\[
2^{2k-1}-2^{k-1}-2^k+1.
\]
Inclusion–exclusion yields precisely
\[
B_{\mathrm{mixed}}=(3g-1)(2g-1)^{k-1}-2g^k-2^{2k-1}+1
\]
mixed integers with at least two representations.

**Step 3: classify pure integers.** There are exactly \(2g^k-1\) pure integers in the interval (counting zero once). Among these, \(0\) and \(1\) are the only unrepresented integers. To see this, every positive pure even integer other than \(1\) either decomposes into two strictly positive even-supported summands or, when it is a single digit \(1\) at a positive even exponent, decomposes into two odd-supported summands via a carry. The symmetric argument handles pure odd integers, since their lowest nonzero exponent is always positive.

The following are **all** pure integers with exactly one unordered representation:

* A single even-position nonzero digit equal to \(2\) or \(3\): \(2k\) integers.
* Exactly two even-position digits equal to \(1\), including the units digit: \(k-1\) integers.
* A single odd-position nonzero digit equal to \(2\) or \(3\): \(2k\) integers.

For justification, summands of the same parity with no carry split a lone digit \(d\) into \(\lfloor d/2\rfloor\) unordered positive pairs, while two isolated unit digits yield just their one partition into distinct summands. Any additional nonzero same-parity digit makes at least two partitions, except two digits equal to one. A pure even integer can also have an odd–odd decomposition only if its units digit is zero and every higher even digit is \(0\) or \(1\); a pure odd integer can have an even–even decomposition only if each odd digit is \(0\) or \(1\). These alternative decompositions eliminate the otherwise-single cases, except the displayed second case with units digit one. Finally, an isolated digit \(1\) beyond the units position has at least \(\lfloor g/2\rfloor\ge2\) unordered decompositions of the opposite parity, since the two preceding-position digits can sum to \(g\). This is the reason for the base threshold \(g\ge4\).

Thus there are \(5k-1\) uniquely represented pure integers and
\[
B_{\mathrm{pure}}=(2g^k-1)-2-(5k-1)=2g^k-5k-2
\]
pure integers with at least two representations. Adding \(B_{\mathrm{mixed}}\) and \(B_{\mathrm{pure}}\) proves the displayed formula. The uniqueness count follows by subtracting the two unrepresented integers and the nonuniqueness count from \(g^{2k}\).

**Step 4: sharp growth.** Since \(2g-1>4\) for \(g\ge4\), the lower-order terms \(2^{2k-1}\) and \(5k+1\) are negligible compared with \((2g-1)^k\). This gives both the asymptotic constant and the exponent.

## Verification
The accompanying standalone `check.py` constructs the digit-partition basis independently and directly enumerates all unordered summand pairs whose sum is below \(g^{2k}\). It checks every combination \(4\le g\le10\) and \(1\le k\le3\), comparing the actual representation function against the exact nonuniqueness and uniqueness formulas and verifying that the zero-set is \(\{0,1\}\). The program checks \(21\) configurations and \(3{,}550{,}513\) contributing summand pairs, with final marker `CERTIFICATE_OK`. These finite checks corroborate, but do not replace, the proof for arbitrary \(g,k\).

## Relationship to prior work
Ling and Tang (2015) studied **the same even–odd digit-partition basis for all bases** and proved thinness, strong minimality, and density-one uniqueness (in their ordered-pair convention, two representations). Their Theorem 1.1 and its proof give no exact count of exceptional integers at finite digit cutoffs. Tang (2026) proves density-one uniqueness for a larger class of \(g\)-adic minimal bases, also without the exact formula for this special partition. Tang and Ling (2018) treat partition conditions for minimality rather than exact multiplicity counts. The new assertion quantifies the exceptional set at every base \(g\ge4\), and determines its growth exponent. A separate ternary specialization is known; the classification of pure unique representations genuinely changes at base four, because \(\lfloor g/2\rfloor\) becomes at least two.

## Limitations
No theorem is asserted for base two or three, arbitrary partitions, more than two summands, or unrestricted cutoffs. The exact asymptotic is along complete \(g^{2k}\) cutoffs. The literature comparisons cannot exclude an equivalent formula hidden in a separate earlier publication. No independent validation has been performed.

## References
1. D. Ling and M. Tang, *On minimal asymptotic \(g\)-adic bases*, Bulletin of the Australian Mathematical Society **92** (2015), 374–379, DOI:10.1017/S0004972715000805. Full six-page primary article inspected.
2. M. Tang, *Minimal asymptotic \(g\)-adic bases from arbitrary partitions*, arXiv:2610.23152v1, first posted 2026-10-16, primary MSC 11B13. Primary full text inspected.
3. M. Tang and D.-R. Ling, *On asymptotic bases and minimal asymptotic bases*, arXiv:1810.10925v1 (2018). Full online text inspected.
