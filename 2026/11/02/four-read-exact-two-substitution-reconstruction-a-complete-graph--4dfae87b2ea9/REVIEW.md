# Independent mathematical audit

## correctness

PASS

After translating the true source to zero, every other candidate differs on a nonempty D and must satisfy |D cap e|=|D|/2 for each four size-two error support. This forces |D|=2 (every edge crossing an exact 2-vertex transversal) or |D|=4 (all used vertices contained in D). For n>=5, the latter happens exactly when <=4 coordinates are incident. Classifying four-edge graphs with >=5 incident vertices by odd-cycle component or forest component-count and minimum bipartition class yields four named motifs plus the five-vertex star only when no isolate is present. Exact labeled counts give A_n. Only triangle+edge and exceptional star lack a uniquely reconstructing 3-read subset; other surviving motifs have three pairwise disjoint edges. An independent brute-force four-edge graph enumeration checking all 2-sets D confirmed motif-stratified totals 15,240,1785,8225,28665 for n5..9. Distinctness and exactly-two rather than at-most-two errors are indispensable.

## originality

PASS

Prior fixed-weight substitution results address worst-case number of reads and majority-vote thresholds, not the exact set of reconstructible quadruples. Wang–Yaakobi–Zhang establish 3-read uniqueness in the at-most error model; that sufficient matching case is explicitly acknowledged, and it does not cover the new irreducible triangle+edge or five-star. A Hamming-ball intersection algorithm can be specialized to evaluate instances but does not state this closed all-n motif enumeration for exact spheres. An older combinatorial transversal-graph formulation might contain equivalent classification, which remains a priority risk.

## value

PASS

Source reconstruction under a fixed exact corruption budget is a natural coding-theoretic question. The graph classification gives a complete natural four-read exact-weight invariant, tight labeled enumeration, and the first genuinely four-read patterns. The length-five star is particularly informative: correct unique decoding despite systematically wrong majority at the center. The result does not claim a new worst-case reconstruction threshold and limits itself to four distinct binary radius-two reads.

The dated certificate retains the supplied scientific assessment, sources and limitations.
