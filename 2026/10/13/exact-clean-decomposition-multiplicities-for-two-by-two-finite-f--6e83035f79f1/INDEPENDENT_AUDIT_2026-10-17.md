# Independent mathematical audit

## correctness

PASS

Over any Fq, rank-one idempotents are ordered pairs of distinct rational lines (L,K), q(q+1) choices, plus 0 and I. For non-scalar A, det(A-E)=det A-tr A+tr(AE); with c=tr A-det A, fixed line L permits q bad complement projections if it is an eigenspace with eigenvalue c, zero if a different eigenvalue, or one if non-eigenline. Since det(A-cI)=det A*det(A-I), c is an eigenvalue precisely if A or A-I is singular. The number of bad rank-one idempotents is (q+1-e(A))+q epsilon(A), yielding c(A)=q²-1+e(A)-q epsilon(A)+u0+u1; scalar cases 1 for lambda0/1, otherwise q²+q+2. Exact field-uniform counting proof works in characteristic 2 and extensions. Independent full enumerations over F2,F3,F5 matched formula for all q^4 matrices and all q(q+1)+2 idempotents; distributions F2 {1:2,3:12,5:2}, F3 {1:2,7:28,8:24,10:18,11:8,14:1}, F5 {1:2,21:78,22:180,26:200,27:72,28:90,32:3}. Finite checks corroborate rather than establish arbitrary q.

## originality

PASS

The ring clean-index literature defines the maximum of the elementwise clean-idempotent counts and proves qualitative existence; that max does not recover a complete similarity-type pointwise multiplicity function. The Chen 2009 complete primary article gives matrix-cleanness criteria but not a count for every A in M2(Fq) in the inspected theorems. Schoonmaker 2018 dissertation abstract says it computes clean indices of M_n(Z/n), potentially including maxima for prime fields, but the full PDF gave HTTP 403, so potential elementwise formulas are a named priority risk. The submitted all-A full multiplicity profile is assessed original relative to accessible statements.

## value

PASS

The complete elementwise number of decompositions A=E+U is a natural enumerative invariant refining the clean index; it distinguishes scalar, eigenline and special eigenvalue strata in every finite field, including char2. The classification is self-contained and reusable for clean ring statistics, not merely a different label for matrix cleanness or a known ring-wide maximum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
