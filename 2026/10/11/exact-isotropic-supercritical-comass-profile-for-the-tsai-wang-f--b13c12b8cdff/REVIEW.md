# Same-model review

## Correctness

PASS. The proof starts from the exact graph-plane evaluation in Chen--Lien. Equal singular values reduce its numerator to an affine function of \(\operatorname{tr}B\). The trace inequality gives an upper bound depending only on the singular values of \(B\). After writing those singular values as tangents of angles, pairwise averaging changes the objective by the nonnegative amount
\[
Q\sin^2v.
\]
Thus the global matrix problem reduces to one scalar \(t\). The scalar derivative has exactly one positive zero: \(t=\lambda\) in the comass-one region and \(t=1/((r-1)\lambda)\) in the supercritical region. In the latter case \(B=-tI_r\) attains every inequality used, so the resulting bound is the exact comass. The packaged symbolic checker replays the critical-point and closed-form algebra for symbolic \(r\).

## Originality

PASS. Chen--Lien prove the exact criterion for the comass to equal one. When the criterion fails, their necessity argument evaluates the form on \(B=-\operatorname{diag}(\lambda_i)\) only to obtain a value of magnitude greater than one. Their inspected text does not optimize the supercritical norm. Tsai--Wang's earlier paper gives broader sufficient estimates but no exact norm on this supercritical isotropic family. Source-specific and equivalent-formulation searches found no statement of the closed formula or reciprocal maximizing slope.

The main residual risk is a very recent or unindexed independent calculation of the same isotropic matrix norm.

## Value

PASS. The result quantitatively continues a newly proved sharp threshold on the canonical equal-singular-value family in every rank. It identifies both the exact amount by which the form ceases to be a calibration and a non-obvious change in the extremizing plane. This is a natural structural refinement of the exact criterion, rather than a numerical example or arbitrary finite slice.

Same-model review: passed. Independent audit: not yet performed.

## Closest literature and limitations

The closest source is Chen--Lien, arXiv:2609.39159v1; Tsai--Wang, arXiv:2604.04336v1, is the underlying construction.

The theorem does not solve the general supercritical problem with unequal singular values. A comass value greater than one concerns this particular differential form and does not imply non-minimality or non-area-minimality of the affine plane by other calibrations.
