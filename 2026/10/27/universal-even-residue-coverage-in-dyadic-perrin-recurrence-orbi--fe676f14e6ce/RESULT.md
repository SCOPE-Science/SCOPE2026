# Universal even-residue coverage in dyadic Perrin recurrence orbits

## Finding

For every integer \(k\ge1\), write \(M=2^k\). Given any triple \((u_0,u_1,u_2)\in(\mathbb Z/M\mathbb Z)^3\) with at least one odd coordinate, extend it by
\[
u_{n+3}=u_{n+1}+u_n\pmod M\qquad(n\ge0).
\]
There exists an index \(r\in\{0,1,\ldots,6\}\), determined *only* by the parity triple, such that
\[
\{u_{r+7t}:0\le t<2^{k-1}\}
=\{0,2,4,\ldots,M-2\}\pmod M,
\]
with **every even residue appearing exactly once** on the left. The chosen \(r\) is uniquely specified by three explicit parity tests in the proof.

More generally, for any nonzero initial triple divisible coordinatewise by exactly \(2^s\), with \(0\le s<k\), some arithmetic progression of \(2^{k-s-1}\) terms contains every residue divisible by \(2^{s+1}\) modulo \(2^k\) exactly once. Consequently **every orbit of the Perrin/Padovan recurrence modulo any power of two visits zero**, and no zero-avoiding orbit exists.

## Assumptions and scope

All triples are ordered, and all statements concern the recurrence with characteristic polynomial \(X^3-X-1\), *not* the three-step Tribonacci recurrence. An initial triple is called primitive modulo \(2^k\) if at least one coordinate is odd. The zero triple is periodic and contains zero trivially. For a nonzero triple, the common valuation \(s\) means the largest common power of two dividing its three integer representatives, capped below \(k\); the normalized triple modulo \(2^{k-s}\) is primitive.

Let \(A\) be the integral companion matrix
\[
A=\begin{pmatrix}0&1&0\\0&0&1\\1&1&0\end{pmatrix},
\quad
B=\frac{A^7-I}{2},\quad C=\frac{A^{14}-I}{4}.
\]
All displayed divisions are exact integer-matrix divisions. For a primitive parity column \(\bar v\in\mathbb F_2^3\), define \(r\in\{0,\ldots,6\}\) by
\[
\bigl(e_1^{\mathsf T}A^r\bar v,\ e_1^{\mathsf T}A^r B\bar v,\ e_1^{\mathsf T}A^r C\bar v\bigr)=(0,1,1)\quad\text{in }\mathbb F_2^3.
\]
The proof shows precisely one \(r\) exists. The main claim uses that \(r\), independent of \(k\) and all higher input bits.

## Proof

**1. Exact matrices and finite-field transitivity.** Direct integer multiplication gives
\[
A^7=\begin{pmatrix}1&2&2\\2&3&2\\2&4&3\end{pmatrix},\quad
B=\begin{pmatrix}0&1&1\\1&1&1\\1&2&1\end{pmatrix},\quad
C=\begin{pmatrix}2&4&3\\3&5&4\\4&7&5\end{pmatrix}.
\]
The characteristic polynomial of \(A\bmod2\) is \(X^3+X+1\), irreducible over \(\mathbb F_2\). As \(A^7\equiv I\pmod2\), its order is seven. Hence both the seven columns \(A^j e_1\) and the seven rows \(e_1^{\mathsf T}A^j\) run through all nonzero vectors of \(\mathbb F_2^3\).

For \(v=e_1\), the three columns \(v,Bv,Cv\) form the matrix
\[
\begin{pmatrix}1&0&0\\0&1&1\\0&1&0\end{pmatrix}\pmod2,
\]
whose determinant is one in \(\mathbb F_2\). Both \(B\) and \(C\) commute with \(A\), being integer polynomials in \(A\). Every nonzero \(v\bmod2\) is \(A^j e_1\) for some \(j\), so the determinant of the column matrix \([v,Bv,Cv]\) is also one modulo two. Accordingly, for every primitive parity triple the three linear tests defining \(r\) select exactly one nonzero row. Since the rows \(e_1^{\mathsf T}A^r\) exhaust all seven nonzero rows, precisely one \(r\in\{0,\ldots,6\}\) satisfies the tests.

**2. Dyadic lifting.** Put \(H=A^7=I+2B\). As \(H^2=A^{14}=I+4C\), repeated squaring yields, for every integer \(j\ge1\),
\[
H^{2^j}\equiv I+2^{j+1}C\pmod{2^{j+2}}.
\]
Indeed it holds for \(j=1\); squaring the displayed congruence increments the valuation by one, with the quadratic correction divisible by the required higher power. At \(j=0\), the corresponding exact relation is \(H=I+2B\).

Fix any primitive integer lift \(v\) and the unique \(r\) above; write
\[
f(t)=e_1^{\mathsf T}A^rH^tv\qquad(t\ge0).
\]
The defining parity tests ensure \(f(t)\equiv0\pmod2\) for all \(t\). For arbitrary \(t\ge0\), since \(H^t\equiv I\pmod2\), the matrix relations give
\[
f(t+1)-f(t)\equiv2\pmod4,
\]
and, for each \(j\ge1\),
\[
f(t+2^j)-f(t)\equiv2^{j+1}\pmod{2^{j+2}}.
\]
The first congruence uses the middle parity test (the \(B\)-column), and every later one uses the last parity test (the \(C\)-column). Each bit added to the index \(t\) therefore toggles exactly the next higher bit of the even residue \(f(t)\), without changing its lower bits.

Inductively, \(f(0),\ldots,f(2^\ell-1)\) run through the \(2^\ell\) even residue classes modulo \(2^{\ell+1}\) exactly once: the assertion is immediate for \(\ell=0\), and the paired indices \(t\) and \(t+2^\ell\) share a residue modulo \(2^{\ell+1}\) but differ by \(2^{\ell+1}\) modulo \(2^{\ell+2}\). Take \(\ell=k-1\) to obtain the asserted bijection modulo \(2^k\).

**3. General triples.** If the initial state is \(2^s v\pmod{2^k}\), with \(v\) primitive modulo \(2^{k-s}\), apply the result at precision \(k-s\), then multiply each term by \(2^s\). The selected subsequence hits every multiple of \(2^{s+1}\) exactly once modulo \(2^k\), including zero. The zero state already contains zero. This proves the theorem and its zero-avoidance corollary.

## Verification

The accompanying standalone \(\texttt{verify.py}\) uses integer arithmetic and the Python standard library only. It independently verifies the exact \(A^7,A^{14}\) matrices, all seven parity classes and the invertibility of their three-column tests, the dyadic matrix-lift congruences through ten levels, and the actual even-residue permutation for all primitive triples modulo \(2,4,8,16\) and 103 predetermined primitive triples modulo \(32\). The checks returned \(\texttt{VERIFY_OK}\). The finite tests support, but do not replace, the general proof above.

## Relationship to prior work

Brent's *On the Periods of Generalized Fibonacci Recurrences* (1994; public arXiv posting 2010) proves, in Theorem 3 and Lemma 2, that every primitive sequence associated with an appropriate primitive trinomial has the full period \(2^{k-1}(2^3-1)\). That **already covers the maximal-period fact** and therefore also the easy orbit-length and orbit-count census; neither is claimed as new here. The present theorem concerns a different property: one prescribed modulo-seven subsequence visits *all even residue values exactly once*, a statement not implied by the period alone. Its proof needs two separate initial 2-adic increment tests and a finite-field basis argument.

Sedaghat's *Zero-Avoiding Solutions of the Fibonacci Recurrence Modulo a Prime* (2014) motivates the structural zero-avoidance question for second-order recurrences over fields; it does not treat Perrin triples over prime-power rings. The OEIS entry A104217 (2005) records periods for a particular Perrin sequence, not the all-initial-state value-distribution theorem. Klaška's 2008 paper concerns the different Tribonacci polynomial. The 2024 work of Bravo and Irmak studies 2-adic valuations of particular Padovan and Perrin sequences, not the uniform arbitrary-initial-state permutation assertion. These comparisons are not claims of comprehensive coverage of every unpublished source.

## Limitations

The theorem is specific to the recurrence \(u_{n+3}=u_{n+1}+u_n\) and moduli that are powers of two. It says neither that every index subsequence has uniform distribution nor that odd residues appear at any fixed frequency, and it gives no classification for odd prime powers. The unique index \(r\) refers to the stated three parity tests, not necessarily to every possible choice of an even-residue-complete subsequence. An equivalent result in unlocated recurrence-distribution literature remains possible. No independent mathematical audit has occurred.

## References

1. Richard P. Brent, *On the Periods of Generalized Fibonacci Recurrences*, Mathematics of Computation **63** (1994), 389–401; public preprint https://arxiv.org/abs/1004.5439 (2010). See Lemma 2 and Theorem 3.
2. H. Sedaghat, *Zero-Avoiding Solutions of the Fibonacci Recurrence Modulo a Prime*, Fibonacci Quarterly **52** (2014), 39–45; https://www.fq.math.ca/Papers1/52-1/Sedaghat.pdf.
3. OEIS Foundation, A104217, *Period of Perrin sequence mod n*, initial entry March 14, 2005; https://oeis.org/A104217.
4. Jiří Klaška, *Tribonacci modulo p^t*, Mathematica Bohemica **133** (2008), 267–288; https://www.dml.cz/handle/10338.dmlcz/140617.
5. Eric Bravo and Nurettin Irmak, *The 2-adic valuation of shifted Padovan and Perrin numbers and applications*, Turkish Journal of Mathematics **48** (2024), 1183–1196; https://doi.org/10.55730/1300-0098.3568.
