# Exact odd-sequence lengths for the Mersenne-power binary Collatz family
## Finding
Let \(M_1=x^2+x+1\). Consider the binary-polynomial Collatz transformation of Gallardo and Rahavandrainy: after an odd polynomial \(F\in\mathbb F_2[x]\), form \(1+M_1F\) and divide out the full powers of \(x\) and \(x+1\) to obtain the next odd polynomial.

For every integer \(R\ge1\) and every integer \(j\) with
\[
0\le j\le 2^{R-1}-1,
\]
the odd sequence associated with
\[
A=M_1^{2^R-j}+1
\]
has exactly \(j+1\) terms. Thus Conjecture 3.1 of Gallardo--Rahavandrainy is true.

A stronger transition formula explains the length. Put \(y=M_1\) and \(z=y+1=x(x+1)\). For \(n\ge1\), define the first odd polynomial
\[
B_n=\frac{y^n+1}{z^{2^{\nu_2(n)}}}.
\]
If \(n\) is not a power of two, write
\[
q=2^{\nu_2(n)},\qquad u=\frac nq,\qquad k=2^{\nu_2(u-1)},\qquad t=q(k-1).
\]
Then exactly \(t\) odd Collatz steps send \(B_n\) to \(B_{n+t}\); the first \(t-1\) steps strip exactly one factor \(z\).

## Assumptions and scope
All polynomial arithmetic is in \(\mathbb F_2[x]\). A polynomial is odd when it is coprime to \(x(x+1)\). Because \(y=x^2+x+1\) and \(z=y+1=x(x+1)\), any polynomial in \(y\) has equal \(x\)- and \(x+1\)-valuations whenever it is divisible by \(z\): if \(P(y)=z^mQ(y)\) with \(Q(1)=1\), then both valuations are exactly \(m\). Therefore the source transformation, restricted to polynomials in \(y\), is exactly the operation of taking the odd part of \(1+yF\) with respect to powers of \(z\).

For \(n=2^a u\) with \(u\) odd, characteristic two gives
\[
y^n+1=z^{2^a}B_n,
\]
and \(B_n(1)=1\), so \(B_n\) is indeed odd. If \(n\) is a power of two, then \(B_n=1\).

The theorem concerns precisely the family and length notion in Conjecture 3.1. It does not settle the source's Conjectures 3.2 or 3.3, nor does it improve the worst-case stopping-time bound for arbitrary binary polynomials.

## Proof
Fix a non-power-of-two \(n\). Write \(n=qu\), where \(q=2^{\nu_2(n)}\) and \(u>1\) is odd. Let
\[
k=2^{\nu_2(u-1)},\qquad u=1+kv,
\]
so \(v\) is odd, and put
\[
K=qk,\qquad t=q(k-1)=K-q.
\]
Set \(w=z^q\). Since \(q\) and \(k\) are powers of two, Frobenius gives
\[
y^q=(1+z)^q=1+w
\]
and
\[
(1+w)^k=1+w^k.
\]
Hence
\[
y^n=(1+w)^u=(1+w)(1+w^k)^v.
\]
Define
\[
Q=\frac{(1+w^k)^v+1}{w^k}.
\]
Because \(w^k=z^K\) and \(1+w^k=y^K\), this is
\[
Q=\frac{y^{Kv}+1}{z^K}=B_{Kv}.
\]
Using \((1+w^k)^v=1+w^kQ\), we obtain
\[
B_n=\frac{y^n+1}w
   =1+w^{k-1}(1+w)Q
   =1+z^t y^qQ.
\]
For \(0\le s\le t-1\), set
\[
F_s=1+z^{t-s}y^{q+s}Q.
\]
Then \(F_0=B_n\). If \(s<t-1\),
\[
1+yF_s
 =z+z^{t-s}y^{q+s+1}Q
 =zF_{s+1}.
\]
Here \(F_{s+1}(1)=1\), so exactly one factor \(z\) is stripped and the next odd polynomial is \(F_{s+1}\).

At the last step,
\[
1+yF_{t-1}=z(1+y^KQ).
\]
Now
\[
1+y^KQ
 =\frac{z^K+y^{K(v+1)}+y^K}{z^K}
 =\frac{y^{K(v+1)}+1}{z^K},
\]
because \(z^K=(y+1)^K=y^K+1\). If \(c=2^{\nu_2(v+1)}\), then
\[
1+y^KQ=z^{K(c-1)}B_{K(v+1)}.
\]
Finally,
\[
K(v+1)=qkv+qk=qu+q(k-1)=n+t.
\]
Thus the full stripping at the \(t\)-th step leaves exactly \(B_{n+t}\). This proves the block transition.

It remains to count blocks. The number \(K=qk\) is a power of two and divides \(q(u-1)=n-q\), so \(K<n<2^R\) whenever \(2^{R-1}<n<2^R\). The number \(n+t=K(v+1)\) is the next multiple of \(K\) after \(n=Kv+q\). Since \(2^R\) is also a multiple of \(K\) and is larger than \(n\), one has
\[
n<n+t\le2^R.
\]
Moreover \(v+1\) is even and \(k\ge2\), so \(\nu_2(n+t)>\nu_2(n)\). Repeating the block transition therefore reaches a power of two after finitely many blocks, never passes \(2^R\), and must end at \(2^R\), the only power of two in \((2^{R-1},2^R]\).

Each block uses exactly as many Collatz steps as the increase in its index. Therefore the total number of odd steps is the telescoping sum
\[
2^R-n=j.
\]
Including the initial odd polynomial gives exactly \(j+1\) odd-sequence terms.

## Verification
The standalone `verify.py` implements exact arithmetic in \(\mathbb F_2[y]\) using bit-polynomial integers. For every \(1\le R\le8\) and every starting index \(2^{R-1}<n\le2^R\), it constructs \(B_n\), executes the source odd-step rule by exact polynomial division by \(y+1\), checks each block transition \(B_n\mapsto B_{n+t}\), checks that the first \(t-1\) valuations in each block are one, and checks the final length \(2^R-n+1\).

Expected output is:

`VERIFY_OK r=1..8 starts=255 odd_steps=10795 block_identity=exact length_formula=exact`

This finite replay is corroborative only. The theorem for all \(R\) is proved by the symbolic block identity above.

## Relationship to prior work
Gallardo and Rahavandrainy's paper introduces the variant with \(x(x+1)\) playing the role of two, proves termination for every nonzero binary polynomial, and states the present Mersenne-power length formula explicitly as Conjecture 3.1 after computer experiments. Its table for \(9\le n\le16\) matches the theorem, but the paper does not prove the conjecture.

Earlier polynomial Collatz literature cited by that paper studies different transformations, most notably maps based on a single factor \(x\) and the multiplier \(x+1\), or broader eventual-periodicity questions. Those results do not imply the exact length formula for the simultaneous \(x\)- and \(x+1\)-stripping variant with multiplier \(M_1=x^2+x+1\). Searches for the exact conjecture, its aliases, and the block transition found no proof or stronger result in the checked literature or published finding index.

## Limitations
The argument exploits that the starting polynomial is a power of \(M_1\) plus one and that the entire odd orbit stays in the subring \(\mathbb F_2[M_1]\). It does not classify lengths for arbitrary starting polynomials. The literature check cannot rule out an unindexed or very recent independent proof; this remains the main originality risk.

## References
1. L. H. Gallardo and O. Rahavandrainy, *A variant of Collatz's Conjecture over Binary Polynomials*, arXiv:2510.07530v1, first public 8 October 2025; journal version, Revista de la Unión Matemática Argentina, DOI 10.33044/REVUMA.5555. Primary MSC 11T55 (also 11T06).
2. G. Alon, A. Behajaina and E. Paran, *On the stopping time of the Collatz map in \(\mathbb F_2[x]\)*, Finite Fields and Their Applications 99 (2024), 102473; arXiv:2401.03210.
3. A. Behajaina and E. Paran, *The Collatz map analogue in polynomial rings and in completions*, Discrete Mathematics 348 (2025), 114273; arXiv:2312.00390.
