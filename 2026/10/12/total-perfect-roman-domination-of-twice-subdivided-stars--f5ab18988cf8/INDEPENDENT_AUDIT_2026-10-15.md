# Independent mathematical audit

## correctness

PASS

Total perfect Roman dominating f:V->{0,1,2} requires each zero exactly one 2-neighbor and each positive vertex a positive neighbor. In Tq^(2) arms c-u_i-v_i-w_i, leaf w_i forces every v_i positive. If center is 0, exactly one u_i=2 and each other arm costs at least3, special arm >=4, yielding 3q+1. For center1, each arm costs >=3 =>1+3q. For center2, u_i=0 forces (u,v,w)=(0,1,1) at cost2; to provide positive neighbor for center, >=1 arm u_i>0 at cost>=3, so total>=2q+3. For q>=3 latter strictly below 3q+1. Equality forces exactly one nonzero-u arm, with either (1,1,1) or (1,2,0), yielding exactly 2q global minima. Independently exhaustively enumerated all 3^(3q+1) assignments for q=2,3,4 (1,655,559 total), obtained (q,min,#opt)=(2,7,24),(3,9,6),(4,11,8), and for q3/4 all minima have center2. Boundary q2 excluded from structural classification. Algebraic center-case proof establishes all q>=3; finite check corroborates.

## originality

PASS

Almulhim 2023 introduces total perfect Roman domination, determines broad upper bounds and equality trees, and calls a subdivided star one subdivision per edge. It does not state the twice-subdivided q-arm exact weight 2q+3 or optimizer count 2q, and known once-subdivided extremal n differs from here (3q+1 vs2q+3). Other Roman/Italian domination literature defines different zero-defender constraints or positive isolation, so variants cannot be substituted. Closest Resultary once-subdivided signed double Italian is unrelated invariant.

## value

PASS

This is a natural next uniform subdivision of the star family singled out by foundational extremal theorem. The weight gap q-2 from the universal order bound and exact two-state optimizer family provide structural information beyond the lower bound or single numerical case; useful as benchmark for dynamic programs and characterizing effects of edge subdivision.

The dated certificate retains the supplied scientific assessment, sources and limitations.
