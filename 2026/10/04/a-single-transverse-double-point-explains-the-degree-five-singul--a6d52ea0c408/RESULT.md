# A single transverse double point explains the degree-five singular scheme in a Hadamard quartic surface
## Finding
Let \(X\subset\mathbb P^5\) and \(Y\subset\mathbb P^5\) be the line and conic in Calussi--Carlini--Fatabbi--Lorenzini, Example 4.1. Their Hadamard product \(S=X\star Y\) has exactly one singular point,
\[
q=[0:17:-51:-66:-77:-44].
\]
The normalization has two points over \(q\), and the two smooth local branches meet transversely. Equivalently,
\[
\widehat{\mathcal O}_{S,q}\cong
\mathbb C[[u,v,s,t]]/(us,ut,vs,vt).
\]
Consequently the intrinsic singular scheme at \(q\) is cut out by \((u,v,s,t)^2\) and has length \(5\). Thus the degree-five zero-dimensional singular scheme reported in the source is supported at one point rather than at five reduced points.

## Assumptions and scope
The ground field is \(\mathbb C\). The line \(X\), conic \(Y\), and Khatri--Rao matrix are exactly those displayed in Example 4.1 of arXiv:1804.01388v4. The conic is smooth. The statement concerns this named example only; it does not assert that every nongeneric line--conic Hadamard product has the same local model.

## Proof
Using the plane coordinates \([z_0:z_1:z_2]\) displayed in the source, substitution into the conic gives
\[
Q=9z_0^2-18z_0z_1+18z_0z_2+11z_1^2+z_1z_2-28z_2^2.
\]
Its symmetric matrix has determinant \(-5913/4\), so \(Y\) is smooth. In the Segre coordinates
\[
(y_0z_0,y_0z_1,y_0z_2,y_1z_0,y_1z_1,y_1z_2),
\]
the displayed Khatri--Rao matrix has rank \(5\). Hence \(S\) is the projection of the smooth Segre embedding \(\mathbb P^1\times Y\subset\mathbb P^5\) from the point represented by
\[
P=\begin{pmatrix}0&-2&0\\3&2&2\end{pmatrix},
\]
and its linear span in the target is \(H=V(w_0+3w_1+w_2)\cong\mathbb P^4\).

The row line of \(P\) can be parametrized by \(z(t)=(3,2-2t,2)\). Restriction of the conic equation is
\[
Q(z(t))=44t^2+16t+17,
\]
whose discriminant is \(-2736=-144\cdot19
eq0\). Thus the row line meets \(Y\) in exactly two distinct points. Any secant decomposition of the rank-two matrix \(P\) by points of \(\mathbb P^1\times Y\) must use precisely those two row directions; once they are fixed, the two \(\mathbb P^1\)-factors are uniquely determined by expressing the two rows of \(P\) in that basis. Therefore exactly one secant of \(\mathbb P^1\times Y\) passes through the projection center.

There are no tangent incidences through the center. Indeed, if \(P\) belonged to the tangent plane at \(y\otimes z\), then the row space of \(P\) would be spanned by \(z\) and a tangent direction to \(Y\) at \(z\); hence its row line would be the tangent line to \(Y\) at \(z\). The nonzero discriminant above shows that the row line meets \(Y\) in two distinct points, so it is tangent at neither. The projection is therefore immersive everywhere. It follows that the only possible singular image is the unique double fiber.

For an exact description, choose \(\omega\) with \(\omega^2=-19\). The two points over the double fiber may be represented by
\[
z_\varepsilon=(33,26-3\varepsilon\omega,22),\qquad
y_\varepsilon=(-22\varepsilon\omega,57-4\varepsilon\omega),\qquad \varepsilon\in\{1,-1\}.
\]
Both project to \(q\). Exact differentiation of the projected parametrization gives three-dimensional vector tangent spaces at each branch, and the common image vector together with two tangent directions from each branch has rank \(5\). A nonzero \(5\times5\) minor is
\[
2357771608607690880\,\omega,
\]
so the two projective tangent planes are transverse in \(H\).

Two smooth surface germs meeting transversely at a point in a smooth fourfold are analytically equivalent to the coordinate planes \(V(u,v)\) and \(V(s,t)\). Their union has ideal
\[
(u,v)\cap(s,t)=(us,ut,vs,vt).
\]
For this local model, the \(2\times2\) Jacobian minors generate, modulo the defining ideal, all quadratic monomials in \(u,v,s,t\). Hence the singular scheme is \(V((u,v,s,t)^2)\), whose local algebra has basis \(1,u,v,s,t\) and length \(5\).

## Verification
The bundled exact checker reconstructs the source conic in plane coordinates, verifies smoothness, computes the projection center and target hyperplane, restricts the conic to the center's row line, checks the two projected preimages of \(q\), certifies immersion at both branches, certifies transversality by the displayed nonzero minor in \(\mathbb Q(\omega)\) with \(\omega^2=-19\), and computes the Jacobian/Fitting singular scheme of the analytic model. Running `python3 artifacts/verify.py` prints `VERIFY_OK`.

## Relationship to prior work
Calussi--Carlini--Fatabbi--Lorenzini state for Example 4.1 that the Hadamard product has dimension \(2\), degree \(4\), and a zero-dimensional singular locus of degree \(5\); they also display the rank-deficient Khatri--Rao matrix. They do not identify the support of that singular scheme or give its analytic local type. The result above refines their degree computation by showing that all length \(5\) is concentrated at one transverse two-branch point and explains the number \(5\) intrinsically as the Jacobian length of two transverse surface branches. Searches for the exact example, its singular-scheme degree, Segre--Veronese projection language, and transverse-double-point terminology did not locate a published statement of this refinement.

## Limitations
The argument is specific to Example 4.1 and to characteristic zero. It classifies the analytic germ and its intrinsic singular scheme, but it does not classify all centers of projection of the \((1,2)\) Segre--Veronese surface. A 2024 monograph on Hadamard products is a plausible place for later discussion; accessible metadata and targeted web searches did not expose the present local classification, but the full monograph text was not available for direct comparison.

## References
G. Calussi, E. Carlini, G. Fatabbi, A. Lorenzini, *On the Hadamard product of degenerate subvarieties*, arXiv:1804.01388v4, especially Section 4, Example 4.1; published in *Portugaliae Mathematica* 76 (2019), 123--141, DOI 10.4171/PM/2029.

C. Bocci, E. Carlini, *Hadamard Products of Projective Varieties*, Frontiers in Mathematics, Birkhauser, 2024, DOI 10.1007/978-3-031-54263-3 (metadata inspected; full text not used).
