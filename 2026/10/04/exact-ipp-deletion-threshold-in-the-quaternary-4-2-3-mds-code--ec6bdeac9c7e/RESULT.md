# Exact IPP deletion threshold in the quaternary \([4,2,3]\) MDS code
## Finding
Let \(\mathbb F_4=\{0,1,\omega,\omega^2\}\) satisfy \(\omega^2=\omega+1\), and consider the standard linear MDS code
\[
C=\{(u,v,u+v,u+\omega v):u,v\in\mathbb F_4\}.
\]
The largest subcode of \(C\) with the two-parent identifiable parent property (IPP) has exactly \(8\) words. There are exactly \(48\) maximum IPP subcodes.

Identify a codeword with its parameter point \( (u,v)\in\operatorname{AG}(2,4)\). Across the twenty affine lines, the maximum subcodes split into two equally large profile classes. Exactly \(24\) have line-intersection multiset \(\{4^2,2^{16},0^2\}\), and exactly \(24\) have \(\{3^8,2^4,1^8\}\).

## Assumptions and scope
The IPP notion is the standard two-parent property. The finite criterion used is: (IPP1) every three distinct codewords have a coordinate at which their three symbols are pairwise distinct; and (IPP2) for every two disjoint pairs of codewords, some coordinate has disjoint two-symbol sets. These conditions are equivalent to the descendant-set definition in the cited source.

The ambient code \(C\) is the quaternary linear \([4,2,3]\) MDS code. The claim concerns subcodes of this fixed natural MDS object, rather than the unrestricted maximum size of all quaternary length-four IPP codes.

## Proof
Represent \(\mathbb F_4\) by two-bit polynomials modulo \(t^2+t+1\), with \(\omega=t\). The sixteen displayed codewords are distinct and every two differ in at least three coordinates, so the ambient code has parameters \([4,2,3]\).

For each three-element subset of \(C\), mark it forbidden exactly when IPP1 fails. For each four-element subset, mark it forbidden exactly when at least one of its three partitions into two disjoint pairs fails IPP2. A subcode is IPP if and only if it contains none of these forbidden subsets. The verifier constructs these forbidden sets directly from the coordinate definitions, then checks all \(2^{16}=65536\) subcodes. The largest admissible cardinality is \(8\), attained by exactly \(48\) subsets; no subset of size at least \(9\) is admissible.

For the geometric refinement, the verifier constructs all twenty affine lines in \(\operatorname{AG}(2,4)\), computes their intersection sizes with every one of the \(48\) maximum parameter sets, and obtains exactly the two stated multisets, each \(24\) times.

## Verification
Run `python3 verify.py` beside the packaged files. It reconstructs the field arithmetic, the ambient code, every forbidden IPP1/IPP2 witness, all \(65536\) subcodes, and all twenty affine lines. The captured run is stored in `verification_output.txt`; the machine-readable totals are in `certificate.json`.

## Relationship to prior work
Blackburn, Etzion and Ng give the standard IPP descendant formulation and the equivalent IPP1/IPP2 criterion, and they use the ternary \((4,3,9)\) Hamming code as the sporadic positive length-four example. Their length-four analysis proves that no nonbinary prolific IPP code of length four exists beyond that ternary example; in particular the quaternary case is the first alphabet size excluded from prolificity. Their result does not determine how large an IPP subcode can remain inside the standard quaternary MDS code, nor does it enumerate the extremal subcodes or their affine-line profiles.

The present finite result quantifies that first excluded MDS case: exactly half of the sixteen MDS codewords can be retained under IPP, and the forty-eight extremizers have two sharply different affine incidence profiles.

## Limitations
This result does not determine the unrestricted maximum size of a quaternary length-four IPP code. It also does not assert that the two affine-line profile classes are the full orbit decomposition under every automorphism of the ambient code. The originality search found no statement of this exact deletion threshold or the \(48=24+24\) profile census, but unindexed finite computations remain a residual literature risk.

## References
1. S. R. Blackburn, T. Etzion, and S.-L. Ng, “Prolific Codes with the Identifiable Parent Property,” IACR Cryptology ePrint Archive, Paper 2007/276, first received 2007-08-07; later SIAM Journal on Discrete Mathematics 22(4), DOI 10.1137/070695551.
