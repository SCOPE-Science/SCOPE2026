# Independent mathematical audit

## correctness

PASS

The original \(d=1\) uniform Floater--Hormann weights are proportional to \((-1,2,-2,1)\), and the audited cardinal functions follow by direct barycentric simplification. Passing to monotone increments turns the data constraints into a simplex, so for fixed \(x\) the exact attainable interval is obtained from the five increment coefficients \(0,1,c_1,c_2,c_3\). On the left cell only \(c_2\) is negative; maximizing its magnitude reduces to a one-variable rational function whose derivative numerator is the stated strictly decreasing quartic on \([0,1]\), giving one critical point. Reflection gives the right-cell overshoot, and the elementary middle-cell bound is strictly smaller. Elimination yields the displayed quartic polynomial for \(\delta\), with a unique positive root. A fresh dense-grid replay of the exact monotone-simplex extrema reproduced \(-0.1844131164\ldots\) and \(1.1844131164\ldots\) at the reflected locations, consistent with the exact verifier.

## originality

PASS

Floater and Hormann's complete primary paper supplies the exact barycentric construction, pole-freeness, and the \(d=1\) weight formula; those are prior inputs. The inspected source analyzes approximation error and uniform-grid weights but does not formulate monotone-data range preservation or the four-node defect. Targeted searches for Floater--Hormann monotonicity, positivity, shape preservation, range defect, and overshoot found later conditioning/generalization work but no theorem giving this constrained sharp constant or sign-reversal witness.

## value

PASS

Range and sign preservation are central shape questions for interpolation, and the four-node uniform \(d=1\) stencil is the smallest genuinely rational Floater--Hormann configuration. The exact worst monotone-data defect, algebraic extremizer, and strictly increasing positive sign-reversal example form a natural benchmark for deciding when a pole-free interpolant nevertheless violates data bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
