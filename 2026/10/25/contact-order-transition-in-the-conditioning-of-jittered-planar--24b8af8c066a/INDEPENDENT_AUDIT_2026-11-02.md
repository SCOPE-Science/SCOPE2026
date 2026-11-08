# Independent mathematical audit

## correctness

PASS

Repaired final result correct for fixed integers a,b>=1, m=a+b, 0<delta<pi/12, -delta<Delta<delta and t downarrow 0. Gram eigenvalues are (m±|sum exp(2i theta_i)|)/2; compactness/no aliasing localizes low s to the rank-one diagonal, where s=||P theta|| (1+O(||P theta||²)). Overlap diagonal segment length sqrt(m)(-Delta) yields sqrt(m) v_(m-1)(-Delta)/(2delta)^m t^(m-1). At Delta=0, mixed-sign support meets diagonal at origin: bounded rescaling gives V_(a,b)/(2delta)^m t^m, V11=1 and V12=sqrt(2/3). Separation yields s²>=1-cos Delta by a two-row PSD sub-Gramian. Layer-cake proves E[s^-p], and bounded sigma_max proves E[kappa^p], finite precisely below those powers, divergent at equality; strictly positive common noise variance gives stated mean-squared error thresholds. The literal original claim incorrectly referred to negative powers of kappa, always <=1, and did not specify strictly positive noise variance in one sentence. Entire RESULT.md is corrected, with no increase of mathematical scope. Independent symbolic/numerical checks test specific consequences only; the unrestricted result rests on analytic arguments.

## originality

PASS

Best-of-knowledge claim-specific originality survives: the exact non-identically-distributed two-window fixed-m laws, interior-to-apex codimension transition, mixed-sign cone leading coefficient, and sharp inverse-risk thresholds do not follow from inspected qualitative observability, generic small-ball theory, or deterministic clustered-node conditioning. This is not a global novelty certificate; the inaccessible specialist Bass–Gröchenig full text and other unindexed special cases remain explicit risks.

## value

PASS

The fixed-m design boundary has substantive mathematical and statistical motivation: almost-sure rank is insufficient for expected inverse-Gram accuracy, and a single support-contact changes codimension and the exact hard-edge exponent. For m=3 the positive-variance mean-squared risk flips from infinite (overlap) to finite (touch), while m=4 suffices in overlap; separation supplies a quantitative deterministic gap. This is a sharp motivated classification and explicit natural cone invariant, not a normalization or arbitrary table entry. The corrections preserve the original value rather than claiming a broader theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
