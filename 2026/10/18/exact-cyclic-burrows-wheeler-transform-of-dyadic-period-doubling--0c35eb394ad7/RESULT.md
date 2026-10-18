# Exact cyclic Burrows–Wheeler transform of dyadic period-doubling words

## Finding
Let \(\theta\) be the binary substitution \(\theta(0)=01\), \(\theta(1)=00\), and let \(W_m=\theta^m(0)\) for every integer \(m\ge 0\). Work with the ordered alphabet \(0<1\). Let \(\operatorname{BWT}(w)\) mean the concatenation of the final letters of **all cyclic rotations** of \(w\), sorted lexicographically; no terminal symbol is adjoined. Define \(z_m=|W_m|_0\) and \(o_m=|W_m|_1\). For every \(m\ge0\),
\[
o_m=\frac{2^m-(-1)^m}{3},\qquad z_m=\frac{2^{m+1}+(-1)^m}{3}.
\]
Define the reverse-complement map \(R(w)=\overline{w^{\mathrm{rev}}}\) (reversal followed by interchanging \(0\) and \(1\)). Starting with \(T_1=1\), define for each \(m\ge2\)
\[
T_m=1^{o_{m-1}}0^{o_{m-1}}R(T_{m-1}).
\]
**Complete transform theorem:** for every integer \(m\ge1\),
\[
\operatorname{BWT}(W_m)=T_m0^{z_{m-1}}.
\]
Consequently the number \(r_m\) of maximal constant-letter runs in this transform is
\[
r_1=2,\qquad r_m=2m-2\quad(m\ge2).
\]
The recurrence determines the entire binary transform, not only its number of runs. For example, \(\operatorname{BWT}(W_4)=1110001001000000\), with six runs.

## Assumptions and scope
The claim concerns exactly the finite iterates \(W_m\) of the given substitution and the **cyclic-rotation** Burrows–Wheeler transform over \(0<1\). In particular, this is not the sentinel-terminated suffix transform or the transform of arbitrary prefix lengths. The empty-word and dimension-zero conventions do not enter the run formula; \(W_0=0\) serves only to determine the letter counts. Every factor and index in the proof is interpreted cyclically when it refers to rotations or neighboring symbols.

## Proof
**1. Counts and forbidden neighboring ones.** Each substituted block begins with \(0\), and its second letter is \(1\) exactly when its source letter is \(0\). Thus every cyclic adjacency in \(W_m\), \(m\ge1\), avoids \(11\), including the last-to-first adjacency. Moreover \(o_{m+1}=z_m=2^m-o_m\) with \(o_0=0\). Solving this recurrence gives the displayed closed forms for \(o_m,z_m\).

**2. Lexicographic block decomposition.** Fix \(m\ge2\) and put \(w=W_{m-1}\), of length \(N=2^{m-1}\). Index letters modulo \(N\). Write \(E_i\) and \(O_i\) for the rotations of \(\theta(w)\) starting at positions \(2i\) and \(2i+1\), respectively. They are
\[
E_i=0(1-w_i)0(1-w_{i+1})\cdots,\qquad O_i=(1-w_i)0(1-w_{i+1})0\cdots.
\]
Because \(11\) never occurs cyclically in \(w\), the rotations split into four **consecutive** lexicographic classes:
\[
\begin{array}{c|c|c}
\text{class}&\text{starting positions}&\text{common initial bits}\\
A&E_i\text{ with }w_i=1&0001\\
B&O_i\text{ with }w_i=1&0010\\
C&E_i\text{ with }w_i=0&01\\
D&O_i\text{ with }w_i=0&1.
\end{array}
\]
These prefixes give strictly the order \(A<B<C<D\). Within each class the relative order of its rotations is **the reverse** of the lexicographic order of the underlying rotations of \(w\): the substitution maps the first differing source symbol to its opposite at the first differing output position (and the same holds after the common one-position shift for odd starts). Equal rotations, if any, have equal preceding symbols and do not affect the transform.

**3. Letters preceding the rotations.** The letter preceding \(E_i\) in \(\theta(w)\) is \(1-w_{i-1}\), whereas the letter preceding \(O_i\) is always \(0\). Split \(\operatorname{BWT}(w)=P_0P_1\) after its first \(z_{m-1}\) letters, corresponding to rotations starting with \(0\); the remaining \(o_{m-1}\) letters correspond to rotations starting with \(1\). Since \(w\) has no cyclic \(11\), every rotation starting in \(1\) has preceding letter \(0\), so \(P_1=0^{o_{m-1}}\). Reading the preceding letters in the four classes \(A,B,C,D\) gives, in order,
\[
R(P_1),\quad 0^{o_{m-1}},\quad R(P_0),\quad 0^{z_{m-1}}.
\]
Thus
\[
\operatorname{BWT}(W_m)=1^{o_{m-1}}0^{o_{m-1}}R(P_0)0^{z_{m-1}}.
\]
The first three classes consist of exactly the rotations of \(W_m\) starting with \(0\), so their transform segment is the next \(P_0\). At \(m=1\), a direct two-rotation check gives \(\operatorname{BWT}(01)=10\), whose segment for zero-starting rotations is \(T_1=1\). Induction therefore identifies \(P_0=T_{m-1}\) and proves the complete-transform recurrence for every \(m\ge1\).

**4. Run count.** The recurrence gives \(T_2=100\), with two runs. For each \(m\ge2\), the first symbol of \(T_m\) is \(1\) and the last is \(0\) (the latter is the complement of the first symbol of \(T_{m-1}\)). Hence, for \(m\ge3\), the word \(R(T_{m-1})\) begins with \(1\). Concatenating \(1^{o_{m-1}}0^{o_{m-1}}\) before it adds exactly two runs; reversing and complementing by itself preserves run count. Thus \(r(T_m)=r(T_{m-1})+2\) for \(m\ge3\), with \(r(T_2)=2\), giving \(r(T_m)=2m-2\). The final suffix \(0^{z_{m-1}}\) merges with the already-zero last run of \(T_m\). The base transform \(10\) has two runs. This proves the stated formula.

## Verification
Run `python3 check_bwt.py` with a standard Python 3 installation. The included checker constructs \(W_m\) directly, forms the proposed transform recursively, and independently sorts its cyclic rotations via rank doubling for all \(1\le m\le13\) (lengths up to \(8192\)). For \(1\le m\le9\), a separate direct full-rotation lexicographic sort provides a second implementation. Every complete transform, length, terminal zero-block size, and stated run count agrees. These finite checks are cross-checks only: the all-dimensions statement follows from the preceding proof, not numerical extrapolation.

## Relationship to prior work
Brlek, Frosini, Mancini, Pergola, and Rinaldi (2019) determine the BWT of standard Thue–Morse words and other morphic families; their substitution \(0\mapsto01,1\mapsto10\) is distinct from the period-doubling substitution here. Frosini, Mancini, Rinaldi, Romana, and Sciortino (arXiv:2202.02609v1, February 2022) prove logarithmic **upper bounds** for binary purely morphic-word BWT run counts, but do not provide the full transform recurrence or this exact count. Fici, Romana, Sciortino, and Urbina (CPM 2023) study changes of BWT runs under morphisms and exhibit period-doubling-morphism sensitivity; their bounds for specially constructed input words do not give the BWT of its successive fixed-point prefixes. The general order-reversal principle for binary morphisms is consistent with Step 2, but does not alone settle the interleaving of even and odd rotation classes in Step 3.

## Limitations
This theorem is not an exact formula for sentinel-based BWT, other alphabets, or arbitrary finite prefixes of the infinite period-doubling word. It does not claim a universal run formula for arbitrary substitution images. Finite computational tests are cross-checks, not independent proof of the infinite theorem. An undiscovered equivalent BWT formulation or unindexed computation in the literature remains possible.

## References
1. S. Brlek, A. Frosini, I. Mancini, E. Pergola, S. Rinaldi, *Burrows–Wheeler Transform of Words Defined by Morphisms*, IWOCA 2019, DOI: 10.1007/978-3-030-25005-8_32; open manuscript: https://flore.unifi.it/retrieve/e398c380-dd2e-179a-e053-3705fe0a4cff/BWT-morphism_%20Last.pdf.
2. A. Frosini, I. Mancini, S. Rinaldi, G. Romana, M. Sciortino, *Logarithmic equal-letter runs for BWT of purely morphic words*, arXiv:2202.02609v1 (5 February 2022), https://arxiv.org/pdf/2202.02609.
3. G. Fici, G. Romana, M. Sciortino, C. Urbina, *On the Impact of Morphisms on BWT-Runs*, CPM 2023, DOI: 10.4230/LIPIcs.CPM.2023.10, https://drops.dagstuhl.de/opus/volltexte/2023/17964/pdf/LIPIcs-CPM-2023-10.pdf.
4. G. Romana et al., *Morphisms and BWT-Run Sensitivity*, MFCS 2025, DOI: 10.4230/LIPIcs.MFCS.2025.49, https://drops.dagstuhl.de/storage/00lipics/lipics-vol345-mfcs2025/html/LIPIcs.MFCS.2025.49/LIPIcs.MFCS.2025.49.html.
