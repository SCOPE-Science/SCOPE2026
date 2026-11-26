# Independent mathematical audit

## correctness

PASS

A forcing seed smaller than n must permit a first force, which consumes at least the degree of its source in initial black vertices. Only the two deleted-edge endpoints have degree 2k-1. A size-(2k-1) seed that forces must therefore be its first source plus all but one of that endpoint's surviving neighbors; in particular the other endpoint is absent, so there is no ambiguity about the first source. Center at 0. After the first move the black set is [-k,k] minus d. For d<k, 0 has no white neighbor. Black x in [2,k] sees the two white vertices k+1,k+2; the negative side is reflected. For black x=1 use k+1 and d, and for x=-1 use -k-1 and d, with d+1<=k. The gap outside [-k,k] has at least two vertices (n>=2k+3), so the indicated neighbors remain white and distinct modulo n. Thus the process stalls. The interval [-k,k-1] grows clockwise using sources 0,1,...,n-2k-1, each with exactly one white neighbor at distance k, avoiding any shorter deleted edge. For d=k the post-first-force set is already this same interval, and grows in the opposite direction using sources -1 through -(n-2k); none equals 0 or k modulo n, so none uses the deleted edge. Reflection handles the other center. The 2k-1 omitted-neighbor choices per center are distinct, and the two centers' families cannot meet since each member contains its own endpoint but not the other. At k=1 this gives the two endpoints of the resulting path. Checked the all-parameter argument in RESULT.md lines 19–36 and inspected the supplied finite verifier without executing it. The recorded 80 cases and 341272 subsets are only corroborative.

## originality

PASS

The closest indexed results classify minimum seeds on the intact cycle power. The distance-sensitive one-edge spread and the complete smaller seed family in the degree-deficient graph are the distinct contributions. The general edge-spread bound and the intact value and interval forcing method are not claimed as new.

## value

PASS

The natural question is which edge classes attain the nontrivial extreme of the known deletion bound on a standard graph family. Resolving every admissible distance, and giving all minimizing seeds precisely when the drop occurs, is structurally useful beyond recomputing the intact value. The argument stays within its sparse-cycle boundary n>=2k+3.

The dated certificate retains the supplied scientific assessment, sources and limitations.
