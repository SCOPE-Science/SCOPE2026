# Complete systematic equality classification for four-bit three-server PIR codes
## Finding
Fix four independent binary information symbols, four designated systematic codeword coordinates, and four separately labeled parity coordinates. Each of the \(2^{16}=65536\) binary matrices \(G=[I_4\mid P]\) encodes four information symbols into eight physical symbols. Exactly \(7800\) such matrices have three mutually disjoint linear recovery sets for every one of the four information symbols.

No binary systematic generator \(G=[I_4\mid P]\) with fewer than four parity columns has this three-server PIR property. The minimum length eight is also known in the unrestricted linear problem; the new result here concerns the complete **systematic presentation** equality layer, not the previously known numerical minimum.

Let \(S_4\times S_4\) act by relabeling the four information symbols and their corresponding systematic columns together, and by independently permuting the four parity columns. Its \(576\) elements partition the \(7800\) qualifying matrices into exactly \(26\) orbits. The orbit-size multiset is
\[
\{288^{\times12},\ 576^{\times6},\ 96^{\times4},\ 144^{\times3},\ 72\}.
\]
The supplied `orbit_representatives.tsv` gives one lexicographically minimal parity-column representative, orbit size, stabilizer order, parity rank, and incidence-criterion result for all \(26\) orbits. Every listed stabilizer has order \(576\) divided by the orbit size. The independent Burnside fixed-point sum is \(14976=576\cdot26\).

**Every** one of the \(7800\) matrices has the stronger three-request batch property: for every multiset of three information-symbol requests, three pairwise disjoint sets of codeword coordinates recover the requested symbols (respecting repetitions). Of the \(7800\), exactly \(456\) matrices in three orbits satisfy the sufficient pairwise-intersection incidence criterion from the foundational 2015 paper. The remaining \(7344\) matrices in \(23\) orbits satisfy three-PIR and three-batch recovery without meeting this sufficient criterion. These matrices are not asserted to be outside every other known construction.

All \(7800\) matrices yield binary linear codes of minimum Hamming distance exactly \(3\). Among the qualifying parity submatrices, \(3000\) have rank \(3\) and \(4800\) have rank \(4\); there are \(13\) symmetry orbits in each rank stratum.

## Assumptions and scope
Write \(e_i\) for the \(i\)-th standard basis column of \(\mathbb F_2^4\), indexed by \(i\in\{1,2,3,4\}\). A recovery set for \(e_i\) is a nonempty subset of the eight **column indices** whose column sum over \(\mathbb F_2\) is \(e_i\); repeated columns at different physical indices are distinct coordinates. A three-server PIR generator has, separately for each \(i\), three pairwise disjoint recovery sets. This does not demand that recovery sets chosen for different information symbols be disjoint simultaneously.

A three-request batch generator must, for **every** multiset \(\{i,j,k\}\) of three information indices, admit three mutually disjoint recovery sets with respective sums \(e_i,e_j,e_k\). There are \(\binom{4+3-1}{3}=20\) request multisets, counting repetitions.

A parity matrix \(P\) has four labeled columns \(p_1,p_2,p_3,p_4\in\mathbb F_2^4\). An incidence-criterion matrix is one where each information index belongs to at least two column supports and any two column supports meet in at most one information index (the \(k=3\) specialization of the published sufficient criterion).

The equivalence relation preserves the specified systematic/parity split. It is **not** an unrestricted linear code equivalence under a general information-basis transformation or mixing the eight physical positions.

## Proof
First reduce the three-recovery condition exactly. For a fixed \(e_i\), any triple of disjoint recovery sets can be replaced by one containing the singleton systematic column \(\{i\}\): at most one of the original three uses physical systematic coordinate \(i\); replace that set by \(\{i\}\), or replace any set if no original set uses \(i\). The other two sets remain disjoint and avoid systematic index \(i\).

Any recovery of \(e_i\) avoiding systematic position \(i\) must use a nonempty set \(T\) of parity coordinates. Let \(u_T=\bigoplus_{j\in T}p_j\). Such a recovery exists exactly when \((u_T)_i=1\), and then its systematic companion indices are uniquely \(\operatorname{supp}(u_T)\setminus\{i\}\). Consequently the three-PIR condition for \(e_i\) is exactly the existence of two nonempty disjoint parity-index sets \(T,U\) for which
\[
(u_T)_i=(u_U)_i=1,\quad
\bigl(\operatorname{supp}(u_T)\setminus\{i\}\bigr)\cap
\bigl(\operatorname{supp}(u_U)\setminus\{i\}\bigr)=\varnothing.
\]
The verifier applies this equivalence to all four information coordinates for every ordered four-tuple of columns, exhausting precisely \(16^4=65536\) possibilities. Independently, without using the reduction, it computes all \(256\) subset sums of the eight physical columns and searches directly for three pairwise disjoint recovery subsets for every \(e_i\). The two complete lists agree and contain exactly \(7800\) matrices. Separate exhaustive tests for zero, one, two, and three parity columns find no solution.

For the stronger batch statement, the verifier constructs the complete set of inclusion-minimal recovery sets for each \(e_i\). Removing redundant columns from a valid recovery preserves its recovered target and does not spoil disjointness, so restricting the test to inclusion-minimal sets loses no solutions. It checks all \(20\) three-request multisets and finds feasible disjoint triples for **each** of the \(7800\) qualifying generators.

The \(24\) information permutations act on the binary masks of parity columns; the \(24\) parity permutations act by rearranging the four physical parity indices. Canonicalizing every qualifying ordered four-tuple under this action yields exactly \(26\) equivalence classes, with the reported sizes and representatives. A second symmetry count directly sums fixed generators over all \(576\) group elements, obtaining \(14976\) and hence \(26\) classes by Burnside's lemma. The rank and incidence counts are obtained by directly evaluating all qualifying matrices; the complete representative table makes their orbit distribution reproducible.

Lastly, direct enumeration of all \(15\) nonzero information words establishes minimum Hamming distance at least \(3\) for every optimum; the standard 3-PIR distance argument gives the same lower bound. Since there is at least one codeword of weight \(3\) for each matrix (verified by the supplied code), the minimum distance is exactly \(3\).

## Verification
From the package directory, execute `python3 verify.py`. The script depends only on the Python standard library. It reconstructs every stated finite value from definitions and verifies its own table against the committed `orbit_representatives.tsv`.

The final replay line is

`VERIFY_OK systematic_optima=7800 orbits=26 batch_all=true incidence_lemma=456 other=7344 burnside=26`

The package contains `verification_output.txt` recording the complete expected output. The finite proof applies only to the exact systematic presentation space stated above.

## Relationship to prior work
Fazeli, Vardy, and Yaakobi introduced systematic and general PIR codes, including the use of three mutually disjoint recovery sets for each information symbol, and exhibited small optimal constructions. Their Lemma 7 explicitly gives a sufficient but not necessary parity-incidence condition: each information symbol occurs in at least \(k-1\) parity supports and distinct supports intersect in at most one position. The present result establishes precisely how sparse that sufficient condition is among all optimal systematic presentations at four information symbols and three servers.

Rao and Vardy proved the three-server redundancy lower bound, which implies that length seven cannot suffice with four information symbols. Kurz and Yaakobi subsequently tabulated exact short-block-length optimal cardinalities and constructions, including the four-message case. Hollmann and Luhaäär showed optimal linear three-PIR and three-batch **constructions**, but construction existence does not imply that every optimal systematic three-PIR presentation is three-batch or determine all \(26\) equivalence classes.

Full-text comparison of the three directly relevant foundational and follow-up papers did not locate a count of \(7800\), a \(26\)-orbit census, or the universal equality of the three-PIR and three-batch conditions **within this restricted systematic equality layer**. Targeted parameter and equivalent-formulation searches also did not locate an implication-equivalent published statement.

## Limitations
The classification concerns generator-matrix presentations \(G=[I_4\mid P]\) with the first four coordinates distinguished as systematic and the last four as parity coordinates, all indices physically labeled. It does not count arbitrary nonsystematic PIR matrices or equivalence classes under general changes of information basis. The batch equivalence is proved for these \(7800\) matrices, not for larger codes or all parameter choices.

The parity-incidence comparison is only to the *sufficient criterion* in the cited 2015 Lemma 7, and does not rule out other published constructions covering the same instances. A residual originality risk is an obscure or unindexed systematic-matrix enumeration, notwithstanding noncoverage in the inspected directly relevant full texts.

## References
1. Arman Fazeli, Alexander Vardy, and Eitan Yaakobi, “PIR with Low Storage Overhead: Coding instead of Replication,” arXiv:1505.06241v1, first public 2015-05-22, especially Definition 3 and Lemma 7.
2. Ankit Rao and Alexander Vardy, “Lower Bound on the Redundancy of PIR Codes,” arXiv:1605.01869v1, 2016.
3. Sascha Kurz and Eitan Yaakobi, “PIR Codes with Short Block Length,” arXiv:2001.03433v1, 2020.
4. Henk D. L. Hollmann and Urmas Luhaäär, “Optimal possibly nonlinear 3-PIR codes of small size,” arXiv:2208.14552v1, 2022.
