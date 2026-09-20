# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The key identities are exact. For \(q\ge0\) and \(k\in\mathbb Z\),
\[
|z|^{2q}\psi(z)^k=z^{q+k}\bar z^{q-k},
\]
whose index sum is \(2q\), and
\[
z|z|^{2q}\psi(z)^k=z^{q+k+1}\bar z^{q-k},
\]
whose index sum is \(2q+1\). Thus equality of one positive-definite extension
gives all Fourier coefficients of the two families of pushed-forward
measures on \(\mathbb T\).

The positive pushed-forward measures and the complex \(z\)-weighted
pushforwards are finite. The latter use
\(\int |z|^{2q+1}d\mu<\infty\), obtained by Cauchy--Schwarz from finite mass
and a sufficiently high even radial moment. Fourier uniqueness on the circle
therefore applies.

Disintegration over the common angular pushforward is legitimate on the
standard Borel spaces involved. The conditional identities hold
simultaneously for all nonnegative integer \(q\) after removing one common
null set. On a finite fiber, Vandermonde inversion recovers the mass assigned
to every distinct value of \(|z|^2\). At a fixed angle modulo \(\pi\) and a
fixed radius, there are at most two possible points, \(\zeta\) and
\(-\zeta\); the additional \(z\)-weighted equations recover the difference
of their weights, so the conditional measure is unique.

For the algebraic application,
\[
r\mapsto p(re^{it},re^{-it})
\]
is a one-variable polynomial and has nonzero constant term \(p(0,0)\).
Hence it cannot vanish identically on a radial line and has finitely many
zeros there. The source paper's Theorem 22(i)--(ii) supplies support
localization, existence of \(\Gamma(\mu)\), vanishing of the circle component,
and surjectivity; the finite-ray theorem supplies the missing injectivity.
The cardinality and singleton consequences then follow exactly as stated.

The argument was stress-tested against the two principal possible losses of
information: multiple radii on one angular fiber and antipodal points at the
same radius. The even-total-degree moments resolve the first by Vandermonde
inversion, while the odd-total-degree moments resolve the second.

## Originality

**PASS, to the best of our knowledge.** The primary 2019 paper was inspected
at the theorem, geometric criterion, examples, and final open-question
sections. Its Theorem 22(v) and Corollary 23 require injectivity of
\(\psi_p\), equivalent to at most one intersection point with each line
through the origin. The paper explicitly observes that familiar algebraic
curves and polynomial automorphisms can violate this condition.

Searches covered the exact title and DOI, the singleton-\(\mathsf{PDE}\)
question, positive-definite extensions on the upper-diagonal lattice,
algebraic-support determinacy, finite fibers, finite radial intersections,
and equivalent geometric wording. A 2020 survey of Szafraniec's work
discusses the determinacy/extendibility paper but does not state the
finite-fiber strengthening. A 2025 paper on a dynamic inverse formulation of
a complex moment problem works with a different one-index moment setup and
does not address these positive-definite extensions.

No accessible source located through the publication date removes the
\(\psi_p\)-injectivity hypothesis for all algebraic zero sets avoiding the
origin. No specific inaccessible paper was identified as especially likely
to contain this exact strengthening. Residual risk remains from differently
phrased, unpublished, or poorly indexed work.

## Value

**PASS.** The source paper presents its algebraic theorem as a partial answer
to a determinacy-from-extendibility question and singles out the radial
injectivity condition geometrically. The present theorem replaces
one-point fibers by finite fibers and shows that, for algebraic zero sets
avoiding the origin, finiteness is automatic. Consequently the strongest
algebraic conclusions hold without the restrictive injectivity assumption,
including curves such as the polynomially transformed parabola discussed by
the source.

The proof also isolates a reusable mechanism: the even levels of the
upper-diagonal extension encode conditional squared-radius moments, while
the odd levels encode enough signed information to split antipodal masses.

## Scientific limitations

The full open problem is not solved. Finite ray fibers are essential to the
present Vandermonde step, and the algebraic corollary assumes an algebraic
zero set that excludes the origin. A support containing a whole radial line
can have an infinite \(\psi\)-fiber and lies outside the argument. The result
is uniqueness-only and gives no quantitative stability bound for noisy or
truncated moment data. Independent audit has not yet been performed.
