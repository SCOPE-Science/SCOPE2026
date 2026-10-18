# Joint star-edge sensitivity and sharp volume smoothness for bipartite Lipschitz balls

## Finding

Let \(p\ge2\), \(q\ge3\), \(2\le k\le q-1\) be integers. In the complete bipartite graph \(K_{p,q}\), give the \(k\) edges from one distinguished first-class vertex to \(k\) distinguished second-class vertices common length \(h\in[1,3]\), leaving every other edge of length one. Use the shortest-path metric. Put \(d=p+q-1\), \(r=q-k\) and let \(V_{p,q,k}(h)\) be the ordinary Lebesgue volume of the real Lipschitz unit ball in coordinates anchored at **an ordinary first-class vertex other than the distinguished one**.

The complete, all-parameter volume response is

\[
\begin{aligned}
V_{p,q,k}(h)={}&\frac{2^d p!q!}{d!}\left(1+\frac{2k}{p(r+1)}\right)\\
&-\frac{2(p-1)!}{r+1}\sum_{j=1}^{k}
\binom{k}{j}\frac{j(r+j)!}{(p+r+j-1)!}
(h-1)^{k-j}(3-h)^{p+r+j-1}.
\end{aligned}
\]

At the deletion/redundancy endpoint,

\[
\frac{V_{p,q,k}(3)}{V_{p,q,k}(1)}=1+\frac{2k}{p(q-k+1)},
\qquad V_{p,q,k}(1)=\frac{2^d p!q!}{d!}.
\]

For the following deletion comparison, extend the notation to \(k=0\) and \(k=1\) by the corresponding graph definitions; \(V_{p,q,0}(1)\) is the unperturbed volume displayed above. The fixed-order increments for deleting one additional edge of this star are

\[
\frac{V_{p,q,k+1}(3)-V_{p,q,k}(3)}{V_{p,q,0}(1)}
=\frac{2(q+1)}{p(q-k)(q-k+1)}\qquad(0\le k\le q-2).
\]

They grow strictly with \(k\): simultaneous deletions have a positive interaction rather than an additive volume response.

Write \(m=p+q-k\). The exact one-sided asymptotic is

\[
V_{p,q,k}(3)-V_{p,q,k}(h)
=\frac{2^k k(p-1)!(q-k)!}{(p+q-k)!}(3-h)^m
+O((3-h)^{m+1})\quad(h\uparrow3).
\]

If \(V\) is extended constantly for \(h\ge3\) (as the shortest-path metric requires), it is precisely \(C^{m-1}\), but not \(C^m\), at \(h=3\). For \(k\ge2\), this order is lower than the previously known one-edge exponent \(p+q-1\); thus the joint volume response is not obtained by summing independent single-edge responses.

## Assumptions and scope

The first vertex class is \(A=\{a_0,a_1,\ldots,a_{p-1}\}\) and the second is \(B=\{b_1,\ldots,b_q\}\). The distinguished vertex is \(a_0\); the exceptional edges are \(a_0b_j\) for \(1\le j\le k\). All other edges retain length one. The anchoring is \(f(a_1)=0\). There are \(d=p+q-1\) remaining real coordinates, and the volume is standard coordinate volume, **not** intrinsic Euclidean volume of the zero-sum embedding (which differs by a fixed factor).

Because \(r=q-k\ge1\) and \(p-1\ge1\), a length-three path avoids each exceptional edge. Accordingly its metric length is \(\min(h,3)\), and for \(h\ge3\) all exceptional inequalities are redundant. All results concern the real scalar field and the specified common-edge-length deformation; no arbitrary pattern of omitted bipartite edges is asserted.

## Proof

**1. Section integration.** Put \(a=p-1\), so \(a\ge1\), and fix the values on the \(a\) ordinary vertices \(a_1,\ldots,a_{p-1}\), including \(f(a_1)=0\). Let \(R\) be their range. The \(q\) values on \(B\) are all constrained by these ordinary vertices to a common interval

\[
I=[\max_{i\ge1}f(a_i)-1,\;\min_{i\ge1}f(a_i)+1]
\]

of length \(L=2-R\). The section is empty when \(R>2\). Translating \(I\) to \([0,L]\) changes no Lebesgue Jacobian in the \(B\) coordinates.

For \(u>0\), define

\[
\phi_u(z;L)=\operatorname{length}([0,L]\cap[z-u,z+u]).
\]

For fixed \(f(a_0)=z\), the \(r\) ordinary second-class coordinates have available interval length \(\phi_1(z;L)\), while the \(k\) exceptional ones have length \(\phi_h(z;L)\). Hence the contribution from the distinguished coordinate and all \(B\)-coordinates is

\[
F_{r,k}(L,h)=\int_{\mathbb R}\phi_1(z;L)^r\phi_h(z;L)^k\,dz.
\]

Reflect around \(L/2\), let \(s=h-1\in[0,2]\), and parameterize the left half of the support by \(v=z+1\in[0,1+L/2]\). There \(\phi_1=\min(v,L)\) and \(\phi_h=\min(v+s,L)\). Therefore

\[
F_{r,k}(L,h)=2\int_0^{1+L/2}\min(v,L)^r\min(v+s,L)^k\,dv.
\]

For \(h=3\) the second factor is identically \(L^k\) on that support, so direct integration gives

\[
F_{r,k}(L,3)=2L^q+\left(\frac{2}{r+1}-1\right)L^{q+1}.
\]

Write \(w=(L-s)_+\). The only region where \(F(L,h)\) differs from \(F(L,3)\) is \(0\le v\le w\). Expanding by the binomial theorem and integrating monomials yields the **exact identity**

\[
\begin{aligned}
F_{r,k}(L,3)-F_{r,k}(L,h)
&=2\int_0^{w}v^r\bigl[L^k-(v+s)^k\bigr]dv\\
&=2\sum_{j=1}^{k}\binom{k}{j}s^{k-j}
\frac{j}{(r+1)(r+j+1)}w^{r+j+1}.
\end{aligned}
\]

**2. Range measure and its moments.** Let \(\nu_a\) be the push-forward of Lebesgue measure in the \(a-1\) free ordinary-vertex coordinates under \(L=2-R\). For \(a=1\), it is a unit point mass at \(L=2\). For \(a\ge2\), the volume of vectors \((0,x_2,\ldots,x_a)\) whose range is at most \(u\) equals \(a u^{a-1}\): the two all-one-sign configurations contribute \(2u^{a-1}\), while cases with negative minimum and positive maximum contribute \((a-2)u^{a-1}\). Thus on \([0,2]\), \(\nu_a\) has density \(a(a-1)(2-L)^{a-2}\).

In either case, elementary beta integration (or the point-mass formula when \(a=1\)) proves for every integer \(b\ge1\), \(0\le s\le2\),

\[
\int(L-s)_+^b\,d\nu_a(L)
=\frac{a!b!}{(a+b-1)!}(2-s)^{a+b-1}.
\]

In particular, with \(s=0\),

\[
I_b:=\int L^b\,d\nu_a(L)
=\frac{2^{a+b-1}a!b!}{(a+b-1)!},
\qquad \frac{I_{q+1}}{I_q}=\frac{2(q+1)}{a+q}.
\]

**3. Exact global formula.** Integrate the endpoint section:

\[
V_{p,q,k}(3)=2I_q+\left(\frac{2}{r+1}-1\right)I_{q+1}
=\frac{2^d p!q!}{d!}\left(1+\frac{2k}{p(r+1)}\right).
\]

Now integrate each monomial in the section deficit of step 1. In the term indexed by \(j\), apply the range identity with \(b=r+j+1\), noting \(a+r+j=p+r+j-1\). This gives

\[
V_{p,q,k}(3)-V_{p,q,k}(h)
=\frac{2(p-1)!}{r+1}\sum_{j=1}^k
\binom{k}{j}\frac{j(r+j)!}{(p+r+j-1)!}
s^{k-j}(2-s)^{p+r+j-1}.
\]

Substitute \(s=h-1\) and \(2-s=3-h\). This is the claimed finite-sum formula. At \(h=1\), only the \(j=k\) summand survives, and simplification yields \(V_{p,q,k}(1)=2^d p!q!/d!\), independent of \(k\), as required. All coefficients in the deficit are nonnegative and the geometric section formula shows \(V\) strictly increases on \([1,3)\).

**4. Deletion interaction and regularity.** The ratio at \(h=3\) follows from step 3. Its consecutive difference is \(2(q+1)/[p(q-k)(q-k+1)]\), strictly increasing for all allowed successive \(k\), including comparison with \(k=0,1\) as boundary cases. For \(h\uparrow3\), the \(j=1\) term has the smallest exponent \(p+r=p+q-k\), with coefficient tending to \(2^k k(p-1)!r!/(p+r)!>0\); all remaining terms are of higher order. The constant extension on the other side of \(3\) has zero derivatives of every positive order, proving the sharp smoothness statement.

## Verification

The standalone `verify_volume.py` directly counts lattice points in integer dilations of the defining difference-inequality polytope, without implementing any integral or beta identity from the proof. Its finite-difference leading coefficient equals the anchored volume by Ehrhart's theorem, since integral difference constraints have integral vertices after clearing the denominator of \(h\). Eight exact rational/integer parameter configurations were run, including \((p,q,k,h)=(2,3,2,3/2)\), giving \(395/32\), and \((3,4,3,3)\), giving \(128/5\). All passed. Run `python3 verify_volume.py` with Python 3 standard library; the general theorem is analytical and is not inferred from this finite test set.

## Relationship to prior work

Ostrovska and Ostrovskii (arXiv:1910.03625v1, first public October 8, 2019) identify the weighted graph transportation-cost space with an \(\ell_1\)-quotient by cycles; this justifies the Lipschitz-dual viewpoint, but does not evaluate multi-edge volume. Alexander, Fradelizi, García-Lirola and Zvavitch (arXiv:1911.10642v1, November 24, 2019) study volume products and finite-dimensional Lipschitz-free geometry, and explicitly compute the equilateral case; their theorems do not cover the present joint weighted bipartite-star deformation. Higashitani, Jochemko and Michałek (arXiv:1807.07678v1, July 20, 2018) determine Ehrhart and facet invariants of **unweighted** complete bipartite symmetric edge polytopes, i.e. the polar type of body. D'Alì, Delucchi and Michałek (arXiv:1910.05193v1) connect those polytopes to finite metric spaces and study other graph invariants.

The previously known \(k=1\) response is recovered by the formula but is not claimed as new. Its deficit is proportional to \((3-h)^{p+q-1}\). The present \(k\ge2\) theorem has a different leading exponent \(p+q-k\) and a nonlinear star-deletion interaction, neither implied by adding single-edge formulas. The cited source material and targeted searches yielded no matching all-\(k\) theorem; absence of a search hit alone is not a uniqueness certificate.

## Limitations

The result requires \(p\ge2\), \(q\ge3\), \(2\le k\le q-1\), common exceptional length \(h\in[1,3]\), and a star of affected edges incident to one vertex. It gives ordinary anchored-coordinate volume, not the polar volume product, arbitrary independently weighted edges, or a general arbitrary-deletion graph formula. The exact lattice checks cover only eight small configurations. The literature comparison is non-exhaustive, and an equivalent result under another normalization or terminology cannot be entirely ruled out. Independent audit is not performed.

## References

1. S. Ostrovska and M. I. Ostrovskii, *On relations between transportation cost spaces and \(\ell_1\)*, arXiv:1910.03625v1 (2019-10-08), https://arxiv.org/abs/1910.03625.
2. M. Alexander, M. Fradelizi, L. C. García-Lirola and A. Zvavitch, *Geometry and volume product of finite dimensional Lipschitz-free spaces*, arXiv:1911.10642v1 (2019-11-24), https://arxiv.org/abs/1911.10642.
3. A. Higashitani, K. Jochemko and M. Michałek, *Arithmetic aspects of symmetric edge polytopes*, arXiv:1807.07678v1 (2018-07-20), https://arxiv.org/abs/1807.07678.
4. A. D'Alì, E. Delucchi and M. Michałek, *Many faces of symmetric edge polytopes*, arXiv:1910.05193v1 (2019-10-11), https://arxiv.org/abs/1910.05193.
