# Self-review
## Correctness
PASS. The exact qubit calculation reconstructs every hypothesis and normalization. The Bloch vector and rotation axis are unit, their cross product gives the stated pool Jacobian, the exact imaginary-time velocity formula gives \(v=(0,-1)^{\mathsf T}\), and the normal equations give \(s_E=1/(5+14\lambda)>0\) for every \(\lambda\ge0\). Independently, \(H^2=2I\) and \(\operatorname{Var}(H)=1/2\), so exact imaginary time has energy derivative \(-1\). The one-term argument covers arbitrary parameter dimension and both regularized and unregularized least squares.

## Originality
PASS. The inspected VIME source defines the descent check and reports energy increase when continuing after failure, but it does not state an exact noise-free minimal example or the one-term/two-term boundary. The original OVQITE source requires the Hamiltonian to lie in the selected operator span and does not state the exact two-term construction or the one-term minimality boundary. Semantic searches over the published prior-result corpus returned no implication-equivalent claim; the closest optimization result concerns weak Gauss–Newton frame dependence and is scientifically distinct.

## Value
PASS. The result separates an intrinsic geometric failure of termwise operator projection from surrogate truncation, sampling noise, and inaccurate linear solves. It also proves the smallest term count at which strict uphill motion can occur, explaining why a descent safeguard can be necessary even in perfect arithmetic and the sharp one-term/two-term boundary for exact local energy ascent.

## Closest literature and limitations
The closest source is arXiv:2610.01954v1, especially its OVQITE review and Appendix A.7 descent test. arXiv:2409.12018v1 is the original OVQITE reference and supplies the single-observable comparison. The claim is local; it does not assert typicality, a molecular failure mode, or any problem with accepted Armijo steps. A contemporaneous equivalent observation remains a residual novelty risk because the anchor is very recent.

Self-review: passed. Independent audit: not yet performed.
