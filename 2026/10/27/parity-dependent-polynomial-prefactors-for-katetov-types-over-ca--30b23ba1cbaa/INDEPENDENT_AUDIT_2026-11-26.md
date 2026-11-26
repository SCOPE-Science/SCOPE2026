# Independent mathematical audit

## correctness

PASS

Homogeneity and the one-point extension property identify types with feasible labeled positive distance words. Such a word is nonalgebraic: arbitrarily many new points can be assigned that same vector with mutual distance 1, which satisfies all triangles. The triangle lower bound on base distances follows from adjacent Lipschitz steps and the fact that the label difference is always less than D. On the high alphabet [ceil(D/2),D], the remaining sum inequalities are automatic. The looped path transfer matrix has eigenvalues 1+2cos(j pi/(m+1)); its simple Perron eigenvalue dominates in absolute value and the projection of the all-ones vector gives S^2/Q. If a label s<=floor(D/2)-1 appears, the two tails at distance at least D must use labels >=D-s, at most floor(D/2) labels in total; counting tail walks around a bounded window and summing over the selected position gives O_D(n mu_D^n) with mu_D<lambda_D (no such labels for D=2,3). This proves the even estimate. For odd D=2r+1 the sole remaining defect label r can occur only within a span L<=D. Its first/last occurrences select a unique span, counted by (B^(L-1))_(r,r), with all internal sum constraints automatic. A nonempty high tail next to the defect is anchored at r+1 and has a_k=e_1^T A^(k-1)1, with a_0=1. For each fixed L, the n-L-1 terms with two nonempty tails contribute the leading Perron product (Sv_1/Q)^2 lambda_D^(n-L-2) per term; the spectral cross terms sum geometrically and the empty-tail terms contribute only O_D(lambda_D^n). This gives the stated positive c_D and error, and the paired dimensions use the same transfer size. At D=3, q=(1,1,2), H_n=2^n and a_k=2^(k-1) for k>=1 give the stated sample and exact formula. The D=4 specialization also gives C_4=(1+sqrt(2))/2.

## originality

PASS

The distinct claim is the full fixed-diameter capped-path spectral asymptotic, with a paired even/odd rate, explicit leading constants and a linear odd-diameter prefactor. The general extension correspondence is known. A capped-tree catalogue record overlaps exactly with the D=3 path formula for n>=8, which is not being credited as novel. The Widom–Rowlinson record itself treats bases with only distances 1 and 2, not general capped diameter-three paths. The strongest inspected matches do not establish the all-diameter asymptotic.

## value

PASS

The natural one-point extension count gauges how much the path distance data constrain the surrounding metric structure. Determining that successive even/odd caps have the same spectral rate yet a linearly differing count is a sharp structural result not visible from exponential growth alone. The proof isolates a freely positioned but bounded span of critical distances, explains the prefactor and gives quantitative leading constants for every fixed cap. The diameter-three example alone is not the value proposition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
