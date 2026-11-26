# Independent mathematical audit

## correctness

PASS

In signs, 2A+I implements open-neighbour majority with tie retention, with no zero local field. For its symmetric matrix H, the two-time energy -s(t)^T Hs(t-1) strictly decreases unless s(t+1)=s(t-1); the finite state space yields eventual periods at most two. For n≥3, the two horizontal neighbours are distinct. An indexed closed walk on overlapping column pairs is determined by its column at each labeled position; no quotient by rotations enters the trace. With a pair of time layers the two local equations are exactly F(x)=y and F(y)=x, with y forced by x. An independent signed-column implementation, using a join of allowed local updates and mutual reachability, reproduced the cyclic SCC sizes, confirmed that the ten two-vertex components are loopless directed 2-cycles, and found a loop in each large strongly connected core, proving primitivity. It reproduced the listed trace counts through n=8, and direct checks through n=5. Exact integer characteristic polynomials via SymPy's DomainMatrix computation, not the frozen Newton-trace routine, give nonzero parts of degrees 16 and 72 and confirm the specified irreducible Perron factors. Positive integer vectors give the two rational Collatz–Wielandt brackets. Exact polynomial root counts show exactly one root of the respective specified factor in each bracket and none of the other factors there; the cubic is increasing above 2. The resulting roots are about 2.20556943040059 and 3.45791276275055. For a primitive core its Perron eigenvalue is algebraically simple with a strict spectral gap, so its trace powers have leading coefficient one; the bounded small-component counts do not affect the asymptotics or the vanishing fixed fraction among recurrent configurations.

## originality

PASS

The supported distinct contribution is the exact fixed and two-step census and the algebraic growth comparison for mixed-degree three-row cylinders, especially the 200-state two-step core and its Perron equation. The period-two bound and transfer method are established precedents and not credited. A later exact fixed-state record covers the same Q_n and its cubic but explicitly excludes the two-cycle census; it is recorded as substantive overlap, not earlier priority.

## value

PASS

The natural comparison after a period-two theorem is the relative growth of the two types of recurrence. The first width with a mixed tie rule on this family supplies a specific nontrivial test, and the exact counts distinguish the fixed and recurrent growth rates rather than merely verifying the known bound or enumerating several small sizes. The trace formulas give every labeled size, including a parity correction, and the limiting ratio answers the recurrence question without asserting anything about attraction basins.

The dated certificate retains the supplied scientific assessment, sources and limitations.
