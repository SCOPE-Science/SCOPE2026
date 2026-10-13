# Scientific review

## Correctness — PASS
The four-dimensional support decomposition is exact: the antipodal rim pair occupies eigenvalue \(0\) antisymmetrically, eigenvalue \(-2\) symmetrically, and both eigenvalues of the explicit \(2\times2\) hub block symmetrically. Equality in the transition-amplitude norm forces the three specified phases. Trace and determinant identities yield a contradiction modulo four for every possible finite-time perfect transfer, independent of \(q\). For transcendental \(q\), algebraic independence of the two frequencies together with Kronecker density ensures simultaneous phase approximation. For rational \(q\), the trace phase enforces the odd-denominator obstruction; nonsquare discriminant supplies an irrational one-dimensional rotation sufficient for approximation. The periodic rational-eigenvalue case cannot support approximate but not exact transfer. `verify.py` independently replays finite matrix and phase cases. The proof does not claim to classify irrational algebraic inputs.

## Originality — PASS, with residual risk
*Irrational quantum walks* (arXiv:2208.08971) gives general exact spectral methods for integral Hamiltonians; fixed rational hub potentials can be reduced to this setting by clearing denominators, but that general decision procedure does not state the complete closed arithmetic family criterion. *Perfect state transfer on graphs with a potential* (arXiv:1611.02093) permits potentials at arbitrary vertices, and therefore does not cover the impossibility under one constrained hub control. *Pretty good fractional revival via magnetic fields* (arXiv:2311.18143) treats more general fractional revival after perturbing different vertex subsets; no exact hub-only wheel classification was found in the inspected results. The unperturbed negative five-vertex wheel case is known and expressly not claimed as novel. A differently indexed special case of a general perturbation theorem remains possible. Published-record and semantic claim checks showed no statement dominating the complete specified criterion.

## Value — PASS
The wheel is the smallest wheel with a pair of antipodal nonadjacent twins. Restricting control to one physically distinguished hub vertex produces a clear gap between exact and approximate controllability, even though unrestricted potentials can enable exact transfer. The arithmetic odd-denominator and discriminant conditions are an exact sharp classification for every rational hub strength, not isolated parameter examples; they expose a concrete barrier and construction for a natural minimalist quantum-transport model.

## Boundaries
All edges are unit-weight and only the hub has an onsite term. Irrational algebraic inputs are not classified, and no numerical scan certifies universality. Residual coverage risk is weakly indexed wheel-specific quantum transport under alternate terminology.

Self-review: passed. Independent audit: not yet performed.
