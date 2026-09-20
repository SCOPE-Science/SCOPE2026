# Same-model review

**Verdict: PASS**

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The proof was rederived from Heron's formula rather than from the published parametrizations.

The key reduction is
\[
x^2-d^2=3y^2,\qquad K=3xy
\]
for sides \((2x-d,2x,2x+d)\). The normalization by \(g=\gcd(x,y)\) was checked carefully: the equation implies \(g\mid d\); after division, \(\gcd(X,D)=1\), \(D\) is odd, and hence the normalized triangle is primitive. The normalized equation also forces \(X,Y\) to have opposite parity, so every area in this family is divisible by \(6\).

Under \(\omega(K)=2\), all factors \(g,X,Y\) are supported on \(\{2,3\}\). The equation excludes \(3\mid X\), giving \(X=2^A\), and coprimality gives \(Y=3^B\). For \(B\ge1\), the equation
\[
D^2=2^{2A}-3^{2B+1}
\]
is either negative when \(A=1\) or congruent to \(5\bmod 8\) when \(A\ge2\). Thus \(B=0\), after which factorization forces \(A=1,D=1\). The converse scaling family was checked directly.

A separate exact-integer scan over all \(1\le d<x\le3000\) found 6,434 Heronian parameter pairs and exactly 44 with area prime support \(\{2,3\}\); all 44 matched the claimed family and no mismatch occurred. The theorem itself does not depend on this finite cutoff.

## Originality

The following literature and data were checked.

- MacDougall (2003): the available full text was inspected, especially the section giving the equation \(d^2+3y^2=x^2\), the complete primitive parametrization, and the table of primitive HAP triangles. No restriction by the number of prime divisors of the area was located in the inspected text.
- Bailey–Gosnell (2012): bibliographic record and abstract were inspected. The work gives a generation method for all HAP triangles and discusses inradius structure. The full article body was not inspected.
- Read (2025), *On HAP triangles*: the publisher extract and reference list were inspected. The full article was not available for inspection. Because its subject is exactly HAP triangles, it is the most significant residual originality risk.
- OEIS A387908: the current entry on counting integer-area arithmetic-progression triangles by perimeter was checked.
- Exact and synonymous searches were performed around “two prime factors,” “two distinct prime divisors,” “prime support,” “smooth area,” and areas of the form \(2^a3^b\), together with arithmetic-progression/Heronian/HAP terminology.
- Current SCOPE records were searched for Heronian, HAP, arithmetic-progression-triangle, MacDougall, and equivalent terms; no overlapping record was found.

No stronger or equivalent published theorem was located. The originality verdict is therefore **PASS to the best of our knowledge**, not a claim of exhaustive bibliographic certainty. The uninspected full text of Read (2025), and to a lesser extent Bailey–Gosnell (2012), remain the clearest sources that could conceivably contain an equivalent special case.

## Value

The result completely classifies the extremal prime-support stratum of a classical and fully parametrized Diophantine family. Since the area is necessarily divisible by both \(2\) and \(3\), two distinct prime divisors are the minimum possible; the theorem shows this minimum is rigid enough to force a single primitive similarity class and gives every nonprimitive example explicitly.

This is a structural classification without a size cutoff, not a new isolated numerical example.

## Scope limitations

The arithmetic-progression hypothesis is essential. The result makes no classification claim for arbitrary Heronian triangles, nor for HAP areas having three or more distinct prime divisors.
