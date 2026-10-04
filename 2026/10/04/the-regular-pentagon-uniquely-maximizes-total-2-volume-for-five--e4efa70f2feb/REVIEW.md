# Review of The regular pentagon uniquely maximizes total \(2\)-volume for five-vector Parseval frames in \(\mathbb R^2\)

## Correctness
**PASS.** The Parseval condition is exactly orthonormality of the two synthesis rows. Pairwise determinant signs linearize the total \(2\)-volume into \(u^{\mathsf T}Sv\), and the orthonormal-pair maximum for fixed skew \(S\) is exactly its top singular value. The characteristic-polynomial reduction uses the identity \(\sigma_1^2+\sigma_2^2=10\) and the sum of squared principal Pfaffians. The switching-normalized enumeration is exhaustive over all \(2^6\) cases and yields only \(C=5\) and \(C=21\). The equality classification is supported by an exact single-orbit computation for every maximizing sign matrix and by the strict top spectral gap. The regular pentagon attains the resulting bound analytically.

## Originality
**PASS with residual literature risk.** The motivating paper formulates the same total-volume optimization and explicitly asks for explicit non-equiangular small-parameter optimizers. Its inspected full text does not give the \(N=2\), \(M=5\), \(k=2\) solution. Searches covered the frame formulation, regular-pentagon formulation, Plücker-coordinate \(\ell^1\) formulation, and skew-sign-matrix spectral formulation. No covering implication was found. The main remaining risk is an unindexed equivalent theorem in exterior algebra, Grassmannian norm optimization, or tournament spectral theory.

## Value
**PASS.** This is a complete exact solution of a natural small non-equiangular instance singled out by the source's open-problem program. It gives the optimum, a closed-form extremizer, and uniqueness up to the natural symmetries. The equality classification also answers structural questions in this case: the optimizer is equal norm and full spark despite not being equiangular.

## Closest literature and limitations
The closest source is Cahill--Casazza, *Optimal Parseval frames: Total coherence and total volume* (arXiv:1910.01733). It proves optimality of equiangular Parseval frames when available and asks for explicit solutions when they are not. The present result is limited to real dimension two with five frame vectors and total \(2\)-volume; no all-parameter extension is claimed.

Same-model review: passed. Independent audit: not yet performed.
