# A two-sided uniformly Kreiss counterexample to strong Cesàro boundedness
## Finding
There exists an invertible bounded operator \(T\) on a separable complex Hilbert space such that both \(T\) and \(T^{-1}\) are uniformly Kreiss bounded, but \(T\) is not strongly Cesàro bounded. The operator may be taken to be exactly the block-diagonal operator in Arnold's 2026 counterexample; no modification of the forward construction is required.

This strengthens the negative separation in the focal paper by imposing symmetric forward/backward uniform Kreiss control. It also places the example next to, but does not resolve, the older two-sided absolute-Cesàro questions of Cohen--Cuny--Eisner--Lin.

## Assumptions and scope
For a bounded operator \(S\), write
\[
F_m(\phi;S)=\frac1m\sum_{k=1}^m e^{ik\phi}S^k.
\]
Uniform Kreiss boundedness is used in the equivalent rotated-Cesàro form
\[
\sup_{m\ge1}\sup_{\phi\in\mathbb R}\|F_m(\phi;S)\|<\infty.
\]
Strong Cesàro boundedness means uniform boundedness of
\[
\frac1N\sum_{k=1}^N\gamma_k S^k
\]
over all \(N\ge1\) and all unimodular coefficients \(\gamma_k\).

Arnold's construction is a Hilbert direct sum of finite-dimensional blocks \(T_n\). In the basis used in each block,
\[
T_n z_{n,j}=e^{i\theta_{n,j}}z_{n,j},
\]
where the positive phases are geometrically separated and the associated partial-sum projections have a uniform bound depending only on the fixed construction parameter. The focal proof establishes a uniform forward Kreiss estimate and a divergent family of signed Cesàro averages.

The present claim concerns this specific construction. It does not assert that the inverse of every uniformly Kreiss bounded invertible operator is uniformly Kreiss bounded.

## Proof
Fix one block and suppress the block index. Arnold's summation-by-parts argument estimates diagonal multipliers on the nonorthogonal basis through a uniform partial-sum projection bound and the total variation of the scalar multiplier sequence.

First consider the inverse block. It is diagonal with coefficients \(e^{-i\theta_j}\). Since the phases are decreasing and positive,
\[
\sum_j\left|e^{-i\theta_j}-e^{-i\theta_{j+1}}\right|
\le \sum_j|\theta_j-\theta_{j+1}|
\le \theta_1.
\]
The same summation-by-parts estimate used in the focal construction therefore gives a block-uniform bound for \(\|T_n^{-1}\|\). Hence the Hilbert direct sum \(T=\bigoplus_nT_n\) is invertible and \(T^{-1}=\bigoplus_nT_n^{-1}\) is bounded.

For the uniform Kreiss estimate, define the scalar Cesàro kernel
\[
F_m(t)=\frac1m\sum_{k=1}^m e^{ikt}.
\]
The multiplier of the rotated average of \(T_n\) is \(F_m(\phi+\theta_j)\). For \(T_n^{-1}\) it is \(F_m(\phi-\theta_j)\). The elementary identity
\[
F_m(-t)=\overline{F_m(t)}
\]
gives, term by term,
\[
\left|F_m(\phi-\theta_j)-F_m(\phi-\theta_{j+1})\right|
=
\left|F_m(-\phi+\theta_j)-F_m(-\phi+\theta_{j+1})\right|.
\]
Arnold's geometric-phase lemma bounds the right-hand variation uniformly in \(m\), the rotation parameter, and the block. Applying that lemma with rotation parameter \(-\phi\), followed by the same summation-by-parts estimate as in the published forward proof, yields
\[
\sup_n\sup_{m\ge1}\sup_{\phi\in\mathbb R}
\left\|\frac1m\sum_{k=1}^m e^{ik\phi}T_n^{-k}\right\|<\infty.
\]
Taking the Hilbert direct sum proves that \(T^{-1}\) is uniformly Kreiss bounded. Arnold already proves the corresponding statement for \(T\).

Finally, the signed-average lower bound in the focal paper applies to the same forward operator \(T\) and is unaffected by the observation about its inverse. Thus \(T\) is not strongly Cesàro bounded. This completes the claim.

## Verification
The proof was checked at the level of the actual multiplier argument, rather than only from the theorem statement. The critical symmetry is the exact identity \(F_m(-t)=\overline{F_m(t)}\), which transports the focal variation estimate from the phase sequence \(\phi+\theta_j\) to \(\phi-\theta_j\) without reversing the basis order or changing any constant. The inverse-boundedness step uses only \(|e^{ia}-e^{ib}|\le |a-b|\) and telescoping of the monotone phase sequence.

No finite experiment is used as proof. The argument does not claim power boundedness, absolute Cesàro boundedness, strong Kreiss boundedness, or any two-sided property beyond uniform Kreiss boundedness.

## Relationship to prior work
Arnold constructs a uniformly Kreiss bounded operator on a separable Hilbert space that is not strongly Cesàro bounded, settling Problem 3 in Cohen--Cuny--Eisner--Lin. The inspected focal text develops the block bases, geometric phases, multiplier-variation lemma, forward uniform-Kreiss estimate, and the signed-average lower bound, but does not state invertibility, uniform Kreiss boundedness of the inverse, or a two-sided version of the counterexample.

Cohen--Cuny--Eisner--Lin separately study invertible operators and two-sided assumptions involving absolute Cesàro boundedness. Their Problem 2 asks whether two-sided absolute Cesàro hypotheses force two-sided power boundedness; this is a different and stronger averaging hypothesis. Their Theorem 2.2 supplies an invertible strongly Kreiss example that is not absolutely Cesàro bounded, but it does not provide the present pair of uniform-Kreiss bounds for \(T\) and \(T^{-1}\) together with failure of strong Cesàro boundedness.

Targeted published-finding corpus and web searches for two-sided/inverse uniform Kreiss formulations returned no statement implying this claim. The nearest published-finding corpus hits were on unrelated operator-theoretic topics rather than Kreiss/Cesàro boundedness.

## Limitations
This is a structural sharpening of one very recent construction, not a classification theorem. It does not answer whether two-sided absolute Cesàro boundedness implies power boundedness, and it does not show that both time directions fail strong Cesàro boundedness. Because the sharpening is a short phase-symmetry observation and the focal preprint is recent, an equivalent observation may exist in incompletely indexed literature or folklore.

## References
1. Loris Arnold, *Uniform Kreiss boundedness does not imply strong Cesàro boundedness*, arXiv:2609.29679v1. First public submission: 2026-08-30.
2. Guy Cohen, Christophe Cuny, Tanja Eisner, Michael Lin, *Resolvent conditions and growth of powers of operators*, arXiv:1912.10507; Journal of Mathematical Analysis and Applications 487 (2020), 124035, DOI 10.1016/j.jmaa.2020.124035.
