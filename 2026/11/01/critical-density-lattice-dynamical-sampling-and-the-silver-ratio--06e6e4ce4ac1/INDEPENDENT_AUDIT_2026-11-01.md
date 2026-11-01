# Independent mathematical audit

## correctness

PASS

For each finite K, the 2K-site dependency blocks partition Z; each observation R^t f(2Kq+s) uses only its assigned block for t<K. In the displayed alternating coordinate order the time-t pair introduces f(-t),f(t+1), each with diagonal 2^(-t), giving determinant 2^(-K(K-1)). The Laurent Chebyshev identity 2 T_j(R)f(n)=f(n-j)+f(n+j) reconstructs all coordinates. The alternating coefficient l1 norm is |T_j(i)|=(alpha^j+(-1)^j alpha^(-j))/2 for alpha=1+sqrt(2), bounding the inverse norm above by polynomial(K)alpha^K and below by alpha^(K-1)/sqrt(K); ||H_K|| lies between 1 and sqrt(2K). Therefore the Kth-root condition number tends to alpha for all positive K, while the frame ratio root is alpha^2. Independently implemented exact Fraction elimination on H_K for K=1..7 and confirmed the determinants; script source was also inspected. These tests are ancillary; the triangularity and Chebyshev proof supply the all-K result.

## originality

PASS

The claim is the precisely specified two-adjacent-sensors-per-2K-cell, K-time full-bandwidth inverse and sharp conditioning exponent, not the general possibility of dynamical sampling. Aldroubi–Davis–Krishtal arXiv:1312.3203 Sections 2 and 3 prove recovery conditions with regular single-residue sampling and, for symmetric filters, auxiliary time-zero spatial samples; Theorems 2.1 and 2.4 do not state this exact adjacent-site local block determinant or Chebyshev/silver-ratio asymptotic. Bulai et al. arXiv:2609.25472 concern bandlimited GPW dynamical frames and finite path conditioning; only abstract was accessible during this independent run, hence no whole-paper exclusion. Resultary returned finite normalized-path and cyclic low-pass dynamical sampling findings with different domains. A possible older exact local observability stencil is residual priority risk, but no known source inspected entails this sharp local constant.

## value

PASS

Full-bandwidth exact critical sampling with local operators is a natural stability benchmark: finite-K exact recovery coexists with an exponentially deteriorating inverse constant, quantified by the nontrivial algebraic base 1+sqrt(2). The result explains a specific sensor-geometry tradeoff rather than asserting global sensor-design optimality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
