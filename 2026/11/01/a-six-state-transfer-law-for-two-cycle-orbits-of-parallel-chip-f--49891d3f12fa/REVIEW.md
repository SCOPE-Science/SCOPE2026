# Independent mathematical audit

## correctness

PASS

For any primitive two-cycle c→F(c)→c on connected graph, summing updates gives Laplacian(s^0+s^1)=0. The sum of two 0/1 firing indicators is constant and cannot be 0 or 2 for a primitive cycle; it is 1. Given phase colors φ_v=s_v^0, opposite-phase neighbour count b_v determines exactly b_v admissible starting chip values: if φ_v=1, d_v≤c_v≤d_v+b_v−1; if φ_v=0, d_v−b_v≤c_v≤d_v−1. All are nonnegative and second update returns, yielding N_G=(1/2)∑_φ∏_v b_v. On open ladders the rung-product factors through sixteen ordered binary pair types; global complement plus row swap collapses to six invariant classes with displayed 6×6 transfer B and vectors L,R. Then N_n=(1/2)L B^{n−2}R. Verified determinant det(I−zB)=(1−z)^3(1+z)(1−12z+z²), scalar numerator cancellation, fourth-order recurrence and asymptotic dominant root 6+√35. Independently computed a direct full sixteen-pair transfer from rung indicators and confirmed first eight integer counts through n=9, plus separate exact matrix characteristic/minimal scalar generating function checks; finite sums not the proof of the all-n rational identity.

## originality

PASS

The phase-cut identity and transfer-matrix methodology are acknowledged background, not independently novel. The originality claim is the explicitly evaluated six-state quotient and exact generating function for counts of primitive temporal two-cycle orbits on every open ladder length. Dall’Asta solves one-dimensional ring fixed-energy dynamics, Jiang restricts temporal periods, Fey–Levine–Wilson has the same ladder geometry but a stationary-density observable with a different transfer eigenvalue, and Jiang–Scully–Zhang constrains firing patterns generally. None of the inspected mathematical statements logically gives these N_n or the rational function; the queried mathematical record corpus returned unrelated six-state/Fourier results. Unindexed transfer enumerations remain a plausible historical risk.

## value

PASS

Open ladders form the smallest genuinely cyclic width-two strip, an intrinsically motivated next family after paths and trees for recurrent parallel chip-firing dynamics. The count includes all labelled nonnegative primitive two-cycles at every n, not a convenient finite sample. The unexpectedly compact rational generating function, fourth-order recurrence and growth constant 6+sqrt(35) quantify recurrent-state complexity and give an exactly solved width-two benchmark. No basins, longer periods or fixed-total counts are implied.

The dated certificate retains the supplied scientific assessment, sources and limitations.
