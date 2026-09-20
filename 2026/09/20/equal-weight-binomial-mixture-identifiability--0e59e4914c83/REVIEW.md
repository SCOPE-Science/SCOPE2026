# Same-model review

**Verdict:** PASS.

Same-model review: passed. Independent audit: not yet performed.

## Correctness

The claim was rederived from the observation model rather than inferred from parameter counting.

For a binomial mixture, factorial moments satisfy
\[
\mathbb E[(X)_j]=(N)_j\int p^j\,dG(p),
\]
so the marginal law determines the mixing moments through degree \(N\). Conversely each binomial pmf coordinate is a polynomial of degree at most \(N\) in \(p\), so equality of these moments is also sufficient for equality of the observed law.

With equal weights and \(r\) known support locations, subtracting the anchor contributions converts the remaining moments into ordinary power sums of \(M=K-r\) unknown support points. The first \(M\) power sums determine the elementary symmetric polynomials by Newton's identities and therefore determine the monic support polynomial and its roots.

Sharpness was checked independently. Perturbing only the constant coefficient of a monic degree-\(M\) polynomial with \(M\) simple roots in an anchor-free subinterval preserves all elementary symmetric coefficients except the product term. For sufficiently small perturbation all roots remain real, distinct and in that subinterval. Newton's identities then give equality of power sums through degree \(M-1\), producing distinct anchored equal-weight mixtures with identical \(\operatorname{Bin}(N,p)\) mixture laws for every \(N\le M-1\).

The concrete \(K=4,r=1\) example was checked exactly:
\[
\{0.1,0.5,0.6\},\quad \{0.2,0.3,0.7\}
\]
have equal first and second power sums; after adjoining anchor \(0.9\), both four-component equal-weight mixtures yield the same \(\operatorname{Bin}(2,p)\) marginal probabilities \((0.3075,0.335,0.3575)\).

Boundary cases were also checked. If \(r=K\), the model is already known. If \(K-r=1\), no positive amount of information below one binomial trial can identify the remaining location, while one first moment does.

## Originality

The search covered exact and synonymous formulations involving equal-weight binomial mixtures, equal mixing proportions, known mixing proportions, sparse Hausdorff moments, \(K\)-coin models, known support locations, prescribed atoms, Newton identities, and finite-mixture identifiability.

Prior art located includes:

- Teicher (1963) and Blischke (1964) on finite/binomial-mixture identifiability, including the classical unrestricted threshold.
- McLachlan, Lee and Rathnayake (2019), which explicitly records nonidentifiability of unrestricted binomial mixtures when \(N<2K-1\).
- Gordon, Mazaheri, Schulman and Rabani (2020) on the sparse Hausdorff moment / \(K\)-coin problem with unknown locations and weights.
- Fan and Li (2023) on robust recovery of arbitrary \(K\)-spike measures from moments through order \(2K-1\).
- Gordon, Kant, Ma, Schulman and Staicu (2023) on a different structured latent-variable model where uniform latent structure can lower observation requirements.

No inspected source stated the exact equal-weight binomial threshold \(N=K\), the anchored threshold \(N=K-r\), or the matching anchor-preserving lower-bound construction.

The originality claim is deliberately narrow. The proof ingredients themselves are classical: factorial moments, Newton's identities, continuity of simple polynomial roots, and finite moment theory. An equivalent theorem may therefore exist in algebraic moment or quadrature language even if it was not located under mixture-model terminology.

### Residual coverage risk

The strongest residual risk is classical moment-space or equal-weight quadrature literature, where the fact that \(K\) equal-weight atoms are determined by their first \(K\) power sums may be treated as an immediate consequence of Newton identities rather than named as a mixture-identifiability theorem. The Product-of-Experts paper establishes a parameter-count-level result under uniform latent variables for a different structured model, so it is related conceptually but does not directly state the binomial \(K\)-coin threshold above.

No inaccessible source was treated as evidence of non-coverage.

## Value

The result cuts the exact global trial requirement for the uniform latent \(K\)-coin model from the unrestricted \(2K-1\) scale to \(K\), and quantifies the value of exact support-side information: each known anchor saves one additional trial. It also provides an explicit sharp lower-bound mechanism rather than only a dimension count.

The theorem is reusable because the recovery map is constructive: factorial moments give power sums, anchor contributions are subtracted, Newton identities give the support polynomial, and its roots give the latent coin biases.

## Search/access limitations

Originality is to the best of our knowledge, not an exhaustive guarantee. Search indexes can miss older equivalent terminology, especially in classical moment problems, Prony systems, and equal-weight quadrature. The primary Blischke abstract and multiple modern full-text/accessible sources were inspected for the unrestricted threshold; the exact equal-weight anchored statement was not found.
