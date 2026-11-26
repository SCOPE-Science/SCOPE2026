# Independent mathematical audit

## correctness

PASS

The frame condition is total mass one and three vanishing moments in directions s,t,s-t; no scaling by the column norm is needed in these equations. On the displayed four-node support each direction sees the three noncentral residues 0,a,-a once each, so the stated positive weights cancel precisely when p/3<a<2p/3. A square three-column weighted Parseval synthesis matrix must be unitary, making its weights 1/3; the cyclotomic argument then excludes it since an integral coefficient vector with sum 3 cannot be constant over p coordinates. Smaller supports fail rank. For rational weights the same minimal polynomial forces each of the three marginal mass vectors to be identically 1/p. First-coordinate marginals force at least p nodes, and at equality force one node and weight 1/p per first coordinate; the other two conditions are exactly the two permutation tests. The example f(t)=2t satisfies both. For the count, the allowed integers number floor((p+1)/3) by considering p modulo 3. Even the unweighted support determines its translation center by summing the four frequencies and dividing by 4 in the field; the horizontal satellite recovers a. The canonical absolute weight difference is (1-h)/(1+h). An independent script checked exact formal moment cancellation and distinct translated supports at six primes and tested the p=5,7 complete-mapping graphs by exact residue counts: python3 /workspace/branches/exact_review_checks.py 2. The frozen floating-point checker and its output were inspected, not executed; neither finite check is the all-primes proof.

## originality

PASS

No full equivalent or covering result was substantiated by the inspected sources. The supported distinction is the exact four versus p optima on this triangle, with explicit four-node rules and the characterization of rational minimizers. Cyclotomic marginal uniformity, complete mappings as a combinatorial object, and the general positive-cubature framework are not claimed new. The closest same-geometry zero-set theorem gives an obstruction for noncollinear three-atom support but does not settle four-node existence or the large-support rational equality classification.

## value

PASS

This is a sharp distinction between two natural exact sampling models on the smallest noncollinear spatial set. The same three moment constraints allow four positive real weights but force at least p rational-weight nodes, yielding an unbounded exact support penalty even as the real construction's weights become nearly uniform. The equality characterization links the rational problem to a standard combinatorial class and explains substantially more than a lower bound or isolated numerical example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
