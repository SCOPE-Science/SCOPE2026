# Mathematical review

**Correctness — PASS.** The three projector entry formulas are exact; rational positivity identities prove all off-diagonal signs, an exact minimum proves the eleven-vertex safe regime, rational timestep witnesses prove negativity from twelve vertices onward, and Descartes' rule proves there are exactly two positive diagonal zeros. Exact matrix-inverse and symbolic checks are reproducible with `verify_radau.py`. No finite test is used to infer the infinite result.

**Originality — PASS (qualified).** The inspected Lóczi–Ketcheson (2013) text addresses rational absolute-monotonicity bounds, and Bonaventura–Della Rocca (2015) analyzes TR-BDF2 positivity. Previously documented Crank–Nicolson and Gauss–Legendre Padé matrix results use different stability functions and do not imply the present two-interval Radau result. Comparable published-record searches included [2/2] Padé and SSP-SDIRK endpoint studies and found no matching implication; specialized unindexed coverage remains possible.

**Mathematical value — PASS.** This is a complete natural network-family classification, not a finite extrapolation: the sharp twelve-state onset and reentrant timestep domain distinguish endpoint positivity from classical A- and L-stability, making a concrete strong-stability design issue exactly decidable.

**Limitations.** All edge conductances and part sizes are uniform; internal RK stages, nonlinearity, and arbitrary generators are outside scope. Independent validation has not occurred.

Self-review: passed. Independent audit: not yet performed.
