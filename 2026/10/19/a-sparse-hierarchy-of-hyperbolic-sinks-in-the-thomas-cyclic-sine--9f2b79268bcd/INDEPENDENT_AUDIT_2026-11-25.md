# Independent mathematical audit

## correctness

PASS

A synchronous equilibrium has b=sin u/u for u≠0. The cyclic Jacobian gives exactly the strict test −2b<cos u<b. By oddness only u>0 is needed. On a positive sine lobe, the derivative numerator of g(u)=sin u/u is u cos u−sin u, strictly decreasing because its derivative is −u sin u. Thus only the decreasing branch passes cos u<b; for k=0 the branch starts at the excluded u=0. After v_k, the second inequality holds precisely before the unique zero of tan u+u/2, which increases from −∞ to a positive value. Applying g to this branch yields (H_k,F_k); converting the root identities to threshold formulas gives the stated square roots. The endpoint inequalities 1+f_{k+1}²>4+h_k² give disjointness, so there is one positive sink at admissible b and its negative partner, with no endpoint sinks on these branches. Setting f=v−δ_F and h=v+δ_H gives δ_F=v⁻¹+O(v⁻³), δ_H=2v⁻¹+O(v⁻³) from the cotangent expansion. Inserting into the denominators gives F=v⁻¹+v⁻³/2+O(v⁻⁵), H=v⁻¹−4v⁻³+O(v⁻⁵), hence width (9/2)v⁻³+O(v⁻⁵). A partial window at ε contributes O(ε³), and the full-window tail starts at v=ε⁻¹+O(1) on a lattice of step 2π; integral comparison gives ∑v⁻³=ε²/(4π)+O(ε³) and ∑v⁻⁵=O(ε⁴), proving the measure formula for all sufficiently small ε. Independent bounded bisection on u cos u+2 sin u confirms H_0≈0.328990102242739 and H_1≈0.119910744243336. The frozen numerical script was inspected, not executed. Its crossing description refers to the right endpoint in u, which is the lower damping endpoint H_k, not F_k. No nonlinear endpoint or nonsynchronous stability claim is needed.

## originality

PASS

Repeated synchronous branch creation and stability loss are already documented, as are the synchronous scalar and spectral equations, the principal window, and the boundary mechanisms. The distinct supported result is the exact disjoint-window and sparsity theorem: an exhaustive full-space synchronous count and a sharp width and damping-parameter measure asymptotic. The substantive originality rests especially on the latter quantitative statements, not the existence of high-lobe stable branches or the Hopf condition.

## value

PASS

For this standard nonlinear flow, the exact count and disjointness distinguish an infinite sequence of locally stable synchronous branches from overlapping windows. The explicit leading measure and remainder quantify the scarcity of stable parameter values despite infinitely many windows. This is a parameter-level statement, not a claim about the basins or about other attractors.

The dated certificate retains the supplied scientific assessment, sources and limitations.
