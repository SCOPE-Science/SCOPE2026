# Independent mathematical audit

## correctness

PASS

The count uses substitutions of the full maximal-ideal-power quotient, not coordinatewise truncation. Any tuple from the maximal ideal defines a map; invertibility on the tangent space gives invertibility on all graded pieces. For an idempotent, choose coordinates u,w along the tangent image and kernel. The substitution u↦e(u), w↦w−e(w) is tangent-identity and intertwines the coordinate projection with e. Thus each image is a copy of the r-generator quotient and its literal tangent plane is well-defined. For a fixed plane U choose a coordinate retraction P onto its copy B0. On each candidate image B, P|B has invertible tangent map between equally sized truncated symmetric algebras, hence is an isomorphism. Its inverse picks unique lifts u_i+k_i with k_i in ker(P)∩m²; conversely every such tuple defines a section of P and the resulting image is a retract. This counts q^{r(H_d(n)−H_d(r))} per plane. Once B=B0 by conjugation, a retraction fixes its generators and freely assigns the n−r remaining generators to m∩B0, giving the stated fiber. The monomial count and Gaussian factor give the cardinality and total, including the augmentation and identity boundaries and d=2. Independent bounded replay: python3 /workspace/branches/independent_checks.py 4 enumerates all 1,024 substitutions for (n,d,q)=(2,3,2) with bitwise multiplication and groups literal image sets. It gives 12 eight-element images with fibers of four and one image each of sizes two and 64 with fibers of one. The frozen checker was inspected, not executed; this replay is finite corroboration.

## originality

PASS

Pass for the uniform formula at arbitrary truncation length, not for the d=3 formulas or for coordinate linearization. An earlier Resultary finding gives all three exact cube-zero counts, a material overlap not cited by the frozen record. Its quadratic idempotency computation does not extend by merely substituting H_d for a quadratic dimension: beyond cube-zero, nonlinear substitutions can act nontrivially on products of degree two, and the earlier linear equation in quadratic tails no longer describes idempotency. The arbitrary-order normalization and count supply that extension. The closest inspected formal/automorphism work does not give the general finite quantitative claim.

## value

PASS

An embedded retract and the number of ways to project onto it are natural invariants of this finite algebra. The all-order formula quantifies how the higher jets change the number of placements and the prescribed-image multiplicity separately, across all characteristics. This gives exact sizes for strata of the idempotent endomorphism monoid, more information than a total or abstract image isomorphism type. Value here is in the general higher-order count, not the known cube-zero or elementary square-zero example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
