# Lowest-channel multiplicity controls spectral-partition attainment on a quantum star
## Finding
Let \(S_m\) be a metric star with finitely many rays \(e_1,\ldots,e_m\), each identified with \([0,\infty)\), and impose the standard continuity--Kirchhoff condition at the central vertex. Let the Schrödinger potential be constant on each ray, \(V|_{e_j}=v_j\ge 0\). Set \(v_*:=\min_j v_j\) and \(r:=\#\{j:v_j=v_*\}\). For the non-covering connected Dirichlet partition convention of Hofmann--Kennedy--Serio, the minimal \(k\)-partition energy satisfies
\[
\mathcal L_k^D(S_m,V)=v_*
\]
for every integer \(k\ge 1\). An admissible \(k\)-partition \((H_1,\ldots,H_k)\) attains this infimum if and only if every cluster \(H_i\) contains an unbounded tail of at least one ray on which the potential equals \(v_*\). Consequently, a minimizing \(k\)-partition exists if and only if \(k\le r\). For every minimizing cluster \(H_i\), one has \(\lambda(H_i)=\Sigma(H_i)=v_*\), but \(v_*\) is not an \(L^2\)-eigenvalue of that cluster.

## Assumptions and scope
The graph has finitely many rays and no finite edges. The edge potential is exactly constant on each ray and is nonnegative. Clusters are connected subgraphs that may be bounded or unbounded, distinct clusters may meet only at boundary points, and the union of the clusters need not cover the whole graph. Dirichlet conditions are imposed at newly created cluster boundary points, with the inherited standard condition at interior vertices. The quantity \(\lambda(H)\) is the bottom of the Schrödinger spectrum on a cluster, \(\Sigma(H)\) is the bottom of its essential spectrum, and \(\mathcal L_k^D\) is the infimum over admissible \(k\)-partitions of the maximum cluster ground energy.

## Proof
For every cluster \(H\) and every form-domain function \(u\),
\[
q_H[u]-v_*\lVert u\rVert_2^2
=\int_H |u'|^2+\int_H(V-v_*)|u|^2\ge 0.
\]
Hence \(\lambda(H)\ge v_*\), and therefore \(\mathcal L_k^D(S_m,V)\ge v_*\) for every \(k\).

For the reverse inequality, choose a ray with potential \(v_*\). For any \(L>0\), place \(k\) mutually disjoint intervals of length \(L\) far out on that ray. Each interval is an admissible connected cluster with Dirichlet endpoints and first eigenvalue \(v_*+\pi^2/L^2\). Thus \(\mathcal L_k^D(S_m,V)\le v_*+\pi^2/L^2\), and sending \(L\to\infty\) proves \(\mathcal L_k^D(S_m,V)=v_*\).

Now fix a connected cluster \(H\). If \(H\) contains an unbounded tail of a ray with potential \(v_*\), translated sine test functions of arbitrarily large support on that tail have Rayleigh quotient \(v_*+\pi^2/L^2\). The preceding lower bound then gives \(\lambda(H)=v_*\). Persson's formula applied outside a compact set also gives \(\Sigma(H)=v_*\).

Conversely, suppose \(H\) contains no unbounded tail of any ray with potential \(v_*\). If \(H\) is bounded, its spectrum is discrete. If \(H\) is unbounded, then outside a sufficiently large compact set it is a disjoint union of tails lying only on rays with potentials strictly larger than \(v_*\); Persson's formula therefore yields \(\Sigma(H)>v_*\). In either case, if \(\lambda(H)=v_*\), then \(v_*\) would be an eigenvalue at the spectral bottom. Equality in the nonnegative quadratic-form identity above would force both \(u'=0\) almost everywhere and \((V-v_*)u=0\) almost everywhere. Such a function cannot be a nonzero \(L^2\) eigenfunction: it vanishes on all higher-potential pieces, and on any remaining finite lowest-potential pieces the boundary and continuity conditions force the constant value to vanish. Hence \(\lambda(H)>v_*\). This proves the cluster characterization.

A minimizing \(k\)-partition must therefore assign a lowest-potential ray tail to every cluster. Two distinct clusters cannot both contain tails of the same ray, because those tails would overlap in an interval of interior points. Thus attainment forces \(k\le r\). If \(k\le r\), choosing one tail on each of \(k\) distinct lowest-potential rays gives an admissible minimizing partition, proving the converse.

Finally, for any minimizing cluster the same quadratic-form equality argument excludes an \(L^2\) eigenfunction at \(v_*\). Thus the common value \(\lambda(H)=\Sigma(H)=v_*\) is a threshold, not a ground-state eigenvalue.

## Verification
The argument is analytic. A standalone standard-library checker in `verify.py` verifies the finite combinatorial part of the attainment criterion and the exact Dirichlet-interval Rayleigh quotient used for the approximating partitions. It is a reproducibility aid rather than a substitute for the proof or for Persson's theorem.

## Relationship to prior work
Hofmann, Kennedy and Serio establish the unbounded-graph partition framework, prove the relevant Persson formula, and in their Example 5.1 treat the zero-potential line and \(m\)-star. In that equal-potential case they prove \(\mathcal L_k^D=\Sigma=0\) for all \(k\) and attainment exactly for \(k\le m\). The statement above extends that model to ray-dependent constant Schrödinger potentials and identifies the multiplicity \(r\) of the lowest asymptotic channel, rather than the total number of rays, as the exact attainment threshold. It also characterizes every minimizing cluster by the presence of a lowest-potential tail and records the absence of a threshold eigenfunction.

Compact-graph partition asymptotics and interlacing results do not address asymptotic channels on unbounded stars. Literature on starlike graphs with potentials for nonlinear Schrödinger ground states and trace formulae for piecewise-constant quantum-graph potentials concerns different spectral questions and does not imply this partition-attainment classification.

## Limitations
The result uses the non-covering partition convention; it is not asserted for a covering-only partition problem. It assumes finitely many rays and exactly constant ray potentials. No claim is made for variable potentials merely converging at infinity, magnetic couplings, nonlinear energies, or graphs with a nontrivial compact core. The originality assessment is based on targeted searches and inspection of the most directly relevant primary sources; an equivalent statement under substantially different terminology remains a residual literature risk.

## References
1. M. Hofmann, J. B. Kennedy, A. Serio, *Spectral minimal partitions of unbounded metric graphs*, arXiv:2209.03658v1; Journal of Spectral Theory 13 (2023), DOI:10.4171/JST/462.
2. M. Hofmann, J. B. Kennedy, D. Mugnolo, M. Plümer, *Asymptotics and Estimates for Spectral Minimal Partitions of Metric Graphs*, arXiv:2007.01412.
3. M. Hofmann, J. B. Kennedy, *Interlacing and Friedlander-type inequalities for spectral minimal partitions of metric graphs*, arXiv:2102.07585.
4. C. Cacciapuoti, D. Finco, D. Noja, *Ground state and orbital stability for the NLS equation on a general starlike graph with potentials*, arXiv:1608.01506.
