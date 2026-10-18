# Independent mathematical audit

## correctness

PASS

For uniform recursive tree (n>=2), L_{n+1}=L_n+1-J_n and W_{n+1}=W_n+n+D_n(U_n). With S_n=sum_leaf D_n(v), sum_all D_n(v)=2W_n gives the conditional closure E[S_{n+1}|T_n]=S_n+(1-1/n)L_n+n+2W_n/n. Solving yields E[W]=n(n+1)H_n-2n²; E[S]=n(n+1)H_{n-1}-(n-1)(7n+6)/4. Subtracting mixed mean recursion gives b_{n+1}=(n+1)b_n/n-(n-1)(n-2)/(4n), b_2=0, hence Cov(L,W)=nH_n-n(n+5)/4+1/2, zero n=2,3 and negative n>=4. Mean distance normalization tends to -1/2. Fresh exact-fraction enumeration over all recursive trees n=2..8 recomputed leaf count, Wiener index and transmissions directly, without treating finite samples as infinite proof.

## originality

PASS

Earlier random-recursive-tree work treats Wiener moments and covariance with internal path length or treats the marginal leaf process. Neither supplies the leaf-transmission auxiliary and its exact mixed-moment closure in the inspected relevant text. The known leaf/internal-path-length covariance does not determine Wiener covariance since Wiener increments depend on all vertex transmissions, not just depth. Resultary and exact harmonic-form searches exposed different operand pairs, no equivalent formula. Foundational Neininger full text not available, retained priority risk.

## value

PASS

Leaf abundance and Wiener index capture genuinely different local branching versus global distance statistics in a canonical random-tree model. The exact finite-n covariance, sign transition, and nonzero limiting covariance with mean pairwise distance make a useful dependence invariant; the auxiliary transmission recurrence gives a reusable proof mechanism. This is not a routine marginal expectation nor a numerical finite table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
