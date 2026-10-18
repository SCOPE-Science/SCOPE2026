# Independent mathematical audit

## correctness

PASS

For any finite field F_q, m>=2, evaluation of m square-free monomials M_i=product_{j!=i}X_j over full affine F_q^m is injective by testing the point with exactly x_i=0. If coefficient support size is r, contributions from points with one zero coordinate are r(q-1)^(m-1). On the torus change variables y_i=a_i/x_i: additive-character orthogonality gives N_r=[(q-1)^r+(q-1)(-1)^r]/q zero sums. Weight therefore w_r=(q-1)^m-(q-1)^(m-r)N_r+r(q-1)^(m-1), with multiplicity C(m,r)(q-1)^r. The difference w_{r+1}-w_r=(q-1)^(m-1)+(-1)^r(q-1)^(m-r) yields w1=w2 and all claimed q=2 and q>2 collisions. Independent enumeration of all evaluations for (q,m)=(2,2),(2,4),(2,6),(3,2),(3,4),(5,3) matched full histograms, including [81,4,24]_3 W=1+32z^24+32z^36+16z^42. Infinite prime-power scope rests on additive character identity, not enumerated fields.

## originality

PASS

Carvalho–López–San-José 2025 preprint/2026 journal open article defines same family and proves generalized Hamming weights or extremal minimum-support quantities; direct inspection of the complete HTML shows it does not enumerate number of single codewords by each Hamming weight. Patanker–Singh concerns toric and GHW variants. Published Resultary similar records address different affine-half and code families; no stronger exact all-Hamming-weight formula was found. General character sum identities are prior technology and could implicitly encode this spectrum, a noted risk.

## value

PASS

The full Hamming enumerator of a natural extremal square-free evaluation-code degree controls error/erasure performance and dual enumerators and refines the already studied generalized minima. Every coefficient-support layer receives an exact multiplicity for every prime power q and arbitrary m, with distinctly different binary weight collisions; this structural family theorem is not a known-table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
