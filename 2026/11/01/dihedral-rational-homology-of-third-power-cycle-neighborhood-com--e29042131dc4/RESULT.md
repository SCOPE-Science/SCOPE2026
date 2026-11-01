# Dihedral rational homology of third-power cycle neighborhood complexes

## Finding
For every integer \(n\geq13\), let \(G_n=C_n^3\) have vertex set \(\mathbb Z/n\mathbb Z\), where two distinct vertices are adjacent if their cyclic distance is at most three. Let \(K_n=\mathcal N(G_n)\) be the **open** Lovász neighborhood complex: a nonempty set is a simplex precisely when its vertices have a common graph neighbor. Let \(D_n=\langle r,s\mid r^n=s^2=1,\;srs=r^{-1}\rangle\) act by \(r(i)=i+1\) and \(s(i)=-i\).

The complete rational homology action is as follows. In degree zero there is one trivial line. For every \(n\), degree-one homology is one line, with \(r\) acting as \(+1\) and \(s\) as \(-1\). If \(n\) is odd, all homology in degrees at least two vanishes over \(\mathbb Q\). If \(n\) is even, precisely two more one-dimensional rational homology groups occur:

\[
\begin{array}{c|cc}
 &r&s\\\hline
H_1(K_n;\mathbb Q)&+1&-1\\
H_2(K_n;\mathbb Q)&-1&-1\\
H_3(K_n;\mathbb Q)&-1&+1
\end{array}
\]

All other rational homology groups vanish. In particular, for even \(n\), the traces of \(sr^j\) on degrees two and three are respectively \((-1)^{j+1}\) and \((-1)^j\). The ordinary symmetry quotients satisfy
\[
\widetilde H_k(|K_n|/D_n;\mathbb Q)=0\quad\text{for every }k,
\qquad
H_k(|K_n|/\langle r\rangle;\mathbb Q)=
\begin{cases}\mathbb Q,&k=0,1,\\0,&k\ge2.\end{cases}
\]
No integral or homotopy equivalence is asserted for these orbit spaces.

## Assumptions and scope
The graph is simple, the neighborhoods exclude their center, the complex includes all nonempty subsets of each six-vertex neighborhood, and \(n\geq13\). The action is the natural dihedral action, regardless of whether other automorphisms are considered. Homology and representation characters use rational coefficients. A quotient is the **ordinary geometric orbit space**, not the Borel construction.

## Proof
**1. Uniform simplicial collapse.** Write \(N(i)=i+\{-3,-2,-1,1,2,3\}\). Every face lies in some \(N(i)\) and has a unique lift to a cyclic interval of length at most six when \(n\geq13\). The original face orbit counts by dimensions zero through five are \((1,6,14,14,6,1)\), so its face vector is \(n(1,6,14,14,6,1)\).

The file `verify.py` specifies ten consecutive translation-orbit pairs \((A,B)\) of a codimension-one free face and its unique coface. Applying their \(n\) translates in the prescribed order removes exactly \(10n\) pairs and leaves a three-dimensional simplicial subcomplex \(L_n\) whose face vector is \(n(1,6,10,5)\). Each free-face assertion follows from a **finite local identity**, not extrapolation from samples: any coface containing vertex zero belongs to one of only six neighborhoods \(N(c)\), where \(c\in\{-3,-2,-1,1,2,3\}\). Their possible vertices lie among the thirteen distinct integer offsets \(-6,\ldots,6\), which remain distinct modulo every \(n\geq13\). Hence testing the prescribed ten pairs against this fixed local incidence system proves the assertions for all \(n\geq13\). Translations preserve that test. The verifier explicitly checks the system and also replays the complete collapse for every \(13\le n\le25\) as corroboration.

**2. Exact periodic boundary computation.** Put \(R=\mathbb Q[t,t^{-1}]\), where \(t\) denotes cyclic translation of an oriented face. Use the unique short-arc ordering of each face as its orientation. After the collapse, one translated representative per face orbit gives a free \(R\)-chain complex with module ranks \((1,6,10,5)\). The representative sets in dimensions one, two, and three, as sorted offset tuples starting at zero, are precisely:

\[
\begin{aligned}
E={}&\{01,02,03,04,05,06\},\\
T={}&\{012,015,016,023,024,025,026,034,045,056\},\\
U={}&\{0126,0156,0234,0245,0256\}.
\end{aligned}
\]
Here, for example, \(0256\) means the ordered face \((0,2,5,6)\), not a base-ten integer. For any ordered representative \(S=(a_0,\ldots,a_d)\), with \(a_0=0\), its oriented boundary is reconstructed by deleting each \(a_i\), translating the remaining face so its minimum becomes zero, multiplying by \(t^{\min(S\setminus\{a_i\})}\), and including sign \((-1)^i\). This determines all three matrices \(D_1,D_2,D_3\) without unstated conventions. The verifier constructs them and checks \(D_1D_2=D_2D_3=0\) identically as polynomial matrices.

Their Smith factors over the PID \(R\) are
\[
D_1:\ (t-1),\qquad D_2:\ (1,1,1,1,1,0),\qquad D_3:\ (1,1,1,1,t+1).
\]
The crucial exact certificates (with **zero-based matrix indices**) are: a \(5\times5\) minor of \(D_2\) with rows \((1,2,3,4,5)\) and columns \((0,1,2,3,4)\) has determinant \(-1\); a \(4\times4\) minor of \(D_3\) with rows \((0,1,3,5)\) and columns \((0,1,2,3)\) has determinant \(-1\); \(D_3\) has rank four at \(t=-1\); and its \(5\times5\) minor using rows \((0,3,5,8,9)\) and all columns equals \(-(t+1)\). Also the entries of \(D_1\) generate the ideal \((t-1)\). These facts prove the Smith statements, since \(D_1D_2=0\) forces \(\operatorname{rank}D_2\le5\).

It follows that the periodic free \(R\)-complex has homology \(R/(t-1)\) in degree zero and \(R/(t+1)\) in degree two, and no other homology. To obtain the finite complex, tensor the free chain complex with \(R/(t^n-1)\). The universal-coefficient short exact sequence for tensoring a free complex over this PID gives the claimed rational homology: \(t-1\) divides \(t^n-1\) for all \(n\), whereas \(t+1\) divides it exactly when \(n\) is even. Translation acts as \(t=+1\) in degree one and \(t=-1\) in degrees two and three (when present).

**3. Reflection on first homology.** A simplex has a unique short cyclic arc of width at most six. The affine barycentric average of its lifted vertex positions, reduced modulo \(n\), consistently defines a continuous map \(f:|K_n|\to\mathbb R/n\mathbb Z\). It intertwines rotations with translations and reflections with reversal. The edge loop \((0,1),(1,2),\ldots,(n-1,0)\) lies in the complex and maps with winding number one. Hence \(f_*\) is nonzero on first homology, and since that group is one-dimensional over \(\mathbb Q\), \(s\) acts by \(-1\).

**4. Reflection traces in higher degrees.** For any face orbit represented by an integer-offset set \(S\subset[0,6]\) with minimum zero and maximum \(m\), a reflection \(sr^j\) can preserve a translated copy only if \(S=m-S\); the translation coordinate must solve \(2i\equiv j-m\pmod n\). If such a solution exists, the fixed simplex contributes sign \((-1)^{q(q-1)/2}\) in chain degree \(q-1\), from reversal of its \(q\) vertices. This gives an exhaustive symbolic trace enumeration from the 42 original face-orbit templates. In chain degrees zero through five, the results are:

\[
\begin{array}{c|rrrrrr|r}
 &C_0&C_1&C_2&C_3&C_4&C_5&L\\\hline
n\text{ odd}&1&-6&-2&4&0&-1&2\\
n\text{ even},\ j\text{ even}&2&-6&-4&6&0&-2&0\\
n\text{ even},\ j\text{ odd}&0&-6&0&2&0&0&4
\end{array}
\]

Here \(L\) is the alternating cellular-chain trace, equal to the homological Lefschetz number. For even \(n\), the already established degree-zero and degree-one traces contribute two to \(L\), leaving \(\chi_2(sr^j)-\chi_3(sr^j)=L-2\). Each remaining character is a sign, so the two reflection cases uniquely give \((-1,+1)\) and \((+1,-1)\), respectively, in degrees two and three. This proves the complete character.

**5. Quotients.** For a finite group acting on a finite simplicial complex, barycentric subdivision removes inversions and rational averaging identifies ordinary quotient homology with invariant rational homology. The characters above yield only degree-zero invariants for \(D_n\), and exactly degree-zero and degree-one invariants for \(\langle r\rangle\), completing the proof.

## Verification
Run `python verify.py` in the package directory (Python 3 and SymPy required). It reconstructs the complete simplicial complexes for \(13\le n\le25\), checks every claimed free-face orbit removal, reconstructs all polynomial boundary matrices from the residual face templates, verifies the stated exact minors and polynomial chain identities, and checks the symbolic reflection trace sums. The recorded execution in `verification_output.txt` concludes `DIHEDRAL_HOMOLOGY_CHARACTER_VERIFY_OK`. The universal claims rest on the explicit local-incidence and PID arguments above; finite replays alone would not establish them.

## Relationship to prior work
Kozlov's 2005 work establishes a general simple-homotopy relation between Lovász neighborhood complexes and graph Hom complexes, not these dihedral characters. Adamaszek, Adams, Frick, Peterson, and Previte-Johnson (2014) determine dihedral homology actions for nerves of circular arcs, whose homotopy types have positive rational homology in at most one degree. This does not cover the even-\(n\) complexes here, which have nonzero rational homology in degrees one, two, and three. Shukla's 2018 preprint treats maximum-degree-three graphs and four-regular circulants; \(C_n^3\) is six-regular. A separate publicly indexed note entitled *Third-power cycle neighborhood complexes collapse to parity-twisted sphere bundles* gives a nonequivariant bundle classification with the same size reduction; this account does **not** claim novelty for that collapse or for ordinary Betti numbers. Its indexed statement does not give the dihedral character or quotient homology; full-text priority comparison with that note remains incomplete. Other studies of three-cut complexes of cycle powers concern different simplicial complexes.

## Limitations
Only the natural dihedral action, rational homology and ordinary orbit spaces are classified; integral torsion, integral representation lattices, equivariant Borel homology and quotient homotopy types are not. The threshold \(n\ge13\) is essential to the present short-arc proof; smaller cycles are unclassified here. No statement about definitive publication priority or independent validation is made.

## References
1. D. N. Kozlov, *Simple homotopy types of Hom-complexes, neighborhood complexes, Lovász complexes, and atom crosscut complexes*, first arXiv submission 2005-03-28, arXiv:math/0503613, https://arxiv.org/abs/math/0503613 .
2. M. Adamaszek, H. Adams, F. Frick, C. Peterson, C. Previte-Johnson, *Nerve complexes of circular arcs*, arXiv first posted 2014-10-16, arXiv:1410.4336, https://arxiv.org/abs/1410.4336 .
3. S. Shukla, *Homotopy type of the neighborhood complexes of graphs of maximal degree at most 3 and 4-regular circulant graphs*, arXiv first posted 2018-02-13, arXiv:1802.04526, https://arxiv.org/abs/1802.04526 .
4. *Third-power cycle neighborhood complexes collapse to parity-twisted sphere bundles*, publicly indexed 2026-10-11, published-finding corpus published research record `5e7bfbfa5a7e`; available record summary, full-text not retrievable during this comparison.
