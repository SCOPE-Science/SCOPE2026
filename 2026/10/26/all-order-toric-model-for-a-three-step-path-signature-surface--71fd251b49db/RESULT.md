# All-order toric model for a three-step path signature surface

## Finding

For every integer \(k\ge 4\), consider the planar axis-parallel path with three successive segment vectors \(a e_1\), \(b e_2\), and \(c e_1\), where \(e_1,e_2\) are the standard basis of \(\mathbb C^2\). Let \(\mathcal A_{(1,2,1),k}\) be the projective closure of its order-\(k\) signature image. After an invertible linear change of target coordinates, \(\mathcal A_{(1,2,1),k}\) is the projectively normal toric surface defined by the lattice polygon

\[
P_k=\operatorname{conv}\{(0,0),(0,k),(k-1,1)\}.
\]

Consequently, \(\deg \mathcal A_{(1,2,1),k}=k(k-1)\). The surface has exactly two singular torus-fixed points: one of cyclic quotient type \(\frac{1}{k-1}(1,1)\), and one of type \(\frac{1}{k}(1,k-1)\), which is the Du Val singularity \(A_{k-1}\). The third torus-fixed point is smooth.

## Assumptions and scope

Work over \(\mathbb C\), with the usual tensor-signature convention in which the signature of a concatenation is the product of the signatures in the tensor algebra. The shape \((1,2,1)\) means first-axis, second-axis, first-axis motion; the segment lengths \(a,b,c\) are parameters. Only the order-\(k\) signature, not the full truncated signature, is used. The claim is for all integers \(k\ge4\); the same coordinate description also specializes to the previously studied cases \(k=2,3\).

## Proof

The tensor-algebra signature of the three segments is
\[
\exp(ae_1)\exp(be_2)\exp(ce_1).
\]
For a word \(1^i2^j1^\ell\) with \(j\ge1\) and \(i+j+\ell=k\), its coefficient is
\[
\frac{a^i b^j c^\ell}{i!j!\ell!}.
\]
The coefficient of the pure word \(1^k\) is \((a+c)^k/k!\); all other words not of the displayed form have coefficient zero. Put \(u=a+c\), \(v=a\), and \(w=b\). The change \((a,c)\leftrightarrow(u,v)\) is invertible. For each fixed \(j\in\{1,\ldots,k\}\), the polynomials \(a^i c^{k-j-i}\), for \(0\le i\le k-j\), form a basis of the homogeneous binary forms of degree \(k-j\) in \(u,v\). Therefore an invertible linear change among the target coordinates for that fixed \(j\) replaces them by the monomials
\[
u^{k-j-q}v^q w^j,\qquad 0\le q\le k-j.
\]
Together with the pure coordinate \(u^k\), these are all the coordinates of the transformed map.

Index a monomial \(u^{k-j-q}v^q w^j\) by the lattice point \((q,j)\). The exponent set is exactly
\[
\{(0,0)\}\ \cup\ \{(q,j)\in\mathbb Z^2:1\le j\le k,\ 0\le q\le k-j\}.
\]
Its convex hull is \(P_k\), with vertices \((0,0),(0,k),(k-1,1)\); the displayed set is precisely \(P_k\cap\mathbb Z^2\). Hence the projective image closure is the monomial toric surface associated with \(P_k\). Every lattice polygon has the integer decomposition property, so the corresponding homogeneous semigroup is saturated and the surface is projectively normal.

The Euclidean area of \(P_k\) is \(k(k-1)/2\). The degree of a projective toric surface is the normalized area of its polygon, so the degree is \(k(k-1)\). For the singularities, the primitive edge directions at the three vertices give the following two-dimensional cones: at \((0,0)\), a cone equivalent to the rays \((1,0),(1,k-1)\), hence quotient type \(\frac{1}{k-1}(1,1)\); at \((0,k)\), the primitive rays form a lattice basis, hence the point is smooth; at \((k-1,1)\), a cone equivalent to \((1,0),(k-1,k)\), hence quotient type \(\frac{1}{k}(1,k-1)\). Since \(\frac{1}{k}(1,k-1)\) is the quotient \(\frac{1}{k}(1,-1)\), it is the Du Val singularity \(A_{k-1}\). A complete toric surface is smooth along the dense torus and the open one-dimensional orbits, so these are the only singular points.

## Verification

The coefficient formula follows directly by multiplying the three exponential series and using Chen's concatenation identity. The linear coordinate change is invertible separately for each number \(j\) of second-axis letters. The lattice-point count is \(1+\sum_{j=1}^{k}(k-j+1)=1+k(k+1)/2\); for \(k=3\) this gives seven coordinates, agreeing with the degree-six surface in the published example. The normalized-area calculation and the primitive-ray determinants give the stated degree and quotient indices. No finite computation is used as a substitute for the all-\(k\) proof.

## Relationship to prior work

Colmenarejo, Galuppi, and Michałek study axis-parallel signature varieties in *Toric geometry of path signature varieties* (first public version 9 March 2019; journal publication 2020). Their Proposition 3.9 establishes toricness for every shape at orders two and three, and their Example 3.7 computes the order-three variety for shape \((1,2,1)\), including its degree-six toric surface. They then ask whether every axis-parallel signature variety is toric. The present result gives an explicit all-order polygon and singularity description for this one natural shape at every order \(k\ge4\); it does not answer the general question for arbitrary shapes.

## Limitations

The result concerns only the fixed shape \((1,2,1)\); no conclusion is drawn for other shapes or for the full universal signature variety. The literature search was targeted rather than exhaustive, so a later unindexed source or supplemental computation could contain the same special case. The proof establishes the stated complex projective variety and its toric invariants, not injectivity of the path-to-signature map on individual paths.

## References

1. L. Colmenarejo, F. Galuppi, and M. Michałek, “Toric geometry of path signature varieties,” *Advances in Applied Mathematics* **121** (2020), article 102102; arXiv:1903.03779 (first submitted 2019-03-09), especially §3.1, Example 3.7, Proposition 3.9, and the question at the end of §3.1.
2. W. Fulton, *Introduction to Toric Varieties*, Annals of Mathematics Studies 131, Princeton University Press, 1993 (standard polygon, degree, and affine toric-cone conventions).
