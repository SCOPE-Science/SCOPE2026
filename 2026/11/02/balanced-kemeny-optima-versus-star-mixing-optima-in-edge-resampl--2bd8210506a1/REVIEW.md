# Independent mathematical audit

## correctness

PASS

Fresh Bernoulli edge snapshots yield block transition matrix P=[[r^b I_a,(1-r^b)/b J],[(1-r^a)/a J,r^a I_b]], because exchangeability makes each neighbor equally likely conditional on moving. Eigenvalues are 1, r^a+r^b-1, r^b multiplicity a-1 and r^a multiplicity b-1. The spectral Kemeny identity gives (a-1)/q_b+(b-1)/q_a+1/(q_a+q_b), with q_k=1-r^k. Convex-decreasing f(x)=1/(1-r^x) and symmetry show strict minimum at balanced parts. The absolute radius is max(r^a,1-r^a-r^b) for a<=b; its opposing monotone branches yield the exact star/balanced/crossover alternatives, including star at p=1/2,n>=5. For balanced K_m,m, the negative near-minus-one part-constant eigenvalue bounds TV mixing below by (log2)/[-log(1-2^(1-m))], while star radius 1/2 gives TV<=2(1/2)^t and mixing by t=3. Kemeny balanced ~2m, star ~4m. Independent direct transition-matrix spectral computations for 474 (n,a,p) instances n=4..18 verified formulas and extrema; small near-ties were excluded from floating comparison, and exact proofs cover all n and 0<p<1.

## originality

PASS

The edge-uniform evolving random-walk transition probability (1-(1-p)^d)/d and Kemeny spectral formula are prior art. The inspected original cover-time study does not derive the complete bipartite Kemeny-vs-eigenradius optimizer conflict or exponential mixing separation at identical p. Static and nonbacktracking Kemeny papers are different Markov chains. Full optimizer comparison is assessed as an original natural exact classification, subject to unindexed prior queueing/random-environment Markov studies.

## value

PASS

Stationary-target average hitting times and worst-start mixing are standard but importantly different objectives in stochastic networks. An exact all-order tradeoff—balanced graph has half the asymptotic Kemeny but exponential mixing delay versus star—is a mathematically motivated counterexample to identifying their optimizers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
