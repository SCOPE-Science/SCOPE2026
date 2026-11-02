# A sharp outlet-versus-local-spill reversal in binary drainage trees

## Finding

Consider a one-step, binary-threshold model of flood propagation along a rooted full binary drainage tree. Four statistically identical headwaters supply independent spill signals with probability \(q\). Each internal confluence has an independent local storm signal with probability \(p\), and spills if at least two of its three inputs (both upstream signals and the local storm) are active. A spill is propagated as **one binary signal**, irrespective of the number of triggering inputs.

There are precisely two nonisomorphic rooted, unordered full binary shapes with four headwaters: balanced, \(B=((1,2),(3,4))\), and comb, \(C=(((1,2),3),4)\). Let \(R_T\) denote the root-spill event and \(N_T\) the number of spilling internal confluences in shape \(T\), including the root. For all \(0\le p,q\le1\), the exact topology differences are

\[
\Pr(R_B)-\Pr(R_C)=pq(1-p)(1-q)(2p-1),
\]
\[
\mathbb E[N_B]-\mathbb E[N_C]
=-q(1-q)(2p-1)\bigl(p^2+(1-2p)q\bigr).
\]

In the nondegenerate region \(0<p,q<1\), the two differences have strictly opposite signs except at the unique common boundary \(p=1/2\). Below it, the balanced shape has strictly **lower outlet-spill probability** but strictly **higher expected number of local spills**; above it, the comb shape has lower outlet-spill probability but a higher local-spill count. At \(p=1/2\) the two quantities tie, for every \(q\). The transition is independent of headwater spill probability. Four leaves are the smallest possible size for a shape-dependent comparison in this class.

For example, with \(q=3/5\), at \(p=3/10\) the balanced-minus-comb root-spill difference is \(-63/3125\) and the local-count difference is \(99/3125\). At \(p=7/10\) the root-spill difference is \(63/3125\) and the local-count difference is \(-3/125\).

## Assumptions and scope

The full binary drainage tree is directed toward a unique outlet; every internal vertex has exactly two children. For a fixed tree with four labeled leaves, let \(X_1,\ldots,X_4\) be independent Bernoulli\((q)\) inputs and \(Y_v\), over its three internal vertices, independent Bernoulli\((p)\) variables. All seven inputs are mutually independent. Recursively, the internal spill variable at a confluence \(v\) is \(Z_v=\mathbf1\{Z_{v_L}+Z_{v_R}+Y_v\ge2\}\), with \(Z_i=X_i\) at headwaters. The root event is \(R_T=\{Z_{\mathrm{root}}=1\}\), and \(N_T=\sum_{v\text{ internal}}Z_v\). A headwater is not included in \(N_T\).

The threshold rule is a **discrete connectivity abstraction**, not a conservation law, calibrated rainfall-to-volume transform, or dynamic flood-routing equation. The claims concern a single update, homogeneous probabilities and mutually independent input signals. No assertion is made about arbitrary trees with more than four leaves, heterogeneous confluence probabilities, volumes, temporal correlations or empirical catchment risks.

## Proof

For independent Bernoulli child signals with success probabilities \(x,y\), and an independent Bernoulli\((p)\) local storm, the confluence activates exactly when at least two inputs activate. Conditioning on the storm gives the polynomial
\[
F_p(x,y)=p(x+y-2xy)+xy=p(x+y)+(1-2p)xy.
\]

Write \(u=F_p(q,q)\) and \(v=F_p(u,q)\). In the balanced tree both first-level confluences have success probability \(u\), independently because they use disjoint primitive inputs, so its root-spill probability is \(F_p(u,u)\). In the comb tree the first two internal confluences have success probabilities \(u\) and \(v\); the final independent leaf gives root probability \(F_p(v,q)\). Consequently,
\[
\Pr(R_B)-\Pr(R_C)=F_p(u,u)-F_p(v,q).
\]
Substitution of \(u=2pq+(1-2p)q^2\) and \(v=p(u+q)+(1-2p)uq\), followed by multiplication and factorization, gives exactly \(pq(1-p)(1-q)(2p-1)\).

Linearity of expectation gives \(\mathbb E[N_B]=2u+F_p(u,u)\) and \(\mathbb E[N_C]=u+v+F_p(v,q)\). Their difference is therefore \(u-v+\Pr(R_B)-\Pr(R_C)\); substitution and expansion give the stated second factorization.

For \(0<p,q<1\), the factor \(p^2+(1-2p)q\) is strictly positive: if \(p\le1/2\), it is at least \(p^2>0\); if \(p>1/2\), it exceeds \(p^2-(2p-1)=(1-p)^2>0\). All remaining factors besides \(2p-1\) have the specified strict sign. This proves the unique interior threshold and the opposite rankings. With fewer than four leaves, there is just one unlabeled rooted full binary shape for each possible leaf count \(1,2,3\); thus four is minimal for nontrivial topology comparison. At \(p=0,1\) or \(q=0,1\), the sign statements become non-strict and the displayed identities remain valid.

## Verification

`CHECK.py` independently enumerates all \(2^7=128\) assignments of four headwater and three local-storm input bits. For each assignment, it evaluates both tree topologies and accumulates the exact bivariate probability polynomial with integer coefficients. The resulting two polynomial differences are compared coefficient by coefficient with the claimed factorizations. Seventeen additional rational parameter pairs test both resulting identities and the root probabilities' interval bounds, for 68 rational assertions. Reproduce with `python3 CHECK.py`; the expected output is `PASS: 128/128 configurations, two exact bivariate polynomial identities, 68 rational checks`. This finite exhaustive computation is independently sufficient for the seven-bit model; the preceding algebra also proves the identities for all real parameters in the given square.

## Relationship to prior work

Peter, de Araújo, Araújo and Herrmann (2014), journal version first available online March 13, 2014 (arXiv posting April 16, 2014), study cascading reservoir overspills and how network topology affects flood behavior. Their full paper uses numerical water balances and connected spill avalanches; its Section 2.1 defines runoff, storage, losses and routed spill, while Sections 2.6 and 3.2 compare network structure and connectivity. Their results do not state the displayed independent binary-threshold two-shape identities or the opposite objective rankings.

Hui and Lund (2014) study allocation rules for flood storage in parallel reservoirs, which is a distinct optimization object. Only their abstract was accessible for this comparison; an equivalence hidden in inaccessible material cannot be ruled out.

Amarù, Gaillardon and De Micheli (2014) develop three-input majority-gate Boolean algebra and circuit transformations. Their associativity identities are identities of Boolean functions with shared variables, not probability comparisons of these two disjoint-input random trees with independent local storm signals, and do not imply the count ranking without further work.

## Limitations

The model is a stylized one-step categorical flood-cascade model, rather than a physical hydrological water-balance model. The findings do not predict the relative environmental performance of actual reservoir layouts, which depend on catchment area, storage capacity, flow rates, seasonality, and correlated weather. Originality is assessed relative to the specified inspected literature and relevant mathematical-result searches, not certified against all possible prior circuit, reliability or hydrological models. The complete Hui–Lund article could not be inspected; this remains a priority risk. No independent audit was performed.

## References

- S. J. Peter, J. C. de Araújo, N. A. M. Araújo, H. J. Herrmann, *Flood avalanches in a semiarid basin with a dense reservoir network*, Journal of Hydrology 512 (2014), 408–420; available online 2014-03-13; arXiv:1404.4232, initially posted 2014-04-16. https://arxiv.org/abs/1404.4232
- R. Hui, J. R. Lund, *Flood Storage Allocation Rules for Parallel Reservoirs* (2014). https://doi.org/10.1061/(ASCE)WR.1943-5452.0000469
- L. Amarù, P.-E. Gaillardon, G. De Micheli, *Majority-Inverter Graph: A Novel Data-Structure and Algorithms for Efficient Logic Optimization* (2014). https://si2.epfl.ch/demichel/publications/archive/2014/PID3143501.pdf
