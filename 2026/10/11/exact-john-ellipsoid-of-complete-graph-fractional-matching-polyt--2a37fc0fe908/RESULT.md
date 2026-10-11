# Exact John ellipsoid of complete-graph fractional matching polytopes

## Finding

For every integer \(n\ge3\), put \(m=\binom n2\) and let \(B\) be the unsigned \(n\)-by-\(m\) incidence matrix of \(K_n\). In the standard Euclidean metric on its edge-coordinate space, consider the fractional matching polytope
\[
F_n=\{x\in\mathbb R^m:x_e\ge0\ (e\in E(K_n)),\ Bx\le\mathbf1_n\}.
\]
Define the positive number
\[
t=\frac{n-4+\sqrt{n^2+8n-16}}{4(n-2)},\qquad
U=1+(n-1)t,\qquad V=1+\frac{n-2}{2}t,
\]
and set
\[
a=\frac tU,\qquad b=\frac1U,\qquad
T=\frac{n(n-3)}2+\frac{n-1}{V}+\frac1U,
\qquad s=\frac{ma^2}{T}.
\]
Then the unique maximum-volume inscribed Euclidean ellipsoid of \(F_n\) is
\[
\boxed{E_n=\{a\mathbf1_m+z:z^{\mathsf T}\Sigma^{-1}z\le1\},\qquad
\Sigma=s\left(I_m+\frac t2 B^{\mathsf T}B\right)^{-1}.}
\]
Its squared principal semiaxes, with multiplicities, are
\[
\boxed{\frac sU\ (1),\quad\frac sV\ (n-1),\quad
s\ \left(\frac{n(n-3)}2\right).}
\]
The last eigenspace is absent when \(n=3\). Its exact \(m\)-dimensional Euclidean volume is
\[
\boxed{\operatorname{vol}_m(E_n)=\frac{\pi^{m/2}}{\Gamma(1+m/2)}\,
\frac{s^{m/2}}{\sqrt U\,V^{(n-1)/2}}.}
\]
Every one of the \(m+n\) facets of \(F_n\) touches \(E_n\) at a distinct point.

## Assumptions and scope

All coordinates correspond to *undirected edges* of the simple complete graph \(K_n\); each edge has one coordinate, and \(B_{i,e}=1\) precisely when vertex \(i\) belongs to edge \(e\). The metric is the ordinary Euclidean metric on \(\mathbb R^m\), not the Frobenius metric on symmetric matrices under an unscaled embedding. The polytope has nonempty interior and its defining nonnegativity and degree inequalities are irredundant for \(n\ge3\). It is the usual fractional matching relaxation, **not** the integral matching polytope with additional odd-set inequalities. The case \(n=2\) is an interval and lies outside the stated formula.

## Proof

**1. Spectrum and variances.** Let \(q_i=B^{\mathsf T}e_i\) denote the normal of the degree constraint at vertex \(i\). Direct edge-counting gives
\[
BB^{\mathsf T}=(n-2)I_n+J_n.
\]
Consequently \(B^{\mathsf T}B\) has eigenvalues \(2(n-1)\), \(n-2\) and \(0\), with multiplicities \(1\), \(n-1\) and \(m-n=n(n-3)/2\), respectively. Thus \(K=(I_m+(t/2)B^{\mathsf T}B)^{-1}\) is positive definite and has eigenvalues \(1/U,1/V,1\) with these multiplicities; in particular \(\operatorname{tr}K=T\). By edge transitivity, every diagonal entry of \(K\) equals \(T/m\). The squared norm of the degree normal's projection onto the constant edge eigenspace is \(2(n-1)/n\); the squared norm of its projection onto the remaining nonzero eigenspace is \((n-1)(n-2)/n\). Hence
\[
q_i^{\mathsf T}Kq_i=D:=\frac{2(n-1)}{nU}+\frac{(n-1)(n-2)}{nV}.
\]

**2. Scalar identity and containment.** The displayed radical \(t\) is the unique positive solution of
\[
2(n-2)t^2-(n-4)t-2=0.
\]
Substituting \(U,V,T,D\) and clearing their strictly positive denominators gives the equivalent identity \(t^2mD=T\). For the proposed center \(c=a\mathbf1_m\), each nonnegativity facet has slack \(a\), and each vertex-degree facet has slack \(1-(n-1)a=b\). The ellipsoid's maximal support displacement toward an inequality with normal \(u\) is \(\sqrt{u^{\mathsf T}\Sigma u}\). By the diagonal formula and the scalar identity,
\[
e_e^{\mathsf T}\Sigma e_e=sT/m=a^2,\qquad
q_i^{\mathsf T}\Sigma q_i=sD=b^2.
\]
Thus every defining halfspace contains \(E_n\), with equality at the corresponding support point; therefore \(E_n\subseteq F_n\) and every facet has a contact.

**3. A global John certificate.** Transform the containing ellipsoid to the unit ball using \(y=\Sigma^{-1/2}(x-c)\). Its unit-norm contact vectors, indexed by edges and graph vertices, are
\[
u_e=-\frac{\Sigma^{1/2}e_e}{a},\qquad
v_i=\frac{\Sigma^{1/2}q_i}{b}.
\]
Assign the strictly positive weights
\[
\alpha=\frac Tm\quad\text{to each }u_e,
\qquad\beta=\frac{T}{2mt}\quad\text{to each }v_i.
\]
Since \(\sum_iq_i=2\mathbf1_m\) and \(a=tb\), direct substitution yields
\[
\sum_e\alpha u_e+\sum_i\beta v_i=0.
\]
The weighted second moment is exactly the identity:
\[
\begin{aligned}
\sum_e\alpha u_eu_e^{\mathsf T}+\sum_i\beta v_iv_i^{\mathsf T}
&=\Sigma^{1/2}\left(\frac\alpha{a^2}I_m+\frac\beta{b^2}B^{\mathsf T}B\right)\Sigma^{1/2}\\
&=\Sigma^{1/2}\frac T{ma^2}\left(I_m+\frac t2B^{\mathsf T}B\right)\Sigma^{1/2}=I_m.
\end{aligned}
\]
John's contact theorem for a not-necessarily-symmetric convex body proves the unit ball is its maximum-volume inscribed ellipsoid. Transforming back proves global optimality of \(E_n\), not merely optimality among invariant ellipsoids. Uniqueness follows from uniqueness of John's ellipsoid. The normals of the \(m+n\) facets are pairwise nonproportional, so their corresponding contact points are distinct.

**4. Semiaxes and volume.** Applying the spectrum in step 1 to \(\Sigma=sK\) gives the three squared semiaxis values above. Multiplying their square roots and the unit-ball volume gives the displayed exact volume.

## Verification

The standalone standard-library script `VERIFY.py` reconstructs \(B\), performs a Gauss–Jordan inverse of \(I_m+(t/2)B^{\mathsf T}B\), and checks all coordinate and degree tangencies, first-moment balancing, every entry of the John second-moment identity, the trace and constant-eigenspace spectrum, and positivity. On dimensions \(3\le n\le10\), it passed all checks, including \(216\) individual facet contacts. It tests finitely many dimensions only: the general claim follows from the exact identities in the proof.

## Relationship to prior work

Blanchard, De Loera and Louveaux [1] define this fractional matching polytope explicitly, including the complete-graph specialization, and establish monotone-path length properties. Sanità [2] studies its combinatorial diameter and half-integral vertices, not the Euclidean maximum-volume inscribed ellipsoid. Behrend [3] gives geometric and face-structure theory for closely related fractional perfect matching polytopes (with degree *equalities*, which are a different polytope). The polytope here is the **degree-inequality** relaxation. General John's theorem is classical; the claimed geometric content is the explicit incidence-matrix formula, radical parameter, full semiaxis spectrum, volume, and simultaneous contact with all facets for the complete-graph family. No assertion of independent literature priority is made.

## Limitations

The theorem is for complete simple graphs and the edge-coordinate Euclidean metric. It does not solve the same ellipsoid problem for arbitrary graphs, the integral matching polytope, or other coordinate metrics. Numerical checks in `VERIFY.py` do not certify all dimensions. A separately published equivalent solution under network-design or optimal-design terminology remains a possible originality risk; no independent audit has been performed.

## References

[1] M. Blanchard, J. A. De Loera and Q. Louveaux, *On the Length of Monotone Paths in Polyhedra*, arXiv:2001.09575 (first posted 2020-01-27); SIAM Journal on Discrete Mathematics 35 (2021), 1746–1768, DOI:10.1137/20M1315646. Primary MSC 52B12. https://arxiv.org/abs/2001.09575

[2] L. Sanità, *The diameter of the fractional matching polytope and its hardness implications*, arXiv:1806.03397 (first posted 2018-06-09). https://arxiv.org/abs/1806.03397

[3] R. E. Behrend, *Fractional Perfect b-Matching Polytopes I: General Theory*, arXiv:1301.7356 (2013). https://arxiv.org/abs/1301.7356
