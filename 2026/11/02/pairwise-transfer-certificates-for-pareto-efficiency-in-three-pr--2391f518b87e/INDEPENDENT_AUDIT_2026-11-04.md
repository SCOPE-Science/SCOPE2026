# Independent mathematical audit

## correctness

PASS

For any n>=1 and x,p^(i) in the normalized 3-simplex, zero-sum triple residuals have L1=2 Linfty. Weak Pareto improvements are exactly the intersection of the simplex with the coordinate box L_j=max(0,max_i(p_ij-r_i)), U_j=min(1,min_i(p_ij+r_i)), r_i=||x-p^i||_infty. If any y strictly improves agent i, the at-most-two active residual coordinates move strictly toward p^i; select their donor/receiver (or one active and an opposite-sign coordinate) and take epsilon sufficiently small. The elementary transfer stays in the same box, strictly decreases i's radius and never worsens anyone. Reverse implication is immediate. Scanning 6 ordered project pairs and n active sets yields O(n) arithmetic operations. Independently re-evaluated the rational four-project counterexample: 5 ideals with x=(1/4)^4 and y=(6/25,13/50,13/50,6/25) give cost [3/10,1/5 x4] to [7/25,1/5 x4], yet each of 12 single directed transfers has a blocking agent. The frozen verify.py tests 49,927 rational grid situations; this finite test is corroboration, not the universal proof. Boundaries r_i=0 and x on simplex facets are handled by the closed box and small-epsilon choice.

## originality

PASS

Against Freeman–Pennock–Peters–Vaughan and Elkind–Greger–Lederer–Suksompong–Teh on L1 portioning, the evaluated iff certificate for arbitrary given three-project x and sharp 4-project obstruction are not stated in the inspected mechanism-based Pareto results. Existing sufficient Pareto guarantees for specific aggregation mechanisms are logically weaker than an iff test for every outcome. Best-of-knowledge, not proof of global priority.

## value

PASS

A linear-in-agent exact local Pareto-efficiency certificate for an arbitrary proposed three-project budget is a natural social-choice decision problem. The explicit four-project failure proves a genuine sharp dimension boundary, rather than parameter renaming or textbook sufficient condition; an O(n) test can be used independently of selection-mechanism design.

The dated certificate retains the supplied scientific assessment, sources and limitations.
