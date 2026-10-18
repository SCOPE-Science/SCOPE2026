# Sharp sink–saddle transition and an exact elliptic center at a symmetric three-dimensional Lozi two-cycle

## Finding

Consider the symmetric subfamily of the three-dimensional thread–sheet Lozi map introduced in [1]. Its quadrant-changing two-cycle was calculated in [1, §4.3]. The additional result here is the complete local stability trichotomy, including the exact invariant ellipses at the critical multiplier crossing.

For every real \(a\) and \(0<b<1\), define
\[
T_{a,b}(x,y,z)=\bigl(a|x|+y\operatorname{sgn}(z)+1,\ b(x+z),\ y\operatorname{sgn}(x)+a|z|+1\bigr),
\]
with \(\operatorname{sgn}(t)=1\) for \(t\ge0\) and \(-1\) otherwise. Set \(Q_4=\{x>0,z<0\}\), \(Q_2=\{x<0,z>0\}\), and \(D=1+a^2-2ab\).

**Theorem.** There is precisely one primitive two-cycle following the strict itinerary \(Q_4\longrightarrow Q_2\longrightarrow Q_4\) if and only if \(a<2b-1\). It consists of \(U\) and \(V\), where
\[
U=\left(\frac{1+2b-a}{D},\frac{2b}{D},\frac{1-2b+a}{D}\right),\qquad
V=\left(\frac{1-2b+a}{D},\frac{2b}{D},\frac{1+2b-a}{D}\right).
\]
Whenever this cycle exists, the following sharp trichotomy holds:

1. If \(a^2(1+4b^2)<1\), it is a locally exponentially attracting sink.
2. If \(a^2(1+4b^2)>1\), it is a hyperbolic saddle with exactly two expanding Floquet directions and one contracting direction.
3. If \(a^2(1+4b^2)=1\), it has one strictly contracting Floquet multiplier and a nonreal conjugate pair of unit-modulus multipliers. Locally in the two-dimensional center plane through \(U\), the second iterate preserves a nested one-parameter family of **exact nondegenerate invariant ellipses**; their images are companion ellipses through the opposite quadrant near \(V\). The two-cycle is Lyapunov stable locally but is not locally attracting.

There is no index-one saddle, full repeller, or intermediate stability regime for this strict two-cycle within \(0<b<1\). The orbit-position formula itself is already contained in [1]; the sharp stability partition and invariant-ellipse structure are the objects of this theorem.

## Assumptions and scope

The state space is \(\mathbb R^3\), all parameters are real with \(0<b<1\), and the two-cycle is required to visit the **strict open** quadrants \(Q_4,Q_2\). No statement is made at \(a=2b-1\), where one of the candidate coordinates is zero and the strict itinerary fails. The classification concerns this specific two-cycle, not all periodic orbits and not global attractor basins. The restriction to equal outer coefficients \(a=c\) is the natural coordinate-symmetric subfamily emphasized in [1].

## Proof

Let \(P(x,y,z)=(z,y,x)\). Then \(P^2=I\) and, because the outer coefficients agree, \(PT_{a,b}=T_{a,b}P\). On \(Q_4\) the affine Jacobian is
\[
J_4=\begin{pmatrix}a&-1&0\\b&0&b\\0&1&-a\end{pmatrix},
\]
and on \(Q_2\) it is \(J_2=PJ_4P\). Consequently the second iterate for this itinerary has derivative
\[
M=J_2J_4=(PJ_4)^2=K^2,\qquad
K=\begin{pmatrix}0&1&-a\\b&0&b\\a&-1&0\end{pmatrix}.
\]
The characteristic polynomial and a return-map determinant factorization are
\[
\det(\lambda I-K)=\lambda^3+a^2\lambda-2ab,
\quad
\det(I-M)=(1+a^2-2ab)(1+a^2+2ab).
\]
Both factors of the last product are strictly positive, since \(1+a^2\pm2ab=(a\pm b)^2+1-b^2>0\). Thus an affine return with itinerary \(Q_4,Q_2\) has **at most one** periodic point.

To construct one, solve \(T_{a,b}(U)=PU\) in the \(Q_4\) branch. Writing \(S=x+z\) and \(H=x-z\), its equations reduce to \(y=bS\), \(H=(2b-a)S\), and \(S=aH+2\). Hence \(S=2/D\), giving the displayed coordinates, with \(D=(a-b)^2+1-b^2>0\). The first coordinate of \(U\) is then positive and its third coordinate negative exactly when \(a<2b-1\): if \(a<2b-1\), then \(1+2b-a>2>0\). In that case \(T(U)=PU=V\) and symmetry gives \(T(V)=U\); the points lie in distinct quadrants and have primitive period two. Uniqueness of the affine return proves the converse, including possible non-symmetric candidates.

For \(a\ne0\), put \(s\) equal to the unique real root of \(s^3+a^2s=2ab\). Monotonicity gives \(\operatorname{sgn}(s)=\operatorname{sgn}(a)\) and \(|s|<1\), because \(1+a^2-2|ab|=(|a|-b)^2+1-b^2>0\). Polynomial division gives
\[
\det(\lambda I-K)=(\lambda-s)\bigl(\lambda^2+s\lambda+a^2+s^2\bigr).
\]
The quadratic discriminant is \(-4a^2-3s^2<0\). Thus the eigenvalues of \(K\) are \(s\) and
\[
\lambda_\pm=-\frac{s}{2}\pm i\sqrt{a^2+\frac{3s^2}{4}},
\qquad |\lambda_\pm|^2=a^2+s^2.
\]
The eigenvalues of the two-step monodromy \(M=K^2\) are \(s^2\in(0,1)\) and \(\lambda_\pm^2\), whose modulus is \(a^2+s^2\). If \(a=0\), then \(\det(\lambda I-K)=\lambda^3\), so all multipliers are zero; this lies in the strict-sink regime whenever the cycle exists.

The scalar function \(t\mapsto t^3+a^2t\) is strictly increasing on \([0,\infty)\). For \(a^2<1\), comparing its value at \(t=\sqrt{1-a^2}\) against \(2|ab|\) yields
\[
a^2+s^2\ \begin{cases}<1\\=1\\>1\end{cases}
\quad\Longleftrightarrow\quad
a^2(1+4b^2)\ \begin{cases}<1\\=1\\>1.\end{cases}
\]
If \(a^2\ge1\), both quantities are above one. This proves the two hyperbolic alternatives and sharpness. Local exponential attraction or hyperbolic saddle behavior follows directly because the return is affine on a whole neighborhood of the strict orbit.

At the equality \(a^2(1+4b^2)=1\), necessarily \(a\ne0\), and substitution into the cubic shows \(s=2ab\) and \(a^2+s^2=1\). The matrix \(K\) has a real one-dimensional stable eigenspace and a real invariant center plane \(W\) corresponding to its complex pair. On \(W\), Cayley–Hamilton gives \(K^2+sK+I=0\). Choose any nonzero \(v\in W\). The vectors \(v,Kv\) are independent, and every vector of \(W\) has unique coordinates \(w=\xi v+\eta Kv\). The action of \(K\) in these coordinates is
\[
(\xi,\eta)\longmapsto(-\eta,\xi-s\eta).
\]
Therefore the positive definite quadratic form
\[
H(\xi,\eta)=\xi^2-s\xi\eta+\eta^2
\]
is preserved by \(K\), and hence by \(M=K^2\). Its positive level sets are ellipses. Since \(U,V\) lie strictly inside their quadrants, every sufficiently small such ellipse centered at \(U\) stays within the same two affine branches under one and two iterates. The map \(T^2\) preserves each ellipse exactly, not merely to leading order. A contracting transverse stable eigenline ensures local Lyapunov stability, while points on these ellipses do not converge to \(U\), proving non-attraction.

## Verification

The accompanying standard-library program `verify.py` checks, using exact rational arithmetic, 320 parameter pairs; at each it verifies the return determinant, the cubic characteristic polynomial at five points, the formal cycle positions, and their strict-quadrant condition. Whenever the strict cycle exists it also confirms both dynamical identities \(T(U)=V\) and \(T(V)=U\). Additional exact rational examples check one sink and one saddle; numerical diagnostics check the quadratic center form and 64 two-step local iterates at the explicit neutral parameter \(b=1/5\), \(a=-5/\sqrt{29}\). Running `python3 verify.py` prints the pass summary. The polynomial factorization, spectral inequalities and existence of uncountably many small invariant ellipses are proved above for the full continuum; finite checks do not substitute for these arguments.

For example, at \((a,b)=(-4/5,1/5)\), the attracting cycle includes \(U=(55,10,-5)/49\); the corresponding stability discriminant is \(-161/625\). At \((a,b)=(-5/4,1/10)\), the cycle is an index-two saddle. The neutral example has \(s=-2/\sqrt{29}\), so the level-set form is explicit.

## Relationship to prior work

Reference [1] introduced this three-dimensional map, identified its coordinate-swap symmetry and gave a general algebraic construction for the quadrant-changing period-two orbit (equations (34)–(45) and numerical examples). These map definitions, orbit equations and example points are prior results. The additional statements here are the exact **all-parameter local stability criterion** on the symmetric family, the exclusion of index-one saddles, and the exceptional **exact invariant-ellipse foliation** at the neutral boundary. Section 4.3–4.4 of [1] computes fixed-point spectra but does not state a Floquet stability diagram for the quadrant-changing two-cycle. Reference [2] analyzes a different higher-dimensional, delay-feedback generalization of the classical Lozi map; its general bifurcation observations do not cover the present sign-coupled map or this orbit. Classical linear spectral theory supplies the method but not the map-specific cubic reduction or critical curve.

## Limitations

No claim is made for unequal outer coefficients, for \(b\notin(0,1)\), for switching-surface points, for the existence or geometry of global chaotic attractors, or for other symbolic itineraries. The neutral invariant ellipses are local subsets of a two-dimensional plane, not a claim that the entire three-dimensional phase space is foliated by invariant surfaces. A separate external literature search did not uncover an equivalent full theorem, but indexed searches alone cannot certify priority; earlier implicit or unpublished derivations remain possible. Scientific review here is not an independent mathematical audit.

## References

[1] René Lozi, *Coexistence of Thread and Sheet Chaotic Attractors for Three Dimensional Lozi Map*, preprint posted 11 May 2023, https://www.preprints.org/manuscript/202305.0775 ; published version *Dynamics* 3 (2023), 315–344, https://doi.org/10.3390/dynamics3020019 .

[2] Shakir Bilal and Ramakrishna Ramaswamy, *A higher-dimensional generalization of the Lozi map: Bifurcations and dynamics*, arXiv:2005.01849 (2020), https://arxiv.org/abs/2005.01849 .
