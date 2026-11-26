# Independent mathematical audit

## correctness

PASS

For the final files, the Euler update is nonnegative and bounded by the interpolation between 1-h*delta_i and h*tau*L_i, both at most one. At equilibrium the response ratio is zero precisely when the input polynomial vanishes; nonnegative terms with positive coefficients give exactly the Boolean support condition. The response from half-density dominates half-density on every fixed support when tau>=tau_* and is zero off it; monotone iteration gives a limit with exactly that support. The Boolean iterates descend and contain all fixed supports. With empty core, the first deleted layer has no input, and every input monomial on the next deleted layer contains a coordinate from an earlier layer. Unrolling the one-step decay recurrence gives the claimed bound with the stated C_k and rho (strictly between zero and one). A nonempty core itself is a fixed support, so a nonzero equilibrium at a large common scale contradicts extinction at every scale. The original assertion that excluding dyadic terms is essential was unsupported and false as a necessity assertion: no step uses the lower bound two, rather than one, on parent-set size. The corrected statement keeps the original purely higher-order model. The original test included a duplicate terminal empty set and so used a weaker envelope than claimed, and its printed equilibrium wording exceeded what was computed. The replacement tests Boolean supports and subsolutions, and indexes the bound by the true layers. An independent in-memory implementation checked 4096 patterns (6753 fixed supports, 1439 empty cores), and verified the individual layer bounds for masks [31,27,24,0] at every time 0 through 100. No submitted script was executed.

## originality

PASS

The final claim does not take credit for generic greatest-fixed-point iteration. The inspected model and graph-family precedents do not give the simultaneous partial-support classification together with the all-scale extinction equivalence and explicit layer-wise trajectory estimate. This passes on the checked statement-level evidence, not on an inference from sparse search returns.

## value

PASS

In this deterministic model a finite Boolean computation settles a universal-in-scale extinction question, where a rate-specific spectral condition does not suffice. It also separates which partial equilibrium supports are topologically possible from the small-scale quantitative question, and quantifies decay via the removal depth. This is a structural classification, not merely a sufficient bound from enumerated examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
