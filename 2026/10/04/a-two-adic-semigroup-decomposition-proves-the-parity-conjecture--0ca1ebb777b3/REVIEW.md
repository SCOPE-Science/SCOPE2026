# Independent mathematical audit

## correctness

PASS

The stabilization-to-semigroup step is exact: after subtracting the \(j\) padding copies of \(1^k\), a fixed offset is eventually representable precisely when it lies in \(S_k\). Every even-base generator reduces recursively by \((2m)^k-1=(m^k-1)+m^k(2^k-1)\), leaving the odd generator \(A_k\) plus even odd-base generators. Splitting the coefficient of \(A_k\) by parity gives the disjoint decomposition. \(T_k\) is numerical because \(A_k\) is odd and \(\gcd(A_k,(A_k^k-1)/2)=1\). Even gaps of \(S_k\) are twice the positive gaps of \(T_k\); odd gaps consist of the \((A_k-1)/2\) positive odds below \(A_k\) plus \(A_k+2t\) for positive gaps \(t\) of \(T_k\). This yields the displayed Frobenius/genus formulas and parity. No finite table is used to infer the all-\(k\) theorem.

## originality

PASS

Benfield--Lippard explicitly state the oddness assertion as Conjecture 10.4 and provide only finite data through \(k=9\). The relevant earlier SCOPE record identifies stable exceptions with gaps of \(\langle n^k-1\rangle\) while addressing a different modular theorem; a second record computes only the special \(k=10\) semigroup. None of the checked sources states the two-adic semigroup decomposition or the general Frobenius/genus transfer formulas.

## value

PASS

This settles an explicit published all-exponent conjecture and does so through a reusable structural decomposition that additionally transfers Frobenius number and genus. It is an infinite theorem explaining a finite observed pattern, not a table extrapolation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
