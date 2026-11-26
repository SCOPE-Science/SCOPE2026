# Independent mathematical audit

## correctness

PASS

Induction on the largest index partitions legal sums into [0,a_j) and a_j+[0,a_(j−f(j))), also when the second interval has length 1. Thus the uniform integer law is the uniform legal-word law. The capped gap automaton is exact, including F=0 (both choices go to the same state and weights add). With enough whole periods, zeros bring any state to F, and a single 1 followed by exactly s<F zeros reaches s; the all-zero word reaches F. Therefore the period matrix is primitive. Its simple Perron eigenvalue and analytic spectral projection give the normalized quasi-power with uniform analytic error at each of the finitely many residue classes. The stationary weighted-edge moment generating matrix is diagonally conjugate to P(e^t)/λ(1), so its first two limiting log derivatives are the same. The Poisson equation splits centered rewards into martingale differences plus a bounded boundary term. Zero rate would force each cycle reward to be its length times the mean; the zero loop and a longer returning walk with one 1 contradict this. A positive-reward edge has positive stationary mass, giving positive mean. Taylor expansion gives the CLT with exact centering/scaling, and subtracting a_n on the adjacent interval gives exactly 1+X_(n−f(n)) for large n. The supplied verifier was inspected, not run; a separate bounded enumeration of patterns (0) and (0,3,1) through n=10 corroborated the two interval bijections only. The exact finite check can be replayed by enumerating binary words on the relevant indices, retaining those satisfying the pair exclusion and testing that their subset sums list each indicated integer exactly once. It is not evidence for uniformity or a limit as f varies.

## originality

PASS

The supported claim is the all-periodic conclusion, with nondegeneracy verified for every fixed nonnegative gap pattern and both sampling intervals. The primary f-decomposition paper asks this question explicitly after proving a special b-bin case. The Kentucky theorem covers a second explicit pattern. Standard analytic automaton methods are not claimed as new: the substantive application is the general periodic gap automaton and its gap-rule-specific certificate of strict positivity, which does not follow merely from an unqualified invocation of a quasi-power theorem. I did not find a substantiated stronger claim that already solves the periodic f question; the closely relevant 2003 symbol-count theorem's full statement was not retrievable in the identified lawful copies.

## value

PASS

This resolves a natural question posed for the entire periodic family rather than computing another bin example. The positivity argument rules out hidden exceptional patterns, and the finite matrix gives usable mean and variance constants for any fixed list of gaps.

The dated certificate retains the supplied scientific assessment, sources and limitations.
