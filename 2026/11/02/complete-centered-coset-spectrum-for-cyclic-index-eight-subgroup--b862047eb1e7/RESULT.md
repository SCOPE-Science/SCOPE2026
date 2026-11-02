# Complete centered-coset spectrum for cyclic index-eight subgroups modulo semiprimes

## Finding
Let \(m=pq\) with distinct odd primes \(p,q\). For a cyclic subgroup \(H\le(\mathbb Z/m\mathbb Z)^\times\) of even order, index eight, and \(-1\notin H\), call a coset \(C\) *centered* if
\[
 S(C):=\sum_{x\in C}\langle x\rangle_m=\frac{m|H|}{2},
\]
where \(\langle x\rangle_m\in\{1,\ldots,m-1\}\) is the least positive representative. Let \(N(H)\) count centered cosets among the eight cosets of \(H\).

**Theorem (sharp spectrum and positive-density realization).** Among all such \(m,H\), the possible values of \(N(H)\) are exactly
\[
\boxed{\{0,2,4,6,8\}.}
\]
Every value occurs for infinitely many semiprime moduli, even with the first prime fixed at \(41\). More precisely, take \(g=6\pmod {41}\), \(K=\langle g^8\rangle=\{1,10,16,18,37\}\), and for every odd prime \(q\ne41\) satisfying \(q\not\equiv1\pmod5\), put
\[
 H_q=\{x\in(\mathbb Z/41q\mathbb Z)^\times:x\bmod41\in K\}.
\]
There is a unique \(h\in\{0,\ldots,7\}\) with \(q\bmod41\in g^hK\), and
\[
\boxed{N(H_q)=8-2\min(h,8-h).}
\]
Among the admissible primes \(q\), the limiting proportions with \(N(H_q)=0,2,4,6,8\), in that order, are \(1/8,1/4,1/4,1/4,1/8\). Unconditionally, among all primes, their densities are \(3/32,3/16,3/16,3/16,3/32\), respectively. The omitted primes \(q\equiv1\pmod5\) form density \(1/4\) and do not belong to this cyclic construction.

## Assumptions and scope
Every claim concerns *multiplicative* cosets of a cyclic subgroup of the unit group modulo the product of **two distinct odd primes**. The universal spectrum is asserted only for even-order, index-eight subgroups with \(-1\notin H\), and the density assertion concerns the explicitly defined conductor-\(41\) family. The condition \(q\not\equiv1\pmod5\) is necessary and sufficient for cyclicity of this particular direct-product subgroup. Density statements are natural densities in the sequence of primes, established using Dirichlet's theorem and the prime number theorem in arithmetic progressions. Finite exceptional primes do not affect the densities.

## Proof
**1. Universal restriction.** If \(-1\notin H\), the eight cosets split into four disjoint pairs \((C,-C)\). For each element \(x\in C\), the two least positive residues \(\langle x\rangle_m\) and \(\langle-x\rangle_m\) sum to \(m\). Consequently
\[
 S(-C)=m|H|-S(C).
\]
Thus \(C\) is centered if and only if \(-C\) is centered, and \(N(H)\in\{0,2,4,6,8\}\).

**2. Cyclicity of the conductor-\(41\) family.** Direct modular exponentiation gives \(6^{20}\equiv-1\pmod{41}\), \(6^8\equiv10\pmod{41}\), and \(6^{40}\equiv1\pmod{41}\). Since the prime factors of \(40\) are \(2\) and \(5\), these congruences prove that \(g=6\) has order \(40\). Hence \(K=\langle g^8\rangle\) has order \(5\) and index \(8\). By the Chinese remainder theorem,
\[
 H_q\simeq K\times\mathbb F_q^\times\simeq C_5\times C_{q-1}.
\]
This group is cyclic exactly when \(\gcd(5,q-1)=1\). It has even order \(5(q-1)\), index \(8\), and omits \(-1\) because the order-two element \(-1\pmod{41}\) is not in the odd-order group \(K\).

**3. Exact local coset sums.** For \(j\in\{0,\ldots,7\}\) set \(C_j=g^jK\) modulo \(41\) and \(R_j=\sum_{x\in C_j}\langle x\rangle_{41}\). Exhaustive direct five-element multiplication in the order \(j=0,\ldots,7\) gives
\[
 (R_0,\ldots,R_7)=(82,82,123,123,123,123,82,82)
 =41(2,2,3,3,3,3,2,2).
\]
For reproducibility the eight sorted cosets are
\[
\begin{array}{c|l|r}
 j&\text{least positive residues}&R_j\\\hline
0&1,10,16,18,37&82\\
1&6,14,17,19,26&82\\
2&2,20,32,33,36&123\\
3&11,12,28,34,38&123\\
4&4,23,25,31,40&123\\
5&15,22,24,27,35&123\\
6&5,8,9,21,39&82\\
7&3,7,13,29,30&82
\end{array}
\]
Each modular coset has five elements, so the displayed table also verifies their cardinalities and partition of \(\mathbb F_{41}^\times\).

**4. Lifted centered deviations.** Fix an admissible \(q\) and choose \(h\) with \(q\in g^hK\pmod{41}\). The eight cosets of \(H_q\) consist of units \(x\bmod41q\) with \(x\bmod41\in C_j\) for \(j=0,\ldots,7\). For any local representative \(r\in C_j\), the \(q\) integers
\(r,r+41,\ldots,r+41(q-1)\) have sum \(qr+41q(q-1)/2\). Exactly one is a multiple of \(q\), namely \(q\langle q^{-1}r\rangle_{41}\). Removing these five multiples over \(r\in C_j\) leaves precisely the units in the lifted coset. Since \(q^{-1}C_j=C_{j-h}\), its sum is
\[
 S_j=qR_j+\frac{41\cdot 5q(q-1)}2-qR_{j-h}.
\]
The middle term is the centered target \(41q\cdot 5(q-1)/2\). Therefore
\[
 \boxed{S_j-\frac{41q\cdot5(q-1)}2=q(R_j-R_{j-h}).}
\]
This lifting identity is a special case of Lemma 5.4 in Ma--Merca--Zhang (2026); the novelty claimed here is the complete index-eight spectrum and its infinite, explicitly dense realizations, not that identity.

**5. Count all eight centered cosets.** Define \(t_j=R_j/41\) so \((t_j)=(2,2,3,3,3,3,2,2)\). The coset with index \(j\) is centered exactly when \(t_j=t_{j-h}\). Directly comparing the two four-element blocks of equal values under all eight cyclic shifts gives
\[
\begin{array}{c|rrrrrrrr}
h&0&1&2&3&4&5&6&7\\\hline
\#\{j:t_j=t_{j-h}\}&8&6&4&2&0&2&4&6.
\end{array}
\]
This proves the sawtooth formula and, together with Step 1, establishes the claimed global spectrum. Concrete witness primes for \(N=0,2,4,6,8\) are respectively \(q=23,53,5,3,37\).

**6. Infinite realization and exact densities.** For any fixed \(h\), the condition \(q\bmod41\in C_h\) comprises five nonzero residue classes modulo \(41\). For primes \(q\ne5\), the cyclicity condition restricts \(q\bmod5\) to \(2,3,4\), comprising three coprime classes modulo \(5\). The exceptional eligible prime \(q=5\) does not affect limiting densities. By CRT these give exactly \(15\) reduced classes modulo \(205\), out of \(\varphi(205)=160\). Each has infinitely many primes by Dirichlet and asymptotic density \(1/160\) among primes by the prime number theorem in arithmetic progressions. Hence each \(h\) has density \(15/160=3/32\) among all primes, and admissibility has total density \(8(3/32)=3/4\). Grouping the eight values of \(h\) by \(N\) gives the two density vectors in the statement. \(\square\)

## Verification
A standalone standard-library Python program `verify.py` independently enumerates the full lifted coset sets for every admissible odd prime \(q<400\) other than \(41\). It verifies cyclicity by constructing an explicit generator, all eight exact residue sums, the centered criterion, the sawtooth count, and the five prescribed witnesses. It checks \(60\) primes and \(480\) coset sums, as well as the exact 15-of-160 reduced-residue-class counts for each of the eight shifts. The program also checks the eight local cosets as a partition and their exact integer sums. These finite checks confirm the algebra for small moduli; infinitude and density rest on the mathematical arguments above, not on enumeration.

## Relationship to prior work
Ma, Merca and Zhang (2026, arXiv:2610.29608v1) establish the general lifting identity (their Lemma 5.4), classify imprimitive index-four kernels in their Theorem 5.5, construct an index-six family, and tabulate index-eight subgroups in a finite census. The present statement combines an independently verified local octic conductor \(41\) with that lifting mechanism to establish an all-five-value **global index-eight centered-coset spectrum**, a uniform formula for its natural infinite family, and explicit prime densities. Their finite index-eight table does not itself imply the all-five-value infinite result.

Pomerance and Ulmer (2012, arXiv:1204.6705) study the stronger condition that all cosets are balanced in half-interval cardinality, equivalent to all cosets having centered first moments for odd moduli. This does not classify the number of individually centered cosets in an index-eight family. Earlier digit-distribution work of Girstmair is a continuing priority risk, especially if general character machinery implicitly specializes to this family.

## Limitations
The universal claim classifies only *possible counts*, not every index-eight subgroup individually. The explicit sawtooth formula applies to the conductor-\(41\) family; general index-eight subgroups with primitive annihilator are not classified here. Both the local lift identity and character method have published precedents. The new arithmetic content is the complete spectrum with an explicit infinite family and densities. Literature searches and the primary texts examined do not establish historical uniqueness; implicit older coverage is possible. No independent mathematical audit has been performed.

## References
1. H. Ma, M. Merca, W. Zhang, *Residue Sums Modulo Products of Two Distinct Odd Primes*, arXiv:2610.29608v1, first posted 2026-10-21, https://arxiv.org/html/2610.29608v1. Especially Lemma 5.4, Theorem 5.5, Section 6 and Section 7.
2. C. Pomerance and D. Ulmer, *On balanced subgroups of the multiplicative group*, arXiv:1204.6705 (2012), https://arxiv.org/abs/1204.6705.
3. K. Girstmair, *Digit frequencies and class numbers*, arXiv:2606.04512v1, https://arxiv.org/abs/2606.04512.
4. K. Girstmair, *Power residues, digit expansions, and relative class numbers*, Surveys in Mathematics and its Applications 21 (2026), 157--176.
