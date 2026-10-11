# Independent mathematical audit

## correctness

PASS

For a complex vector \(z\), a phase rotation diagonalizes the real/imaginary Gram matrix, reducing \(|\operatorname{Re}(e^{-i\theta}z)|^2\) to \(\lambda\cos^2\theta+(1-\lambda)\sin^2\theta\) with \(\lambda\in[1/2,1]\). For \(0<c\le1/\sqrt2\), the angular set where the real projection exceeds \(c|z|\) has measure at least \(4\arccos c\), with the collinear case extremal. Averaging this indicator estimate and applying Mukherjee’s real-input weak constant \(2\) to \(\operatorname{Re}(e^{-i\theta}f)\), together with \(\int_0^{2\pi}|\operatorname{Re}(e^{-i\theta}w)|d\theta=4|w|\), gives \(2/(c\arccos c)\). Maximizing \(c\arccos c\) yields \(c=\cos\theta_*\) with \(\theta_*\tan\theta_*=1\). Fresh numerical solution gives \(c_*=0.65218462390919\) and \(C_\mathbb C=3.5644502804062665\), matching the claim.

## originality

PASS

Mukherjee’s primary abstract explicitly states the dimension/drift-free constant \(2\) for real-valued inputs. The Euclidean predecessor supplies the same endpoint background. Targeted searches for a quantitative real-to-complex weak-\(L^1\) transfer with the angular constant, including searches under complexification and rotation terminology, did not locate an equivalent theorem; the published SCOPE corpus likewise returned the audited record rather than an earlier equivalent. Because the proof is an abstract rotation lemma, an older functional-analytic formulation under different terminology remains a genuine priority risk, but no inspected source implies the specific constant.

## value

PASS

Extending a newly sharp real endpoint to complex data is a natural analytic gap, and the optimized rotation argument gives a universal constant strictly below the naive real/imaginary split value \(4\). The phase-measure lemma is reusable for Hilbert-valued complexifications and the optimization identifies the exact constant of this method. This is more than a notation change or routine componentwise estimate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
