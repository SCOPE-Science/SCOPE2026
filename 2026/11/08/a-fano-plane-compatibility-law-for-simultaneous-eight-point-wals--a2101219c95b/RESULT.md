# A Fano-plane compatibility law for simultaneous eight-point Walsh spectra

## Finding

Fix an integer \(d\ge 7\) and let \(G=\mathbb F_2^d\). Write \(e_1,\ldots,e_d\) for its coordinate vectors. For \(u=\sum_{i=1}^{6}u_i e_i\), define two eight-element sets
\[
A=\{0,e_1,\ldots,e_7\},\qquad
B_u=\{0,e_1,\ldots,e_6,e_7+u\},\qquad
h=\sum_{i=1}^{6}u_i.
\]
An *orthogonal Walsh spectrum* of an eight-point set \(E\subset G\) means an unordered eight-element frequency subset \(\Lambda\subset G\) whose eight characters \(x\mapsto(-1)^{\lambda\cdot x}\), restricted to \(E\), are a mutually orthogonal basis of \(\mathbb C^E\). Frequency sets are counted as actual subsets, without quotienting by translation or automorphisms.

**Theorem.** The exact number of frequency sets which are orthogonal Walsh spectra of **both** \(A\) and \(B_u\) is
\[
\boxed{
\#\big(\operatorname{Spec}(A)\cap\operatorname{Spec}(B_u)\big)
=2^{8(d-7)}
\begin{cases}
480,&h=0,\\
96,&h\in\{3,4\},\\
0,&h\in\{1,2,5,6\}.
\end{cases}}
\]
Each individual set always has \(480\,2^{8(d-7)}\) spectra. Thus changing only one vertex of an affine simplex can eliminate all common orthogonal exponential bases, or leave exactly one fifth of them, according to the displacement weight.

## Assumptions and scope

All vector spaces, pairings, weights, and sums in this theorem are over the two-element field. The coordinate-disjoint hypothesis \(u\in\operatorname{span}(e_1,\ldots,e_6)\) guarantees that both supports are affinely independent eight-point sets. The Hamming weight \(h\) lies between zero and six. Orthogonality uses the unnormalized counting inner product on each support; each restricted character has squared norm eight, so eight mutually orthogonal characters automatically form a basis. The theorem is about *simultaneous* exact spectra, not general Fourier frames, arbitrary weighted supports, or all pairs of eight-point subsets.

## Proof

**1. Orthogonality becomes a weight-four condition.** First work in \(G=\mathbb F_2^7\). For \(v=(v_1,\ldots,v_7)\), the Walsh transform of \(1_A\) is
\[
W_A(v)=\sum_{a\in A}(-1)^{v\cdot a}
=1+\sum_{j=1}^7(-1)^{v_j}=8-2\operatorname{wt}(v).
\]
Hence \(W_A(v)=0\) exactly when \(\operatorname{wt}(v)=4\). Two distinct frequencies \(\lambda,\mu\) are orthogonal on \(A\) if and only if \(W_A(\lambda+\mu)=0\). Translating the frequency set does not alter this condition.

**2. All eight-frequency spectra of \(A\) are affine simplex codes.** Suppose that \(\Lambda\) is a spectrum, and translate one of its points to the origin. Write its remaining elements as \(v_1,\ldots,v_7\). Then all seven have weight four, and each \(v_i+v_j\) has weight four for distinct indices. Let \(T_i\subset\{1,\ldots,7\}\) be the three-element complement of the support of \(v_i\). The identity
\[
\operatorname{wt}(v_i+v_j)=8-2|\operatorname{supp}(v_i)\cap\operatorname{supp}(v_j)|=4
\]
forces \(|T_i\cap T_j|=1\). The seven distinct triples contain \(7\binom 32=21\) coordinate pairs, no pair repeated; hence every pair lies in exactly one triple. They form the unique Steiner triple system on seven points, the Fano plane.

For completeness, uniqueness follows by relabeling any line as \(123\): the two other lines through point \(1\) can be called \(145\) and \(167\); those through point \(2\) must cross the displayed pairs, and can be called \(246\) and \(257\); the remaining two lines are forced to be \(347\) and \(356\). This incidence structure is isomorphic to the seven nonzero vectors of \(\mathbb F_2^3\), with lines \(\{a,b,a+b\}\).

Arrange these seven distinct nonzero three-vectors as columns of a \(3\times7\) binary matrix \(M\). Every nonzero row combination of \(M\) is one on exactly four columns; its three zeros are a Fano line. Thus \(\{0,v_1,\ldots,v_7\}\) equals the three-dimensional row space \(L\) of \(M\). Conversely, every such row space has seven nonzero words of weight four and every coset is an orthogonal Walsh spectrum of \(A\).

There are \(7!\) ways to arrange the distinct nonzero columns of \(\mathbb F_2^3\), and two arrangements give the same row space exactly when their rows differ by an invertible \(3\times3\) binary matrix. Therefore the number of distinct such subspaces is
\[
\frac{7!}{|\mathrm{GL}(3,2)|}
=\frac{5040}{(2^3-1)(2^3-2)(2^3-2^2)}=30.
\]
Every such \(L\) has \(2^{7-3}=16\) cosets, giving exactly \(30\cdot16=480\) spectra of \(A\).

**3. The mutation selects a Hamming-code orthogonality condition.** The two supports differ only at one vertex. For each \(v\in\mathbb F_2^7\),
\[
W_{B_u}(v)=W_A(v)+(-1)^{v_7+v\cdot u}-(-1)^{v_7}.
\]
On a nonzero word \(v\in L\), the first term is zero, and the remaining difference vanishes precisely if \(v\cdot u=0\). Therefore a coset of \(L\) is a simultaneous spectrum of \(A\) and \(B_u\) if and only if \(u\in L^\perp\). Once \(L\) is admissible, all its sixteen cosets are admissible.

The dual \(L^\perp\) is the binary \([7,4,3]\) Hamming code associated with the seven nonzero columns of \(M\). A vector of weight \(j\) belongs to it exactly when its chosen \(j\) distinct columns sum to zero. There is one word of weight zero, no words of weight one or two, and exactly seven words of weight three: every two distinct nonzero columns determine their third and each triple is counted three times. The sum of all seven nonzero columns is zero, so complementing these seven weight-three words gives seven weight-four words and the all-ones weight-seven word. The complete weight enumerator is thus
\[
1+7z^3+7z^4+z^7.
\]
In particular the allowed displacement weights within the first six coordinates are zero, three and four.

**4. Exact incidence counts.** For \(u=0\), all thirty subspaces qualify. For a nonzero fixed \(u\) of weight three, each of the thirty dual codes contains exactly seven weight-three vectors. The permutation group on the seven coordinates acts transitively on the \(\binom73=35\) weight-three vectors and permutes the thirty codes, so each such vector lies in exactly
\[
\frac{30\cdot7}{\binom73}=6
\]
code duals. The same argument applies to weight four, using the seven complementary codewords and \(\binom74=35\). Every other nonzero weight in \(\{1,2,5,6\}\) lies in none. Multiplication by sixteen cosets per qualifying subspace yields \(480\), \(96\), and \(0\), respectively.

**5. Higher ambient dimension.** For \(d>7\), let \(\pi:\mathbb F_2^d\to\mathbb F_2^7\) retain the first seven frequency coordinates. The supports lie entirely in the first seven spatial coordinates, so restrictions of characters depend only on \(\pi(\lambda)\). Two frequencies in an orthogonal eight-character family cannot have the same projection, since their restrictions would then coincide. Thus every simultaneous spectrum projects bijectively onto one in \(\mathbb F_2^7\). Conversely, each of its eight frequency points can be lifted independently by any of the \(2^{d-7}\) kernel vectors, giving exactly \(2^{8(d-7)}\) different eight-point frequency sets. The same factor applies to each individual spectrum count, proving the theorem for all \(d\ge7\).

## Verification

The standalone file `CHECK.py` uses integer-only arithmetic. It constructs every three-dimensional binary length-seven subspace whose seven nonzero words have weight four, finds precisely thirty, generates the full collection of 480 translated spectra, and checks their Walsh orthogonality directly. It tests both supports for each of the 64 possible displacement vectors and every projected spectrum, making 860,160 eight-character-pair tests. It also independently checks the incidence profile over all 128 seven-bit vectors. The executable reports:

`CHECK_OK subspaces=30 spectra=480 mutations=64 direct_pair_tests=860160 incidence_vectors=128`

These finite computations confirm the dimension-seven base classification and incidence constants. The proof, not the enumerations, supplies the classification of all possible spectra and the theorem in every ambient dimension.

## Relationship to prior work

Kadowaki's 2026 work proves spectrality/tiling for eight-element binary sets and constructs spectra for affine-independent supports; it does not enumerate the intersection of the spectra of two one-vertex-related eight-point supports. Ferguson and Iosevich's 2026 work establishes binary Fuglede's conjecture in dimension eight and proves stronger tiling-complement existence statements, but the inspected results do not give this pairwise common-spectrum count. Published results on simultaneous three- or four-point binary spectra and an eight-point spectral census in the four-dimensional Boolean cube have different cardinalities or ambient affine ranks. The Fano-plane and Hamming-code ingredients are classical; the claimed result is the exact simultaneous compatibility classification and number of distinct spectra under this seven-dimensional one-vertex perturbation.

## Limitations

This does not classify common spectra for arbitrary pairs of eight-point subsets, nor bases with weights or non-Walsh characters. The count is for distinct unordered frequency subsets without equivalence identification. Even a complete search of accessible indexed literature cannot rule out an older equivalent formulation of this specialized Fano-plane incidence fact. The theorem has undergone a self-review, not an independent mathematical audit or publication-priority certification.

## References

1. A. Kadowaki, *Fuglede's conjecture holds in \(\mathbb F_2^7\)*, arXiv:2610.24022, first public posting 2026-10-16, especially Lemma 2.4 and Theorem 3.1. https://arxiv.org/abs/2610.24022
2. S. J. Ferguson and J. Iosevich, *Fuglede's conjecture holds in eight dimensions over the field with two elements*, arXiv:2610.36417, first public posting 2026-10-26, especially Sections 2–4. https://arxiv.org/abs/2610.36417
3. *Linearization and exact multiplicity of simultaneous four-point Walsh spectra*, publicly indexed mathematical finding, 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-linearization-and-exact-multiplicity-of-simultaneous-four-point--171a2694aaac
4. *Exact Walsh-spectrum multiplicities for eight-point subsets of the Boolean four-cube*, publicly indexed mathematical finding, 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-walsh-spectrum-multiplicities-for-eight-point-subsets-of-t--b981e436a3b1
