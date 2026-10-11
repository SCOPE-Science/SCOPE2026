# Independent mathematical audit

## correctness

PASS

The rank criterion is correct: a kernel vector with all five time coordinates nonzero and no additional Fourier zeros exists exactly when the kernel is nontrivial, is not contained in any coordinate hyperplane, and is not contained in any extra Fourier-row kernel; finite-union avoidance over \(\mathbb C\) combines these separate noncontainments into one vector. Translation and modulation reduce five-sets and seven-sets independently because their sizes are coprime to 16, giving \(\binom{16}{5}/16=273\), \(\binom{16}{7}/16=715\), and 195195 orbit pairs. The actual exact verifier at blob 7ea1a87b98f5adb3074d13439f8fb1fe31a3d6bf was inspected: determinants are reduced exactly in \(\mathbb Q(\zeta_{16})\) via \(\Phi_{16}(X)=X^8+1\), so rank decisions use integer coefficient vectors rather than floating tolerances. Its reported census is arithmetically consistent: 193416+1779=195195 and 27+1752=1779; the final 136 deletion-surviving rank-four cases all fail an extension test. Thus the finite exhaustive certificate proves the hole.

## originality

PASS

Krahmer, Pfander and Rashkov give the same exact-support rank criterion but explicitly describe the order-16 five-versus-nine nonexistence as numerical evidence requiring singular-value calculations over 49,969,920 five-by-seven submatrices, not as an exact proof. The audited record replaces that numerical observation by an exact cyclotomic-rank exhaustion. Current Resultary searches found the assigned exact certificate and nearby Fourier-support classifications, but no earlier exact proof of this historical hole. Broader prime-power uncertainty results and later no-hole regions do not decide this point, since \(5+9=14<17\).

## value

PASS

This is a motivated finite certification: it resolves a specific hole explicitly highlighted in the foundational uncertainty-diagram paper as numerical only. The exact cyclotomic census removes tolerance dependence from a historically concrete support-pattern question. A single exact finite hole is valuable here because the object is the finite uncertainty diagram itself, not an arbitrary sample from a larger parameter space.

The dated certificate retains the supplied scientific assessment, sources and limitations.
