# Scientific review: sharp two-outfall oxygen-deficit phase diagram

## Correctness — PASS

The domain is fully specified: two positive BOD increments in a saturated, constant-flow, no-settling Streeter–Phelps river, with fixed rates \(0<a<b\), separation \(s>0\), and secondary-to-first load ratio \(k>0\). Superposition produces the continuous oxygen deficit. The derivative before the second outfall has one zero at \(t_0\); the derivative after it is a difference of two exponentials and can have at most one zero. The sign of the right derivative at the second outfall proves the exact second-peak criterion, including equality cases. The critical load curve is strictly increasing then decreasing; its derivative and second derivative yield both reentrant intervals and the fold expansion. A direct logarithmic inequality proves the sharp \(e^{-2}\) universal bound. The bundled standard-library script checks the exact rational example and 15,000 randomized compositions and derivative classifications. These tests cannot prove the infinite parameter classification; the analytical proof does.

## Originality — PASS with documented priority risk

The accessible full Streeter–Phelps 1925 bulletin establishes the single-outfall oxygen-sag equations and discusses additional upstream pollution; those known equations are not claimed as new. Bhargava's 1986 compounded-sag and 2007 multi-outfall overlapping-settling treatments are especially relevant. Public bibliographic and abstract information was inspected but complete texts were inaccessible. Arbabi–Elzinga–ReVelle (1974) provides critical-deficit convexity for the classical sag; its available abstract does not state the sharp reentrant count. The present comparison is at theorem/implication level: the result determines the global number of distinct strict local maxima as a function of source separation, derives two separation boundary branches and their square-root merger, rather than only giving a single critical point or a composite concentration profile. More general exponential-kernel or hidden multi-outfall results could imply the claim and historical uniqueness is not asserted. See AUDIT.json for search strings, distinctions, inspected materials, and residual risks.

## Mathematical value — PASS

For an ecologically motivated linear transport model, whether two inflows produce one or two downstream oxygen minima is a concrete geometric classification. The unexpected two-sag / one-sag / two-sag reentrance as separation increases at small load ratios is more informative than a single new parameter example. The sharp universal contrast bound and fold laws give the complete parameter boundary. This does not establish field-scale validity, water-quality threshold violations, or optimal sampling under noisy observations.

## Closest literature and limitations

Sources: Streeter–Phelps, U.S. Public Health Bulletin 146 (1925), printed pp. 18–21; Bhargava, *Modelling for compounded DO sags* (1986); Bhargava, *DO Sag Model for Extremely Fast River Purification* (1986); Bhargava, *Dissolved oxygen sag analysis for a settling fields overlapping type multi-wastewater-outfall* (first publicly available 6 September 2007), DOI:10.1007/s10669-007-9120-x; Arbabi, Elzinga and ReVelle, *The Oxygen Sag Equation: New Properties and a Linear Equation for the Critical Deficit* (1974). Only the 1925 primary scan was fully accessed; the other listed sources were examined through lawful abstracts or bibliographic records. All claims concern strict local maxima in the ideal model, not the worst global deficit or downstream ecological harm.

Self-review: passed. Independent audit: not yet performed.
