# Explicit fork-inequality distortion threshold for iterated Laakso graphs into 2-uniformly convex targets

## Context
Quantitative Ribe theory asks which finite metric families separate L_p-type (1<p<2) from power-type-2 uniform convexity (Hilbert, L_q q>=2). Iterated Laakso graphs with fork/Markov inequalities are the standard objects and method. Nearest prior work is qualitative/asymptotic (Mendel-Naor Markov convexity; Baudier-Gartland fork theory; Baudier et al. diamonds) except Dilworth-Kutzarova-Stankov (arXiv:2203.08229), which proves L_2->L_1[0,1] >= 9/8 via negative-type weights; its Remark 14 transfers only to the squared-Hilbert snowflake (ell_2,||.||_2^2), not standard bi-Lipschitz distortion into ell_2.

## Definitions
- L_0 = one edge; L_{k+1} replaces every edge of L_k by the 6-vertex cell L_1 with vertices A,T,L,R,B,U and edges {A,T},{T,L},{T,R},{L,B},{R,B},{B,U}, unit length, shortest-path metric. |V(L_k)|=2+4(6^k-1)/5, |E(L_k)|=6^k, diam(L_1)=4, d(A,U)=4^k at top scale (so D_j=4^j).
- L_1 fork table (verified): d(A,U)=4, d(L,R)=2, d(T,B)=2; full 6x6 matrix: A:[0,4,1,2,2,3], U:[4,0,3,2,2,1], T:[1,3,0,1,1,2], L:[2,2,1,0,2,1], R:[2,2,1,2,0,1], B:[3,1,2,1,1,0] in order (A,U,T,L,R,B).
- Distortion dist(f)=Lip(f)Lip(f^{-1}) after optimal scaling; normalized to ||f(x)-f(y)||<=d(x,y) with lower constant 1/D, so dist(f)=D.
- Y 2-uniformly convex in squared form: ||(x+y)/2||^2 + c_Y||x-y||^2 <= (||x||^2+||y||^2)/2 for some c_Y>0. Hilbert/ell_2: c_Y=1/4 exact (parallelogram/Apollonius).

## Result
Fix 1<p<2 (e.g. p=3/2, exponent 1/p-1/2=1/6). Let Y be 2-uniformly convex in squared form with constant c_Y>0 (Hilbert/ell_2: c_Y=1/4). Then every bi-Lipschitz f:L_k->Y satisfies

D^2 >= 1 + 2 c_Y k, and for Hilbert/ell_2 D^2 >= 1 + k/2 exactly,

hence for every fixed 1<p<2, D >= sqrt(2 c_Y) k^{1/p-1/2} (Hilbert: D >= 2^{-1/2} k^{1/p-1/2}; p=3/2: D >= k^{1/6}/sqrt(2)). The target's tightness-counterexample alternative (a level-k embedding beating k^{1/p-1/2}) is ruled out uniformly.

## Proof / evidence
1. Fork inequality (single analytic input): squared 2-UC form above; Hilbert equality at c_Y=1/4. With x=t-l, y=t-r, m=(l+r)/2: ||t-m||^2 <= (||t-l||^2+||t-r||^2)/2 - c_Y||l-r||^2.
2. Quadrilateral (Hilbert exact): for fork images t,l,r,b, m=(l+r)/2, s=||l-r||^2: ||t-b||^2 <= ||t-l||^2+||t-r||^2+||b-l||^2+||b-r||^2 - s, via summed Apollonius. Randomized checks pass.
3. Per-block drop: write a-u=(a-t)+(t-m)+(m-b)+(b-u), apply ||sum_4||^2<=4sum||.||^2 with Apollonius for ||t-m||^2, ||m-b||^2. With subcell scale L, e(C)=||a-u||^2/(16L^2), ebar=(2eY+sum eS+2eZ)/8 (weights (2,1,1,1,1,2)/8): e(C)<=ebar-s/(8L^2); general 2-UC: e(C)<=ebar-c_Y s/(2L^2). Verified on 3000 random trials.
4. Gluing induction: scale-j blocks (D_j=4^j) partition into six scale-(j-1) subcells; hierarchical weights omega_child=omega_parent*w_pos preserve total weight. Branch separation s_C>= (2D_{j-1}/D)^2 (branch distance 2D_{j-1}). Hence W_j<=W_{j-1}-1/(2D^2) (Hilbert), general drop 2c_Y/D^2. Leaf average W_0<=1, top W_k>=1/D^2 give 1/D^2<=1-k/(2D^2), i.e. D^2>=1+k/2 (general 1+2c_Y k).
5. Exponent reduction: sqrt(1+k/2)>=sqrt(k/2)>=k^{1/p-1/2}/sqrt2 for k>=1 since 1/2-(1/p-1/2)=1-1/p>0. General: sqrt(2c_Y k)>=sqrt(2c_Y)k^{1/p-1/2}.

## Limitations
- Hilbert/ell_2 bound exact and machine-checked at identity/inequality level. General 2-UC extension cites (not re-derives) classical modulus-to-squared-form conversion mu->c_Y (Ball-Carlen-Lieb/Xu-type); check conversion for the specific Y at hand.
- First pointwise midpoint form (U1) failed on random data and is unused; proof uses only averaged energy consequence (passes 3000 trials). Earlier standalone L_1 D>=sqrt(2) computation was arithmetically wrong (sum bound 20 not 8) and is withdrawn; k=1 induction case replaces it.
- k^{1/p-1/2} form is a corollary of the stronger proved sqrt(k) bound, not a separate p-dependent estimate. Constant 1/2 not claimed optimal; no sharpness embedding claimed.

## Reproducibility
- output/artifacts/verify_laakso.py: builds L_k by edge replacement, checks counts, full L_1 table, L_2 diam 16 / top skeleton 4x L_1, L_3 d(A,U)=64, 200 Hilbert identity/quadrilateral trials, telescoping algebra. Expect VERIFY_OK.
- output/artifacts/verify_fork_inequalities.py: 3000 trials of (H1) quadrilateral, (H2) per-block drop, (G) general-shaped form mu=1/8. Expect STRESS_OK.
- Independent recomputation: BFS on L_2/L_3 top vertices {A,U,T,L,R,B} gives 4x/16x L_1 tables respectively.

## References
- M. Mendel, A. Naor, Markov convexity and local rigidity of distorted metrics, arXiv:0803.1697.
- S. J. Dilworth, D. Kutzarova, S. Stankov, Metric embeddings of Laakso graphs into Banach spaces, arXiv:2203.08229 (L_2->L_1 >=9/8; Remark 14 snowflake only).
- F. Baudier et al., On the geometry of the countably branching diamond graphs, arXiv:1612.01984.
- S. Li, Markov convexity and nonembeddability of the Heisenberg group, arXiv:1404.6751.
