# Independent mathematical audit

## correctness

PASS

For two exact base-b digits 1<=a<b and 0<=c<b, digit-factorial fixed-point equation ab+c=a!+c! forces the UNIQUE base b=(a-1)!+(c!-c)/a. Integrality iff a divides c!-c. Exhaustive case split: c=0 only (a,c,b)=(1,0,2); c=1 or 2 requires a>=4 with b=(a-1)!; c>=3,a<=c gives a|c (because a|c!) and excludes sole (a,c)=(3,3) failing strict digit bound; c>=3,a>c gives a|c!-c, then b>(a) since a>=4. All inequalities and edge cases are algebraic. Disjoint divisor sets give for fixed c>=4 count tau(c)+#{a>c:a|(c!-c)}. Independently checked all 6480 digit pairs a=1..80,c=0..80, including c=0 and small bounds; finite checks corroborate unrestricted proof.

## originality

PASS

OEIS A193163 and A260651 already tabulate arbitrary-base factorions; public descriptions include (m,1),(m,2) at base (m-1)! and (1,m) at base m!-m+1. The submitted four-case theorem includes those families but also new c>=3,a>c divisor solutions (e.g. a=5,c=4 -> b=4!+4=28) and a COMPLETE iff converse/fixed-trailing divisor count. Kiss 1977 deals with decimal fixed points. Gupta 2004 note has closest title but complete text unavailable (Oxford vpn disconnected), so this remains material priority risk; elementary algebra classification could exist in unindexed recreational sources.

## value

PASS

Factorions are a natural digit-dynamical fixed-point object; classifying exactly two-digit solutions simultaneously for all integer bases yields the complete first nontrivial digit-length stratum. The forced-base and divisor dichotomy identify previously missing trailing/leading digit families and give an exact arithmetic fiber count tau(c)+number of large divisors of c!-c for fixed c>=4; these are natural precise answers, not arbitrary finite sample or only renamed standard examples. The elementary derivation does not by itself diminish the complete classification, but substantially longer lengths remain open.

The dated certificate retains the supplied scientific assessment, sources and limitations.
