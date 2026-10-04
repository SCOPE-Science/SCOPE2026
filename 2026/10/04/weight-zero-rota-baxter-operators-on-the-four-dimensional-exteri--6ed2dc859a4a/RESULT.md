# Weight-zero Rota–Baxter operators on the four-dimensional exterior algebra over \(\mathbb F_2\)
## Finding
Let \(A=\Lambda_{\mathbb F_2}(e_1,e_2)\) with ordered basis \((1,e_1,e_2,z)\), where \(z=e_1e_2\). Thus
\[
e_1^2=e_2^2=z^2=e_1z=e_2z=0,\qquad e_1e_2=e_2e_1=z.
\]
A weight-zero Rota–Baxter operator is an \(\mathbb F_2\)-linear map \(R:A\to A\) satisfying
\[
R(x)R(y)=R\bigl(R(x)y+xR(y)\bigr)\qquad(x,y\in A).
\]
There are exactly \(80\) such operators. Every one satisfies \(R(z)=0\). Their ranks have distribution
\[
\#\{R:\operatorname{rank}R=0,1,2,3\}=(1,25,30,24),
\]
and no weight-zero Rota–Baxter operator has rank \(4\).

The algebra automorphism group has order \(24\), and conjugation by \(\operatorname{Aut}(A)\) partitions the \(80\) operators into exactly \(12\) classes. The orbit sizes are
\[
1,1,3,3,6,6,6,6,6,6,12,24.
\]
A complete set of representatives is given below. Each displayed four-tuple is \((R(1),R(e_1),R(e_2),R(z))\); zero entries mean the zero vector.

| rank | orbit size | representative |
|---:|---:|---|
| \(0\) | \(1\) | \((0,0,0,0)\) |
| \(1\) | \(1\) | \((z,0,0,0)\) |
| \(1\) | \(3\) | \((0,0,z,0)\) |
| \(1\) | \(3\) | \((z,0,z,0)\) |
| \(1\) | \(6\) | \((0,0,e_1,0)\) |
| \(1\) | \(6\) | \((e_1,0,0,0)\) |
| \(1\) | \(6\) | \((e_1,0,e_1,0)\) |
| \(2\) | \(6\) | \((e_1,0,z,0)\) |
| \(2\) | \(6\) | \((e_1,0,e_1+z,0)\) |
| \(2\) | \(6\) | \((z,0,e_1,0)\) |
| \(2\) | \(12\) | \((e_1,z,0,0)\) |
| \(3\) | \(24\) | \((e_1,e_2,z,0)\) |

## Assumptions and scope
The field is exactly \(\mathbb F_2\), the algebra is the ordinary exterior algebra on two generators, and the Rota–Baxter weight is exactly zero. The classification is for all \(\mathbb F_2\)-linear operators, not only homogeneous, graded, idempotent, or splitting operators. Equivalence means conjugacy by unital algebra automorphisms of \(A\).

Characteristic two is a genuine boundary: in \(A\), the usual exterior relation \(e_1e_2=-e_2e_1\) becomes \(e_1e_2=e_2e_1\). Therefore classifications proved under characteristic different from two do not specialize formally to this case.

## Proof
An \(\mathbb F_2\)-linear endomorphism of the four-dimensional vector space \(A\) is determined by the four images \(R(1),R(e_1),R(e_2),R(z)\), each of which has \(16\) possibilities. Hence there are exactly
\[
16^4=2^{16}=65536
\]
linear maps to test.

For fixed \(R\), the defect
\[
D_R(x,y)=R(x)R(y)-R\bigl(R(x)y+xR(y)\bigr)
\]
is bilinear in \((x,y)\). Thus \(D_R\equiv0\) on all of \(A\times A\) if and only if it vanishes on the \(16\) ordered pairs of basis vectors from \((1,e_1,e_2,z)\). Exhaustive evaluation of those \(65536\) maps gives exactly \(80\) solutions. Direct inspection of the complete solution set gives \(R(z)=0\) for every solution and the rank distribution \((1,25,30,24)\).

For the automorphisms, let \(J=(e_1,e_2,z)\) be the Jacobson radical. Then \(J^2=\mathbb F_2 z\), so every automorphism preserves both \(J\) and \(J^2\). Its induced map on \(J/J^2\) is any element of \(\operatorname{GL}_2(\mathbb F_2)\). Since every nonzero determinant in \(\mathbb F_2\) equals \(1\), every such lift fixes \(z\). Independently, each of the two lifted generators may be shifted by an arbitrary multiple of \(z\). Therefore
\[
|\operatorname{Aut}(A)|=|\operatorname{GL}_2(\mathbb F_2)|\,2^2=6\cdot4=24.
\]
Conjugating the complete \(80\)-element solution set by these \(24\) automorphisms produces the \(12\) displayed orbits. Their sizes sum to \(80\), and the listed representatives are one element from each orbit.

## Verification
The standalone verifier `artifacts/verify.py` performs the complete finite proof twice at its critical point. Its first implementation enumerates all \(65536\) linear maps using a bit-level multiplication routine and tests the Rota–Baxter identity on the \(16\) basis pairs. A separately written tuple-coordinate multiplication routine then rechecks every accepted operator on all \(16^2=256\) ordered pairs of algebra elements.

The same verifier independently enumerates all invertible unital multiplicative linear maps, recovering exactly \(24\) automorphisms, computes every conjugacy orbit, checks orbit stability, checks that the orbit sizes sum to \(80\), and verifies the rank profile and the universal identity \(R(z)=0\). The recorded output ends with `CHECK_OK` and reports all twelve representatives.

## Relationship to prior work
Shakoor and Noor-ul-Ain classify Rota–Baxter operators on the same four-dimensional Grassmann algebra over the real numbers; their preprint was first submitted on September 7, 2026, and lists MSC 2020 codes 15B33 and 17B38. Their ground field excludes the characteristic-two multiplication law used here.

Hua and Liu's 2013 work on Rota–Baxter operators on the exterior algebra in two variables is indexed as assuming an algebraically closed field of characteristic different from two. Gubarev's 2021 work on unital algebras likewise states its Grassmann-algebra results in characteristic zero. These results establish that this small exterior algebra is a natural Rota–Baxter classification object, while their hypotheses do not imply the present characteristic-two enumeration or its automorphism-orbit reduction.

Targeted searches for characteristic-two exterior/Grassmann Rota–Baxter classifications, for the exact count \(80\), for the \(12\)-orbit decomposition, and for the rank profile did not locate an equivalent statement. This is evidence against direct prior coverage, not a proof of absolute novelty.

## Limitations
The theorem is only for \(\mathbb F_2\) and weight zero. It does not classify operators over larger fields of characteristic two, nonzero weights, higher exterior rank, or isomorphism classes of the induced dendriform structures. The exhaustive argument is finite and complete for the stated field and algebra, but it does not by itself reveal a parameterized characteristic-two classification over arbitrary fields.

A residual literature risk remains because the 2013 exterior-algebra paper is not readily available in full text through the inspected public index, although its indexed abstract explicitly assumes characteristic different from two. Unindexed or differently titled characteristic-two classifications could also exist.

## References
1. K. Shakoor and N.-u.-Ain, “The Classification of the Rota-Baxter Operators on Four-dimensional Grassmann Algebra,” arXiv:2609.07377v1, 2026. https://arxiv.org/abs/2609.07377
2. X. Hua and W. Liu, “Rota-Baxter Operators on Exterior Algebra,” Journal of Harbin University of Science and Technology 18(4) (2013), 125–128. The characteristic restriction is reported in the indexed abstract and the paper is cited bibliographically in later Rota–Baxter literature.
3. V. Gubarev, “Rota-Baxter operators on unital algebras,” Moscow Mathematical Journal 21(2) (2021), 325–364.
