# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

The moment bound follows from an exact identity, not an asymptotic argument. With a simple zero at the origin,
\[
p(z)=Az\prod_{k=1}^{n-1}(z-z_k),
\qquad
p'(z)=nA\prod_{j=1}^{n-1}(z-\zeta_j),
\]
comparison at zero gives
\(\prod z_k=n\prod\zeta_j\). Since \(|z_k|\le1\), the product of critical radii is at most \(1/n\); arithmetic--geometric mean then proves the sharp bound for every \(\lambda>0\). A multiple zero at the origin makes the reciprocal moment infinite.

The equality analysis was checked separately from the inequality. Equality forces all nonzero zeros onto the unit circle and all critical points onto the circle of radius \(r=n^{-1/(n-1)}\). Both the root polynomial \(q=p/z\) and the rescaled derivative then have all zeros on the unit circle and hence satisfy self-inversive coefficient identities. Combining the two identities yields
\[
\frac{k+1}{n-k}=n^{-1+2k/(n-1)}
\]
for every nonzero coefficient. The logarithmic interpolation function used in `RESULT.md` is strictly concave on the first half of its interval and antisymmetric about the midpoint, so only the two endpoint coefficients and, in odd degree, the middle coefficient can survive.

The remaining quadratic-in-\(z^h\) test is exact. When \(n=2h+1\),
\[
q(z)=z^{2h}+t\eta z^h+\eta^2
\]
has all zeros on the unit circle exactly when \(|t|\le2\), while the normalized derivative has all zeros on the required critical circle exactly when
\[
|t|\le 4\sqrt n/(n+1).
\]
The latter is the stronger restriction. For even \(n\), no middle coefficient exists and only the binomial family remains.

The radial stability identities were rederived from the same exact product relation. They require no compactness argument and remain valid uniformly in \(\varepsilon\). No numerical experiment is used as a substitute for proof.

## Originality

**PASS, to the best of our knowledge.**

The primary 2026 source, arXiv:2609.19126, was inspected at Theorem 1.3, Corollary 1.4, and the endpoint argument in Lemma 8.3. It proves the quadratic Tang--Zhang inequality at every zero, obtains all exponents \(\lambda\ge2\) by power-mean monotonicity, and at the centered endpoint proves
\[
(n-1)^{-1}\sum|\zeta_j|^{-2}\ge n^{2/(n-1)}
\]
by the same constant-term product identity used here. Accordingly, neither that product argument nor the centered quadratic lower bound is claimed as new.

The new claim is the sharp centered theorem for every \(\lambda>0\), especially the subquadratic range, together with the full equality set for the stronger centered bound and the quantitative radial stability. The equality set is materially different from the global Tang--Zhang equality set: odd degrees admit the real one-parameter family in `RESULT.md`.

Targeted searches used the source identifier and title together with `centered zero`, `reciprocal moment`, `power mean`, `critical points same modulus`, `self-inversive derivative`, `unit-circle zeros`, and variants of the sparse family. Searches of the current SCOPE archive by source identifier and equivalent terminology found no overlap.

The strongest older residual-risk literature concerns Smale's mean-value problem under equal critical radii. Hinkkanen--Kayumov explicitly summarize a theorem of Sheil-Small, *Complex Polynomials*, pp. 361--362, and an improvement of Dubinin for polynomials whose critical points have equal modulus. The accessible statements concern bounds for normalized critical values, not classification of polynomials whose nonzero zeros are unimodular while all critical points have the specific radius \(n^{-1/(n-1)}\). The full cited pages of Sheil-Small's book were not independently inspected, so that book remains the most plausible inaccessible source capable of reducing the originality claim. No available metadata gave concrete evidence that it contains the parity-dependent family above.

Classical self-inversive coefficient symmetry, Cohn-type theory, and the elementary quadratic unit-circle criterion are standard tools and are not claimed as new. Because the direct source is recent and the classification is elementary once the equality conditions are isolated, an unindexed concurrent observation also remains possible.

## Value

**PASS.**

The result converts a stronger but unclassified endpoint estimate in the new Tang--Zhang work into a complete sharp picture. It extends the centered reciprocal-moment law to every positive exponent, resolves all equality cases, and reveals a parity bifurcation that is invisible in the global quadratic theorem. The stability inequalities also show that near equality forces every nonzero root radially toward the unit circle and all normalized reciprocal critical radii toward one.

The result does not purport to solve the difficult noncentral \(1\le\lambda<2\) Tang--Zhang problem; its value is a complete theorem at the distinguished symmetric endpoint.

## Limitations

Only the centered zero \(a=0\) is covered. The stability result is radial and gives no angular distance to the extremizer manifolds. The general noncentral subquadratic Tang--Zhang inequalities remain open. The full text of the most relevant older book pages was not independently inspected, so originality remains explicitly to the best of our knowledge. No independent validation, formal proof-assistant verification, or independent audit is claimed.
