# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The argument uses the source system exactly as published. The quadratic identity
\[
\frac12\frac d{dt}(\|a\|_2^2+\|c\|_2^2)
=-d_1\|\nabla a\|_2^2-d_3\|\nabla c\|_2^2-\int b(c-a)^2
\]
is the same dissipative identity used in Proposition 2.5 of Nguyen--Tang, but it is applied here without assuming the boundary-only mass regime. The source's uniform boundedness and heat regularization justify decay of \(\|\nabla a\|_2\) and \(\|\nabla c\|_2\). The conservation laws then reduce all possible long-time limits to two branches. The scalar identity \(B'=\int b(c-a)\) rules out any third branch, while a mean-zero energy estimate for \(b-B\) proves convergence of the catalyst component on the positive branch.

The decisive basin argument was stress-tested against the invariant face. If \(B_0=0\), nonnegativity forces \(b_0\equiv0\), and uniqueness preserves that face exactly, so convergence to the boundary equilibrium is unavoidable. If \(B_0>0\) and boundary convergence were assumed, heat-semigroup smoothing upgrades the already established \(L^p\) convergence of \(a,c\) to uniform convergence. Since the boundary gap is \(2M_2-M_1>0\), eventually \(c-a\) is uniformly positive and hence \(B'\ge b_*B\), contradicting the conserved upper bound \(B\le M_2\). No positivity stronger than positive total catalyst mass is used.

The edge cases were checked explicitly. The argument includes \(M_1=M_2\), where the boundary equilibrium is \((0,0,M_2)\), and excludes \(M_1=2M_2\), where the two equilibria coalesce and the repelling gap vanishes. The eventual exponential statement is not claimed as a new global rate: it follows only after global convergence places the trajectory inside the local stability neighborhood already proved in the source.

## Originality

**PASS, to the best of our knowledge.** The final open-access 2026 article was inspected directly. It states that in the coexistence regime \(M_2\le M_1<2M_2\), local stability of the positive equilibrium and Lyapunov instability of the boundary equilibrium do not rule out a later return to the boundary, and it explicitly formulates global convergence to the positive equilibrium as a conjecture. The literal conjecture says "non-negative initial data", which includes the invariant face \(b_0\equiv0\); the source does not state the sharp catalyst-mass exception or the basin classification proved here.

Searches used the exact article title, DOI 10.1007/s00033-026-02847-0, arXiv:2410.22928, the reaction terms \(b(c-a)\), catalyst/boundary-equilibrium terminology, the mass regime, and global-attractor/convergence formulations. No later correction, corrigendum, or paper was found that proves the source-specific global basin dichotomy or repairs the conjecture in this way. Searches for the exact reaction network \(A+B\to C\), \(B+C\to A+2B\) likewise did not identify prior coverage.

The general ingredients--Poincare--Wirtinger, heat-semigroup smoothing, scalar Gronwall estimates, and Lyapunov dissipation--are standard and are not claimed as new. The originality claim is only the source-specific global classification and the sharp identification of \(\int b_0>0\) as the necessary and sufficient condition selecting the positive equilibrium in the coexistence mass class.

No specific inaccessible paper was identified as a high-probability source of direct coverage. The most relevant primary source is open access and its full HTML theorem/proof text was inspected. As usual, the literature search cannot exclude an equivalent argument under substantially different terminology.

## Value

**PASS.** The result converts the source's unresolved local-versus-global question into an exact basin theorem. It is stronger than merely showing that the boundary equilibrium is unstable: it proves that the boundary basin is precisely the catalyst-free invariant face, while every positive catalyst mass selects the positive equilibrium. It also corrects an unavoidable exception in the literal wording of the published conjecture and recovers eventual exponential convergence by linking the global argument to the source's local theorem.

## Limitations

The result is restricted to system (1.1) in the source setting with homogeneous Neumann boundary conditions. It does not cover the source's second symmetric network, other reaction graphs, the coalescence case \(M_1=2M_2\), or provide a new explicit global exponential rate from the initial time. Originality is asserted only to the best of our knowledge.
