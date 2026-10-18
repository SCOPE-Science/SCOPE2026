# Independent mathematical audit

## correctness

PASS

For the stated even rational window g(x)=(x^2-1)/((x^2+1)(x^2+4)(x^2+9)) and alpha beta=4/5, the modulus-integer fiberization yields a continuous 4-by-5 matrix M_{j,t}=sum_m g((j+4m-4t/5)/beta). Reflection j->4-j, t->5-t decomposes row space into dimensions 3 and 1, and its even 3-by-3 block B has exactly the supplied h_beta coefficients; recomputed the reflection basis entries. The absolutely convergent Cauchy-series partial fractions give h_beta. Independently evaluated determinant at beta=3/20 as +2.1035333493165e-6 and beta=7/20 as -5.68237067634317e-6; the pinned verify_gabor_4_5.py uses rational interval bounds for pi, exp, cosine and the determinant, and its rational truncation/tail arguments were inspected. IVT yields a singular fiber for an intermediate beta. Local uniform convergence ensures continuity of fibers, hence singularity forces arbitrarily small singular values on positive-measure neighborhoods and excludes a positive Gabor frame lower bound. Proof establishes existence at one beta, not all beta at this product.

## originality

PASS

Best-of-knowledge PASS with material residual risk. The primary Ghosh 2026 abstract and identified statements treat exactly this window, prove the indices through p=3, and report numerical evidence for p=4; a numerical plot/sign scan is not a rigorous sign certificate. Existing parity/fiber reduction is acknowledged as prior art, but certified opposite determinant signs and consequent actual 4/5 non-frame theorem are distinct. The full Ghosh preprint was not accessible through attempted public copies; the authorized institutional download returned a disconnected-VPN blocker, so no whole-paper noncoverage is asserted. A previously unnoticed proof in that paper would alter originality; the assessment depends on the stated index separation and observed primary abstract.

## value

PASS

PASS. Rigorously settling the first remaining index in a naturally stated rational-density Gabor non-frame conjecture for the exact studied generator is a motivated advance. The exact sign certificate converts tentative numerical evidence into a theorem, while the finding expressly stops short of all p.

The dated certificate retains the supplied scientific assessment, sources and limitations.
