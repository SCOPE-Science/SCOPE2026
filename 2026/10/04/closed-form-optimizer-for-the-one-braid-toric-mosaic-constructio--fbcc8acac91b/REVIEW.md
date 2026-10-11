# Independent mathematical audit

## correctness

PASS

The source one-braid construction minimizes \(N=q-h-v\) over nonnegative integers satisfying its four linear inequalities, so equivalently it maximizes \(s=h+v\). Feasibility forces \(q\ge3p-4\), attained at the boundary. In the low range \(3p-4\le q\le4p-4\), the second inequality bounds \(s\le q-3p+4\), and the displayed witnesses attain it, giving \(N=3p-4\). For \(q\ge4p-3\), adding the two oblique inequalities yields the half-sum bound on \(s\); integer parity gives the ceiling expression. When \(q\equiv2\pmod4\), equality in that half-sum bound would force the incompatible parity condition \(h-v=p\), producing exactly the one-unit penalty stated in the theorem; the supplied residue-class witnesses attain all remaining cases. An independent brute-force solution of the integer program for every coprime \(2\le p<25\), \(p<q<100\) found no mismatch with the closed form.

## originality

PASS

The defining toric-mosaic paper states exactly this integer program and says optimal solutions can be computed by an integer-linear-programming routine; it gives a formula only for \(p=2\) and finite/special tables for \(p=3,4\). The complete primary paper does not provide an all-parameter symbolic optimum or the residue-\(2\pmod4\) penalty. Targeted Resultary and web searches on the one-braid inequalities found no later equivalent closed form.

## value

PASS

The result converts a published parametric ILP into an exact all-parameter theorem, identifies the feasibility threshold, and isolates a genuine parity obstruction. That is a natural complete optimization of a named construction and removes repeated integer-program solving; it is not a tiny numerical improvement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
