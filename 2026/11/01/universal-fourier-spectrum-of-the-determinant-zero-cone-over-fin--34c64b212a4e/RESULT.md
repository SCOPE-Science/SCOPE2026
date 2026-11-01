# Universal Fourier spectrum of the determinant-zero cone over finite chain rings

## Finding

Let \(R\) be any finite **commutative** chain ring, with maximal ideal \((\pi)\), residue-field cardinality \(q\ge 2\), and nilpotency length \(k\ge 1\), so that \(|R|=q^k\). On the additive group \(G=M_2(R)\), let \(C=\{X\in G:\det X=0\}\) (determinant **equal to zero in the ring**, not merely nonunit). Let \(T_C f=\mathbf1_C*f\), without normalization, on \(\ell^2(G)\). The Fourier character at \(M\in G\) is \(X\mapsto\psi(\langle M,X\rangle)\), with \(\langle M,X\rangle=\sum_{i,j}M_{ij}X_{ij}\) and a generating additive character \(\psi\) of \(R\). Reversing the character sign has no effect on the eigenvalues below.

Put \(B_q=(q-1)(q+1)^2\), \(L=\lfloor k/2\rfloor\), and
\[
\mathcal R_{q,k}=q^{4(k-L)}+B_q\sum_{j=0}^{L-1}q^{3k-2-2j}.
\]
The sum is empty when \(L=0\). **The exact rank** and nullity of the convolution operator are
\[
\operatorname{rank}T_C=\mathcal R_{q,k},\qquad
\dim\ker T_C=q^{4k}-\mathcal R_{q,k}.
\]
This rank and the **complete eigenvalue multiset** depend only on \((q,k)\), not on the characteristic or isomorphism class of the finite chain ring. The multiset, with multiplicities, is:

* The top eigenvalue \(q^{3k}+q^{3k-1}-q^{2k-1}\), multiplicity one.
* For each integer \(0\le v\le k-1\), the strictly positive eigenvalue \(q^{2k-1}(q^{v+1}-1)\), multiplicity \(B_q q^{3(k-v-1)}\).
* The single negative eigenvalue \(-q^{2k-1}\), multiplicity \(\mathcal R_{q,k}-1-B_q\sum_{i=0}^{k-1}q^{3i}\).
* Eigenvalue \(0\), multiplicity \(q^{4k}-\mathcal R_{q,k}\).

Thus there are exactly \(k+3\) distinct eigenvalues for \(k\ge2\) and exactly three for \(k=1\); no zero eigenvalue occurs at \(k=1\). For fixed \(q\), the Fourier-support fraction \(\mathcal R_{q,k}/q^{4k}\) tends to zero exponentially in \(k\), even though every field-level operator \((k=1)\) is invertible.

**Fourier-null classification.** For any nonzero \(M\in G\), write \(M=\pi^v M_0\), where \(0\le v<k\), and regard the primitive matrix \(M_0\) as an element of \(M_2(R/(\pi^{k-v}))\). Put \(d=\nu_{k-v}(\det M_0)\), with \(\nu_r(0)=r\) and \(\nu_r(a)\) the \(\pi\)-valuation truncated at \(r\). The unnormalized Fourier multiplier is exactly
\[
\widehat{\mathbf1_C}(M)=
\begin{cases}
0, & d+2v<k-1,\\
-q^{2k-1}, & d+2v\ge k-1\text{ and }d+v\le k-1,\\
q^{2k-1}(q^{v+1}-1), & d+v\ge k.
\end{cases}
\]
At \(M=0\), it equals the top eigenvalue. In particular, the kernel is the span of precisely those additive characters with \(d+2v<k-1\). The three cases are disjoint and exhaustive.

## Assumptions and scope

Every ring here is finite, associative, unital, **commutative**, and a chain ring. The maximal ideal has successive quotients of size \(q\), and \(\pi^k=0\) but \(\pi^{k-1}\ne0\) unless \(k=1\), when the ring is a field. No restriction to odd characteristic is needed: characteristic two and noncyclic additive groups are included. Any generating additive character gives a perfect pairing, hence the same spectrum. The Fourier transform is unnormalized, \(\widehat f(M)=\sum_{X\in G}f(X)\psi(-\langle M,X\rangle)\). The ring determinant zero fibre is not the full set of noninvertible matrices when \(k>1\).

## Proof

**1. Generating characters and orthogonality.** A finite commutative chain ring is Frobenius. Directly, its socle \((\pi^{k-1})\) is a minimal nonzero ideal, and a nontrivial additive character of that socle extends to the finite additive group of \(R\). The extension is nontrivial on every nonzero ideal (each contains the socle). Fix such a character \(\psi\). For every quotient \(R_r=R/(\pi^r)\), \(1\le r\le k\), the function \(\psi_r(x)=\psi(\pi^{k-r}\widetilde x)\) is well-defined and generating. Character orthogonality holds over \(R_r\).

**2. Exact multiplier before cancellation.** For any \(a\in R_r\) define the ring Ramanujan sum
\[
c_r(a)=\sum_{u\in R_r^\times}\psi_r(ua)
=q^r\mathbf1_{\{a=0\}}-q^{r-1}\mathbf1_{\{a\in(\pi^{r-1})\}}.
\]
Thus its three possibilities are \((q-1)q^{r-1}\), \(-q^{r-1}\), and \(0\), according as the valuation of \(a\) is \(r\), \(r-1\), or smaller. To impose \(\det X=0\), insert the character identity
\[
\mathbf1_{\{\det X=0\}}=q^{-k}\sum_{s\in R}\psi(s\det X).
\]
For \(s\ne0\), write \(s=\pi^j u\) for a unique \(0\le j<k\) and a unit \(u\) of \(R_{k-j}\). The sum over \(X\in M_2(R)\) vanishes unless every entry of \(M\) is divisible by \(\pi^j\). If this divisibility holds, each matrix entry contributes \(q^j\) lifts from \(R_{k-j}\), and the two hyperbolic pairs \((a,d)\) and \((b,c)\) satisfy
\[
\sum_{a,d\in R_{k-j}}\psi_{k-j}(uad-Aa-Dd)
=q^{k-j}\psi_{k-j}(-AD/u),
\]
with the analogous identity for \(-ubc\). Therefore the two pairs contribute \(q^{2(k-j)}\psi_{k-j}(-\det(M/\pi^j)/u)\). Inversion and negation permute the unit group. The \(s=0\) term is the ordinary additive orthogonality term. Consequently, with each quotient determinant interpreted modulo \(\pi^{k-j}\),
\[
\widehat{\mathbf1_C}(M)
=q^{3k}\mathbf1_{\{M=0\}}
+\sum_{j=0}^{k-1}q^{k+2j}\mathbf1_{\{M\in\pi^jG\}}
\,c_{k-j}\bigl(\det(M/\pi^j)\bigr).
\tag{1}
\]
No use is made of dividing by two, or of a quadratic Gauss-sum square-root formula, so this derivation works over every finite commutative chain ring.

**3. Cancellation lemma and the three nonzero-frequency cases.** Let \(M\ne0\) have common entry valuation \(v\), and let \(M_0,d\) be as above. For \(0\le j\le v\), the valuation of the relevant determinant is the truncation of \(d+2(v-j)\) at \(k-j\). Thus the \(j\)-summand of (1) is nonzero exactly when
\[
j\le d+2v-k+1.
\]
If the right-hand side is negative, all summands vanish. Otherwise, the summands with strictly smaller \(j\) are \((q-1)q^{2k+j-1}\), while at equality the summand is \(-q^{2k+j-1}\). If equality is reached by \(j\le v\), the finite sum equals
\[
(q-1)q^{2k-1}\sum_{i=0}^{j-1}q^i-q^{2k+j-1}=-q^{2k-1}.
\]
If equality lies above \(v\), all \(v+1\) available terms are positive, and sum to \(q^{2k-1}(q^{v+1}-1)\). These are precisely the claimed cases. At the zero frequency, (1) sums to \(q^{3k}+q^{3k-1}-q^{2k-1}\), also equal to \(|C|\).

**4. Spectral multiplicities.** Over the residue field, the number of nonzero rank-one \(2\times2\) matrices is
\[
B_q=\frac{(q^2-1)^2}{q-1}=(q-1)(q+1)^2.
\]
Fix \(v\) and put \(r=k-v\). The positive eigenvalue indexed by \(v\) occurs exactly when the primitive \(M_0\) has \(\det M_0=0\) in \(R_r\). The reduction of \(M_0\) must then have rank one. At each such reduction, a partial derivative of the determinant is a unit, so each successive digit of the determinant cuts the \(q^4\) possible lifts to exactly \(q^3\) lifts. Hence the count is \(B_q q^{3(r-1)}\), yielding every stated positive multiplicity. The top eigenvalue belongs only to \(M=0\).

**5. Exact rank by disjoint valuation strata.** For \(M=\pi^vM_0\) primitive modulo \(\pi^{k-v}\), Fourier nonvanishing is equivalent to \(\det M_0\) being divisible by \(\pi^{t_v}\), where \(t_v=\max(0,k-1-2v)\). If \(t_v\ge1\), the reduced matrix must have rank one and the number of such primitive matrices is
\[
B_q q^{4(k-v-1)-(t_v-1)}=B_q q^{3k-2-2v}.
\]
If \(t_v=0\), all primitive matrices count, giving \(q^{4(k-v)}-q^{4(k-v-1)}\). The transition occurs at \(v=L=\lfloor k/2\rfloor\). Summing over \(0\le v<L\), then telescoping the high-valuation terms \(L\le v<k\) and adding the zero frequency, gives exactly \(\mathcal R_{q,k}\). The negative multiplicity follows by subtracting the positive and top multiplicities from this rank, and the zero multiplicity by subtracting rank from \(|G|=q^{4k}\). All multiplicities are nonnegative by these direct counts. Fourier characters form a basis, so these exhaust the spectrum and nullspace.

## Verification

The standalone `check_determinantal.py` performs **exact** character computations, not floating-point zero tests. On cyclic prime-power rings, it computes the full determinant-zero fibre and tests every frequency by reducing integer root-of-unity coefficient vectors modulo the relevant prime-power cyclotomic polynomial. It additionally computes all coefficients over the noncyclic additive group of \(\mathbb F_2[t]/(t^2)\), using its explicit generating character. The completed runs were:

```
EXACT_CYCLIC_OK 2 1 size 16 cone 10 rank 16
EXACT_CYCLIC_OK 2 2 size 256 cone 88 rank 160
EXACT_CYCLIC_OK 2 3 size 4096 cone 736 rank 1408
EXACT_CYCLIC_OK 3 1 size 81 cone 33 rank 81
EXACT_CYCLIC_OK 3 2 size 6561 cone 945 rank 2673
EXACT_NONCYCLIC_OK F2[t]/(t^2) size 256 cone 88 rank 160
ALL_EXACT_DETERMINANTAL_CHECKS_OK
```

Every finite test enumerates **all** frequencies, and the theorem for unbounded \(q,k\) is proved by the preceding character calculation and counting, not inferred from the tests. Reproduce with `python3 check_determinantal.py` (Python standard library only).

## Relationship to prior work

Iosevich and Koh (arXiv:0804.4505v1) develop finite-field Fourier analysis of quadratic surfaces and character-sum methods. Their field-level nonzero quadratic shells and restriction estimates do not give the determinant-zero cone spectrum for arbitrary finite chain-ring lengths. Maeda (arXiv:1303.5188v1) studies Gauss sums weighted by irreducible group characters on the invertible matrix group over prime-power rings, rather than the additive Fourier transform of the zero-determinant fibre on the entire matrix ring. Xu, Kan, and Han (arXiv:2509.11681v1) study Fourier-dual rank partitions of chain-ring matrix spaces and prove nonreflexivity of rank-weight partitions; their stated theorems neither give the determinant-equals-zero fibre multipliers nor the above rank, though their broader framework is relevant. These comparisons do not establish absolute historical priority.

## Limitations

The claim is restricted to two-by-two determinant-zero fibres on finite commutative **chain** rings, with unnormalized additive convolution. It does not claim the same formula for determinant nonunits, higher square matrices, arbitrary finite rings, multiplicative-group convolution, or an independent audit. The character-sum computation is elementary in principle; an implicit specialization of older quadratic-form, local zeta, or matrix-association literature remains possible. Source comparison was bounded and cannot establish uniqueness. No claims about analytic restriction bounds or arbitrary matrix-rank association schemes are made.

## References

1. Alex Iosevich and Doowon Koh, *Extension theorems for the Fourier transform associated with non-degenerate quadratic surfaces in vector spaces over finite fields*, first public arXiv version 2008-04-28, arXiv:0804.4505v1, https://arxiv.org/html/0804.4505v1.
2. Taiki Maeda, *Gauss Sums on GL2(Z/p^lZ)*, first public arXiv version 2013-03-21, arXiv:1303.5188v1, https://arxiv.org/abs/1303.5188.
3. Yang Xu, Haibin Kan, and Guangyue Han, *Reflexive Partitions Induced by Rank Support and Non-Reflexive Partitions Induced by Rank Weight*, first public arXiv version 2025-09-15, arXiv:2509.11681v1, https://arxiv.org/abs/2509.11681.
