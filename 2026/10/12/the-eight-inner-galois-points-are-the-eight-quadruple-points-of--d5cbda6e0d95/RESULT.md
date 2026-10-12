# The eight inner Galois points are the eight quadruple points of the Schur line configuration
## Finding
Over \(\mathbb C\), consider the maximal-inner-Galois quartic
\[
S_8:\quad X^4+XY^3+Z^4+ZW^3=0.
\]
Miura--Taki record that this smooth quartic has exactly eight inner Galois points, namely
\[
[0:0:0:1],\quad [0:0:\zeta_6^i:1],\quad [0:1:0:0],\quad [\zeta_6^i:1:0:0]\qquad (i\in\{1,3,5\}).
\]
Let \(\alpha\in\mathbb C\) satisfy \(\alpha^4=-1\). The projective transformation
\[
(x_0,x_1,x_2,x_3)=(X,-Y,\alpha Z,-\alpha W)
\]
sends \(S_8\) to Schur's quartic
\[
S:\quad x_0^4-x_0x_1^3-x_2^4+x_2x_3^3=0.
\]
Under this equivalence, the eight inner Galois points are exactly the eight quadruple intersection points of the complete 64-line configuration on \(S\).

More precisely, let
\[
L=V(x_0,x_1),\qquad M=V(x_2,x_3).
\]
The transformed Galois points are the four points \(p_1,\ldots,p_4=L\cap S\) and the four points \(q_1,\ldots,q_4=M\cap S\). The 16 Schur lines incident with quadruple points are exactly
\[
\ell_{ij}=\overline{p_iq_j}\qquad (1\le i,j\le4).
\]
Thus the point-line incidence restricted to these eight Galois points and these 16 lines is the complete bipartite graph \(K_{4,4}\): each Galois point lies on exactly four Schur lines, each of the 16 lines contains exactly two Galois points, and the other 48 Schur lines contain none.

## Assumptions and scope
The base field is \(\mathbb C\). “Galois point” means an inner Galois point for the projection of the smooth quartic surface, in the sense used by Miura--Taki. “Quadruple point” refers to a point incident with exactly four distinct lines in the complete 64-line configuration on the Schur quartic; it is not a singular point of the quartic surface, which is smooth.

The statement uses three literature inputs. Miura--Taki give the equation of the unique maximal case and list its eight inner Galois points. Rojas--Lira give the Schur equation, the two skew coordinate lines \(L,M\), their four intersection points with \(S\), and prove that all Schur lines meeting either \(L\) or \(M\) are precisely the 16 joins \(\ell_{ij}\). Nurowski's complete incidence census states that the 64-line arrangement has exactly eight quadruple points and that the 16 lines incident with them are precisely the lines incident with two such points.

## Proof
Substituting
\[
x_0=X,\qquad x_1=-Y,\qquad x_2=\alpha Z,\qquad x_3=-\alpha W
\]
into the Schur equation gives
\[
x_0^4-x_0x_1^3-x_2^4+x_2x_3^3
=X^4+XY^3+Z^4+ZW^3,
\]
because \(\alpha^4=-1\). Hence the two quartics are projectively equivalent.

Write \(\xi=\zeta_3\). The first four Galois points map to
\[
[0:0:0:1],\ [0:0:1:1],\ [0:0:\xi:1],\ [0:0:\xi^2:1]
\]
in some order, since \(\{-\zeta_6,-\zeta_6^3,-\zeta_6^5\}=\{\xi^2,1,\xi\}\). These are exactly the four points \(p_i=L\cap S\) in Rojas--Lira. The other four map analogously to
\[
[0:1:0:0],\ [1:1:0:0],\ [\xi:1:0:0],\ [\xi^2:1:0:0],
\]
which are exactly the four points \(q_j=M\cap S\).

Rojas--Lira prove that the 16 joins \(\ell_{ij}=\overline{p_iq_j}\) are distinct lines on \(S\), and moreover that every Schur line meeting \(L\) or \(M\) is one of these 16. Therefore every Schur line through any transformed Galois point is one of the joins. For fixed \(i\), the four lines \(\ell_{ij}\) are the only Schur lines through \(p_i\); similarly the four \(\ell_{ij}\) with fixed \(j\) are the only ones through \(q_j\). Thus all eight Galois points are quadruple points of the 64-line arrangement, and the join-incidence graph is \(K_{4,4}\).

Nurowski's complete incidence census contains exactly eight quadruple points in the full 64-line arrangement. Since the eight transformed Galois points are already eight distinct quadruple points, they exhaust that set. The same census characterizes the 16 distinguished lines as exactly the lines incident with two quadruple points. Hence those 16 lines are precisely the joins \(\ell_{ij}\). The remaining 48 lines avoid all eight Galois points.

## Verification
The accompanying script `verify_schur_galois.py` performs exact symbolic checks. It verifies the projective equation change, transforms the eight Galois points and matches them to the two four-point coordinate-line sets, constructs all 16 joins, substitutes a two-parameter point on every join into the Schur quartic, checks all 16 projective lines are distinct via Plücker coordinates, and checks the \(4+4\) incidence degrees. A fresh replay returned

`VERIFY_OK transform=S8_to_Schur galois_points=8 join_lines=16 incidence=K4,4 each_galois_point_on_join_lines=4`

The assertion that no additional Schur line passes through these points is not inferred from the finite script; it is the exact content of Rojas--Lira, Lemma 3.1. The assertion that there are no other quadruple points is likewise taken from the complete 64-line incidence census in Nurowski.

## Relationship to prior work
Miura--Taki study the eight Galois points and the associated Eisenstein/singular \(K3\) geometry, but the inspected full text contains no occurrence of “Schur.” Rojas--Lira analyze Schur's 64 lines and the 16 joins between the two coordinate four-point sets, but the inspected full text contains no occurrence of “Galois.” Nurowski identifies exactly eight quadruple points and the associated 16-line incidence skeleton, but the inspected full text likewise contains no occurrence of “Galois.” The present statement is the explicit bridge between these descriptions.

## Limitations
The result is stated over \(\mathbb C\) and for the maximal inner-Galois quartic. It does not classify line configurations for quartics with fewer Galois points, nor does it determine the full projective automorphism action on the eight points. The exact global line-incidence conclusions use the published 64-line enumeration/census rather than a new independent enumeration of all 64 lines.

## References
1. K. Miura and S. Taki, *Quartic surfaces with a Galois point and Eisenstein K3 surfaces*, arXiv:2308.11102v1, 2023.
2. J. Rojas and D. Lira, *The maximal number of skew lines on Schur's quartic*, Rend. Sem. Mat. Univ. Padova 142 (2019), 81--91, DOI:10.4171/RSMUP/31.
3. P. Nurowski, *The Reye geometry inside the 64 lines of the Schur quartic*, arXiv:2609.10751v2, 2026.
