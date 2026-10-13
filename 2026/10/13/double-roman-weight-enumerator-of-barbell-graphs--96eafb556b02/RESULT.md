# Double Roman weight enumerator of barbell graphs

## Finding
For an integer \(n\ge2\), let \(B_n\) be the barbell graph formed from two disjoint copies of \(K_n\) by joining distinguished vertices \(u\) and \(v\) with one bridge edge. A double Roman dominating function is a map \(f:V(B_n)\to\{0,1,2,3\}\) such that every vertex labeled \(0\) has either a neighbor labeled \(3\) or at least two neighbors labeled \(2\), and every vertex labeled \(1\) has a neighbor labeled at least \(2\). Let \(\omega(f)=\sum_{z\in V(B_n)}f(z)\), and define the weight enumerator
\[
\mathcal D_n(x)=\sum_f x^{\omega(f)},
\]
where the sum ranges over all double Roman dominating functions on \(B_n\).

Put \(m=n-1\), \(S(x)=1+x+x^2+x^3\), and
\[
H_n(x)=S(x)^m-(1+x)^m-mx^2(1+x)^{m-1},
\]
\[
G_n(x)=H_n(x)+mx^{m+1},
\qquad
J_n(x)=S(x)^m-(1+x)^m+x^m.
\]
Define the \(4\times4\) transfer matrix, with rows and columns indexed by the bridge-endpoint labels \(0,1,2,3\),
\[
M_n(x)=
\begin{pmatrix}
H_n&H_n&G_n&G_n\\
xG_n&xG_n&xG_n&xG_n\\
x^2J_n&x^2J_n&x^2J_n&x^2J_n\\
x^3S^m&x^3S^m&x^3S^m&x^3S^m
\end{pmatrix}.
\]
Then
\[
\boxed{\mathcal D_n(x)=\operatorname{tr}\bigl(M_n(x)^2\bigr)}.
\]
Equivalently,
\[
\begin{aligned}
\mathcal D_n(x)={}&H_n^2+(xG_n)^2+(x^2J_n)^2+(x^3S^m)^2\\
&+2\Bigl(H_nxG_n+G_nx^2J_n+G_nx^3S^m+xG_nx^2J_n+xG_nx^3S^m+x^2J_nx^3S^m\Bigr).
\end{aligned}
\]
The minimum weight and its multiplicity are
\[
(\gamma_{dR}(B_2),[x^{\gamma_{dR}(B_2)}]\mathcal D_2)=(5,4),
\]
\[
(\gamma_{dR}(B_3),[x^{\gamma_{dR}(B_3)}]\mathcal D_3)=(6,13),
\]
and, for every \(n\ge4\),
\[
\gamma_{dR}(B_n)=6,
\qquad
[x^6]\mathcal D_n(x)=n^2.
\]
For \(n\ge4\), the minimum functions are exactly those that place one label \(3\) in each clique and label every other vertex \(0\).

## Assumptions and scope
The barbell convention here is exactly two vertex-disjoint cliques \(K_n\) joined by one edge between distinguished vertices, with \(n\ge2\). Labels are allowed to use all four values \(0,1,2,3\); the enumerator counts every feasible function, not only minimum functions. The result does not concern variants such as total, signed, independent, or restrained double Roman domination.

## Proof
Fix one clique side and call its bridge endpoint \(u\). Let the opposite bridge endpoint have label \(b\in\{0,1,2,3\}\), and fix \(f(u)=a\in\{0,1,2,3\}\). The other \(m=n-1\) vertices form a complete graph and have ordinary weight-generating factor \(S(x)^m\).

If \(a=3\), every vertex on that side is automatically protected, so the side polynomial is \(x^3S(x)^m\), independently of \(b\).

If \(a=2\), every internal vertex labeled \(1\) sees a label \(2\). An internal vertex labeled \(0\) fails exactly when there is no internal label \(2\) or \(3\). The bad assignments use only \(0,1\) and contain at least one \(0\), whose polynomial is \((1+x)^m-x^m\). Hence the side polynomial is
\[
x^2\bigl(S(x)^m-(1+x)^m+x^m\bigr)=x^2J_n(x),
\]
again independently of \(b\).

Now take \(a\in\{0,1\}\). For the internal vertices to be protected, one of three mutually exhaustive situations must hold: there is at least one internal label \(3\); there are at least two internal labels \(2\); or there is exactly one internal label \(2\), no label \(3\), and every remaining internal vertex has label \(1\). Therefore the internal-valid polynomial is
\[
G_n(x)=S(x)^m-(1+x)^m-mx^2(1+x)^{m-1}+mx^{m+1}.
\]
When \(a=1\), every assignment counted by \(G_n\) already contains an internal label at least \(2\), so the endpoint is protected and the side polynomial is \(xG_n\) for every \(b\).

When \(a=0\), the endpoint itself must also be protected. If \(b=3\), this is automatic. If \(b=2\), the only delicate internal-valid case has exactly one internal label \(2\) and all remaining internal labels \(1\), and the external \(2\) supplies the required second label \(2\), so this case is also valid. Thus the side polynomial is \(G_n\) for \(b\in\{2,3\}\). If \(b\in\{0,1\}\), that delicate case fails at the endpoint, so its polynomial \(mx^{m+1}\) must be removed, leaving \(H_n\).

These four endpoint rows are exactly the displayed matrix \(M_n(x)\). A full labeling of \(B_n\) with bridge-endpoint labels \((a,b)\) is valid precisely when the left side contributes an assignment counted by \((M_n)_{a,b}\) and the right side contributes one counted by \((M_n)_{b,a}\). Hence
\[
\mathcal D_n(x)=\sum_{a,b=0}^3(M_n)_{a,b}(M_n)_{b,a}=\operatorname{tr}(M_n(x)^2).
\]
This proves the enumerator.

For \(n\ge4\), each clique side has double-Roman weight at least \(3\). Indeed, side weight at most \(2\) contains no label \(3\) and at most one label \(2\); because the side has at least three non-bridge vertices, some internal vertex labeled \(0\) cannot have two neighboring labels \(2\) and cannot see a label \(3\). Side weight \(3\) is feasible exactly when one side vertex is labeled \(3\) and all other side vertices are labeled \(0\). Therefore every minimum function has weight \(6\), with independently chosen label-\(3\) vertices on the two sides, giving exactly \(n^2\) minimum functions. For \(n=2\) and \(n=3\), substitution into the exact polynomial gives lowest terms \(4x^5\) and \(13x^6\), respectively.

## Verification
A standalone verifier constructs \(B_n\) directly from adjacency, tests the double Roman conditions without using the transfer formula, and exhaustively checks every labeling for \(2\le n\le5\). It compares the complete coefficient table with the matrix formula and verifies the stated minimum layers. It also evaluates the exact formula through \(n=12\) as a finite algebraic consistency check.

Replay command:

`python3 verify_double_roman_barbell.py`

Expected output:

`VERIFY_OK n_bruteforce=2..5 labelings=1118464 valid_functions=892974 formula_n=2..12 coefficient_checks=408 max_order=24`

The finite computation is not the proof of the infinite family; the proof is the endpoint-state decomposition above.

## Relationship to prior work
Beeler, Haynes, and Hedetniemi introduced double Roman domination and studied its relationship with domination and Roman domination, together with general bounds on the minimum weight. A public institutional record gives the exact day-level date 2016-10-01. A separate search index reports only “May 2016” without a day; because the package requires an exact calendar date and no day was verified for that earlier month-level signal, 2016-10-01 is the exact day-level date recorded here, not a claim that no public trace existed earlier in 2016. Yang and Zhou later studied minimum-weight properties and special graph families; their open full text contains no occurrence of “barbell”, “polynomial”, or “clique”. Banerjee, Henning, and Pradhan gave a linear-time algorithm for the double Roman domination number on block graphs, a class containing barbell graphs, but that optimization result does not enumerate all feasible functions or their weights.

The present statement is coefficientwise: it counts every double Roman dominating function on the entire barbell family. The bridge interaction is isolated in a four-state transfer matrix, and the low-weight layer yields an exact multiplicity statement not supplied by minimum-number algorithms.

## Limitations
The theorem is restricted to the standard symmetric barbell \(B_n\). It does not give a formula for unequal cliques, longer connecting paths, or multiple bridge edges. The literature comparison cannot exclude unindexed or inaccessible family-specific results. The block-graph algorithm source was available only at abstract/metadata level in the checked route, so a hidden family-specific enumeration inside inaccessible supplementary material remains a residual originality risk. No claim is made about roots, unimodality, log-concavity, or asymptotics of \(\mathcal D_n\).

## References
1. R. A. Beeler, T. W. Haynes, and S. T. Hedetniemi, “Double Roman domination,” *Discrete Applied Mathematics* 211 (2016), 23–29. DOI: 10.1016/j.dam.2016.03.017.
2. H. Yang and X. Zhou, “Some Properties of Double Roman Domination,” *Discrete Dynamics in Nature and Society* 2020, Article 6481092. DOI: 10.1155/2020/6481092.
3. S. Banerjee, M. A. Henning, and D. Pradhan, “Algorithmic results on double Roman domination in graphs,” *Journal of Combinatorial Optimization* 39 (2020), 90–114. DOI: 10.1007/s10878-019-00457-3.
4. D. Rupnik Poklukar and J. Žerovnik, “Double Roman Domination: A Survey,” *Mathematics* 11 (2023), 351. DOI: 10.3390/math11020351.
