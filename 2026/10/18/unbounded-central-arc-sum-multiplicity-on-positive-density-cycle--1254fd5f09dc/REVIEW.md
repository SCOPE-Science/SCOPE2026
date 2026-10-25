# Independent mathematical audit

## correctness

PASS

For each h, PNT supplies 2h distinct odd primes d_i,e_i in fixed proportion intervals with 3/4<e_i/d_i<4/5. CRT chooses k with d_i|k and e_i|(4k+1), giving full k progression modulo P=product d_ie_i. Set n=4k, u_i=2ke_i/d_i even, v_i=d_i(4k+1)/e_i odd, and u_iv_i=n(n+1)/2. Thus endpoints (v-u+1)/2,(v+u-1)/2 are integers, interior to [1,n] by ratio bounds for sufficiently large k; their interval sum is half the total. Different ratios yield h distinct lengths <n/2 and their complementary wrapping arcs >n/2 yield 2h distinct arcs. Progression n=4k mod 4P has density 1/(4P). With primes at X=h(log h)^2, P<=(1.01X)^(2h), representative k in [P,2P), log n<=(2+o(1))h log h; hence quantitative limsup >=1. Independently checked (d,e,k)=(17,13,68): n=272, arc [127,230] length104 and its complement have target sum18564. Source code checks finite examples only; quantified proof invokes PNT/CRT.

## originality

PASS

Best-of-knowledge originality based on actual compared primary scientific claims and explicit residual risks; inaccessible texts not presumed to be absent or covering.

## value

PASS

The half-total arc target is fixed by complement symmetry in the consecutive-label cycle and is a canonical invariant of the existing cycle-sum question. Showing its multiplicity unbounded on a positive-density arithmetic progression and an explicit limsup rate provides an arithmetically meaningful counterpoint to known global sum-incompleteness, not an arbitrary slice. The proof supplies infinite progressions rather than a single numerical witness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
