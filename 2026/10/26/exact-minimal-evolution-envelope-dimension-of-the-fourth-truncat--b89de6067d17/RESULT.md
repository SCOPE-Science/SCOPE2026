# Exact minimal evolution-envelope dimension of the fourth truncated polynomial algebra over \(\mathbb F_2\) and \(\mathbb F_3\)

## Finding
For either \(K=\mathbb F_2\) or \(K=\mathbb F_3\), put \(A=K[t]/(t^4)\). Among all finite-dimensional evolution \(K\)-algebras containing an isomorphic copy of \(A\) as an algebra (equivalently, as an ideal of an evolution envelope), the smallest possible dimension is **eight**:
\[
\operatorname{edim}_K(K[t]/(t^4))=8\qquad(K=\mathbb F_2,\mathbb F_3).
\]
In each field an explicit eight-dimensional envelope is supplied below. In particular, the seven-dimensional value attained over sufficiently large fields does not hold for either of these two prime fields.

## Assumptions and scope
An evolution algebra is a commutative, not necessarily associative, algebra with a natural basis \(f_1,\ldots,f_m\) such that \(f_i f_j=0\) for distinct indices. An embedding is an injective \(K\)-linear algebra homomorphism. An *evolution envelope* of \(A\) is an evolution algebra \(E\) equipped with an embedding \(\Phi:A\hookrightarrow E\) satisfying \(E^2\subseteq\Phi(A)\); thus \(\Phi(A)\) is automatically an ideal. The minimum over all embeddings equals the minimum over envelopes, by projecting all natural-basis squares onto the embedded algebra (see the first reference, Proposition 3.2).

We use the basis \((1,t,t^2,t^3)\) of \(A\) and write \(a=(a_0,a_1,a_2,a_3)\). A four-digit word \(u_0u_1u_2u_3\) over \(K\) represents the linear form \(\ell_u(a)=\sum_{i=0}^3u_i a_i\), or an algebra element \(\sum_{i=0}^3u_i t^i\), as specified by its column. There is no assertion here for larger finite fields or higher truncation degree.

## Proof
**Step 1: the rank-one symmetric bilinear reduction, valid in characteristic two.** Let \(m\) be the dimension of any evolution envelope of a unital commutative algebra \(A\). Write \(\Phi(a)=\sum_{j=1}^m\ell_j(a)f_j\) and \(f_j^2=\Phi(v_j)\). Then
\[
 ab=\sum_{j=1}^m \ell_j(a)\ell_j(b)v_j\qquad(a,b\in A).
\]
Conversely, given such an identity, unitality makes \(L:A\longrightarrow K^m\), \(L(a)=(\ell_j(a))_j\), injective: \(L(a)=0\) implies \(a=a1=0\). Define an evolution multiplication on \(K^m\) by \(f_j^2=L(v_j)\) and \(f_if_j=0\) for \(i\ne j\). The identity gives \(L(a)L(b)=L(ab)\), and every basis square lies in \(L(A)\), yielding an envelope. This argument uses the entire multiplication tensor, not the squaring map, and is valid even when \(\operatorname{char}K=2\). Hence \(\operatorname{edim}_K(A)\) equals the least number of terms in the displayed symmetric-factor bilinear identity.

**Step 2: finite matrix reformulation.** Let \(S\) be the ten-dimensional space of symmetric \(4\times4\) matrices. For \(k=0,1,2,3\), define \(T_k\in S\) by \((T_k)_{ij}=1\) when \(i+j=k\), and zero otherwise (indices start at zero). The coordinate of \(ab\) on \(t^k\) is \(a^{\mathsf T}T_k b\). For \(u\in K^4\), write \(R(u)=uu^{\mathsf T}\). An \(m\)-term factorization exists exactly when there are \(m\) vectors \(u_j\) with
\[
 \operatorname{span}_K\{T_0,T_1,T_2,T_3\}\subseteq
 \operatorname{span}_K\{R(u_1),\ldots,R(u_m)\}.
\]
Zero forms can be omitted, and forms proportional by a nonzero scalar can be combined into one summand (absorbing the square of the scalar into its output vector). Thus for \(K=\mathbb F_p\), \(p=2,3\), it suffices to test subsets of normalized nonzero forms, whose first nonzero coefficient is 1. There are \((p^4-1)/(p-1)\) forms: fifteen for \(p=2\), forty for \(p=3\). If a factorization of length at most seven existed, a seven-element subset containing the chosen forms would work.

**Step 3: exhaustive seven-term obstruction with a six-coordinate pruning certificate.** Order the ten matrix entries as \((00,01,02,03,11,12,13,22,23,33)\). The quotient \(S/\operatorname{span}(T_0,\ldots,T_3)\) is represented by the six coordinates
\[
 Q(M)=(M_{02}-M_{11},\ M_{03}-M_{12},\ M_{13},\ M_{22},\ M_{23},\ M_{33}).
\]
For \(u=(a,b,c,d)\) this is
\[
 Q(R(u))=(ac-b^2,ad-bc,bd,c^2,cd,d^2).
\]
If seven rank-one matrices span all four \(T_k\), their six-coordinate quotient images have rank at most three, because the kernel of the quotient on their span has dimension at least four. The verifier enumerates **all** increasing seven-element subsets of normalized forms whose quotient rank is at most three; any branch reaching rank four is soundly pruned by monotonicity. It then tests containment of all four \(T_k\) using exact Gaussian elimination in \(\mathbb F_p\). For \(p=2\), among the \(\binom{15}{7}=6435\) seven-element subsets, exactly one passes the necessary quotient-rank bound and fails the final containment test. For \(p=3\), among the \(\binom{40}{7}=18643560\) subsets, exactly 2355 pass the quotient bound; all fail containment. Consequently \(\operatorname{edim}_K(A)\ge8\) in both cases. This is a complete finite exhaustion, not a randomized search or an extrapolation.

**Step 4: explicit eight-term upper certificates.** In the following tables each row gives a coefficient word for \(\ell_j\) followed by a coefficient word for \(v_j\). Interpret words from left to right in basis order \((1,t,t^2,t^3)\):

| \(j\) | \(\mathbb F_2:\ell_j\) | \(\mathbb F_2:v_j\) | \(\mathbb F_3:\ell_j\) | \(\mathbb F_3:v_j\) |
|---:|:---:|:---:|:---:|:---:|
|1|1000|1111|0001|2122|
|2|0100|0111|1210|0110|
|3|1100|0100|1100|0010|
|4|0010|0011|1110|0101|
|5|1010|0010|1002|2120|
|6|0110|0001|0120|0221|
|7|0001|0001|1220|0201|
|8|1001|0001|1001|2121|

For each field, direct entrywise multiplication of symmetric matrices gives
\[
 T_k=\sum_{j=1}^8 (v_j)_k\,R(u_j),\qquad k=0,1,2,3,
\]
where \(u_j\) is the row word for \(\ell_j\). Thus the eight-term factorization of Step 1 holds. The eight forms span the four-dimensional dual of \(A\), so \(L\) is injective. Define the ambient eight-dimensional evolution algebra using the multiplication \(f_j^2=L(v_j)\); it contains the desired ideal \(L(A)\). This proves \(\operatorname{edim}_K(A)\le8\) and completes the theorem.

## Verification
Run `python3 verify.py` from the same directory. The program uses only Python's standard library and arithmetic modulo 2 or 3. It enumerates all normalized projective forms, performs the exhaustive rank-pruned seven-form obstruction, verifies the eight-form coefficient identities by modular Gaussian elimination, checks injectivity, and exhaustively checks the resulting bilinear multiplication on all \(16^2=256\) input pairs over \(\mathbb F_2\) and all \(81^2=6561\) pairs over \(\mathbb F_3\). Expected lines begin `FIELD=2: VERIFY_OK` and `FIELD=3: VERIFY_OK`. The exhaustive multiplication test is finite because the theorem itself concerns these finite algebras; it is not used as an infinite-field argument.

## Relationship to prior work
Costoya, Fernández Ouaridi and Viruel establish the evolution-envelope framework for all fields and the simultaneous-Waring interpretation when the characteristic is not 2. Their Theorem 5.6 gives \(2n-1\) as the truncated-polynomial evolution dimension provided the characteristic is odd and the field has at least \(2n-1\) distinct elements. For \(n=4\), Remark 5.4 explicitly observes by computation that the Waring rank over \(\mathbb F_3\) exceeds seven; it does not specify the exact minimum. The present eight-term certificate determines that exact value and independently supplies a complete obstruction. The characteristic-two assertion cannot be deduced from their Waring-squaring argument, because the squaring map loses cross terms in characteristic two; the bilinear reduction above handles that loss explicitly. The general Alder–Strassen lower bound from tensor complexity only yields seven here, not the strict lower bound of eight.

## Limitations
The result does not determine evolution dimensions for \(\mathbb F_4\), \(\mathbb F_5\), or arbitrary truncation length, nor classify the isomorphism types of all minimal envelopes. No claim is made about ordinary (unrestricted) multiplication-tensor rank as distinct from the symmetric-factor rank relevant to evolution envelopes. Originality against unpublished or unindexed work remains uncertain; the finite-field claims and certificates are supplied for checking.

## References
1. C. Costoya, A. Fernández Ouaridi, A. Viruel, *Commutative algebras are ideals of evolution algebras*, arXiv:2609.32784v1 (first made public 2026-09-26), especially Proposition 3.2, Theorem 3.5, §4, Remark 5.4, Theorem 5.6. https://arxiv.org/html/2609.32784
2. M. Bläser, *A Complete Characterization of the Algebras of Minimal Bilinear Complexity*, SIAM Journal on Computing 34 (2005), 277–298, DOI:10.1137/S0097539703438277. Provides general bilinear rank context, not the symmetric envelope classification established here.
