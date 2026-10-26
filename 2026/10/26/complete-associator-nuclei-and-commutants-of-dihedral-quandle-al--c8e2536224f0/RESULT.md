# Complete associator nuclei and commutants of dihedral quandle algebras

## Finding

Let \(K\) be any field, \(n\ge2\), and \(A=K[R_n]\), with basis \(e_i\), \(i\in\mathbb Z/n\mathbb Z\), and bilinear product \(e_i e_j=e_{2j-i}\). Write \(N_l,N_m,N_r\) for the left, middle, and right associator nuclei, \(N=N_l\cap N_m\cap N_r\) for the associative nucleus, \(C=\{a\in A:ab=ba\text{ for all }b\in A\}\) for the commutant, and \(Z=N\cap C\) for the nonassociative center. Set \(m=n/2\) in the even case.

The six exact \(K\)-dimensions \((\dim N_l,\dim N_m,\dim N_r,\dim C,\dim N,\dim Z)\) are

\[
\begin{array}{c|c}
\text{condition}&(\dim N_l,\dim N_m,\dim N_r,\dim C,\dim N,\dim Z)\\\hline
n\text{ odd}&(1,1,1,\gcd(n,3),1,1)\\
n\equiv2\pmod4&(2,m+1,m+1,0,2,0)\\
4\mid n,\ \operatorname{char}K\ne2&(2,m+1,m,0,0,0)\\
4\mid n,\ \operatorname{char}K=2&(2,m+1,m,0,2,0).
\end{array}
\]

These are classifications of subspaces, not just dimensions. With \(a=\sum_i a_i e_i\), the coefficient conditions are as follows.

* If \(n\) is odd, \(N_l=N_m=N_r=N=Z=K\Omega\), where \(\Omega=\sum_i e_i\). The commutant consists of coefficient sequences constant on residue classes modulo \(\gcd(n,3)\).
* If \(n=2m\), write \(s_j=a_j+a_{j+m}\) for \(0\le j<m\). Then \(N_l\) consists exactly of sequences constant separately on even and odd indices; \(N_m\) is given by \(s_0=\cdots=s_{m-1}\); and \(N_r=N_m\) when \(m\) is odd, whereas \(N_r=\{a:s_j=0\text{ for every }j\}\) when \(m\) is even. The commutant and center are zero.

For even \(n\), put \(\Omega_0=\sum_{i\text{ even}}e_i\), \(\Omega_1=\sum_{i\text{ odd}}e_i\). Whenever \(N\ne0\), its basis is \(\Omega_0,\Omega_1\) and its multiplication is explicitly

\[
(\alpha\Omega_0+\beta\Omega_1)(\gamma\Omega_0+\delta\Omega_1)
=m(\gamma+\delta)(\alpha\Omega_0+\beta\Omega_1).
\]

For odd \(n\), the center is the line \(K\Omega\), with \(\Omega^2=n\Omega\). In particular, in characteristic different from \(2\), the associative nucleus vanishes for every order divisible by \(4\), although all three individual nuclei remain nonzero. In characteristic \(2\) it jumps to dimension \(2\), with zero internal multiplication, for those same orders.

## Assumptions and scope

The operation is always \(i\triangleright j=2j-i\) modulo \(n\); changing the left/right quandle convention without corresponding changes to the algebra changes the nucleus labels. A field of arbitrary characteristic, including \(0\), is permitted. No separability, algebraic closure, or invertibility of \(n\) in \(K\) is assumed. All statements hold simultaneously for every integer \(n\ge2\). The word 'center' means the intersection of the three associator nuclei and the commutant, not merely the commutant.

## Proof

Identify the underlying vector space with \(K[t]/(t^n-1)\) by mapping \(e_j\mapsto t^j\). This is only a linear identification: ordinary polynomial multiplication is not the quandle-algebra multiplication. Write \(P(t)=\sum_j a_jt^j\), and interpret negative exponents modulo \(t^n-1\). Bilinearity reduces each universal associator or commutator identity to pairs of basis elements. Direct use of \(e_i e_j=e_{2j-i}\) yields four equivalent systems:

\[
\begin{aligned}
a\in N_l&\iff P(t)=t^{2v}P(t^{-1})\quad\text{for all }v,\\
a\in N_m&\iff t^{2u}P(t^{-2})=t^{2v}P(t^{-2})\quad\text{for all }u,v,\\
a\in N_r&\iff t^{2u}P(t^2)=P(t^4)\quad\text{for all }u,\\
a\in C&\iff t^{3v}P(t^{-1})=P(t^2)\quad\text{for all }v.
\end{aligned}
\]

For the first equivalence, setting \(v=0,1\) gives reversal symmetry \(P(t)=P(t^{-1})\) and invariance under multiplication by \(t^2\). Such a coefficient sequence is constant on the orbits of index translation by \(2\). These are one orbit if \(n\) is odd and the even/odd orbits if \(n\) is even; in either case reversal preserves the orbits. This proves the left-nucleus description.

For the middle nucleus, the displayed condition reduces exactly to invariance of \(P(t^{-2})\) under multiplication by \(t^2\). If \(n\) is odd, doubling permutes the indices, hence all coefficients of \(P\) are equal. If \(n=2m\), the coefficient of \(t^{2j}\) in \(P(t^2)\) is \(s_j=a_j+a_{j+m}\); the same fact holds with the indices reversed for \(P(t^{-2})\). Multiplication by \(t^2\) is transitive on these \(m\) even exponents. Thus middle-nucleus membership is exactly constancy of all \(s_j\), giving dimension \(m+1\).

For the right nucleus, the equations demand both invariance of \(Q=P(t^2)\) under multiplication by \(t^2\) and the identity \(Q=P(t^4)\). The odd case again gives precisely constant \(P\). In the even case the first demand is \(s_j=s\) for all \(j\), so \(Q=s\sum_{j=0}^{m-1}t^{2j}\). If \(m\) is odd, doubling permutes the even exponents and \(Q(t^2)=Q\) automatically. If \(m\) is even, \(Q(t^2)\) is supported on exponents divisible by \(4\), while \(Q\) has coefficient \(s\) at exponent \(2\), forcing \(s=0\). Conversely \(s=0\) makes both equations true. This proves the right-nucleus alternatives without dividing by \(2\) in \(K\).

For the commutant, the equations at \(v=0,1\) show that \(P(t^{-1})\) is invariant under multiplication by \(t^3\); hence its coefficients are constant on residue classes modulo \(d=\gcd(n,3)\). If \(n\) is even, \(P(t^2)\) has no odd-degree coefficients, whereas every residue class modulo \(d\in\{1,3\}\) contains an odd index, so the equality at \(v=0\) forces every coefficient to vanish. If \(n\) is odd, multiplication of exponents by \(2\) is bijective. For \(d=1\), every constant sequence satisfies the equality; for \(d=3\), \(2^{-1}\equiv-1\pmod3\), giving \(P(t^{-1})=P(t^2)\) for every sequence constant modulo \(3\). Thus the commutant has dimension \(d\).

Finally, when \(n\) is odd the three nuclei are \(K\Omega\) and \(\Omega\) lies in the commutant. When \(n=2m\), a left-nuclear vector has coefficients \(c_0\) on even indices and \(c_1\) on odd indices. If \(m\) is odd, its pair sums are all \(c_0+c_1\), so it belongs to both remaining nuclei. If \(m\) is even, its pair sums are \(2c_0\) or \(2c_1\); the right-nucleus condition makes both vanish. Hence the intersection is zero unless \(\operatorname{char}K=2\), in which case both vanish automatically and the full left nucleus survives. The commutant is zero for all even \(n\), establishing the center formula. Each \(\Omega_\epsilon e_j=\Omega_\epsilon\) because the reflection \(i\mapsto2j-i\) permutes each parity class, proving the stated two-dimensional multiplication. The odd case follows similarly by summing over all \(j\). This completes all claims.

## Verification

The standalone file `verify.py` constructs the multiplication table, forms the *original linear associator and commutator constraints* directly at every triple of basis indices, and computes their nullities by modular Gaussian elimination; it does not encode the claimed basis vectors as input. It verifies all six dimensions for each \(2\le n\le14\) in characteristics \(2,3,5\), checks the explicit bases of the full nuclei and their multiplication wherever nonzero, and checks the predicted commutant coefficient patterns. Reproduce with `python3 verify.py`. The code also prints each compared tuple, ending with `ALL_NUCLEUS_CHECKS_OK` on success. These are finite tests; the proof above, not extrapolation, establishes arbitrary size and characteristic.

## Relationship to prior work

Kaur and Singh, *Decomposition of quandle rings of dihedral quandles* (arXiv:2206.03162, first posted 2022-06-07), determine right-module decompositions for even-order dihedral quandle rings over the real or complex field, distinguishing orders divisible by \(4\). Their orbit-sum submodules motivate the parity vectors above, but the six associator/commutant spaces and the characteristic-two jump are different invariants and are not stated there.

Elhamdadi, Fernando, and Tsvelikhovskiy, *Ring Theoretic Aspects of Quandles* (arXiv:1805.05908, 2018), establish the general quandle-ring framework and analyze its ideals, but do not state this nucleus classification. Sangaré and Ta, *Idempotents, automorphism groups, and commutator widths of quandle algebras* (arXiv:2608.01550, 2026), explicitly prove \(N_l=K\Omega\) in odd order (Proposition 4.7): that component is prior work, not an independent novelty claim. The full middle/right/commutant profile, the even-order regimes, and the characteristic-sensitive full nucleus constitute the distinct assertion here.

## Limitations

The theorem concerns dihedral quandles with the displayed multiplication, not arbitrary Alexander quandles. No claims about automorphism groups, all ideals, or module decompositions are made. The checked sources do not establish exhaustive publication priority; a nucleus classification under alternative terminology may exist. A later work already proves the odd-order left-nucleus component, and the result does not claim otherwise. Numerical verification covers prime fields and finitely many orders only; all-field validity is justified by the algebraic argument.

## References

1. D. Kaur and P. Singh, *Decomposition of quandle rings of dihedral quandles*, arXiv:2206.03162 (first submitted 2022-06-07), https://arxiv.org/abs/2206.03162.
2. M. Elhamdadi, N. Fernando and B. Tsvelikhovskiy, *Ring Theoretic Aspects of Quandles*, arXiv:1805.05908 (2018), https://arxiv.org/abs/1805.05908.
3. B. Sangaré and L. Ta, *Idempotents, automorphism groups, and commutator widths of quandle algebras*, arXiv:2608.01550 (2026), especially Proposition 4.7, https://arxiv.org/html/2608.01550v1.
