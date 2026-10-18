# Exact Pell-state cycle spectrum modulo powers of two

## Finding

Let \(A=\begin{pmatrix}0&1\\1&2\end{pmatrix}\), and for each integer \(k\ge1\) let \(T_k\) be the permutation of \((\mathbb Z/2^k\mathbb Z)^2\) induced by \(A\), equivalently
\[
T_k(a,b)=(b,a+2b)\pmod {2^k}.
\]
A cycle means an orbit of the permutation, counted once regardless of its starting state. For every \(k\ge2\), the total number of cycles is exactly
\[
\boxed{N_k=2^{k+1}-2},
\]
and \(N_1=3\).

More precisely, for \(k\ge3\), the numbers of cycles of least periods \(1,2,4\) are respectively \(2,1,7\). For each integer \(j\) with \(3\le j<k\), there are exactly \(3\cdot2^{j-1}\) cycles of least period \(2^j\). Finally, there are exactly \(2^{k-1}\) cycles of least period \(2^k\), with no other least periods. At \(k=2\), the multiplicities of periods \(1,2,4\) are \(2,1,3\), and at \(k=1\), those of periods \(1,2\) are \(2,1\).

The complete fixed-point spectrum, from which these claims follow, is also explicit. Write \(F_j(k)=\#\{v\in(\mathbb Z/2^k\mathbb Z)^2:T_k^{2^j}(v)=v\}\). Then for every \(k\ge1\),
\[
F_0(k)=2,\qquad F_1(k)=4,\qquad
F_j(k)=2^{\min(k,j)+\min(k,j+1)}\quad(j\ge2).
\]

## Assumptions and scope

The modulus is an integral power \(2^k\) with \(k\ge1\). **Every initial pair** of residues is included, not only the standard Pell seed \((0,1)\), primitive pairs, or pairs generating a fixed cyclic subgroup. The companion matrix \(A\) has determinant \(-1\), and therefore acts as a permutation for every specified modulus. All periods are least positive periods of pairs, not periods of an individual coordinate in isolation.

## Proof

For an integer matrix \(B\) with nonzero determinant, let its two integer Smith invariant factors be \(d_1,d_2\), where \(d_1\) is the greatest common divisor of its four entries and \(d_1d_2=|\det B|\). If \(v_2(d_i)=e_i\), then the number of solutions of \(Bv\equiv0\pmod{2^k}\) is
\[
2^{\min(k,e_1)+\min(k,e_2)}.
\]
Indeed, unimodular row and column operations reduce \(B\) to a diagonal matrix without changing its kernel over \(\mathbb Z/2^k\mathbb Z\); the scalar congruence with coefficient \(2^eu\), \(u\) odd, has \(2^{\min(k,e)}\) solutions.

Direct exact matrix multiplication gives
\[
A-I=\begin{pmatrix}-1&1\\1&1\end{pmatrix},\qquad
A^2-I=\begin{pmatrix}0&2\\2&4\end{pmatrix},
\]
so their Smith invariant factors are, respectively, \((1,2)\) and \((2,2)\). Consequently \(F_0(k)=2\) and \(F_1(k)=4\) for every \(k\ge1\).

Next,
\[
A^4-I=4C_2,\qquad C_2=\begin{pmatrix}1&3\\3&7\end{pmatrix},
\qquad\det C_2=-2.
\]
For every \(j\ge2\), inductively write \(A^{2^j}=I+2^jC_j\). Squaring yields the exact integer-matrix relation
\[
C_{j+1}=C_j(I+2^{j-1}C_j).
\]
Because \(j\ge2\), the second factor is congruent to \(I\) modulo \(2\) and therefore has odd determinant. Hence it is invertible over the ring of \(2\)-adic integers, and multiplying on the right by it leaves the \(2\)-adic Smith invariant exponents of \(C_j\) unchanged. Since \(C_2\) has one odd entry and determinant of \(2\)-adic valuation one, these exponents are \((0,1)\) for every \(C_j\). Thus the Smith exponents of \(A^{2^j}-I\) are precisely \((j,j+1)\) for every \(j\ge2\). The kernel-counting formula proves the displayed expression for \(F_j(k)\).

In particular, \(F_k(k)=2^{2k}\) for \(k\ge2\), while the same equality follows for \(k=1\) from \(F_1(1)=4\). Hence \(A^{2^k}\equiv I\pmod{2^k}\), so every least orbit period divides \(2^k\) and is a power of two. Let \(c_j(k)\) be the number of cycles with least period \(2^j\). Every such cycle contains exactly \(2^j\) states; consequently
\[
c_0(k)=F_0(k),\qquad
c_j(k)=\frac{F_j(k)-F_{j-1}(k)}{2^j}\quad(1\le j\le k).
\]
For \(k\ge3\) these differences give \(c_0=2\), \(c_1=1\), \(c_2=7\), \(c_j=3\cdot2^{j-1}\) when \(3\le j<k\), and \(c_k=2^{k-1}\). Direct substitution gives the two stated small boundary cases. Summing for \(k\ge3\),
\[
\sum_{j=0}^{k}c_j(k)
=10+3\sum_{j=3}^{k-1}2^{j-1}+2^{k-1}
=2^{k+1}-2.
\]
For \(k=2\), the sum is \(2+1+3=6=2^3-2\). This proves all claims.

## Verification

The accompanying standalone Python 3 program `verify.py` verifies the three base matrix identities, the exact \(2\)-adic Smith exponents of \(A^{2^j}-I\) for \(2\le j\le14\), and separately enumerates every state orbit for all \(1\le k\le9\). It checks the complete period-multiplicity dictionary for each modulus, that the cycle lengths account for exactly \(2^{2k}\) states, and the asserted cycle total. Invoke it as `python3 verify.py`. The expected terminal marker is `VERIFY_OK`.

The finite checks are not substitutes for the all-\(k\) lifting argument above; they directly stress-test its premises and consequences.

## Relationship to prior work

The ordinary Pell sequence satisfies \(P_{n+2}=2P_{n+1}+P_n\). Deveci and Karaduman (2015, Theorem 2.2) determine the period of the standard Pell sequence modulo a power of two, which is a statement about one chosen initial condition and the order of its companion matrix. The present classification considers **every** initial pair and determines the full period spectrum and the number of distinct state cycles, none of which follows merely from knowing that maximal period. Their other theorems give prime-power period growth and periods in dihedral groups, not the all-seed orbit multiplicity formula.

Deveci, Akdeniz, and Karaduman (2015, Sections 2–4) study generalized Pell \(p\)-sequences and basic orbit periods in finite groups; these are related to period lifting but do not state the two-dimensional complete-cycle census above. Brent's work on generalized Fibonacci recurrence periods under irreducibility modulo two also does not yield this particular classification: the characteristic polynomial here, \(t^2-2t-1\), reduces to \((t+1)^2\) modulo two, so the irreducibility assumption of the cited principal-period theorem does not apply. Published Pell/Pisano period tables similarly record the orbit of the standard seed rather than all modular states.

## Limitations

This is a theorem for the specified trace-two Pell companion map over powers of two only. It does not classify odd-prime moduli, arbitrary traces, or nonlinear Pell maps. It is not a claim that the general Smith-normal-form method or period-lifting principle is new. The claim of a previously unreported complete cycle census is based on comparisons with the cited literature and mathematical-result searches, not an exhaustive search of every publication. Independent audit has not been performed.

## References

1. Ö. Deveci and E. Karaduman, “The Pell Sequences in Finite Groups,” *Utilitas Mathematica* **96** (2015), 263–276, especially Theorems 2.1–2.6 and Table 1. https://www.researchgate.net/publication/295591003_The_Pell_Sequences_in_Finite_Groups
2. Ö. Deveci, M. Akdeniz, and E. Karaduman, “The Generalized Pell \(p\)-Sequences in Groups,” *Ars Combinatoria* **120** (2015), 383–401, especially Sections 2–4. https://combinatorialpress.com/article/ars/Volume%20120/volume-120-paper-34.pdf
3. R. P. Brent, “On the periods of generalized Fibonacci recurrences,” *Mathematics of Computation* **63** (1994), 389–401. Open version published 30 April 2010: https://arxiv.org/abs/1004.5439
4. “Pisano period,” background and tabulated periods of Pell numbers, https://en.wikipedia.org/wiki/Pisano_period (consulted for distinction between a chosen-seed period and all-state cycles).
