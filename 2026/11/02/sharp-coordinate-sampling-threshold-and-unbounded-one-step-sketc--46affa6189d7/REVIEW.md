# Scientific review

## Correctness — PASS

The defining sketch objective for one Krylov vector is \(\sigma_{\min}(Sb)=\|Sb\|_2\). The central lower bound follows from decomposing an SPD matrix around the midpoint of its spectral interval and applying the coordinate-selector contraction. The construction is an explicit symmetric involution exchanging the normalized full vector and its normalized coordinate projection, so its two nontrivial eigenvalues and the sampled-image cancellation are exact. The one-variable least-squares calculation gives the asserted residual ratio; numerical checks are not substitutes for these derivations. Verified 62,206 reproducible assertions with `check.py`.

## Originality — PASS within inspected literature; residual historical risk

The 2026 deterministic sketching preprint [1] optimizes \(\sigma_{\min}(SV)\) but its dsGMRES samples \(SAV\) and expressly leaves an error-bound problem open. It does not state the sharp \(\sqrt{s/n}\) SPD annihilation frontier or the exact unbounded residual factor for a basis-maximizing coordinate sketch. The 2021 sGMRES paper [2] proves guarantees conditional on embedding the affine residual space, an assumption intentionally absent here. The finite-precision analysis [3] and DEIM/GappyPOD studies [4,5] address different stability objects. Searches of published mathematical research records, targeted web queries, and accessible earlier claims did not produce an implication covering this exact theorem. A stronger unpublished or unindexed equivalent remains a risk; the underlying operator-norm decomposition is elementary and is not claimed as novel in isolation.

## Mathematical value — PASS

The construction answers a concrete design question raised by [1]: optimizing representation of a Krylov basis alone need not safeguard the image entering sketched residual minimization. Its threshold is dimensionwise sharp, extends to arbitrary fixed oversampling \(s<n\) for the globally best basis selector, and yields arbitrarily large exact residual loss despite uniformly well-conditioned SPD systems. It motivates testing sampled image and residual-space geometry, rather than only basis geometry.

## Scope and risks

For \(s>1\) the result concerns an oracle maximizing the basis-only criterion, not a proof that a particular heuristic follows those selected rows. It does not challenge established error estimates under affine-subspace embedding hypotheses. The checks were performed in exact mathematical arguments plus floating-point computational tests; independent reproduction and exhaustive priority verification remain outstanding.

Self-review: passed. Independent audit: not yet performed.
