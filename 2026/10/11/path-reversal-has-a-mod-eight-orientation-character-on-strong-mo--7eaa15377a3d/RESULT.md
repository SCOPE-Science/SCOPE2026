# Path reversal has a mod-eight orientation character on strong Morse matching complexes

## Finding

Let \(P_n\) be the graph with vertices \(v_0,\dots,v_n\) and edges \(v_iv_{i+1}\), for every integer \(n\geq 1\). Let \(X_n=\mathcal{SM}(P_n)\) be the **full strong discrete Morse matching complex** of Knudson and Owens–White, not its pure subcomplex and not the ordinary discrete Morse complex. Let \(r\) be the simplicial involution induced by reversing the path, \(v_i\mapsto v_{n-i}\). The complete representation of \(\langle r\rangle\cong C_2\) on reduced rational homology is:

\[
\widetilde H_j(X_n;\mathbb Q)\cong
\begin{cases}
\mathbb Q_{(-1)^k},&n=4k,\ k\geq1,\ j=2k-1,\\
\mathbb Q_{(-1)^{k+1}},&n=4k+1,\ k\geq0,\ j=2k,\\
0,&\text{otherwise}.
\end{cases}
\]

Here \(\mathbb Q_{\lambda}\) is the one-dimensional rational representation on which \(r\) acts by the scalar \(\lambda\in\{+1,-1\}\). Equivalently, path reversal acts by \(-1\) in the nonzero homology group exactly for \(n\equiv1,4\pmod8\), and acts by \(+1\) exactly for \(n\equiv0,5\pmod8\). The remaining congruence classes have zero reduced homology. In particular, the rational reduced homology of the quotient \(X_n/\langle r\rangle\) is nonzero precisely when \(n\equiv0,5\pmod8\); in that case it is one-dimensional in the degree displayed above.

## Assumptions and scope

A vertex of \(X_n\) is a vertex-edge incidence of \(P_n\). Following the source's numbering, the right-directed incidence on the edge from \(v_i\) to \(v_{i+1}\) is numbered \(2i\), and the left-directed incidence is numbered \(2i+1\), for \(0\leq i<n\). Thus the involution is exactly
\[
r(2i)=2(n-1-i)+1,\qquad r(2i+1)=2(n-1-i).
\]

A face can be encoded as a length-\(n\) word over \(\{>,<,-\}\), where the two arrow symbols specify the two possible incidence vertices for an edge, and \(-\) specifies that neither is present. The empty face is included in augmented simplicial chains, although it is not a geometric point of \(X_n\). A word represents a face if and only if it contains neither of the contiguous subwords \(<>\) and \(<->\). This follows from the explicit forbidden-pair characterization of \(X_n\) in Knudson–Owens–White, Theorem 10.6, and also follows by taking downward closure of their valid direction strings from Definition 6.4. In particular, imposing the even-dash-run condition on **every face** rather than only on generating matchings would be incorrect.

No restriction on the parity of \(n\) is imposed. The boundary case \(n=1\) has two isolated vertices; \(n=2,3\) have contractible complexes. Coefficients are \(\mathbb Q\); no assertion about equivariant homotopy type or integral-module splitting is made.

## Proof

**1. Nonequivariant concentration.** Proposition 6.2 and Theorem 6.6 of Knudson–Owens–White prove that \(X_{4k}\simeq S^{2k-1}\) for \(k\geq1\), \(X_{4k+1}\simeq S^{2k}\) for \(k\geq0\), and \(X_{4k+2}\) and \(X_{4k+3}\) are contractible. This determines the degree and dimension of reduced homology but does not determine the action of \(r\).

**2. Classifying setwise fixed faces.** Reversal swaps the two incidences on a reflected edge. A reversal-invariant face therefore has no individually fixed vertices and consists of \(a\) transposition pairs, so it has \(2a\) vertices. If \(n\) is odd, reversal fixes the middle edge but interchanges its two incidence vertices; both cannot occur in one face, forcing the middle symbol to be a dash. Write \(h=\lfloor n/2\rfloor\). Every invariant word is uniquely of the form
\[
p\,\bigl(-\text{ if }n\text{ is odd, otherwise nothing}\bigr)\,\operatorname{reverse}(\operatorname{swap}(p)),
\]
where \(p\) has length \(h\), and \(\operatorname{swap}\) interchanges \(>\) and \(<\) and fixes \(-\). It is a face precisely when \(p\) avoids \(<>\) and \(<->\) and, if nonempty, does not end in \(<\). Indeed, the two prohibited patterns internal to each half correspond under reversal, and the only newly forbidden pattern across the center is \(<>\) for even \(n\), or \(<->\) for odd \(n\), both occurring exactly when \(p\) ends in \(<\).

**3. Signed augmented Lefschetz count.** On the ordered vertices of any invariant nonempty face, reversal permutes \(a\) pairs, so its orientation sign is \((-1)^a\). The face has dimension \(2a-1\), hence contributes \(-(-1)^a\) to the reduced Lefschetz number. The empty augmented face contributes \(-1\). Therefore, letting \(\mathcal P_h\) be the set of allowed half-words just described and letting \(a(p)\) count their arrow symbols,
\[
\widetilde L(r;X_n)=-S_h,\qquad S_h=\sum_{p\in\mathcal P_h}(-1)^{a(p)}.
\]
This is an equality of alternating traces on augmented simplicial chains and hence of alternating traces on reduced homology; no freeness of the action is required.

**4. Exact transfer recurrence.** Among all words of length \(h\) avoiding the two forbidden patterns, define their signed sums \(A_h,B_h,C_h,D_h\) according to their endings: respectively \(>\), \(<\), \(<-\), and \(-\) not preceded by \(<\). Put the empty word in the fourth state, so \((A_0,B_0,C_0,D_0)=(0,0,0,1)\). Appending an arrow multiplies the weight by \(-1\), and appending a dash leaves it unchanged. The allowed transitions give
\[
\begin{aligned}
A_{h+1}&=-(A_h+D_h),\\
B_{h+1}&=-(A_h+B_h+C_h+D_h),\\
C_{h+1}&=B_h,\\
D_{h+1}&=A_h+C_h+D_h.
\end{aligned}
\]
The permitted half-words are those in states \(A,C,D\), so \(S_h=A_h+C_h+D_h\). The transitions imply \(S_{h+1}=B_h+C_h\), while \(B_h=-(S_{h-1}+B_{h-1})\) and \(C_h=B_{h-1}\) for \(h\geq1\). Consequently
\[
S_{h+1}=-S_{h-1},\qquad S_0=1,\qquad S_1=0.
\]
Thus \(S_{2k}=(-1)^k\) and \(S_{2k+1}=0\) for all \(k\geq0\). It follows that
\[
\widetilde L(r;X_{4k})=\widetilde L(r;X_{4k+1})=(-1)^{k+1},\qquad
\widetilde L(r;X_{4k+2})=\widetilde L(r;X_{4k+3})=0.
\]

**5. Extracting the one-dimensional character.** In the noncontractible cases, there is exactly one nonzero reduced rational homology group, in degree \(d=2k-1\) for \(n=4k\) and degree \(d=2k\) for \(n=4k+1\). Therefore \(\widetilde L(r)=(-1)^d\operatorname{tr}(r_*\mid \widetilde H_d)\). Substituting the preceding exact formula yields \((-1)^k\) and \((-1)^{k+1}\), respectively, as asserted. For a finite group acting simplicially, rational homology of its orbit space agrees with the invariant part of the rational homology of the original space (after barycentric subdivision), yielding the stated quotient consequence.

## Verification

The accompanying standalone Python 3 file `verify.py` checks the face language in two independent ways: it generates all full valid direction strings with even dash runs and takes their downward closure, and independently generates all words avoiding \(<>\) and \(<->\). These agree for \(1\leq n\leq11\). Direct signed simplicial Lefschetz traces for the same eleven sizes agree with both half-word enumeration and the recurrence. Exact augmented mod-two boundary ranks for \(1\leq n\leq10\) recover the cited nonequivariant homology pattern. Half-word enumeration agrees with the recurrence for \(1\leq n\leq24\), and the recurrence agrees with the closed formula for \(1\leq n\leq300\). Run `python3 verify.py` from the directory containing the file; expected first line is `VERIFY_OK`. The recurrence proof, rather than this finite enumeration, establishes the statement for all admissible \(n\).

## Relationship to prior work

Knudson and Owens–White, arXiv:2609.06844v1, introduced the full strong Morse matching complexes, provided the face characterization in their Definitions 6.3–6.4 and Theorem 10.6, and proved their nonequivariant homotopy types in Proposition 6.2 and Theorem 6.6. Those statements are prerequisites, not claimed as new. The additional result here is the **path-reversal action** on the unique reduced rational homology group, including its exact mod-eight sign, obtained from a signed fixed-face transfer recurrence. Chari and Joswig, arXiv:math/0011234v1, studied the larger ordinary discrete Morse complex of a graph and its pure part; their rooted-forest and path results concern a different complex and do not determine the strong-complex reversal character.

## Limitations

The conclusion is a rational \(C_2\)-module classification for the particular reversal automorphism of a path. It does not assert a canonical equivariant sphere model, determine integral equivariant extensions, describe arbitrary graph automorphisms, or compute the homology of other strong Morse families. Finite test cases only corroborate, rather than prove, the all-parameter recurrence. Published coverage was compared at the statement-and-implication level, but an unindexed independent derivation cannot be ruled out absolutely.

## References

1. Kevin P. Knudson and Abigail Owens–White, *Complexes of strong discrete Morse matchings*, arXiv:2609.06844v1 (first publicly posted 2026-09-06), especially Definition 4.2, Proposition 6.2, Definitions 6.3–6.4, Theorem 6.6, and Theorem 10.6. https://arxiv.org/pdf/2609.06844v1
2. Manoj K. Chari and Michael Joswig, *Discrete Morse Complexes*, arXiv:math/0011234v1 (2000), especially Sections 3–4. https://arxiv.org/pdf/math/0011234
