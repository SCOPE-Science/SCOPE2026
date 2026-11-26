# Independent mathematical audit

## correctness

PASS

In each indexed prism column a selected rung, top rail or bottom rail excludes all other edges starting in the same or a neighboring column. At directed separation two a starting rung allows every second type; a starting rail allows only the opposite rail. The wrap-around tests enforce both orientations when n=4, and for n=3 every pair of distinct columns is consecutive. Larger separations in both directions cannot give adjacent endpoints. The seven-state closed walks keep the first column fixed by the vertex labels, so trace counts indexed words, not rotation classes. Independently, the block for the allowed distance-two pairs in order R,T,B has rows (1,1,1),(0,0,1),(0,1,0). Eliminating the transit states gives, with d=zt², the determinant (1+d)[(1−t)(1−d)^2−zt³(3−d)], the claimed factorization. The formal logarithmic derivative gives the traces; the only excluded traces are 1 and 1+2z at lengths one and two. All-rung choices attain floor(n/2). At odd n, the sole gap of length three leaves an open chain of occupied types; there are n choices for the gap and n types of chains (all rungs or a first rail of either kind followed by forced alternation). At even n, each of two supports allows all rungs and allows two additional alternating rail assignments exactly when n/2 is even. Independent exact adjacency checks over 87,360 words for n=3..8 agreed, including 1+24z+148z²+176z³+6z⁴ at n=8. Frozen verify.py was inspected, not executed; it documents a separate finite check through order nine and extremal traces through order 44. The graph bijection, determinant identity, and gap proof, not either finite range, establish the theorem.

## originality

PASS

The strongest inspected open-ladder formula gives exactly one determinant factor, but it has different boundary conditions and already different coefficients for four columns. The closest same-host exact indexed result counts vertex dissociation sets, and the univariate size marking does not select those with no isolated vertex. The cyclic trace, its additional factor and the closed maximum-set multiplicities survive those and the matching-table comparisons. This is a bounded assessment, not a priority guarantee.

## value

PASS

The prism is the natural periodic version of the classical open width-two problem. Closure changes the transfer modes that contribute to the all-size distribution, and changes the extremal structure sharply: quadratically many optima at odd n become only six or two at even n. This supplies exact benchmarks for a canonical cubic family rather than a few computed coefficients.

The dated certificate retains the supplied scientific assessment, sources and limitations.
