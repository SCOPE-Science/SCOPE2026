# Powers of two in two-cycles of the shifted Euler map
## Finding
For an integer \(k\ge0\), define
\[
F_k(n)=\varphi(n)+k,
\]
where \(\varphi\) is Euler's totient function. A power of two \(2^a\) belongs to a nontrivial exact two-cycle of \(F_k\) if and only if \(a\ge4\). When this happens the parameter and the partner are forced:
\[
k=5\cdot2^{a-3},
\qquad
2^a\longleftrightarrow 9\cdot2^{a-3}.
\]
Thus the first examples are \(16\longleftrightarrow18\) for \(k=10\), \(32\longleftrightarrow36\) for \(k=20\), and \(64\longleftrightarrow72\) for \(k=40\).

Equivalently, for every \(a\ge1\), the complete set of positive-integer solutions of
\[
y+\varphi(y)=3\cdot2^{a-1}
\]
is \(y=2^a\), together with \(y=9\cdot2^{a-3}\) exactly when \(a\ge4\).

## Assumptions and scope
The state space is the positive integers and \(k\) is a nonnegative integer. "Exact two-cycle" means two distinct positive integers \(x,y\) with \(F_k(x)=y\) and \(F_k(y)=x\). The theorem classifies exact two-cycles containing a power of two; it does not classify all periodic orbits of \(F_k\).

## Proof
Assume first that \(2^a\) and \(y\ne2^a\) form a two-cycle. Since
\[
\varphi(2^a)=2^{a-1},
\]
the two cycle equations are
\[
y=2^{a-1}+k,
\qquad
2^a=\varphi(y)+k.
\]
Eliminating \(k\) gives
\[
y+\varphi(y)=3\cdot2^{a-1}. \tag{1}
\]
Conversely, any positive solution \(y\) of (1) gives \(k=y-2^{a-1}\), and the two displayed cycle equations then hold. It therefore suffices to solve (1).

There is no odd solution. For \(a\ge2\), the right side of (1) is even, whereas \(y+\varphi(y)\) is odd for odd \(y>1\); \(y=1\) gives \(2\). For \(a=1\), any odd \(y\ge3\) gives \(y+\varphi(y)\ge5>3\).

Hence write
\[
y=2^c m,
\qquad c\ge1,
\qquad m\ \text{odd}.
\]
Multiplicativity of the totient gives
\[
2m+\varphi(m)=3\cdot2^{a-c}. \tag{2}
\]
If \(m=1\), then (2) forces \(a-c=0\), so \(y=2^a\).

Now suppose \(m>1\). If \(\nu_2(\varphi(m))\ge2\), then \(2m\equiv2\pmod4\), so the left side of (2) has exact \(2\)-adic valuation \(1\). Thus \(a-c=1\), but then (2) would have right side \(6\), while its left side is at least \(2\cdot3+\varphi(3)=8\), a contradiction. Therefore
\[
\nu_2(\varphi(m))=1.
\]
For odd
\[
m=\prod_i p_i^{e_i},
\]
one has
\[
\nu_2(\varphi(m))=\sum_i \nu_2(p_i-1).
\]
Every summand is at least \(1\), so there is exactly one distinct odd prime divisor and it is congruent to \(3\pmod4\). Thus \(m=p^e\) for a prime \(p\equiv3\pmod4\). Equation (2) becomes
\[
p^{e-1}(3p-1)=3\cdot2^{a-c}. \tag{3}
\]
The factors \(p\) and \(3p-1\) are coprime, and \(3p-1\not\equiv0\pmod3\). Since the only odd prime factor on the right side of (3) is \(3\), equation (3) forces
\[
p^{e-1}=3.
\]
Hence \(p=3\) and \(e=2\). Then \(3p-1=8\), so \(a-c=3\). Consequently
\[
m=9,
\qquad
c=a-3,
\qquad
y=9\cdot2^{a-3}.
\]
The condition \(c\ge1\) is exactly \(a\ge4\). This proves the stated classification of (1).

For \(a\ge4\), the corresponding parameter is
\[
k=y-2^{a-1}=5\cdot2^{a-3}.
\]
Finally,
\[
F_k(2^a)=2^{a-1}+5\cdot2^{a-3}=9\cdot2^{a-3},
\]
while
\[
\varphi(9\cdot2^{a-3})=3\cdot2^{a-3},
\]
and therefore
\[
F_k(9\cdot2^{a-3})=8\cdot2^{a-3}=2^a.
\]
The two states are distinct, so the period is exactly \(2\).

## Verification
The bundled `verify.py` independently computes Euler totients by a sieve and exhaustively solves
\[
y+\varphi(y)=3\cdot2^{a-1}
\]
for every \(1\le a\le18\). It checks that the only solutions are those in the theorem and directly verifies every predicted two-cycle in this range. Its recorded output is:

`VERIFY_OK a_cases=18 equation_values=786429 cycle_cases=15`

This finite replay is a regression check; the proof above establishes the infinite statement.

## Relationship to prior work
Leonetti and Luca study exactly the map \(n\mapsto\varphi(n)+k\), prove that every orbit is eventually periodic, and discuss the problem of understanding nontrivial cycle size and structure. Their paper does not classify exact two-cycles containing powers of two. A later published finding on the same map proves a general upper bound for the maximum of a period-\(T\) cycle and characterizes equality, but that bound neither implies the existence criterion here nor determines the unique parameter attached to a prescribed state \(2^a\).

Targeted searches for the equivalent Diophantine equation \(y+\varphi(y)=3\cdot2^t\), for shifted-totient two-cycles, and for the concrete first cycle \(16\leftrightarrow18\) did not locate a statement implying this classification. This is evidence of noncoverage, not a proof that no equivalent result exists anywhere.

## Limitations
The theorem concerns only cycles of exact period \(2\) that contain a power of two. It does not classify two-cycles with neither entry a power of two, longer cycles, or the total number of cycles for a fixed \(k\). The literature comparison is necessarily bounded by the sources and searches listed in the accompanying review; specialized work on Diophantine totient equations remains a residual novelty risk.

## References
1. P. Leonetti and F. Luca, "On the iterates of shifted Euler's function," arXiv:2302.01783, first public version 3 February 2023; published as "On the iterates of the shifted Euler's function," *Bulletin of the Australian Mathematical Society* 109 (2024), 206--214, DOI:10.1017/S0004972723000394.
2. Finding `02d25ffc-40ae-4cc1-8b88-9a377c0e984c`, "Sharp period-size bound and extremal structure for shifted Euler cycles."
