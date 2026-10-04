# Review of Quasiregularity restores canonical \(H^1\) splitting at the endpoint

## Correctness

PASS. The proof redoes the primary source's regularized Laplacian comparison at \(p=1\). The weak quasiregular inequality first gives
\[
\Lambda_f^2
\le
\frac{2K^2}{K^2+1}(|h'|^2+|g'|^2)
+
\frac{2K_0}{K^2+1}.
\]
For the source's regularized functions \(U_\varepsilon\) and \(V_\varepsilon\), this yields a strictly positive endpoint lower bound for \(\Delta V_\varepsilon\), while direct differentiation gives the required upper bound for \(\Delta U_\varepsilon\). The comparison \(V_\varepsilon^2\le2U_\varepsilon^2\) converts these into
\[
\Delta U_\varepsilon\le D_K\Delta V_\varepsilon.
\]
Green's identity and \(g(0)=0\) then give the radial integral estimate. The endpoint passage is legitimate because the regularization keeps the comparison functions smooth and positive, and the right-hand radial integrals are finite for each fixed radius. Taking suprema proves \(h,g\in H^1\).

The control example is exact: the positive Poisson kernel belongs to harmonic \(\mathbf h^1\), but its canonical analytic factors are \(1/(1-z)\) and \(z/(1-z)\), whose \(H^1\) integral means diverge logarithmically.

## Originality

PASS. The closest primary source, arXiv:2609.33159v1, states its Littlewood--Paley theorem only for \(1<p\le2\). Its proof contains the component-comparison mechanism for \(p>1\), but it does not state the endpoint \(H^1\) splitting. The accepted argument independently checks that the regularized differential step survives at \(p=1\).

The strongest directly relevant endpoint comparison found is the full 2025 paper of Das, Huang, and Rasila. For a general harmonic member of \(\mathbf h^1\), their Theorem 3(ii) obtains only \(h,g\in H^p\) for every \(0<p<1\). Their endpoint \(H^1\) lemma applies only to the combination \(h+g\) under a nonvanishing hypothesis. Thus it does not imply the present component-wise \(H^1\) conclusion.

Candidate-specific published-finding searches covered weak harmonic quasiregularity, canonical splitting, analytic/co-analytic projections, the \(H^1\) endpoint, and the source identifier. No returned statement covered the claim. Residual risk remains that an older equivalent theorem exists under different quasiregular Hardy-space terminology.

## Value

PASS. The analytic/co-analytic projection is an endpoint obstruction for general harmonic \(\mathbf h^1\): the explicit Poisson-kernel example already destroys component-wise \(H^1\) membership. The recent source needs component control as the first step in its Littlewood--Paley theorem but stops at \(p>1\). Showing that weak quasiregularity restores the component splitting exactly at \(p=1\) isolates which part of that argument genuinely survives the endpoint and separates it from the later square-function obstruction.

This is a structural endpoint lemma with a quantitative bound, not a routine recomputation of the source's \(p>1\) estimate.

Same-model review: passed. Independent audit: not yet performed.
