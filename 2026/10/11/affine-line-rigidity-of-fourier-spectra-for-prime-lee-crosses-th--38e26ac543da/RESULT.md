# Affine-line rigidity of Fourier spectra for prime Lee crosses through thirteen

## Finding
For each \(p\in\{5,7,11,13\}\), put \(d=(p-1)/2\) and define the radius-one Lee cross
\[
 A=\{0,\pm e_1,\dots,\pm e_d\}\subset \mathbb F_p^d.
\]
Every Fourier spectrum \(B\subset\mathbb F_p^d\) for the counting-measure space \(\ell^2(A)\) is an affine line
\[
 B=b+\mathbb F_p u,\qquad
 \{0,\pm u_1,\dots,\pm u_d\}=\mathbb F_p.
\]
Conversely, every line of that form is a spectrum. The complete numbers of distinct spectra, in the order \(p=5,7,11,13\), are
\[
 10,\quad392,\quad5622144,\quad1425765120.
\]
In dimension six at \(p=13\), compatible *partial* orthogonal character families need not lie on a line; the rigidity emerges only when the full family contains thirteen characters.

## Assumptions and scope
All arithmetic below is in the prime field \(\mathbb F_p\), and the four listed primes are the entire domain of the classification. Standard basis vectors in \(\mathbb F_p^d\) are denoted by \(e_j\). For \(b\in\mathbb F_p^d\), the character on \(A\) is
\[
 \chi_b(x)=\exp(2\pi i\langle b,x\rangle/p).
\]
A *Fourier spectrum* of \(A\) is a set of exactly \(p=|A|\) distinct vectors \(B\) whose restricted characters are pairwise orthogonal. Their equal squared norms \(p\) then make them an orthogonal basis. The result counts frequency sets \(B\), not ordered bases or bases modulo translation.

## Proof
**Fourier zero set.** Let \(\zeta=\exp(2\pi i/p)\) and \(\Phi_p(z)=1+z+\cdots+z^{p-1}\). For \(u\in\mathbb F_p^d\),
\[
 F_A(u)=\sum_{x\in A}\chi_u(x)
      =1+\sum_{j=1}^d(\zeta^{u_j}+\zeta^{-u_j}).
\]
The right side is a polynomial in \(\zeta\) with \(p=2d+1\) nonnegative integral terms, counted with multiplicity. Since \(\Phi_p\) is the minimal polynomial of \(\zeta\) over \(\mathbb Q\), \(F_A(u)=0\) holds precisely when the occurrence count of each residue in \(\mathbb F_p\) equals one. Hence the nonzero Fourier zero set is
\[
 D_p=\bigl\{u:\{0,\pm u_1,\ldots,\pm u_d\}=\mathbb F_p\bigr\},
 \qquad |D_p|=2^d d!.
\]
The group of signed coordinate permutations preserves \(D_p\) and acts transitively on it. Every nonzero scalar multiple of an element of \(D_p\) also belongs to \(D_p\).

**Reduction to one exact graph.** Orthogonality is equivalent to \((B-B)\setminus\{0\}\subset D_p\). Translate any spectrum to include \(0\), choose any second point \(u\in D_p\), and apply a signed coordinate permutation to normalize
\[
 u=(1,2,\ldots,d).
\]
All remaining \(p-2\) points must belong to
\[
 V_p=\{v\in D_p:v-u\in D_p\}.
\]
Define the finite simple graph \(\Gamma_p\) with vertex set \(V_p\), joining distinct vertices \(v,w\) if and only if \(v-w\in D_p\). The remaining frequency points form a clique of size \(p-2\). The \(p-2\) vectors
\[
 R_p=\{2u,3u,\ldots,(p-1)u\}
\]
constitute such a clique.

**Exhaustive exact certificate.** The standalone `checker.py` constructs \(D_p\) from every permutation of \(1,\ldots,d\) and every independent sign choice, enumerates \(V_p\) and each integer-modular graph edge, and exhaustively enumerates all *maximal* cliques using the standard Bron--Kerbosch pivot recursion. Its complete exact-integer certificate is:

| \(p\) | \(|D_p|\) | \(|V_p|\) | Graph edges | Maximal clique-size multiplicities |
|---:|---:|---:|---:|---|
| 5 | 8 | 3 | 3 | \(\{3:1\}\) |
| 7 | 48 | 5 | 10 | \(\{5:1\}\) |
| 11 | 3840 | 69 | 156 | \(\{2:120,9:1\}\) |
| 13 | 46080 | 319 | 926 | \(\{1:24,2:324,3:225,5:42,11:1\}\) |

The recursion is finite and exhaustive: every candidate vertex is placed in the growing clique or moved to the excluded set, and a leaf is recorded exactly when neither a candidate nor an excluded vertex can extend it. The pivot only removes branches that would be covered by an extending neighbour; it cannot omit a maximal clique. In each of the four verified graphs, there is exactly *one* maximal clique of size \(p-2\), and no larger one. As \(R_p\) is such a clique, it is the unique possible completion. Therefore every normalized spectrum is \(\{0,u,2u,\ldots,(p-1)u\}\). Undoing the normalization gives exactly the stated affine lines.

Conversely, differences of two distinct points of any stated affine line are nonzero multiples of a vector in \(D_p\), hence all character inner products vanish. The \(p\) characters are therefore a basis. Every direction comprises \(p-1\) vectors in \(D_p\), and each one-dimensional direction has \(p^{d-1}\) distinct affine translates. The count is consequently \(2^d d!\,p^{d-1}/(p-1)\), giving the four displayed integers.

**A local-versus-global distinction.** At \(p=13\), the three vectors
\[
 a=(1,2,3,4,5,6),\quad b=(2,4,7,10,8,1),\quad
 c=(5,10,6,2,4,12)
\]
all lie in \(D_{13}\), and all three pairwise differences lie in \(D_{13}\); yet \(b\notin\mathbb F_{13}a\). Thus \(\{0,a,b,c\}\) is a noncollinear pairwise orthogonal four-character family, demonstrating that the full-spectrum assertion is stronger than pairwise/triple collinearity.

## Verification
Run `python3 checker.py` using Python 3.10 or later; the script has no nonstandard dependencies. The four graph profiles, direction counts, affine spectrum totals, and the noncollinear local example are tested with `assert` statements; the final line is `CHECK_PASS`. The exact counts concern exhaustively listed finite graphs; they are not statistical sampling. The argument does not extrapolate to other primes. The self-contained code is part of this result and is required for the enumerative certificate.

## Relationship to prior work
Kiss, D. Matolcsi, M. Matolcsi, and Somlai formulate finite-group spectrality and prove general ray structure for Fourier zero sets (their Section 2); their results do not, as stated, classify every spectrum for the fixed radius-one Lee crosses considered here. Iosevich, Kolountzakis, Lyubarskii, Mayeli, and Pakianathan connect spectral pairs with finite Gabor orthonormal bases; that implication also does not enumerate all Fourier bases for this family. The new distinction is exact *all-spectrum* rigidity, including the noncollinear local compatibility at thirteen and the four exact enumeration counts. General existence of a linear spectrum is elementary and is not claimed as new.

## Limitations
No conclusion is asserted for primes larger than thirteen, for nonprime rings, or for differently shaped Lee balls. The proof relies on a transparent exhaustive finite computation for four specific primes. Prior-work comparisons are bounded by examined accessible literature and cannot exclude an obscure equivalent classification in coding-theory or finite-Hadamard sources. Independent mathematical audit has not been performed.

## References
1. G. Kiss, D. Matolcsi, M. Matolcsi, G. Somlai, *Tiling and weak tiling in \((\mathbb Z_p)^d\)*, arXiv:2212.05513v1, first posted 11 December 2022, https://arxiv.org/abs/2212.05513.
2. A. Iosevich, M. Kolountzakis, Yu. Lyubarskii, A. Mayeli, J. Pakianathan, *On Gabor Orthonormal Bases Over Finite Prime Fields*, manuscript dated 27 December 2017, https://eigen-space.org/ps/gaborzp.pdf (public posting date not verified).
