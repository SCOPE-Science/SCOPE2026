# Associator nuclei and commutant of even-order dihedral quandle algebras

## Finding

Let \(K\) be any field, let \(n=2m\ge2\), and give \(A=K[R_n]\) basis \(e_i\) for \(i\in\mathbb Z/n\mathbb Z\), with bilinear multiplication \(e_i e_j=e_{2j-i}\). Write \(N_l,N_m,N_r\) for the subspaces of elements that annihilate every associator in the left, middle and right positions, respectively; write \(N=N_l\cap N_m\cap N_r\), \(C=\{a:ab=ba\text{ for every }b\in A\}\) and \(Z=N\cap C\). For \(a=\sum_i a_i e_i\), put \(s_j=a_j+a_{j+m}\) for \(0\le j<m\).

* \(N_l\) consists of the vectors with coefficients constant separately on the even and odd indices.
* \(N_m\) consists of the vectors with \(s_j\) constant in \(j\).
* If \(m\) is odd, \(N_r=N_m\). If \(m\) is even, \(N_r\) consists of the vectors with all \(s_j=0\).
* \(C=Z=0\) for all even orders.

The dimensions follow:

| Condition | \(\dim N_l\) | \(\dim N_m\) | \(\dim N_r\) | \(\dim C\) | \(\dim N\) | \(\dim Z\) |
|---|---:|---:|---:|---:|---:|---:|
| \(m\) odd | 2 | \(m+1\) | \(m+1\) | 0 | 2 | 0 |
| \(m\) even, \(\operatorname{char}K\ne2\) | 2 | \(m+1\) | \(m\) | 0 | 0 | 0 |
| \(m\) even, \(\operatorname{char}K=2\) | 2 | \(m+1\) | \(m\) | 0 | 2 | 0 |

Whenever \(N\ne0\), it is spanned by the parity sums \(\Omega_0,\Omega_1\), where \(\Omega_\epsilon=\sum_{i\equiv\epsilon\bmod2}e_i\). Its multiplication is
\[
(\alpha\Omega_0+\beta\Omega_1)(\gamma\Omega_0+\delta\Omega_1)
=m(\gamma+\delta)(\alpha\Omega_0+\beta\Omega_1).
\]
In particular, for \(4\mid n\), the full nucleus vanishes outside characteristic two, even though all three individual nuclei are nonzero. In characteristic two it is two-dimensional with zero internal multiplication.

## Assumptions and scope

The associator is \((a,b,c)=(ab)c-a(bc)\) and the multiplication convention is the one given above. No field extension or inversion of \(2\), \(m\), or \(n\) in \(K\) is assumed. The theorem concerns even orders only, including \(n=2\), and the center is distinguished from the commutant.

## Proof

Identify the vector space linearly with \(K[t]/(t^n-1)\) by \(e_i\mapsto t^i\); polynomial multiplication is used only for indexing and is not the quandle-algebra product. Put \(P(t)=\sum_i a_i t^i\). Since the product is bilinear, it suffices to test associators and commutators with basis elements in the other positions. In the left nucleus identity with \(e_u,e_v\), the two exponents for the input term \(a_i e_i\) are \(2v-2u+i\) and \(4v-2u-i\). In the middle identity they are \(2v+u-2i\) and \(4v-u-2i\). In the right identity they are \(2i-2v+u\) and \(4i-2v-u\). And for \(a e_v=e_v a\) they are \(2v-i\) and \(2i-v\). Removing common shifts gives
\[
\begin{aligned}
a\in N_l&\iff P(t)=t^{2v}P(t^{-1})\quad(\text{all }v),\\
a\in N_m&\iff t^{2u}P(t^{-2})=t^{2v}P(t^{-2})\quad(\text{all }u,v),\\
a\in N_r&\iff t^{2u}P(t^2)=P(t^4)\quad(\text{all }u),\\
a\in C&\iff t^{3v}P(t^{-1})=P(t^2)\quad(\text{all }v).
\end{aligned}
\]

For the left system, \(v=0,1\) gives reversal symmetry and invariance under a shift of two. Exactly the sequences constant on each parity orbit have both properties. For the middle system, \(P(t^2)=\sum_{j=0}^{m-1}s_jt^{2j}\); reversing exponents does not affect the property of shift invariance. A shift of two is transitive on the even exponents, so the condition is constancy of the \(s_j\). The map to \((s_j)\) is onto because the first \(m\) coefficients can be chosen freely and the second \(m\) set to zero; its kernel has dimension \(m\) over every field.

For the right system, \(u=0,1\) first forces \(Q=P(t^2)\) to be shift invariant, hence \(Q=s\sum_{j=0}^{m-1}t^{2j}\), and then requires \(Q(t^2)=Q(t)\). Doubling permutes the even exponents when \(m\) is odd, so this is automatic. If \(m\) is even, \(Q(t^2)\) has no coefficient at exponent 2, since reduction modulo \(n\) preserves divisibility by 4. The equality forces \(s=0\), which conversely suffices.

For the commutant, \(v=0,1\) implies invariance of \(P(t^{-1})\) under a shift of three. Its coefficient sequence is therefore constant modulo \(\gcd(n,3)\), which is odd; every such orbit contains an odd index. The equality at \(v=0\) forces every odd-indexed coefficient to be zero, because \(P(t^2)\) has even support. Thus the commutant and the center vanish.

If \(m\) is odd, the pair sums of a vector in \(N_l\) add coefficients of opposite parities and are therefore all equal. If \(m\) is even, the pair sums are twice the coefficient on their respective parity, so the condition \(s_j=0\) gives precisely the stated characteristic switch (both parities are represented). Finally the reflection \(i\mapsto2j-i\) permutes each parity class, so \(\Omega_\epsilon e_j=\Omega_\epsilon\). Bilinearity gives the displayed product.

## Verification

The accompanying `verify.py` constructs all constraints directly from the basis multiplication using modular elimination. Its even-order checks cover \(2\le n\le14\) over the prime fields of orders 2, 3 and 5, including the dimension switch, parity bases when the full nucleus is nonzero and their product. It also includes odd-order checks as comparisons outside this theorem. Run `python3 verify.py`; the success marker is `ALL_NUCLEUS_CHECKS_OK`. The exact proof above, not extrapolation from these checks, establishes the even-order result over every field.

## Relationship to prior work and limitations

The odd-order dihedral quandle is Latin: \(1-T=2\) is invertible on the index group for \(T=-1\). The general Latin-quandle and Latin Alexander-quandle nucleus classifications in [1,2] already cover all three odd-order nuclei and the resulting nonassociative center. Sangaré–Ta [3, Proposition 4.7] also covers the odd left nucleus directly. The split Alexander commutant theorem in [4] specializes to the odd-order dihedral commutant over its finite splitting fields. None of these odd-order statements is part of the present finding. In even order the quandle is not Latin, and the pair-sum collapse and right-nucleus condition are not captured by that specialization. Kaur–Singh [5] distinguish even orders divisible by four in right-module decompositions over \(\mathbb R\) or \(\mathbb C\); the associator kernels and the characteristic-two intersection here are different invariants. This theorem does not classify non-Latin Alexander quandle algebras in general or establish publication priority over unexamined work.

## References

1. *Associator span and nuclei of connected and Latin quandle algebras*, [Resultary record 84e5c5bb458f](https://github.com/Resultary/2026/blob/main/2026/10/13/SCOPE-associator-span-and-nuclei-of-connected-and-latin-quandle-algebr--84e5c5bb458f/RESULT.md), Finding and assumptions.
2. *Associator quotients and the three nuclei of finite Latin Alexander quandle rings*, [Resultary record 2cc2877d146f](https://github.com/Resultary/2026/blob/main/2026/10/25/SCOPE-associator-quotients-and-the-three-nuclei-of-finite-latin-alexan--2cc2877d146f/RESULT.md), Finding and assumptions.
3. B. Sangaré and L. Ta, *Idempotents, automorphism groups, and commutator widths of quandle algebras*, [arXiv:2608.01550v1](https://arxiv.org/html/2608.01550v1), Proposition 4.7.
4. *Exact commuting-pair counts and commutants of split finite Alexander quandle algebras*, [Resultary record 41d844a58011](https://github.com/Resultary/2026/blob/main/2026/10/25/SCOPE-exact-commuting-pair-counts-and-commutants-of-split-finite-alexa--41d844a58011/RESULT.md), Finding and proof §3.
5. D. Kaur and P. Singh, *Decomposition of quandle rings of dihedral quandles*, [arXiv:2206.03162](https://arxiv.org/abs/2206.03162).
