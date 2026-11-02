# Independent mathematical audit

## correctness

PASS

PASS. Sorting each four-digit input into A≥B≥C≥D yields u=A-D, v=B-C with 1≤u≤b−1 and 0≤v≤u. Direct subtraction gives Y=(b³−1)u+(b²−b)v, injective by reducing modulo b and realizable for every pair. Choosing D in b−u ways and the internal gap s in 0..u−v yields permutation totals 12u−4 at v=0, 24(u−v) at 0<v<u, and 6 at v=u. Constant strings give exactly b zero preimages. Quadratic optimization of the interior branch gives 24 floor((b−1)²/4) for b≥3, with parity-dependent tie count, versus 8 at b=2. Positive image pairs fill an integer triangle; under uniform image output the interior Riemann-sum limit has density two on s,t>0,s+t<1 and Q=24st. Integrating its hyperbolic tail yields the displayed sqrt/log law supported on [0,6]. An independently written exact direct enumeration matched every output fiber, maximum, and mass for bases 2 through 14; finite checks only corroborate the symbolic all-base proof.

## originality

PASS

PASS to best of knowledge with original classical gap coordinates credited. Hanover and Walden develop standard four-digit gap coordinates and forward trajectories, not the exact ordered-input inverse-fiber law or its image-uniform asymptotic distribution in the material read. The complete 2026 odd-base primary paper (Chen–Ono–Schwartz–Thakur, JIS 29, Article 26.4.7) was inspected in its theorem and proof sections; it classifies forward stable-region dynamics and terminal cycles, not input-string inverse-fiber multiplicities. No exact coverage found in Resultary or bibliographic/table search, not proof of absolute priority.

## value

PASS

PASS. The complete indegree/fiber spectrum measures one-step compression of a natural arithmetic functional graph and is not determined by its terminal cycles or fixed points. A parameter-uniform closed formula, sharp maximum and nontrivial limiting law for uniformly chosen distinct outputs answer a mathematically natural inverse-dynamics question. The logarithmic tail and explicit sampling normalization distinguish this from routine small-base computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
