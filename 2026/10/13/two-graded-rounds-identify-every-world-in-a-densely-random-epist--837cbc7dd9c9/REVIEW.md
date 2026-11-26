# Independent mathematical audit

## correctness

PASS

Reconstructed the asymptotic argument for independent Bernoulli markings at each fixed 0<rho<1 and two named reflexive relations. Depth one is exactly (atom,row degree,column degree) because the row and column sizes are known; depth two detects each row's histogram of column degrees at marked cells and the transposed histogram at each column. In fact the two histograms plus the atom give the exact depth-two type: they give the respective own degrees by summation, and the unmarked counts at each opposite degree are its globally fixed marginal count minus the marked count. Pairwise distinct histograms on both sides suffice, but are not assumed necessary for cell injectivity. For a fixed pair of rows, columns where entries agree contribute zero; at a disagreement the column degree equals its degree with both rows removed plus one. Conditioning on all such reduced degrees therefore leaves disjoint bins of independent centered variables taking values -1,0,1. Their characteristic function is nonnegative, and Gaussian domination on [-pi,pi] gives the required O_rho(m^(-1/2)) zero-sum bound. A central window of order sqrt(n) reduced degrees has point masses bounded below by a rho-dependent multiple of n^(-1/2) by Stirling, so Chernoff and the union bound ensure all these bins have at least order sqrt(n) columns with failure O_rho(sqrt(n) exp(-c_rho sqrt(n))). Multiplying the conditional bounds and adding that failure gives o(n^(-2)) for each pair and hence no collisions on either side with probability tending to one. Hoeffding bounds both ranges of degrees by O(sqrt(n log n)), giving at most O(n log n) depth-one types. A union bound excludes monochromatic rows and columns; same-atom equivalence is then an ordinary bisimulation by the availability of both colors for each named move. Finite Boolean closure gives the two claimed algebra sizes and the sharp quotient ratio. An independent exact enumeration of the direct depth-two signature (replay: /workspace/branches/record-2-independent.py) reproduced the supplemental 2, 8 and 144 fully separated matrices at sizes 1, 2, 3, respectively. The frozen code was read, not executed; these finite counts are not evidence for the limiting probability bound. No assertion uniform over varying densities or all finite n is needed.

## originality

PASS

The distinct content supported here is the sharp dense random cell-modal depth and simultaneous ordinary collapse, with an exact independent-bin argument, not generic graded refinement semantics or the extremal quotient ratio. The known sparse deterministic extremal example materially overlaps the ratio and terminal algebras but makes a different parameter and minimal-depth assertion. No verified stronger result covering the fixed-density random statement was found in the comparisons below.

## value

PASS

For a standard product of two equivalence frames with one random atom, the sharp minimal modal depth and contrast between the two resulting algebras answer a natural typical-case expressivity question, not merely an example giving the maximum ratio. The conditioned-degree-bin argument gives a usable mechanism for separating profiles in a model where taking full degrees as independent would be wrong. The value is specific to the fixed-density theorem and does not require a sparse threshold theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
