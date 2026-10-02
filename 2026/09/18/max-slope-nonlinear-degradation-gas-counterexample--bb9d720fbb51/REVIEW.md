# Review status

Fresh independent mathematical audit: **passed**.

- Correctness: **PASS** — The counterexample was reconstructed analytically. The localized bump is disjoint from \(x_*=1\), so \(h_A(1)=h_A'(1)=1\), while the bump lies inside the invariant interval and makes \(\max_{[m,M]}h_A'=1+A\). Also \(L_g=2\) and \(f(1)=e^{-0.01}\), so the conjectured quantity is \(<2e^{-0.01}/(1+A)\), below \(0.019605\) already at \(A=100\), for every delay. The source linearization has \(\mathcal A=1.01\) and \(\mathcal B=2e^{-0.01}\), giving the source critical-delay formula \(\tau_*=1.236578022\ldots\). Thus \(\tau=2\) is linearly unstable although the proposed GAS test is satisfied. The interval check \(F_A(1.501)=1.63198<g(0)=1.97408\) and monotonicity put the bump inside \([m,M]\).
- Originality: **PASS** — The primary 2026 JMAA paper was inspected through the relevant full web text and explicitly says that replacing the linear \(\mu\) by \(\max_{[m,M]}h'\) is a conjecture for which the authors have no proof. Fresh Resultary search returned the assigned counterexample but no stronger or earlier published SCOPE resolution, and targeted web searches found no correction or counterexample to this precise conjecture.
- Value: **PASS** — The construction refutes a concrete recent stability conjecture by an arbitrarily strong margin and identifies the structural error: a remote maximum derivative is not a lower damping rate at the equilibrium. This is a motivated counterexample with a reusable boundary lesson.

Detailed comparisons and limitations are in `INDEPENDENT_AUDIT_2026-10-01.md` and `INDEPENDENT_AUDIT_2026-10-01.json`.
Earlier same-model evidence remains preserved in `AUDIT.json` as historical evidence.
