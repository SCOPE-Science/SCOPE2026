# Flow-realized entropy flexibility passes to every nonzero time map
## Finding
Let \(\phi=(\phi_t)_{t\in\mathbb R}\) be a continuous flow on a compact metric space. Suppose that every finite entropy level \(c\) with \(0\le c<h_{\mathrm{top}}(\phi)\) is realized on a compact flow-invariant set \(\Gamma_c\) by a flow-invariant probability measure \(\mu_c\), in the exact sense
\[
h_{\mathrm{top}}(\phi|_{\Gamma_c})=h_{\mu_c}(\phi)=c.
\]
Then every nonzero time map \(\phi_t\) is entropy flexible. More precisely, for every finite \(d\) with
\[
0\le d<h_{\mathrm{top}}(\phi_t),
\]
there are a compact \(\phi_t\)-invariant set \(K_d\) and an ergodic \(\phi_t\)-invariant probability measure \(\nu_d\) supported on \(K_d\) such that
\[
h_{\mathrm{top}}(\phi_t|_{K_d})=h_{\nu_d}(\phi_t)=d.
\]
Arbieto, Oprocha and Rego realize the entropy levels in their flow results by strictly ergodic flow-invariant subsystems. Their Theorems A--C therefore imply entropy flexibility for every nonzero time map, not only for the time-one map used to define flow entropy in that paper.

## Assumptions and scope
The phase space is compact and the flow is continuous. The entropy level \(d\) is finite. This is automatic when the ambient topological entropy is finite; if it is infinite, the statement concerns each finite target level below it. The hypothesis is stronger than merely knowing that the time-one map is entropy flexible: the witnessing measure and compact set must be invariant for the whole flow. Strict ergodicity of the witnessing flow subsystem is sufficient but is not required by the argument.

The result makes no claim that the original flow-realizing measure remains ergodic for every sampled time. Indeed, resonant time maps can fail to preserve flow ergodicity. The proof instead extracts a time-map ergodic component without losing entropy.

## Proof
Fix \(t\ne0\) and a finite target \(d<h_{\mathrm{top}}(\phi_t)\). Entropy scaling for continuous flows on compact spaces gives
\[
h_{\mathrm{top}}(\phi_t)=|t|\,h_{\mathrm{top}}(\phi),
\]
and the same formula holds after restriction to a compact flow-invariant set. Put
\[
c=\frac{d}{|t|}.
\]
Then \(0\le c<h_{\mathrm{top}}(\phi)\), so choose \(\Gamma_c\) and \(\mu_c\) from the hypothesis. Since \(\mu_c\) is invariant under the whole flow, metric entropy scales as
\[
h_{\mu_c}(\phi_t)=|t|\,h_{\mu_c}(\phi)=d.
\]
Likewise,
\[
h_{\mathrm{top}}(\phi_t|_{\Gamma_c})=|t|\,h_{\mathrm{top}}(\phi|_{\Gamma_c})=d.
\]
Thus \(\mu_c\) is a measure of maximal entropy for the restricted time map, although it need not be ergodic for that time map.

Take the ergodic decomposition of \(\mu_c\) for the homeomorphism \(\phi_t\):
\[
\mu_c=\int \nu\,d\eta(\nu).
\]
Because \(\mu_c(\Gamma_c)=1\) and \(\Gamma_c\) is \(\phi_t\)-invariant, the components satisfy \(\nu(\Gamma_c)=1\) for \(\eta\)-almost every \(\nu\). Entropy decomposes affinely,
\[
d=h_{\mu_c}(\phi_t)=\int h_\nu(\phi_t)\,d\eta(\nu).
\]
Every such component is supported on \(\Gamma_c\), hence the variational principle gives
\[
h_\nu(\phi_t)\le h_{\mathrm{top}}(\phi_t|_{\Gamma_c})=d.
\]
Since the average of these nonnegative quantities equals their common upper bound \(d\), one has \(h_\nu(\phi_t)=d\) for \(\eta\)-almost every component. Choose one such ergodic component \(\nu_d\), and set
\[
K_d=\operatorname{supp}(\nu_d).
\]
The set \(K_d\) is compact and \(\phi_t\)-invariant. The variational principle and monotonicity under restriction give
\[
d=h_{\nu_d}(\phi_t)\le h_{\mathrm{top}}(\phi_t|_{K_d})
\le h_{\mathrm{top}}(\phi_t|_{\Gamma_c})=d.
\]
Therefore both inequalities are equalities, which is exactly entropy flexibility for \(\phi_t\).

## Verification
The proof was checked separately at the two places where arbitrary real sampling can fail to behave like integer iteration. First, the chosen witness is invariant under the whole flow, so both topological and metric entropy scale by \(|t|\). Second, no ergodicity of \(\mu_c\) for \(\phi_t\) is assumed: the ergodic-decomposition argument recovers an ergodic component at the same maximal entropy, and passing to its support recovers a compact subsystem with exactly that entropy.

For the motivating source, the definition of entropy flexibility appears in the introduction; flow entropy is explicitly defined through the time-one map; Theorem A constructs compact invariant strictly ergodic suspension subsystems at every intermediate entropy; and the authors state that their flow results realize entropy flexibility through strictly ergodic subsystems. These are precisely the hypotheses used above.

## Relationship to prior work
Arbieto--Oprocha--Rego prove entropy flexibility for several classes of flows and realize the intermediate entropy values by strictly ergodic flow-invariant subsystems. Their paper does not state the arbitrary-time sampling consequence above. A separate published published-finding corpus finding proves invariance of entropy flexibility under positive integer iterates of a compact homeomorphism, but that statement does not cover irrational or otherwise noncommensurable real sampling times of a flow and does not use flow-invariant realizers. Another published-finding corpus finding studies resonance and maximal-entropy-measure multiplicity for time maps of three-dimensional flows; it does not provide intermediate-entropy realizers.

The present observation isolates the extra structure that removes the real-time sampling obstruction: flow-invariant entropy realizers. Resonance may split the realizing measure into several \(\phi_t\)-ergodic components, but maximality forces almost every component to retain the full target entropy.

## Limitations
The argument does not show that a time-one entropy-flexible homeomorphism embedded in a flow has entropy-flexible arbitrary time maps unless its entropy witnesses can be chosen flow-invariant. It also does not assert that the strictly ergodic flow subsystem remains strictly ergodic for every time map. The conclusion is only entropy flexibility of the sampled map, obtained after taking a time-map ergodic component and its support.

No uniqueness of the resulting \(\phi_t\)-ergodic measure is claimed. No statement is made about noncompact flows or infinite target entropy levels.

## References
1. A. Arbieto, P. Oprocha, and E. Rego, *Entropy Flexibility of Dynamical Systems*, arXiv:2507.11048v1, first posted 2025-07-15. In particular: the definition of entropy flexibility, Theorem A, the discussion that the flow results are realized by strictly ergodic subsystems, and the definition of flow entropy via the time-one map.
2. Standard entropy-scaling and ergodic-decomposition facts for continuous flows and compact dynamical systems: \(h_{\mathrm{top}}(\phi_t)=|t|h_{\mathrm{top}}(\phi_1)\), \(h_\mu(\phi_t)=|t|h_\mu(\phi_1)\) for flow-invariant \(\mu\), and the affine ergodic-decomposition formula for metric entropy.
