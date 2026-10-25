# Independent mathematical audit

## correctness

PASS

For arbitrary positive r,s,g, the carry identity s2(n+t)-s2(n)=r+s-C and explicit two-state digit-transfer matrices with geometric tail recover the exact rational carry PGF and natural density (uniform finite-residue approximation). Subtracting gap-g and gap-(g+1) PGFs gives z^(g+1)(1-z)^2 S_r S_s/[2^(r+s+g)(2-z)]. Truncation at carry count r+s gives difference 4^(-g-1)(N_h - sum_(k=1)^h N_(h-k)/4^k), h=r+s-g-1, and zero for g>=r+s. Interval-convolution adjacent coefficients vary by at most one, so N_(h-k)<=N_h+k and the parenthetical factor >=(2/3)N_h-4/9>=2/9, proving strictness, sharp last increase and plateau. Independently computed 175 parameter/gap exact rational checks; 972 original finite transitions plus 45 distinct residue checks inspected, not substituted for proof.

## originality

PASS

Known correlation-transfer frameworks permit evaluating c_t, and prior two-run lower bounds are close; inspected primary analysis does not state/prove the universal positive adjacent-gap differences with exact first stationary gap r+s. The new result is a strict parameter inequality, not the already-known coefficient algorithm.

## value

PASS

Separating-zero length is a canonical physical/statistical parameter within the two-one-run correlation family singled out in prior work. Sharp strictly increasing density until exact finite saturation at total ones r+s (not merely asymptotic decorrelation) is a useful structural boundary; exact increments quantify the entire transition for every pair of block lengths. Not reducible to generic digit-sum existence or a textbook carry fact without substantive sign analysis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
