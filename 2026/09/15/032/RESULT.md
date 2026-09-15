# Tensor-diagonal refutation of amalgamated-Avitzour necessity over M2

## Context

The admitted target asks for necessary and sufficient simplicity and unique-trace conditions for reduced amalgamated free products of finite-dimensional C*-algebras over a finite-dimensional subalgebra D with dim D >= 2, and in particular whether simplicity is equivalent to the conjunction of (i) absence of a Dykema-type exceptional summand/character obstruction from trace weights and (ii) an amalgamated Avitzour kernel-unitary condition. The finding answers the necessity direction negatively inside the target domain.

## Definitions

Let D = M2(C) with normalized trace tau_D. Let B1 = C^3 with faithful trace weights lambda = (0.6, 0.2, 0.2) and B2 = C^5 with uniform weights mu = (0.2,...,0.2). Put A1 = D tensor B1 ~= M2^{oplus 3}, A2 = D tensor B2 ~= M2^{oplus 5}, with product traces tau_i = tau_D tensor tau_{Bi}, unital diagonal inclusions iota_i(d) = d tensor 1, and tau-preserving conditional expectations E_i = id tensor tau_{Bi} : A_i -> D tensor 1. Let (A, E) = (A1, E1) *_D (A2, E2) be the reduced amalgamated free product and tau = tau_D o E. An amalgamated Avitzour hypothesis means existence of unitaries u_i in A_i with E_i(u_i) = 0 (plus further orthogonality); it fails if either side has no kernel unitary at all.

## Result

For the above data, which satisfy dim D = 4 >= 2, faithful compatible traces, and strict finite-dimensional unital inclusions: (a) ker E1 contains no unitary; (b) all Dykema-type pairwise trace sums are strictly below 1 (maximum 0.8 on central minimal projections, 0.4 on rank-one minimal projections); (c) A ~= M2 tensor B trace-preservingly where (B, phi) = (B1, tau_{B1}) * (B2, tau_{B2}) is the scalar reduced free product, hence A is simple with unique tracial state tau. Consequently simplicity plus unique trace does not imply the amalgamated Avitzour condition even under the Dykema pairwise condition; the conjunction (i)+(ii) is sufficient but not necessary.

## Proof / evidence

No unitary in ker E1: a unitary u = (U1, U2, U3) in M2^3 satisfies E1(u) = 0.6 U1 + 0.2 U2 + 0.2 U3, and ||0.6 U1|| = 0.6 > 0.4 >= ||0.2 U2 + 0.2 U3||, so ||E1(u)|| >= 0.2 > 0. Pairwise sums: central weights give max 0.6 + 0.2 = 0.8 < 1; rank-one projections (trace 1/2 on M2 factor) give max 0.3 + 0.1 = 0.4 < 1. Splitting lemma: ker E_i = D tensor ker tau_{Bi}; with tilde{A} = D tensor B and tilde{E} = id tensor phi, alternating D-words expand entrywise into scalar alternating words of phi-mean zero, the copies generate tilde{A}, and the universal property of the reduced amalgamated product (Voiculescu; Blanchard-Dykema) gives (tilde{A}, tilde{E}) ~= (A, E). Scalar factor: Dykema Theorem 1 (funct-an/9702015) applies to B since dim B1 = 3, dim B2 = 5 with L+ = L0 = empty, so B is simple with unique trace phi. Lift: a nonzero ideal of M2 tensor B compresses by a matrix unit to a nonzero ideal of B, giving simplicity; any trace sigma satisfies sigma(x tensor b) = tr_2(x) sigma(1 tensor b) since x -> sigma(x tensor b) is a tracial functional on M2, so sigma = tr_2 tensor psi with psi = phi. Numerics in output/artifacts/check_candidate.py print ALL CHECKS PASSED.

## Limitations

Refutes necessity of the (i)+(ii) conjunction only; no replacement necessary-and-sufficient criterion over arbitrary Bratteli multiplicities or non-tensor embeddings is claimed. Exact ideal lattice and trace simplex outside the tensor-diagonal subfamily remain open. D is noncentral here, unlike abelian-diagonal models where D stays central and simplicity is impossible.

## Reproducibility

Run python3 output/artifacts/check_candidate.py. Verify Dykema Theorem 1 in funct-an/9702015 and the amalgamated construction in Blanchard-Dykema / Voiculescu; check the norm gap, pair sums, and splitting computation in DRAFT sections 3-6.

## References

K. Dykema, Simplicity and stable rank of some free product C*-algebras, funct-an/9702015, Theorem 1 and Section 3. K. McClanahan, Simplicity of reduced amalgamated products of C*-algebras, Canad. J. Math. 46 (1994). N. Ivanov, On the structure of some reduced amalgamated free product C*-algebras, arXiv:0705.3919. Blanchard-Dykema, Embeddings of reduced free products of operator algebras.
