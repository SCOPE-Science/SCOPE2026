# Wild cusps and tame normalizations of Hurwitz plane curves at bad primes

## Finding
Let \(n\ge2\) be any integer and let \(p\) be a prime dividing \(N=n^2-n+1\). Write \(N=p^eM\), where \(e\ge1\) and \(p\nmid M\). Over \(\mathbb F_p\), consider the plane Hurwitz curve
\[
H_n:\quad X^nY+Y^nZ+Z^nX=0\quad\subset\mathbb P^2.
\]
This curve is geometrically integral. Over an algebraic closure it has exactly \(M\) singular points. Each is geometrically unibranch, and its completed local ring is isomorphic to
\[
\overline{\mathbb F}_p[[u,v]]/(v^2-u^{p^e}).
\]
In particular, each singularity has delta invariant \((p^e-1)/2\); the normalization \(\widetilde H_n\) has genus \((M-1)/2\). The normalization is isomorphic, as a smooth projective curve over \(\mathbb F_p\), to the smooth completion of the tame Kummer curve
\[
W_n:\quad w^M=(-1)^{n+1}\frac{t^n}{1-t}.
\]
The normalization map is bijective on \(\mathbb F_{p^r}\)-points for every \(r\ge1\), hence
\[
Z(H_n/\mathbb F_p,T)=Z(\widetilde H_n/\mathbb F_p,T).
\]
If \(M=1\), the normalization is \(\mathbb P^1\) and \(\#H_n(\mathbb F_{p^r})=p^r+1\) for every positive \(r\).

## Assumptions and scope
Here \(n\) is an integer at least two, \(N=n^2-n+1\), \(p\mid N\), and \(e=v_p(N)\). As \(N\) is odd, the bad prime \(p\) is odd. The word singularity denotes a geometric singular point of the reduced plane curve, not merely an arithmetic rational point. Local equations and delta invariants are over \(k=\overline{\mathbb F}_p\). An isomorphism of smooth projective models means an isomorphism of their function fields over the stated constant field. The assertion about zeta functions concerns the potentially singular projective plane curve itself, not a semistable model.

## Proof
**1. Irreducible torus equation.** Work in the chart \(Z=1\), where \(F=x^ny+y^n+x\). On the dense coordinate torus put \(t=-x^{n-1}y\). Then \(y=-t/x^{n-1}\), and substitution gives the exact relation
\[
x^N(1-t)=(-1)^{n+1}t^n.\tag{1}
\]
Conversely, a solution of (1) with \(x,t,1-t\ne0\) recovers a point on \(F=0\) by that formula for \(y\). The right-hand rational function \(f(t)=(-1)^{n+1}t^n/(1-t)\) has a simple pole at \(t=1\). Hence \(X^N-f(t)\) is irreducible in \(k(t)[X]\): its reciprocal is Eisenstein at the discrete valuation \(t=1\). Thus the torus part is geometrically integral; no coordinate line is a component of \(H_n\), so the whole curve is geometrically integral.

**2. Exhaustive singular locus.** From \(F=x^ny+y^n+x\), the three projective points where at least one coordinate vanishes are \([1:0:0]\), \([0:1:0]\), \([0:0:1]\), all smooth (the respective linear terms in an appropriate local chart are nonzero). On the torus, the change of coordinates \((x,y)\mapsto(x,t)\) is étale because its Jacobian determinant in the \(y\)-direction is \(-x^{n-1}\ne0\). Write the local equation as \(G(x,t)=x^N-f(t)=0\). Since \(p\mid N\), \(\partial G/\partial x=0\), so singular points occur exactly at zeros of \(f'(t)\). Direct differentiation gives
\[
f'(t)=(-1)^{n+1}\frac{t^{n-1}(n-(n-1)t)}{(1-t)^2}.
\]
The congruence \(n(n-1)\equiv-1\pmod p\) ensures \(p\nmid n(n-1)\). There is therefore precisely one critical torus parameter \(t_0=n/(n-1)\) in \(\mathbb F_p\), with \(t_0\ne0,1\). The nonzero equation \(x^N=f(t_0)\) has exactly \(M\) distinct geometric solutions, because \(N=p^eM\) and \(p\nmid M\). This lists every geometric singular point.

**3. Exact completed local type.** The above critical point is simple: the numerator \(n-(n-1)t\) of \(f'(t)\) vanishes to first order and its other factors are units at \(t_0\). Therefore
\[
f(t)-f(t_0)=(t-t_0)^2h(t-t_0),\qquad h(0)\ne0.
\]
Fix a singular point \((x_0,t_0)\). The parameter \(u=x^M-x_0^M\) is a regular local coordinate because \(Mx_0^{M-1}\ne0\), and \(x^N-x_0^N=u^{p^e}\). Since \(p\ne2\), the formal unit \(h\) has a square root after a harmless constant-field extension (already included in \(k\)). Set \(v=(t-t_0)\sqrt{h(t-t_0)}\). Equation (1) now reads \(u^{p^e}=v^2\) in the completed local ring. Because \(p^e\) is odd, this is a single branch parametrized by \(u=s^2\), \(v=s^{p^e}\). Its local normalization is \(k[[s]]\) and its conductor length (delta invariant) is \(\dim_k k[[s]]/k[[s^2,s^{p^e}]]=(p^e-1)/2\).

**4. Normalization as a tame cover.** Let \(K=\mathbb F_p(H_n)=\mathbb F_p(x,t)\) be the function field of (1), and put \(w=x^{p^e}\). Then \(L=\mathbb F_p(t,w)\subset K\) has equation \(w^M=f(t)\). This is a separable degree-\(M\) Kummer extension of \(\mathbb F_p(t)\), since \(p\nmid M\) and \(f\) has valuation \(-1\) at \(t=1\). In \(L\), the valuation of \(w\) at its unique point above \(t=1\) is \(-1\); in particular \(w\) is not a \(p\)-th power. Consequently \([K:L]=p^e\) via \(x^{p^e}=w\). On the other hand, for a one-variable function field over the perfect field \(\mathbb F_p\), \([K:K^{p^e}]=p^e\). As \(K^{p^e}\subseteq L\), equality of these indices gives \(K^{p^e}=L\). The \(p^e\)-Frobenius is an isomorphism of \(\mathbb F_p\)-function fields \(K\simeq L\), proving the asserted isomorphism of smooth projective models.

The Kummer map \(W_n\to\mathbb P^1_t\) has degree \(M\). The orders of \(f\) at \(t=0,1,\infty\) are \(n,-1,1-n\), respectively; each is coprime to \(M\) because \(M\mid n^2-n+1\). For \(M>1\), these are three totally tamely ramified points and there is no other ramification; for \(M=1\), each ramification index is one. Riemann--Hurwitz gives
\[
2g(\widetilde H_n)-2=-2M+3(M-1)=M-3,
\]
so \(g=(M-1)/2\), also agreeing with the independent plane-genus check \(g_a(H_n)-M\delta=(N-1)/2-M(p^e-1)/2\).

**5. Finite-field points and zeta.** Each singularity is geometrically unibranch; the normalization has precisely one geometric point over it. The normalization is an isomorphism away from the singular locus. Since the map is defined over \(\mathbb F_p\), it is a bijection on geometric points compatible with Frobenius, hence a bijection on the fixed-point sets of every Frobenius power, i.e. on \(\mathbb F_{p^r}\)-points for all \(r\ge1\). Equal counts in every extension give equal zeta functions. If \(M=1\), the Kummer cover has degree one, hence \(\widetilde H_n\simeq\mathbb P^1\) and the asserted point formula follows.

## Verification
The accompanying standalone `verify.py` implements exact modular arithmetic and small finite-field enumerations using only the Python standard library. It tests the polynomial critical point and genus identities, and counts the plane curve and tame-cover points for \((n,p)=(5,3),(5,7),(19,7)\) over the prime and quadratic extension fields. For example, \(n=5,p=7\) gives \(N=21\), \(M=3\), precisely three \(v^2=u^7\) cusps and genus one; the computed counts are \(9\) over \(\mathbb F_7\) and \(63\) over \(\mathbb F_{49}\). For \(n=19,p=7\), \(N=343\), \(M=1\), and a degree-twenty plane curve of arithmetic genus \(171\) has a single cusp with delta \(171\) and rational normalization. These enumerations corroborate the proof; the infinite theorem follows from the algebraic arguments, not from extrapolation of finite experiments.

## Relationship to prior work
Bennama and Carbonne (1997) established a birational Kummer model for Hurwitz curves; the birational-transform formula is explicitly reproduced in Bisogno et al., Section 3.3 (2018). The tame Kummer presentation alone is therefore **not** asserted as new. Montanucci and Speziali (2016), Introduction and Section 4, explicitly restrict to smooth Hurwitz curves with \(p\nmid n^2-n+1\). Bisogno et al. (2018), Sections 2.1 and 3--4, study the smooth/supersingular regime and do not give the wild singularity arrangement at \(p\mid N\). The contribution assessed here is the uniform complete classification of the singular points and their exact formal types for every bad prime (including higher powers), the consequent genus collapse, and the normalization-point/zeta comparison. A previously reported characteristic-seven Klein-quartic cusp is one special case \((n,p)=(3,7)\), not a general theorem.

## Limitations
The geometric singular points need not all be individually rational over \(\mathbb F_p\); only their total geometric number is asserted. No explicit numerator for the zeta function is claimed when \(M>1\); equality with the tame Kummer model is the established statement. The precise 1997 paper by Bennama and Carbonne was identified bibliographically and through its reproduced transformation in a later full-text source, but its original full text was not accessible for complete priority comparison. 

## References
1. M. Montanucci and P. Speziali, *The \(a\)-numbers of Fermat and Hurwitz curves* (first arXiv posting 2016-03-11), arXiv:1603.03604, https://arxiv.org/abs/1603.03604. Read: Introduction, Sections 2 and 4.
2. D. Bisogno, E. Dawson, H. Frauenhoff, M. Lynch, A. Price, R. Pries, S. Somerstep and E. Work, *The Supersingularity of Hurwitz Curves* (first arXiv posting 2018-10-03), arXiv:1810.01582, https://arxiv.org/abs/1810.01582. Read: Sections 2.1, 3.2--3.3, 4.
3. H. Bennama and P. Carbonne, *Courbes \(X^mY^n+Y^mZ^n+Z^mX^n=0\) et décomposition de la jacobienne*, J. Algebra **188** (1997), 409--417. Bibliography and transformation corroborated through reference 2; original full text not inspected.
