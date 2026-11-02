# Independent mathematical audit

## correctness

PASS

Read actual 8571-byte RESULT.md at blob f665bb8dd199b19ac875141ebec4587114984932 and verify.py at 111c952a0e29946039f78bf4585fc193786f26c9. Use iid Uniform[0,1] probability integral transformation. For i<j the record event depends only on preblock values, independent of block relative ranks. For i past the window, a record depends on earlier block only through its unordered values, conditionally independent of internal ranking. Inside the block i=j+r−1, the event requires a prefix maximum and all j−1 earlier values below the block σ_r-th order statistic, giving η E[B_{σ_r,k+1−σ_r}^{j−1}]. Its exact beta moment establishes the kernel. Summing proper prefix-record values gives k/(k−b) by E(1−B)^−1 and a harmonic cancellation gives −(k−1). Independent enumeration of all uniform permutations n=3..7 and k≤4 checked 2170 positional covariances and all 30 k=3 total covariance formulas. The derivation proves all n≥k and fixed-k limit; no asymptotic independence is claimed.

## originality

PASS

Qualified PASS: Borga derives consecutive-pattern CLTs for restricted permutation classes; Crane–DeSalvo treats consecutive-pattern avoidance and Poisson approximations; Even-Zohar treats classical pattern representation statistics. None of the primary material inspected states the global-record/consecutive-pattern positional joint kernel or sharp constant. However joint-statistic identities could have appeared in older record theory without using this terminology.

## value

PASS

The kernel localizes a global record statistic against a finite-window permutation pattern, reducing all cross-covariances to one beta moment. Its exact limiting extremizers and finite sign reversal reveal nontrivial dependence not determined by either marginal expectation; the all-pattern formula is a natural structural statistic, not a one-off small enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
