# Independent mathematical audit

## correctness

PASS

The frozen structural and counting statements are correct. Bracket preservation forces the central block C=Λ²A; idempotence gives A²=A and BA+CB=B. For V=U⊕K, with U the image and K the kernel of A, the off-diagonal restrictions are B(U)⊂ker C and B(K)⊂im C. The shear with T|U=B|U, T|K=−B|K satisfies TA−CT=B and conjugates the graded projection to F, also in characteristic two. Counting U, its complements and the two independent restrictions of B gives the frozen map count. Images are graphs over U modulo Λ²U; each such graph is realized by a shear, has exactly the stated number of maps from the choices of K and B|K, and is not an ideal for 0<r<n because u∧k lies outside Λ²U. An independent binary n=3 packed-bit check tested all 64³ generator-image triples by checking F(F(e_i))=F(e_i) for every basis vector and comparing the image point sets. It gave [1,224,896,1] maps, [1,56,112,1] images and fibers [1,4,8,1] by rank (`python3 /workspace/branches/review_replay.py 4`). The frozen checker was inspected, not executed. For the repaired law: extracting the Gaussian factor gives W=q^E c with 1≤c≤C_q and the stated cubic E. Its derivative is positive at 0, negative at n, with unique positive root t_n; E'' at the root is −S_n. The exact cubic expansion gives left and right exclusion gaps at least S_n/2−7 and S_n/2+1 respectively, and all farther ranks are smaller by monotonicity. This proves the quantitative upper bound and ratio limit. The additional sharpness proof uses E(r+1)−E(r)=−3r²+(n−5)r+(n²+3n−4)/2. Its root is an integer r=(n−5+m)/6 on the norm-nine Pell sequence (7n+4)^2−7m²=9 with n+m≡5 mod 6. Checked the seed and that multiplication by 8+3√7 preserves both conditions and grows n, with r,r+1 admissible. Equal consecutive values and the strict increase/decrease force r=k_n. Both c-factors tend to C_q, so the two probabilities converge to 1/2 because the outside mass goes to zero. The first 12 iterations were also checked with exact integers; the first four pairs of n and tied lower rank are (24,14),(391,237),(6240,3791),(99457,60432). The infinite assertion is analytic, not numerical extrapolation.

## originality

PASS

Original as packaged: FAIL on the claimed complete conjugacy and labeled-map census as a distinct contribution, because 7573f7956962 already gives both over the same domain. The embedded-image formulas are straightforward supporting linear algebra; they are no longer headline claims. The repaired scope explicitly credits the known weight, uses two-rank localization as context, and makes the distinct contribution the explicit infinite subsequence with two adjacent ranks of limiting mass exactly 1/2 each. Neither the finite-count statement nor two-rank localization alone establishes that a single moving rank cannot suffice. This pass is for the repaired claim only.

## value

PASS

The repaired theorem distinguishes localization from actual concentration on a single moving rank, a distinction of interest in exact discrete rank laws. It identifies a motivated infinite resonance: on the explicit norm-equation sequence the two main counts become equal in proportion and every other rank has exponentially small total mass. Thus there is an obstruction to improving the number of retained ranks, not just a change of constants or a recomputation of a known rank table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
