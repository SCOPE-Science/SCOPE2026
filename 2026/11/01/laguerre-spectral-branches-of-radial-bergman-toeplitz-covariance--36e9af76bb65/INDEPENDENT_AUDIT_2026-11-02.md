# Independent mathematical audit

## correctness

PASS

The actual m-channel defect is a positive Gram form: sum_{ij}< (T_{u^{i+j}}-T_{u^i}T_{u^j})x_j,x_i> = ||(I-P) sum_j u^j x_j||^2. Radial Toeplitz action on homogeneous degree n reduces to U=1-||z||²~Beta(b=α+1,a=n+d), so the block is exactly the covariance of U,U²,...,U^m, with entries (b)_{i+j}/(a+b)_{i+j}−(b)_i(b)_j/((a+b)_i(a+b)_j). Strict beta positivity makes each G_n positive definite and injective. Gram-Schmidt with monic shifted-Jacobi norms gives det G_n[1:k]=prod_{j<=k} j!(a)_j(b)_j /((a+b)_{2j}(a+b+j-1)_j). Under nU converging in moments to Gamma(b), diagonal scaling by n^-j gives positive limiting covariance H, minmax separates eigenvalues by n^-2k. The unique dominant principal minor in e_k is [1:k], so ratios of elementary symmetric functions give n^{2k}λ_k(n)->k!(b)_k, the Laguerre monic norm. Multiplicity h_{n,d}=binom(n+d-1,d-1), accumulated ~N^d/d!, yields s_J~c_k/(d!J)^{2k/d}, S_p iff p>d/(2k), exact log mass c_k^{d/(2k)}/d! at critical exponent, and full defect p>d/2. Fresh rational beta Gram determinants for (a,b)=(2,1),(3,2),(7,4),(12,3) and k<=3 matched the full product; finite tests support, do not prove asymptotic.

## originality

PASS

Best-of-knowledge PASS for the whole positive matrix semicommutator spectral hierarchy, with explicit Jacobi principal-minor determinant, Laguerre limiting eigenbranches, multiplicities and Schatten/log endpoint constants. Classical radial diagonalization and beta/Jacobi facts are prior ingredients, while the inspected operator-algebra and trace-semcommutator sources do not establish this fixed monomial covariance block hierarchy.

## value

PASS

A natural multichannel Toeplitz multiplicativity defect on a classical weighted Bergman space has a hierarchy of spectral decay powers n^-2,n^-4,... rather than one scalar compactness threshold. Exact Jacobi Gram determinants, ordered Laguerre branch constants, sharp Schatten cutoffs and endpoint logarithmic masses give precise new operator invariants that a specialist could use in semicommutator and spectral asymptotic questions. Natural boundary-distance monomials motivate the channels; it is not just a fabricated small matrix.

The dated certificate retains the supplied scientific assessment, sources and limitations.
