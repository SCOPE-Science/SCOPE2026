# Independent mathematical audit

## correctness

PASS

For nonnegative neighboring secants \(a,b,c,d\), the Akima derivative is a weighted average of \(b,c\). The displayed algebra proves the sharp enough universal estimate \(0\le m\le(a+b+c+d)/2\), including the zero-weight convention. On a uniform grid the four secants telescope, giving \(0\le h m_i\le M/2\). In the Hermite representation, the data-value basis functions are a convex pair, while the two derivative basis functions have signs \(+,-\); their extrema are \(4/27\), so the interpolant lies between \(-2M/27\) and \(M+2M/27\). The explicit monotone family has endpoint derivatives \(\varepsilon\) and \(1/2-2\varepsilon\) and value \((104\varepsilon-2)/27\) at \(t=2/3\), approaching the lower endpoint; reversal-complement symmetry gives the upper endpoint. I independently checked the derivative lemma on the exact integer box \(0\le a,b,c,d\le8\) and the rational sharpness witness, including the strictly positive transformed value \(-2/75\).

## originality

PASS

Akima's original work introduces the local cubic rule; Fried--Zietz explicitly report that Akima interpolation can significantly overshoot abrupt data, so qualitative overshoot is prior. Fritsch--Butland pursue a different derivative rule designed to preserve monotonicity. Targeted web and Resultary searches did not locate the sharp \(2/27\) global range constant, the half-four-secant derivative lemma, or an equivalent extremal Hermite formulation for the original uniform Akima rule. Because the original 1970 article was not recovered in complete verified text and the authorized institutional attempt returned an operational error, it remains a named residual risk rather than being treated as evidence of noncoverage.

## value

PASS

Akima interpolation remains a standard local cubic method, and overshoot on monotone bounded data is a longstanding practical limitation. An exact, scale-free global defect with a sharp family and a strictly positive-data undershoot witness gives a useful method-level stability invariant and a quantitative benchmark for shape-preserving modifications.

The dated certificate retains the supplied scientific assessment, sources and limitations.
