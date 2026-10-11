# Independent mathematical audit

## correctness

PASS

The source declares a Caputo-Fabrizio model and its existence section explicitly uses the associated Losada--Nieto integral with a local term plus an ordinary time integral. For the exact scalar rodent-total equation, that integral implies initial compatibility at equilibrium for a continuous solution and otherwise a right jump followed by an ordinary exponential transient. The source's displayed Mittag-Leffler boundedness transient is instead the classical Caputo solution. Likewise, the printed Adams--Bashforth--Moulton method uses the power-law Volterra weights of the Diethelm--Ford--Freed Caputo scheme. An independent algebra replay with positive generic coefficients verifies the CF right-limit and exponential rate, so the operator mismatch is mathematical rather than terminological.

## originality

PASS

The open primary article itself exposes both sides of the inconsistency: it says the model uses Caputo-Fabrizio, writes the CF local-plus-integral relation in the existence section, and reports Adams--Bashforth--Moulton simulations. Diethelm--Ford--Freed explicitly derive their predictor-corrector for the classical Caputo derivative and its power-law Volterra equation. Targeted correction and Resultary searches found no published source-specific operator correction.

## value

PASS

The mismatch affects both analytical boundedness formulas and the entire fractional-order simulation method, while leaving the integer-order endpoint unchanged. It therefore determines which differential operator the published numerical figures actually validate and is a substantive reproducibility issue rather than a minor convention difference.

The dated certificate retains the supplied scientific assessment, sources and limitations.
