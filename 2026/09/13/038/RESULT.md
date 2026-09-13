# Two-sided certified enclosure of the logarithmic capacity of the third middle-third Cantor prefractal

## Context

The logarithmic capacity of the middle-third Cantor set and its finite prefractal
approximations is a classical hard quantity in logarithmic potential theory. No
closed form is known. Numerical approximations of the limit set exist, but
rigorously certified two-sided enclosures of a fixed prefractal are rare because
they require exact error control for both the energy minimization and the
Frostman minimum principle.

## Definitions

Let `E_3` be the union of the eight closed intervals `[k/27,(k+1)/27]` for
`k in {0,2,6,8,18,20,24,26}`, the third stage of open-middle-third deletion
from `[0,1]`. For compact `E` of positive capacity with kernel `log(1/|x-y|)`,
let `I(mu)` be the logarithmic energy of a Borel probability measure `mu` on
`E`, `V(E)=inf_mu I(mu)` the Robin constant, and `cap(E)=exp(-V(E))` the
logarithmic capacity. For a finite-energy measure `nu`, let `U^nu` be its
logarithmic potential.

## Result

Let `c_3 = cap(E_3)`. Then:

```
0.221 <= c_3 <= 0.230.
```

More precisely the certificates establish `c_3 >= 0.2215368` and
`c_3 <= 0.2292253`. The true value is numerically about `0.2246`
(non-rigorous estimate); no optimality of the trial measures is claimed.

## Proof and evidence

Two standard one-sided tools are used (Ransford, Potential Theory in the
Complex Plane, Theorems 5.1.2 and 5.5.9): every trial probability measure `mu`
gives `V <= I(mu)` hence a lower bound on capacity; and for every trial
probability measure `nu`, `V >= min_{E_3} U^nu` hence
`cap <= exp(-min U^nu)`.

Lower bound: a piecewise-uniform measure on 16 half-interval cells with exact
rational endpoints in `(1/54)Z` and symmetric rational weights
`q_g/2000`, `q=(210,130,111,123,111,89,93,133)`. The averaged kernel has the
closed form with `phi(u)=u^2/2(-log|u|+3/2)`. Summation gives certified
`I(mu) <= 1.507166683 < 1.509592577 <= -log(0.221)`, whence
`cap(E_3) >= exp(-1.507166683) >= 0.2215368 >= 0.221`.

Upper bound: a piecewise-uniform measure on 96 exact rational edge-clustered
cells (rounded-cosine mesh with denominator `27*1728`) and symmetric rational
weights from `upper_weights.json` (total mass 1). The potential has the closed
form with `F(t)=t log|t|-t`. For each probe interval and cell, writing
`s=a-x` and `h(s)=g(s)-g(s+l)` with `g(t)=t log|t|`, `h'(s)=ln|s|-ln|s+l|`
vanishes only at `s=-l/2` with singularities only at `{-l,0}`; splitting there
makes `h` strictly monotone on each subpiece, so the range minimum is the
minimum of split-point values. Summation with certified logarithm enclosures
over 384 probes covering `E_3` gives
`min U^nu >= 1.473049700 > 1.469675970 >= -log(0.230)`, whence
`cap(E_3) <= exp(-1.473049700) <= 0.2292253 <= 0.230`.

All logarithms are enclosed by self-contained exact-rational atanh-series
bounds with geometric remainder in `Fraction` arithmetic; only the Python
standard library is used.

## Limitations

The certified claim is the outer interval `[0.221,0.230]`; the sharper digits
are certified outer bounds as above. The `~0.2246` midpoint is a non-rigorous
mesh estimate. The trial measures are not claimed to be optimal or to be
equilibrium measures.

## Reproducibility

```
python3 output/artifacts/lower_cert.py  # expect LOWER: PASS, cap >= 0.2215368
python3 output/artifacts/upper_cert.py  # expect UPPER: PASS, cap <= 0.2292253
```

Both scripts exit 0 on PASS. Lower bound runs in seconds; upper bound in
minutes on a single core.

## References

- T. Ransford, Potential Theory in the Complex Plane, Theorems 5.1.2, 5.5.9.
- T. Ransford and J. Rostand, Computation of capacity, Math. Comp. 2007
  (limit Cantor set estimate ~0.2209, distinct object).
- V. N. Dubinin and D. Karp, Two-sided bounds for the logarithmic capacity of
  multiple intervals, arXiv:0905.3283 (general formulas, no E_3 enclosure).
- J. Liesen, M. M. S. Nasser and O. Sete, Computing the logarithmic capacity
  of compact sets having many components with the Charge Simulation Method,
  arXiv:2201.10228 (non-rigorous approximations with extrapolation).
