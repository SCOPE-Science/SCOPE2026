# Sharp three-block digit-sum density with single-zero separators

## Finding
Let \(s_2(n)\) count the ones in the binary expansion of \(n\), and for each positive integer \(t\) define the natural density
\[
c_t=\lim_{N\to\infty}\frac{1}{N}\bigl|\{0\le n<N:s_2(n+t)\ge s_2(n)\}\bigr|.
\]
For any integers \(a,b,c\ge1\), let \(t=t(a,b,c)\) be the integer whose binary expansion, from most to least significant digit, is \(1^c0\,1^b0\,1^a\), with exactly one zero between consecutive one-blocks. Put \(A=4^{-a}\), \(B=4^{-b}\), \(C=4^{-c}\). Then
\[
\boxed{c_{t(a,b,c)}=\frac{115+32A+8B+32C+16AB-8AC+16BC+32ABC}{216}.}
\]
For each of its three integer arguments, the density strictly decreases as that argument increases, holding the other two fixed. Consequently
\[
\boxed{c_{t(a,b,c)}>\frac{115}{216},\qquad \inf_{a,b,c\ge1}c_{t(a,b,c)}=\frac{115}{216}.}
\]
The infimum is approached if and only if all three block lengths tend to infinity. For instance, \(c_{t(2,2,2)}=567/1024<5/9\), so the sharp two-block lower bound \(5/9\) does not extend to this three-block family.

## Assumptions and scope
All lengths are positive integers; the two intervening zero runs have length exactly one, and there are no other non-leading zeros in the binary representation. Natural density is over \(n\ge0\). The result describes weak increase of binary digit sum, not strict increase. The theorem does not cover three blocks with zero gaps longer than one, nor all three-block integers.

## Proof
Write \(w=a+b+c\) and \(L=w+2\). In binary addition of an integer \(n\) to \(t\), each binary input digit of \(n\) is asymptotically an independent fair bit. Starting with carry zero, let \(K\) count the outgoing carries over all digit columns (including any columns above the highest nonzero digit of \(t\)). The standard bit identity gives
\[
s_2(n+t)-s_2(n)=s_2(t)-K=w-K.
\]
The identity follows columnwise from \(n_i+t_i+e_i=o_i+2e_{i+1}\), whose sum over all columns is \(s_2(n)+s_2(t)+\sum e_i=s_2(n+t)+2\sum e_{i+1}\). Carries are almost surely finite. Therefore \(c_t=\Pr(K\le w)\).

For each fixed digit \(d\in\{0,1\}\) of \(t\), the probability-weighted outgoing carry polynomial, from incoming carry states zero and one, has transition matrix
\[
M_1(u)=\begin{pmatrix}1/2&u/2\\0&u\end{pmatrix},\qquad
M_0(u)=\begin{pmatrix}1&0\\1/2&u/2\end{pmatrix}.
\]
Every outgoing carry one contributes one power of \(u\). After the \(L\) nonzero-length digit columns of \(t\), define polynomials \(P(u),R(u)\) by
\[
(P(u),R(u))=(1,0)M_1(u)^aM_0(u)M_1(u)^bM_0(u)M_1(u)^c.
\]
Above those columns, all digits of \(t\) vanish. From outgoing carry zero there are no additional carries. From outgoing carry one, the number of additional carries has geometric law \(\Pr(J=j)=2^{-j-1}\) for \(j\ge0\), and hence probability generating function \(1/(2-u)\). Thus the exact generating function of \(K\) is
\[
G(u)=P(u)+\frac{R(u)}{2-u}.
\]
The polynomial \(P\) has degree at most \(w\): ending with carry zero at the final (one-)bit forces the preceding and final outgoing carries to be zero. The polynomial \(R\) has degree at most \(w+2\). Its coefficient of \(u^{w+2}\) is precisely \(1/8\), because the only way to carry from all \(L\) columns is to initiate carry with probability \(1/2\) at the low bit and maintain it through each of the two zero separators with conditional probability \(1/2\); all one-bits thereafter propagate it surely.

Writing \(R(u)=\sum_{j=0}^{w+2}r_ju^j\) and summing the geometric tail gives the exact identity
\[
\Pr(K>w)=\sum_{j\le w+1}r_j2^{-(w+1-j)}+r_{w+2}=\frac{R(2)}{2^{w+1}}-r_{w+2}.
\]
Consequently \(c_t=9/8-R(2)/2^{w+1}\).

Introduce \(X=2^a\), \(Y=2^b\), \(Z=2^c\). Directly raising the upper-triangular matrix \(M_1(2)\) to positive integer powers yields
\[
U(X):=M_1(2)^a=\begin{pmatrix}X^{-1}&\frac23(X-X^{-1})\\0&X\end{pmatrix},
\qquad V:=M_0(2)=\begin{pmatrix}1&0\\1/2&1\end{pmatrix},
\]
with the same \(U\) formula for \(Y,Z\). Thus \(R(2)\) is the upper-right entry of \(U(X)VU(Y)VU(Z)\). Exact matrix multiplication gives
\[
\frac{27XYZ}{2}R(2)
=16X^2Y^2Z^2-4X^2Y^2-X^2Z^2-2X^2-4Y^2Z^2+Y^2-2Z^2-4.
\]
Substituting this identity into \(9/8-R(2)/(2XYZ)\) and putting \(A=X^{-2}\), \(B=Y^{-2}\), \(C=Z^{-2}\) yields the displayed formula.

For strict monotonicity, the numerator's partial derivatives in the independent real variables \(A,B,C\) are respectively
\[
32+16B-8C+32BC,\quad 8+16A+16C+32AC,\quad 32+16B-8A+32AB.
\]
Each is strictly positive on \(0<A,B,C\le1/4\). Therefore increasing any block length strictly reduces \(c_t\). Taking all lengths to infinity sends \(A,B,C\) to zero and gives exactly \(115/216\). Conversely, because the derivatives remain strictly positive even when other variables vanish, approaching this infimum requires each variable to vanish. The example follows by substituting \(A=B=C=1/16\).

## Verification
The accompanying `verify.py` is executable using only Python's standard library. First it checks the matrix identity at eight exact rational interpolation points. After multiplication by \(XYZ\), both sides are multiaffine in the three variables \(X^2,Y^2,Z^2\); agreement at two distinct values of each variable proves the displayed polynomial identity for all nonzero \(X,Y,Z\). Next it compares the derived density to exact rational transfer matrices for all \(216\) triples of lengths from one through six. Finally, it independently enumerates all \(2^L\) low-bit residues for each of \(27\) triples with lengths from one through three, summing the exact upper-carry geometric tail. These are supplementary and independently motivated checks; the general result is proved algebraically above.

## Relationship to prior work
Drmota, Kauers and Spiegelhofer (2015 preprint, 2016 journal) introduced the digit-sum densities in this problem and established the relevant carry recurrences and asymptotic results. Sobolewski and Spiegelhofer (2024 preprint) proved \(c_t>5/9\) when the binary expansion of \(t\) has at most two one-blocks. Their Conjecture 13 predicts an extremal \(N\)-block limit; their Proposition 16 evaluates its \(N=3\) value as \(115/216\), but their theorem does not establish this bound for finite three-block shifts, and their discussion explicitly notes that block-length monotonicity fails for some longer patterns. The present result proves the conjectured sharp bound, strict monotonicity, and a fully explicit finite-parameter formula for the canonical three-block slice with the two shortest possible zero gaps. Cheng (2026) proved \(c_t>1/2\) for every positive integer \(t\); that general positivity theorem does not specify this sharp three-block constant, the formula, or its block-length dependence.

## Limitations
This is not a proof of the full three-block Conjecture 13 when the two zero gaps are arbitrary. It does not assert any analogous block-length monotonicity for more blocks. The limiting constant \(115/216\) itself is known from Sobolewski and Spiegelhofer; the new content is its rigorous finite-word extremal role on the specified natural slice and the explicit three-variable correction polynomial. An equivalent finite-parameter specialization could exist in unlocated literature. No independent mathematical audit has been performed.

## References
1. M. Drmota, M. Kauers, L. Spiegelhofer, *On a Conjecture of Cusick Concerning the Sum of Digits of n and n + t*, arXiv:1509.08623, first public version 2015-09-29; SIAM J. Discrete Math. 30 (2016), 621–649. https://arxiv.org/abs/1509.08623
2. B. Sobolewski, L. Spiegelhofer, *Decomposing the sum-of-digits correlation measure*, arXiv:2411.07779, first public version 2024-11-12, §§5.3, 6.1, Conjecture 13, Proposition 16. https://arxiv.org/abs/2411.07779
3. K. Cheng, *A first-exit proof of Cusick's sum-of-digits conjecture*, arXiv:2606.23398, first public version 2026-06-22, Theorem 1.1. https://arxiv.org/abs/2606.23398
