# Scientific review of the beta attenuation law

## Correctness

PASS. The pseudoinverse reduces every rank-one sketch coefficient error to a Gaussian or Haar scalar-denominator ratio applied to the full deterministic residual block. The Haar leverage has an exact beta law, and conditional rotational invariance supplies an independent sphere direction. Beta–gamma factorization converts that direction's radial law to an independent beta scaling of a Gaussian vector. Dominated convergence supplies the claimed exact tail constants. The 845 standalone checks reconstruct both sketch algorithms and verify moment, CDF and tail consequences. Numerical tests support rather than replace the proof.

## Originality

PASS under accessible comparisons, subject to historical-priority uncertainty. Epperly and Webber's Theorem 2.1 and Proposition 5.7 provide mean-error identities, not a full finite-dimensional distributional coupling or stochastic dominance. Their matrix-beta machinery is acknowledged as a starting point, not new. Bartan and Pilanci and Sridhar, Pilanci, and Özgür treat Gaussian-sketch error and do not supply the cross-sketch beta attenuation. Relevant asymptotic inference and pseudoinverse analyses likewise do not logically imply the stated all-threshold comparison. The closest mathematical database hits concerning Haar moment bounds and Gaussian coefficient models did not describe the same distributional result. Specialized older matrix-variate distributions could contain an equivalent identity; exhaustive historical priority is not asserted.

## Value

PASS. The sharp published mean-squared-error comparison does not answer whether the orthonormal sketch has smaller failure probability at a specified tolerance. The independent-beta coupling resolves exactly that practical numerical-reliability question for all real rank-one designs and all right-hand-side blocks; it also gives the full moment range and a sharp heavy-tail coefficient. The distinction is not merely a change of parameters in a mean-error bound. Limits: no assertion for arbitrary design rank, alternative embeddings, finite precision or operational runtimes.

Self-review: passed. Independent audit: not yet performed.
