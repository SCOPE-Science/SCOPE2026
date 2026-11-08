# Independent mathematical audit

## correctness

PASS

Exact utility calculations for all four directed A/B deviations give -min(x_i,y_j)<=x_i*y_j-y_i*x_j<=min(y_i,x_j) for all mixed blocks; all unmixed blocks have a zero-utility agent who can improve, and singleton moves cannot improve from mixed blocks. Cauchy-Schwarz gives W<=2ab/(a+b) with equality exactly at common type ratio a:b. If b=qa, residual integers y_i-q*x_i sum to zero and opposite-sign residuals violate the Nash determinant bound, forcing all block ratios (s,qs); those blocks are strict-core stable. If b=qa+r, 0<r<a, the (1,q)/(1,q+1) witness meets the determinant bounds, has exact positive gap 2r(a-r)/((q+1)(q+2)((q+1)a+r)), and a direct weak strict-core blocking coalition. The labeled exponential formula a!(qa)![z^a] exp(sum z^s/(s!(qs)!)) follows from unlabeled SET blocks. Actual code verification/checker.py independently computes utilities for all labeled partitions through ten agents (not an all-size proof).

## originality

PASS

PASS best-of-knowledge for sharp unilateral Nash arithmetic boundary and labeled count, excluding previously established strict-core characterization and welfare ratio inequality. Primary Nash and core literature establishes overlapping background but not the exact all-Nash divisibility iff statement in inspected material.

## value

PASS

A necessary and sufficient all-parameter arithmetic classification of when individual equilibrium, social optimum and strict core coincide; explicit family of nonoptimal Nash witnesses and exact equilibrium counts distinguish genuine equilibrium inefficiency from price-of-stability one. This is a natural complete classification, not merely a small computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
