# Independent mathematical audit

## correctness

PASS

For fixed \(\sigma\in[0,1]\), all four printed shares are nonnegative and their sum is identically one for every \((\alpha_1,\alpha_2)\in[0,1]^2\). The reported coordinates satisfy \(0.6242+0.8157=1.4399\), so they are valid under the share map but excluded by the later triangle. On the square, every point has objective at least the maximum of the two coordinatewise minima, and choosing independent minimizers attains that lower bound. Fresh exact-rational replay verifies the numerical witness; the universal identities are symbolic.

## originality

PASS

The initiating paper itself supplies the inconsistent statements: its four nested shares already exhaust one resource pool for every independent pair of within-stratum splits, yet it later imposes a triangle and then reports a numerical policy outside that triangle. Broader epidemic-allocation literature does not imply this source-specific correction, and targeted exact-ratio and correction searches found no prior correction. The finding is therefore best-of-knowledge original as a diagnosis of this model, not as a new theorem about simplices.

## value

PASS

This is not merely a normalization check: the extra triangle deletes valid policies, excludes the source's own reported optimum, and converts two independent within-stratum choices into an artificial tradeoff. Correcting it materially changes the optimization problem and reproducibility of the model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
