# Independent mathematical audit

## correctness

PASS

For nonempty intervals [i,j] on a line of n points, strict root order is proper interval containment, no extra predicates or named simple roots. A rank-3 sentence exists chains of length k<=7: pick x with r lower and s upper chain elements, r+s+1=k, r,s<=3; the two side clauses each have rank<=2 and the outer quantifier adds 1. For upper bound, exact full atomic triple diagram H_n = { { {At(x,y,z):z}:y}:x} completely characterizes quantifier rank 3. The source C++ enumerates n=1..26, corroborated by a separate immutable Python code through n=12. Independently implemented a new exhaustive C++ ordered triple signature for all n<=26 and recovered exactly seven theories, with n>=7 identical through 26. For n>=26 the proved endpoint-gap EF game invariant t_0=0,t_(r+1)=3t_r+2, t_3=26 maintains exact small gaps and large gaps, for at most two endpoints per interval move, hence uniform rank-three tail; combine finite census and infinite EF argument. The rank-three threshold is sharp.

## originality

PASS

Best-of-knowledge originality after checking exact formulations, stronger work, tables and implication: Finite linear-order EF bounds can be transferred to intervals using two endpoints per move but their coarse threshold t3=26 does not establish the exact seven cutoff. These general root-system studies have broader object families but do not imply the claimed first-order rank-3 equality of finite type-A reducts. None of the compared root-poset enumerations implies rank-3 elementary-equivalence for all n>=7. Interval interpretation plus the basic EF game gives a much weaker sufficient cutoff 26; the sharp finite range remains additional work.

## value

PASS

Complete sharp classification of the first useful nontrivial finite-model-theoretic type spectrum for the natural type-A root-poset containment reduct, including a finite representative of at most 28 roots. Exact finite certification plus a uniform infinite EF game argument settles a mathematically natural structural question; the seven cutoff is not a mere renaming of ordinary finite-linear-order EF theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
