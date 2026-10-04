# Same-model scientific review

## Correctness

PASS. Centering the regular simplex gives unit vertex directions \(u_i\) with pairwise inner product \(-1/n\), and the opposite facet has equation \(\langle u_i,x\rangle=-r\). Hence \(d_i(P)=r+\langle u_i,p\rangle\). The regular-simplex directions satisfy the tight-frame identity \(\sum_i u_i u_i^{\mathsf T}=((n+1)/n)I\), so the squared norm of every difference vector is recovered exactly from the squared differences of its facet-distance coordinates. The image statement follows from \(d_i(P)=(n+1)r\lambda_i\) in barycentric coordinates. All quantifiers, boundary points, and the inverse map are covered symbolically. The deterministic checker is supplementary only.

## Originality

PASS with terminology and historical-access risk. Zhou's inspected primary text characterizes when the signed-distance sum to oriented hyperplanes is constant; De Villiers' inspected paper gives the equal-face-area tetrahedron and polyhedral first-moment generalizations. Neither states that the complete facet-distance vector of a regular simplex is a scaled Euclidean isometry, nor the resulting pairwise-distance and centered second-moment identities. Repeated semantic searches using facet-distance, barycentric-coordinate, regular-simplex, variance, and Euclidean-isometry formulations returned no equivalent record. The main residual risk is a classical equivalent in barycentric-coordinate or tight-frame literature under different vocabulary.

## Value

PASS. The statement upgrades a familiar scalar conservation law into a full metric reconstruction theorem. It gives an exact inverse coordinate map, reconstructs every pairwise distance from facet-distance measurements, and turns the centered second moment of those measurements into an exact radial coordinate. This is a natural structural fact about regular simplices, not an arbitrary finite computation or a parameter-only restatement.

## Closest literature and limitations

Zhou, arXiv:1008.1236, supplies the hyperplane-normal characterization of constant signed-distance sums. De Villiers, DOI 10.1017/S0025557200000188, develops the three-dimensional equal-face-area version. Alhajjar–Nasta connects Viviani and Minkowski theory in higher dimensions but only its abstract/reference material was inspected. The exact metric identity may have an older equivalent formulation in simplex-coordinate or frame literature; historical exhaustiveness is not asserted.

Same-model review: passed. Independent audit: not yet performed.
