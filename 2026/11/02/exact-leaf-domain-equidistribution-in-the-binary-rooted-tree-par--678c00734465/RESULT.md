# Exact leaf-domain equidistribution in binary rooted-tree partial automorphisms

## Finding
Let \(B_n=\{0,1\}^n\). For every \(n\geq0\) and every fixed \(S\subseteq B_n\), the number of root-preserving partial automorphisms whose domain has terminal-vertex set exactly \(S\) is
\[
F_n(S)=2^{2^n-1}-\mathbf 1_{\{S=\varnothing\}}.
\]
In particular, the full terminal-domain rank polynomial is
\[
H_n(t)=2^{2^n-1}(1+t)^{2^n}-1.
\]
The result counts each **specified set**, not only its cardinality: different subsets, even when they are not equivalent under rooted-tree automorphisms, have identical counts whenever they are nonempty.

Write \(b=2^n\), \(c=2^{b-1}\), \(N=c2^b-1\), and let \(S_n\) be the terminal-domain subset of a uniformly chosen partial automorphism. The exact probability is
\[
\mathbb P(S_n=S)=\frac{c-\mathbf1_{\{S=\varnothing\}}}{N}.
\]
Conditional on \(S_n\ne\varnothing\), it is uniform over the \(2^b-1\) nonempty subsets. If \(U_n\) is an independent fair-coin subset of \(B_n\), then
\[
d_{\mathrm{TV}}(\mathcal L(S_n),\mathcal L(U_n))
=\frac{2^b-1}{2^b(c2^b-1)}.
\]
Consequently, with \(R_n=|S_n|\),
\[
\frac{R_n-b/2}{\sqrt b/2}\ \xrightarrow[n\to\infty]{\mathrm d}\ \mathcal N(0,1),\qquad
\frac{R_n}{b}\xrightarrow[n\to\infty]{\mathbb P}\frac12.
\]
This describes the number of **defined terminal vertices**, not the ultimate rank or count of nonzero eigenvalues.

## Assumptions and scope
For each integer \(n\ge0\), let \(T_n\) have vertex set all binary words of lengths at most \(n\), root the empty word, and edges between a word and its one-letter extensions. A rooted subtree must contain the root and be closed under taking prefixes. An element of \(\mathcal P_n\) is a rooted graph isomorphism from one such subtree to another; composition is the usual partial-map composition. The domain and image are nonempty (each contains the root). A subtree is permitted to omit every vertex on the bottom level. A partial automorphism can therefore have terminal-domain rank zero without having an empty underlying domain. All assertions above are valid for every \(n\ge0\).

## Proof
Define \(C_n\) as the common count for a nonempty specified terminal-domain subset and \(Z_n\) as the count for the empty subset. At height zero there is just the root identity, so \(C_0=1\) and \(Z_0=0\).

Assume for height \(n-1\) that \(Z=C-1\), where \(C=C_{n-1}\). Every element at height \(n\) is uniquely determined by a partial bijection between selected first-level children (two choices of each side) and by one height-\(n-1\) partial rooted isomorphism for each selected domain child. There are respectively \(1,4,2\) first-level partial bijections of ranks \(0,1,2\). The domain's prescribed bottom-level subset splits into left and right halves.

If both halves are empty, top rank zero contributes one element, rank one contributes \(4Z\), and rank two contributes \(2Z^2\). Therefore
\[
Z_n=1+4Z+2Z^2=2C^2-1.
\]
If exactly one half is nonempty, top rank one contributes \(2C\) (either image child), while top rank two contributes \(2CZ\) (either child permutation, with the other subtree morphism terminal-empty). Hence
\[
F_n(S)=2C+2CZ=2C^2.
\]
If both halves are nonempty, the top permutation must have rank two, with two possibilities and \(C\) choices per active child. Thus
\[
F_n(S)=2C^2
\]
again. It follows that \(C_n=2C_{n-1}^2\) and \(Z_n=C_n-1\). The initial value \(C_0=1\) solves to \(C_n=2^{2^n-1}\), proving the exact subset formula for all \(n\).

Summing over the \(\binom{2^n}{k}\) subsets of size \(k\) gives the displayed polynomial. Normalization yields \(N=\sum_S F_n(S)=c2^b-1\). Comparison of its probabilities against the uniform distribution on all \(2^b\) subsets gives the displayed exact total-variation distance (the single empty-subset deficit has absolute magnitude \((2^b-1)/(2^b N)\); all other subsets have equal compensating surpluses). Since this distance tends to zero and an independent fair subset has binomial size \(\operatorname{Bin}(b,1/2)\), the classical binomial central limit theorem and law of large numbers transfer to \(R_n\).

The binary hypothesis is sharp in this form. For a \(d\)-ary rooted tree of height one, fixing a nonempty leaf subset of size \(k\) leaves \((d)_k=d!/(d-k)!\) possible injections of its children into the \(d\) image children. At \(d=3\), this is \(3\) for \(k=1\) but \(6\) for \(k=2\), so the subset equidistribution statement fails.

## Verification
The self-contained `verify.py` independently enumerates every rooted prefix-closed domain subtree for heights \(n=0,1,2,3\), assigns a canonical unordered rooted-tree shape to each, counts isomorphic image subtrees, and weights each image by the domain shape's rooted automorphism-group order. It does not use the two-child count recurrence above to obtain the tested distribution. It checks **every** terminal-leaf bitmask, the total count, and the rank histogram, reporting `VERIFY_OK`. At heights \(0,1,2,3\), the total numbers of maps are respectively \(1,7,127,32767\). The finite checks corroborate, but are not substitutes for, the induction that covers every height.

## Relationship to prior work
Kochubinska's 2007 study of partial wreath powers established the semigroup construction, idempotent counting, and structural Green-relation machinery. Kochubinska's 2018 study of the binary tree established the total number of elements and **the sum of their terminal-domain ranks**, as well as a spectral concentration theorem; these known results are not claimed here. The June 28, 2020 preprint studies regular rooted-tree partial automorphisms and the vanishing proportion of nonzero eigenvalues. The additional assertion here is a **set-resolved count for every specified terminal subset**, its collapsed binomial polynomial and exact near-independent fair-subset law. Summing or differentiating this polynomial recovers previously known total and first-moment formulas. The limiting half-density of *defined* leaves complements the previously established spectral result, but there is no contradiction because terminal-domain size and ultimate rank are different invariants.

## Limitations
The result is for rooted partial isomorphisms whose nonempty domain and image are prefix-closed subtrees; it does not cover arbitrary partial injections of all tree vertices. The equidistribution phenomenon fails for branching degree three and higher at the first nontrivial height. The finite verifier covers heights only through three; the unrestricted statement rests on the displayed induction. A pre-existing identity deduced from the known shape-by-shape Green-class formulas might give equivalent coverage under different terminology, so the literature comparison is not independent publication-priority certification.

## References
1. E. Kochubinska, “Combinatorics of partial wreath power of finite inverse symmetric semigroup \(\mathcal{IS}_d\),” *Algebra and Discrete Mathematics* (2007), 49–61; freely available at https://arxiv.org/abs/2006.15564.
2. E. Kochubinska, “Spectral properties of partial automorphisms of a binary rooted tree,” *Algebra and Discrete Mathematics* 26(2) (2018), 280–289; https://admjournal.luguniv.edu.ua/index.php/adm/article/download/532/pdf.
3. E. Kochubinska, “Spectrum of partial automorphisms of regular rooted tree,” arXiv:2006.15558v1, first posted June 28, 2020; https://arxiv.org/abs/2006.15558 (published subsequently in *Semigroup Forum* 103 (2021), 567–574).
