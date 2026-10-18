# Independent mathematical audit

## correctness

PASS

For uniform VOLUME measure on each centered solid, tetrahedron/cube/octahedron have quartic polynomial Q(u)=qΣu_i^4+6pΣ_{i<j}u_i²u_j². Dirichlet integration yields (q,p,R4)=(3/35,1/21,19/35),(1/5,1/9,19/15),(1/35,1/210,4/35), giving η=5(q−3p)/R4=−10/19,−10/19,5/8. For each solid, decomposition into centered face pyramids gives κ=25/21[1+β²(8+4c+3c²)/(180B²)], B=1−β+β(2+c)/6; exact Platonic c,β yield κ values 95/63,19/15,80/63,(338875−37475√5)/211722,(185−15√5)/126. The rotational icosahedral character of harmonic degrees 2 and 4 has zero fixed multiplicity, proving η=0 for dodecahedron/icosahedron. Independent exact SymPy reductions reproduced every κ and the first three η. The source verify.py was actually read: exact symbolic face, Dirichlet, character calculations and supplementary Monte Carlo (not proof). Scope is filled volume, not vertices/surface.

## originality

PASS

Módis–Kovács full eight-page primary 2024 paper handles EXACT fourth-order rotational-invariance classes, so no novelty is claimed for η=0 of icosa/dodecahedron or anisotropy existence for others. It does not give the two-parameter quantitative normalized η/κ table or the tetrahedron–cube equality of directional profiles. Older mechanics papers may include individual cube coefficients, explicitly risked. Complete all-five-body numerical spectrum with radial ratios is not a direct implication of qualitative invariance. Best-of-knowledge originality survives despite cheap individual entries and prior known symmetry.

## value

PASS

Uniform-volume rank-four moment tensors of the five regular solids are canonical integral-geometric invariants. Their complete scale-independent two-number spectrum determines all fourth-order tensor entries; equality of tetrahedral and cubic angular profiles despite differing radial kurtosis is a nontrivial natural comparison, and exact dodecahedral/icosahedral radial ratios complete the list. These numbers are usable precise benchmarks beyond an arbitrary slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
