# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS.

The central identity is a direct coordinate calculation. With `d=gcd(n,v)` and `ell=n/d`, addition by `v` partitions `Z/nZ` into `d` disjoint cycles of length `ell`. Ordering each cycle as `r,r+v,...` turns the defining formula of `chi_{n,v}` into the ordinary `chi_ell` formula independently on every cycle. For `chi_{n,-2v}`, the block map is `psi_ell(z)_t=z_t+z_{t-2}z_{t-1}+z_{t-1}`; substitution verifies `psi_ell=A chi_ell A` for the affine involution `A(z)_t=z_{-t}+1`.

The permutation criterion follows because a direct product is bijective exactly when its factor is bijective, and ordinary `chi_ell` is bijective exactly for odd `ell`. The equivalence `ell odd <=> 2^k | v` for `n=2^k n_0` is immediate from `ell=n/gcd(n,v)`.

Order is preserved under conjugacy, giving the known ordinary-chi order with `ell` in place of `n`. Algebraic degree is preserved under affine permutations, so the known inverse degree `(ell+1)/2` transfers to both explicit families. The exact inverse monomial count is claimed only for `chi_{n,v}`, where the conjugating transformation is a coordinate permutation rather than a translation.

For differential behavior, derivative counts of a Cartesian product factor exactly over blocks. The ordinary-chi differential formula gives maximum differential probability `1/4` for every odd `ell>=3`: its exponent `w(a)` is at least 2 for nonzero `a`, and equality occurs for a single-bit difference. Hence the product has maximum probability exactly `1/4`, attained by activating one block only, and differential uniformity `2^n/4=2^(n-2)`. Affine conjugacy preserves differential uniformity, so the second family has the same value. Input/output cyclic coordinate shifts preserve it as well, which gives the corollary for the nondegenerate nonlinear members of Feng et al.'s full classification.

The finite verifier exhaustively confirms the block identities at `(6,2)`, `(10,2)`, `(12,4)` and the predicted differential uniformities at representative tractable dimensions. These checks support but are not used in place of the general proof.

## Originality

PASS, to the best of our knowledge.

The primary source inspected in full is Feng, Wang, Yu and Zhang, arXiv:2609.19548v1, submitted 17 September 2026. It introduces the two explicit generalized families and proves their permutation criterion. Its proof does partition a derivative equation into arithmetic-cycle subsystems and explicitly reduces part of the argument to an odd cycle; this is the closest prior mechanism and is credited in the result. However, the paper does not state a map-level direct-product conjugacy, does not discuss differential uniformity of the new maps, and does not state the inherited order or inverse-degree formulas. Its only occurrence of differential terminology in the searchable full text is bibliographic context, and no direct-product statement appears.

Targeted searches were made using the paper title and arXiv identifier together with `direct product`, `decomposition`, `gcd`, `differential`, `differential uniformity`, and exact-formula variants of the new maps. Searches also covered the nearby chi literature: Schoone-Daemen on state diagrams and algebraic/differential properties of ordinary chi; Kriepke-Kyureghyan on even-dimensional siblings; Lyu et al. on a different generalized chi function; and the ChiChi generalizations. No source located stated the present direct-product theorem or its DDT/differential consequences for the Feng-Wang-Yu-Zhang family.

Internal overlap searches in the current SCOPE repository by `chi_n`, `2609.19548`, generalized-chi and differential-uniformity terminology found no existing record covering this contribution.

No specifically identified inaccessible paper emerged as a likely source of exact prior coverage. The main residual originality risk is temporal rather than access-based: the motivating preprint is extremely recent, so a simultaneous response, an unindexed note, or a revised version could independently contain the same observation. A second residual risk is older cellular-automata literature phrasing the elementary gcd-cycle decomposition in more general language without the present cryptographic consequences.

The novelty claim is therefore deliberately narrow: the map-level direct-product/affine decomposition of the newly introduced families and the resulting exact structural, inverse-degree, and differential consequences. None of the cited ordinary-chi formulas is claimed as new.

## Value

PASS.

The motivating paper presents the new degree-two maps as low-latency shift-invariant permutations that work in even dimension. The decomposition shows that their even-dimensional instances are interleavings of multiple independent smaller odd-dimensional chi maps rather than indecomposable nonlinear layers. It immediately imports exact order and inverse complexity and gives the full DDT as a product object, including the closed-form differential uniformity `2^(n-2)`. For even `n`, the permutation condition forces at least two invariant coordinate cycles, so no number of iterations of either explicit family creates cross-cycle diffusion. This is directly relevant to understanding the cryptographic structure of the new construction while not overstating it as a break of any complete cipher.

## Limitations

The exact order claim is limited to the two explicitly conjugated families. The corollary for the broader classified family is limited to nondegenerate nonlinear cases and to invariants preserved by input/output coordinate shifts, such as differential uniformity and inverse algebraic degree. No claim is made about security once an external linear diffusion layer is interleaved. No independent audit has been performed.
