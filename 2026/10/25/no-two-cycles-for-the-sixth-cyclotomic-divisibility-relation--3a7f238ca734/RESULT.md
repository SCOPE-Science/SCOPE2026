# No two-cycles for the sixth cyclotomic divisibility relation

## Finding
Let \(\Phi_6(T)=T^2-T+1\). For **every** pair of positive integers \(x,y\), the simultaneous divisibilities
\[
x\mid\Phi_6(y),\qquad y\mid\Phi_6(x)
\]
hold if and only if \(x=y=1\). Thus the directed relation \(u\to v\) defined on integers greater than one by \(u\mid\Phi_6(v)\) has **no directed two-cycle** (and no loop).

As an application, define for positive integers \(n\)
\[
\mathcal H(n)=\sum_{j=1}^{n}\frac1{\gcd(n,j)}.
\]
For all distinct primes \(p,q\), the value \(\mathcal H(pq)\) is **not** an integer. More generally, when \(n>1\) is squarefree and \(\mathcal H(n)\) is integral, every connected component of a directed prime-dependency functional graph selected by choosing, for each \(p\mid n\), a distinct prime \(q\mid n\) with \(p\mid\Phi_6(q)\), has a directed cycle of length at least three.

## Assumptions and scope
All divisibilities are in the positive integers; no primality or coprimality hypothesis is needed for the first assertion. For the applications, \(p,q\) are **distinct primes** and \(n>1\) is **squarefree**. The orientation of each directed edge is \(p\to q\) when \(p\mid\Phi_6(q)\). The graph has one outgoing edge at each prime vertex, and is not claimed to have a unique global directed cycle. Nothing is asserted for nonsquarefree \(n\) or for cycles of length three or more.

## Proof
**Mutual-divisibility descent.** Put \(F(t)=t^2-t+1\). The pair \((1,1)\) clearly satisfies both divisibilities. Conversely, if \(x=1\), then \(y\mid F(1)=1\), so \(y=1\), and symmetrically for \(y=1\). If \(x=y>1\), then \(F(x)\equiv1\pmod x\), contradicting \(x\mid F(x)\).

Suppose a solution with both entries at least two exists. By symmetry, take \(2\le x<y\), and choose among all such solutions one having **smallest smaller entry** \(x\). Since \(y\mid F(x)\), write
\[
z=\frac{F(x)}{y}\in\mathbb Z_{>0}.
\]
As \(F(x)<x^2\) for \(x>1\) and \(y>x\), we have \(1\le z<x\). Reducing \(yz=F(x)\) modulo \(x\) yields
\[
yz\equiv1\pmod x.
\]
In particular \(y\) and \(z\) are units modulo \(x\), and \(z\equiv y^{-1}\pmod x\). The polynomial has the reciprocal identity
\[
t^2F(t^{-1})=F(t)
\]
for units \(t\) in any commutative ring. Therefore
\[
y^2F(z)\equiv y^2F(y^{-1})=F(y)\equiv0\pmod x.
\]
Since \(y\) is invertible modulo \(x\), this implies \(x\mid F(z)\). Also \(z\mid F(x)\), because \(F(x)=yz\). Hence \((z,x)\) satisfies the same reciprocal divisibilities, with \(z<x\). If \(z=1\), then \(x\mid F(1)=1\), impossible; otherwise \((z,x)\) is a nontrivial solution with smaller smaller entry. Both alternatives contradict the choice of \((x,y)\). Thus no nontrivial solution exists.

**Squarefree application.** Let \(A(n)=n\mathcal H(n)\). Grouping the summands according to their gcd, one has
\[
A(n)=\sum_{d\mid n}d\varphi(d).
\]
This function is multiplicative, and for primes \(p\),
\[
A(p)=1+p(p-1)=F(p).
\]
Consequently, for distinct primes \(p,q\),
\[
\mathcal H(pq)=\frac{F(p)F(q)}{pq}.
\]
Because \(F(p)\equiv1\pmod p\) and \(F(q)\equiv1\pmod q\), integrality would force \(p\mid F(q)\) and \(q\mid F(p)\), contrary to the proved classification.

For any squarefree \(n>1\), \(A(n)=\prod_{p\mid n}F(p)\). If \(n\mid A(n)\), then each \(p\mid n\), unable to divide its own \(F(p)\), divides at least one \(F(q)\) for a **different** prime \(q\mid n\). Select one such \(q\) for each \(p\). The resulting finite functional digraph has directed cycles; loops are excluded by \(F(p)\equiv1\pmod p\) and two-cycles by the mutual-divisibility classification. Hence every component contains a cycle of length at least three.

## Verification
The accompanying `verify.py` independently enumerates all ordered distinct positive integer pairs bounded by \(1000\) and confirms no mutual divisibility, checks the exact multiplicative formula for the example \(n=614341\) by direct gcd summation, and checks an explicit four-cycle of the prime-dependency relation. The universal theorem is proved by descent, not by finite enumeration.

In the example, \(614341=7\cdot13\cdot43\cdot157\), the edges \(7\to157\to13\to43\to7\) occur, and \(\mathcal H(614341)=486361\). This demonstrates that excluding two-cycles does **not** exclude all integer values or longer cycles.

## Relationship to prior work
De Koninck and Letendre, arXiv:2610.10572 (first posted 2026-10-04), introduce this integrality problem and its prime-dependency functional graphs. Their Section 5, Proposition 1 explicitly considers a pair of odd primes satisfying \(a p=\Phi_6(q)\) and \(b q=\Phi_6(p)\), and gives an **upper bound on the number of such pairs**; its stated result does not exclude them. The descent here supplies the exact impossibility of that squarefree two-cycle configuration. Their Theorem 1 bounds the counting function for all integral values, which does not itself yield a zero count for squarefree semiprimes. The relation between \(A(n)\) and the sum of element orders in a cyclic group is recorded as OEIS A057660, while OEIS A317480 lists examples of integral \(\mathcal H(n)\). These background formulas and numerical data are credited, not claimed new.

## Limitations
This result does not rule out two-cycles in divisibility graphs using prime-square local factors, establish whether integral values occur with precisely three distinct prime factors, determine the smallest cycle length actually realized, or improve the general counting-function estimate of the motivating paper. Completeness of literature indexing is not established; a similar descent might have been previously known. Independent validation of originality and proof has not been performed.

## References
- J.-M. De Koninck and P. Letendre, *The Integer Values of the Sum of Reciprocal GCDs*, arXiv:2610.10572 (2026-10-04), https://arxiv.org/html/2610.10572v1 . Section 2 and especially Section 5, Proposition 1.
- OEIS Foundation, A317480, integer values of reciprocal gcd sums, https://oeis.org/A317480 .
- OEIS Foundation, A057660, the sum of orders of elements in a finite cyclic group, https://oeis.org/A057660 .
