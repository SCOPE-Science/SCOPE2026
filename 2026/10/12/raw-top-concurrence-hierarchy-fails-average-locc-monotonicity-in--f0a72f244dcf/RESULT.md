# Raw top concurrence hierarchy fails average LOCC monotonicity in every dimension \(d\ge 3\)
## Finding
For every integer \(d\ge 3\), consider the pure state
\[
|\psi_d\rangle=\sqrt{\frac{2d+1}{3d}}|11\rangle+\sum_{i=2}^d\sqrt{\frac1{3d}}|ii\rangle.
\]
Fan, Matsumoto, and Imai define the top member of their raw concurrence hierarchy by the elementary symmetric product
\[
C_d(|\psi\rangle)=\prod_{i=1}^d\lambda_i,
\]
where \(\lambda_i\) are the Schmidt probabilities. For \(|\psi_d\rangle\), a single local two-outcome measurement raises this quantity on average. Therefore the raw \(C_d\) is not an entanglement monotone in the standard strong sense of nonincrease on average under local operations for any \(d\ge 3\).

The violation is quantified exactly by
\[
\frac{\sum_j p_j C_d(|\psi_j\rangle)}{C_d(|\psi_d\rangle)}=\frac{3^{d-1}}{2d+1}>1,
\]
and this factor diverges as \(d\to\infty\).

## Assumptions and scope
The statement concerns finite-dimensional bipartite pure states in \(\mathbb C^d\otimes\mathbb C^d\), with \(d\ge 3\), and the unrooted elementary-symmetric concurrence hierarchy of Fan--Matsumoto--Imai. It uses the standard strong monotonicity requirement that for every local measurement with outcome probabilities \(p_j\) and normalized postmeasurement states \(|\psi_j\rangle\), an entanglement monotone \(E\) obeys
\[
\sum_j p_j E(|\psi_j\rangle)\le E(|\psi\rangle).
\]

The finding does not contradict the source's deterministic pure-to-pure theorem based on Nielsen majorization: each raw elementary symmetric function is Schur-concave, so it cannot increase along a deterministic LOCC conversion. The counterexample instead separates that deterministic condition from average monotonicity under a measurement with retained outcomes.

The statement also does not apply to Gour's later normalized rooted concurrence monotones
\[
\widetilde C_k=\left(\frac{S_k(\lambda)}{S_k(1/d,\ldots,1/d)}\right)^{1/k},
\]
including \(G_d=d(\prod_i\lambda_i)^{1/d}\).

## Proof
Set
\[
\lambda_1=\frac{2d+1}{3d},\qquad \lambda_2=\cdots=\lambda_d=\frac1{3d}.
\]
These numbers are positive and sum to one. The raw top concurrence is
\[
C_d(|\psi_d\rangle)=\prod_{i=1}^d\lambda_i
=\frac{2d+1}{(3d)^d}.
\]

Alice performs the local measurement with Kraus operators
\[
K_1=\operatorname{diag}\!\left(\frac1{\sqrt{2d+1}},1,\ldots,1\right),
\qquad
K_2=\operatorname{diag}\!\left(\sqrt{\frac{2d}{2d+1}},0,\ldots,0\right).
\]
Their squared diagonal entries add coordinatewise to one, hence
\[
K_1^\dagger K_1+K_2^\dagger K_2=I.
\]

For outcome \(1\), every unnormalized Schmidt probability equals \(1/(3d)\): the first one is
\[
\frac{2d+1}{3d}\frac1{2d+1}=\frac1{3d},
\]
and the remaining \(d-1\) are already \(1/(3d)\). Thus
\[
p_1=\frac13,
\]
and after normalization all Schmidt probabilities equal \(1/d\). Therefore
\[
C_d(|\psi_1\rangle)=\frac1{d^d}.
\]

For outcome \(2\), only the first Schmidt term survives. Hence \(p_2=2/3\), the normalized state is a product state, and
\[
C_d(|\psi_2\rangle)=0.
\]
Consequently
\[
\sum_{j=1}^2 p_j C_d(|\psi_j\rangle)
=\frac13\frac1{d^d}
=\frac1{3d^d}.
\]
Dividing by the input value gives
\[
\frac{1/(3d^d)}{(2d+1)/(3d)^d}
=\frac{3^{d-1}}{2d+1}.
\]
At \(d=3\), \(3^{d-1}=9>7=2d+1\). If \(3^{d-1}>2d+1\), then
\[
3^d>3(2d+1)=6d+3>2(d+1)+1,
\]
so induction proves \(3^{d-1}>2d+1\) for every \(d\ge 3\). This proves strict average increase in every such dimension. The ratio diverges because its numerator grows exponentially while its denominator grows linearly.

## Verification
The analytic proof establishes the infinite family. The bundled standard-library script `verify_counterexample.py` independently checks the Kraus completeness identities, branch probabilities, input and output raw top concurrences, and exact gain ratio using rational arithmetic for representative dimensions. Its packaged output is `verification_output.txt` and begins with `VERIFY_OK`.

The finite checker is not used as an exhaustive proof over infinitely many dimensions; the all-\(d\) conclusion comes from the symbolic calculation and induction above.

## Relationship to prior work
Fan, Matsumoto, and Imai define the concurrence hierarchy as elementary symmetric functions of the Schmidt probabilities and state that it does not increase under local operations and classical communication. Their proof of this assertion invokes Nielsen's deterministic pure-state conversion criterion and Schur concavity, establishing deterministic pure-to-pure monotonicity. It does not analyze the average over distinct outcomes of a local measurement.

Vidal's framework for entanglement monotones uses monotonicity under local transformations, and later formulations make the average condition explicit. Gour subsequently introduced a slightly different concurrence family: the normalized \(k\)-th roots of the same elementary symmetric functions. Gour proves the rooted functions concave and therefore entanglement monotones, with the top member
\[
G_d=d\left(\prod_i\lambda_i\right)^{1/d}.
\]
The present counterfamily concerns the earlier unrooted product, not \(G_d\). The distinction is substantive: taking the root changes the response to probabilistic local filtering.

Targeted searches for the source title, raw elementary-symmetric hierarchy, strong or average LOCC monotonicity, local-measurement counterexamples, and the later \(G\)-concurrence found no source stating this all-dimension counterfamily or an implication-equivalent result. The closest inspected later source is Gour's rooted construction, which repairs the relevant concavity issue by changing the functional.

## Limitations
The result addresses only the top raw member \(C_d\) for \(d\ge 3\). It does not classify which lower raw members fail or satisfy average monotonicity, and it does not claim that every use of the phrase "entanglement measure" in the older literature imposed the same strong convention. The source's deterministic majorization theorem remains intact.

The novelty assessment is literature-based rather than a proof of global uniqueness. Poorly indexed notes or pedagogical treatments could contain an equivalent observation. No claim is made about mixed-state convex-roof extensions of the raw hierarchy.

## References
1. H. Fan, K. Matsumoto, and H. Imai, "Quantify entanglement by concurrence hierarchy," arXiv:quant-ph/0204041, first public 8 April 2002; Journal of Physics A 36 (2003), 4151--4158, DOI 10.1088/0305-4470/36/14/316.
2. G. Vidal, "Entanglement monotones," arXiv:quant-ph/9807077; Journal of Modern Optics 47 (2000), 355--376, DOI 10.1080/09500340008244048.
3. G. Gour, "Family of Concurrence Monotones and its Applications," arXiv:quant-ph/0410148; Physical Review A 71, 012318 (2005), DOI 10.1103/PhysRevA.71.012318.
