# Independent mathematical audit

## correctness

PASS

For nonzero A, U=im A has dimension r and AB maps into U. If the restriction to U has a vanishing kth power then (AB)^(k+1)=0, and nilpotency of AB conversely implies nilpotency of the restriction. The restriction map on B is onto End(U): compose a prescribed endomorphism with a linear section of A and extend from U. Every fiber has cardinality q^(n^2-r^2). The Fine–Herstein count used here can also be reconstructed: let N_j count nilpotents and G_j=|GL_j(F_q)|, with N_0=G_0=1. Each endomorphism in dimension r has a unique Fitting decomposition as direct sum of a nilpotent and an invertible part. Counting decompositions with nilpotent dimension j gives G_r N_j/G_j endomorphisms, so q^(r^2)/G_r=sum_{j=0}^r N_j/G_j. Subtract dimension r-1 and use q^(r^2)/G_r=product_{i=1}^r (1-q^(-i))^(-1), giving N_r=q^(r^2-r). Thus there are q^(n^2-r) product partners before deleting zero and the self-partner exactly when A is nilpotent. The symmetric relation follows from (BA)^(k+1)=B(AB)^k A. Residues of the two degree types differ modulo q since n>=2; each type then determines the rank. The gaps of the powers exceed one, so the maximum is precisely rank-one nonnilpotent and the minimum precisely rank n (which is never nilpotent). `python3 /workspace/reviews/reproduce.py 1` independently exhausts the n=2 graph over the non-prime field F4 using trace and determinant; 60 rank-one nonnilpotents have degree 63, 15 rank-one nilpotents degree 62, and 180 invertibles degree 15. The frozen prime-field verifier was inspected, not executed.

## originality

PASS

Pass is for the all-rank, loopless-graph degree classification and inverse conclusion. The known total nilpotent-matrix count, the defining graph, and the previously computed rank-one values are not distinct contributions. The nearest catalogued formula is for zero products, with a different graph and type.

## value

PASS

This is a uniform local invariant of a standard matrix-ring graph. Recovering both rank and nilpotency from the degree, not merely exhibiting unequal degrees, separates all realized vertex types across all field sizes. The compression handles every singular rank and exposes why the only dependence on nilpotency type comes from removing the loop. This is more than recomputing the known rank-one witnesses.

The dated certificate retains the supplied scientific assessment, sources and limitations.
