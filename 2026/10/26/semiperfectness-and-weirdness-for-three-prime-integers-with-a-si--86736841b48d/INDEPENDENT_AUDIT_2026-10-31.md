# Independent mathematical audit

## correctness

PASS

For n=2p^a q^b, p<q odd primes, sigma(n)/n=(3/2)(sum_{i=0}^a p^{-i})(sum_{j=0}^b q^{-j}). If p>=7 q>=11 then upper bound <=77/40<2; if p=5 q>=17 it is <=255/128<2; p=5,a=1,q=11 or13 gives upper bound <=99/50<2. Thus only p=3 or (5,7),(5,11),(5,13) remain. Every p=3 n is multiple of semiperfect 6. The lone squarefree odd-part case 70 has sigma=144 but is not semiperfect: an excluded set would total sigma−2n=4, whereas available proper divisors <=4 are only 1,2. Exact divisor-complement seed certificates: 350 exclusion 2+7+10+25=44; 490 exclusion 1+10+35=46; 550 exclusion 1+5+10=16; 650 exclusion 2=2. Complements of excluded proper divisors sum each seed. Semiperfectness passes to multiples, and all surviving families have one seed as divisor. Every proper divisor of the seeds is deficient or equals 70,110,130, all nonsemiperfect, so seeds are primitive. All other semiperfect members contain a proper semiperfect divisor. Independent subset-sum and classification checks for 495 parameter instances n<=15000 confirmed; proof applies to unbounded exponents.

## originality

PASS

Best-of-knowledge originality of the precisely delimited final claim after comparing exact object/parameter theorem implications; known tools and antecedents are credited. Primary full-text coverage where available and access exceptions are disclosed. Benkoski–Erdős gives examples and general groundwork; Amato et al. gives other factor-bound results. The exact universal 2p^a q^b classification is not a direct consequence of either inspected statement without new argument.

## value

PASS

The natural fixed-support, v2(n)=1 family is completely classified for all exponents, including the unique weird exception and all primitive semiperfect members. Though seeds and 70 are classical, proving there are no other members in the infinite class is a motivated exact number-theoretic boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
