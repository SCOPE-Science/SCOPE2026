# Sharp generating radius after deleting a Fano line

## Finding
Let \(\mathcal L\) denote the seven lines of the Fano plane, and delete any line \(e_0\). For each of the six remaining lines \(e\), choose arbitrary strictly positive real coefficients \(\theta_{e,v}>0\) for \(v\in e\) satisfying \(\sum_{v\in e}\theta_{e,v}=1\). The real operator
\[
G:\ell_\infty^7(\mathbb R)\longrightarrow\ell_\infty^6(\mathbb R),\qquad (Gx)_e=\sum_{v\in e}\theta_{e,v}x_v
\]
has norm \(1\) and sharp quantitative generating radius
\[
\boxed{\rho(G)=\frac35.}
\]
After restoring the deleted line, with any strictly positive normalized coefficients, the corresponding seven-row operator has generating radius \(1\). Both values are independent of all strictly positive row weights and of the deleted line.

## Assumptions and scope
Write \(B=[-1,1]^7\) and \(\operatorname{att}(G)=\{x\in B:\|Gx\|_\infty=1\}\). Define the maximal generating radius by
\[
\rho(G)=\max\{r\in[0,1]:rB\subseteq\operatorname{conv}(\operatorname{att}(G))\}.
\]
For finite-dimensional domains this agrees with the supremal \(r\)-generating constant in Definition 2.2 and Corollary 2.6 of Kadets–Martín–Merí–Quero (2023). All spaces and operators are **real**. Strict positivity, rather than nonnegativity, of every coefficient is assumed.

For an explicit model identify the seven points with \(V=\{1,2,3,4,5,6,7\}\), the nonzero binary three-vectors written as integers under bitwise XOR. The lines are \(\{a,b,a\mathbin{\mathrm{xor}}b\}\) with distinct \(a,b\in V\):
\[
123,\quad145,\quad167,\quad246,\quad257,\quad347,\quad356.
\]
Here a three-digit string denotes an unordered triple of point labels, not an integer-valued parameter. We remove \(123\); all other removals are equivalent under invertible binary-linear changes of coordinates.

## Proof
**1. Norm-attaining vertices.** Since every row is a strictly positive convex average, \(\|G\|=1\) (apply it to the all-one vector). For \(x\in B\), a row has modulus \(1\) if and only if all three coordinates on its line equal \(+1\), or all equal \(-1\). Consequently, the norm-attainment set is a union of cube faces, and its convex hull equals \(K=\operatorname{conv}(S)\), where
\[
S=\{\sigma\in\{-1,1\}^7:\text{one of the six retained triples is monochromatic under }\sigma\}.
\]
This description is independent of the values of the positive row coefficients.

**2. An exact support function.** Let \(a\in\mathbb R^7\) with \(\sum_{v\in V}|a_v|=1\). For a triple \(e\), put
\[
P_e(a)=\sum_{v\in e}\max(a_v,0),\qquad
N_e(a)=\sum_{v\in e}\max(-a_v,0),\qquad
\delta(a)=\min_{e}\min\{P_e(a),N_e(a)\},
\]
where the minimum is over the six retained triples. Maximizing \(a\cdot\sigma\) over sign vertices constant on one fixed triple \(e\) gives
\[
\sum_{v\notin e}|a_v|+\Big|\sum_{v\in e}a_v\Big|
=1-2\min\{P_e(a),N_e(a)\}.
\]
Taking the maximum over triples therefore gives \(h_K(a)=1-2\delta(a)\). Since \(rB\subseteq K\) exactly when \(rh_B(a)\le h_K(a)\) for every \(a\), and \(h_B(a)=\sum|a_v|\),
\[
\rho(G)=1-2\max_{\sum|a_v|=1}\delta(a).
\tag{1}
\]
This is a finite-dimensional support-function identity, with no unverified limiting step.

**3. Classify the relevant two-colourings.** If \(\delta(a)>0\), the signs of all nonzero \(a_v\), with arbitrary signs on zero entries, give a colouring in which none of the six retained triples is monochromatic. The three matchings on \(\{4,5,6,7\}\) paired with points \(1,2,3\) are respectively
\[
M_1=\{45,67\},\qquad M_2=\{46,57\},\qquad M_3=\{47,56\}.
\]
Suppose, up to colour exchange and relabelling these three matchings, that points \(1,2\) have colour \(+\) and point \(3\) has colour \(-\). The \(+\)-coloured leaves must be an independent set in the four-cycle \(M_1\cup M_2\), yet must meet both pairs of \(M_3\) to prevent a \(-\)-monochromatic retained triple. This is impossible: an independent set in that four-cycle has size at most two, and a size-two independent set is exactly one pair of \(M_3\). Thus the three points on the deleted line have a common colour.

Suppose that common colour is \(+\). The \(+\)-coloured leaves then form an independent set in \(M_1\cup M_2\cup M_3=K_4\); hence at most one of the four leaves is \(+\). Reversing colours gives the complete classification: the deleted triple is monochromatic, and either all four other points have the opposite colour or exactly one of them shares its colour.

**4. Bound and attain the mass separation.** Write \(b_v=|a_v|\) and \(d=\delta(a)>0\).

If all four leaves oppose the deleted triple, each of the three base points belongs to a retained line in which it is the sole point of its sign, so \(b_1+b_2+b_3\ge3d\). Every retained line has two opposite-coloured leaves. As each leaf appears on exactly three retained lines, summing the six opposite-colour mass constraints gives \(3(b_4+b_5+b_6+b_7)\ge6d\); thus the leaf mass is at least \(2d\). Therefore \(1\ge5d\), or \(d\le\frac15\).

If exactly one leaf, say point \(4\), shares the base colour, then each base point belongs to a retained line avoiding point \(4\), giving \(b_i\ge d\) for \(i=1,2,3\). Each of the other three leaves occurs with point \(4\) in one retained line and is the sole opposite-coloured point there, giving \(b_j\ge d\) for \(j=5,6,7\). Hence \(1\ge6d\), so \(d\le\frac16\). For sign patterns having a monochromatic retained triple, \(d=0\). Consequently \(\delta(a)\le\frac15\) for every normalized \(a\).

Equality is achieved by the explicit functional
\[
a_1=a_2=a_3=\frac15,\qquad a_4=a_5=a_6=a_7=-\frac1{10}.
\]
Its \(\ell_1\)-norm is \(1\), and every retained triple has positive and negative mass exactly \(\frac15\). Thus \(\max\delta(a)=\frac15\), and (1) yields \(\rho(G)=\frac35\).

**5. Restore the line.** The colouring classification in Step 3 shows that every cube sign vertex that was not norm-attaining for the six-line operator is monochromatic on the deleted line. Restoring that line makes every cube vertex norm-attaining. Their convex hull is \(B\), so the restored operator is \(1\)-generating. The general deleted-line case follows from transitivity of the invertible binary-linear group on Fano lines.

## Verification
The accompanying standalone `fano_radius_exact_check.py` uses exact rational arithmetic and enumerates all \(128\) cube sign vectors. It confirms that precisely \(10\) avoid all six monochromatic retained triples, that \(118\) are norm-attaining, that all \(128\) become norm-attaining when the seventh line is restored, and that the explicit norm-one supporting functional has support value \(\frac35\). It also checks the two colouring classes, all seven possible deletions, and representative strictly positive rational row weights. Run with `python3 fano_radius_exact_check.py`. The proof above—not finite sampling—establishes the statement for every strictly positive choice of real row weights.

## Relationship to prior work
Kadets, Martín, Merí and Quero introduced quantitative generating operators and proved that, in finite dimensions, \(r\)-generation is equivalent to inclusion of a scaled unit ball in the convex hull of the norm-attainment set (Definition 2.2 and Corollary 2.6). That general criterion does not evaluate the six-line Fano invariant. Keevash and Sudakov record the classical edge-critical non-two-colourability of the Fano plane: deleting any line permits a proper two-colouring. Their combinatorial observation yields the qualitative loss of full generation but does not imply the exact residual radius \(\frac35\). The related graph-edge averaging classification applies to two-vertex edges; the Fano rows have three strictly positive coordinates and cannot be reduced to that claim by relabelling coordinates.

## Limitations
The theorem concerns real \(\ell_\infty\) spaces, Fano incidences, and strictly positive normalized coefficients. It does not classify arbitrary hypergraphs or allow signed or zero coefficients. Exact full generation for the complete Fano plane and the qualitative edge-criticality are classical; the claimed contribution is the sharp quantitative constant and its weight-independence after one deletion. This work has not undergone independent external scientific validation.

## References
1. V. Kadets, M. Martín, J. Merí, A. Quero, *Generating operators between Banach spaces*, arXiv:2306.02645v1, first public 2023-06-05, especially Definition 2.2 and Corollary 2.6. https://arxiv.org/pdf/2306.02645
2. P. Keevash and B. Sudakov, *The Turán number of the Fano plane*, Combinatorica 25 (2005), 561–574; Section 5 records edge-critical two-colourability. https://people.maths.ox.ac.uk/keevash/papers/fano-journal.pdf
