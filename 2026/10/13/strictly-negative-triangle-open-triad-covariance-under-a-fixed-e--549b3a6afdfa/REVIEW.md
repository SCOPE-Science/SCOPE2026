# Independent mathematical audit

## correctness

PASS

For n>=4, N=n(n-1)/2, t=C(n,3), q_j=(m)_j/(N)_j. Let S count noninduced 2-stars, T triangles and W induced exactly-two-edge triples; W=S-3T. By shared-edge overlap, E(TS)=t[3q3+6(n-3)q4+(3t-3-6(n-3))q5]; E(T²)=t[q3+3(n-3)q5+(t-1-3(n-3))q6]. Subtract products and factor: Cov(T,W)=-6tq3(N-m)(N-m-1)[(n²-3n-8)m+(n-1)(n²-n-4)]/[(n+1)(n+2)(N-5)(N-4)(N-2)]. The bracket is >0 in the claimed range (n=4 gives 24-4m, m=3..4); thus strict negative iff 3<=m<=N-2, zero otherwise. As n→∞ m/N→p∈(0,1), n^-3 Cov→-p^4(1-p)^2. Substituting independent p^j gives 3t p^4(1-p)[2(n-3)-(3n-8)p]. Independently derived hypergeometric moment formulas and direct enumerated all labeled graphs n=4,5,6 to check exact covariance; finite checks through n=40 corroborate sign but all-n algebraic factor proof controls universal statement.

## originality

PASS

Subgraph-count covariance and G(n,m) conditional central-limit theory are established. Dey-Terlov fully readable arxiv §4.4 gives joint conditional CLT involving triangle and ordinary wedge, not the finite-n sign of covariance with induced W=S-3T; Reinert-Röllin handle independent-edge asymptotics. Janson (1990) considers both fixed-edge and induced subgraph statistics and is a material plausible stronger source: full primary was inaccessible after public/OA tries and authorized institutional retrieval returned vpn_disconnected. No whole-article noncoverage claim is made; best-of-knowledge novelty concerns exact all-(n,m) negativity and G(n,p) sign reversal, not general overlap-moment techniques.

## value

PASS

The edge-conditioned versus independent-edge sign reversal is an exact structural dependence effect between canonical three-vertex graph motifs. The theorem determines every finite edge-density boundary and the dense asymptotic coefficient; these are natural quantities useful in random graph motif inference, separate from a general CLT.

The dated certificate retains the supplied scientific assessment, sources and limitations.
