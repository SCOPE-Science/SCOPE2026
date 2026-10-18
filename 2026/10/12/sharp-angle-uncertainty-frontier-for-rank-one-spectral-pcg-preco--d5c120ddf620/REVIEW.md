# Independent mathematical audit

## correctness

PASS

Normalize A=diag(1,r) with 0<r<1. For F_q=I+(q-1)vv^T and t=1-|u_L^Tv|^2, determinant of symmetrically preconditioned B=F_q^(1/2) A F_q^(1/2) is rq and trace is q+r+(1-q)(1-r)t. Exact first steepest-descent/PCG energy contraction maximized over error weights gives the tight Kantorovich factor 1-4 det(B)/tr(B)^2, achieved by endpoint spectral weights in inverse eigenvalue ratio. The trace as a function of t puts worst t at T for q<=1 and t=0 for q>=1; on q<=1 derivative of q/(a_T q+b_T)^2 has sole stationary q=b_T/a_T<1 iff T<1/2. For q>=1, q/(q+r)^2 strictly decreases, giving unique q=1 for T>=1/2. Algebraic substitution gives Q_star and q=r nominal threshold sqrt(r)/(1+sqrt(r))^2; small-curvature T=cr limit c/(1+c) holds. Independently checked rational case r=1/4, T=1/5: q_star=8/17, Q_star=9/34. The original verifier includes matrix eigenproblem and worst-case errors; its finite tests are supplementary.

## originality

PASS

Best-of-knowledge new content is the exact angle-uncertainty robust minimax design for a rank-one spectral multiplier and the two distinct sharp thresholds. Known Kantorovich one-step factor and exact spectral preconditioner construction are prior ingredients, not claimed as novel.

## value

PASS

The closed-form unique robust multiplier explicitly identifies when approximate eigendirection information helps, a sharp 45-degree do-not-correct boundary, and a different fourth-root nominal-safety threshold. These are motivated design facts for a canonical two-mode spectral preconditioning problem, not merely a repackaging of the Kantorovich inequality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
