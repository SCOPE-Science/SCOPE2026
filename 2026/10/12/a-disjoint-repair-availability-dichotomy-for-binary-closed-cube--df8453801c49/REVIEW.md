# Independent mathematical audit

## correctness

PASS

With d=r−1 cube bit-flip matrices T_i commuting and squaring to I over F2, B=sum T_i satisfies B²=dI and S=I+B satisfies S²=(r mod2)I. All dual checks are exactly (St,t). Odd r yields S²=I, so dual code is self-orthogonal; two target-containing checks disjoint off the target would have odd intersection, impossible. Even r yields S²=0; systematic symbols are similarly restricted by orthogonality of image vectors St; parity admits disjoint checks for t=e_v and t=Se_v. For even r>=4, rank(S)=N/2, ker S=im S self-orthogonal, and every nonzero image has weight>=4; among k disjoint parity checks at most one has zero image, giving 4(k−1)<=N. For r=4 the explicit hex t=c3,11,09 give three mutually disjoint helper supports, sharp at k=3. Independent exact dual-check enumeration at r=2,3,4 confirmed systematic/parity availability (1,2),(1,1),(1,3) and localities (2,1),(3,3),(4,3). This finite enumeration does not claim exact availability for even r>=6, appropriately left bounded.

## originality

PASS

Kenjale and Garge establish the Suslin–Rao systematic block construction and parameters; Fish–Key–Mwambene older reflexive cube papers study closed-cube code constructions, self-duality and related designs. The full 2026 source examined did not identify a theorem about unlimited-size pairwise disjoint recovery sets for the two fixed coordinate classes. The 2011 paper was only available by abstract; stronger prior repair/classification coverage remains material risk, but inaccessibility alone is not scientific failure. Searches of indexed results for these exact cube-code recovery facts found no covering theorem.

## value

PASS

A clean parity-dependent obstruction and construction for disjoint linear single-symbol repair in a natural structured code family is of genuine coding-theoretic interest; the r=4 sharp three-way recovery and general even-r upper bound are structural rather than tiny arbitrary brute-force invariants. Exact larger-even availability is honestly left open.

The dated certificate retains the supplied scientific assessment, sources and limitations.
