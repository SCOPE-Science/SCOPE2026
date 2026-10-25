# Independent mathematical audit

## correctness

PASS

For each prescribed r=1,2,3 disjoint edges, inclusion probability p_r is the reciprocal product (2n-1)(2n-3)... . Regularity implies nd_i color-i edges and 2n d_i d_j intersecting ordered pairs for i != j, giving second moments and covariance A_n(di delta_ij -di dj/(2n-1)), positive rank q-1. For ordered triple choices, starting with disjoint i,j edges, counting k-edges away from four endpoints produces Q_ijk=n(n^2-6n+10)d_i d_j d_k -T_ijk: each forbidden common third vertex is one colorful triangle. Plugging Q p3 into the definition of third joint cumulant gives exactly the asserted universal coefficient and negative triangle term. For affine K8, colors are nonzero XOR differences; a+b+c=0 gives 8 triangles, else 0. Independent standard-library exhaustive enumeration of all 105 perfect matchings on eight vertices reproduces kappa(1,2,3)=-32/1715, kappa(1,2,4)=296/5145, and kappa(1,3,7)=296/5145 without using the asserted counting formula. This is a finite check, not the all-n proof.

## originality

PASS

Woolbright-Fu prove a rainbow perfect matching exists in every one-factorization, not third cumulants under the uniform random-matching measure. Acan Theorem 4.2 gives Poisson limits of fixed short-chord counts in random chord diagrams, not exact third cumulants for arbitrary regular color partitions. General edge-inclusion moment expansions could algebraically recover T_ijk; no dominating published closed triangle-fingerprint theorem was found. The exact dependence, covariance universality, and affine sign switch are the proposed original package.

## value

PASS

The third mixed cumulant pinpoints the first statistic sensitive to triangle geometry even though means and covariances are fixed by color degrees. It supplies a directly reconstructible combinatorial invariant and an explicit opposite-sign witness inside one regular factorization, of use to random matching and edge-colored design comparisons.

The dated certificate retains the supplied scientific assessment, sources and limitations.
