# Dyadic-twist resilience of three-by-three prime-fiber Fourier minors

## Finding

**Theorem.** Let \(H\) be any finite abelian \(2\)-group, let \(p\ge3\) be an odd prime, and let \(G=H\times\mathbb Z/p\mathbb Z\). For three characters \((\chi_i,u_i)\in\widehat H\times\mathbb F_p\), \(i=0,1,2\), with pairwise distinct \(u_i\), and three points \((h_j,v_j)\in H\times\mathbb F_p\), \(j=0,1,2\), with pairwise distinct \(v_j\), the character-table submatrix
\[
M_{ij}=\chi_i(h_j)\exp(2\pi\mathrm i\,u_iv_j/p)
\]
has \(\det M\ne0\), regardless of the dyadic characters or point coordinates. Rows and columns are independently selected; **no principal-minor assumption is made**.

Equivalently, a signal supported on three points in three different prime-coordinate fibers cannot have Fourier transform zero at three characters in three different prime-coordinate fibers. This is a nonvanishing assertion on infinitely many non-prime groups despite their Fourier matrices having numerous other singular minors.

## Assumptions and scope

The group \(H\) may be trivial, cyclic, elementary abelian, or an arbitrary finite product of cyclic groups of powers of two. All character pairings are complex and unnormalized; multiplying rows or columns by nonzero scalars has no effect on nonsingularity. Distinctness is imposed only on the three \(\mathbb F_p\) coordinates on each side, not on the \(H\)-coordinates. There is no claim about four-by-four minors or about row or column triples with repeated prime-coordinate projections.

## Proof

Write \(\omega=\exp(2\pi\mathrm i/p)\). Choose a positive integer \(r\) such that every character value on \(H\) is a \(2^r\)-th root of unity, and put \(K=\mathbb Q(\zeta_{2^r})\). Because the conductors \(p\) and \(2^r\) are coprime, their cyclotomic fields are linearly disjoint. Hence the minimal polynomial of \(\omega\) over \(K\) is
\[
\Phi_p(X)=1+X+\dots+X^{p-1}.
\]

Expand the determinant as \(D=\sum_{\sigma\in S_3}\mathrm{sgn}(\sigma)\eta_\sigma\omega^{e_\sigma}\), where \(e_\sigma=\sum_{i=0}^2u_iv_{\sigma(i)}\pmod p\) and \(\eta_\sigma=\prod_{i=0}^2\chi_i(h_{\sigma(i)})\) is a root of unity of \(2\)-power order. Collect exponents: \(D=\sum_{e=0}^{p-1}C_e\omega^e\), with \(C_e\in\mathbb Z[\zeta_{2^r}]\).

Suppose \(D=0\). By the displayed minimal polynomial, all coefficients \(C_e\) must be equal. Let \(\mathfrak p\) be any prime ideal of \(\mathbb Z[\zeta_{2^r}]\) lying above \(2\). In its residue field, every \(2^r\)-th root of unity is \(1\), since \(X^{2^r}-1=(X-1)^{2^r}\) in characteristic two. The determinant signs also reduce to \(1\). Therefore \(C_e\bmod\mathfrak p\) is simply the parity of the number of the six exponents \(e_\sigma\) equal to \(e\). All these parities are the same because the \(C_e\) are equal; their sum is the parity of six, namely zero. Since \(p\) is odd, their common parity is zero. **Thus every exponent must occur an even number of times.**

Equality patterns of the six exponents are unchanged by translating the three \(u_i\), translating the three \(v_j\), and multiplying either coordinate triple by a nonzero field scalar. Thus we can normalize \((u_0,u_1,u_2)=(0,1,t)\) and \((v_0,v_1,v_2)=(0,1,s)\) with \(s,t\in\mathbb F_p\setminus\{0,1\}\). Direct enumeration of the six permutations gives the three even-permutation exponents
\[
\{1+ts,\ s,\ t\},
\]
and the three odd-permutation exponents
\[
\{s+t,\ ts,\ 1\}.
\]
Here the labels 'even' and 'odd' refer to permutation sign, not arithmetic parity in \(\mathbb F_p\).

Neither \(s\) nor \(t\) equals any of \(s+t\), \(ts\), or \(1\): every such equality would force \(s=0\), \(t=0\), \(s=1\), or \(t=1\), contrary to the normalization. If \(s\ne t\), each of \(s\) and \(t\) occurs at least once among the three even-permutation exponents and cannot occur in the odd list. There is only one further even-permutation exponent, \(1+st\), so these two different values cannot both have even multiplicity. Hence the all-even-multiplicity condition forces \(s=t\).

For \(s=t\), the six exponents are
\[
\{1+t^2,t,t\}\quad\text{and}\quad\{2t,t^2,1\}.
\]
The two occurrences of \(t\) contribute an even multiplicity and may be discarded modulo two. But \(1+t^2\) is different from each of \(2t\), \(t^2\), and \(1\): these equalities would imply respectively \((t-1)^2=0\), \(1=0\), or \(t^2=0\). Hence it occurs an odd number of times in the remaining four-element multiset, a contradiction. The determinant cannot vanish. \(\square\)

The normalization step uses only equality patterns: translating the \(u_i\) or \(v_j\) adds a permutation-independent constant to every exponent, while a nonzero scaling multiplies all exponents by one field unit.

## Verification

The proof is valid for every odd prime and every finite abelian \(2\)-group, without finite enumeration. The standalone source `verify.cpp` independently forms cyclotomic coefficient vectors over \(\mathbb Z[\mathrm i]\) for \(H=C_4\), and over integer sign coefficients for \(H=C_2\times C_2\). It enumerates all row and column triples containing the identity with distinct prime projections for \(p=3,5,7\), and also for \(p=11\) in the cyclic-four case. Every such determinant is nonzero by exact equality testing of its \(p\) cyclotomic coefficients. It separately checks the combinatorial parity obstruction for every normalized pair at each prime in the printed finite list through \(103\). These calculations are **finite consistency tests** only; the cyclotomic and parity argument above establishes the unrestricted claim.

Compile and run with `g++ -std=c++17 -O2 verify.cpp -o verify && ./verify`; no external arithmetic package is needed. The finite run outcomes and scope are reported in `VERIFICATION.md`.

## Relationship to prior work

Chebotarev's theorem and Tao's 2003 account show that every square minor of the Fourier matrix of prime order is invertible, but their group has no dyadic factor. Alexeev–Cahill–Mixon analyze full-spark Fourier row selections and prime-power configurations; full spark on a prime component does not itself imply stability of nonprincipal minors under arbitrary dyadic phase twists. Krahmer–Pfander–Rashkov discuss uncertainty on finite abelian groups and the subgroup-induced failure of blanket nonvanishing at composite orders. Zhou (2025) proves results concerning **principal** minors of certain tensor-product Fourier matrices; the independent row/column choices here are not covered by the principal-minor statements. Earlier exact three-by-three classifications for \(\mathbb Z/(2p)\), \(\mathbb Z/(p^2)\), and \(\mathbb F_p^2\) do not imply the claim for an arbitrary dyadic factor \(H\).

## Limitations

This is a partial minor-nonvanishing theorem, not a full spark result for an entire row-selected matrix. It does not classify singular minors when prime-coordinate projections collide, does not extend to nonabelian dyadic factors, and does not establish priority against every unindexed treatment of cyclotomic character tables. The proof's modulus-two collapse is essential to the argument as written. Independent mathematical validation has not been performed.

## References

- T. Tao, *An uncertainty principle for cyclic groups of prime order*, arXiv:math/0308286v1, publicly posted 2003-08-29, https://arxiv.org/abs/math/0308286.
- F. Krahmer, G. Pfander, P. Rashkov, *Uncertainty in time-frequency representations on finite Abelian groups and applications*, arXiv:math/0611493v1, posted 2006-11-16, https://arxiv.org/abs/math/0611493.
- B. Alexeev, J. Cahill, D. G. Mixon, *Full Spark Frames*, arXiv:1110.3548v1, posted 2011-10-17, https://arxiv.org/abs/1110.3548.
- W. Zhou, *Principal Non-singularity of Fourier Matrices on \(\mathbb Z_p\times\mathbb Z_q\) and \(\mathbb Z_2^k\times\mathbb Z_q\)*, arXiv:2505.01189v1, posted 2025-05-02, https://arxiv.org/abs/2505.01189.
- Published exact classification, *Singular three-by-three Fourier minors on even semiprime cycles*, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-singular-three-by-three-fourier-minors-on-even-semiprime-cycles--8f025c6183d3.
- Published exact classification, *All singular three-by-three minors of prime-square Fourier matrices*, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-all-singular-three-by-three-minors-of-prime-square-fourier-matri--feb52ea6712b.
