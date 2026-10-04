# A maximal proper hull inside the unique ternary length-22 non-circulant DT optimum
## Finding

Let \(C\) be the unique ternary DT-optimal double Toeplitz \([22,11,8]_3\) code in the Harada--Yamaguchi classification that is inequivalent to every DT-optimal double circulant and double negacirculant code at length \(22\). Their data give
\[
t=1,
\qquad
a=(0,1,2,1,1,2,1,1,1,2),
\qquad
b=(1,1,2,2,2,1,2,2,1,2).
\]
For the systematic generator
\[
G=[I_{11}\mid T(t,a,b)],
\]
the Euclidean Gram matrix has
\[
\operatorname{rank}_{\mathbb F_3}(GG^{\mathsf T})=1.
\]
Consequently
\[
\dim_{\mathbb F_3}(C\cap C^\perp)=10.
\]
This is the largest possible proper hull dimension for a length-\(22\), dimension-\(11\) code.

Writing \(H=C\cap C^\perp\), the hull is a self-orthogonal ternary \([22,10,9]_3\) code with exact weight enumerator
\[
W_H(z)=1+1540z^9+14784z^{12}+31680z^{15}+10780z^{18}+264z^{21}.
\]
It is distance-optimal among all ternary linear \([22,10]\) codes.

The ambient code has exact weight enumerator
\[
\begin{aligned}
W_C(z)={}&1+990z^8+1540z^9+16128z^{11}+14784z^{12}+59400z^{14}\\
&+31680z^{15}+38808z^{17}+10780z^{18}+2772z^{20}+264z^{21}.
\end{aligned}
\]
The quotient \(C/H\) has order \(3\). Its two nonzero cosets have the same weight distribution,
\[
495z^8+8064z^{11}+29700z^{14}+19404z^{17}+1386z^{20}.
\]
Thus every word of weight divisible by \(3\) in this particular spectrum lies in the hull, while all words in the two nonzero hull cosets have weights congruent to \(2\pmod 3\).

## Assumptions and scope

The object is the specific double Toeplitz code determined by the source triple \((t,a,b)\) above. The Toeplitz matrix convention is
\[
T_{ij}=
\begin{cases}
t,&i=j,\\
a_{j-i},&j>i,\\
b_{i-j},&i>j,
\end{cases}
\]
with indices for \(a\) and \(b\) starting at \(1\). All arithmetic is over \(\mathbb F_3\), and the hull is the Euclidean hull for the standard inner product.

The source classification establishes that this is the unique DT-optimal class at length \(22\) outside the double-circulant and double-negacirculant subclasses. The calculations here concern that displayed representative; hull dimension is invariant under monomial equivalence over \(\mathbb F_3\), because nonzero coordinate scalings square to \(1\).

## Proof

For any full-rank generator matrix \(G\) of a \([n,k]\) code \(C\), a codeword \(xG\) lies in \(C^\perp\) exactly when
\[
xGG^{\mathsf T}=0.
\]
Therefore
\[
\dim(C\cap C^\perp)=k-\operatorname{rank}(GG^{\mathsf T}).
\]

Exact row reduction over \(\mathbb F_3\) for the source matrix gives
\[
\operatorname{rank}(G)=11,
\qquad
\operatorname{rank}(GG^{\mathsf T})=1.
\]
Hence the hull has dimension \(10\). Since the Gram matrix is nonzero, \(C\) is not self-orthogonal. A dimension-\(11\) self-orthogonal code of length \(22\) would be self-dual, so dimension \(10\) is the maximal proper hull dimension.

A basis of \(\ker(GG^{\mathsf T})\) gives a generator matrix for \(H\). Exhausting all \(3^{10}=59049\) hull words gives the stated hull enumerator and minimum distance \(9\). Since \(H\subseteq C^\perp\), the hull is self-orthogonal.

For comparison with the absolute linear-code bound, the ternary Griesmer sum for a hypothetical \([22,10,10]_3\) code is
\[
\sum_{i=0}^{9}\left\lceil\frac{10}{3^i}\right\rceil
=10+4+2+1+1+1+1+1+1+1
=23.
\]
Thus no ternary linear \([22,10,10]_3\) code exists, and the hull distance \(9\) is optimal.

Finally, exhausting all \(3^{11}=177147\) words of \(C\) gives the ambient enumerator. Choosing any word outside \(H\) and enumerating its two nonzero cosets gives the identical coset distribution displayed above; adding the two coset distributions to \(W_H\) recovers \(W_C\).

## Verification

`artifacts/verify.py` uses only the Python standard library. It reconstructs the exact Toeplitz matrix from the source triple, verifies the ranks of \(G\) and \(GG^{\mathsf T}\), computes a nullspace basis, and checks directly that the resulting hull generator is self-orthogonal.

The verifier exhausts all \(177147\) words of \(C\), all \(59049\) words of \(H\), and both nonzero cosets of \(H\) in \(C\). It checks every coefficient of the three displayed distributions and evaluates the Griesmer sum for \((q,k,d)=(3,10,10)\). Successful replay prints `VERIFY_OK`.

## Relationship to prior work

Harada and Yamaguchi classify DT-optimal double Toeplitz codes and identify the unique length-\(22\) ternary DT-optimal class that is inequivalent to any DT-optimal double circulant or double negacirculant code. Their paper and accompanying Magma data provide the exact triple \((t,a,b)\) and the minimum distance \(8\), but do not state the Gram rank, hull dimension, hull weight enumerator, or hull-coset decomposition established here.

Shi, Xu, and Solé introduced double Toeplitz codes and proved that every such code is isodual, with self-dual double Toeplitz codes restricted to the double-circulant or double-negacirculant cases. Isoduality alone does not determine the Euclidean hull. In particular, it does not imply the codimension-one hull, the optimal \([22,10,9]_3\) self-orthogonal subcode, or the exact spectra above.

Related work on Toeplitz constructions with small hulls studies different matrix families and typically targets LCD or one-dimensional-hull behavior. The present phenomenon is at the opposite extreme: a maximal proper hull inside the unique non-circulant/non-negacirculant ternary DT optimum at this length.

## Limitations

The result is object-specific. It does not assert that other DT-optimal codes have codimension-one hulls, nor does it classify all ternary self-orthogonal \([22,10,9]_3\) codes up to equivalence.

The optimality statement for \(H\) is only for minimum distance among ternary linear \([22,10]\) codes and follows from the Griesmer bound. No claim is made that the displayed hull is unique among all optimal ternary \([22,10,9]_3\) codes.

## References

1. Masaaki Harada and Keito Yamaguchi, *Double Toeplitz codes and their average weight enumerators*, arXiv:2603.20699, first submitted 21 March 2026.
2. Masaaki Harada and Keito Yamaguchi, companion Magma data for ternary DT-optimal length-\(22\) codes, `F3-DTC-22-8.magma`.
3. Minjia Shi, Li Xu, and Patrick Solé, *On Isodual Double Toeplitz Codes*, Journal of Systems Science and Complexity 37 (2024), 2196--2206; arXiv:2102.09233.
4. F. J. MacWilliams and N. J. A. Sloane, *The Theory of Error-Correcting Codes*, North-Holland, 1977.
