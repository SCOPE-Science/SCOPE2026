# Independent mathematical audit

## correctness

PASS

For the rational normal curve \(C_d\subset\mathbb P^d\), the standard determinantal/Hilbert-series description of the secant swept by \(k+1\) points gives \(D_{d,k}=\binom{d-k}{k+1}\) throughout the proper range \(0\le k\le\lfloor(d-2)/2\rfloor\). Legendre's digit-sum formula gives \(\nu_p(D_{d,k})=(s_p(k+1)+s_p(d-2k-1)-s_p(d-k))/(p-1)\), equivalently the number of base-\(p\) carries in \((k+1)+(d-2k-1)\). For parity put \(x=d+1\) and \(a=k+1\). Lucas' criterion says \(\binom{x-a}{a}\) is odd exactly when every one-bit of \(a\) survives in \(x-a\). If \(d+2\) is a power of two, \(x\) is an all-ones binary word and subtraction makes \(x-a\) the bitwise complement of \(a\), so every proper degree is even. Otherwise, with \(t=\nu_2(d+2)\), the first admissible \(a\) producing no conflicting one-bit is \(a=2^t\), hence the first odd stage is \(k=2^t-1\); all smaller \(a\) fail by the trailing-one complement argument.

## originality

PASS

The primary algebraic-geometry sources determine the secant degrees and Hilbert series, but the inspected full texts do not state the two-adic all-even classification or the exact first odd secant index. Searches for parity, two-adic valuation, and valuation in the most directly relevant rational-normal-secant thesis found no such theorem, and Resultary returned only the assigned record as the exact binary-phase hit.

## value

PASS

This is a complete parity/valuation classification for a canonical geometric degree tower, including the exact first odd stage. It is a short consequence of classical ingredients, but the quantified phase boundary is a natural complete invariant rather than an arbitrary parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
