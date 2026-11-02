# Independent mathematical audit

## correctness

PASS

For odd b>=3 and integer k>(b+1)/2, translation by (1/2,1/2) makes a right triangle with legs d/2,d/b, d=k-(b+1)/2, so area=(2k-b-1)^2/(16b). No facet has an integer point. Exactly I=sum_{j=0}^{q-1} floor((b j+r)/2) interior points for k=bq+r,0<=r<b. Because b odd, parity of bj+r is parity of j+r; the explicit count of odd terms yields Delta=(2r-b-1)^2/(16b) plus 0 if q even, -1/4 if q odd r even, +1/4 if q odd r odd. Minimizing the even r square gives -1/4 if b=3 mod4 and -(b-1)/(4b) if b=1 mod4, with stated exhaustive residues; maximizing gives (b+1)^2/(16b) with q even r=0 or q odd r=1. The negative criterion is q odd,r even and |2r-b-1|<2 sqrt(b). Independent exact rational enumeration tested 13161 admissible parameter pairs and sign/extrema. The universal proof uses exact finite row summation, not finite enumeration.

## originality

PASS

Qualified PASS for complete two-parameter signed discrepancy spectrum, exact equality residue classes and sparse negative phase O(sqrt(b)). The unimodular halfway-Pick theorem of Chu–Karshon is outside this family because the primitive normal determinant sequence is 1,2,b. Beck–Robins Dedekind–Rademacher counting can in principle produce every individual count, but a general computation procedure alone is not a published uniform sharp spectrum; exact earlier specialization remains possible.

## value

PASS

The family is a clean minimal nonunimodular perturbation of halfway-lattice Pick-type triangles. Its signed defect can be negative, unlike the positive unimodular constant, and the exact residue-based phase/extrema explain when the topological defect persists or reverses. Complete strict bounds and sparse negative interval are meaningful structural data, not arbitrary sample instances.

The dated certificate retains the supplied scientific assessment, sources and limitations.
