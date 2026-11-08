# The least cyclic octic conductor: exact residue sums at \(41q\)

## Finding

Let \(q\ne41\) be any odd prime, let \(K=\langle 10\rangle=\{1,10,16,18,37\}\subset\mathbb F_{41}^{\times}\), and let \(H_q\subset (\mathbb Z/41q\mathbb Z)^\times\) be the inverse image of \(K\) under reduction modulo \(41\). For a set \(X\) of units modulo \(m\), let \(S_m(X)\) denote the sum of its least positive integer representatives, and call \(X\) *centered* if \(S_m(X)=m|X|/2\). Here *all-coset centered* means that this equality holds for every multiplicative coset of \(H_q\), not just for \(H_q\) itself.

Write \(C_j=6^jK\subset\mathbb F_{41}^{\times}\), with indices modulo \(8\), and choose \(j\) by \(q\bmod41\in C_j\). Then \(H_q\) has index \(8\), order \(5(q-1)\), and is cyclic precisely when \(q\not\equiv1\pmod5\). Its exact centering defect is
\[
S_{41q}(H_q)-\frac{41q|H_q|}{2}=\begin{cases}
0,&j\in\{0,1,2,7\},\\
-41q,&j\in\{3,4,5,6\}.
\end{cases}
\]
Moreover every coset of \(H_q\) is centered simultaneously exactly when \(j=0\), or equivalently \(q\bmod41\in K\).

Among all rational primes \(q\), the natural densities of **cyclic and centered**, **cyclic and centered but not all-coset centered**, and **cyclic and all-coset centered** are \(3/8\), \(9/32\), and \(3/32\), respectively. The modulus prime \(41\) is the smallest odd prime conductor supporting a cyclic index-eight subgroup containing the entire other-prime CRT unit factor. At modulus \(123\) the subgroup \(H_3\) is centered but not all-coset centered.

For an odd modulus, all-coset centeredness in this *first-moment* sense is equivalent to the all-coset half-interval balance condition studied by Pomerance and Ulmer; the equivalence is also stated explicitly by Ma, Merca and Zhang. In contrast, centeredness of the subgroup **alone** need not imply either all-coset property, as the modulus-123 example shows. This corrects a misleading distinction between the two all-coset notions sometimes made when describing this example; no novelty is claimed for their equivalence.

## Assumptions and scope

The second prime ranges over every odd prime except \(41\), including \(q=5\), although the latter is excluded automatically in the density calculation by the reduced progression classes. The term *cyclic* describes the finite multiplicative subgroup \(H_q\), not the quotient of the full unit group. All multiplicative cosets are cosets in \((\mathbb Z/41q\mathbb Z)^\times\). Prime density means the natural density relative to \(\pi(x)\), justified by the prime number theorem in fixed coprime progressions. Only the imprimitive index-eight subgroup containing the full second-prime CRT factor is classified, not arbitrary octic characters or all index-eight subgroups of semiprime unit groups.

## Proof

**Local coset structure.** Direct modular arithmetic shows that \(6\) has order \(40\) modulo \(41\): \(6^{20}\equiv-1\pmod{41}\) and \(6^8\equiv10\ne1\pmod{41}\). Thus \(K=\langle6^8\rangle\) is the unique index-eight subgroup. The cosets \(C_j=6^jK\), with their exact representatives and integer sums, are

| \(j\) | Elements of \(C_j\) in increasing order | Sum \(s_j\) |
|:--:|:--|--:|
|0|1, 10, 16, 18, 37|82|
|1|6, 14, 17, 19, 26|82|
|2|2, 20, 32, 33, 36|123|
|3|11, 12, 28, 34, 38|123|
|4|4, 23, 25, 31, 40|123|
|5|15, 22, 24, 27, 35|123|
|6|5, 8, 9, 21, 39|82|
|7|3, 7, 13, 29, 30|82|

**Exact lifting identity.** Let \(X_i\) be the coset of units modulo \(41q\) with CRT components \(C_i\times\mathbb F_q^\times\). Fix \(a\in C_i\). The \(q\) positive integers \(a+41t\), \(0\le t<q\), have total sum \(qa+41q(q-1)/2\); exactly one is divisible by \(q\), namely \(q[aq^{-1}]_{41}\), where \([\cdot]_{41}\) denotes the least positive representative modulo \(41\). Removing it and summing over \(a\in C_i\) gives, when \(q\bmod41\in C_j\),
\[
S_{41q}(X_i)-\frac{41q|X_i|}{2}
=q\left(\sum_{a\in C_i}a-\sum_{b\in C_{i-j}}b\right)
=q(s_i-s_{i-j}),\qquad |X_i|=5(q-1).\tag{1}
\]
This is an equality of ordinary integer sums, with no passage to representatives after summation. Its derivation also covers \(q=5\).

**Index, cyclicity and the subgroup defect.** The Chinese remainder theorem gives \(H_q\cong C_5\times C_{q-1}\), so its order is \(5(q-1)\), index is eight, and it is cyclic exactly when \(\gcd(5,q-1)=1\). Applying (1) with \(i=0\), the defect is \(q(82-s_{-j})\). The coset-sum vector is \((82,82,123,123,123,123,82,82)\), so \(s_{-j}=82\) if and only if \(j\in\{0,1,2,7\}\), proving the two-valued law.

**All-coset condition and the witness.** By (1), all eight cosets are centered if and only if cyclic translation by \(j\) fixes the entire sequence \((s_i)\). The four low-sum positions \(\{6,7,0,1\}\) form one cyclic interval of length four, with no nonzero translational period; hence \(j=0\). In particular
\[
H_3=\{1,10,16,37,59,83,92,98,100,119\}
\]
has sum \(615=123\cdot10/2\), while the coset with first CRT component \(C_1\) has sum \(492\). Thus an individually centered subgroup need not have all its cosets centered or balanced. The known equivalence between the **all-coset** first-moment and half-interval conditions is not contradicted: both fail in this example.

**Densities.** The reduced residue classes modulo \(205=41\cdot5\) number \(\varphi(205)=160\). Exactly \(120\) have \(q\not\equiv1\pmod5\). Among those, \(60\) lie in the four centered octic classes; \(15\) have \(j=0\); and \(45\) are centered but not all-coset centered. The prime number theorem in arithmetic progressions therefore yields \(60/160=3/8\), \(45/160=9/32\), and \(15/160=3/32\). The finitely many excluded primes do not change these limits.

**Minimal conductor.** For another prime conductor \(p\), an index-eight subgroup of \(\mathbb F_p^\times\times\mathbb F_q^\times\) containing the complete second CRT factor has the form \(C_{(p-1)/8}\times C_{q-1}\), requiring \(8\mid p-1\). Since \(q-1\) is even, cyclicity forces \((p-1)/8\) odd, equivalently \(p\equiv9\pmod{16}\). The only positive integers below \(41\) in that residue class are \(9\) and \(25\), both composite; \(p=41\) works with \(q=3\). Thus the conductor is least in the precisely stated family.

## Verification and independent limits

The supplied exact program `verify.py` reconstructs the eight local cosets and their sums, independently checks all eight lifted coset sums for the 51 odd primes below 251 distinct from 41, and verifies the modulus-123 example and all 160 coprime residue classes modulo 205. These computations corroborate local arithmetic; they do not establish an all-prime law or prime-density theorem. Those follow from the symbolic identity (1), CRT, and standard prime equidistribution. Nothing here asserts a classification of primitive octic characters or all semiprime subgroups.

## Relationship to prior work

Ma, Merca and Zhang, *Residue Sums Modulo Products of Two Distinct Odd Primes* (arXiv:2610.29608v1, 2026-10-21), supply general odd-character identities and imprimitive index-four and index-six examples. Their general discussion expressly identifies all-coset centering with Pomerance–Ulmer balance for odd moduli. The present calculation applies that established framework to the first possible cyclic imprimitive index-eight conductor and evaluates its complete octic local coset-sum vector, individual and simultaneous centering classes, and prime densities. This is not a claim to have discovered the CRT lifting principle or the balance equivalence; an unindexed octic period table or a stronger prior theorem might contain the local evaluation.

Pomerance and Ulmer, *On balanced subgroups of the multiplicative group* (arXiv:1204.6705, 2012), study balance in half intervals across every coset. That all-coset notion is equivalent to all-coset first-moment centering for odd moduli, as distinguished from centering a single specified subgroup. The equivalence does not itself imply which residue classes \(q\bmod41\) satisfy the condition, since that requires the displayed octic sums.

## Limitations

All statements concern the full-second-factor imprimitive index-eight family at the smallest viable conductor. There is no assertion about all index-eight subgroups, all prime conductors, primitive characters, or effective prime-density errors. The finite verifier is not a proof of historical priority or an infinite-prime proof. The coefficientwise CRT argument gives the infinite-prime conclusion; comparison with unindexed local-period tables may still change the originality judgment of the concrete finite evaluation.

## References

1. H. Ma, M. Merca, and W. Zhang, *Residue Sums Modulo Products of Two Distinct Odd Primes*, arXiv:2610.29608v1 (2026-10-21), https://arxiv.org/abs/2610.29608.
2. C. Pomerance and D. Ulmer, *On balanced subgroups of the multiplicative group*, arXiv:1204.6705 (2012), https://arxiv.org/abs/1204.6705.
