# Independent mathematical audit

## correctness

PASS

For indexed binary cyclic words, nonconstant profiles have z zeros, o=n-z ones and t= m01=m10>=1. Mark a 01 transition and compose t alternating nonempty runs to derive exactly B_n(z,t)=n/t*C(z-1,t-1)*C(o-1,t-1), valid for periodic words. For t>=2 the adjacent-z ratio has cleared difference (t-1)(n-2z-1), forcing centered z/o; n>=6 centered t=2 dominates all t=1. The t-ratio (z-t)(o-t)/(t(t+1)) has sign from zo-t(n+1). The four n mod 4 cases yield the asserted exact H_n, all optimizer ties, and boundary n<=5; Stirling gives 4*2^n/(pi*n)(1+O(1/n)). Independently enumerated every indexed word through n=14 and independently compared all fibers and maxima, including H6=12,H8=36,H9=54,H12=400,H14=1400; actual supplied verify.py and crosscheck.cpp code and blob IDs inspected. These finite checks corroborate, not prove, the all-n ratios.

## originality

PASS

Known Whittle-type formulas count one fixed Markov type, and Jacquet–Knessl–Szpankowski count the number of balanced types; neither supplies the exact global largest type class, four congruence-dependent optimizers and all short-length ties. The established per-fiber composition formula is not claimed as original. A targeted Resultary search surfaced only distinct linear multispectrum counts and other read channels; historical priority remains best-of-knowledge.

## value

PASS

Worst inverse list size is an intrinsic ambiguity invariant of exact cyclic 2-gram reconstruction. An all-length sharp value with the optimal symbol counts, run counts, unusual n=4k+1 ties and asymptotic leading constant is a usable precise extremal fact for reconstruction, unlike merely counting output classes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
