# Efficient randomized parity queries without large monochromatic affine subspaces

## Statement

There is a family of total Boolean functions
\[
\phi_N:\mathbb F_2^N\to\{0,1\}
\]
such that
\[
R^{\oplus}(\phi_N)=O(\log N\,\log\log N),
\]
while every affine subspace on which \(\phi_N\) is constant has codimension
\[
N^{\Omega(1)}.
\]
Consequently,
\[
D^{\oplus}(\phi_N)=N^{\Omega(1)}.
\]
In particular, this gives a negative answer to Gavinsky's Question 14 (Random Structures & Algorithms, 2025): an efficient randomized parity-query protocol need not force the function to be constant on any affine subspace of polylogarithmic codimension.

The family is the one-variable XOR quotient of the total communication function constructed by Wang and Wu in *Efficient Randomized Communication Without Large Monochromatic Rectangles* (ECCC TR26-190 / arXiv:2609.20763). The new point is that their particular public-coin protocol descends to a parity-query protocol for the quotient function, while their rectangle bound converts directly into an affine-subspace bound.

## Construction as an XOR function

Use Wang and Wu's parameters \(k\ge 12\), \(m=2^k\), and \(d=O(km^2)\). A communication input on each side has length
\[
N=km+4km(2d-1),
\]
so \(k=\Theta(\log N)\). Alice has \((x,u)\), Bob has \((y,v)\), where \(x,y\in\mathbb F_2^{km}\), and \(u=(u_1,\ldots,u_m)\), \(v=(v_1,\ldots,v_m)\) are certificate tables. Put
\[
z=x\oplus y,\qquad c_j=u_j\oplus v_j.
\]
Their Definition 3.8 is
\[
F((x,u),(y,v))=
\begin{cases}
\operatorname{Check}(z,c_{\operatorname{Ads}(z)}),&\operatorname{Ind}(z)=1,\\
0,&\operatorname{Ind}(z)=0.
\end{cases}
\]
Thus \(F\) depends only on the bitwise XOR of the two parties' complete inputs. Define the total Boolean function \(\phi_N\) on \(w=(z,c_1,\ldots,c_m)\in\mathbb F_2^N\) by the same formula. Then exactly
\[
F(a,b)=\phi_N(a\oplus b).
\]

## Randomized parity-query upper bound

Wang and Wu's randomized protocol first estimates the \(k\)-bit address. Let
\[
q=\lceil18\ln(6k)\rceil.
\]
For each of the \(k\) Gap-Hamming blocks it samples \(q\) coordinates of \(z\). A parity-query algorithm for \(\phi_N\) simply asks those \(kq\) singleton linear queries and computes the same estimated address \(h\).

At that address, Wang and Wu use their Theorem 3.7: a test for \(\operatorname{Check}(z,c_h)\) making four linear queries over
\[
E=\mathbb F_{2^{4k}}.
\]
Fix an \(\mathbb F_2\)-basis of \(E\). Each returned field element has \(4k\) binary coordinates. Because an \(E\)-linear evaluation with fixed coefficients is in particular \(\mathbb F_2\)-linear in the binary coordinates of \((z,c_h)\), each binary coordinate is one ordinary parity query. Hence the four field-valued queries can be recovered using \(16k\) parity queries.

The resulting parity-query algorithm has the same random choices and the same acceptance rule as the centralized version of Wang and Wu's test. Their completeness/soundness analysis therefore gives worst-case error below \(1/3\), with
\[
R^{\oplus}(\phi_N)
\le k\lceil18\ln(6k)\rceil+16k
=O(k\log k)
=O(\log N\,\log\log N).
\]

## Affine-subspace lower bound

Wang and Wu prove that every monochromatic rectangle for \(F\) has uniform density at most
\[
\operatorname{rect}(F)\le 2^{-m/(8k)}.
\]
Now suppose \(C=a+H\subseteq\mathbb F_2^N\) is an affine subspace of codimension \(r\) on which \(\phi_N\) is constant. Then
\[
H\times(a+H)
\]
is a monochromatic rectangle for \(F\), because
\[
\{x\oplus y:x\in H,\ y\in a+H\}=a+H=C.
\]
Each side has density \(2^{-r}\), so this rectangle has density \(2^{-2r}\). Therefore
\[
2^{-2r}\le 2^{-m/(8k)},
\]
and hence
\[
\boxed{\operatorname{codim}(C)=r\ge \frac{m}{16k}.}
\]
Since \(m=2^k\) and \(N=km+4km(2d-1)\) with \(d=O(km^2)\), this is \(N^{\Omega(1)}\).

Every leaf of a deterministic parity decision tree is a monochromatic affine subspace whose codimension is at most the tree depth. Thus the same estimate gives
\[
D^{\oplus}(\phi_N)\ge \frac{m}{16k}=N^{\Omega(1)}.
\]

## Relation to prior questions

Gavinsky explicitly asked whether every Boolean function with an efficient randomized parity-query protocol must be constant on a large affine subspace. The family above has an \(O(\log N\log\log N)\)-query randomized protocol, yet every monochromatic affine subspace has polynomial codimension, so in particular none has polylogarithmic codimension.

Hatami, Hosseini, and Lovett proved a polynomial equivalence between deterministic communication complexity of XOR functions and deterministic parity decision-tree complexity. Their work also highlighted the randomized analogue as an open direction. The present observation does **not** establish a general randomized communication-to-parity-query simulation for XOR functions. It uses the special form of Wang and Wu's protocol: the address stage samples coordinates of the XOR, and the certificate stage consists of fully linear finite-field queries.

## Limitations

The polynomial codimension exponent is inherited from Wang and Wu's parameters; no attempt is made here to optimize it. The argument applies to their specific construction and protocol, not to arbitrary randomized protocols for XOR functions. It also does not resolve the general randomized analogue of the Hatami-Hosseini-Lovett simulation theorem.

## References

1. Haoyu Wang and Pei Wu, *Efficient Randomized Communication Without Large Monochromatic Rectangles*, ECCC TR26-190 (2026), arXiv:2609.20763. https://eccc.weizmann.ac.il/report/2026/190/ ; https://arxiv.org/abs/2609.20763
2. Dmytro Gavinsky, *Unambiguous Parity-Query Complexity*, Random Structures & Algorithms 66(3), e70010 (2025). https://doi.org/10.1002/rsa.70010
3. Hamed Hatami, Kaave Hosseini, and Shachar Lovett, *Structure of Protocols for XOR Functions*, SIAM Journal on Computing 47(1):208-217 (2018); FOCS 2016. https://doi.org/10.1137/17M1136869
