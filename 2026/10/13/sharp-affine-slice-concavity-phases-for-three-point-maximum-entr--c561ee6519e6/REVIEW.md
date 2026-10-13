# Self-review

## Correctness — PASS

The claim uses \(0<a<1\), \(\gamma>0\), and the exact slice \(\Delta=\{x\in[0,1]^3:\sum_i x_i=2\}\). Reconstructing the determinant through Sylvester's identity gives the coefficient identity \(D=1+2(b+k)+b(b+2k)e_2+b^2(b+3k)e_3\), which was independently checked against direct rational determinants. Positivity holds at the boundary as well as in the interior. Spectral log-determinant concavity proves the two outer ranges; slice concavity of \(e_2\) and \(e_3\) closes the additional low interval. In the excluded gap, the exact second derivative \(-2(B+H\delta)/D>0\) at \((\delta,1-\delta/2,1-\delta/2)\) disproves concavity. Symmetry and Jensen establish the exact optimum. A concave quadratic derivative numerator proves strict low-branch scale monotonicity, and a uniform negative Hessian margin proves robustness to covariance perturbations. The checker verified 770 rational determinant identities and additional parameter, boundary and curvature identities, but the real-parameter theorem rests on the analytic proof.

## Originality — PASS with residual risks

The closest direct source, Anstreicher–Fampa–Lee–Li–Ponte (arXiv:2609.01214v1), introduces scaled NLP-Id and gives spectral-region concavity on the cube, a sufficient but nonsharp equicorrelation condition in Theorem 17, and a remark that affine-slice curvature is an additional problem. Its results do not classify necessity and sufficiency on the exact three-variable, size-two slice. Ponte–Fampa–Lee (arXiv:2511.04350v3) gives the related D-optimality equivalences at spectral scaling, not all-scale curvature. Ponte–Fampa–Lee (Algorithmica, DOI:10.1007/s00453-026-01373-9) works with generalized factorization and dual relaxations rather than the scaled NLP-Id determinant. Relevant published-record searches revealed no same-claim record; they do not establish novelty. The full 1996/1999 classical formulations were not obtained; an equivalent result hidden there or elsewhere cannot be excluded without further human examination.

## Value — PASS

The exact two-range classification resolves a natural minimal nontrivial affine-cardinality case raised by the motivating analysis, not an arbitrary grid slice. It permits convex solution of a parameter interval beyond the eigenvalue sufficient bound and provides a closed-form decreasing upper-bound profile. Its explicit strong-concavity modulus establishes stability for open families of nonequicorrelated matrices with genuinely different pairwise selection objectives. No higher-dimensional generalization, quantitative perturbation radius or end-to-end algorithmic speedup is claimed.

Self-review: passed. Independent audit: not yet performed.
