# Same-model review

## Correctness
PASS. For \(\gamma\le1\) and \(\sigma>0\), \(V=\tfrac12[x^2+y^2+(2-\gamma)z^2/\sigma]\) is positive definite and proper. Direct expansion yields \(\dot V=-x^2-(y-z)^2-(1-\gamma)z^2\). Negative definiteness proves the strict case; at \(\gamma=1\), the largest invariant subset of \(x=0,y=z\) is the origin because \(\dot x=y^2\). For \(\gamma>1\), explicit nonzero equilibria disprove global attraction. The compact-invariant-measure statement follows from integrating the same defect and applying invariance of support.

## Originality
PASS with a stated residual literature risk. The 2023 source fixes \(\gamma=20\) for its uncontrolled chaotic example and focuses on feedback stabilization. The 2017 same-model paper establishes equilibrium/local bifurcation structure and numerical convergence for \(0<\gamma<1\), but not the global Lyapunov theorem or the nonhyperbolic endpoint proof. The 2026 same-model stability paper identifies the local threshold \(\gamma=1\), but the inspected material does not contain this global storage identity or compact-invariant-measure rigidity. published-finding corpus searches for the exact model and threshold returned no same-model finding.

## Value
PASS. The result turns a repeatedly used chaotic-motor benchmark into a sharp closed parameter theorem. It separates the uncontrolled regime where recurrent dynamics are impossible from the regime where nonzero equilibria already obstruct global attraction, and it resolves the nonhyperbolic boundary exactly rather than by simulation. This supplies a useful baseline for interpreting chaos-control studies of the same normalized PMSM.

## Closest literature and limitations
The closest source-level comparison is He (2017), which reaches the same equilibrium threshold and reports numerical global dynamics but only derives local stability/bifurcation conditions. The later Hunaish et al. (2026) study also locates the threshold at \(\gamma=1\). The theorem here is limited to the uncontrolled zero-load model with \(\sigma>0\); an inaccessible older proof in an equivalent normalization remains possible.

Same-model review: passed. Independent audit: not yet performed.
