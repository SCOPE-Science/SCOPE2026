# The complete length spectrum of asymmetric binary dimension-five codes

## Finding

A full-support binary linear code of dimension \(5\) and length \(n\) has trivial coordinate-permutation automorphism group **if and only if**
\[
12\le n\le19.
\]
Every admissible length is witnessed by an explicit generator matrix described below. Here full support means no coordinate is identically zero. This statement concerns the existence of such codes, not the classification of all codes at each length.

## Assumptions and scope

The ambient field is \(\mathbb F_2\). A generator matrix of rank \(5\) has columns in \(\mathbb F_2^5\), and its code is the row space. Coordinate-permutation automorphisms are permutations of the \(n\) positions preserving this row space. A full-support code has no zero generator column. If two columns coincide, swapping them is a nonidentity automorphism; thus trivial automorphism forces the columns to form a subset \(S\) of the \(31\) nonzero vectors in \(\mathbb F_2^5\).

We encode the vector \((v_0,v_1,v_2,v_3,v_4)\) as the integer \(v_0+2v_1+4v_2+8v_3+16v_4\). In the code certificates below, lists of integers are therefore **literal column encodings**, not codewords. Write \(G=\operatorname{GL}(5,2)\). For a rank-five set of distinct columns, the coordinate-permutation automorphism group is isomorphic to its setwise stabilizer in \(G\): every code automorphism induces a unique invertible row operation and conversely.

## Proof

**Nonexistence below length \(12\).** If a subset \(S\) spans a proper subspace, a nonidentity invertible transformation can fix that subspace pointwise, so its stabilizer is nontrivial. We may therefore assume \(S\) spans \(\mathbb F_2^5\). The order of \(G\) is
\[
(31)(30)(28)(24)(16)=9{,}999{,}360.
\]
A subset with trivial stabilizer has a \(G\)-orbit of that size, but for \(5\le n\le8\), \(\binom{31}{n}\le\binom{31}{8}=7{,}888{,}725\). Thus such sets do not exist.

For \(n\in\{9,10,11\}\), choose five independent members of \(S\) and map them to the standard basis by a linear change of basis. Every possible set then appears among the subsets consisting of the five standard basis vectors plus \(n-5\) vectors selected from the other \(26\) nonzero vectors. The complete normalized counts are respectively \(14{,}950\), \(65{,}780\), and \(230{,}230\). The exhaustive algorithm in `verify_lower.cpp` checks all these sets and finds **zero** with trivial stabilizer. Its stabilizer test exhausts the images of the five basis vectors. It prunes only by necessary invertibility, image-membership, and pair-sum incidence conditions, so it omits no admissible automorphism.

**Existence for lengths \(12\) through \(15\).** Let \(S_n\) be the first \(n\) entries of the following ordered list for each \(n\in\{12,13,14,15\}\):

```text
1 2 4 8 16 3 5 6 9 14 18 25 17 22 24
```

Each \(S_n\) contains the standard basis, hence spans, and has distinct nonzero elements. The independent exhaustive program `verify_spectrum.py` considers **every** ordered image of the standard basis among the columns of \(S_n\), tests invertibility, and checks whether the induced linear transformation preserves the entire set. It finds exactly one, the identity, for each \(n\). This is a finite proof certificate of trivial stabilizers, not a probabilistic or incomplete search.

**Existence for lengths \(16\) through \(19\).** If a linear map preserves a subset \(S\) of the \(31\) nonzero binary five-vectors, it preserves its complement, and conversely. Consequently the setwise stabilizers of \(S\) and \(\mathbb F_2^5\setminus(S\cup\{0\})\) are identical. The complements of \(S_{15},S_{14},S_{13},S_{12}\) have sizes \(16,17,18,19\), respectively, and trivial stabilizers. They span \(\mathbb F_2^5\), because any proper subspace has at most \(15\) nonzero vectors. Thus they give rank-five full-support generator matrices.

**Nonexistence above length \(19\).** A full-support code with trivial automorphism cannot have repeated columns, so it has at most \(31\) columns. If its column set has \(n\ge20\) members, its complement among the \(31\) nonzero vectors has at most \(11\) members. The lower-length argument, including the proper-subspace case, shows that every such complement has a nontrivial \(G\)-stabilizer, which also stabilizes the original set. This rules out every \(n\ge20\). Together the four cases prove the claimed exact interval.

## Verification

Both embedded checkers were executed from their actual source files. Compile and run the exhaustive small-set checker with

```sh
g++ -std=c++17 -O3 verify_lower.cpp -o verify_lower
./verify_lower 9 11
```

It returns zero rigid normalized sets at each of the \(14{,}950\), \(65{,}780\), and \(230{,}230\) cases. Run the independent explicit-basis checker with

```sh
python3 verify_spectrum.py
```

It checks all ordered independent images of five basis vectors for each of the four witness sets and prints `VERIFY_OK`. The verification does not enumerate higher-dimensional binary codes and makes no inference from timeouts.

## Relationship to prior work

Haily and Harzalla (2015) study binary codes with trivial automorphism group, including the smallest such constructions and uniqueness of a smallest TAG-code. No new priority is claimed for the known length-twelve boundary. Li, Wang and Zhou (2026) establish asymptotic high-probability triviality for random linear codes under growing-dimension conditions; their theorem does not determine the **finite fixed-dimension** attainable-length spectrum. Bouyukliev, Bouyuklieva and Kurz (2020) give general code-classification algorithms and tabulate various parameter families, but do not state the sharp full-support dimension-five automorphism-free length interval. The present result combines a normalized obstruction, an explicit nested chain and the complementary-set duality to settle every possible length in this fixed dimension.

## Limitations

The theorem is specific to full-support **binary dimension-five** codes and the coordinate-permutation automorphism group. It does not assert a list of all inequivalent codes at each length, a general formula in dimension, or resistance to decoding attacks. If an identically zero coordinate is allowed, appending one zero coordinate to a rigid full-support code preserves its trivial automorphism group; the full-support hypothesis is therefore essential at the upper endpoint. A complete inspection of the 2015 journal article was not possible; an unindexed earlier statement of the same full length spectrum remains a literature risk. The exact computations are exhaustive only over the stated finite normalized sets and witness basis images.

## References

1. Xiaoru Li, Qi Wang, Yue Zhou, *The automorphism groups of random linear codes*, arXiv:2607.23936 (first submitted 2026-07-27), https://arxiv.org/abs/2607.23936.
2. Abdelfattah Haily and Driss Harzalla, *On Binary Linear Codes Whose Automorphism Group is Trivial*, Journal of Discrete Mathematical Sciences and Cryptography 18 (2015), 495–512, https://doi.org/10.1080/09720529.2014.927650.
3. Iliya Bouyukliev, Stefka Bouyuklieva, Sascha Kurz, *Computer classification of linear codes* (2020), https://doi.org/10.15495/EPub_UBT_00004618.
