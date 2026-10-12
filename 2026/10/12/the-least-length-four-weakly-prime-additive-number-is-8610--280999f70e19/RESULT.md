# The least length-four weakly prime-additive number is 8610

## Finding
A positive integer \(n\) is weakly prime-additive if there are distinct prime divisors \(p_1,\ldots,p_t\mid n\) and positive integers \(a_1,\ldots,a_t\) such that
\[
n=p_1^{a_1}+\cdots+p_t^{a_t}.
\]
Write \(\kappa_n\) for the minimum possible \(t\). Then the least integer with \(\kappa_n=4\) is
\[
\boxed{8610}.
\]
More precisely, no \(n<8610\) has length \(4\), while
\[
8610=2\cdot3\cdot5\cdot7\cdot41
\]
has the unique four-term representation, up to ordering,
\[
8610=3^8+5^2+7^3+41^2.
\]

## Assumptions and scope
All exponents are positive integers and the prime bases in a representation are distinct prime divisors of the represented integer. The statement concerns the exact least element of the length-
\(4\) class; it makes no asymptotic claim about how often length \(4\) occurs.

## Proof
A representation with two terms is impossible. Indeed, if \(n=p^a+q^b\) for distinct primes \(p,q\mid n\), reduction modulo \(p\) gives \(q^b\equiv0\pmod p\), contradicting \(p\ne q\). Thus every weakly prime-additive number has length at least \(3\).

For \(8610\), direct arithmetic gives
\[
3^8=6561,\qquad 5^2=25,\qquad 7^3=343,\qquad 41^2=1681,
\]
and their sum is \(8610\). Each base divides \(8610\), so \(\kappa_{8610}\le4\).

It remains to exclude a three-term representation of \(8610\) and every length-
\(4\) integer below it. The accompanying exact checker performs a finite exhaustive enumeration. For each \(2\le n\le8610\), it factors \(n\), chooses every three- and four-element subset of its distinct prime divisors, enumerates every positive power of each chosen prime that is smaller than \(n\), and tests the resulting sums using exact integer arithmetic. The first \(n\) with at least one four-term representation and no three-term representation is \(8610\). At \(8610\) the three-term list is empty and the four-term list consists of exactly the displayed representation. Combined with the two-term obstruction, this proves both \(\kappa_{8610}=4\) and minimality.

## Verification
Run `python3 verify.py`. The expected terminal line is:

`VERIFY_OK first_length4=8610 three_reps=0 four_reps=1 factor_primes=2,3,5,7,41 witness=3^8+5^2+7^3+41^2`

The checker uses only exact integer arithmetic and the Python standard library. Its search is exhaustive over the finite domain stated in the proof; no probabilistic primality test, floating-point comparison, or external table is used.

## Relationship to prior work
Fang and Chen introduced the terminology of shortest weakly prime-additive numbers for length \(3\). Leung's paper studies the length-
\(4\) class directly and, under a stated prime-distribution assumption known under GRH, proves that for every positive integer \(m\) infinitely many length-
\(4\) examples are divisible by \(m\). That result establishes conditional infinitude but does not identify the least example.

OEIS A296717 lists weakly prime-additive numbers and explicitly records \(8610\) among those that are not shortest. Its current entry and b-file do not state that \(8610\) has length exactly \(4\), do not give the four-term representation above, and do not establish that no smaller nonshortest term has length \(4\). The present finite classification supplies precisely those three facts.

## Limitations
The result is a finite least-element theorem. It does not prove unconditional infinitude of length-
\(4\) weakly prime-additive numbers, does not classify all later length-
\(4\) examples, and does not give a density or counting asymptotic. The originality comparison is limited by the possibility of unindexed computations not present in the inspected literature and databases.

## References
1. W. H. Leung, “On the Weakly Prime-Additive Numbers with Length 4,” arXiv:1903.10668v1 (2019); INTEGERS 24 (2024), Article A9, DOI: 10.5281/zenodo.10580934.
2. J.-H. Fang and Y.-G. Chen, “On the shortest weakly prime-additive numbers,” Journal of Number Theory 182 (2018), 258–270, DOI: 10.1016/j.jnt.2017.06.013.
3. OEIS Foundation Inc., OEIS A296717, “Weakly prime-additive numbers,” including the linked b-file through the relevant range.
