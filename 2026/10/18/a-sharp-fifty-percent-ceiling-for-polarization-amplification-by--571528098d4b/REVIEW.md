# Scientific review

## Correctness — PASS

The one-edge perturbation has the rank-one Laplacian \(bb^{\mathsf T}\). Sherman–Morrison gives the exact mean-centered transform \(T=I-(Ab)b^{\mathsf T}/(1+b^{\mathsf T}Ab)\). Its nontrivial singular-square eigenvalues have a quadratic with the stated trace and determinant. The certificate \(q(3/2)=((1-3r)^2/4+3(r-\tau))/(1+r)^2\) is nonnegative because \(A^2\preceq A\); the smaller singular square is below one, proving the upper bound. Equality at finite weights contradicts \(r=\tau=1/3\), while the exact two-\(K_6\) eigen-decomposition approaches equality. The included exact rational script passes 881 checks. Risks: symbolic tests do not replace analytic quantifiers; the proof explicitly supplies them.

## Originality — PASS, residual priority risk

The closest prior single-edge formula is Rácz–Rigobon [3, Lemma 3.3], which establishes the polarization difference and previous nonmonotonicity, and the closest local-edge framework is Bhalla–Lechowicz–Musco [2]. The inspected materials do not state an exact universal, opinion-independent relative worst-case coefficient \(3/2\) with a twelve-vertex asymptotically sharp family. The existing formula is a starting identity, not by itself the sharp optimization over every graph and every opinion vector. Searches covered relevant equivalent words, rank-one perturbations, edge-addition effects and stronger parameter ranges; residual risk is an unindexed operator-norm implication or equivalent published result. No claim of certified priority or independence is made.

## Value — PASS

A single link can increase polarization, so an absolute sharp amplification ceiling is relevant to risk assessment of social-link recommendations. The exact coefficient identifies the maximum possible damage in this model, and the twelve-agent family shows the constant is genuinely optimal rather than a loose sufficient estimate. The theorem holds at every graph size and supplies a checkable norm formula for each proposed edge. It is not a textbook rearrangement of a single-graph example; a tight uniform worst-case guarantee requires the singular-spectrum and resolvent-moment bound.

## Closest literature and limitations

[1] Musco–Musco–Tsourakakis (2017), arXiv:1712.09948; [2] Bhalla–Lechowicz–Musco (2021), arXiv:2111.14020; [3] Rácz–Rigobon (2022), arXiv:2206.08996. All rely on or develop the same basic equilibrium model, and [3] has a single-edge change identity. The result does not cover directed graphs, variable stubbornness or adding arbitrary-weight links. Sharpness for simple connected unweighted networks is not established. Independent publication-priority verification and independent scientific review remain outstanding.

Self-review: passed. Independent audit: not yet performed.
