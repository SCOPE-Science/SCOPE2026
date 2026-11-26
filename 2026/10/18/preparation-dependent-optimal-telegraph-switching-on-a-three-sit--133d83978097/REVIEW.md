# Independent mathematical audit

## correctness

PASS

An independent closure uses G=diag(ξ₁,1,ξ₂) and σ=GρG. Between flips the Hamiltonian of σ is the fixed hopping matrix; a flip conjugates σ by the deterministic diagonal reflection on the corresponding endpoint. Since each flip intensity is λ independently of the state, averaging gives the fixed commutator plus λ times each reflection-conjugation minus identity. The diagonal is unchanged, and the damping is 2λ for each imaginary nearest-neighbor coherence and 4λ for the real end-to-end coherence. This yields the closed real system with c_jk=−Im σ_jk, D=Re σ₁₃, and the two reflection-sector factors. Both factors are Hurwitz for all λ>0. The two shifts in RESULT.md lines 48–57 give strictly positive cubic Routh–Hurwitz margins 8a²λ and 4λ(6λ−5δ_Q)(2λ−δ_Q). Endpoints excite the slower quadratic: its transform is proportional to (z+2λ)/Qλ(z), with no cancellation. At the center this sector is absent, and Pλ(z)=z[(z+2λ)(z+4λ)+2a²]+6a²(z+4λ), which excludes a common root with the center numerator. A noncancelled multiple pole produces the polynomial prefactor; the limsup yields the real-part exponent even with oscillatory zeros. Below the unique discriminant crossing the real root is −u with 3λ<u<4λ (evaluate Pλ at these two endpoints). Writing w=u/λ−3 gives t²=8w/[(3+w)(1−w²)], increasing on (0,1), and normalized cubic gap t(3−w)/2. The derivative of its square with respect to w has sign 9(1−w)+7w²+9w³. Above the crossing the depressed cubic has two positive y roots and one negative y root. The largest z root −g therefore has 0<g<2λ. Its simple-root derivative has the sign of −g(3g²−16λg+24λ²)/(3λ−g), strictly negative. At the crossing the positive double y root is the slow root, with a genuine double pole proving defectiveness. Independent bisection of 32+t²(−21+t²(24−4t²)) on [2,3], then evaluation of 2t−sqrt((4t²−8)/3), gives t≈2.3008118172002835, gap≈2.505998025926741, versus √2≈1.4142135623730951. No finite-grid inference is used. The supplied verifier was inspected, not run; its counter of 100 includes 90 population comparisons and ten spectral checks (its printed label overstates the number of population comparisons).

## originality

PASS

The supported distinct claim is the combined exact observable-sector result: localized endpoint versus center on the equal-hop, independently switching, stationary telegraph chain, with distinct unique optimizers of the logarithmic ensemble population exponent and a center slow-root collision. The noise model, stochastic Liouville method and the broad principle that noise optima can depend on preparation are not claimed as new. Closest indexed analogues optimize a different observable or channel. No equivalent or implying theorem was found in the inspected material; this is not a historical priority guarantee.

## value

PASS

The same physical generator has different optimal observable relaxation rates when localized preparation suppresses its slower reflection sector. The two strict global optima and their exact values, and the center exceptional point visible without relying on numerics, supply a concrete benchmark for when a generator-gap optimization mispredicts an experiment that measures populations. This is a distinct, motivated exact result even for three sites.

The dated certificate retains the supplied scientific assessment, sources and limitations.
