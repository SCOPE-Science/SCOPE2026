# Independent mathematical audit

## correctness

PASS

Reconstructed all vertex and capacity inequalities for k-limited domination: a singleton shore cannot dominate omitted neighbors; any two vertices fail either chosen load or an omitted paired vertex. A three-vertex candidate with one L_i and two R vertices forces i>t and both opposite indices <=t; conversely each such configuration works and has selected outside-neighbor count n-2. The mirrored types exhaust |D|=3. Every 2+2 set works for |D|=4; at endpoint t=0,1,n no 1+3 can work and one-shore sets fail, so these are exactly all minima. An independent adjacency/bitset enumeration (not executing package checker) exhaustively confirmed every case n=3..8, all t (39 profiles), agreeing with both counts; universal conclusion follows from the case proof, not finite tests.

## originality

PASS

Bozovic et al. Proposition 1(iv) gives the intact complete-bipartite t=0 case and k-limited definition; matched and unmatched vertices at 0<t<n create two degree classes outside the statement of the complete multipartite formula. Resultary neighboring crown-graph records concern different domination notions. The exact dip, its two transitions, full minimizer classification and multiplicities are not implied by intact endpoint values.

## value

PASS

Edge removal can either decrease or increase the minimum under a fixed near-maximum local omission capacity, disproving both monotonicity intuitions for this natural nested graph family. Exact minimizer geometry/counts can be used as sharp test cases for nonregular limited domination bounds. The capacity n-2 has a structural role, not an arbitrary numerically selected slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
