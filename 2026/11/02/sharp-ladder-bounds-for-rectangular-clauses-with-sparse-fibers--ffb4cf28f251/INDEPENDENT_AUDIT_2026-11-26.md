# Independent mathematical audit

## correctness

PASS

In a selected triangular incidence matrix, a nonempty rectangle has last row a at most its first column b, and enlarging it to the canonical cut at any c in [a,b] adds no false cells. The uncovered right-neighbors of the first row of each cut-free gap include all columns in that gap, forcing length at most s. With k distinct cuts this gives t<=k+(k+1)s<=r+(r+1)s. Conversely periodic cuts starting at index s leave at most s successive columns uncovered in each row, giving the asserted minimum at every t. On the real line the rectangle clauses and the s translates y=x+h realize the full extremal triangle on consecutive integer points and never introduce a selected lower-triangle cell. Equality forces k=r and all gaps length s for every allowed cut choice; changing one rectangle's cut alone would either change that unique cut set or cause a duplicate, so both endpoint indices of the rectangle equal its forced cut. The empty construction at r=s=0, and the separate r=0 and s=0 limits, agree with the formulas.

## originality

PASS

The checked antecedents include the zero-residual biclique-cover endpoint and qualitative semilinear stability. They do not cover the positive left-residual budget and equality rigidity. No novelty is credited to Boolean rank of the triangular matrix or to qualitative closure of stable relations.

## value

PASS

The theorem quantifies how many rectangular clauses are needed to create an order pattern when each left point can have a bounded number of exceptional incidences. Exact periodic placement and rigidity turn a qualitative stability observation into a sharp constraint on all extremal witnesses; the bound is realized within a simple semilinear class as well as on finite matrices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
