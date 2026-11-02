# Scientific review: sharp Fock Toeplitz-composition factor lengths

## Correctness (C): PASS

The domain is the one-variable Gaussian Fock Hilbert space for any positive Gaussian scale, and **every factor is both an affine composition operator and a one-symbol bounded Toeplitz operator**. The generator recognition condition \(\Re\mu\ge|\mu|^2>0\), with zero intercept on the equality boundary, is stated in Lin--Lu--Zu, Corollary 3.1, and follows from the recovered Gaussian symbol's quadratic and linear exponent. For a product of nonzero slopes, the sum of arguments equals the target argument modulo \(2\pi\). Strict concavity of \(\log\cos\) bounds the modulus at fixed argument and forces all slopes onto the generator boundary at equality. Such factors have zero intercept, proving the nonzero-translation exclusion exactly. Equal-slope constructions realize every admissible interior point and the centered boundary. The threshold is eventually strictly increasing, so the integer word-length formula and angular asymptotic follow. The excluded zero and nontrivial unitary cases follow from products of permitted nonzero slopes. All quantifiers and the zero-threshold convention are explicit in RESULT.md.

The supplementary checker executed with 79,629 deterministic finite assertions. These are checks of arithmetic and sample constructions, not an exhaustive or infinite proof.

## Originality (O): PASS on accessible evidence, with residual priority uncertainty

The closest source, Lin--Lu--Zu (arXiv:2607.04102, Section 3.1 and Corollary 3.1), determines **single-factor representability** but not a product word ball, shortest factor length, or boundary translation penalty. Bauer--Fulsche--Rodriguez Rodriguez (arXiv:2405.20792, Section 3.3) considers membership in the broader Fock Toeplitz algebra and cannot imply this word metric in the restricted generator class. Chalendar--Partington (arXiv:2106.00427) studies unrestricted composition semigroups and iterations, lacking bounded-symbol Toeplitz restrictions on each factor. Cho--Park--Zhu (arXiv:1212.0045) analyzes boundedness of analytic/anti-analytic Toeplitz products, not such restricted operator products. Relevant full-text mathematical portions of these open-access papers were read rather than relying on title matching. No equivalent implication was found from their theorems.

The exact product-disk/semigroup geometry might be known under another name. No claim of uniqueness or priority follows merely from unsuccessful searches. An independent literature and mathematical assessment has not been undertaken.

## Mathematical value (V): PASS

The restricted generating family arises naturally because recent Toeplitz recognition singles out a proper subset of bounded affine composition operators; the ambient Fock Toeplitz algebra contains many more. A complete length classification answers how costly it is to construct the missing affine operators by repeated use of permitted **composition** generators. The boundary is unexpectedly rigid: an arbitrarily small nonzero translation raises the exact minimum factor count when a centered slope saturates the optimal angular modulus. The geometric law also quantifies a nontrivial, diverging number of factors as a nonidentity rotation is approached along a ray. These constitute a motivated global classification with exact thresholds and a sharp boundary mechanism, not a parameter-picked finite example.

## Remaining limits

All results are in one complex dimension and use the restricted generator class, not arbitrary bounded Toeplitz factors. The arithmetic tests cannot certify the universal theorem. Equivalent earlier elementary semigroup geometry remains a priority risk. Independent validation is not asserted.

Self-review: passed. Independent audit: not yet performed.
