# Independent mathematical audit

## correctness

PASS

Before hub v joins a uniform boundary-edge tree from hub u of K_{2,n}, the boundary has exactly n edges: at state k (k peripheral vertices already present), k edges enter v and n-k attach new peripherals; hence P(K=k)=k(n)_k/n^(k+1), k=1..n. After v joins each of n-k remaining peripherals attaches to u or v by an independent fair coin, so D|K=k=k+Bin(n-k,1/2). Exact conditioning gives mean (n+EK)/2 and variance (n-EK+VarK)/4. Birthday-tail product produces K/sqrt(n)=>Rayleigh, with all moments controlled by exp(-k(k-1)/(2n)); conditional binomial characteristic functions converge to independent Gaussian, giving (K/sqrt n,(D-n/2)/sqrt n)=>(R,(R+G)/2), mean and variance constants, and P(D>n/2)->1/2+1/(2sqrt2). For uniform spanning tree bridge-vertex enumeration yields D_U=1+Bin(n-1,1/2), and shared coins couple D>=D_U, strict for n>=2. Independent exact boundary-edge enumeration n=1..7 confirms the finite mixture and dominance but does not prove the limits.

## originality

PASS

Best-of-knowledge O PASS for the precise assessed final statement. Reviewed the actual final package and compared statements/implications with primary literature and published SCOPE/Resultary semantic results, using aliases, broader cases, tables and corollary checks. A birthday bridge and a Gaussian–Rayleigh root-degree law for K_{2,n}: the cited prior results cover background tools, objects and/or weaker observables; no identified theorem implies the complete evaluated final statement. Negative search is not a novelty proof; primary-source limitations and risks are explicit.

## value

PASS

The frontier-growth process and uniform spanning trees are natural but different laws on exactly the same simple K_{2,n} graph. An explicit birthday-derived two-scale root-degree distribution and strict stochastic bias quantify that difference and identify a non-Gaussian Gaussian–Rayleigh mixture, not merely a named distribution substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
