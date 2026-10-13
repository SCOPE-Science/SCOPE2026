# All two-local half-derivations of the three-dimensional Heisenberg Lie algebra

## Finding

Let \(K\) be any field with \(\operatorname{char}K\ne2\). For the three-dimensional Heisenberg Lie algebra \(H=Kx\oplus Ky\oplus Kz\), with \([x,y]=z\) and \(z\) central, write \(u=(a,b)\in K^2\) and identify \(a x+b y+t z\) with \((u,t)\). A map \(\Delta:H\to H\), not assumed additive, is a two-local \(\frac12\)-derivation if and only if
\[
\Delta(u,t)=(g(u),h(u,t)),
\]
where \(g:K^2\to K^2\) and \(h:K^3\to K\) are **arbitrary homogeneous maps of degree one**:
\[
g(\lambda u)=\lambda g(u),\qquad h(\lambda u,\lambda t)=\lambda h(u,t)
\quad(\lambda\in K).
\]
In particular the induced map on \(H/Kz\) is independent of the input's central coordinate, but need not be additive. No other compatibility between \(g\) and \(h\) is required.

For every odd prime power \(q\), the number of such maps over \(K=\mathbb F_q\) is exactly
\[
\boxed{q^{q^2+3q+3}}.
\]
Exactly \(q^7\) of these maps are linear, and exactly \(q^6\) are genuine linear \(\frac12\)-derivations. Thus the number of nonlinear two-local \(\frac12\)-derivations is \(q^{q^2+3q+3}-q^7\).

## Assumptions and scope

The term \(\frac12\)-derivation means a **linear** \(K\)-map \(D:H\to H\) satisfying
\[
D([v,w])=\frac12\bigl([D(v),w]+[v,D(w)]\bigr)
\quad\text{for all }v,w\in H.
\]
The map \(\Delta\) is **two-local** when for every ordered pair \(v,w\in H\), there exists such a linear \(D_{v,w}\) with \(\Delta(v)=D_{v,w}(v)\) and \(\Delta(w)=D_{v,w}(w)\). The field need not be finite or algebraically closed. In positive characteristic, the only restriction is \(\operatorname{char}K\ne2\); the counting assertion additionally assumes \(K=\mathbb F_q\), so \(q\) is odd.

## Proof

**Linear half-derivations.** Every such \(D\) has, and conversely every choice in the following formula gives, the form
\[
D_{B,\ell}(u,t)=\left(Bu,\ell(u)+\tau t\right),\qquad
\tau=\frac12\operatorname{tr}B,
\]
with \(B\in M_2(K)\) arbitrary and \(\ell\in(K^2)^*\) arbitrary. To establish necessity, \(D(z)\) is the image under \(D\) of \([x,y]\) and hence lies in \(Kz\); direct evaluation of the defining identity at \((x,y)\) gives its coefficient \((B_{11}+B_{22})/2\). The remaining bracket identities with \(z\) vanish and impose no further conditions. There are exactly six free field parameters.

**Necessity for two-local maps.** Applying the two-local definition to \(v\) and \(\lambda v\) forces \(\Delta(\lambda v)=\lambda\Delta(v)\) for every \(\lambda\in K\), including \(\lambda=0\). For fixed \(u\in K^2\) and arbitrary \(s,t\in K\), applying it to \((u,s),(u,t)\) gives the same projected output \(Bu\) at both points. Thus the first two coordinates of \(\Delta(u,t)\) define a single function \(g(u)\), independent of \(t\). The last coordinate defines \(h(u,t)\). Homogeneity of \(\Delta\) forces precisely the two displayed homogeneity identities.

**Sufficiency for every pair.** Fix \(v=(u,s)\), \(w=(v_0,t)\), and write \(\kappa=h(0,1)\). Two elementary facts hold: for \(u\ne0\), one can prescribe \(Bu=g(u)\) and \(\operatorname{tr}B=2\tau\) for *any* \(\tau\in K\) by choosing a basis beginning with \(u\); and a linear functional \(\ell\) can be prescribed independently on any two independent vectors.

If \(u,v_0\) are independent, choose the unique \(B\) with \(Bu=g(u)\), \(Bv_0=g(v_0)\), set \(\tau=\operatorname{tr}B/2\), and choose \(\ell\) so that \(\ell(u)=h(u,s)-\tau s\) and \(\ell(v_0)=h(v_0,t)-\tau t\). These choices give \(D_{B,\ell}\) realizing both outputs.

If \(u=v_0=0\), homogeneity gives \(h(0,s)=\kappa s\) and \(h(0,t)=\kappa t\). Choose any \(B\) of trace \(2\kappa\) and any \(\ell\). If exactly one projected vector vanishes, choose \(B\) taking the nonzero projected vector to its \(g\)-image and of trace \(2\kappa\); adjust \(\ell\) on that nonzero vector to realize its prescribed central output. This also realizes the point on the center.

It remains to suppose \(u\ne0\) and \(v_0=\lambda u\) for some nonzero \(\lambda\). If \(t=\lambda s\), homogeneity makes the two prescribed values proportional. Choose any \(B\) sending \(u\) to \(g(u)\) and then choose \(\ell(u)=h(u,s)-\operatorname{tr}(B)s/2\). If \(t\ne\lambda s\), put
\[
\tau=\frac{h(\lambda u,t)-\lambda h(u,s)}{t-\lambda s}.
\]
Take \(B\) with \(Bu=g(u)\) and \(\operatorname{tr}B=2\tau\), and put \(\ell(u)=h(u,s)-\tau s\). Since \(\ell(\lambda u)=\lambda\ell(u)\) and \(g(\lambda u)=\lambda g(u)\), the resulting \(D_{B,\ell}\) has both required values. The cases exhaust all pairs.

**Exact finite-field count.** Every degree-one homogeneous map \(K^d\to K^m\) is uniquely determined by freely choosing its value at one representative of each one-dimensional subspace of \(K^d\): homogeneity determines all its other values, including zero. There are \((q^d-1)/(q-1)\) such projective directions, hence \(q^{m(q^d-1)/(q-1)}\) homogeneous maps. Choosing \(g\) contributes \(q^{2(q+1)}\); choosing \(h\) contributes \(q^{q^2+q+1}\). Their product gives the stated exponent. A linear map has the specified form exactly when its two projected output coordinates ignore the central input, yielding four coefficients for \(B\), two for \(\ell\), and an independent one for the central scaling, hence \(q^7\). The genuine half-derivations obey the additional single relation \(\tau=\operatorname{tr}(B)/2\), hence \(q^6\).

## Verification

Execute `python3 verify.py` from the directory containing the standalone accompanying script. It exhausts the \(q^6\) candidate linear half-derivations for \(q=3,5\), verifies the half-derivation identity on all basis pairs, checks over 100,000 two-point interpolation conditions for random homogeneous maps, exhausts all ordered pairs for explicit non-additive and linear-but-not-half-derivation examples, confirms a deliberately invalid map fails, and computes projective-direction counts. Successful execution terminates with `VERIFY_OK`. The proof, rather than finite testing, establishes the theorem for all fields of characteristic different from two.

## Relationship to prior work

Arzikulov–Shodiev, arXiv:2610.01556v1, study local and two-local half-derivations on totally graded filiform Lie algebras, including \(m_0(3)\cong H\). Their Theorem 24 constructs nonlinear examples by adding a central homogeneous function of two abelianized variables to the identity. Their Section 5 does not give an if-and-only-if classification of every two-local map, nor any finite-field cardinality. Their displayed Theorem 7 half-derivation matrix for \(m_0(n)\) restricts the \(e_1\)-component of the image of \(e_2\), whereas at \(n=3\) the direct bracket identity allows an arbitrary \(2\times2\) projected block. The present proof determines this smallest-dimensional boundary directly rather than relying on that formula.

Khudoyberdiyev–Yusupov, arXiv:2402.09818v1, treat larger solvable Lie algebras whose nilradicals can be Heisenberg; their results for these extensions do not classify two-local half-derivations of the isolated three-dimensional nilpotent algebra. Guo–Kaygorodov–Tang, *Mathematics* 12 (2024), 802, treat the infinite-dimensional mirror Heisenberg–Virasoro Lie algebra, not \(H\). A related prior center–abelianization construction produces nonadditive examples for broad Lie-algebra classes, including \(H\), but implies neither the converse structural classification nor the finite-field count here.

## Limitations

No assertion is made in characteristic two, where the coefficient \(\frac12\) does not exist. The exact counting formula is for finite fields of odd cardinality, not all fields. The accompanying finite computations test examples and the linear half-derivation parametrization; they do not enumerate the astronomical set of nonlinear two-local maps. The proof does not classify higher-dimensional Heisenberg or arbitrary filiform Lie algebras. Novelty cannot be certified merely by unsuccessful search; an older, differently phrased operator-interpolation theorem may conceivably subsume the classification.

## References

1. F. Arzikulov and M. Shodiev, *Local and 2 local 1/2-derivation of n-dimensional totally graded filiform Lie algebras*, arXiv:2610.01556v1 (first public 2026-10-01), especially Sections 3.1 and 5, Theorems 7 and 24. https://arxiv.org/html/2610.01556v1
2. A. Kh. Khudoyberdiyev and B. B. Yusupov, *Local and 2-Local 1/2-Derivations on Finite-Dimensional Lie Algebras*, arXiv:2402.09818v1 (2024), especially its Heisenberg-nilradical solvable-algebra section. https://arxiv.org/abs/2402.09818
3. X. Guo, I. Kaygorodov, and L. Tang, *Maps on the Mirror Heisenberg–Virasoro Algebra*, Mathematics 12 (2024), 802. https://doi.org/10.3390/math12060802
