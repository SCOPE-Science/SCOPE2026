# Independent mathematical audit

## correctness

PASS

For binary closed-neighborhood Lights Out, subtracting vertex equations within one independent part forces a common press bit y_i. With epsilon_i=n_i mod2 and t=sum_j epsilon_j y_j, each part equation is (1+epsilon_i)y_i+t=1 over F2. If no odd parts all y_i=1 is the unique clearing vector; otherwise every odd part forces t=1 and every even part y_i=0, leaving parity-odd selections of odd parts. This yields the full press-set polynomial [prod_{odd}(1+z^{n_i})-prod_{odd}(1-z^{n_i})]/2, 2^{o-1} solutions, and minimal support min odd part size. The homogeneous equation similarly has dimension max(o-1,0), so A+I invertible iff o<=1. Independent explicit toggling-mask exhaustive checks over multiple multipartite profiles (including 5 odd singleton parts) match the formula and count. The proof applies arbitrary r,n_i, not merely bounded enumerations.

## originality

PASS

Best-of-knowledge PASS for general multipartite all-on clearing-set WEIGHT ENUMERATOR and full solution characterization, not general affine F2 formulation already known. Earlier Ballard–Budge–Stephenson covers complete BIPARTITE nullity over cyclic rings and Codsi et al. 2026 covers extremal graphs more generally; neither inspected source supplies the stated full multinomial-part odd-selection enumerator.

## value

PASS

The complete multipartite graph is a natural dense graph family and all-on press-subset size distribution is a meaningful finer Lights Out invariant. Formula simultaneously classifies every optimizer, all clearing sets and binary nullity, extending bipartite scalar statements; a mathematician studying minimum-press instances can use its exact coefficients.

The dated certificate retains the supplied scientific assessment, sources and limitations.
