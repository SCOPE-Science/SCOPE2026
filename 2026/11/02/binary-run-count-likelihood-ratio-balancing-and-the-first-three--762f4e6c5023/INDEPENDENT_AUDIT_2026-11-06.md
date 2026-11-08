# Independent mathematical audit

## correctness

PASS

For a fixed binary composition (k,n-k), splitting into positive 0/1 run lengths yields A(2s)=2*C(k-1,s-1)*C(n-k-1,s-1) and A(2s+1)=(n-2s)/s times their product. The next-row/old-row ratio h_s=k(n-k-s)/[(k-s+1)(n-k-1)] is nondecreasing along the shared support, and strictly increasing between adjacent run-pairs when k<floor(n/2); any new right-tail support has old count zero. Handle k=0 and odd central equality by complements. Finite exchangeability conditions on K, a convex mixture of fixed-composition laws, so balanced tails dominate. Direct three-color exact suffix recurrence gives old (3,1,4) counts at r=7,8 of 60,14 and new (2,2,4) of 120,24, a negative minor -240; the recurrence exhausts all positive 3-color balancing moves for n<=7 and proves the first obstruction at n=8. The boundary restriction to three positive classes and elementary balancing is essential.

## originality

PASS

The classical conditional run-count distribution, exchangeable representation, and multicolor run enumeration are prior. The evaluated claim instead orders entire binary laws across compositions by monotone likelihood ratio and proves a sharp positive three-color cutoff; these implications were not found in earlier displayed distribution formulas. Best-of-knowledge PASS, with substantial uninspected original text of Schuster–Gu and earlier order-theoretic run-statistics literature as priority risk.

## value

PASS

The monotone-likelihood-ratio envelope identifies the sharp worst-case run-count tails over all finitely exchangeable binary sequences; the fully classified first genuine 3-color failure pinpoints the limit of binary theory. These are interpretable nontrivial ordering facts with direct applications to conditional run statistics, beyond textbook enumeration alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
