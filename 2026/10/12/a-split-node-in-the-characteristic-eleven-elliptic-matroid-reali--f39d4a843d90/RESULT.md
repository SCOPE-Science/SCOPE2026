# A split node in the characteristic-eleven elliptic-matroid realization scheme

## Finding
Let \(k\) be an algebraically closed field of characteristic \(11\). Let \(T_{11}\) be the rank-three matroid on \(\mathbb Z/11\mathbb Z\) whose dependent triples of distinct labels are precisely those with zero sum. Let \(\mathscr R_{11,k}\) be its scheme of labeled projective-plane realizations, modulo projective transformations. In this scheme consider the labeled configuration
\[
Q_i=(i:1:i^3)\in\mathbb P^2(k),\qquad i\in\mathbb F_{11}.
\]
The completed local ring at this configuration is an **ordinary split node**:
\[
\widehat{\mathcal O}_{\mathscr R_{11,k},[Q]}
\cong k[[U,V]]/(UV).
\]
In particular, the local dimension is \(1\), the embedding dimension is \(2\), the Hilbert–Samuel multiplicity is \(2\), and the normalization has exactly two branches at \([Q]\).

More explicitly, fix the projective frame consisting of the points with labels \(0,1,2,3\) and write the fourth remaining coordinate point as \(Q_4=(x:1:z)\). Then a neighborhood of \([Q]\) is an open neighborhood of \((x,z)=(4,9)\) in the plane curve
\[
G(x,z)=x^3+3x^2z+2x^2-5xz^2+3xz-x-5z^3+z^2+z=0
\quad\text{over }\mathbb F_{11}.
\]
Writing \(u=x-4\) and \(v=z-9\), the exact local equation is
\[
G(4+u,9+v)=3u(v-u)+u^3+3u^2v-5uv^2-5v^3.
\]
The tangent cone is therefore the union of the two distinct \(k\)-lines \(u=0\) and \(v=u\).

## Assumptions and scope
The realization scheme uses the ordinary scheme-theoretic incidence conditions: all \(15\) dependent Plücker determinants vanish, and all \(150\) basis determinants are inverted. The quotient by projective transformations is understood on the open projective-frame chart; the four labels \(0,1,2,3\) constitute a projective frame at every realization of this matroid. This is the scheme of configurations of \(11\) distinct labeled points, not a compactification allowing colliding labels or a Drinfeld-level moduli scheme. The claim concerns the germ at the displayed configuration in characteristic \(11\).

## Proof
**1. A cuspidal realization.** For three distinct elements \(a,b,c\in\mathbb F_{11}\), the determinant of the columns \((a,1,a^3)^\mathsf T\), \((b,1,b^3)^\mathsf T\), \((c,1,c^3)^\mathsf T\) is, up to sign,
\[
(a-b)(b-c)(c-a)(a+b+c).
\]
Thus the determinant vanishes exactly when \(a+b+c=0\). The \(11\) points are distinct and realize precisely \(T_{11}\). Their containing cubic is \(X^3=Y^2Z\), smooth at all the marked points and cuspidal at the unmarked point \((0:0:1)\).

**2. Twelve incidence equations eliminate six points.** Normalize the projective frame to
\[
Q_0=(0:1:0),\quad Q_1=(1:1:1),\quad
Q_2=(2:1:8),\quad Q_3=(3:1:5),
\]
and put \(Q_4=(x:1:z)\). Use \(L_{ij}=Q_i\times Q_j\) for the line through two points, and \(L_{ij}\times L_{kl}\) for the intersection of two lines. The incidence conditions determine the six other points, scheme-theoretically near the marked configuration, in the following order:
\[
\begin{aligned}
Q_8&=L_{03}\times L_{12}, & Q_7&=L_{13}\times L_{04},\\
Q_6&=L_{23}\times L_{14}, & Q_5&=L_{06}\times L_{24},\\
Q_{10}&=L_{01}\times L_{48},& Q_9&=L_{02}\times L_{58}.
\end{aligned}
\]
Here each cross product supplies a homogeneous representative, without further rescaling. The six representatives' second coordinates at \((x,z)=(4,9)\), in the order shown, are \(-5,-2,5,-4,-2,4\), respectively, all nonzero modulo \(11\). Consequently all intersections and the indicated affine-coordinate normalizations are valid on a neighborhood of the point. The twelve used dependent triples are
\[
(0,3,8),(1,2,8),(1,3,7),(0,4,7),(2,3,6),(1,4,6),
(0,5,6),(2,4,5),(0,1,10),(4,8,10),(0,2,9),(5,8,9).
\]
These equations are precisely the pairs of independent linear incidence conditions eliminating the six points.

**3. The three residual equations generate one ideal.** The only remaining dependent triples are \((3,9,10)\), \((5,7,10)\), and \((6,7,9)\). In the homogeneous representatives obtained above, exact polynomial cross-product expansion over \(\mathbb F_{11}[x,z]\) gives
\[
\begin{aligned}
\det(Q_3,Q_9,Q_{10})&=3G,\\
\det(Q_5,Q_7,Q_{10})&=(-2x+2z)G,\\
\det(Q_6,Q_7,Q_9)&=(-2x+5z-3)G.
\end{aligned}
\]
All three factors multiplying \(G\) are units at \((4,9)\): they take the values \(3,-1,1\) in \(\mathbb F_{11}\). Therefore the local incidence ideal is exactly \((G)\), with no unaccounted equations or scheme-theoretic components. The \(150\) basis determinants remain units because they are nonzero at the exhibited realization. Thus
\[
\mathcal O_{\mathscr R_{11,k},[Q]}
\cong\bigl(k[x,z]/(G)\bigr)_{(x-4,z-9)}.
\]

**4. The node.** Substitution yields the displayed exact expansion of \(G(4+u,9+v)\); the constant and linear parts vanish, and the degree-two initial form \(3u(v-u)\) has two distinct linear factors. The usual formal node criterion, valid in characteristic \(11\), identifies the completed local ring with \(k[[U,V]]/(UV)\). This proves the stated dimensions, multiplicity and branch count.

## Verification
The accompanying standard-library-only program `verify_node.py` reconstructs all eleven homogeneous points over \(\mathbb F_{11}[x,z]\), verifies the precise three polynomial identities, checks all \(165\) distinct triples at the marked point (\(15\) nonbases and \(150\) bases), verifies that the six necessary coordinate denominators are units, and checks the complete translated cubic equation. Execute `python3 verify_node.py`; the expected success marker is `NODE_CERTIFICATE_OK`. This exact symbolic calculation is a reproducibility aid to the elementary polynomial proof, not a finite-data extrapolation.

## Relationship to prior work
Baker, *Elliptic matroids and modular curves* (arXiv:2608.05299v1, first public 2026-08-05), proves a scheme-theoretic correspondence over \(\mathbb Z[1/n]\); his explicit discussion of the primes dividing \(n\) explains why that correspondence does not extend directly. The present result computes a local singularity in the excluded characteristic \(11\), with distinct geometric labels and a cuspidal source cubic. Borisov and Roulleau (arXiv:2404.04364v1) give the characteristic-prime-to-level modular interpretation and incidence framework. Corey and Luber (arXiv:2307.11915v2) prove that rank-three realization spaces on at most eleven elements are smooth over \(\mathbb C\); this does not control their characteristic-eleven fibers. None of these inspected results supplies the displayed local equation or split-node calculation.

## Limitations
This is a local result at one specified realization. It does not classify all points or irreducible components of the characteristic-eleven realization scheme, prove a global modular interpretation at bad primes, or address analogous configurations at other characteristics. The two branches are branches of the completion at the marked point; no global labeling or global parametrization of those branches is claimed. The polynomial equations and chart are valid on a neighborhood where the stated frame, intersections and basis minors remain nondegenerate.

## References
- M. Baker, *Elliptic matroids and modular curves*, arXiv:2608.05299v1 (first public 2026-08-05), §§10.2, 11–15.
- L. Borisov and X. Roulleau, *Modular curves X1(n) as moduli spaces of point arrangements and applications*, arXiv:2404.04364v1 (2024), §§2–5.
- D. Corey and D. Luber, *Singular matroid realization spaces*, arXiv:2307.11915v2 (2025 revision), Theorem 1.1.
