# Complete mod-two homology spectra of ternary affine-plane line erasures

## Finding
Write \(P=\mathbb F_3^2\) for the nine points of the ternary affine plane and \(\mathcal L\) for its twelve three-point lines. For every \(E\subseteq\mathcal L\), define the line-erasure complex
\[
K_E=\{S\subseteq P:\ L\nsubseteq S\text{ for every }L\in\mathcal L\setminus E\}.
\]
Thus \(E\) consists of the forbidden lines whose constraints have been erased. Put \(m=|E|\) and \(b_i(E)=\dim_{\mathbb F_2}\widetilde H_i(K_E;\mathbb F_2)\).

**Complete spectrum.** At \(m=0\), the only nonzero reduced Betti numbers are \(b_2=1\) and \(b_3=11\). For \(1\le m\le7\), every \(b_i\) vanishes except possibly \(b_3\); its complete frequency distribution over all \(\binom{12}{m}\) choices is:

| Erased lines \(m\) | Values of \(b_3\) and number of erasures attaining each value |
| --- | --- |
| \(1\) | \(9:12\) |
| \(2\) | \(7:54,\quad 9:12\) |
| \(3\) | \(4:36,\quad5:72,\quad6:108,\quad10:4\) |
| \(4\) | \(0:9,\quad3:288,\quad4:162,\quad6:36\) |
| \(5\) | \(0:72,\quad1:108,\quad2:468,\quad3:144\) |
| \(6\) | \(0:324,\quad1:528,\quad2:72\) |
| \(7\) | \(0:684,\quad1:108\) |

At \(m=8\), precisely nine choices have \(b_4=1\) and all other reduced Betti numbers zero; these choices are exactly those for which the four **retained** lines are the full pencil through one of the nine points. The other \(486\) choices have zero reduced mod-two homology. At \(m=9\), precisely four choices have \(b_5=1\) and all other reduced Betti numbers zero; these are exactly the choices for which the three retained lines form a parallel class. The other \(216\) choices have zero reduced mod-two homology. For \(10\le m\le12\), every reduced mod-two homology group vanishes. Together these cases cover all \(2^{12}=4096\) line-erasure patterns.

In particular, line deletion need not monotonically eliminate homology: isolated degree-four and degree-five classes reappear after the degree-three classes have disappeared in many intermediate patterns. The exceptional cases detect the pencil and parallel-class geometries. **Every immediate predecessor** of each of these exceptional line-erasure complexes (obtained by restoring any single missing line constraint) is mod-two acyclic; thus the new sphere class actually appears after the previous one-line step had no reduced mod-two homology.

## Assumptions and scope
All lines are the affine one-dimensional subspaces or translates in the *fixed* plane \(\mathbb F_3^2\), and each line constraint forbids containing all three of its points. No other forbidden faces or new points are introduced. Homology groups in the complete spectrum are **reduced homology over \(\mathbb F_2\)**. The two exceptional cases also have the indicated sphere homotopy types. The complete table is not a claim about integral homology, homotopy types for every line selection, higher-order affine planes, or ranks of maps between these complexes.

## Proof
A fully bounded exact enumeration proves the spectrum. Index \(P\) by \(j=3x+y\), with \(x,y\in\{0,1,2\}\). Form all twelve distinct three-point line masks from the pairs \(a\ne b\) and their third point \(c=2b-a\pmod3\). Each of the \(2^{12}\) bitmasks on the line set specifies exactly one retained-line family \(R=\mathcal L\setminus E\). For each \(R\), enumerate the \(2^9-1=511\) nonempty vertex subsets and retain precisely the masks containing no line of \(R\). This defines *every* simplex, with no sampled or omitted cases.

For each \(k\), form the mod-two simplicial boundary matrix \(D_k:C_k(K_E;\mathbb F_2)\to C_{k-1}(K_E;\mathbb F_2)\), whose column for a \(k\)-simplex has one bit for each of its codimension-one faces. Exact binary Gaussian elimination computes \(r_k=\operatorname{rank}D_k\). Set \(r_0=1\) to incorporate augmentation for reduced degree-zero homology, and set the absent upper rank to zero. Then \(b_k=f_k-r_k-r_{k+1}\), with \(f_k\) the enumerated number of \(k\)-simplices. The identity \(D_{k-1}D_k=0\) holds because each codimension-two face appears exactly twice in a simplicial boundary. Enumerating, ranking and counting the resulting vectors gives exactly the frequency table in the Finding section and the stated empty-homology ranges. The attached `verify_line_erasure.py` is complete executable source for this finite proof, checks the expected counts and Euler identities, and independently recomputes all ranks over the prime fields of orders three and 101 as a consistency test. The latter checks do **not** assert integral torsion-freeness.

The geometry of the two exceptional families also yields direct homotopy proofs. If the four retained lines form the pencil through \(v\), deleting \(v\) leaves a full simplex on the other eight vertices. The link of \(v\) is the join of four zero-spheres, one from each two-point set of the pencil away from \(v\); hence the link is \(S^3\). Gluing the cone \(v*\operatorname{lk}(v)\) to the full simplex along that link yields a space homotopy equivalent to its suspension, \(S^4\). If the three retained lines are a parallel class, they partition \(P\) into three disjoint triples. The complex is the join of the boundaries of these three triangles: \(S^1*S^1*S^1\cong S^5\). There are exactly nine pencils (one per point) and four parallel classes (one per direction), agreeing with the exhaustive checks. All remaining assertions, including uniqueness of the exceptional configurations among the relevant sizes, follow from the exact full enumeration.

## Verification
Run `python3 verify_line_erasure.py` using Python 3.8 or later. The script has no external dependencies and checks all 4096 line systems, the listed multiplicities, both geometric exceptional predicates and absence of any other nonzero mod-two Betti number. An additional independent-prime check is performed for every configuration. The expected final output is JSON with `total_line_subsets` equal to 4096, `pencils` equal to 9, `parallel_classes` equal to 4, and `status` equal to `PASS`.

## Relationship to prior work
Work on affine Steiner triple systems and partial block specifications motivates studying the effect of erasing selected line constraints (Gower, 1997/1998). The full-line complex \(K_\varnothing\), including its integral homology, is already studied by Lew (2021, Chapter 7, Figure 1.1): the present \(m=0\) data are a **previously known baseline**, not a new claim. Lew's 2020 paper establishes general representability and boxicity results for complexes whose missing faces form partial Steiner systems, including an abstract duality reduction for homology, but does not state the 4096-case Betti distribution or the line-erasure exceptional families. The complete block-erasure spectrum, rather than the original full-system Betti numbers or boxicity, is the assertion here. The primary Gower article's full text was not accessible for direct comparison; its bibliographic abstract concerns defining sets rather than homology, and this remains a stated literature-access risk.

## Limitations
This is an exact **finite** result for the order-three affine plane, not a theorem for arbitrary order. Equality of computations over several fields does not establish integral homology without an integral calculation. Mod-two acyclicity does not imply contractibility. The table does not determine inclusion-induced maps, integral torsion, arbitrary homotopy types, or Betti numbers outside the specified 4096 systems. The 1997/1998 defining-sets paper was not inspected in full, although its abstract and topic were examined; a later full-text comparison could narrow the originality claim.

## References
1. R. A. H. Gower, *Defining sets for the Steiner triple systems from affine spaces*, Journal of Combinatorial Designs **5** (1997), 155–175; verified first online appearance 7 December 1998. DOI: `10.1002/(SICI)1520-6610(1997)5:3<155::AID-JCD1>3.0.CO;2-E`.
2. A. Lew, *Representability and boxicity of simplicial complexes*, arXiv:2008.09997 (first submitted 23 August 2020), particularly Theorems 3 and 5.
3. A. Lew, *Studies in topological combinatorics*, doctoral thesis (August 2021), Chapter 7 and Figure 1.1. `https://www.math.cmu.edu/users/alanlew/files/theses/phd%20thesis.pdf`.
