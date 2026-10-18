# Independent mathematical audit

## correctness

PASS

For SPD quadratic and exact line search, source SRMIL/SMRMIL coefficient reduces to β_{k+1}=g_{k+1}·(g_{k+1}−g_k)/||d_k||² and spectral factor becomes one. Exact orthogonality yields β1=||g1||²/||g0||² and d0ᵀAd1=0. Under g1,g2 !=0, the first conjugacy and search conditions force g2⊥g1, giving β2=||g2||²/||d1||², α1 d1ᵀAd1=||g1||², g2ᵀAd1=||g2||²/α1; substituting gives d2ᵀAd1=(d1ᵀAd1)||g2||²(1/||d1||²−1/||g1||²)<0 because ||d1||²=||g1||²+β1²||d0||²>||g1||². In dimensions 1,2 first 1,2 conjugate directions suffice. Independent SymPy exact SPD A=diag(1,2,3), x0=(1,1,1) gave alphas 7/18,342/581,9764867/13418142, defect −38/4067 and nonzero g3=(32871,52536,−45981)/9769349. The witness proves failure of dimension-step termination, not universal divergence.

## originality

PASS

PASS best-of-knowledge: foundational SRMIL/SMRMIL paper states exact-search coefficient coincidence and descent but the inspected text does not state the universal strictly negative third-direction A-conjugacy formula or minimal dimension three with exact finite-termination counterexample. Older CG conjugacy theory is comparator, not this coefficient result; recent revised spectral conjugacy papers motivate a different method rather than logically implying the sign-defect identity.

## value

PASS

PASS: a structural theorem about when a proposed nonlinear CG variant stops preserving quadratic conjugacy, sharp onset at the third direction and smallest failing dimension, plus a fully exact counterexample. This specifically determines a rigorous boundary of classical finite-step termination and helps interpret algorithmic assertions, without confusing loss of conjugacy with practical nonconvergence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
