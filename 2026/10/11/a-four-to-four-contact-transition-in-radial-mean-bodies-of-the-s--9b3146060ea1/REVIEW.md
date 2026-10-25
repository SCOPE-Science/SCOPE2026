# Mathematical review

## Correctness — PASS
For \(Q=[-1,1]^2\), the direction \(u\) reduces by square symmetry to \(q=\min(|u_1|,|u_2|)/\max(|u_1|,|u_2|)\in[0,1]\). The normalized ray covariogram is \((1-t/T)(1-qt/T)\) up to \(T=2\sqrt{1+q^2}\). Its Mellin moment converges for all \(p>-1\) and gives the stated exact radial profile, with the logarithmic continuous limit at \(p=0\). The log radial derivative factors as \(-(q-1)((p+1)q-1)/((1+q^2)(p+2-pq))\); this yields every minimum, and confines maxima to axes or diagonals. The strict monotonicity of \(\tfrac12\log 2-\log(1+p/2)/p\) proves that the maximum switches exactly at \(p=2\). Its slope is \((\log 2-1/2)/4>0\); there are precisely eight maximal directions at equality. Exact symbolic checks and regularized quadrature corroborate the equations; finite samples are not treated as infinite proofs.

## Originality — PASS, with narrow scope and priority risk
Langharst, Manui and Zvavitch (arXiv:2601.20117v2, §3.3, Proposition 34) **already give the general cube radial integral and exact axial and diagonal radii**. The square radial profile is a short specialization and integration of that published identity; those facts are not claimed as independently new. Langharst (arXiv:2603.14134v4) proves the negative-parameter convexity and general moment formula. Haddad's relevant polygon formula excludes opposite parallel sides, and Wang–Zhang's dual quermassintegral inequalities address different extrema. The inspected primary texts do not state the complete all-parameter square global directional contact classification, including the interior oblique minima and unique simultaneous eightfold outer contact. The short elementary deduction from the known cube formula substantially limits the contribution and is a live novelty/value boundary. The original 1998 Gardner–Zhang full text could not be inspected through authorized access; an older or unindexed equivalent square computation remains possible. The indexed identical record is not separate prior evidence.

## Mathematical value — PASS
The complete Euclidean inradius and circumradius contact diagram is a naturally motivated exact benchmark for the recently extended radial-mean operator, not an arbitrary isolated number. It distinguishes the negative-parameter region, the appearance of eight oblique shortest directions, and the sharp axis/diagonal longest-contact transition. Its merit is restricted to this canonical square and does not imply universal results for arbitrary convex bodies.

## Verification and limitations
The algebraic and numerical checks reproduce the moment normalization, derivative signs, boundary radii and crossing. They do not provide formal verification, external expert attestation or a blanket historical-priority guarantee. The analytic theorem covers all finite real \(p>-1\); the stated contact classification is Euclidean rather than affine-invariant.

## Primary references
- D. Langharst, A. Manui and A. Zvavitch, *On the Fourier Mean Bodies of a Convex Body*, arXiv:2601.20117v2, Proposition 34 and equations (72)–(73).
- D. Langharst, *Convexity of Radial Mean Bodies via an Extension of Ball's Bodies*, arXiv:2603.14134v4, Theorem 3 and Proposition 10.
- J. Haddad, *Planar radial mean bodies are convex*, arXiv:2412.01475v2.
- W. Wang and T. Zhang, *Inequalities for dual quermassintegrals of the radial p-th mean bodies*, J. Inequal. Appl. 2014:252.
- R. J. Gardner and G. Zhang, *Affine inequalities and radial mean bodies*, Amer. J. Math. 120 (1998), 505–528; original full text not inspected.
