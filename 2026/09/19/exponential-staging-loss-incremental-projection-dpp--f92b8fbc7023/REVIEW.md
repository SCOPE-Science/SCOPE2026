# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness — PASS

The argument reduces the staged sampler to an explicit finite-state omission chain. For the nested Givens basis, the stage-\(s\) projection kernel is \(I-z^{(s)}(z^{(s)})^\top\) on \(s+1\) active coordinates, so a rank-\(s\) projection-DPP sample omitting \(j\) has probability \((z_j^{(s)})^2\). Conditioning on the retained stage-\((s-1)\) set leaves exactly two possible omissions. Their weights are \((1-c_s^2)A\) and \(c_s^2\), which gives the exact conditional inverse-weight expectation \(2/((1-c_s^2)A+c_s^2)\).

The hierarchical choice \(c_s=\varepsilon^{2^{s-2}}\) makes the new weight negligible relative to every old possible omission weight at each fixed stage. Starting from inverse-weight expectation 2 therefore yields the limit \(2^d\).

The orthogonal CSS calculation is independent of the oblique interpolation algebra. Because the final subset has \(d\) of \(d+1\) columns, the residual is the distance of the omitted column from the span of the others. The Schur complement gives this squared distance as \(1/(G^{-1})_{jj}\). The explicit singular decomposition then yields the exact normalized residual \(1/(a_j+\sigma^2b_j)\). With \(\sigma^2=c_d^4\) and \(\min_j a_j\asymp c_d^2\), this converges uniformly to \(1/a_j\). Averaging under the staged and one-shot omission laws gives \(2^d\) and \(d+1\), respectively.

Distinct fixed leading singular values remove basis-order degeneracy: the cumulative vectors used by the stages are the uniquely ordered dominant right singular vectors up to signs. A high-precision standalone artifact checks the null-weight recursion, probability normalization, and both expected normalized errors for several dimensions and parameter values.

## Originality — PASS, to the best of our knowledge

The motivating Grigori–Xue preprint was inspected beyond the abstract, including the conditional-DPP construction, Theorems 3.1–3.3, the stated multi-stage product bound, its discussion of the \(2^t\) one-column-per-stage case, and the numerical-comparison setup. The paper proves tightness of a *single* conditional step for a prescribed initial set, but it does not give a single nested family on which all one-column stages compound to \(2^d\). It explicitly reports that its experiments find multi-stage ARP comparable to one-shot ARP.

Classical volume sampling and ARP already supply the \(d+1\) one-shot bound and its worst-case optimality; these are excluded from the novelty claim. Cortinovis–Kressner and Epperly establish ARP/volume-sampling guarantees and the projection-DPP interpretation. Grigori–Xue themselves point to exponential worst-case behavior of deterministic CPQR as an analogy. Those results do not state an exponential lower bound for the new conditional-DPP/MSARP distribution, nor an exponential separation from one-shot ARP on the same exact singular subspace.

The novelty claim is therefore restricted to the nested Givens construction showing simultaneous asymptotic sharpness of the \(2^d\) MSARP factor, the fact that the same factor survives **orthogonal** column-subset projection, and the resulting \(2^d/(d+1)\) staged-versus-one-shot separation with distinct ordered leading singular values.

Repository searches by the source identifier, conditional-DPP terminology, multi-stage ARP/MSARP, projection-DPP column selection, and column-subset-selection terminology found no overlapping SCOPE record. External searches for staged/incremental projection-DPP sharpness, conditional volume-sampling lower bounds, and multi-stage ARP counterexamples found the motivating preprint, ARP/volume-sampling background, and unrelated DPP work, but no equivalent theorem.

### Residual literature risk

Two older sources remain the most plausible places for ingredients that could narrow the novelty claim. Cortinovis–Kressner, DOI 10.1137/24M1719189, was inspected through its accessible abstract and through the ARP theorem as reproduced in the motivating paper and Epperly's accessible text; its complete journal text was not inspected here. It predates MSARP, so it cannot analyze the 2026 staged algorithm by name, but it could contain sharp one-shot constructions related to the final family. Deshpande–Rademacher, DOI 10.1109/FOCS.2010.38, was inspected through bibliographic metadata and its abstract describing the classical \(\sqrt{k+1}\) Frobenius volume-sampling guarantee and matching lower bound; its complete proof was not inspected. That source may cover one-shot extremizers but not the later conditional-DPP staging rule.

The motivating preprint is very recent and was updated after initial submission, so contemporaneous or not-yet-indexed follow-up work cannot be excluded. No inaccessible source found provides concrete evidence that the staged theorem is already covered.

## Value — PASS

The source's \(2^d\) factor could otherwise be interpreted as an artifact of repeatedly applying a loose stagewise inequality, especially because its experiments show little loss from staging. The construction proves that the exponential factor is a genuine worst-case phenomenon for one-column incremental selection.

The lower bound is stronger than sharpness of the analyzed oblique interpolant: it applies to the best orthogonal approximation from the sampled columns, which is the error metric commonly used to evaluate column subsets. It also uses the exact dominant singular subspace and distinct ordered singular values, removing approximate-subspace and basis-degeneracy explanations.

The comparison with one-shot ARP isolates the cost of irrevocability on the same matrices. The expected squared error changes from the classical \(d+1\) scale to \(2^d\), an exponential separation. This gives a concrete reason to use larger stages, allow resampling/swaps, or periodically restart global selection when worst-case robustness matters, without claiming that such variants are automatically optimal.

## Limitations checked

The construction is adversarial and becomes increasingly ill-conditioned because the optimal rank-\(d\) tail singular value tends to zero. The theorem fixes \(d\) and lets \(\varepsilon\to0\); it is an asymptotic sharpness result, though every desired proximity to \(2^d\) is attained by a finite full-rank matrix. It treats the maximally incremental schedule of one column per stage and does not establish sharpness of the general product \(\prod_i(1+k_i)\) for arbitrary block sizes. It does not address average-case data, finite-precision sampler stability, spectral-norm error, or the practical matrices used in the source experiments.