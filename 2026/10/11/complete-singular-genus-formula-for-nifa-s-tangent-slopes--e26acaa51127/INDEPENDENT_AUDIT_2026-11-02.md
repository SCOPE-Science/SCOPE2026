# Independent mathematical audit

## correctness

PASS

At pinned RESULT.md the claim is: for N>=2 and all m not zero, write M=|m|=Na+r, 0<=r<N, and cl_Gamma_N(lambda^m)=1+ceil(a(N-1)/2) for r=0, otherwise 1+ceil((a(N-1)+r-1)/2), equivalently 1+floor((1+M(N-1)/N)/2), with cl(1)=0. Nifa Proposition 2.3 establishes the exact quotient and peripheral map. Reconstruct rho_N(lambda)=Q R_{pi(1-1/N)} Q^-1 using h= a^2=b^3 and mu=b^-1 a; its Mth power is conjugate to translation by e=M(N-1)/N. EHN strict criterion requires e<2g-1, so the least admissible g is exactly the floor formula. Upper bound: r=0 is Nifa Theorem 6.5; r>0 choose D=M boundary permutation C of cycle type N^a r, parity A=D-(a+1), and epsilon=A mod2, P0 identity/transposition. (CP0)^-1 even equals UV with U,V D-cycles (Bertram, plus all low degrees checked), so choose A0=U, B0 with [A0,B0] C P0=1. This transitive monodromy defines a connected D-fold cover of the two-boundary torus capped with epsilon simple branching; it has a+1 boundary components and Euler characteristic -D-epsilon, giving g=1+ceil((D-(a+1))/2). Centrality z=lambda^N makes the boundary product a conjugate of z^a lambda^r=lambda^M, yielding an actual g-commutator expression. M=1 has genus 1, M=0 is the identity, and inversion handles m<0. The peripheral loop b lambda_j+q s_j maps to lambda^{b-Nq}; singular genus equals cl by Nifa Lemma 6.6 and Liu--Ni--Sun--Wang Remark 3.3. The restriction gcd(N,6j-1)=1 is required for the related core torus to be in S^4, not for the group identity.

## originality

PASS

The result provides exact ordinary (unstable) commutator lengths of all powers lambda^m, hence singular genus for every primitive tangent slope. In the full primary 2026 Nifa preprint, Theorem 6.5 proves only the N-divisible exponents (powers of z=lambda^N) while Remark 6.8 explicitly declines the other slopes. The 2013 Liu--Ni--Sun--Wang paper provides the genus/commutator interpretation, not this family. The prior stable formula cannot determine integer rounding/residue corrections. Resultary semantic searches returned the same October 11 published finding but no distinct stronger published SCOPE record. Best-of-knowledge PASS with indexing/priority risks, not a universal novelty certificate.

## value

PASS

The group and invariant arise from a natural geometric family of knotted tori with common exterior, not an arbitrary parameter slice. For primitive tangent slopes (b,q) with gcd=1, every m=b-Nq can occur (e.g., q=1, b=m+N), so exact cl(lambda^m) gives the complete singular-genus classification. Nifa explicitly left these nondivisible slopes without formula in Remark 6.8. The new integer correction distinguishes unstable genus from homogenized seminorm and can be used to compare exact slope bounds for this family. This is a motivated complete classification of a natural invariant; it does not require a novel four-manifold family or a general commutator theorem to be valuable.

The dated certificate retains the supplied scientific assessment, sources and limitations.
