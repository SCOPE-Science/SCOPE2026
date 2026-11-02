# The least cyclic octic conductor: exact residue sums at \(41q\)

## Finding
Let \(q\) be any odd prime other than \(41\). Let \(K=\langle10\rangle=\{1,10,16,18,37\}\) be the order-five subgroup of \(\mathbb F_{41}^{\times}\), and let \(H_q\) comprise the invertible residues modulo \(41q\) whose reductions modulo \(41\) lie in \(K\). For a finite subset \(X\) of the units modulo \(m\), write \(S_m(X)\) for the sum of the least positive integer representatives of its elements; say that \(X\) is *centered* when \(S_m(X)=m|X|/2\). The term *all-coset centered* means that **every multiplicative coset** of \(H_q\) is centered in this sum-of-representatives sense. It is not the same as the half-interval-count definition of balanced subgroups used in other literature.

Let \(C_j=6^jK\), with subscripts taken modulo \(8\), and write \(q\bmod41\in C_j\). Then \(H_q\) has index \(8\), has order \(5(q-1)\), and is cyclic if and only if \(q\not\equiv1\pmod5\). Its sum has the exact two-valued law
\[
S_{41q}(H_q)-\frac{41q|H_q|}{2}=
\begin{cases}
0,&j\in\{0,1,2,7\},\\
-41q,&j\in\{3,4,5,6\}.
\end{cases}
\]
Moreover all eight multiplicative cosets are centered simultaneously if and only if \(q\bmod41\in C_0=K\).

Among rational primes \(q\), the three densities for *cyclic and centered*, *cyclic and centered but not all-coset centered*, and *cyclic and all-coset centered* are, respectively, \(3/8\), \(9/32\), and \(3/32\). The finite exclusions \(q=5,41\) do not affect densities.

The conductor \(41\) is the smallest odd prime \(p\) for which a cyclic index-eight subgroup of \((\mathbb Z/pq\mathbb Z)^\times\) containing the full unit factor at \(\mathbb F_q^\times\) exists. In particular, modulo \(123\), \(H_3\) is centered but not all-coset centered.

## Assumptions and scope
The second prime \(q\) ranges over **all odd primes distinct from \(41\)**. For the cyclic classification no restriction on the ordering of \(41\) and \(q\) is imposed; \(q=5\) is included, even though it does not belong to a reduced residue class modulo \(205\). Natural prime density means \(\lim_{x\to\infty}\#\{q\le x:\text{property}\}/\pi(x)\), whose existence follows here from Dirichlet's theorem and the prime number theorem for fixed arithmetic progressions. The claim only treats the imprimitive index-eight kernel containing the *entire second-prime CRT factor*. It does not classify all index-eight subgroups modulo semiprimes.

## Proof
**Step 1: the unique local subgroup.** The element \(6\) has order \(40\) modulo \(41\): its \(20\)-th power is \(-1\), and its eighth power is \(10\ne1\), so its order has neither prime-factor reduction by \(2\) nor \(5\). Thus the unique subgroup of index eight is \(K=\langle6^8\rangle\). The eight cosets and their sums of representatives are the following exact table:

| \(j\) | Elements of \(C_j\) in increasing order | \(\sum_{a\in C_j}a\) |
|:--:|:--|--:|
|0|1, 10, 16, 18, 37|82|
|1|6, 14, 17, 19, 26|82|
|2|2, 20, 32, 33, 36|123|
|3|11, 12, 28, 34, 38|123|
|4|4, 23, 25, 31, 40|123|
|5|15, 22, 24, 27, 35|123|
|6|5, 8, 9, 21, 39|82|
|7|3, 7, 13, 29, 30|82|

**Step 2: exact lifting sum.** For any \(i\), the coset \(X_i\) modulo \(41q\) with CRT components \(C_i\times\mathbb F_q^\times\) is the set of positive integers \(n<41q\) satisfying \(n\bmod41\in C_i\) and \(q\nmid n\). For a fixed representative \(a\in C_i\), the \(q\) integers \(a+41t\) with \(0\le t<q\) contain exactly one multiple of \(q\), namely \(q[aq^{-1}]_{41}\), where \([\cdot]_{41}\) denotes the least positive representative modulo \(41\). Their sum after this removal is
\[
q a+\frac{41q(q-1)}{2}-q[aq^{-1}]_{41}.
\]
If \(q\bmod41\in C_j\), multiplication by \(q^{-1}\) carries \(C_i\) onto \(C_{i-j}\). Summing the preceding exact identity over its five members proves
\[
S_{41q}(X_i)-\frac{41q|X_i|}{2}
=q\biggl(\sum_{a\in C_i}a-\sum_{b\in C_{i-j}}b\biggr).
\tag{1}
\]
Notice that \(|X_i|=5(q-1)\) and the sum over all \(t\) was computed before any modular reduction; there is no ambiguity about least representatives.

**Step 3: index, cyclicity, and the two possible sums.** CRT identifies \(H_q\) with \(K\times\mathbb F_q^\times\), which has order \(5(q-1)\) and index \(40(q-1)/(5(q-1))=8\). Since each factor is cyclic, their product is cyclic exactly when \(\gcd(5,q-1)=1\), equivalently \(q\not\equiv1\pmod5\). Substituting \(i=0\) in (1) gives \(q(82-s_{-j})\), where the vector of coset sums is
\[
(s_0,s_1,s_2,s_3,s_4,s_5,s_6,s_7)
=(82,82,123,123,123,123,82,82).
\]
Thus \(s_{-j}=82\) exactly when \(j\in\{0,1,2,7\}\); in the other four classes the difference is \(q(82-123)=-41q\).

**Step 4: all-coset centeredness.** Equation (1) vanishes for all eight cosets exactly if the cyclic word \((s_0,\ldots,s_7)\) is invariant under translation by \(j\). Its four low entries form one cyclic interval \(\{6,7,0,1\}\), which is not invariant under any nonzero translation modulo eight. Hence this happens exactly when \(j=0\). For \(q=3\), the subgroup is
\[
H_3=\{1,10,16,37,59,83,92,98,100,119\},
\]
whose sum is \(615=123\cdot10/2\); but the coset corresponding to \(C_1\) has sum \(492\), not \(615\). This is an explicit centered but not all-coset centered case.

**Step 5: prime densities.** Among the \(\varphi(205)=160\) reduced residue classes modulo \(205\), exactly \(120\) satisfy \(q\not\equiv1\pmod5\). Of these, \(60\) have the favorable index \(j\in\{0,1,2,7\}\); \(15\) have \(j=0\), and the other \(45\) have \(j\in\{1,2,7\}\). Dirichlet's theorem and equidistribution among fixed coprime progressions give densities \(60/160=3/8\), \(45/160=9/32\), and \(15/160=3/32\).

**Step 6: least possible conductor.** For a general prime conductor \(p\), an index-eight imprimitive kernel containing the entire CRT factor \(\{1\}\times\mathbb F_q^\times\) must have \(8\mid p-1\) and CRT structure \(C_{(p-1)/8}\times C_{q-1}\). Cyclicity requires \(\gcd((p-1)/8,q-1)=1\). Since \(q-1\) is even, \((p-1)/8\) must be odd, so \(p\equiv9\pmod{16}\). No prime less than \(41\) lies in that congruence class (the positive candidates below it are \(9\) and \(25\), both composite), while \(p=41\) works with \(q=3\). This proves the minimal-conductor assertion.

## Verification
The accompanying self-contained program `verify.py` independently reconstructs the eight cosets, their exact sums, and CRT residue sums by direct enumeration of every coset for \(51\) odd primes \(q<251\) different from \(41\). It checks \(408\) exact coset sums, the rational prime progression class counts modulo \(205\), the centered-but-not-all-centered witness modulo \(123\), and the first-conductor restriction. The finite enumeration is corroborating evidence only: the preceding symbolic argument establishes all primes and the limiting densities.

## Relationship to prior work
Ma, Merca, and Zhang study the centered least-positive-residue sum problem modulo products of two odd primes; their October 2026 paper explicitly develops the index-four imprimitive case and index-six families. It also provides a general odd-character expansion and a finite census that are methodological antecedents. Neither the cited index-four or index-six classifications nor the general expansion alone gives this explicit *first-conductor index-eight* two-valued law with the three prime densities without the local octic coset computation and CRT analysis above. A finite semiprime census is not an infinite classification.

Pomerance and Ulmer study *balanced* subgroups by equality of cardinalities in the two half intervals. That is a different invariant from equality of the sums of least positive representatives in the present theorem. Both notions have natural character-theoretic expressions, but one should not identify them.

## Limitations
Only the conductor-\(41\), full-second-factor imprimitive index-eight kernel is classified. Other index-eight subgroups, higher conductors, and primitive characters are not treated. The elementary CRT sum identity may already be implicit in earlier work; priority of the explicit conductor-\(41\) classification and density split has not received independent specialist assessment. The finite verification does not prove any assertion for all primes. The prime-density argument uses the standard prime number theorem in arithmetic progressions, not an effective error bound.

## References
1. H. Ma, M. Merca, and W. Zhang, *Residue Sums Modulo Products of Two Distinct Odd Primes*, arXiv:2610.29608v1 (2026-10-21), https://arxiv.org/abs/2610.29608 .
2. C. Pomerance and D. Ulmer, *On balanced subgroups of the multiplicative group*, arXiv:1204.6705 (2012), https://arxiv.org/abs/1204.6705 .
