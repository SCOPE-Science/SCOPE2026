# Independent mathematical audit

## correctness

PASS

The connected-graph two-step Laplacian kernel forces the consecutive firing indicator vectors of a primitive period-two state to be complementary, and local threshold inequalities yield exactly o_v(f) independently selectable chip values per vertex; dividing oriented phases by two gives N(G)=sum_f prod_v o_v(f)/2. For K_{n,n}, grouping left/right firing counts (i,j) produces q_n(i,j)=Pr[Bin(n,1-j/n)=i]Pr[Bin(n,1-i/n)=j]; the local Gaussian along i+j=n yields sum q_n~sqrt(pi*n)/2 and the normalized Beta(1/2,1/2) marginal; maximal binomial-mass bounds make both tails negligible. For deletion H_n with max degree R fixed, each removed edge has exactly 2/n conditional expected logarithmic cut-weight contribution; bounded-degree fixed-size sampling gives O_R(1/n) variance on each interior strip, hence uniform E[exp(-X)]~exp(-2|E(H_n)|/n). Endpoint domination extends uniformity and log degree product=-2m_n/n+O_R(1/n). Thus N(G_n)/N(K_{n,n})=exp(-2m_n/n)(1+o_R(1)) and N(G_n)~sqrt(pi*n)/4 prod_v degree_G(v) uniformly; the arcsine phase law survives. This proves only primitive period-two configurations, not attraction basins or all possible periods.

## originality

PASS

Best-of-knowledge conclusion from actual source-tree proof reconstruction, current Resultary published-finding search and material inspected from primary literature: The submitted result requires new uniform sampling estimates after edge deletion. The strong known starting identity does not imply the additional asymptotic without those estimates. Source access and possible historical equivalents remain listed as residual risks.

## value

PASS

This is a natural robustness theorem for exactly solvable parallel chip firing: arbitrary adversarial bounded-degree edge deletions destroy exchangeability, yet the asymptotic orbit census retains a universal edge-number factor and the nonuniform arcsine marginal. It determines asymptotic behavior for infinitely many irregular graph families, not just one small example or a renamed exact counting identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
