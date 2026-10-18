# Independent mathematical audit

## correctness

PASS

Original three-stage 3D Douglas–Rachford with commuting directional Laplacian lifts eliminates to R=I+3PxPyPz−PxPy−PxPz−PyPz. Entries according to 0,1,2,3 different coordinates have signs determined by 1+3abc−ab−ac−bc, p(3bc−b−c), pq(3c−1), and 3pqr respectively. Positive inverse offdiagonals and minimal endpoint diagonals d_n=D_{n−1}/D_n make each of the three 3d_i d_j≥d_i+d_j necessary and sufficient for n_i≥2 and Δt>0. Continuant D_n recurrence plus monotone resolvent gives cubic d_n≥2/3, unique τ_n↑(3−√6)/2 and τ_2=(√7−1)/6. An independently constructed exact 8×8 rational Kronecker step at s=7/25 yielded min entry −3241875/3189506048 and 24 negative entries. Infinite all-grid result rests on analytic entry classification, not this finite example.

## originality

PASS

The original 1956 three-dimensional Douglas–Rachford scheme and unconditional stability are established prior facts, but stability does not ensure positivity of every matrix entry. The exact pairwise resolvent-diagonal inequalities and finite-grid sharp thresholds appear absent from inspected modern positive-ADI records. The 1956 paper and 1962 follow-up were blocked in fresh authorized full-text retrieval (Oxford VPN disconnected), so originality is a qualified best-of-knowledge PASS with material historical risk, not a claim of complete original paper noncoverage.

## value

PASS

Monotonicity/positivity is a separate numerical-analysis property from the original Douglas–Rachford unconditional stability. Sharp all-rectangular-grid pairwise conditions, the finite-n cubic threshold curve, and an exact sign counterexample quantify when the original 1956 three-dimensional scheme violates discrete maximum principles. The claim is specific to the identified scheme and avoids claiming later ADI methods.

The dated certificate retains the supplied scientific assessment, sources and limitations.
