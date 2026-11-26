# Independent mathematical audit

## correctness

PASS

With r(0)=0 the length equals the first mismatch index, not one less. Since r(2t)=r(t), a first mismatch cannot be even. Existence for arbitrary d also has a direct check: write d=2^s u with u odd, choose L>=3 with 2^L congruent to 1 modulo u (arbitrary L>=3 if u=1), and form 2^s times the sum of u copies of 3 at shifts 0,L,...,(u-1)L. This is a positive multiple of d with exactly u separated 11 occurrences. For prescribed odd k>=3, padded duplication at width L with 2^L=2Q leaves just the boundary pair, so r((2Q+1)x) is 1 exactly for odd Q<=x<2Q in that width. The largest odd a<=Q/(k-1) satisfies a>Q/(k-1)-2. Thus (k-2)a<Q<=ka<2Q, using Q/(k-1)>=2k; all earlier odd multiples stay below Q and even multiples have parity zero. The least admissible Q is <4k(k-1), giving a<4k and d<32k^3. Larger dyadic Q give strictly increasing differences as a is positive and nondecreasing. k=1 is checked by 3 times powers of two. This proves all quantifiers in RESULT.md:5–53.

## originality

PASS

The exact all-odd spectrum for 11 and its polynomial witness bound are distinct on the inspected evidence. Sobolewski posed the matching attainment conjecture and already supplied the duplicated-block formula. Here the multiplier is solved for as a function of the target length, with control of the first mismatch and of the difference size, rather than held fixed to bound lengths as the width increases.

## value

PASS

Resolves a concrete published open question for the classical pattern 11 with exact attainable values, not just unboundedness; gives explicit witnesses of cubic size and infinitely many distinct differences per length. The construction for k>=3 in fact supplies infinitely many odd differences, beyond the trivial rescaling by powers of two.

The dated certificate retains the supplied scientific assessment, sources and limitations.
