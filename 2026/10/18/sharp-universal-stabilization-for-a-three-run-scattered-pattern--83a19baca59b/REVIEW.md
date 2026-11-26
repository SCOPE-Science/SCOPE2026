# Independent mathematical audit

## correctness

PASS

For k>0 the gap bijection has A>=s+t and exactly s+t inactive gaps. A one in active gap i contributes C(i,s)C(A−i,t), as positions of the selected zeroes before and after it are independent. Setting u=A−s−t+1 and j=i−s gives weight at least (j+1)(u−j)=u+j(u−1−j), so u*h<=k for h active ones. The inequality u+h<=uh+1 gives M<=s+t+k, and enumeration of the inactive gaps yields the stated fixed-k length series. For n>=k+1 a term with n<M has 0<=n−M+d<d and vanishes in both interpretations. At n=k only maximal M contributes a defect of (−1)^d per configuration. Equality requires uh=k and u=1 or h=1. The u=1 configuration always exists; when h=1 and k>=2 an interior gap has weight>k, and the two endpoints contribute exactly for t=1 and s=1 respectively. When k=1 these cases coincide. The u=1 term also makes the leading coefficient strictly positive. Inspected check.py and its recorded output, not executed. Independently enumerated literal position tuples for n=0..10, s,t=1..3, k=1..6, and counted active vectors via multisets: 594 length identities and 54 exact signed-defect checks passed. Replay: python3 /workspace/check_three_run_independent.py. The unbounded conclusion rests on the inequalities and equality classification, not those checks.

## originality

PASS

Credit earlier polynomiality, exact degree, and general skeleton enumeration. The supported contribution is the sharp uniform onset and defect for the complete three-run singleton-middle family, with a gap representation giving precise numerator support and its top multiplicity.

## value

PASS

A natural infinite pattern family admits a stabilization age bounded solely by the frequency, even for arbitrarily long outer runs. The exact nonzero defect shows this bound is attained for each parameter choice and identifies precisely when additional maximal configurations occur. Those facts refine prior eventual polynomiality substantively; the degree statement by itself would not.

The dated certificate retains the supplied scientific assessment, sources and limitations.
