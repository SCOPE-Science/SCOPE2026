# Exact Fibonacci rank-map stabilization heights on 7-smooth integers

## Finding
Let \(F_0=0,F_1=1,F_{j+2}=F_{j+1}+F_j\), and define the Fibonacci order-of-appearance map \(z(n)=\min\{j\ge1:n\mid F_j\}\) on positive integers. Write \(z^{\circ0}(n)=n\) and \(h(n)=\min\{t\ge0:z^{\circ t}(n)=z^{\circ(t+1)}(n)\}\). For integers \(a,b,c,d\ge0\), put \(n=2^a3^b5^c7^d\), and \(q(a)=\max\{0,\lceil(a-2)/2\rceil\}\).

The exact stabilization height is
\[
h(n)=\begin{cases}
\max\{d+1,b-1,q(a)\},&d\ge2,\\
3,&d=1,\ a=0,\ b\le1,\\
\max\{2,b-1,q(a)\},&d=1\text{ and }(a\ge1\text{ or }b\ge2),\\
\eta(a,b),&d=0,\ a\le3,\ b\le1,\\
\max\{0,b-1,q(a)\},&d=0\text{ and }(a\ge4\text{ or }b\ge2),
\end{cases}
\]
where \(\eta(0,0)=0\), \(\eta(0,1)=3\), \(\eta(1,0)=4\), \(\eta(1,1)=1\), \(\eta(2,0)=2\), \(\eta(2,1)=0\), \(\eta(3,0)=2\), and \(\eta(3,1)=1\).

The eventual fixed point is \(5^c\) when \(a=b=d=0\), and \(12\cdot5^c\) otherwise. For each integer \(t\ge5\), the **least positive 7-smooth integer** with height exactly \(t\) is, uniquely,
\[3^{t+1}.\]
Here 7-smooth means that every prime divisor is at most \(7\).

## Assumptions and scope
The domain comprises **all** positive integers of the form \(2^a3^b5^c7^d\), with all four exponents nonnegative; the definitions include \(n=1\). The height is the number of actual applications of \(z\) *before* arriving at a fixed point, rather than a period or the number of distinct values in an orbit. Exponents of \(5\) have no effect on height, but do determine which fixed point is reached. The least-number assertion is only among 7-smooth positive integers and only for \(t\ge5\).

## Proof
**Prime-power ranks.** The rank-of-apparition divisibility and lifting identities give \(z(\operatorname{lcm}(u,v))=\operatorname{lcm}(z(u),z(v))\), with
\[
 z(2)=3,\quad z(4)=6,\quad z(2^a)=3\cdot2^{a-2}\ (a\ge3),\quad
 z(3^b)=4\cdot3^{b-1}\ (b\ge1),
\]
\[
 z(5^c)=5^c\ (c\ge0),\qquad z(7^d)=8\cdot7^{d-1}\ (d\ge1).
\]
For the final formula use \(z(7)=8\) and \(\nu_7(F_8)=\nu_7(21)=1\), followed by standard odd-prime rank lifting. The special two-adic ranks follow from the standard Fibonacci two-adic valuations. The rank of \(1\) is \(1\).

**Exponent transition.** If \((a,b,c,d)\) are the exponents of an input, the exponents \((A,B,c,D)\) of its image are the following exactly specified function. Initialize \(A=B=0\). For \(a=1\), set \(B=1\); for \(a=2\), set \((A,B)=(1,1)\); for \(a\ge3\), set \((A,B)=(a-2,1)\). If \(b\ge1\), replace \(A\) by \(\max(A,2)\) and \(B\) by \(\max(B,b-1)\). If \(d\ge1\), replace \(A\) by \(\max(A,3)\). Finally set \(D=\max(d-1,0)\). This is exactly the least-common-multiple of the preceding prime-power rank formulas, not merely a bound.

The transition fixes only \((0,0,c,0)\) and \((2,1,c,0)\): if \(d>0\), the last coordinate decreases; if \(d=0\), direct analysis of the first two coordinates gives the indicated two possibilities. The exponent of \(5\) never changes.

**Iteration with at least two factors of \(7\).** For \(d\ge2\), direct substitution for the second iterate and induction for every integer \(j\ge2\) yield
\[
 (a_j,b_j,d_j)=\bigl(\max\{2,a-2j,3\mathbf1_{j\le d}\},\ \max\{1,b-j\},\ \max\{0,d-j\}\bigr).
\]
Here \(\mathbf1_P\) equals one when \(P\) holds and zero otherwise. For \(j\ge2\), the iterated state can be fixed only at \((2,1,0)\). The three exact conditions for this are \(j\ge d+1\), \(j\ge b-1\), and \(j\ge\lceil(a-2)/2\rceil\). Their maximum gives the first case of the theorem, with no earlier fixed iterate.

**Exactly one factor of \(7\).** If \(d=1,a=0,b\le1\), the first-coordinate trajectories are \((0,b,1)\to(3,0,0)\to(1,1,0)\to(2,1,0)\), which has height three. In every other case with \(d=1\), the first iterate has \(a_1\ge3\), \(b_1\ge1\), and \(d_1=0\). A second substitution followed by induction yields, for every \(j\ge2\),
\[
(a_j,b_j,d_j)=(\max\{2,a-2j\},\max\{1,b-j\},0).
\]
It is first fixed at the earliest \(j\ge2\) satisfying \(j\ge b-1\) and \(j\ge\lceil(a-2)/2\rceil\), proving the second and third cases.

**No factor of \(7\).** For \(d=0,a\le3,b\le1\), evaluating the transition directly on the eight possible exponent pairs gives the table \(\eta\) in the statement. Otherwise (\(a\ge4\) or \(b\ge2\)), after the first transition one has \(a_1\ge2,b_1\ge1\), and for all \(j\ge1\),
\[
(a_j,b_j)=(\max\{2,a-2j\},\max\{1,b-j\}).
\]
The first fixed iterate occurs exactly at \(\max\{0,b-1,q(a)\}\), including the possibility \(j=1\). If \((a,b,d)=(0,0,0)\), the initial value \(5^c\) is itself fixed, as covered by the table.

**Least input of prescribed large height.** For \(t\ge5\), all exceptional cases have smaller height. Every 7-smooth integer of height \(t\) must therefore satisfy at least one of \(b\ge t+1\), \(a\ge2t+1\), or \(d\ge t-1\). Hence the input is at least one of \(3^{t+1}\), \(2^{2t+1}\), or \(7^{t-1}\). For \(t\ge5\), both of the last two exceed \(3^{t+1}\), strictly. The input \(3^{t+1}\) has height \(t\) by the preceding formula. Equality forces the unique input \(3^{t+1}\), proving the assertion.

## Verification
The accompanying `verify.py` reproduces three independent finite checks. First, for every 7-smooth \(n\le5000\), it iterates Fibonacci residues modulo \(n\) directly until the first zero and checks the rank from the exponent transition (265 integers). Second, it checks the closed height formula and final fixed-point exponents by repeated application of the exponent transition for \(0\le a,b<64\), \(0\le d<20\), and \(c\in\{0,3\}\) (163,840 states). Third, it independently enumerates all 7-smooth inputs up to \(3^{t+1}\) for \(t=5,6,7,8\) to check the minimum and uniqueness in those finite cases. Execute `python3 verify.py` using the Python standard library only. Finite verification is evidence for implementation and small boundary cases; the proof above establishes the universal assertion.

## Relationship to prior work
Luca and Tron (2014), particularly their Lemmas 1.3–1.4 and Theorem 2.2, provide rank and lifting facts and establish eventual stabilization but do not determine this 7-smooth height function. FitzGibbons, Miller, and Verga (2023), particularly Lemmas 2.1–2.4 and 4.1–4.2, prove fixed-point and iterate facts, including exact heights of sufficiently large powers of \(2\); those power-of-two heights are included here as **known special cases**, not claimed as new. The contribution assessed here is the complete four-parameter height formula, its two exceptional boundary layers, and the sharp minimum restricted to 7-smooth inputs. Earlier results for powers of \(10\), powers of \(2\), and general convergence are acknowledged, not reasserted as original.

## Limitations
No assertion is made about arbitrary integers having prime factors above \(7\), the globally least integer of a given height, or a general formula for the height of every positive integer. Exact mathematical equivalence to an unlocated specialization in the broader literature cannot be ruled out solely by searches. The finite verifier cannot independently certify the proof for infinitely many exponent tuples.

## References
1. Florian Luca and Emanuele Tron, *The Distribution of Self-Fibonacci Divisors*, arXiv:1410.2489v1, first posted 2014-10-09; https://arxiv.org/abs/1410.2489 .
2. Molly FitzGibbons, Steven J. Miller, and Amanda Verga, *Dynamics of the Fibonacci Order of Appearance Map*, arXiv:2309.14501v1, first posted 2023-09-25; https://arxiv.org/abs/2309.14501 .
3. Earlier fixed-point classification by Diego Marques (2012), as discussed and referenced in item 2.
