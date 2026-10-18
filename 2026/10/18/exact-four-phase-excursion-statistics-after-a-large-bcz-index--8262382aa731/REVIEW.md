# Review: exact BCZ cusp-excursion statistics

## Correctness — PASS

The stated BCZ cylinder has an exact, invertible rational parameterization by a unit square with Jacobian \(4/(k+t+s)^3\). Following the forced digit \(1\), the branch \(2\) acts by translation in denominator coordinates and its first escape is exactly the ceiling of \((k+s-3t-6)/4\). The three rational triangle integrals evaluate to the stated probabilities. An exact Fraction implementation independently replayed 8,160 admissible rational starts. The proof, not finite sampling, covers all integers \(k\ge12\).

## Originality — PASS, with disclosed access risk

Artiles–Best–Bordignon (2026) prove mixing of the same transformation but do not give a moving rare-digit conditional law. Hall–Shiu (2003) give a one-digit marginal; Augustin–Boca–Cobeli–Zaharescu (2001) treat fixed spacing windows. Korolev (2025) applies related itinerary polygons in colored Farey problems. Searches did not identify this specific four-phase closed formula or a statement directly implying it. Korolev's 89-page full text could not be materially inspected; general polygon machinery may cover more than the accessible descriptions reveal. This is a residual priority risk, not a claim that all related sources have been fully checked.

## Mathematical value — PASS

The exact probabilities quantify a canonical *growing-time cusp excursion* after an unusually large Farey index, rather than an arbitrary slice of a coding problem. The explicit \(k\bmod4\) phase variation survives when the index tends to infinity and is not determined by strong mixing. The result is self-contained and finite-time; it neither asserts a mixing rate nor assumes that independent validation has occurred.

## Limits

Only the first run of the digit \(2\) after an initial index \(k\ge12\) is classified. No statistics of subsequent runs are claimed, and no source's inaccessible text is certified to be non-covering.

Self-review: passed. Independent audit: not yet performed.
