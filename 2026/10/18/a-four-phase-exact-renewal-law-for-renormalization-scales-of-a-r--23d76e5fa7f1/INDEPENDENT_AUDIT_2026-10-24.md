# Independent mathematical audit

## correctness

PASS

The original full-branch inverse of the generalized Lüroth map has cylinder probability q^{|i|+1}, so the digit exponents are iid with P(X=1)=q and P(X=j)=2q^j (j>=2). A complete renormalization pairs two digits; its multiplier is q^{Z} and W(z)=[qz(1+qz)/(1-qz)]^2. The renewal identity U(z)=1/(1-W(z)) has partial fractions 1/[4(1-z)]+1/[4(1+q^2 z)]+(1-qz)/[2(1+q^2 z^2)], giving exact u_m and the four residue-class asymptotics. The overshoot first-crossing convolution P(H_m=k)=sum_{j=1}^m u_{m-j} w_{j+k} yields the stated F_k and, by dominated convergence plus EZ=4, the normalized limiting mass (1/4)P(Z>=k+1). Independent floating-point renewal convolutions matched the exact hit expression at m=0..40 to 2.4e-15, and normalized overshoot distributions at seven thresholds with exact P(H=0)=u_m, P(H=1)=u_{m+1}. Proof extends to arbitrary m; numerical testing alone does not.

## originality

PASS

Best-of-knowledge originality is assigned to the exact strengthened/specialized claim, not to previously published premises: Theorem 1(iii) of Lowenstein–Vivaldi gives q^{|i|+|j|+2}; paired full-branch measures allow but do not already evaluate all u_m. Standard renewal recurrence structurally implies U=1/(1-W), so the leading 1/4 limit is not credited as a new general theorem; the evaluated poles, four-phase correction and F_k do require explicit new specialization. Targeted Resultary searches and primary-paper comparisons were performed; unsuccessful searches are not priority proof. The generic renewal theorem gives u_m->1/EZ=1/4 after identification of W; it does not state the oscillating correction or full finite-m generating functions. Exact overshoot renewal identities in generic theory are algorithmic antecedents, not a table of this evaluated special-family distribution.

## value

PASS

An intrinsic geometric question for renormalizable piecewise isometries asks whether a particular lattice scale occurs at any complete induction and by how much first passage jumps past it. The exact four-phase correction and full family of overshoot generating functions provide more precise parameter-space information than mere self-similarity or the generic renewal limit. The specific finite-scale distribution is a natural exact invariant, even though ordinary renewal machinery provides a conceptual framework.

The dated certificate retains the supplied scientific assessment, sources and limitations.
