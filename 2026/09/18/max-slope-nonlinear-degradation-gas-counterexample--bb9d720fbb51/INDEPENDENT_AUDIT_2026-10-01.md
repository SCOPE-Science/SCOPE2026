# Independent mathematical audit — SCOPE-20260918-bb9d720fbb51

Final disposition: **PASS**.

## Correctness
**PASS** — The counterexample was reconstructed analytically. The localized bump is disjoint from \(x_*=1\), so \(h_A(1)=h_A'(1)=1\), while the bump lies inside the invariant interval and makes \(\max_{[m,M]}h_A'=1+A\). Also \(L_g=2\) and \(f(1)=e^{-0.01}\), so the conjectured quantity is \(<2e^{-0.01}/(1+A)\), below \(0.019605\) already at \(A=100\), for every delay. The source linearization has \(\mathcal A=1.01\) and \(\mathcal B=2e^{-0.01}\), giving the source critical-delay formula \(\tau_*=1.236578022\ldots\). Thus \(\tau=2\) is linearly unstable although the proposed GAS test is satisfied. The interval check \(F_A(1.501)=1.63198<g(0)=1.97408\) and monotonicity put the bump inside \([m,M]\).

## Originality
**PASS** — The primary 2026 JMAA paper was inspected through the relevant full web text and explicitly says that replacing the linear \(\mu\) by \(\max_{[m,M]}h'\) is a conjecture for which the authors have no proof. Fresh Resultary search returned the assigned counterexample but no stronger or earlier published SCOPE resolution, and targeted web searches found no correction or counterexample to this precise conjecture.

### Equivalent formulations
The counterexample attacks the literal conjecture, not a weaker rephrasing.

### Broader coverage
No inspected broader theorem repairs the conjecture under the same hypotheses or already supplies this remote-bump counterfamily.

### Exact database or table
The problem is theorem-level rather than a database value; the search is supporting evidence only.

### Claim versus prior implication
The assigned counterexample is not implied by the source; it negates an open assertion made there.

## Value
**PASS** — The construction refutes a concrete recent stability conjecture by an arbitrarily strong margin and identifies the structural error: a remote maximum derivative is not a lower damping rate at the equilibrium. This is a motivated counterexample with a reusable boundary lesson.

## Source inspections
- **Global stability and periodicity in a delay differential model** (DOI 10.1016/j.jmaa.2026.130555): full relevant web text including the sentence after Theorem 3.6 and the local-instability discussion Assessment: PRIMARY_SOURCE_OPEN_CONJECTURE. Evidence: The paper states: the authors believe Theorem 3.6 extends to nonlinear monotone \(h\) with \(\mu=\max h'\) and currently have no proof.

## Residual risks
- Search cannot exclude unindexed simultaneous work after publication, but no competing resolution was located.
- The result refutes only the literal max-slope extension; it does not classify valid nonlinear GAS criteria.
