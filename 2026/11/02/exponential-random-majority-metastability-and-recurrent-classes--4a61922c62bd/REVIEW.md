# Independent mathematical audit

## correctness

PASS

RESULT.md lines 16–30: each branch has four vertices at distances 1, 2, 3, 3 from the hub, so the tree has 1+s+4k vertices and diameter six for k≥2. The anchor triple stays white by induction, without pinning. With s=k−1, the blue hub and hub leaves keep their colors for one step in U, and U is left exactly when all k fresh ties are white. The constant one-step hazard gives the claimed geometric law, starting with the stated coloring in U. Three consecutive all-white floating updates have conditional probability at least 2^(−3k) from any anchored state: the first forces the hub white at the second update, and the second and third ensure the hub, hub leaves and floats are white at the third. This works even with arbitrary initial hub-leaf colors. Consequently all-white is the only accessible closed class, its mean hitting time is at least the mean exit time and at most 3·2^(3k). With s=k+1 the blue leaves win even against all k white floats, so the hub and leaves stay blue, and the product of independent fair ties gives the entire closed class and its uniform law. The two state counts refer to separate graphs.

## originality

PASS

The supported distinction is the pair of explicit diameter-six witnesses, including the exact geometric exit law and one-step-uniform exponential class under independent fair ties. General exponential stabilization and recurrent-class size under random majority are prior art. Bounded source and catalogue comparisons did not establish coverage of the tree-specific claim.

## value

PASS

Acyclicity and bounded diameter are natural candidates for suppressing the known general-graph behavior. These are exact counterexamples to both restrictions under the same rule, with a useful two-leaf change and controlled stochastic transition laws. They are not bounded-degree examples, typical-initial-state claims, or minimality theorems.

The dated certificate retains the supplied scientific assessment, sources and limitations.
