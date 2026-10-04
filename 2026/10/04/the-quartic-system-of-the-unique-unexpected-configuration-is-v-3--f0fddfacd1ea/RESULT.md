# The quartic system of the unique unexpected configuration is \(V_{(3,1)}\oplus V_{(2,1,1)}\)
## Finding
Let
\[
Z=\{[-1:0:1],[0:-1:1],[1:0:1],[0:1:1],[0:0:1],[1:-1:0],[1:1:0],[0:1:0],[1:0:0]\}\subset\mathbb P^2_{\mathbb C}.
\]
This is the standard nine-point configuration underlying the unique unexpected quartic. Its full projective stabilizer is
\[
\operatorname{Aut}_{\mathbb P^2}(Z)\cong S_4.
\]
For the six-dimensional vector space \(I(Z)_4\) of quartics through \(Z\), the stabilizer representation decomposes as
\[
I(Z)_4\cong V_{(3,1)}\oplus V_{(2,1,1)},
\]
where \(V_{(3,1)}\) is the standard three-dimensional representation of \(S_4\) and \(V_{(2,1,1)}\cong V_{(3,1)}\otimes\operatorname{sgn}\). Explicitly, the two invariant summands are
\[
B=\langle xyz^2,xy^2z,x^2yz\rangle\cong V_{(3,1)}
\]
and
\[
A=\langle yz(y^2-z^2),xz(x^2-z^2),xy(x^2-y^2)\rangle\cong V_{(2,1,1)}.
\]
Thus \(I(Z)_4^{S_4}=0\), and there is no nonzero invariant subspace of dimension one or two. The character of \(I(Z)_4\), ordered by cycle types \(1,(12),(12)(34),(123),(1234)\), is \((6,0,-2,0,0)\).

## Assumptions and scope
The ground field is \(\mathbb C\). The configuration is used in the explicit coordinates above; these are the coordinates given in the lead paper and are the projectivized root directions of type \(B_3\). The assertion concerns the projective stabilizer of the finite set and its induced action on degree-four forms vanishing on that set. It does not assert a new classification of unexpected quartics: uniqueness of the projective configuration and existence of its unexpected quartic are prior results.

## Proof
The nine points are the projectivized directions of the type-\(B_3\) roots. Signed permutation matrices therefore stabilize \(Z\). Their group has order \(48\), and the scalar subgroup \(\{\pm I\}\) acts trivially on projective space, giving a projective subgroup of order \(24\).

The incidence structure supplies the matching upper bound. Among all lines spanned by pairs of points of \(Z\), exactly four contain three points and exactly three contain four points. The four three-rich lines have six distinct pairwise intersection points, all belonging to \(Z\), and no three of these four lines are concurrent. Any projective automorphism of \(Z\) must permute the four three-rich lines. This action is faithful: an element fixing all four lines fixes their six pairwise intersections, hence fixes a projective frame and is the identity. Therefore the full stabilizer injects into \(S_4\), so its order is at most \(24\). The signed-permutation subgroup already has order \(24\) projectively, proving \(\operatorname{Aut}_{\mathbb P^2}(Z)\cong S_4\).

Evaluation at the nine points has rank \(9\) on the fifteen-dimensional space of quartics, so \(\dim I(Z)_4=6\). Direct substitution shows that the six displayed quartics form a basis. Signed permutations preserve separately the spans \(A\) and \(B\). Computing traces on the five conjugacy classes of the induced permutation group on the four three-rich lines gives
\[
\chi_A=(3,-1,-1,0,1),\qquad \chi_B=(3,1,-1,0,-1).
\]
These are exactly the characters of \(V_{(2,1,1)}\) and \(V_{(3,1)}\). Their sum is \((6,0,-2,0,0)\), proving the claimed decomposition. Since neither irreducible constituent is trivial and they are nonisomorphic, there is no invariant line, invariant plane, or invariant quartic.

The scalar ambiguity in lifting a projective symmetry to \(\mathrm{GL}_3\) does not affect the conclusion: changing a lift by \(-I\) acts trivially in degree four, and tensoring all lifts by the sign character would only exchange the two three-dimensional constituents.

## Verification
The included `artifacts/verify.py` uses only the Python standard library and exact integer/rational arithmetic. It verifies the rank-nine evaluation matrix, the six displayed basis forms, the four three-rich and three four-rich lines, the six distinct pairwise intersections of the three-rich lines, all \(48\) signed permutation matrices and their \(24\) projective actions, the \(S_4\) cycle-type census, the total character \((6,0,-2,0,0)\), and the two constituent characters. Running `python3 artifacts/verify.py` prints `VERIFY_OK`.

## Relationship to prior work
Farnik--Galuppi--Sodomaco--Trok prove that this is, up to projective equivalence, the unique configuration admitting an unexpected quartic of degree four, and give the displayed point coordinates. Bauer--Malara--Szemberg--Szpond identify the same configuration with the \(B_3\) arrangement and record that the quartics through its nine points form a six-dimensional vector space. Di Marca--Malara--Oneto treat the same configuration in the theory of special line arrangements. Those inspected sources do not state the \(S_4\)-module character or the decomposition of \(I(Z)_4\) into its two three-dimensional irreducible constituents.

The identification of the projective symmetry group from the \(B_3\) model is structurally expected and is not presented here as the principal novelty. The new invariant is the exact representation carried by the degree-four interpolation space that supports the unexpected phenomenon.

## Limitations
The calculation is specific to the unique nine-point unexpected-quartic configuration and degree four. It does not classify stabilizer representations for higher-degree unexpected configurations, nor does it determine the stabilizer of an individual unexpected quartic obtained after imposing a general triple point. A residual literature risk remains that an equivalent representation-theoretic computation appears in root-system or arrangement literature under terminology not indexed by unexpected-quartic searches.

## References
1. Ł. Farnik, F. Galuppi, L. Sodomaco, W. Trok, *On the unique unexpected quartic in \(\mathbb P^2\)*, arXiv:1804.03590, DOI:10.1007/s10801-019-00922-6. First public version: 2018-04-10.
2. T. Bauer, G. Malara, T. Szemberg, J. Szpond, *Quartic unexpected curves and surfaces*, arXiv:1804.03610, DOI:10.1007/s00229-018-1091-3.
3. M. Di Marca, G. Malara, A. Oneto, *Unexpected curves arising from special line arrangements*, DOI:10.1007/s10801-019-00871-0.
