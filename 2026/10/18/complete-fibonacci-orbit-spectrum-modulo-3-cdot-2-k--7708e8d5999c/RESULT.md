# Complete Fibonacci orbit spectrum modulo \(3\cdot 2^k\)

## Finding

For integers \(k\ge3\), put \(m=3\cdot2^k\). Define the Fibonacci state map
\[
T_m:(\mathbb Z/m\mathbb Z)^2\longrightarrow(\mathbb Z/m\mathbb Z)^2,\qquad
T_m(a,b)=(b,a+b).
\]
Its determinant is \(-1\), so every state belongs to a finite cycle. Let \(c_k(d)\) be the number of distinct cycles of **least** length \(d\), with states counted up to cyclic rotation.

For \(k=3\), the complete list of nonzero multiplicities is
\[
(c_3(1),c_3(3),c_3(6),c_3(8),c_3(12),c_3(24))=(1,1,2,1,4,21).
\]
For every \(k\ge4\), the complete list is
\[
(c_k(1),c_k(3),c_k(6),c_k(8),c_k(12),c_k(24))=(1,1,2,1,4,93),
\]
and in addition
\[
c_k(3\cdot2^{j-1})=9\cdot2^{j-1}
\quad(5\le j\le k).
\]
Every cycle length not specified is absent. In particular,
\[
\boxed{\sum_{d\ge1}c_k(d)=9\cdot2^k-42=3(3\cdot2^k-14)\qquad(k\ge3).}
\]
Thus the explicit conjecture for OEIS A015134 recorded in 2023 holds in every claimed case. The finer multiplicity statement is a complete classification, not merely a total count.

## Assumptions and scope

All congruences use integer residue rings. A *cycle* is an orbit of the invertible state map, not a collection of equal-value terms and not a recurrence with canonical initial values only. The parameter \(k\) is an arbitrary integer at least \(3\). The result makes no assertion about other moduli or unrelated recurrences.

Write \(A=\left(\begin{smallmatrix}0&1\\1&1\end{smallmatrix}\right)\). A vector modulo \(2^j\) is *primitive* if at least one coordinate is odd. A vector modulo \(2^k\) has valuation layer \(j\) when it equals \(2^{k-j}\) times a primitive vector modulo \(2^j\); the zero vector is layer \(0\).

## Proof

**1. Exact primitive periods at powers of two.** The matrix identities
\[
A^3=\begin{pmatrix}1&2\\2&3\end{pmatrix},\quad
A^6=\begin{pmatrix}5&8\\8&13\end{pmatrix},\quad
A^{12}=\begin{pmatrix}89&144\\144&233\end{pmatrix}
\]
are direct multiplications. Each of the integral matrices
\[
\frac{A^3-I}{2}=\begin{pmatrix}0&1\\1&1\end{pmatrix},\qquad
\frac{A^6-I}{4}=\begin{pmatrix}1&2\\2&3\end{pmatrix},\qquad
\frac{A^{12}-I}{8}=\begin{pmatrix}11&18\\18&29\end{pmatrix}
\]
has odd determinant. In particular, each induces an invertible linear transformation modulo \(2\).

Modulo \(2\), the three primitive states form one cycle of length \(3\). The displayed matrices show that every primitive state modulo \(4\) has least period \(6\), and every primitive state modulo \(8\) has least period \(12\): passage from modulus \(2\) to \(4\), and from \(4\) to \(8\), strictly doubles the period because the respective normalized matrices are invertible modulo \(2\).

For the remaining moduli set \(B_0=(A^{12}-I)/8\), so \(B_0\) is invertible modulo \(2\). Inductively,
\[
A^{12\cdot2^s}=I+2^{s+3}B_s,\qquad B_s\equiv B_0\pmod2,
\]
because squaring replaces \(B_s\) by \(B_s+2^{s+2}B_s^2\). Hence, if \(v\) is primitive, the vector \((A^{12\cdot2^s}-I)v\) is divisible by \(2^{s+3}\) but not by \(2^{s+4}\). For any odd integer \(u\), taking the \(u\)-th power leaves the normalized difference invertible modulo \(2\), so an odd multiplier cannot produce earlier return. Every primitive vector modulo \(2^j\) therefore has least period
\[
L_1=3,\qquad L_2=6,\qquad L_j=3\cdot2^{j-1}\ (j\ge3).
\]

At layer \(j\ge1\) there are exactly \(2^{2j}-2^{2j-2}=3\cdot2^{2j-2}\) states: the difference between all pairs modulo \(2^j\) and pairs both even. Multiplication by \(2^{k-j}\) identifies this layer with primitive states modulo \(2^j\), preserving the period. Therefore, the orbit multiplicities modulo \(2^k\) are precisely one fixed zero orbit, one cycle of length \(3\), two cycles of length \(6\), and \(2^{j-1}\) cycles of length \(3\cdot2^{j-1}\) for every \(3\le j\le k\).

**2. The modulo-three component.** Direct computation gives
\[
A^4\equiv-I\pmod3,\qquad
A^2-I\equiv\begin{pmatrix}0&1\\1&1\end{pmatrix}\pmod3.
\]
The second matrix is invertible modulo \(3\). Thus every nonzero vector modulo \(3\) has least period \(8\), while the zero vector is fixed. Since there are eight nonzero vectors, the modulo-three map has exactly one cycle of length \(1\) and one cycle of length \(8\).

**3. Chinese remaindering and exact assembly.** Since \(3\) and \(2^k\) are coprime, CRT conjugates \(T_m\) to the product of the two state permutations described above. A product of cycles of respective lengths \(r\) and \(s\) decomposes into exactly \(\gcd(r,s)\) cycles, each of length \(\operatorname{lcm}(r,s)\); this is verified by indexing their positions modulo \(r\) and \(s\) and translating both indices by one.

The length-one modulo-three orbit reproduces the power-of-two cycle spectrum. The length-eight modulo-three orbit contributes one cycle of length \(8\) from the power-of-two zero orbit, then \(1,4,16\) cycles of length \(24\) from the power-of-two layers \(j=1,2,3\). When \(k\ge4\), the layer \(j=4\) contributes an additional \(8\) cycles of length \(24\) from the length-one modulo-three orbit and \(64\) from the length-eight orbit. Hence the length-\(24\) count becomes \(1+4+16+8+64=93\). For each layer \(j\ge5\), its length \(3\cdot2^{j-1}\) is divisible by \(8\), so the two modulo-three cycles together produce \((1+8)2^{j-1}=9\cdot2^{j-1}\) cycles at that length. At \(k=3\), there is no layer \(j=4\), giving \(1+4+16=21\) length-\(24\) cycles instead. The remaining lengths are \(1,3,6,8,12\) with multiplicities \(1,1,2,1,4\).

Finally the total at \(k=3\) is \(30\). For \(k\ge4\), the total equals
\[
1+1+2+1+4+93+\sum_{j=5}^k9\cdot2^{j-1}
=102+9(2^k-16)=9\cdot2^k-42.
\]
(The sum is empty for \(k=4\).) This proves every asserted count and exhaustiveness.

## Verification

The accompanying dependency-free Python program `verify.py` independently enumerates every state orbit modulo \(3\cdot2^k\) for \(3\le k\le7\), compares all cycle-length multiplicities to the theorem, checks the total number of states, and independently enumerates the modulo-\(2^j\) and modulo-\(3\) spectra. It also verifies the three normalized matrix base identities modulo \(2\). Successful execution prints `VERIFY_OK`. These finite computations corroborate, but do not replace, the infinite matrix-and-CRT proof.

## Relationship to prior work

Avila and Khovanova (2014, arXiv:1403.4614, sections 8–10) motivate studying all Fibonacci-like initial pairs modulo a composite modulus and describe the cycles modulo \(8\). Renault (1996, thesis, section 3.1) establishes the classical period of Fibonacci sequences modulo powers of two and the least-common-multiple rule for a generalized sequence under coprime decomposition. OEIS A015134 already gives the total cycle counts numerically and explicitly records Stephen Bartell's **conjecture** \(a(3\cdot2^k)=3(3\cdot2^k-14)\) for \(k\ge3\); the identity itself is not claimed as a previously unstated prediction. The contribution here is an all-\(k\) proof together with the complete distribution by least cycle length. OEIS A015135 tabulates the number of distinct lengths, not their multiplicities. Pudelko (2025, arXiv:2510.24882, section 3) investigates generalized Fibonacci orbit landscapes and proposes prime-power self-similarity, but does not present this mixed-modulus spectral theorem.

## Limitations

The proof uses the specific primes \(2\) and \(3\). It does not prove the other conjectures in OEIS A015134, nor the general prime-power conjectures of Pudelko. A historical proof of the exact total conjecture or stronger orbit-spectrum coverage could exist in literature not found by the stated comparisons.

## References

- B. Avila and T. Khovanova, *Free Fibonacci Sequences*, arXiv:1403.4614 (first public version March 18, 2014), especially sections 8–10. https://arxiv.org/abs/1403.4614
- OEIS A015134, *Number of distinct cycles of Fibonacci-type sequences modulo an integer*, including Bartell's August 20, 2023 conjecture. https://oeis.org/A015134
- OEIS A015135, *Number of distinct periods of Fibonacci-type sequences modulo an integer*. https://oeis.org/A015135
- M. Renault, *The Fibonacci Sequence Under Various Moduli*, Wake Forest University thesis, May 1996, section 3.1. https://webspace.ship.edu/msrenault/fibonacci/fibthesis.pdf
- M. T. Pudelko, *Modular Periodicity of Random Initialized Recurrences*, arXiv:2510.24882 (2025), section 3. https://arxiv.org/abs/2510.24882
