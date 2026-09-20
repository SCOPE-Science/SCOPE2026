# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

The argument has three independent checks.

First, the zonal block is exactly the well-conditioned finite family furnished by the spherical-design plus restricted-invertibility mechanism. Passing to a principal subfamily cannot decrease the lower bound on the least eigenvalue of its Gram matrix. Orthonormalization therefore preserves a point value of size \(\gtrsim \sqrt{N_k}\) at each selected pole.

Second, after projecting the rotational Gaussian-beam tight frame onto the orthogonal complement \(V\) of the zonal span, the frame operator is exactly \(N_k^{-1}P_V\). A finite equal-weight approximation has stable rank arbitrarily close to \(\dim V\). Restricted invertibility therefore supplies at least \(M\) well-conditioned projected beams whenever \(M/(N_k-M)<1\), which is precisely the condition \(\rho<1/2\). Orthonormalization gives a uniform lower bound on pairing with the corresponding original Gaussian beam.

Third, the final vectors \((z_i\pm q_i)/\sqrt2\) are orthonormal because the two blocks lie in orthogonal subspaces. The projected beam component vanishes at the relevant zonal pole by the reproducing identity, so the high-\(p\) point peak cannot cancel. The sign is chosen so the Gaussian-beam dual pairing cannot cancel. Hölder then gives the low-\(p\) sharp lower bound, while the point peak plus the standard \(k^{-1}\)-scale gradient estimate gives the high-\(p\) lower bound. Sogge's estimate supplies all matching upper bounds.

The floor functions only require taking \(k\) sufficiently large after \(\rho,\delta,\eta\) are fixed. No limiting argument changes the uniform lower spectral constants.

## Originality

**PASS, to the best of our knowledge.**

Han's arXiv:2609.14023v1 was inspected in full-text HTML at the relevant theorem and proof statements. Theorem 2 gives a density-\((1-\varepsilon)\) orthonormal family maximizing all \(p\ge p_n\); Theorem 3 gives a density-\((1-\varepsilon)\) family maximizing all \(2<p\le p_n\). The paper explicitly uses distinct zonal and Gaussian-beam constructions and notes that each branch mechanism fails to recover the other branch. It does not state that one common orthonormal family simultaneously maximizes both branches.

Searches for formulations involving simultaneous Sogge saturation, all-exponent spherical-harmonic maximizers, mixed zonal/highest-weight extremizers, and a common positive-density orthonormal family did not locate the theorem stated here. Standard sources describe the zonal and highest-weight examples as the two separate sharpness mechanisms.

No specifically identified inaccessible paper was found whose title or abstract gives concrete evidence of this simultaneous positive-density statement. The principal residual risk is that the synthesis is structurally short and the source preprint is very recent, so a folklore or unindexed parallel observation may exist.

## Value

**PASS.**

The result changes the quantifier structure in a substantive way. Branchwise abundance does not by itself imply abundance of their intersection: two subsets of an \(N_k\)-dimensional eigenspace can each have density arbitrarily close to one in different orthonormal systems without producing a common orthonormal family carrying both extremal mechanisms. The projected-frame argument constructs such an intersection at every fixed density below \(1/2\).

It also supplies a concrete analytic mechanism: the high-\(p\) point peak is protected by forcing the beam block into the orthogonal complement of the selected zonal kernels, while the low-\(p\) lower bound is protected by restricted-invertibility pairing with the unprojected beams.

The result does not settle the optimal simultaneous density, full density, or the existence of a complete basis with simultaneous all-\(p\) maximal growth.

## Literature checked

- X. Han, arXiv:2609.14023v1, including the introduction, Theorems 2 and 3, Gaussian-beam norm lemma, zonal reproducing identities, gradient estimate, and restricted-invertibility setup.
- X. Han, arXiv:1404.5016 / J. Geom. Anal. 26 (2016), as prior low-\(p\) positive-density work.
- D. A. Spielman and N. Srivastava, arXiv:0911.1114, for the restricted-invertibility principle used in Han's formulation.
- Standard Sogge sharpness literature describing zonal and highest-weight spherical harmonics as the two branchwise extremizers.

## Scope of the claim

The novelty claim is limited to the simultaneous positive-density conclusion and the orthogonal-complement synthesis. No novelty is claimed for Sogge's estimates, the two classical extremizers, Han's branchwise density theorems, the Gaussian-beam tight frame, gradient propagation, or restricted invertibility.
