# Sharp incidence-matching fault threshold for graph-state entanglement on even-order projective planes

## Finding

**Theorem (exact matching-fault law).** Let \(\Pi\) be any finite projective plane of even order \(q\ge2\), including a non-Desarguesian plane when such a plane exists. Write \(\mathcal P\) and \(\mathcal L\) for its points and lines, with \(v=q^2+q+1\) members in each class. Make the pure qubit graph state \(\lvert G_\Pi\rangle\) by preparing \(\lvert+\rangle\) at each of its \(2v\) vertices and applying a controlled-\(Z\) gate across each incidence \(p\in\ell\). Let \(F\) be any matching of omitted incidence gates of size \(k\), with \(0\le k\le q+1\). Denote its point and line endpoint sets by \(P(F)\subset\mathcal P\) and \(L(F)\subset\mathcal L\), respectively.

Then the von Neumann entropy and *every* positive-order Rényi entropy, in bits, between the full point and line registers are equal, and their common value is

\[
S(F)=\operatorname{rank}_{\mathbb F_2}(N)+k-\epsilon(F),
\]

where \(N_{p\ell}=1\) if \(p\in\ell\), and

\[
\epsilon(F)=
\begin{cases}
1,&k=q+1\text{ and }\bigl[P(F)\text{ is a projective line}\ \text{or } L(F)\text{ is a full point-pencil}\bigr],\\
0,&\text{otherwise}.
\end{cases}
\]

Thus every omission matching of up to \(q\) bonds adds exactly one entanglement bit per missing bond. At precisely \(q+1\) missing bonds, geometric alignment of *either* endpoint class loses one of those gains. Both gains \(q\) and \(q+1\) occur in every even-order projective plane.

For \(\Pi=\operatorname{PG}(2,2^a)\), the previously known binary incidence rank yields

\[
\operatorname{rank}_{\mathbb F_2}N=3^a+1,
\]

so the exact entropy is explicit. For example, the baseline and possible critical entropies are \(4\) and \(6,7\) at \(q=2\); \(10\) and \(14,15\) at \(q=4\); and \(28\) and \(36,37\) at \(q=8\).

## Assumptions and scope

The projective plane has its usual axioms: every line contains \(q+1\) points; every point lies on \(q+1\) lines; distinct points determine one line; distinct lines meet once. Only \(q\) even is used in the geometric threshold classification. No coordinatization or transitivity of automorphisms is assumed there. A matching means that the omitted incidences have *distinct point endpoints and distinct line endpoints*. All gates are ideal controlled-\(Z\) operations, and every unomitted incidence gate is applied exactly once. The measured quantity is entropy across the fixed entire point-versus-line bipartition; no claim concerns entanglement among arbitrary smaller subsystems. The baseline rank is left as the exact matrix rank for arbitrary even-order planes; the separate closed formula is asserted only in the Desarguesian case.

## Proof

**1. Stabilizer cut reduction.** For a pure bipartite graph state, the reduced state on either side has a flat nonzero Schmidt spectrum of size \(2^{r}\), where \(r\) is the binary rank of the across-cut adjacency submatrix. This standard stabilizer fact, already established in [1], shows that all positive-order Rényi entropies and the von Neumann entropy equal \(r\) bits. Because omitted controlled-\(Z\) gates toggle the corresponding incidences, the present cut submatrix is \(N+UV^T\) over \(\mathbb F_2\), where the \(k\) columns of \(U\) and \(V\) are the respective distinct coordinate vectors of the matched endpoints.

**2. Minimum-weight binary incidence words, including their equality cases.** The column space \(C=\operatorname{im}N\) and row space \(C^*=\operatorname{im}N^T\) both have minimum nonzero Hamming weight \(q+1\). Their only words of weight exactly \(q+1\) are respectively incidence vectors of entire lines and of full point-pencils. This classical type of code statement is credited to the projective-geometry coding literature [2]; here it follows directly for every even-order plane. Indeed, in characteristic two, \(N^TN=\mathbf1\mathbf1^T\): off-diagonal entries are one because two distinct lines meet once, and diagonal entries are one because \(q+1\) is odd. Thus for \(0\ne c=Nz\), every projective line intersects its support in parity \(\sum z\). If this parity is even, choose a point in the support; each of its \(q+1\) lines needs a distinct additional support point, hence the weight is at least \(q+2\). If the parity is odd, choose a point outside the support; its \(q+1\) lines partition the support into nonempty sets, hence the weight is at least \(q+1\). If equality holds, every line through any exterior point meets the support in exactly one point. The line through any two support points can therefore have no exterior point, and so the support is exactly an entire projective line. Such a line is indeed a binary codeword (a column of \(N\)). Duality proves the statement for \(C^*\), with a full point-pencil as its minimum word. The all-ones support is not an exception: its weight is \(v>q+1\).

**3. Rank perturbation through the cokernel.** Let \(r=\operatorname{rank}N\). Choose invertible row and column transformations taking \(N\) to \(\operatorname{diag}(I_r,0)\), and write their transforms of \(U,V\) as upper and lower blocks \(U_1,U_2\) and \(V_1,V_2\). Block elimination in the usual augmented matrix gives the exact identity

\[
\operatorname{rank}(N+UV^T)-r
=\operatorname{rank}\begin{pmatrix}0&U_2\\V_2^T&I_k+V_1^TU_1\end{pmatrix}-k.
\]

The kernel of \(U_2\), as a map on \(\mathbb F_2^k\), consists exactly of coefficient vectors whose selected point-support is a word of \(C\). The kernel of \(V_2\) similarly consists of selected line-support words in \(C^*\). For \(k\le q\), both lower blocks have full rank \(k\) by Step 2. The displayed block matrix then has rank \(2k\), and the gain is exactly \(k\).

At \(k=q+1\), each lower block has either rank \(k\) or rank \(k-1\). The latter happens for \(U_2\) exactly when the selected points form a projective line \(\ell_0\), and for \(V_2\) exactly when the selected lines form a point-pencil at \(p_0\). The one-dimensional kernel in each deficient case is generated by \(\mathbf1_k\). If exactly one lower block is deficient, the block matrix has rank \(2k-1\); if neither is, its rank is \(2k\).

When **both** are deficient, its rank is \(2k-2+\delta\), with

\[
\delta=\mathbf1_k^T(I_k+V_1^TU_1)\mathbf1_k
=1+N_{p_0\ell_0}\pmod2.
\]

The second identity follows because the two endpoint indicator vectors are \(N e_{\ell_0}\) and \(N^T e_{p_0}\); the inverse pivot transformations in the pairing cancel. The matching constraint forces \(p_0\notin\ell_0\): if \(p_0\) lay on \(\ell_0\), every other point of \(\ell_0\) would lie on no line of the pencil except \(\ell_0\), preventing an injective incidence pairing of \(q+1\) endpoints. Hence \(\delta=1\), the block matrix has rank \(2k-1\), and even simultaneous alignment gives exactly one fewer bit than the generic gain. These cases prove the asserted iff law.

**4. Both threshold values occur.** Choose a projective line \(\ell\) and a point \(z\notin\ell\). For each point \(p\in\ell\), omit its incidence with the unique line joining \(p\) to \(z\). This is a matching of size \(q+1\) whose point endpoints are collinear and whose line endpoints concur at \(z\); its gain is \(q\). To produce gain \(q+1\), take any \(q\) of the points of \(\ell\), matched to their distinct join lines to \(z\), and add an incidence \((p_*,\ell_*)\) with \(p_*\notin\ell\) and \(\ell_*\) passing through \(p_*\) but not through \(z\). The selected point set contains an exterior point and \(q\) collinear points (hence is not a projective line), and the selected lines comprise \(q\) lines through \(z\) and one not through \(z\) (hence are not a pencil). The gain is \(q+1\). This works already for \(q=2\), since two lines through \(z\) and a third line not through \(z\) cannot form a pencil through a different point.

**5. Desarguesian baseline.** For \(q=2^a\), regard nonzero triples in \(\mathbb F_q^3\) as projective points, with dual triples for lines. The complementary incidence matrix \(M=\mathbf1\mathbf1^T+N\) has entries \((a\cdot x)^{q-1}\in\mathbb F_2\). In characteristic two,

\[
(a_0x_0+a_1x_1+a_2x_2)^{q-1}
=\prod_{j=0}^{a-1}\bigl(a_0^{2^j}x_0^{2^j}+a_1^{2^j}x_1^{2^j}+a_2^{2^j}x_2^{2^j}\bigr).
\]

Expanding yields exactly \(3^a\) distinct monomial pairs, each with coefficient one. The corresponding degree-\(q-1\) homogeneous monomials are linearly independent as functions on projective triples: they have individual degrees less than \(q\), so a polynomial relation vanishing on all projective points would vanish on all of \(\mathbb F_q^3\), contrary to elementary polynomial interpolation. Their counterpart evaluation vectors on dual triples are also independent. Thus \(\operatorname{rank}_{\mathbb F_2}M=3^a\), using invariance of the rank of a binary matrix under field extension. Every column of \(M\) has even weight \(q^2\), but the all-ones vector has odd weight \(v\). Moreover, \(N\mathbf1=\mathbf1\) and \(M\mathbf1=0\), so \(\operatorname{im}N=\operatorname{im}M\oplus\langle\mathbf1\rangle\). Hence \(\operatorname{rank}N=3^a+1\).

## Verification

`VERIFY.py` independently constructs normalized projective points and dual lines over binary extension fields for \(q=2,4,8,16\), forms the point-by-line incidence matrix, and calculates ranks by binary elimination. It tests the formula directly from toggled incidence matrices. For \(q=2\), it enumerates **every** incidence matching with \(0\le k\le3\): counts by size are \(1,21,168,644\). For \(q=4\), it tests \(2{,}000\) sampled matchings; for \(q=8\), \(350\); and for \(q=16\), \(45\). Explicit constructions of *both* critical outcomes are checked in all four planes. The baseline ranks obtained are \(4,10,28,82\). The exact output is in `verification_output.json`. Run `python3 VERIFY.py` with Python 3's standard library; deterministic random seeds are used. These are finite checks only; Steps 1–4 prove the theorem for **every** even-order projective plane, and Step 5 proves the Desarguesian baseline for every \(a\ge1\).

## Relationship to prior work

Hein, Eisert and Briegel [1] establish the graph-state cut-rank law and general edge deletion bounds, including that a single edge changes entanglement by at most one bit. These are the starting tools, not new results. Bagchi and Narasimha Sastry [2] provide a geometric proof for minimum words of Desarguesian projective geometry codes, citing earlier discovery by Smith and Delsarte and collaborators. The weight/distance characterization is also not claimed as new; an elementary proof above extends the needed case to every even-order plane. Cautrès and collaborators [3], in Section 4.2, study point-line incidence graphs of projective planes as graph-state resources for entanglement generation and prove pairability properties. Their inspected result is not an exact entropy response to deleting a *matching* of preparation gates. Here the combined all-plane placement classification at the sharp threshold, including the collinear/pencil iff and simultaneous-alignment case, is the assessed contribution. None of the inspected sources is claimed to prove its historical uniqueness.

## Limitations

This is a zero-noise pure-state assertion about *omission* of ideal controlled-\(Z\) gates with distinct endpoints. It does not address repeated-endpoint fault sets, measurements, decoherence, other bipartitions, arbitrary finite incidence structures, or more than \(q+1\) missing gates. For non-Desarguesian even-order planes, the theorem determines the exact entropy **shift** relative to the original binary incidence rank but does not supply a universal closed baseline formula. The combinatorial equivalence of the claim to a binary-rank perturbation makes undiscovered specialized coding or matrix-theory antecedents a historical originality risk; independent validation is not asserted.

## References

1. M. Hein, J. Eisert, H. J. Briegel, *Multi-party entanglement in graph states*, arXiv:quant-ph/0307130 (first posted 18 July 2003), especially Sections III.2 and III.3, https://arxiv.org/abs/quant-ph/0307130 .
2. B. Bagchi and N. S. Narasimha Sastry, *Minimum weight words of binary codes associated with finite projective geometries*, Discrete Mathematics 57 (1985), 307–310; full accessible text https://repository.ias.ac.in/1009/1/1-s2.0-0012365X85901839-main.pdf .
3. C. Cautrès, A. Claudet, M. Mhalla, S. Perdrix, J. Savin, S. Thomassé, *Vertex-minor universal graphs for generating entangled quantum subsystems*, arXiv:2402.06260, especially Section 4.2, https://arxiv.org/abs/2402.06260 .
