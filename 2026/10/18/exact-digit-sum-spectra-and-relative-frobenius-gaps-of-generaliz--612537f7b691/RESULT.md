# Exact digit-sum spectra and relative Frobenius gaps of generalized repunits

## Finding

Fix integers \(b\ge2\) and \(r\ge4\). Let \(s_b(N)\) be the ordinary base-\(b\) sum of digits and let the length-\(r\) repunit be
\[
M_{b,r}=1+b+\cdots+b^{r-1}=\frac{b^r-1}{b-1}.
\]
The full set of positive digit sums attained by positive multiples of this modulus is
\[
\boxed{\mathcal S_{b,r}=\{s_b(kM_{b,r}):k\ge1\}
=\bigcup_{j=1}^{b-1}\{rj+(b-1)t:t\in\mathbb Z_{\ge0}\}.}
\]
Thus the arithmetic progressions above, without any exceptions inside them, are exactly the attainable digit sums. Put \(d=\gcd(r,b-1)\), \(a=r/d\), and \(c=(b-1)/d\). In the sublattice of positive multiples of \(d\), there are exactly
\[
\boxed{G^{(d)}_{b,r}=\frac{(a-1)(c+1)}2}
\]
missing values. The greatest missing positive multiple of \(d\) is \(F^{(d)}_{b,r}=dc(a-1)\) if \(a>1\); when \(a=1\), the spectrum is precisely all positive multiples of \(d\), and by convention we put \(F^{(d)}_{b,r}=0\). The first positive multiple of \(d\) beyond every gap, a sharp relative conductor, is therefore \(d[c(a-1)+1]\). If \(d=1\) these are the usual Frobenius number, genus, and conductor; if \(d>1\), infinitely many nonmultiples of \(d\) remain excluded and ordinary cofinite Frobenius terminology is inapplicable.

For instance, multiples of decimal \(1111\) have every positive digit sum except
\[
\{1,2,3,5,6,7,9,10,11,14,15,18,19,23,27\};
\]
this is an exact 15-gap classification and the ordinary conductor is \(28\).

## Assumptions and scope

Here \(b\) and \(r\) range independently over integers, with \(b\ge2\) and \(r\ge4\). The multiplier \(k\) ranges over *all* positive integers, with no upper bound. A digit sum is always computed from the standard positional expansion with digit values in \(\{0,1,\dots,b-1\}\). In the progressions, \(j\) is an integer between \(1\) and \(b-1\), inclusive, and \(t\) is a nonnegative integer. Only relative gaps among positive multiples of \(d\) are counted by \(G^{(d)}_{b,r}\).

## Proof

**1. Reduce every attainable sum by cyclic carries.** Write any positive multiple \(N=kM_{b,r}\) as a sum of \(w=s_b(N)\) powers of \(b\), each ordinary base-\(b\) digit of value \(u\) being expanded into \(u\) unit summands. As \(b^r\equiv1\pmod{M_{b,r}}\), grouping exponents modulo \(r\) gives nonnegative integers \(c_0,\ldots,c_{r-1}\), with \(\sum_i c_i=w\), such that
\[
\sum_{i=0}^{r-1}c_i b^i\equiv0\pmod{M_{b,r}}.
\]
Whenever some \(c_i\ge b\), remove \(b\) units from position \(i\) and add one unit at position \(i+1\pmod r\). For \(i<r-1\), the change in numerical value is exactly zero. For \(i=r-1\), the change is \(1-b^r\), divisible by \(M_{b,r}\). Consequently, divisibility is preserved. The total unit count decreases by exactly \(b-1>0\) at each step; it never becomes zero, because replacing \(b\) nonnegative units by one still leaves a positive count. The process therefore terminates in a nonzero vector \((u_0,\ldots,u_{r-1})\) with \(0\le u_i<b\).

The resulting integer \(T=\sum_{i=0}^{r-1}u_i b^i\) is a positive multiple of \(M_{b,r}\) and satisfies \(1\le T\le b^r-1=(b-1)M_{b,r}\). Thus \(T=jM_{b,r}\) for a unique \(j\in\{1,\ldots,b-1\}\). Since the standard base-\(b\) expansion of \(jM_{b,r}\) consists of \(r\) copies of the digit \(j\), the terminal count is \(rj\). If \(t\) reductions occurred then \(w=rj+(b-1)t\). This proves *necessity*, including the precise nonnegative sign of \(t\).

**2. Construct a positive multiple for every proposed sum.** Start with \(c_i=j\) for every \(0\le i<r\), where \(1\le j\le b-1\). Its weighted value is \(jM_{b,r}\), a multiple of the modulus, and its unit count is \(rj\). To increase that count by \(b-1\), choose any occupied coordinate \(i\), remove one unit there, and insert \(b\) units at coordinate \(i-1\pmod r\). If \(i>0\), the weighted value is unchanged; if \(i=0\), it changes by \(b^r-1\), still divisible by the modulus. At every stage at least one coordinate remains occupied. Repeating this operation \(t\) times yields nonnegative counts \(c_i\) summing to \(rj+(b-1)t\) and having weighted sum divisible by \(M_{b,r}\).

Turn this cyclic multiset into ordinary distinct powers of \(b\) by using, for each position \(i\), the exponents \(i,i+r,\dots,i+r(c_i-1)\). Across all positions these exponents are pairwise distinct. Consequently,
\[
N=\sum_{i=0}^{r-1}\sum_{h=0}^{c_i-1}b^{i+rh}
\]
has digits only zero or one, so \(s_b(N)=\sum c_i=rj+(b-1)t\). Also \(N\equiv\sum c_i b^i\equiv0\pmod{M_{b,r}}\). It is strictly positive. This proves *sufficiency* and the exact spectrum.

**3. Compute the exceptional relative genus and conductor.** With \(d=\gcd(r,b-1)\), \(a=r/d\), \(c=(b-1)/d\), observe that \(\gcd(a,c)=1\). Progressions with indices \(j\) and \(j+c\) differ by \(rc=(b-1)a\); thus every progression with \(j>c\) is contained in an earlier one. After dividing the spectrum by \(d\), one obtains exactly
\[
\bigcup_{j=1}^{c}\{aj+ct:t\ge0\}.
\]
Because \(a\) is invertible modulo \(c\), these \(c\) progressions occupy each residue class modulo \(c\) exactly once. For a given \(j\), the positive integers in its residue class *not* attained number exactly \(\lfloor(aj-1)/c\rfloor\). The identity
\[
\sum_{j=1}^{c}\left\lfloor\frac{aj-1}{c}\right\rfloor
=\frac{(a-1)(c-1)}2+(a-1)
=\frac{(a-1)(c+1)}2
\]
follows from the permutation of nonzero residues \(aj\bmod c\) for \(1\le j<c\), together with the \(j=c\) term \(a-1\). This includes the case \(c=1\). The largest omitted positive integer in the rescaled lattice is \(c(a-1)\), the predecessor of the starting value \(ac\) in the zero residue class; it is absent when \(a>1\). Every other omitted integer is smaller, since its progression starts at \(aj\le ac\). If \(a=1\) there are no positive omissions and the same bound equals zero. Multiplication by \(d\) establishes the stated relative Frobenius number, gap count, and sharp relative conductor. \(\square\)

## Verification

Run `python3 verify.py` with Python 3 and no additional dependencies. It independently constructs reachability by residue-state dynamic programming, for all selected settings with modulus at most 1800; compares 1518 attainable-digit-sum decisions in 34 base/length settings with the exact progression formula; directly checks finite relative-gap counts and boundaries; and constructs 1260 explicit positive multiples using the inverse-carry algorithm for lengths from four through seven. It reports `PASS` when every assertion holds. These checks are finite corroboration, not an exhaustive test of infinitely many bases, lengths, or multipliers; the quantified theorem follows from the preceding symbolic proof.

## Relationship to prior work

The core questions of which digit sums appear as multiples and whether the spectrum is cofinite were formalized by Phunphayap, Noppakaew, and Pongsriiam (2023); their Theorem 1 gives the gcd-based congruence condition, while Question 2 requests complete spectra when that restriction is not sufficient. Clokie, Lidbetter, Molina Lovett, Shallit, and Witzman (2020) proved general equivalence with sums of distinct powers (Theorem 3), upward closure by increments of \(b-1\) (Theorem 4), and sturdiness of the generalized-repunit family (Corollary 7). These are important antecedents but do not themselves tabulate the residue-class threshold \(rj\) for every class, the complete length-\(r\) spectrum, or the sharp gap count/conductor. Dartyge, Luca, and Stănică (2009) studied equal digit sums of multiples and a density-zero property for globally sturdy numbers; their results concern a different invariant. The proof above derives the previously unstated cyclic-normal-form threshold for all lengths \(r\ge4\). Length three already admits a separate complete calculation and is deliberately outside the new claim.

## Limitations

No conclusion about digit sums of multiples of arbitrary moduli is asserted. For \(d>1\), the ordinary Frobenius number over all positive integers does not exist because nonmultiples of \(d\) are never represented. The finite checks do not replace the all-parameter proof. An independent mathematical audit has not been performed. A possible unpublished or unindexed exact-spectrum treatment, or an unnoticed explicit corollary in older digit-sum work, remains a literature-overlap risk.

## References

1. T. Clokie, T. F. Lidbetter, A. Molina Lovett, J. Shallit, and L. Witzman, *Computational Aspects of Sturdy and Flimsy Numbers*, first arXiv version 2020-02-07, arXiv:2002.02731, https://arxiv.org/abs/2002.02731 .
2. P. N. Phunphayap, P. Noppakaew, and P. Pongsriiam, *Directed graphs of integers with arcs determined by an arithmetic function*, first arXiv version 2023-03-23, arXiv:2303.13017, https://arxiv.org/abs/2303.13017 .
3. C. Dartyge, F. Luca, and P. Stănică, *On digit sums of multiples of an integer*, Journal of Number Theory 129 (2009), 2820–2830, DOI:10.1016/j.jnt.2009.04.003, https://faculty.nps.edu/pstanica/research/2009JNT_digit-sums-multiple.pdf .
