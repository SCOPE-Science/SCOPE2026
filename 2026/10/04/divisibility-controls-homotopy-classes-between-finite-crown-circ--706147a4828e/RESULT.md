# Divisibility controls homotopy classes between finite crown circle models

## Finding
For integers \(m,n\ge 2\), let \(\mathfrak C_r\) be the \(2r\)-point crown poset obtained from the infinite alternating fence by quotienting modulo \(2r\), and let \([\mathfrak C_m,\mathfrak C_n]\) denote unbased homotopy classes of continuous maps of the associated finite \(T_0\)-spaces. Every map has an integer winding degree \(d\) with \(|d|\le \lfloor m/n\rfloor\). For every nonextremal degree, meaning \(|d|<m/n\), all degree-\(d\) maps are homotopic. If \(n\nmid m\), these are all maps and
\[
\left|[\mathfrak C_m,\mathfrak C_n]\right|=2\left\lfloor\frac{m}{n}\right\rfloor+1.
\]
If \(n\mid m\), writing \(k=m/n\), each degree with \(|d|<k\) gives one homotopy class, while for each extremal degree \(d=\pm k\) there are exactly \(n\) maps and every one is isolated in the pointwise mapping poset. Equivalently, for all \(m,n\ge2\),
\[
\left|[\mathfrak C_m,\mathfrak C_n]\right|
=2\left\lfloor\frac{m-1}{n}\right\rfloor+1+2n\,\mathbf 1_{n\mid m}.
\]

## Assumptions and scope
For \(r\ge2\), write \(\mathfrak F\) for the infinite fence on \(\mathbb Z\), with \(2j<2j-1\) and \(2j<2j+1\), and define \(\mathfrak C_r=\mathfrak F/(2r\mathbb Z)\). Continuous maps between the corresponding finite \(T_0\)-spaces are exactly order-preserving maps. The winding degree is normalized so that a lift \(\widehat f:\mathfrak F\to\mathfrak F\) satisfies
\[
\widehat f(i+2m)=\widehat f(i)+2nd.
\]
Homotopy is unbased finite-space homotopy. Pointwise-comparable maps are homotopic, and the homotopy classes are the connected components of the comparability graph of the pointwise mapping poset.

## Proof
Choose a lift and put \(a_i=\widehat f(i)\) and \(\delta_i=a_{i+1}-a_i\). Order preservation gives \(\delta_i\in\{-1,0,1\}\). Whenever \(\delta_i\ne0\), the parity of \(a_i\) agrees with the parity of \(i\). Hence every zero run lying between nonzero increments has even length. Summing over one source period gives
\[
2nd=\sum_{i=0}^{2m-1}\delta_i,
\]
so \(|d|\le\lfloor m/n\rfloor\).

Two elementary finite-space homotopies control the cyclic increment word:
\[
(+1,-1)\longleftrightarrow(0,0),\qquad
(-1,+1)\longleftrightarrow(0,0),
\]
and
\[
(+1,0,0)\longleftrightarrow(+1,-1,+1)\longleftrightarrow(0,0,+1),
\]
with the sign-reversed analogue. Every arrow changes one source value through an adjacent comparable target value while preserving order. Thus zero pairs slide through unit steps, and opposite signs can be brought together and cancelled.

Repeated cancellation reduces every nonconstant degree-\(d\) map to a sign-pure word with exactly \(2n|d|\) unit increments of sign \(\operatorname{sgn}(d)\) and \(2m-2n|d|\) zeros. Degree zero reduces to a constant map; all constants are homotopic because the crown comparability graph is connected.

If \(|d|<m/n\), at least one zero pair remains. Sliding zero pairs gathers the zeros into one block. Moving one zero pair once through the cyclic block of unit increments changes the lift phase by two target vertices while returning the increment word to the same cyclic form. Iteration connects all \(n\) admissible phases. Hence every nonextremal degree gives exactly one class. A word with \(2n|d|\) unit increments followed by the remaining zeros realizes every integer degree in the stated range.

No zero remains exactly when \(n\mid m\) and \(|d|=m/n\). Then every increment has the same sign. There are exactly \(n\) choices for the image of one even source point, so there are \(n\) maps of each extremal sign. Each is isolated. Indeed, a strict pointwise increase could only move an even source coordinate to one of the two adjacent target maxima, which then destroys its required comparability with the other neighboring source maximum; the dual argument excludes a strict pointwise decrease. Counting the nonextremal degrees and the two extremal families gives the formula.

## Verification
The symbolic proof is parameter-uniform. The accompanying `verify.py` independently enumerates all order-preserving maps for \((m,n)=(2,3),(3,2),(3,3),(4,2),(4,3)\), computes winding degree from lifted increments, builds the finite-space homotopy graph by valid one-coordinate comparable moves, and compares connected components with the theorem. These checks include shorter-to-longer, unequal-size, diagonal, divisibility, nondivisibility, and higher-degree cases.

## Relationship to prior work
Barmak and Minian supply the archive-qualified finite-\(T_0\)-space/poset homotopy framework. Farley and Currie--Visentin enumerate order-preserving maps of fences and crowns, but the exposed statements are enumerative rather than homotopy classifications. Cavallo and Sattler define the same crown winding number and prove the shorter-to-longer zero-winding case; they do not give this all-\((m,n)\) homotopy classification.

Čukić and Kozlov classify connected components and homotopy types of graph-homomorphism complexes between ordinary cycle graphs. Their result has a related wrap-number/divisibility pattern, but graph homomorphisms cannot collapse an edge, while order-preserving crown maps can collapse comparable pairs. The argument above supplies the finite-space bridge: collapsed pairs can be created, slid, and cancelled by pointwise homotopies, while maximal winding is rigid.

## Limitations
The theorem classifies unbased homotopy classes, not the internal homotopy type of each full mapping-poset component. The graph-homomorphism analogy is a genuine residual originality risk, although the inspected graph theorem does not state the finite-space result or the collapse-and-slide bridge. The finite verifier checks representative cases only and is not the proof of the infinite parameter statement.

## References
1. J. A. Barmak and E. G. Minian, *Minimal Finite Models*, arXiv:math/0611156v1.
2. J. D. Farley, *The number of order-preserving maps between fences and crowns*, Order 12 (1995), 5--44, DOI:10.1007/BF01108588.
3. J. D. Currie and T. I. Visentin, *The number of order-preserving maps of fences and crowns*, Order 8 (1992), 133--142, DOI:10.1007/BF00383399.
4. S. L. Čukić and D. N. Kozlov, *The homotopy type of complexes of graph homomorphisms between cycles*, arXiv:math/0408015.
5. E. Cavallo and C. Sattler, *Relative elegance and Cartesian cubes with one connection*, arXiv:2211.14801.
