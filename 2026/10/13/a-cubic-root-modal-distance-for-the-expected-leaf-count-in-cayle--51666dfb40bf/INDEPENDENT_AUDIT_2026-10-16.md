# Independent mathematical audit

## correctness

PASS

For a fixed 1-to-2 path with s=k+1 vertices, n−s=r remaining vertices, the matrix-tree principal minor det(nI_r−J_r)=s n^(r−1) counts rooted attachments; deleting an off-path leaf gives probability ((n−1)/n)^(r−1) and deleting a path-end leaf gives (s−1)/s times that probability. Linearity gives the stated expectation for 1≤k≤n−2, with the spanning-path endpoint k=n−1 giving 2. Subtracting successive exact fractions yields sign 2n−(k²+1)(k+2), with exceptional last difference (3−n)/(n−1). Strict increase of the cubic proves unimodality and exact ties, including n=3, while uniform expansion for k=O(n^(1/3)) proves first mode (2n)^(1/3)+O(1) and peak advantage 1/e+O(n^(−1/3)). Independent Prüfer enumeration n≤7, 18,248 trees and 21 conditional means, agrees, but is not the infinite proof.

## originality

PASS

Exact full global-leaf-count regression at all fixed-pair distances and cubic-root mode were not supplied by the retrieved distance-profile, endpoint-degree or Wiener-index statements. Distinct from established rooted-forest enumeration as a general tool; originality remains best-of-knowledge because older bivariate enumerators may implicitly specialize to it.

## value

PASS

Both global leaf extremity and distinguished-pair distance are canonical observables for Cayley trees. Their conditional relationship has an unexpected nonmonotone all-n shape, a sharp cubic turning threshold versus typical sqrt(n) distances, and a nonzero limiting O(1) advantage; researchers can use the exact regression and finite tie classification without a separate general limit theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
