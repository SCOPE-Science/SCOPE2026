# Arbitrarily Hilbert-close uniformly convex renormings with an unbounded nonexpansive fixed-point set

## Finding
For every \(\eta>0\) there exists a **2-uniformly convex** equivalent norm on the real Hilbert vector space \(\mathbb R\oplus\ell_2\) at distortion strictly below \(1+\eta\) from its Hilbert norm, and a single fixed unbounded closed convex subset with the fixed-point property for **every** nonexpansive selfmap in that norm. The subset does not depend on the renorming parameter.

Specifically, let \(\beta>0\) and define
\[
\gamma(s,x)=\sup\bigl\{|s+\langle x,u\rangle|:\ u_j\ge0,\ \|u\|_2\le1\bigr\},\qquad
N_\beta(s,x)=\bigl(s^2+\|x\|_2^2+\beta\gamma(s,x)^2\bigr)^{1/2}.
\]
If \(0<\beta<((1+\eta)^2-1)/2\), then
\[
\|(s,x)\|_2\le N_\beta(s,x)\le\sqrt{1+2\beta}\,\|(s,x)\|_2<(1+\eta)\|(s,x)\|_2
\]
for every nonzero \((s,x)\). The same set
\[
C=\bigl\{(s,x):s\ge0,\ x_j\ge0\ (j\ge1),\ s+\langle w,x\rangle=1\bigr\},\quad w=(2^{-j})_{j\ge1},
\]
has the fixed-point property for all nonexpansive selfmaps \(C\to C\) with respect to \(N_\beta\), for **each** \(\beta>0\).

## Assumptions and scope
All spaces and maps are real. \(\ell_2=\ell_2(\mathbb N;\mathbb R)\). The positive cone is coordinatewise, and the auxiliary vectors \(u\) range over its closed unit ball. The Hilbert norm on the product is \(\|(s,x)\|_2=(s^2+\|x\|_2^2)^{1/2}\). For a normed space \(Y\), its modulus of convexity is
\[
\delta_Y(\varepsilon)=\inf\left\{1-\left\|\frac{h+k}{2}\right\|_Y:\ \|h\|_Y=\|k\|_Y=1,\ \|h-k\|_Y\ge\varepsilon\right\}\quad(0<\varepsilon\le2).
\]
Nonexpansive means \(N_\beta(Tz-Tz')\le N_\beta(z-z')\) for every \(z,z'\in C\). The statement concerns one particular family of (possibly nonsmooth) uniformly convex norms, not arbitrary renormings.

## Proof
**1. Norm and quadratic uniform convexity.** Each map \((s,x)\mapsto s+\langle x,u\rangle\) is linear and uniformly bounded in Hilbert norm; its supremum of absolute values, \(\gamma\), is a continuous seminorm. Writing \(x_+\) and \(x_-\) for the coordinatewise positive and negative parts, respectively, gives the exact formula
\[
\gamma(s,x)=\max\{\,|s+\|x_+\|_2|,\ |s-\|x_-\|_2|\,\}.
\]
Indeed, as \(u\) ranges over the positive Hilbert unit ball, \(\langle x,u\rangle\) ranges over the interval \([-\|x_-\|_2,\|x_+\|_2]\). Furthermore, \(\gamma(s,x)\le|s|+\|x\|_2\le\sqrt2\|(s,x)\|_2\). Thus \(N_\beta\) is a complete norm equivalent to the Hilbert norm and obeys the claimed distortion bounds.

The function \(\gamma^2\) is convex (as the square of a nonnegative convex seminorm). The Hilbert parallelogram law therefore gives, for arbitrary \(h,k\),
\[
N_\beta\bigl((h+k)/2\bigr)^2\le\frac{N_\beta(h)^2+N_\beta(k)^2}{2}-\frac{\|h-k\|_2^2}{4}.
\]
For \(N_\beta(h)=N_\beta(k)=1\) with \(N_\beta(h-k)\ge\varepsilon\), we obtain
\[
N_\beta\bigl((h+k)/2\bigr)^2\le1-\frac{\varepsilon^2}{4(1+2\beta)},\qquad
\delta_{N_\beta}(\varepsilon)\ge1-\sqrt{1-\frac{\varepsilon^2}{4(1+2\beta)}}\ge\frac{\varepsilon^2}{8(1+2\beta)}.
\]
In particular \((X,N_\beta)\) has the fixed-point property on all nonempty bounded closed convex sets by the standard Browder–Göhde–Kirk theorem.

**2. Unbounded positive slice.** The set \(C\) is nonempty (it contains \(p=(1,0)\)), closed and convex. Every \(z=(s,x)\in C\) satisfies \(0\le s\le1\). For the standard unit vectors \(e_j\), the points \(q_j=(0,2^je_j)\) belong to \(C\) and satisfy \(N_\beta(q_j)=2^j\sqrt{1+\beta}\to\infty\). Hence \(C\) is unbounded.

**3. Localization at the distinguished point.** Fix \(y=(b,v)\in C\setminus\{p\}\). Since \(v_j\ge0\) and all \(w_j>0\),
\[
d_y:=1-b=\langle w,v\rangle>0.
\]
We show that the Kirk–Ray localization set
\[
G_C(p,y)=\{z\in C:N_\beta(z-y)\le N_\beta(z-p)\}
\]
is bounded. Suppose instead there is a sequence \(z_n=(s_n,x_n)\in G_C(p,y)\) with \(N_\beta(z_n)\to\infty\). Since \(0\le s_n\le1\) and \(N_\beta\) is equivalent to the Hilbert norm, \(r_n=\|x_n\|_2\to\infty\). Put
\[
d_n=1-s_n=\langle w,x_n\rangle\in[0,1],\qquad g_n=x_n/r_n\in\ell_2^+,\qquad\|g_n\|_2=1.
\]
For every fixed \(j\), \(0\le(g_n)_j\le (r_n w_j)^{-1}\to0\). Since \(\{g_n\}\) is bounded in \(\ell_2\), coordinatewise convergence yields \(g_n\rightharpoonup0\). In particular \(\langle g_n,v\rangle\to0\).

For sufficiently large \(n\), \(r_n\ge2\). Define \(h_n=z_n-p=(-d_n,x_n)\), \(m_n=r_n-d_n>0\), and the linear functional \(\ell_n(s,x)=s+\langle x,g_n\rangle\). Because the scalar products \(\langle x_n,u\rangle\) with positive unit-ball vectors cover exactly \([0,r_n]\),
\[
\gamma(h_n)=\max\{d_n,r_n-d_n\}=m_n=\ell_n(h_n),\qquad |\ell_n(k)|\le\gamma(k)
\]
for every \(k\in X\). Here the equality \(r_n-d_n\ge d_n\) uses \(r_n\ge2\) and \(d_n\le1\).

Define the explicit support functional
\[
F_n(k)=\frac{\langle h_n,k\rangle_2+\beta m_n\ell_n(k)}{N_\beta(h_n)},\qquad k\in X.
\]
It is norm-one in \((X,N_\beta)^*\): the Cauchy–Schwarz inequality in \(\mathbb R^2\), together with \(|\ell_n(k)|\le\gamma(k)\), gives
\[
|F_n(k)|\le\frac{\|h_n\|_2\|k\|_2+\beta m_n\gamma(k)}{N_\beta(h_n)}\le N_\beta(k),\qquad F_n(h_n)=N_\beta(h_n).
\]
Writing \(k=p-y=(d_y,-v)\) gives the exact quotient
\[
F_n(p-y)=\frac{-d_n d_y-r_n\langle g_n,v\rangle+\beta(r_n-d_n)\bigl(d_y-\langle g_n,v\rangle\bigr)}{\bigl(r_n^2+d_n^2+\beta(r_n-d_n)^2\bigr)^{1/2}}.
\]
Divide numerator and denominator by \(r_n\). Because \(d_n/r_n\to0\) and \(\langle g_n,v\rangle\to0\), we obtain the **strictly positive** limit
\[
F_n(p-y)\longrightarrow\frac{\beta d_y}{\sqrt{1+\beta}}>0.
\]
On the other hand, since \(z_n\in G_C(p,y)\) and \(h_n=z_n-p\), the support inequality gives
\[
0\ge N_\beta(z_n-y)-N_\beta(z_n-p)\ge F_n(h_n+p-y)-F_n(h_n)=F_n(p-y),
\]
a contradiction. Hence \(G_C(p,y)\) is bounded for every \(y\ne p\).

**4. Fixed point conclusion.** The Kirk–Ray localization theorem states that if a Banach space has the fixed-point property on bounded closed convex subsets and \(G_C(p,Tp)\) is bounded for a nonexpansive \(T:C\to C\), then \(T\) has a fixed point. For any such \(T\), either \(Tp=p\) already or Step 3 applies to \(y=Tp\); Step 1 supplies the ambient bounded-set property. The theorem follows for all \(\beta>0\), and choosing \(\beta\) small establishes arbitrary Hilbert closeness. \(\square\)

## Verification
The norm is explicitly computable from positive and negative parts by the formula in Step 1. Every inequality in the proof follows from the Hilbert parallelogram law, the seminorm triangle inequality, Cauchy–Schwarz, and positivity of the coordinates of \(w\). The key asymptotic limit is a rigorous weak-convergence argument: bounded coordinatewise-null sequences are weakly null in \(\ell_2\), and division by \(r_n\) leaves the strictly positive quantity \(\beta d_y/\sqrt{1+\beta}\). This analytical verification covers infinite dimensions; no finite experiment is asserted to certify the fixed-point theorem. The only imported non-elementary ingredients are the classical bounded-set fixed-point theorem for uniformly convex Banach spaces and the Kirk–Ray localization theorem, with statements specified above and cited below.

## Relationship to prior work
Japón and Laguna-Ricart (2026) construct the same positive affine slice in a renormed Hilbert space with the fixed-point property for nonexpansive mappings, using a maximum of two gauges and a normal-structure estimate. Their stated norm is not shown to be uniformly convex and has a fixed distortion bound. The new quadratic-sum norm retains their localization mechanism for **every positive perturbation size**, gives an explicit power-type-two convexity modulus, and approaches the original Hilbert norm arbitrarily closely. Thus the result does not merely restate their existence theorem for an isomorphic Hilbert space.

Ray's classical theorem excludes unbounded closed convex fixed-point sets in the genuine Hilbert norm. Saejung (2010) treats a different family of firmly nonexpansive-like maps in **smooth, strictly convex, reflexive** spaces; the norm here need not be smooth. Indeed at \((1,0)\), for a fixed positive basis direction \((0,e_1)\), the right and left directional derivatives of the \(\gamma^2\) contribution differ, since \(\gamma(1,te_1)=1+t\) for \(t>0\) and \(\gamma(1,te_1)=1\) for small \(t<0\). The smooth-space restriction of that earlier theorem is therefore not met, and its maps are not interchangeable with ordinary nonexpansive maps.

## Limitations
The norm is an **explicitly nonsmooth** but uniformly convex renorming; smooth or uniformly smooth analogues are not established. The same fixed set works for each \(\beta>0\), but the class of nonexpansive maps depends on \(\beta\). Exactly at \(\beta=0\), the norm is Hilbert and Ray's theorem rules out this conclusion. No assertion about all norms sufficiently close to Hilbert, or about a common fixed point for an arbitrary family of maps, is made. Historical-priority searches and public-result-index comparisons do not establish global uniqueness; related constructions outside the inspected literature may exist.

## References
1. M. Japón and J. Laguna-Ricart, *An Unbounded Convex Set with the Fixed Point Property for Nonexpansive Mappings*, arXiv:2610.14868v1, first posted 2026-10-10. https://arxiv.org/html/2610.14868v1
2. W. A. Kirk and W. O. Ray, *Fixed-point theorems for mappings defined on unbounded sets in Banach spaces*, Studia Mathematica 64 (1979), 127–138. https://doi.org/10.4064/sm-64-2-127-138
3. W. O. Ray, *The fixed point property and unbounded sets in Hilbert space*, Transactions of the American Mathematical Society 258 (1980), 531–537. https://doi.org/10.1090/S0002-9947-1980-0558189-1
4. S. Saejung, *Ray's Theorem for Firmly Nonexpansive-Like Mappings and Equilibrium Problems in Banach Spaces*, Fixed Point Theory and Applications (2010), article 806837. https://doi.org/10.1155/2010/806837
5. J. García-Falset, *Fixed points of continuous nonlinear mappings in Banach spaces*, Journal of Fixed Point Theory and Applications 27 (2025), article 63. https://doi.org/10.1007/s11784-025-01217-z
