# A normalized finite-topology discrepancy has no dimension-free bottleneck bound

## Finding

For every integer \(N\ge4\), there are two coarsening filtrations of finite topologies on the same \(N\)-point set whose uniform normalized minimal-open discrepancy is \(1/N^2\), while the degree-one bottleneck distance of the induced persistence diagrams is exactly \(1\). Consequently, no constant \(C\) independent of \(N\) can bound \(d_B\le C\Delta_N\) for all such filtrations.

Write \(U_t(x)\) for the minimal open neighborhood of \(x\) at level \(t\), and define

\[
\Delta_N=\sup_{t\in\mathbb R}\frac{1}{N^2}\sum_{x\in X_N}
\left|U_t^{\mathbb X_N}(x)\mathbin{\triangle}U_t^{\mathbb Y_N}(x)\right|.
\]

The persistence diagrams are those of the order-complex homology over any field.

## Assumptions and scope

The index set is \(\mathbb R\). Both filtrations use the discrete topology for \(t<0\), a finite \(T_0\) Alexandrov topology for \(0\le t<2\), and the indiscrete topology for \(t\ge2\). The finite topologies at the middle stage are specified by the posets below, with the down-set convention \(U(x)=\{y:y\le x\}\). The terminal indiscrete space has a one-point \(T_0\)-quotient. The discrepancy is the supremum of the normalized per-level minimal-open symmetric-difference quantity used in finite-topology filtration studies. The result concerns abstract finite-topology filtrations; it does not assert that these examples arise from a particular metric-density or anchor-selection algorithm.

## Proof

Let \(P\) be the four-element poset on \(\{a,b,c,d\}\) with strict relations

\[
a<c,\quad a<d,\quad b<c,\quad b<d,
\]

and no other strict relations. Let \(P'\) be obtained by adding the single relation \(a<b\). For each \(N\ge4\), add \(N-4\) isolated elements to both posets, obtaining \(P_N\) and \(P'_N\). These isolated elements have singleton minimal opens and do not change first homology.

For the down-set convention, at the middle stage of \(P_N\),

\[
U(a)=\{a\},\quad U(b)=\{b\},\quad U(c)=\{a,b,c\},\quad U(d)=\{a,b,d\}.
\]

In \(P'_N\), the only change among minimal opens is \(U(b)=\{a,b\}\); all other minimal opens are unchanged. Thus exactly one point is added to one minimal open, and

\[
\sum_{x\in X_N}|U^{P_N}(x)\mathbin{\triangle}U^{P'_N}(x)|=1.
\]

The order complex of \(P\) is the four-cycle with edges \(ac,ad,bc,bd\), so its first homology is \(\mathbb Z\). The order complex of \(P'\) adds the edge \(ab\) and the two triangles \(abc\) and \(abd\). It is the union of two triangles along their common edge, hence a disk, so its first homology is zero. These descriptions also show the integral homology directly; the conclusion holds over every coefficient field.

For \(t<0\), both spaces are discrete and have zero first homology. For \(0\le t<2\), the first persistence module is one-dimensional and the second is zero. For \(t\ge2\), both spaces have a one-point \(T_0\)-quotient and zero first homology. The induced degree-one diagrams are therefore

\[
\operatorname{Dgm}_1(\mathbb X_N)=\{(0,2)\},\qquad
\operatorname{Dgm}_1(\mathbb Y_N)=\varnothing.
\]

The cost of matching \((0,2)\) to the diagonal is half its lifetime, so the bottleneck distance is exactly \(1\). The normalized discrepancy is zero outside the middle interval and equals \(1/N^2\) within it. Hence \(\Delta_N=1/N^2\), and the ratio of bottleneck distance to discrepancy is \(N^2\). For any proposed constant \(C\), choosing \(N>\sqrt C\) violates \(d_B\le C\Delta_N\). This proves the claim.

## Verification

The included `verify_example.py` uses only the Python standard library. It enumerates the order-complex faces and computes exact rational ranks of the simplicial boundary matrices, confirming face counts \((4,4,0)\) for \(P\) and \((4,5,2)\) for \(P'\), first Betti numbers \(1\) and \(0\), and the single-point minimal-open difference. The integral homology statement follows from the explicit cycle and disk descriptions in the proof, not from a finite numerical approximation. The persistence interval and bottleneck distance are computed exactly from the three constant stages and their structure maps.

## Relationship to prior work

Kayacan introduced a functorial finite-topology persistence framework and proved stability under bounded perturbations of the input metric in the density-based construction. A later version defines the normalized finite-topological discrepancy from symmetric differences of minimal opens and compares it empirically with bottleneck distances, while explicitly noting that the discrepancy is not an interleaving distance. The present example proves a stronger, precise limitation: over the class of all abstract finite-topology filtrations on a shared labelled set, no dimension-independent Lipschitz bound for the bottleneck distance can depend only on this normalized discrepancy. This does not contradict metric-perturbation stability, because no closeness of input metrics or membership in the paper's practical construction is assumed here.

## Limitations

The result is a counterexample for the broad class of abstract finite-topology filtrations. It does not establish instability within the density-based metric-generated subclass, the practical profile/adaptive procedures, or filtrations satisfying additional local-refinement or fibre hypotheses. It rules out a dimension-independent bound from the stated discrepancy alone; it does not rule out bounds that depend on \(N\) or on stronger structural controls.

## References

1. Selçuk Kayacan, “Persistent Homology via Finite Topological Spaces,” arXiv:2512.23348v1 (first public 29 December 2025), especially §§2–4. https://arxiv.org/html/2512.23348v1
2. Selçuk Kayacan, “Finite Topological Space Filtrations: A Topological Framework for Data Analysis,” arXiv:2512.23348v4 (22 September 2026), especially §5.4 for the normalized minimal-open discrepancy and its empirical comparison with bottleneck distance. https://arxiv.org/html/2512.23348v4
3. Frédéric Chazal, Vin de Silva, Marc Glisse, and Steve Oudot, *The Structure and Stability of Persistence Modules*, SpringerBriefs in Mathematics, 2016.
