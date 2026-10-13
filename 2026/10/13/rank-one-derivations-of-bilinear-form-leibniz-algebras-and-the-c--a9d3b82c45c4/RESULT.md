# Rank-one derivations of bilinear-form Leibniz algebras and the characteristic-two idempotent jump

## Finding

Let \(K\) be any field, let \(n\ge 2\), and let \(B:V\times V\to K\) be a nondegenerate bilinear form on an \(n\)-dimensional vector space. Give \(L_B=V\oplus Kz\) the product
\[
[v+az,w+bz]=B(v,w)z.
\]
Define the intrinsic symmetrization radical
\[
W_B=\{u\in V:B(u,v)+B(v,u)=0\text{ for all }v\in V\},\qquad r=\dim_K W_B.
\]
Every rank-one derivation \(D:L_B\to L_B\) kills \(z\), and exactly one of the following holds:

* **Central type:** \(D(v)=f(v)z\) for a nonzero \(f\in V^*\).
* **Noncentral type:** choose a line \(\ell\subset W_B\), a fixed nonzero representative \(u\in\ell\), and arbitrary \(t\in K^\times\), \(s\in K\); then
\[
D(v)=B(u,v)(tu+sz),\qquad D(z)=0.
\]
Every such choice is a derivation of rank one, and for fixed representatives it is unique. In the second type,
\[
D^2=tB(u,u)D.
\]

For \(K=\mathbf F_q\), the exact number of rank-one derivations is
\[
\boxed{q^n-1+q(q^r-1)}.
\]
If \(q\) is odd, every rank-one derivation is square-zero. If \(q\) is even, put \(Q(u)=B(u,u)\) on \(W_B\). When \(Q|_{W_B}=0\), all rank-one derivations are again square-zero. Otherwise, for **each** \(\lambda\in\mathbf F_q^\times\), precisely \(q^r\) rank-one derivations satisfy \(D^2=\lambda D\). In particular there are exactly \(q^r\) rank-one idempotent derivations and \((q-1)q^r\) non-square-zero rank-one derivations in this case. These counts include every finite characteristic, including characteristic two.
For example, over \(\mathbf F_{2^e}\), the forms with matrices \(I_2\) and \(\begin{pmatrix}0&1\\1&0\end{pmatrix}\) both have \(r=2\), yet the first has exactly \(q^2\) rank-one idempotent derivations and the second has none. Thus the diagonal invariant \(Q|_{W_B}\), rather than \(r\) alone, detects the characteristic-two jump.

## Assumptions and scope

The form \(B\) need not be symmetric or alternating. Nondegenerate means that both induced maps \(V\to V^*\) are isomorphisms. The chosen central line is the whole derived ideal because \(B\ne0\). The multiplication is a two-step nilpotent symmetric Leibniz multiplication (indeed, products land in the annihilating center). Derivation means a \(K\)-linear map satisfying \(D([x,y])=[D(x),y]+[x,D(y)]\). Rank is ordinary \(K\)-linear rank of the map on \(L_B\), not rank of the matrix of \(B\).

The normal form is relative to a fixed splitting \(L_B=V\oplus Kz\), and the counting result is for a fixed bilinear-form algebra rather than an enumeration of isomorphism classes. Rescaling a representative of \(\ell\) changes \((t,s)\), so choosing one representative per line is part of the parametrization.

## Proof

**Step 1 (center and linear blocks).** Since \([L_B,L_B]=Kz\) and derivations preserve this ideal, any derivation satisfies \(D(z)=\lambda z\) and \(D(v)=Av+f(v)z\), with \(A\in\operatorname{End}(V)\) and \(f\in V^*\). Evaluating the derivation identity on \(v,w\in V\) gives
\[
\lambda B(v,w)=B(Av,w)+B(v,Aw)\quad\text{for all }v,w.
\]
If \(D\) has rank one and \(\lambda\ne0\), then \(z\) belongs to the one-dimensional image, forcing \(A=0\); the displayed equation then forces \(\lambda=0\), a contradiction. Thus every rank-one derivation kills \(z\).

**Step 2 (central and noncentral cases).** If \(A=0\), the preceding equation is automatic for any \(f\), and rank one is equivalent to \(f\ne0\). Otherwise \(A\) has rank one. Write \(A(v)=\psi(v)u\) with \(u\ne0\), \(\psi\ne0\). Since the image of \(D\) is one-dimensional, its central coordinate satisfies \(f=c\psi\) for a scalar \(c\). The derivation equation becomes
\[
\psi(v)B(u,w)+\psi(w)B(v,u)=0\quad\text{for every }v,w.
\]
Pick \(v_0\) with \(\psi(v_0)=1\). Substitution of elements of \(\ker\psi\) separately in the first and second slots shows that both \(B(u,-)\) and \(B(-,u)\) vanish on \(\ker\psi\). Therefore \(B(u,-)=a\psi\) and \(B(-,u)=b\psi\). Nondegeneracy gives \(a\ne0\), while the equation at \((v_0,v_0)\) gives \(a+b=0\). Thus \(u\in W_B\), and rewriting \(\psi=a^{-1}B(u,-)\) gives the claimed \((t,s)\)-form with \(t=a^{-1}\ne0\). Conversely, \(u\in W_B\) makes
\[
[D(v),w]+[v,D(w)]=tB(u,w)\bigl(B(u,v)+B(v,u)\bigr)z=0,
\]
so the map is a rank-one derivation. Its noncentral image determines \(\ell=Ku\); after one representative is fixed, the coefficient of \(u\) gives \(t\) uniquely and the central coefficient gives \(s\) uniquely.

**Step 3 (squaring).** For a noncentral map, \(D(u)=B(u,u)(tu+sz)\) and \(D(z)=0\), hence \(D^2=tB(u,u)D\). Central-type maps square to zero. If \(\operatorname{char}K\ne2\), then for \(u\in W_B\), \(2B(u,u)=0\), whence \(D^2=0\).

**Step 4 (finite-field enumeration).** Central-type maps number \(q^n-1\). There are \((q^r-1)/(q-1)\) lines in \(W_B\), and each line contributes \((q-1)q\) distinct noncentral maps, giving the asserted total. In characteristic two the function \(Q(u)=B(u,u)\) on \(W_B\) satisfies \(Q(u+v)=Q(u)+Q(v)\) and \(Q(au)=a^2Q(u)\). For \(q=2^e\), \(u\mapsto Q(u)^{2^{e-1}}\) is an ordinary \(\mathbf F_q\)-linear functional. If nonzero it has a codimension-one kernel, so exactly \(q^{r-1}\) projective lines have \(Q(u)\ne0\). For each such line and fixed \(\lambda\ne0\), the equation \(tB(u,u)=\lambda\) fixes \(t\) uniquely while \(s\) has \(q\) choices. This yields \(q^r\) maps for every \(\lambda\in\mathbf F_q^\times\); \(\lambda=1\) is the idempotent case. No rank-one derivations have been omitted by Steps 1–2.

## Verification

Run `python3 verify.py` with standard Python (no third-party packages). The program directly enumerates all endomorphism matrices over the indicated small fields, checks the Leibniz derivation identity directly on all basis pairs, computes matrix rank and square, and compares the observed counts with the theorem. It covers three noncongruent \(2\)-dimensional forms over \(\mathbf F_2\), two \(3\)-dimensional forms over \(\mathbf F_2\), three \(2\)-dimensional forms over \(\mathbf F_3\), and three \(2\)-dimensional forms over \(\mathbf F_4\), including a characteristic-two extension field. The exact test transcript terminates in `VERIFY_OK`.

These finite calculations corroborate the proof; they do not replace its arbitrary-dimension and arbitrary-field arguments. In particular no brute-force test is used to infer a universal quantifier.

## Relationship to prior work

Mancini and La Rosa's *Two-step nilpotent Leibniz algebras* (arXiv:2106.12904, public v1 2021-06-24, primary MSC 17A32) classifies these nilpotent algebras in terms of bilinear-form pencils and canonical indecomposable types. Its structural classification is used as motivation and is not claimed here. La Rosa and Mancini's *Derivations of two-step nilpotent algebras* (arXiv:2301.11058, public v1 2023-01-26) gives detailed derivation-algebra matrices for canonical classes, principally over characteristic different from two. Consequently many fixed-characteristic, fixed-algebra rank-one instances can be extracted from their general derivation descriptions. The present result instead isolates the entire rank-one stratum for **every nondegenerate (possibly nonsymmetric) form**, gives uniform finite-field multiplicities, and identifies the characteristic-two non-square-zero and idempotent phenomenon absent from the stated characteristic assumptions of both papers.

## Limitations

The theorem assumes nondegeneracy and a one-dimensional derived ideal. It does not classify higher-rank derivations, degenerate forms, all automorphisms, or different isomorphism types of the Leibniz algebras. The finite-field idempotent count applies only to rank-one derivations, not arbitrary idempotent endomorphisms or derivations. Literature overlap remains possible under alternative low-rank endomorphism terminology; no claim of definitive global novelty or independent validation is made.

## References

1. M. Mancini and G. La Rosa, *Two-step nilpotent Leibniz algebras*, arXiv:2106.12904v1 (2021-06-24); *Linear Algebra and its Applications* 637 (2022), 119–137. https://arxiv.org/html/2106.12904v2
2. G. La Rosa and M. Mancini, *Derivations of two-step nilpotent algebras*, arXiv:2301.11058v1 (2023-01-26); *Communications in Algebra* 51 (2023), 4928–4948. https://arxiv.org/html/2301.11058v3
