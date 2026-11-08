# Independent mathematical audit

## correctness

PASS

All nonconstant palindromes center at a complete equal-symbol run; symmetric wings are forced by alternating a/b run lengths, and boundary distances at j-th run are min((j-1)p,(k-j)p+b) or min((j-1)p+a,(k-j)p). Their maximum over run indices gives displayed R0,R1 (odd/even k). Every binary palindromic cvc extension of an occurring interior is a unique candidate; subtracting already present palindromes gives B(z)=2z^2H-H+1+2z. The radii sum (k-1)p, so |MAPW|=kp+4 and longest=kp-min(a,b)+2. Independent literal-factor checker recomputed every occurrence and MAPW length coefficient in 125 triples 1<=a,b,k<=5; no finite experiment substituted for the all-triples proof.

## originality

PASS

The general eertree missing-palindromic-extension theorem is Mieno et al. prior work; rich periodic words already explain the easy total count |W|+4. No examined primary result gives both finite-power run-center rays and the complete coefficient-by-coefficient MAPW length spectrum. Qualifies only on the explicit structure/spectrum, with residual specialized-formula risk.

## value

PASS

The complete spectrum, not the previously inferable total, is a natural exact boundary-sensitive string invariant; the two distinct center radii permit individual length counts and maximum length for all finite two-block powers. It is reusable in palindrome-indexing and absent-palindrome benchmarks without presenting a routine generic missing-edge identity as new.

The dated certificate retains the supplied scientific assessment, sources and limitations.
