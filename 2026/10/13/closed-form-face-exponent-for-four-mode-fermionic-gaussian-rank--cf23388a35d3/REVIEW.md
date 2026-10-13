# Self-review

## Correctness
PASS. On the face \(w_3=0\), the source weighted Gram matrix has one scalar identity block plus four and three copies of the same two-eigenvalue template in the degree-one and degree-two groups. This gives the displayed entropy formula exactly. Introducing \(r=m/(4-m)\) converts the denominator entropy into a Gibbs variational problem. The Gibbs bound is attained precisely at the unique positive stationary point because the induced mean obeys the same self-consistency relation. The derivative has a single sign change, proving global face optimality and uniqueness. The small-entropy expansion then gives the \(4/3\) coefficient, and binary-entropy asymptotics give the \(16/3\) coefficient in \(t\). Risk: the theorem is intentionally a face optimum and lower certificate; no step assumes it is the global source optimum.

## Originality
PASS. The closest primary source, arXiv:2610.02172v1, defines the full base \(B_t\) through a three-parameter entropy maximization and proves positivity using only the one-dimensional witness \((1-u,u,0,0)\) near \(u=0\). Its inspected theorem and proof do not optimize the larger face \(w_3=0\), state the closed form \(\widehat B_t\), or give its near-Gaussian \(4/3\) entropy-squared law. Targeted published-finding corpus searches under the exact arXiv identifier, weighted-Gram, Gaussian-rank, face-optimization, and asymptotic aliases returned no covering finding. Current and prior own ledgers were also searched for the source identifier and equivalent terminology and contained no overlap. Cudby--Strelchuk's earlier Gaussian-rank work studies finite-copy decompositions and extent, not this tensor-power lower exponent.

Residual risk: because the anchor is extremely recent, an equivalent independent calculation may exist under different terminology or may appear contemporaneously. No claim of exhaustive historical priority is made.

## Value
PASS. The source theorem guarantees an exponential lower base for every nonzero \(t\), but its general \(B_t\) remains an implicit three-parameter optimization, and the published positivity witness gives no quantitative rate as \(t\to0\). The exact \(w_3=0\) solution turns that existence statement into a closed-form certificate usable at every \(t\) and reveals a natural weak-non-Gaussianity scale \(h(\theta_t)^2\sim4t^4\log^2(1/t)\). The face is structurally motivated by the source Gram matrix rather than an arbitrary numerical slice, and the result does not overclaim global optimality.

## Closest literature and limitations
The closest literature is arXiv:2610.02172v1 itself, followed by arXiv:2307.12654v4 on Gaussian rank and extent for matchgate simulation and arXiv:2501.17071v1 on coherent-superposition simulation. The claim is restricted to the source four-mode family and one natural face of its variational lower-bound method.

Self-review: passed. Independent audit: not yet performed.
