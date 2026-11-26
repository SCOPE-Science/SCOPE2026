# Independent mathematical audit

## correctness

PASS

Each coordinate of the greedy product represents the longest matched prefix and leaves exactly the corresponding pattern tail. In the region with i<r and j=s+t, the t post-threshold zeros are among the i zeros read, so t<=i; the other one-threshold region is its mirror. The first threshold crossing before the other forces the earlier finisher to progress when the later threshold is crossed, excluding (r,s). The supplied witnesses cover all other listed states. Testing whether continuations intersect 0*1* and 1*0* distinguishes the four regions. For example in the second region a continuation 0^a1^s0^b is accepted exactly when a>=r-i and a+b>=r-t; since r-i<=r-t, these are separately attained minima and recover both coordinates. The mirror test, two single-threshold tests in the first region, and independent remaining letter counts in the fourth cover all pairs. The four cardinalities sum to (r+s)(r+s+3)/2+rs. The acceptor is complete, with the terminal pair accepting and absorbing, and the count also gives 3t(t+1) when r=s=t.

## originality

PASS

The inspected older literature provides subsequence-ideal and piecewise-testable frameworks and general bounds, not the exact restricted quotient count. A distinct later catalogued finding explicitly states the same intersection result alongside a union theorem; that is equivalent coverage, but does not show earlier coverage of the frozen finding. This is a bounded pass, not an absolute priority determination.

## value

PASS

This family tests simultaneous satisfaction of two opposite-order subsequence constraints, a natural composition of simple pattern monitors. The result gives the exact achievable memory in states for every threshold pair and identifies the full quotient structure, rather than only bounding the product or reporting a minimum accepted length. The two threshold regions and their separately observable continuation minima explain the state count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
