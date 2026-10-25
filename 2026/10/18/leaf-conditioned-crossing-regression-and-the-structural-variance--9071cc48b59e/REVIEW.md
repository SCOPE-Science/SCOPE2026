# Independent mathematical audit

## correctness

PASS

PASS. For a uniform labelled Cayley tree in a fixed convex cyclic order, conditional on abstract tree shape each vertex-disjoint edge pair crosses under uniform relabeling with probability 1/3. Writing m=n-2, B=binom(m,2), and J for equal-code-position pairs in iid Prüfer word, the number of disjoint tree-edge pairs is B-J, giving U_n=(B-J)/3. Conditioning on L=ell missing symbols means k=n-ell occupied symbols; merging a specified equal pair of positions gives conditional collision probability S(m-1,k)/S(m,k). Stirling row strict log-concavity and recurrence prove the displayed strictly decreasing leaf regression, with path and star endpoints. Counting covariance of pair-equality with symbol-absence indicator yields Cov(X,L)=-B ((n-1)/n)^(n-3)/(3n). Distinct pair-equality indicators are pairwise uncorrelated, giving Var(U)=B(n-1)/(9n²); direct absence covariance supplies exact leaf variance and asymptotic squared Corr(U,L)=1/[2(e-2)]. The published total variance Var(X)~n³/45 is explicitly prior, giving shape fraction 5/(2n²) and Corr(X,L)~constant/n. Independently enumerated the 125 n=5 Prüfer words and actual crossings: means for 2,3,4 leaves (1,2/3,0), covariance -16/125, matching formula. Inspected source verify.py exhaustively enumerates n<=8 and tests Stirling inequalities through m=100; finite checks do not prove all n.

## originality

PASS

Best-of-knowledge PASS for the precise leaf-stratified crossing regression, strict monotonicity, mixed covariance and structural-vs-geometric variance split. The known fixed-tree expected crossing count and known total crossing variance are properly prior; the conditional occupancy/Stirling calculation and its sharp correlation quantify the new leaf effect.

## value

PASS

PASS. Leaves encode tree branching and crossings encode geometric entanglement of a random labelled tree; their negative conditional relation is a natural joint statistic. The exact all-leaf regression, strictly ordered boundary and separation of shape-induced versus geometric crossing variance answer a meaningful structural explanation question, including a quantitatively precise 69.6% linear contribution to the shape mean.

The dated certificate retains the supplied scientific assessment, sources and limitations.
