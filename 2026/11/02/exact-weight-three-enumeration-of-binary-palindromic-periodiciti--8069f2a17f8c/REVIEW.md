# Independent mathematical audit

## correctness

PASS

Definition reconstructed from a prefix of repetitions of a symmetric period. Writing marked positions as circular gaps (u,v,h) and offset x gives a bijection with positive u+v+h=n and 0<=x<h. The all-distinct case has offset count h for h<min(u,v), min(u,v) for min<h<max, and max(0,2max-h) for h>max; any coincident gap makes the full word symmetric. Verified the three-root-one-count cases and their offset intervals. Summing these disjoint cases gives the displayed rational generating function and hence the quasipolynomial via its cyclotomic denominator; highest-order pole 1/3 at z=1 proves Q(n)~n^3/18. Independent literal prefix-period/palindrome-split enumeration for all binom(n,3) words n=3..21 agreed with a separate gap summation and coefficients of a rational-denominator recurrence, including Q(3..17)=1,4,10,14,25,36,52,68,93,116,150,182,225,268,324. Finite checks corroborate, do not replace, all-n proof.

## originality

PASS

Fici–Shallit–Simpson establish the symmetric-word-period definition and general properties; their 2025 conclusion asks unrestricted counting. Their trapezoidal-word theorem and counts of symmetric words do not imply the fixed weight-three palindromic-periodicity generating function because proper symmetric periods contribute words that are themselves not symmetric. Simpson 2024 supplies the framework, not the resolved weight-three distribution. Best-of-knowledge distinct finite-weight exact result, with unindexed equivalent enumerations a residual risk.

## value

PASS

Weight three is the first nontrivial fixed Hamming-weight layer: all words with <=2 ones have reflection-symmetric circular mark sets. Exact rational enumeration for this first nontrivial layer is a natural structural step toward unrestricted palindromic-periodicity counting, with explicit density and quasipolynomial rather than only finite counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
