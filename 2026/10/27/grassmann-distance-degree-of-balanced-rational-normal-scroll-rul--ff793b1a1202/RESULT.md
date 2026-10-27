# Grassmann distance degree of balanced rational-normal-scroll rulings

## Finding

For every integer \(m\ge2\), consider the smooth rational-normal surface scroll \(S(m,m)\subset\mathbb P^{2m+1}_{\mathbb C}\) and its curve \(\mathcal R_m\) of ruling lines, viewed in the complex orthogonal-projection Grassmannian \(\operatorname{pGr}(2,2m+2)\). Then

\[
\boxed{\operatorname{GDdeg}(\mathcal R_m)=\operatorname{EDdeg}(\mathcal R_m)=4m-2.}
\]

For a general projection data point, all these \(4m-2\) critical points are distinct, regular points of the ruling curve, and lie outside the algebraic cut locus. The ED equality is already established by Friedman–Hoşten–Rosana; the new statement is the GD computation and the absence of cut-locus critical points.

## Assumptions and scope

Work over \(\mathbb C\) with its nondegenerate **bilinear** dot product, not a Hermitian form. Write \(V=\mathbb C^{m+1}\oplus\mathbb C^{m+1}\), \(v(t)=(1,t,\ldots,t^m)\), and \(s(t)=1+t^2+\cdots+t^{2m}\). The parameterized ruling plane is \(U_t=\langle(v(t),0),(0,v(t))\rangle\). For \(s(t)\ne0\), its orthogonal projector is

\[
P(t)=\operatorname{diag}\!\left(\frac{v(t)^\top v(t)}{s(t)},\frac{v(t)^\top v(t)}{s(t)}\right).
\]

The missing parameters are precisely the zeros of \(s\); the parameter \(t=\infty\) is included using \(u=1/t\). This gives the smooth projection-Grassmannian model \(\mathcal R_m\). A data point \(Q\) is a general rank-two symmetric idempotent matrix. The **GD degree** is the number of critical points of \(\operatorname{tr}(PQ)\) on the smooth model after removing \(\operatorname{cut}(Q)=\{P:\operatorname{rank}(QP)<2\}\). A general data point means outside a proper complex algebraic subset; the real locus is Zariski dense.

## Proof

**1. Trace objective.** Represent \(Q=uu^\top+ww^\top\) with \(u^\top u=w^\top w=1\) and \(u^\top w=0\). Split \(u=(a,c)\), \(w=(b,d)\) across the two blocks and regard \(a,b,c,d\) as polynomials of degree at most \(m\) formed from their coordinate vectors. Then

\[
F_Q(t)=\operatorname{tr}(P(t)Q)=\frac{f_Q(t)}{s(t)},\qquad
f_Q(t)=a(t)^2+b(t)^2+c(t)^2+d(t)^2.
\]

We prove that the map from the orthogonal two-frame variety to the coefficient space of all polynomials of degree at most \(2m\), \((u,w)\mapsto f_Q\), is **dominant**. Choose the frame

\[
u_0=\frac{(e_0,e_1)}{\sqrt2},\qquad w_0=\frac{(e_m,e_0)}{\sqrt2},\]

where \(e_j\) is the standard coordinate vector in \(\mathbb C^{m+1}\). These vectors are orthonormal for \(m\ge2\). Write perturbations of the four polynomial blocks as \((\alpha,\beta,\gamma,\delta)\) in the order \((a,c,b,d)\). Linearized orthonormality gives exactly

\[
\alpha_0+\beta_1=0,\quad \gamma_m+\delta_0=0,\quad
\alpha_m+\beta_0+\gamma_0+\delta_1=0.
\]

Up to a nonzero scalar, the differential of the numerator map is

\[
\mathcal L(\alpha,\beta,\gamma,\delta)=\alpha+t\beta+t^m\gamma+\delta.
\]

Without the three linear constraints this map is onto the \((2m+1)\)-dimensional polynomial space: \(\alpha\) covers degrees \(0\) through \(m\), and \(t^m\gamma\) covers degrees \(m\) through \(2m\). The kernel of \(\mathcal L\) contains the three vectors

\[
(-t,1,0,0),\quad(-t^2,t,0,0),\quad(-1,0,0,1).
\]

Their constraint-value triples are respectively \((0,0,1)\), \((1,0,-1)\) when \(m=2\) and \((1,0,0)\) otherwise, and \((-1,1,0)\). They are linearly independent in every case \(m\ge2\). Thus the three constraints can be corrected by elements of \(\ker\mathcal L\) without changing the requested output polynomial. Therefore the differential restricted to the tangent space of the orthogonal-frame variety is surjective, and the numerator map is dominant. Because changing the frame by an orthogonal matrix leaves \(Q\) and \(f_Q\) unchanged, this is also dominance for projection data matrices.

**2. Critical-point count.** For generic \(Q\), \(f_Q\) is a generic polynomial of degree \(2m\), by dominance. Differentiation gives

\[
F'_Q(t)=\frac{H_Q(t)}{s(t)^2},\qquad
H_Q(t)=f'_Q(t)s(t)-f_Q(t)s'(t).
\]

Both \(f_Q\) and \(s\) have degree \(2m\); their top derivatives cancel, leaving degree at most \(4m-2\). The coefficient of \(t^{4m-2}\) is the negative of the coefficient of \(t^{2m-1}\) in \(f_Q\), so generically \(\deg H_Q=4m-2\). The polynomial \(s\) has \(2m\) simple nonzero roots; indeed \((t^2-1)s(t)=t^{2m+2}-1\), and the roots \(t=\pm1\) cancel. Generically \(f_Q\) is nonzero at each root of \(s\), hence \(\gcd(H_Q,s)=1\). The discriminant of \(H_Q\) is not identically zero: for any \(t\) with \(s(t)\ne0\), the two equations \(H_Q(t)=H'_Q(t)=0\) impose independent linear conditions on the free coefficients of \(f_Q\) (vary its first and second jets). Their incidence over one parameter has proper image in coefficient space. Thus \(H_Q\) is generically squarefree, and its \(4m-2\) roots are finite, regular and away from the poles. Since \(\deg H_Q=4m-2\), no critical point occurs at \(t=\infty\): in the coordinate \(u=1/t\), the first derivative at \(u=0\) is generically nonzero.

**3. Excluding the cut locus.** Fix a parameter \(t\) with \(s(t)\ne0\). Let \(U=U_t\) and regard \(Q\) as a nondegenerate two-plane \(W\subset V\). The condition \(\operatorname{rank}(QP(t))<2\) is the Schubert-divisor condition \(W\cap U^\perp\ne0\). This is an irreducible divisor in the Grassmannian of two-planes. The derivative \(\operatorname{tr}(P'(t)Q)\) does not vanish identically on that divisor: because \(t\mapsto U_t\) is immersive, choose \(e\in U\) and \(z\in U^\perp\) with \(z^\top P'(t)e\ne0\), then a nondegenerate two-plane \(W\) generated by a suitable mixed vector \(e+z\) and a suitable orthogonal vector in \(U^\perp\) lies on the divisor and has \(\operatorname{tr}(P'(t)Q)\ne0\). There is room for the latter choice because \(\dim U^\perp=2m\ge4\). Thus simultaneous criticality and cut membership impose at least two independent conditions on \(Q\) for fixed \(t\). Allowing \(t\) to vary over a curve leaves a proper condition on \(Q\). Generic critical points therefore avoid \(\operatorname{cut}(Q)\).

Each finite critical parameter gives a different point of the ruling curve: the first rank-one diagonal block recovers the line \(\mathbb Cv(t)\), and hence \(t\). Altogether there are exactly \(4m-2\) GD-critical points.

**4. ED comparison.** Theorem 2.2 of Friedman–Hoşten–Rosana calculates the ED degree of the ruling curve of \(S(m,m)\) as \(2\deg s-2=4m-2\), yielding the asserted equality.

## Verification

The accompanying standalone `checker.py` uses exact SymPy rational arithmetic. For \(m=2,3,4,5\) it constructs genuine rank-two projection data from two normalized vectors supported on the respective coordinate blocks, computes the full critical polynomial, and verifies its degree \(4m-2\), squarefreeness, coprimality with \(s\), and absence of cut-locus critical points. These special computations independently check examples; the dominance, incidence, and genericity arguments above prove the formula for all integers \(m\ge2\).

## Relationship to prior work

Friedman, Hoşten and Rosana, *Euclidean Distance Optimization Within the Grassmannian*, arXiv:2610.02018, Section 2 and Theorem 2.2, introduce the scroll-ruling model and compute its ED degree. Their Section 4 defines GD degree and the algebraic cut locus, but does not determine the GD degree of those scroll curves. Friedman, Rosana and Sturmfels, *Distance Optimization in the Grassmannian of Lines*, arXiv:2601.22843, develops GD degree for line Grassmannians and specific other models but does not provide this balanced-scroll computation. The present result tests exactly whether restricting the data to projection matrices changes the critical count for an infinite natural family, and proves that it does not.

## Limitations

The theorem concerns **balanced surface scrolls** \(S(m,m)\), with \(m\ge2\), and their ruling curves. It does not classify the GD degree of all unbalanced scrolls or higher-dimensional scrolls, and does not enumerate real critical points. It uses the non-Hermitian complex bilinear extension standard for algebraic ED/GD degree. The checker is finite illustrative evidence, not a substitute for the general proof. Historical priority remains subject to discovery of older equivalent results, including unindexed computations.

## References

- H. Friedman, S. Hoşten and A. Rosana, *Euclidean Distance Optimization Within the Grassmannian*, arXiv:2610.02018v1 (2026-10-01), especially Theorem 2.2 and Definition/Proposition 4.2. Full text: https://arxiv.org/html/2610.02018v2.
- H. Friedman, A. Rosana and B. Sturmfels, *Distance Optimization in the Grassmannian of Lines*, arXiv:2601.22843v1 (2026-01-30), especially the GD-degree framework. Full text: https://arxiv.org/html/2601.22843v1.
