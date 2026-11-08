# Independent mathematical audit

## correctness

PASS

PASS. Normalize the one-sided exponential sqrt(2gamma) exp(-gamma x) 1_{x>0} and ab=2/3 by unitary dilation, set eta=gamma/b, u=exp(-2eta/3). Rational 3/2 oversampling gives a 2-by-2 fiber from 3 translation residue classes and 2 sequence components. Direct summation of geometric Fourier series gives trace T=sum_{j=0}^5 u^j and determinant u(1+u^2)|1-u^3 z|^2 in the Gram numerator. The eigenvalue extrema occur at phase z=1 and opposite x endpoints by monotonicity in |1-u^3 z|^2 and exp(-2eta x). They yield sharp bounds A=F(u)u(1-sqrt(1-h(u))), B=F(u)(1+sqrt(1-h(u))) with h=4u(1+u^2)(1-u)^2/(1+u^3)^2. The exact palindromic derivative identity gives the only possible stationary u via s=(3+sqrt(65))/2, and K=B/A diverges at both endpoints, proving the unique global optimum at eta=1.25698128176 and K=11.23795167. Independently recomputed an arbitrary fiber by an 80-term Fourier geometric sum and matched the analytic spectrum to floating tolerance; this finite check supports, not proves, global sharpness.

## originality

PASS

PASS with explicit priority qualification. The rational Zak/Zibulski–Zeevi reduction is classical, and Janssen’s 1995 general formula could in principle be specialized. Faulhuber–Shafkulovska’s inspected Theorem 2.6 and section 7 assume integer oversampling n∈N, and Janssen 1996 treats integer-oversampled exponentials. They do not themselves give the noninteger density-3/2 sharp constants or unique radical optimizer.

## value

PASS

PASS. Density 3/2 is the smallest noninteger rational oversampling with a nontrivial coupled matrix fiber, furnishing exact best frame bounds and a uniquely optimal rectangular time/frequency aspect for a classical window. This is a natural conditioning benchmark extending beyond integer lattice formulas.

The dated certificate retains the supplied scientific assessment, sources and limitations.
