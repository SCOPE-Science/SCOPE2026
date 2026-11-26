# Independent mathematical audit

## correctness

PASS

The nonzero equilibrium and its characteristic polynomial follow by substitution and expansion. An independent check bypasses singular Routh rows: write the cubic as (z−r)(z²+uz+b/r), where r>0 exists by the sign of the constant term. The other two roots have positive product and the sign of their real parts is the opposite of the sign of u. With p=b−a and Δ=p(1−ab+2b/a)+b one has u=p+r and Δ=u(b/r−pr). Thus p≥0 gives index one, and for p<0 the index is three exactly for Δ<0, with only Δ=0 giving a neutral pair. Substitution of b=at gives Δ/a=a²t(1−t)+2t²−1; at neutrality the remaining quadratic is z²+t/(1−t). The derivative of b_H(t)² in RESULT.md lines 51–55 gives strict monotonicity on either side of its sole maximum, and b_H(t)²−1/2=−(2t−1)²(1+t)/(2(1−t)) also confirms genuine quadratic contact. At fixed b the map a=b/t is bijective, so the two crossings bound exactly the index-three interval; at tangency and on the rest of the neutral curve the strict-positive count is one. No nonlinear Hopf claim is needed. The frozen checker was inspected, not run; its finite samples are not the proof.

## originality

PASS

The inspected sources supply the precise Case H model and numerical two-parameter dynamical regions but not the exact unstable-index wedge, neutral spectrum and fixed-b coalescence theorem. This is a best-of-knowledge finding restricted to that local spectral claim.

## value

PASS

An exact local benchmark for a canonical two-parameter chaotic-flow family: it tells users where an index-three equilibrium can exist, when two neutral parameters merge, and where that entire mechanism is excluded. The complete slice classification and exact cutoff add information beyond applying a cubic sign rule at a chosen sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
