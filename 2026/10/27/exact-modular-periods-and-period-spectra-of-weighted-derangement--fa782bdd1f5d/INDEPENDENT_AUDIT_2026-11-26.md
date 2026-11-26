# Independent mathematical audit

## correctness

PASS

Expanding the fixed-point weight by subsets gives (n!/j!)u^j for subsets of size j. The resulting recurrence R_n=nR_{n-1}+u^n starts at R_0=1 and yields R_{m+n}=u^m R_n modulo m, by the vanishing term at n=m followed by induction. Thus lcm(m,ord_m(u)) is a full period. For any period P from index zero, the recurrence differences at n=1 and n=2 give P=u(1-u^P) and P(1+u)=u^2(1-u^P) modulo m. Subtracting u times the first from the second gives P=0 modulo m, and then cancellation of the unit forces u^P=1 modulo m. This is necessary for every P, not simply divisors of the candidate. A finite abelian unit group contains an element of order equal to its exponent, whose powers attain all exponent divisors; taking prime valuations of lcm(m,h)/m gives exactly the divisors of lambda(m)/gcd(lambda(m),m). At m=2 the order of -1 is 1 and the stated even-modulus rule is still correct. Inspected VERIFICATION.md and verify.py without executing frozen code. Independent bounded replay: python3 /workspace/independent_checks.py computes residues from the polynomial rather than the recurrence and finds primitive words by prefix comparisons for all 773 unit-parameter pairs with 2<=m<=50. This corroborates the period and spectra on that range; the exact argument has no upper bound on m.

## originality

PASS

The supported distinct claim is the exact least-period law for every unit-weight evaluation and composite or prime modulus, together with the complete unit-parameter spectrum. The recurrence and some modular upper bounds are known. Prior indexed dyadic residue multiplicities already imply the exact ordinary-derangement period on their range; this is a genuine overlap with a specialization, not a second independent novelty claim. Neither the inspected prior congruences nor the indexed dyadic results supply both necessary divisibilities for arbitrary unit weights. A highly relevant older modular periodicity paper remains a named risk, not evidence of either coverage or noncoverage.

## value

PASS

The weighted fixed-point enumerator is classical, and its least modular period is a natural exact invariant rather than a handpicked finite slice. The lower obstruction collapses possible smaller periods to simultaneous divisibility by m and the unit order, resolving the ambiguity in an upper bound. The resulting spectrum describes every possible period across unit weights, including when a modulus admits more than one, and can be used directly without computing the sequence. The ordinary example illustrates rather than supplies the distinct contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
