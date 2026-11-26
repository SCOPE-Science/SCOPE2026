# Independent mathematical audit

## correctness

PASS

The structural theorem applies strictly in both claimed ranges, since k>0.4n+0.8. It leaves the all-odd clique and sets wholly in an upper window of size m+2 (starting at m or m-1). Such a window has too few odds to allow even one edge to the all-odd clique. Classification by the minimum is exhaustive: odd n with minimum m forbids 2m and requires omitting one of m+1,2m+1; even n with minimum m-1 forbids 2m-2 and the pairs {m,2m-1}, {m,2m}, {m+1,2m}. The other minimum cases have only the doubling constraint or none. This yields exactly the listed families. In the upper window, an edge is equivalently an intersection of size one between the two-element omission sets (odd n), or of size two between the three-element omission sets (even n). In the even case, writing a=m-1,b=m,c=m+1,d=2m-2,e=2m-1,f=2m, omissions are {a,b,t}, {a,f,s}, and {d,e,f},{b,d,f},{b,c,d}; common pairs give exactly 2(m-1) U-to-V edges and the nine stated others. In the odd case the omissions are {m,t}, {2m,2m+1}, {m+1,2m}, producing the five extra edges. These edges give the two connected components and the edge totals for all n in scope. An independent exhaustive combination/bit-shift enumeration and common-deletion adjacency at /workspace/review-evidence/3/boundaries.py reproduced (18,47,[9,7,1,1]) at n=13 and (31,125,[20,9,1,1]) at n=18, and the stabilization profiles at n=15 and n=20. The conclusion is sharp for eventual stabilization, not a monotonicity claim below the thresholds. Supplied scripts and recorded outputs were inspected, not executed.

## originality

PASS

Best-of-knowledge pass for the fixed-size exchange graph, including its sharp parity boundary, not for density structure or extremal set size. The strongest prior theorem is precisely the structural dichotomy used in the proof. It supplies a search domain for the upper-window configurations, but not their legal omissions, adjacency classes, connectivity, or the boundary counterchecks. No equivalent exact table or stronger covering theorem was found in the sources inspected.

## value

PASS

One deletion and insertion is the natural fixed-size move, and one below maximum is the first near-extremal slice where new states and links matter. The full clique/attachment description determines reachability and bottlenecks, while the independently checked counterexamples identify the exact distinct stabilization cutoffs by parity. The contribution is the connected structure, not merely a few small counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
