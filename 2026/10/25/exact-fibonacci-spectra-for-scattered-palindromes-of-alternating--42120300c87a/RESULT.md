# Exact Fibonacci spectra for scattered palindromes of alternating binary words

## Finding

For each integer \(N\geq 0\), let \(w_N\) be the length-\(N\) prefix of the alternating infinite binary word \(010101\cdots\). For \(1\leq k\leq N\), let \(p_{N,k}\) be the number of *distinct* nonempty palindromic strings of length \(k\) that occur as scattered subsequences of \(w_N\); set \(p_{N,k}=0\) otherwise. Then the complete length-refined generating function is

\[
\boxed{\sum_{N\geq0}\sum_{k\geq1}p_{N,k}z^N t^k
=\frac{tz(1+z)}{1-z}
+\frac{t^2z^3(1+z)\bigl(1+t(1+z^2)\bigr)}{(1-z)\bigl(1-t^2(z^2+z^4)\bigr)}.}
\]

Writing \(P_N=\sum_{k\geq1}p_{N,k}\), this specializes to

\[
\boxed{\sum_{N\geq0}P_Nz^N=\frac{z(1+z)(1+z^2)}{(1-z)(1-z^2-z^4)}.}
\]

For Fibonacci numbers \(F_0=0\), \(F_1=1\) and \(F_{j+2}=F_{j+1}+F_j\), the exact totals are

\[
\boxed{P_{2m}=2F_{m+3}-4\quad(m\geq1),\qquad P_{2m+1}=F_{m+5}-4\quad(m\geq0),\qquad P_0=0.}
\]

In particular, if \(\varphi=(1+\sqrt5)/2\), then

\[
P_{2m}\sim\frac{2\varphi^3}{\sqrt5}\,\varphi^m,
\qquad
P_{2m+1}\sim\frac{\varphi^5}{\sqrt5}\,\varphi^m,
\qquad \lim_{N\to\infty} P_N^{1/N}=\sqrt\varphi.
\]

## Assumptions and scope

Words have the fixed labeled binary alphabet \(\{0,1\}\). A scattered subsequence is obtained by deleting zero or more positions without reordering; distinct strings are counted once even if they have several embeddings. Palindrome means literal reversal invariance, not reverse-complement invariance. The empty string is excluded from all counts. The prefix \(w_0\) is empty. The formal variables \(z\) and \(t\) respectively mark the host-prefix length and the length of a counted palindrome. No assertion is made about maximization among all binary host words.

## Proof

**1. Greedy minimal-prefix cost.** For any nonempty binary word \(u=u_1\cdots u_\ell\), let \(c(u)\) be the length of the shortest alternating prefix containing \(u\) as a scattered subsequence. Greedily match each successive letter at its first available position. The initial match is at position \(1\) if \(u_1=0\), and position \(2\) if \(u_1=1\). Between consecutive matched letters, the position advances by \(1\) when the letters differ and by \(2\) when they agree. Induction on \(\ell\) proves that greedy matching finishes no later than any competing embedding, and hence

\[
\boxed{c(u)=\ell+\mathbf1_{\{u_1=1\}}+\sum_{j=1}^{\ell-1}\mathbf1_{\{u_j=u_{j+1}\}}.}
\]

Consequently \(u\) occurs in \(w_N\) if and only if \(c(u)\leq N\). This equivalence is exact for every nonempty \(u\), including the one-letter and two-letter boundary cases.

**2. Distinct palindrome enumeration by outer half.** Every palindrome of even length \(2h\), \(h\geq1\), has the unique form \(b_1\cdots b_h b_h\cdots b_1\). Its greedy cost is

\[
2h+1+\mathbf1_{\{b_1=1\}}+2\sum_{j=1}^{h-1}\mathbf1_{\{b_j=b_{j+1}\}}.
\]

The first letter contributes \(tz\)-independent multiplicity \(1+z\); the middle repeated pair incurs the additional \(z\); and each outward-to-inward transition contributes either \(t^2z^2\) (different) or \(t^2z^4\) (equal). More precisely, summing the even palindromes with \(z^{c(u)}t^{|u|}\) gives

\[
Q_{\mathrm{even}}(z,t)=\frac{t^2z^3(1+z)}{1-t^2(z^2+z^4)}.
\]

For odd length \(2h+1\), \(h\geq1\), insert one center letter after the half \(b_1\cdots b_h\). Relative to the even case, this changes the central \(z\) to \(tz\) when the center differs from \(b_h\), or to \(tz^3\) when it equals \(b_h\); the net factor is \(t(1+z^2)\). Therefore

\[
Q_{\mathrm{odd},\geq3}(z,t)=\frac{t^3z^3(1+z)(1+z^2)}{1-t^2(z^2+z^4)}.
\]

Finally the palindromes of length one, namely \(0\) and \(1\), contribute \(tz(1+z)\). The choices of outer halves and center letters are bijective with distinct palindrome strings, so no embedding multiplicity enters these sums. Adding the three cases yields

\[
Q(z,t):=\sum_{u\text{ nonempty palindrome}}z^{c(u)}t^{|u|}
=tz(1+z)+\frac{t^2z^3(1+z)(1+t(1+z^2))}{1-t^2(z^2+z^4)}.
\]

**3. From minimal lengths to host-prefix counts.** Each individual palindrome \(u\) contributes one unit to \(p_{N,|u|}\) exactly for \(N\geq c(u)\). Therefore summing \(z^N\) over host lengths multiplies the exact-cost series by \(1/(1-z)\), proving the bivariate generating function. Taking \(t=1\) gives the displayed univariate fraction after the polynomial cancellation

\[
(1-z^2-z^4)+z^2(2+z^2)=1+z^2.
\]

**4. Fibonacci coefficient extraction.** Substitute \(v=z^2\), split the fraction into even and odd powers of \(z\), and use

\[
\sum_{m\geq0}F_{m+3}v^m=\frac{2+v}{1-v-v^2},\qquad
\sum_{m\geq0}F_{m+5}v^m=\frac{5+3v}{1-v-v^2}.
\]

One obtains the parity generating functions

\[
\sum_{m\geq1}P_{2m}v^m
=\frac{2(2+v)}{1-v-v^2}-\frac4{1-v},\qquad
\sum_{m\geq0}P_{2m+1}v^m
=\frac{5+3v}{1-v-v^2}-\frac4{1-v}.
\]

Their coefficients give the two stated Fibonacci formulas, including \(P_0=0\). Binet's identity \(F_j=(\varphi^j-(-\varphi)^{-j})/\sqrt5\) then proves the parity-sensitive asymptotics and the common exponential base \(\sqrt\varphi\).

**5. Comparison with all distinct scattered subsequences.** The same greedy cost formula without the palindrome condition gives the exact-cost series \((z+z^2)/(1-z-z^2)\): choose the initial bit of cost \(z\) or \(z^2\), then at each extension choose a changed bit of cost \(z\) or a repeated bit of cost \(z^2\). Thus the number \(U_N\) of all distinct nonempty subsequences satisfies

\[
\sum_{N\geq0}U_N z^N=\frac{z+z^2}{(1-z)(1-z-z^2)}.
\]

Its exponential growth base is \(\varphi\), whereas the palindrome count has base \(\sqrt\varphi\). In particular, \(\lim_{N\to\infty}N^{-1}\log(P_N/U_N)=-\tfrac12\log\varphi\). This comparison is a corollary for this alternating family, not an extremal statement about arbitrary host words.

## Verification

The independent checker `verify_alternating.py` generates the entire distinct-subsequence set by successive single-letter extensions for every alternating prefix length from \(0\) through \(22\), then filters literal palindromes and records counts by palindrome length. Separately, it expands the displayed bivariate rational series by a formal denominator recurrence; the two length spectra agree in every tested case. It also independently checks the Fibonacci totals and the known published values \(1,2,4,6,9,12,17,22,30,38\) for host lengths \(1\) through \(10\). All checks terminate successfully. These finite checks support, but do not substitute for, the proof applying to every \(N\).

## Relationship to prior work

Mahalingam and Pandoh (2021), *Counting scattered palindromes in a finite word*, introduced the distinct scattered-palindrome statistic and tabulated its **maximum over binary words** for host lengths through \(10\); Table 4 gives precisely the initial values obtained here for the alternating family. Their Section 4 proves general upper bounds and Section 5 treats the large-alphabet regime \(q\geq N/2\); their conclusion leaves the fixed-small-alphabet regime unresolved. The present claim is not that those listed values are new, but rather that the complete length-resolved rational generating function, the exact all-length Fibonacci formulas, and their alternating-family asymptotics hold. A maximum-over-all-binary-words theorem is neither claimed nor required for this result.

Müllner and Ryzhikov (2019), *Palindromic Subsequences in Finite Words*, study extremal **lengths** of palindromic or antipalindromic subsequences, not the number of distinct palindromic strings in alternating prefixes. Results about contiguous palindromic **factors** are not equivalent to scattered-pattern counts. General algorithms for counting distinct palindromic subsequences of a given input word do not by themselves provide this closed rational bivariate family formula without a new analysis of the alternating structure.

## Limitations

The result does not establish which binary words maximize the number of distinct scattered palindromes at arbitrary length. It neither counts embeddings with multiplicity nor extends directly to arbitrary periodic words or alphabets of size greater than two. The detailed analysis is elementary enough that an equivalent formula in unindexed earlier literature is possible; the closely related 2009 *On highly palindromic words* was available only as a bibliographic description, not inspected in full. The numerical checks are finite; completeness for all host lengths follows from the greedy-cost bijection and exact formal-power-series algebra, not the checker output.

## References

1. K. Mahalingam and P. Pandoh, *Counting scattered palindromes in a finite word*, arXiv:2108.02729, first publicly submitted 2021-08-05. https://arxiv.org/abs/2108.02729
2. C. Müllner and A. Ryzhikov, *Palindromic Subsequences in Finite Words*, arXiv:1901.07502, first publicly submitted 2019-01-22. https://arxiv.org/html/1901.07502v1
3. Š. Holub and K. Saari, *On highly palindromic words*, Discrete Applied Mathematics 157 (2009), 953–959. (Full text not inspected; comparison limited to the account in reference 1.)
