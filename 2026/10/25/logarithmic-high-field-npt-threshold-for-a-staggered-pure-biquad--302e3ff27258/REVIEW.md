# Review: Logarithmic high-field NPT threshold for a staggered pure-biquadratic spin-1 dimer

## Correctness

The claim is restricted to \(J>0\), \(h>0\), \(k_B=1\), and \(h/J\to\infty\). The exact singlet-projector identity and the three 2×2 partial-transpose blocks reduce the NPT question to three scalar inequalities. The lowest-eigenpair expansion gives the controlling block entry, and the other two inequalities remain inactive at the first crossing. Numerical values from `verify_threshold.py` corroborate the expansion but are not used as proof.

## Originality

The closest published work inspected includes the 1989 spin-1 biquadratic chain, the 2011 two-qutrit XXZ-plus-DM model in an inhomogeneous field, the 2005 nonlinear-coupling optical-lattice abstract, and the 2021 open spin-1 dimer paper with uniform field and single-ion anisotropy. None of the read statements gives the exact Hamiltonian and logarithmic NPT coefficient here. The 2005 and 1989 full texts were not accessible in the bounded search, so residual overlap risk remains.

## Value

The asymptotic threshold is a natural thermal-robustness invariant for a staggered-field spin-1 dimer. It predicts NPT at temperatures asymptotically large relative to J but small relative to h, with the coefficient fixed by a particular partial-transpose block. This is more informative than a finite parameter sweep.

Self-review: passed. Independent audit: not yet performed.
