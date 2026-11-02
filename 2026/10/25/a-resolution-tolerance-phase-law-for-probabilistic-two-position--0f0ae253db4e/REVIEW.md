# Independent mathematical audit

## correctness

PASS

The complete resolution-k four-composition alphabet has b_i=(i+1)(k-i+1) symbols in GC-bin i, and the probability of exactly one GC in a pair is (i(k-j)+(k-i)j)/k^2. With weighted matrix T_ij=b_j 1_{success>=1-eps}, standard Perron walk growth gives 2^{C}=rho(T). When 0<=eps<1/2, allowable bins must lie on opposite GC halves with failure p+h-2ph>=max(p,h), forcing both bins to the extreme eps tails and hence row sums <=W_k(floor(k eps)). The smaller eps/2 tail rectangle is a complete bipartite induced subgraph with Perron root W_k(floor(k eps/2)); W_k(m)=(m+1)(m+2)(3k+3-2m)/6 leads to uniform absolute-factor k(1+k eps)^2 bounds and the exponent 3-2 min(alpha,1). For eps<1/k only the two pure bins remain, giving rho=k+1; at eps=1/k for k>=3, the four-bin weighted path yields rho=[k+1+sqrt((k+1)(9k+1))]/2 and asymptotic one-bit jump. Independently checked rational adjacency and numerical Perron roots against bounds and threshold for k=2..15 and multiple tolerances. Finite checks are corroborative only; k=2 is properly excluded at eps=1/k.

## originality

PASS

The motivating October 7 2026 primary paper Theorem 15 already supplies the exact general weighted transfer matrix/capacity for arbitrary windows, so that framework is NOT new. Its materially read Sections II-III and Appendix yield bin multiplicities and generic capacity but do not state or imply, without new Perron-tail analysis, the uniform resolution-dependent two-sided estimates and explicit onset eigenvalue. The earlier deterministic all-realizations composite GC model is distinct. Best-of-knowledge originality with explicit general-theorem corollary risk.

## value

PASS

Resolution and permissible synthesis error are natural design parameters in probabilistic composite-DNA constrained coding. The uniform capacity scaling and precise first change at eps=1/k provide a reproducible two-parameter phase description beyond a general transfer-matrix algorithm, without asserting wet-lab gains or error-correction properties.

The dated certificate retains the supplied scientific assessment, sources and limitations.
