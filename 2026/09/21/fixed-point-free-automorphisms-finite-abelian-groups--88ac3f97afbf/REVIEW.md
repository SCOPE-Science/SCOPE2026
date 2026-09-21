# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The proof reduces fixed-point-free automorphisms of a finite abelian \(p\)-group to finite-field diagonal blocks in the Hillar–Rhea matrix model. When cyclic summands are ordered by exponent, the representing matrix modulo \(p\) is block upper triangular, with one diagonal block for each repeated exponent. Hillar–Rhea's automorphism criterion makes invertibility equivalent to invertibility of all diagonal blocks. Applying the same criterion to \(\varphi-I\) shows that \(\varphi\) is fixed-point-free exactly when every diagonal block has no eigenvalue \(1\).

The reduction map from \(\operatorname{Aut}(P)\) to the product of the corresponding general linear groups is a surjective homomorphism with equal-size fibers. Consequently the desired count is exactly the automorphism-group order multiplied by the product of the proportions of matrices with no eigenvalue \(1\). The standard automorphism-order formula then gives the closed partition formula.

The formula for \(D_m(p)\) was independently rederived by Möbius inversion on the subspace lattice. For each \(j\)-space \(W\), the number of invertible matrices fixing \(W\) pointwise is \(p^{j(m-j)}|GL_{m-j}(p)|\), and after multiplying by the Gaussian binomial coefficient this becomes \(|GL_m(p)|/|GL_j(p)|\). This gives the stated alternating sum.

Exact finite checks agree with the theorem for several groups with repeated and nonrepeated exponents, including \(C_2^2\), \(C_4^2\), \(C_2\oplus C_4\), \(C_2^2\oplus C_4\), \(C_3\oplus C_9\), and \(C_3^2\oplus C_9\). The proof does not depend on these checks.

## Originality

**PASS, to the best of our knowledge.** Hayat, López-Aguayo and Abbas (2018) prove the rank-two distinct-exponent formula
\[
\theta(C_{p^a}\oplus C_{p^b},1)=p^{3a+b-2}(p-2)^2\qquad(a<b)
\]
and conclude by posing the theta-value problem for arbitrary direct sums with pairwise distinct exponents. The present formula specializes exactly to their rank-two result and gives \(d=1\) for every rank. Their paper was inspected at the theorem and concluding-question level.

Hillar and Rhea (2007) provide the matrix description and total automorphism count used here, but do not state a count of fixed-point-free automorphisms. Gross (1968) gives an existence characterization for abelian \(2\)-groups; the present formula recovers that criterion but additionally counts all such automorphisms. Senden (2023) determines Reidemeister spectra of finite abelian groups—equivalently, which fixed-point cardinalities occur—but the inspected finite-abelian-group sections do not enumerate how many automorphisms realize each value.

Targeted literature searches used combinations and synonymous formulations involving "fixed-point-free automorphisms", "finite abelian p-group", "number/count/proportion", "theta(G,1)", "Hillar Rhea", "linear derangement", "Reidemeister spectrum", and "eigenvalue 1". No source was located with the product formula by exponent multiplicities, the partition closed form, or the all-rank distinct-exponent specialization. Related literature on fixed-point-free automorphism groups, Alexander quandles, and power automorphisms concerns existence or classification rather than this enumeration.

No overlapping SCOPE record was located under searches for fixed-point-free automorphisms, finite abelian groups, theta values, Reidemeister fixed points, or equivalent terminology.

The main residual originality risk is that the derivation is short once the standard matrix description of \(\operatorname{Aut}(P)\) is available. The formula could therefore exist implicitly in older literature, a thesis, or a differently indexed enumeration of automorphisms. No concrete evidence of such coverage was found.

## Value

**PASS.** The theorem gives a uniform exact enumeration for every finite abelian group, rather than a single rank or exponent pattern. It resolves the fixed-point-free slice of an explicit 2018 higher-rank theta-value question, explains why only multiplicities of equal exponents affect the fixed-point-free proportion, and refines a classical existence theorem for abelian \(2\)-groups into an exact count.

## Limitations

Only \(\theta(A,1)\) is determined. Counts \(\theta(A,d)\) for \(d>1\) require finer information about kernels of \(\varphi-I\) and are not claimed here. The full theta-value problem for pairwise distinct exponents therefore remains open beyond the fixed-point-free case.
