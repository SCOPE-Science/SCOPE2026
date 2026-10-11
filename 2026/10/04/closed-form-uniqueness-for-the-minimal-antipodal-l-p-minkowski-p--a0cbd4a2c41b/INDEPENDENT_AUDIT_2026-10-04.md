# Independent mathematical audit

## correctness

PASS

Shan's support-transfer lemma implies that any solution for this discrete antipodal measure is a polytope whose facet normals are exactly \(\pm u_i\). With exactly \(n\) independent antipodal pairs, the polytope is therefore a parallelotope. Writing \(y=Ux\) turns it into an axis box with widths \(w_i=a_i^++a_i^-\). Because the rows of \(U\) are unit normals, the Euclidean area of either facet normal to \(u_i\) is \(d^{-1}\prod_{j\ne i}w_j\), where \(d=|\det U|\). The discrete \(L_p\) mass equation \(\alpha_i^\pm=(a_i^\pm)^{1-p}A_i\) determines the plus/minus split of each width. Taking \(q=1-p\), summing the \(q\)-th roots fixes \(w_i\), and multiplying the resulting equations determines the common scale uniquely, giving exactly the displayed \(b_i,B_i,\lambda,a_i^\pm\) formulas. Independent random-dimensional numerical reconstruction for \(n=2,3,4,5\) reproduced all prescribed masses to floating-point residual below \(2\times10^{-15}\).

## originality

PASS

Shan proves a complete existence characterization for arbitrary positive masses on antipodal supports and, for even data, existence of a symmetric solution. The complete paper does not state uniqueness or an explicit inverse formula in the minimal-support case of exactly \(n\) independent antipodal pairs. Targeted searches for a negative-\(p\) antipodal parallelotope uniqueness formula found no equivalent theorem. The audited result uses Shan's existence/support theorem as a starting ingredient, but the algebraic inversion and uniqueness are additional.

## value

PASS

Negative-\(p\) Minkowski problems are generally nonunique, so a minimal-support regime with global uniqueness and a closed inverse map from masses to support numbers is a meaningful structural boundary. The result is exact for every dimension and all positive masses and is not a finite or arbitrarily sliced computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
