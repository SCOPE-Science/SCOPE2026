# Ziller's primorial-difference conjecture at \(k=45\)

## Finding
Let
\[
P_k=p_k\#
\]
be the \(k\)-th primorial, and let \(D(k)\) denote the set of values that occur as differences between consecutive positive integers coprime to \(P_k\). Let \(N_{\min}(k)\) be the largest even threshold such that every positive even integer not exceeding it occurs in \(D(k)\), in the notation of Ziller.

For every \(k\ge1\),
\[
D(k)\subseteq D(k+1).
\]
Combining this persistence property with the complete row-\(44\) data proves
\[
N_{\min}(45)\ge616=h(44).
\]
Thus the \(k=45\) case of Ziller's conjecture
\[
h(k-1)\le N_{\min}(k)
\]
is true.

## Assumptions and scope
Ziller defines \(D(k)\) from consecutive integers coprime to \(p_k\#\), identifies the maximal gap with the primorial Jacobsthal value \(h(k)\), reports exhaustive computations through \(k=44\), and conjectures that every positive even integer through \(h(k-1)\) occurs in \(D(k)\) for every \(k>1\).

The finite input used here is the public row-\(44\) summary:
\[
\#D(44)=308,\qquad \max D(44)=h(44)=616.
\]
The first equality is OEIS A329815, the maximum identity is recorded in OEIS A331118, and \(h(44)=616\) is OEIS A048670. OEIS A331118 also records that every value in these rows is a positive even integer.

No claim is made here for \(k\ge46\).

## Proof
First prove persistence. Fix \(k\ge1\), set
\[
P=P_k,\qquad q=p_{k+1},
\]
and suppose \(d\in D(k)\). By the definition of a consecutive gap, there is an integer \(x\) such that
\[
(x,P)=(x+d,P)=1
\]
and
\[
(x+j,P)>1\qquad(1\le j\le d-1).
\]

For
\[
t\in\{0,1,\ldots,q-1\},
\]
put
\[
x_t=x+tP.
\]
Because \(q\nmid P\), the residues \(x_t\bmod q\) run through all residue classes modulo \(q\). Hence at most one value of \(t\) makes \(q\mid x_t\), and at most one value makes \(q\mid x_t+d\). Since \(q\ge3\), there is a value of \(t\) for which neither endpoint is divisible by \(q\).

For this choice of \(t\), periodicity modulo \(P\) gives
\[
(x_t,P)=(x_t+d,P)=1.
\]
Together with the choice modulo \(q\), this yields
\[
(x_t,Pq)=(x_t+d,Pq)=1.
\]
For every \(1\le j\le d-1\),
\[
x_t+j\equiv x+j\pmod P,
\]
so \((x_t+j,P)>1\), and therefore \((x_t+j,Pq)>1\). Thus \(x_t\) and \(x_t+d\) are consecutive integers coprime to \(Pq=P_{k+1}\). Hence
\[
d\in D(k+1),
\]
which proves
\[
D(k)\subseteq D(k+1).
\]

Now apply the public row-\(44\) data. OEIS A329815 gives
\[
\#D(44)=308,
\]
while OEIS A048670 and A331118 give
\[
\max D(44)=h(44)=616.
\]
All elements of \(D(44)\) are positive and even. There are exactly
\[
616/2=308
\]
positive even integers at most \(616\). Therefore the \(308\) distinct elements of \(D(44)\), all even and at most \(616\), must be precisely
\[
\{2,4,6,\ldots,616\}.
\]
By persistence,
\[
\{2,4,6,\ldots,616\}\subseteq D(45),
\]
so
\[
N_{\min}(45)\ge616=h(44).
\]
This is exactly Ziller's conjectured inequality at \(k=45\).

## Verification
The accompanying `verify.py` checks the exact published sequence entries
\[
A329815(44)=308,\qquad A048670(44)=616,\qquad A048670(45)=642,
\]
and confirms that there are exactly \(308\) positive even integers through \(616\).

As a regression check on the symbolic persistence proof, the script constructs complete reduced-residue gap sets for the first six primorial stages and verifies
\[
D(k)\subseteq D(k+1)
\]
for those small cases. The infinite persistence statement is proved symbolically above; the small computation is not used as an infinite proof.

## Relationship to prior work
Ziller's paper reports exhaustive computations only through \(k=44\) and states the inequality
\[
h(k-1)\le N_{\min}(k)
\]
as an empirical conjecture beyond the computed range. The public OEIS row summaries stop the full distinct-gap table at row \(44\).

The persistence of gap values is compatible with the standard wheel recursion in Holt's work on cycles of gaps; it is not claimed here as a new general sieve principle. The new claim is the consequence obtained by combining persistence with the exact row-\(44\) cardinality and maximum: the first case beyond Ziller's reported exhaustive range, \(k=45\), follows without constructing the enormous \(45\)-th primorial residue system.

Brown's 2024 paper gives general counting formulas for fixed gap lengths in primorial unit groups and cites Ziller, but its inspected text does not state the \(k=45\) consequence or the threshold \(616\). Targeted searches for the exact \(k=45\) statement, \(N_{\min}(45)\), and the endpoint \(616\) did not locate a covering publication.

## Limitations
This proves one new case of the conjecture, not the full conjecture. The argument alone gives no information sufficient for the \(k=46\) target \(h(45)=642\), because persistence from row \(44\) guarantees only the values through \(616\).

The originality claim concerns the explicit \(k=45\) consequence. The gap-persistence mechanism itself is a standard feature of primorial-wheel recursions. A non-indexed note or computation could already have recorded the same \(k=45\) observation.

## References
1. Mario Ziller, “On differences between consecutive numbers coprime to primorials,” arXiv:2007.01808v1, first posted 3 July 2020.
2. OEIS A329815, number of distinct first-difference values in the reduced residue system of the \(n\)-th primorial.
3. OEIS A331118, primitive first differences in reduced residue systems of primorials.
4. OEIS A048670, the primorial Jacobsthal function.
5. Fred B. Holt, “Combinatorics of the gaps between primes,” arXiv:1510.00743.
6. Steven Brown, “Distance between consecutive elements of the multiplicative group of integers modulo \(n\),” *Notes on Number Theory and Discrete Mathematics* 30 (2024), 81–99, DOI 10.7546/nntdm.2024.30.1.81-99.
