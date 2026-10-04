# Same-model review

## Claim
For the real Banaś–Frączek plane \(R_\lambda^2=(\mathbb R^2,N_\lambda)\), \(N_\lambda(x_1,x_2)=\max\{\lambda|x_1|,\sqrt{x_1^2+x_2^2}\}\), the Ptolemy constant satisfies \(C_{\mathrm{Pt}}(R_\lambda^2)=\lambda\) for every \(1<\lambda\le\sqrt2\).

## Correctness
**PASS.** Writing \(N_\lambda=\max\{E,F\}\) reduces the numerator to four active-branch cases. The \(E/E\) and \(F/F\) cases obey exact Ptolemy inequalities with factor \(1\). Each mixed case costs at most \(F\le\lambda E\), giving the global upper bound \(C_{\mathrm{Pt}}\le\lambda\). The explicit triple
\[
x=\left(\frac12,\frac12\right),\qquad
y=\left(\frac12,-\frac12\right),\qquad
z=(1,0)
\]
has ratio exactly \(\lambda\) when \(1<\lambda\le\sqrt2\). The endpoint is valid because the relevant branches tie.

## Originality
**PASS, with a stated access residual.** Targeted semantic searches found no direct statement for the Banaś–Frączek Ptolemy constant. The exact-object 1993 source and the generalized 2016 source were inspected in full and contain no Ptolemy result. The 2012 Ptolemy paper treats absolute normalized norms and a superficially similar symmetric max norm, but not this anisotropic Banaś–Frączek norm. After the natural linear normalization, its Euclidean comparison ratio is strictly larger at the branch-transition point than at \(1/2\), so the paper's relevant midpoint exactness criterion does not imply the claim. The 2018 comparison paper was also inspected: its midpoint criteria do not apply, and its off-midpoint theorem requires symmetry absent here.

The 2015 reconsideration article is a residual access risk because only its abstract, bibliography, and metadata were readable; a full-text comparison could not be completed. No direct Banaś–Frączek Ptolemy statement was found in targeted searches, and that 2015 bibliography does not list the Banaś–Frączek source.

## Value
**PASS.** The Ptolemy constant is a standard quantitative invariant of Banach-space geometry, and the Banaś–Frączek plane is a named deformation repeatedly used for exact geometric-constant calculations. The interval \(1<\lambda\le\sqrt2\) is not an arbitrary slice: \(\sqrt2\) is exactly the threshold at which all four denominator sides of the extremizing configuration cease to be Euclidean-branch vectors. The result therefore identifies a natural exact regime and a reusable structural proof mechanism.

## Closest literature and limitations
The closest inspected sources are Banaś--Frączek (1993), Zuo (2012), Yang--Yang (2016), and Zuo (2018). The 2015 reconsideration remains an access-limited comparison. No statement is made for \(\lambda>\sqrt2\).

Same-model review: passed. Independent audit: not yet performed.
