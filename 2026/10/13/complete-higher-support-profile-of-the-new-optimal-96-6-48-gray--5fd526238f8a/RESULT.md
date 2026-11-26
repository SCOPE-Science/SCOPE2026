# Higher-support profile of the binary Gray image in Example 4.4

## Finding

Let \(C\) be the binary \([96,6,48]_2\) Gray-image code of Yadav, Tiwari, and Sarma's Example 4.4 with \(q=2\), \(m=3\), \(A=\{1,2\}\), and \(B=\{1,3\}\). For each dimension \(r\), the complete support-size distribution of its \(r\)-dimensional subcodes is below; \(w:N\) means that exactly \(N\) subcodes have union of supports of size \(w\).

| \(r\) | \(w:N\) |
|---|---|
| 1 | 48:58, 56:4, 64:1 |
| 2 | 72:504, 76:112, 80:33, 88:2 |
| 3 | 84:736, 86:448, 88:182, 92:28, 96:1 |
| 4 | 90:128, 91:256, 92:204, 94:56, 96:7 |
| 5 | 94:40, 95:16, 96:7 |
| 6 | 96:1 |

Its generalized Hamming weights are \((48,72,84,90,94,96)\). The first row reproduces the published ordinary weight enumerator. In dimensions four and five the spectrum contains odd sizes despite all nonzero codeword weights being multiples of eight.

## Assumptions and scope

Set \(R=\mathbb F_2+u\mathbb F_2\) with \(u^2=0\). For \(S\subseteq\{1,2,3\}\) let \(\Delta_S\) be the binary coordinate space supported on \(S\). Take the ring evaluation code on \(D=R^3\setminus(\Delta_A+u\Delta_B)\) and apply the Gray map \(\Phi(s+ut)=(t,s+t)\) to each coordinate. The result concerns this particular example, not all instances of the source family or all optimal codes with these parameters.

## Proof

Write a message as \(a+ub\) and a defining vector as \(d_1+ud_2\). With messages in the order \((a,b)\), the Gray generator columns are \((d_2,d_1)\) and \((d_1+d_2,d_1)\). Each map is an invertible linear map on \(V=\mathbb F_2^6\), so the length-48 blocks have column sets \(V\setminus S_1\) and \(V\setminus S_2\), with multiplicities retained across blocks. In the order \((x_1,x_2,x_3,y_1,y_2,y_3)\) these deleted spaces are
\[
 S_1=\{(x,y):x_2=0,\ y_3=0\},\qquad
 S_2=\{(x,y):x_2+y_2=0,\ y_3=0\}.
\]
They have dimensions 4 and intersect in dimension 3. Each block spans \(V\): its 48 distinct vectors cannot fit into the at most 32 vectors of a proper subspace. Thus the message map is injective.

For an \(r\)-dimensional message space let \(W\) be its orthogonal complement, \(h=6-r\), and \(a_i=\dim(W\cap S_i)\). A coordinate is zero on the subcode exactly when its generator column lies in \(W\). Counting by blocks gives
\[
 |\operatorname{Supp}|=96-2^{h+1}+2^{a_1}+2^{a_2}.
\]
By dimension, \(a_i\ge\max(0,h-2)\). Both lower bounds are attained at once. Let \(e_j\) denote the \(j\)-th coordinate vector and \(K=\langle e_6,e_2\rangle\). On \(K\), each of the maps \((x,y)\mapsto(x_2,y_3)\) and \((x,y)\mapsto(x_2+y_2,y_3)\) is an isomorphism. For \(h\le2\), use an \(h\)-space inside \(K\); for \(h\ge2\), use an \(h\)-space containing \(K\), so the two restricted maps have rank two. For example, take the span of the first \(h\) vectors in \((e_6,e_2,e_1,e_3,e_4,e_5)\). Inserting \(a_1=a_2=\max(0,h-2)\) gives the stated hierarchy.

For the histogram, enumerate each \(W\) by intersection with the coordinate hyperplane \(x_{\mathrm{last}}=0\) in the ambient space being recursed on. For every subspace \(X\) of the hyperplane, emit \(X\) itself and \(X\cup(v+X)\) for one representative \(v\) of each coset of \(X\) in the affine hyperplane \(x_{\mathrm{last}}=1\). Every subspace not contained in the coordinate hyperplane has exactly one such intersection \(X\) and exactly one such affine coset. The recursion starts with the unique space in dimension zero. Direct counts from the generator columns agree at every step with the displayed intersection formula. The numbers of spaces for \(r=1,\ldots,6\) are \(63,651,1395,651,63,1\), in agreement with the Gaussian coefficients. Their exact support histogram is the table above.

## Verification

Run `python3 artifacts/verify.py` from this directory. It uses the Python standard library, reconstructs both Gray blocks from the defining vectors, verifies the deleted spaces and the simultaneous-minimum flag, and checks every histogram entry against both the direct column count and the intersection formula. No coordinates are collapsed when counting support.

## Context and limitations

The source determines the ordinary distribution and minimum-distance optimality. The two-deleted-space description and column multiplicities also follow from the general Gray-image geometry in [4]. Its hierarchy theorem is for the length-56 projective core, which keeps only one copy of every distinct column; it does not report the support spectra of the length-96 code, where 40 of those columns occur twice. The contribution here is the complete higher-dimensional support census of the uncompressed code, including the frequencies at the minima. In particular, neither a distance-optimal parameter table nor the strictly nested deletion construction in [2] gives the spectrum for these equal-dimensional, non-nested spaces.

## References

1. A. Yadav, A. Tiwari, and R. Sarma, *Linear Codes over \(\mathbb F_q+u\mathbb F_q\) associated with Simplicial Complexes, Their Gray Images, and Subfield Codes*, arXiv:2609.11783v1, Example 4.4.
2. X. Pan, H. Chen, H. Liu, and S. Liu, *Optimal Few-SSW Linear Codes and Their Subcode Support Weight Distributions*, IEEE Transactions on Information Theory, DOI 10.1109/TIT.2024.3519672.
3. V. K. Wei, *Generalized Hamming weights for linear codes*, IEEE Transactions on Information Theory 37 (1991), 1412–1418.
4. *Projective-flat compression of simplicial Gray codes*, [archived result](https://github.com/Resultary/2026/blob/main/2026/10/12/SCOPE-projective-flat-compression-of-simplicial-gray-codes--f91818bd3af7/RESULT.md).
