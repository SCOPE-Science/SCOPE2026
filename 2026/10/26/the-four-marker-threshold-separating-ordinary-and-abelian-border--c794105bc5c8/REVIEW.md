# Independent mathematical audit

## correctness

PASS

Ordinary border implies Abelian border. For a binary word with <=3 occurrences of either bit, if endpoints agree it has a length-one ordinary border; otherwise orient 0...1, let a leading zero run and d final pre-one zero run. If a<=d the literal border 0^a1 exists. If a>d, any disjoint prefix/suffix before left first 1 has fewer 1s than the suffix, and with <=3 ones they cannot each have >=2 ones; hence no Abelian border. For four ones, write 0^a1 0^b1 0^c1 0^d1. Exceptional iff a>d, a+b<=c+d, b!=d; first two enforce an Abelian border with exactly two ones per side and prevent one-one literal border; b!=d excludes the only possible two-one literal border. Reversal covers endpoint 1...0; complementary words covered by sparse rigidity. Parametrize a=d+e,c=b+e+f with e>=1,f>=0,b!=d, yielding 4z^8/((1-z)(1-z^2)^2(1-z^4)), shortest n=8, B_n~n^3/24 and B_n/binom(n,4)~1/n. Independently enumerated all 44,550 words of length <=22 with <=4 ones and checked the mixed-border condition and initial coefficients; proof extends all lengths.

## originality

PASS

The shortest mixed-border word was already known; Goc–Rampersad–Rigo–Salimov (2014) full manuscript explicitly discusses binary Abelian-border paths and global counts, but does not classify the joint condition ordinarily unbordered AND Abelian bordered by exactly four occurrences. Christodoulakis et al (2014) relevant same-object abstract was accessible but full journal article unavailable. The new claim is the sharp sparse rigidity plus complete fixed-weight-four exceptional enumeration and rational generating function; the existence of the length-8 example is explicitly prior.

## value

PASS

The exact point where ordinary and Abelian border notions separate under sparse symbol multiplicity is a natural threshold in combinatorics on words; the first exceptional layer is a complete infinite family with explicit gap inequalities, rational enumerator and asymptotic proportion. This is more informative than merely repeating a known length-eight example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
