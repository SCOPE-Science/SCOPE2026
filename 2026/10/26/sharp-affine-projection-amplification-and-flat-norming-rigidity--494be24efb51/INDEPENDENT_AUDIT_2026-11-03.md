# Independent mathematical audit

## correctness

PASS

For fixed p∈(2,∞) and normalized volume measure, beta/gamma integration yields coordinate variance s²=[Γ(3/p)/Γ(1/p)]Γ(1+d/p)/Γ(1+(d+2)/p), so the exact affine projector kernel is 1+<a,y>/s². With independent generalized Gaussians Gi (density p e^{-|t|^p}/(2Γ(1/p))) and Exp(1) E, X=G/(Σ|Gi|^p+E)^{1/p} is exactly uniform. Gamma ratios give d^{1/p}s→b_p=p^{1/p}√(Γ(3/p)/Γ(1/p)); the radial multiplier Q_d=v_p/[s(Σ|Gi|^p+E)^{1/p}]→1 in probability. For R=d^{1/p−1/2}||a||₂≥η, max_i|a_i|/||a||₂≤1/(η d^{1/2−1/p}) and the Lyapunov ratio of Σa_iGi is O(d^{−1/2+1/p}), uniformly along arbitrary sequences; Slutsky and exact unit variance imply convergence of E|<a,X>/(s||a||₂)| to √(2/π). For R<η, Cauchy–Schwarz bounds the normalized row by O(η)+d^{-1/2}. Hence sup_a|Λ(a)/√d−c_p R(a)|→0 and sup norm/√d→c_p. Hölder gives R≤1 with flat boundary sign vectors saturating. Near norming iff R→1; with yi=(d^{1/p}|a_i|)^p and θ=2/p<1, mean yi≤1 and mean yi^θ→1 force the nonnegative strict concavity defect 1+θ(yi−1)−yi^θ to have mean→0. Its linear tail and unique zero at 1 imply mean|yi−1|→0; |yi^{1/p}−1|^p≤|yi−1| yields normalized p-mean flatness. Converse follows by Hölder/triangle inequality. Independent 25,000-draw gamma-volume computations for p=3,4,6 and d=32,128 corroborated profiles for flat and axis rows; exact p=2 variance checked for d=1,2,3,10,50. This numerical sampling alone does not prove the uniform theorem. Dimension d=1, a=0, flat signs, and sequential order of p endpoint limits are compatible; no finite-d exact optimizer or p-uniformity is established.

## originality

PASS

Best-of-knowledge originality belongs to the exact fixed-finite-p>2 sharp gamma coefficient, uniform-in-evaluation-point Lebesgue-function profile and iff normalized-p-mean flatness of all asymptotic norming sequences. Barthe–Guédon–Mendelson–Naor 2005 Theorem 1 supplies the normalized-volume representation itself; its Theorem 7 identifies best Khintchine constants only up to universal multiplicative factors (explicitly stated immediately before theorem), not the claimed leading coefficient and iff rigidity. Figueroa 2016 Theorem 1.1 is a degree-growing weighted Sobolev error estimate on a Euclidean ball. Defant et al. arXiv:2405.12123v4/published 2026 concern minimal projections and L1 Jacobi kernels on Euclidean spheres; their real-Hilbert formula (5) does not cover finite-p>2 volume balls. Xu 2001/2002 concerns polynomial-degree Lebesgue growth on weighted Euclidean balls. Three new Resultary semantic searches and targeted current literature found no stronger implication. Sündermann 1984 potentially concerns unit-ball projection constants but its text remained inaccessible after an arXiv/legitimate OA search and an institutional attempt that returned vpn_disconnected. This is a qualified priority assessment, not proof of uniqueness.

## value

PASS

The L∞ norm of the L²-affine projection is a canonical stability/amplification invariant for least-squares approximation on volume-uniform high-dimensional convex bodies. A complete sharp dimension-growth coefficient for each fixed finite superquadratic p and the *uniform* Lebesgue-function profile distinguish flat boundary directions from sparse/partially supported ones. The iff coordinate-flatness criterion classifies all asymptotic norming sequences, a natural structural strengthening not supplied by the earlier up-to-universal-factor moment bounds. It is an exact family-wide asymptotic geometry theorem, not a textbook substitution or a single arbitrary computation. Future high-dimensional approximation work can use its precise constants and sharp worst-point character. Scope is deliberately limited to degree 1, p>2 fixed, normalized uniform volume and real L∞ endpoints.

The dated certificate retains the supplied scientific assessment, sources and limitations.
