# A seven-dimensional space of symmetric biderivations in characteristic two

## Finding

Let \(k\) be any field of characteristic \(2\), and let \(\mathfrak g\) be the three-dimensional vector space with basis \(e_1,e_2,e_3\) and alternating bracket
\[
[e_1,e_2]=e_3,\qquad [e_2,e_3]=e_1,\qquad [e_3,e_1]=e_2.
\]
Then \(\mathfrak g\) is a perfect Lie algebra. The vector space of symmetric biderivations \(B:\mathfrak g\times\mathfrak g\to\mathfrak g\) has dimension exactly \(7\) over \(k\). Every such map is uniquely determined by seven scalars \(a,b,d,e,g,h,i\in k\) through
\[
\begin{aligned}
B(e_1,e_1)&=(a+g)e_1+(b+h)e_2+(e+i)e_3,\\
B(e_1,e_2)&=(b+h)e_1+a e_2+d e_3,\\
B(e_1,e_3)&=(e+i)e_1+d e_2+g e_3,\\
B(e_2,e_2)&=a e_1+b e_2+e e_3,\\
B(e_2,e_3)&=d e_1+e e_2+h e_3,\\
B(e_3,e_3)&=g e_1+h e_2+i e_3.
\end{aligned}
\]
All coefficients are interpreted in \(k\), so addition and subtraction coincide.

## Assumptions and scope

The bracket is extended bilinearly and satisfies \([x,x]=0\) for every \(x\in\mathfrak g\). A symmetric biderivation means a symmetric bilinear map \(B\) such that, for each fixed \(x\), the linear map \(D_x(y)=B(x,y)\) is a derivation:
\[
B(x,[y,z])=[B(x,y),z]+[y,B(x,z)]\qquad(x,y,z\in\mathfrak g).
\]
The claim classifies only these adjoint-valued biderivations of this explicit three-dimensional algebra; it does not classify biderivations of all perfect Lie algebras or maps with values in arbitrary modules.

## Proof

The Jacobiator is trilinear. For three distinct basis vectors its value is
\([e_1,e_1]+[e_2,e_2]+[e_3,e_3]=0\); if two inputs coincide, alternation and skew-symmetry make it zero. Thus the bracket is a Lie bracket. Each basis vector is a bracket of two basis vectors, so \([\mathfrak g,\mathfrak g]=\mathfrak g\). In dimensions one and two an alternating bracket has image of dimension at most \(\dim\bigwedge^2\mathfrak g\le1\), so no Lie algebra of dimension below three can be nonzero and perfect. This example is therefore dimension-minimal among nonzero perfect Lie algebras.

Write a general symmetric bilinear map by its six values on unordered basis pairs, each with three coordinates: there are \(18\) scalar unknowns. The derivation identity for each basis choice of \(x\), each of the three unordered pairs \((y,z)\), and each output coordinate gives a homogeneous linear system with \(27\) equations. Row reduction over the prime field \(\mathbb F_2\) gives rank \(11\), hence nullity \(18-11=7\). Taking the seven free coordinates to be the \(e_1,e_2\) coordinates of \(B(e_2,e_2)\), the \(e_1,e_2\) coordinates of \(B(e_2,e_3)\), and all three coordinates of \(B(e_3,e_3)\), the remaining coordinates are forced to be exactly the displayed formulas.

Conversely, substituting the displayed formulas into the derivation identity for all basis triples verifies the identity; bilinearity then gives it for all triples. The seven free coordinates occur unchanged among the displayed values, so the parameterization is injective and exhausts the seven-dimensional solution space. The coefficient matrix has entries in \(\mathbb F_2\); its rank and the same row-reduction formulas persist over every field of characteristic \(2\). The bracket itself is a nonzero symmetric biderivation in characteristic \(2\), consistent with the classification.

## Verification

The accompanying standalone script `verify.py` checks the Jacobi identity on basis triples, perfectness, the rank \(11\) of the derivation-equation matrix over \(\mathbb F_2\), and the biderivation identities for every one of the \(2^7=128\) parameter choices over \(\mathbb F_2\). The universal-field conclusion follows from the explicit linear system over the prime field, not from finite testing alone.

## Relationship to prior work

Recent work on biderivations of \(\mathfrak{sl}_2\) in prime characteristic explicitly assumes characteristic \(p>2\); a separate classification for classical simple Lie algebras assumes characteristic different from \(2\) and \(3\). A theorem for finite-dimensional perfect Lie algebras assumes characteristic zero. Those statements motivate the characteristic-two boundary but do not imply the present classification: the algebra here is defined directly by the displayed bracket, and the result is an exact calculation of its full symmetric-biderivation space. No general statement about all characteristic-two simple or perfect Lie algebras is claimed.

## Limitations

The calculation concerns one explicit algebra and adjoint-valued symmetric biderivations only. It does not establish a classification for other characteristic-two Lie algebras, prove that this algebra represents every relevant isomorphism type, or address module-valued biderivations. Bounded literature searches did not find this exact seven-parameter classification; absence from those searches is not a proof of global novelty.

## References

1. Shujuan Wang, Yufeng Yao, and Zhaoxin Li, “Biderivations of \(\mathfrak{sl}(2)\) on All Simple Modules in Prime Characteristic,” *Frontiers of Mathematics* 20 (2025), no. 5, 1097–1108. DOI: 10.1007/s11464-023-0134-6. Published online 2025-11-01.
2. Qiufan Chen, Yufeng Yao, and Kaiming Zhao, “Biderivations of Lie algebras,” *Canadian Mathematical Bulletin* 68 (2025), no. 2, 440–455; arXiv:2406.06376.
3. Ignacio Bajo, Saïd Benayadi, and Hassan Oubba, “Non-existence of symmetric biderivations on finite-dimensional perfect Lie algebras,” arXiv:2503.13059 (2025).
4. Wei Bai and Wende Liu, “Biderivations of Simple Modular Lie Algebras of Cartan-Type,” *Mathematics* 13 (2025), no. 16, 2596. DOI: 10.3390/math13162596.
