# Independent mathematical audit

## correctness

PASS

Over F2, the k-subset permutation module is exterior-degree k, with adjacency A=wedge_u contraction_i plus kI. Even k and n imply A^2=0; decomposition along a distinguished vector with contraction_i=1 gives rank r=binom(n-2,k-1). For deleted adjacent k-subsets u,v, U=span(e_u,e_v,Ae_u,Ae_v) is four-dimensional, since A e_u and A e_v have supports outside u,v and can be separated. B e_u=Ae_u+e_v, B e_v=Ae_v+e_u, B(Ae_u)=e_u and B(Ae_v)=e_v. From this explicit 4x4 action, B^3 swaps each paired coordinate, B^6 fixes all of U, only zero is fixed, and B^3 has exactly four fixed vectors, giving one 3-cycle and two 6-cycles. The rank-two edge term makes B²=AE+EA+E² with image exactly U. The preimage count is 2^{N-(r+2)} per attractor state for one more step, giving exact cumulative totals. Independent GF2 adjacency and orbit assertions reproduce six n,k instances and exhaustive populations for N<=15; universal formulas come from the algebra, not those samples.

## originality

PASS

Peeters 2002 Section 4.1 gives the unmodified Johnson graph binary rank rk_2(J(n,k)+kI)=binom(n-2,k-1) for even n and other modular ranks; this known prerequisite is not novel. His paper does not discuss deleting one edge, synchronous finite-state parity dynamics, the 4-dimensional invariant block after perturbation, periods 3 and 6, or the exact transient census. The unperturbed rank plus explicit independent edge-update analysis are necessary new implications. Resultary related Johnson graph and parity dynamics concern other adjacency graphs and orbit problems.

## value

PASS

A single missing edge converts a nilpotent synchronous XOR network into a uniform finite recurrent attractor with genuinely new primitive three- and six-cycles for an infinite graph family. Exact one- versus two-step basin sizes measure a sharp robustness failure; the claim is not simply unperturbed rank recomputation. This has a direct motivation as fault response of linear network dynamics and a concise structural answer.

The dated certificate retains the supplied scientific assessment, sources and limitations.
