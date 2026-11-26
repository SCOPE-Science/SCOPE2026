# Independent mathematical audit

## correctness

PASS

For each size-m support the restriction is uniform: fixing any restricted word leaves the same number of placements of its 2m positions and fillings with the complementary labels. No paired letter may occur more than twice, so on a full support a palindrome is either the entire even restriction or the entire restriction minus one copy of the center. There are m! templates of each parity. For a fixed odd template the 2m possible insertion gaps yield 2m-1 distinct host words: only the two gaps next to the unique center yield the same word. Double-counting word/string pairs and dividing by (2m)!/2^m gives 2m/(2m-1)!! per support; linearity does not require independent restrictions. For the asymptotic, write the summand as (2q)^m/(2m-1)! times the falling-factorial correction R_{q,m}=product_{j<m}(1-j/q), taking R=0 above q. Under weights proportional to (2q)^m/(2m-1)!, the variable 2m-1 is Poisson(sqrt(2q)) conditioned odd. Its odd-event probability tends to 1/2, so the usual Poisson concentration gives m/sqrt(q) tending to 1/sqrt(2). On any fixed compact neighborhood of this ratio, log R=-m(m-1)/(2q)+O(m^3/q^2), tending to -1/4 in probability; boundedness yields convergence of its mean. The weight sum is sqrt(2q)sinh(sqrt(2q)). This establishes the prefactor and scale, including the correct factorial normalization. The checker was inspected, not executed.

## originality

PASS

The supported distinct claim is the uniform multiplicity-two expectation for distinct palindrome strings and its sharp leading asymptotic, not the known extremal count, basic chord matching counts, or standard asymptotic analytic techniques. Direct comparison includes an exact mean-level weighted nesting representation; no inspected source gives this target mean as such a weighted statistic together with the necessary palindrome relationship or the stated sharp growth law.

## value

PASS

Uniform matching of the two occurrences of every symbol is a natural fixed-content model. Its exact expected number of distinct symmetric patterns is not inferred from the known sharp exponential maximum. The result distinguishes average and extremal growth quantitatively, including the leading correction to the unconstrained Poisson-style sum. This provides a benchmark for other word models or higher-moment analysis without claiming concentration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
