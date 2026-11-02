# Independent mathematical audit

## correctness

PASS

Over GF16=F2[a]/(a⁴+a+1), the Hermitian pairing h(v,w)=Σv_i w_i⁴ defines 1105 isotropic projective points among 4369 total; every maximal totally isotropic line has 17 rational points, and independent exhaustive projective enumeration recovered exactly 325 lines. On a smooth quintic surface, adjunction gives self-intersection -3 for each line and any two distinct projective lines intersect once transversely if they meet, giving off-diagonal 0/1. Independently reconstructed the 325×325 Gram matrix from shared-point incidence. Each line has 68 others intersecting it; its line intersection graph is strongly regular with (v,k,λ,µ)=(325,68,3,17), giving adjacency eigenvalues 68 (once), 3 (272 times), -17 (52 times), hence Gram A−3I has rational rank 53. Separate exact modular elimination on the independently reconstructed matrix yielded rank mod2=37, rank mod3=53 and local Smith pivot counts mod4: 37 units plus 16 factors with valuation exactly 1. The resulting 53 nonzero factors exhaust the rational rank, excluding all 2-adic valuations≥2. The cited Shimada/Harashita Hermitian cycle-lattice theorem ensures odd-prime factors do not occur in the nonzero line-lattice discriminant; hence full Smith form diag(1^37,2^16,0^272). Source script verification/hermitian_quintic_smith.py was fully read, and an independently written finite-field and modular-linear-algebra script reproduced the numbers, including the independent srg equation. The general p-primary theorem is used as a mathematical premise rather than falsely inferred from a mod3 check.

## originality

PASS

Harashita, arXiv:2610.01731 (Oct 1 2026), treats these Hermitian line-cycle lattices uniformly. In §6 Corollary 6.2 it bounds each p-adic elementary exponent by νm=2 for the present q=4, m=1; Remark 6.3 expressly says lower bounds/multiplicities are not treated. The exact 1^37 2^16 specialization is not a corollary of those upper bounds, which permit valuation-two factors. Shimada (2001) establishes full rational rank and p-primary discriminant; its complete paper could not be read, so a forgotten exact q=4 example there remains a real priority risk. The published near-match 85-line Yu–Zhu quintic is a different surface and Gram matrix.

## value

PASS

The 325 rational maximal-isotropic lines on a Hermitian quintic are a canonical highly symmetric finite configuration whose intersection lattice is central to algebraic cycles. Their complete integral Smith profile is a precise unknown natural invariant, sharpening the published annihilator bound from 4 to 2, determining the entire 2-primary elementary multiplicity and rank. Such exact structure can be used to test index/saturation predictions and is a motivated complete arithmetic calculation, not an arbitrary tiny instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
