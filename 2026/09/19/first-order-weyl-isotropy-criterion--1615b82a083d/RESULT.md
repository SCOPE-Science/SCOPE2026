# First-order Weyl elements satisfy the isotropy criterion beyond local finiteness

## Statement

Let \(\Bbbk\) be an algebraically closed field of characteristic zero and
\[
A_1=\Bbbk\langle p,q\mid pq-qp=1\rangle.
\]
For
\[
w=a(p)q+b(p)\in A_1\setminus\Bbbk,
\qquad a,b\in\Bbbk[p],
\]
write \(D=\operatorname{ad}_w\). Then the following trichotomy holds.

1. If \(a\in\Bbbk\), then \(D\) is locally nilpotent and \(\operatorname{Aut}_D(A_1)\) contains automorphisms of arbitrarily large degree.
2. If \(\deg a=1\), then \(D\) is locally finite but not locally nilpotent; after conjugation, \(w\) has the form \(\lambda pq+\mu\), and the isotropy group is conjugate to the degree-one torus \(\Bbbk^\times\).
3. If \(d:=\deg a\ge2\), then \(D\) is not locally finite and its isotropy group is finite. More precisely, after a triangular change of \(q\) and a translation of \(p\), one may write
\[
W=A(p)q+R(p),
\]
where \(\deg A=d\), the coefficient of \(p^{d-1}\) in \(A\) is zero, and \(\deg R<d\). For this normalized element,
\[
\operatorname{Aut}_{\operatorname{ad}_W}(A_1)
=
\left\{\rho_\zeta:\ p\mapsto\zeta p,\ q\mapsto\zeta^{-1}q\ :\
A(\zeta p)=\zeta A(p),\ R(\zeta p)=R(p)\right\}.
\]
In particular it is a finite cyclic group of order dividing \(d-1\).

Consequently, on the entire first-order-in-\(q\) stratum,
\[
\boxed{
\operatorname{Aut}_{\operatorname{ad}_w}(A_1)\text{ has unbounded degree}
\iff
\operatorname{ad}_w\text{ is locally nilpotent}.}
\]
Thus the open isotropy criterion posed for arbitrary elements of \(A_1\) has an affirmative answer for every element of \(q\)-degree at most one, including a genuinely non-locally-finite family.

There is also an exact order formula in the normalized case \(d\ge2\). Write
\[
A(p)=\sum_{j=0}^d A_jp^j,
\qquad
R(p)=\sum_{j=0}^{d-1}R_jp^j,
\]
and let
\[
g=\gcd\Bigl(\{|j-1|:A_j\ne0,\ j\ne1\}\cup
\{j:R_j\ne0,\ j\ge1\}\Bigr).
\]
The set is nonempty because \(A_d\ne0\), and \(g\mid d-1\). Then
\[
\boxed{\operatorname{Aut}_{\operatorname{ad}_W}(A_1)\cong\mu_g.}
\]

## Reduction to normal form

Assume first that \(a\ne0\). Divide
\[
b(p)=a(p)h(p)+r(p),\qquad \deg r<\deg a.
\]
The triangular automorphism \(p\mapsto p\), \(q\mapsto q-h(p)\) sends \(w\) to
\[
a(p)q+r(p).
\]
If \(d=\deg a\ge2\), a translation of \(p\) makes the coefficient of \(p^{d-1}\) in \(a\) vanish while preserving \(\deg r<d\). This gives the normalized pair \((A,R)\) above.

If \(a=c\in\Bbbk^\times\), the same triangular change sends \(w\) to \(cq+\mu\), and the scalar is irrelevant to the associated inner derivation. If \(a=0\), then \(w=b(p)\) with \(b\) nonconstant. Both cases are standard locally nilpotent normal forms.

If \(a(p)=\lambda p+\beta\) has degree one, the same division leaves a constant remainder, and translating \(p\) sends the result to \(\lambda pq+\mu\). The known isotropy computation for \(pq\) therefore gives a conjugate of the scaling torus.

## Exact isotropy for \(\deg A\ge2\)

Let \(W=A(p)q+R(p)\) be normalized as above and let
\[
\rho(p)=P,\qquad \rho(q)=Q.
\]
The standard description of isotropy for inner derivations says
\[
\rho\in\operatorname{Aut}_{\operatorname{ad}_W}(A_1)
\iff
\rho(W)-W\in\Bbbk.
\]
Hence
\[
A(P)Q+R(P)=A(p)q+R(p)+c
\]
for some \(c\in\Bbbk\).

Use the standard total-degree filtration on \(A_1\). Its associated graded algebra is \(\Bbbk[p,q]\), hence a domain. Put
\[
m=\deg P,\qquad n=\deg Q.
\]
Both are at least one. Since \(\deg A=d\),
\[
\deg A(P)=dm,
\qquad
\deg(A(P)Q)=dm+n,
\qquad
\deg R(P)\le(d-1)m.
\]
The top term of \(A(P)Q\) therefore cannot cancel against \(R(P)\). The right-hand side has total degree \(d+1\), so
\[
dm+n=d+1.
\]
For \(d\ge2\) and \(m,n\ge1\), this forces
\[
m=n=1.
\]
Thus every isotropy automorphism is affine linear:
\[
P=\alpha p+\beta q+\gamma,
\qquad
Q=\delta p+\varepsilon q+\eta,
\qquad
\alpha\varepsilon-\beta\delta=1.
\]

Comparing leading homogeneous terms in the commutative associated graded ring gives
\[
(\alpha p+\beta q)^d(\delta p+\varepsilon q)=p^dq
\]
up to the common nonzero leading coefficient of \(A\). Unique factorization and \(d\ge2\) force
\[
\beta=\delta=0,
\]
so
\[
P=\alpha p+\gamma,
\qquad
Q=\alpha^{-1}q+\eta.
\]
Comparing the coefficient of \(q\) gives
\[
A(\alpha p+\gamma)=\alpha A(p).
\]
Because the coefficient of \(p^{d-1}\) in \(A\) is zero, comparison of the leading two coefficients yields
\[
\alpha^{d-1}=1,
\qquad
\gamma=0.
\]
The remaining polynomial part satisfies
\[
\eta A(\alpha p)+R(\alpha p)-R(p)\in\Bbbk.
\]
Since \(\deg A=d>\deg R\), this forces \(\eta=0\). Then
\[
R(\alpha p)-R(p)\in\Bbbk.
\]
Evaluating at \(p=0\) shows that this constant is zero. Thus every isotropy automorphism has exactly the announced form
\[
p\mapsto\alpha p,
\qquad
q\mapsto\alpha^{-1}q,
\]
with
\[
A(\alpha p)=\alpha A(p),
\qquad
R(\alpha p)=R(p).
\]
The converse is immediate, so the description is exact.

Coefficient comparison shows that the allowed \(\alpha\) are precisely those satisfying
\[
\alpha^{j-1}=1\quad(A_j\ne0),
\qquad
\alpha^j=1\quad(R_j\ne0,\ j\ge1).
\]
Hence they form \(\mu_g\) with \(g\) as above. In particular, for \(d=2\) the isotropy group is trivial.

## Failure of local finiteness for \(\deg a\ge2\)

The restriction of \(D=\operatorname{ad}_{a(p)q+b(p)}\) to \(\Bbbk[p]\) is
\[
D(f(p))=-a(p)f'(p).
\]
Set \(f_0=p\) and \(f_{n+1}=D(f_n)\). If \(d=\deg a\ge2\), characteristic zero gives
\[
\deg f_n=1+n(d-1)
\]
for every \(n\ge0\). Thus \(D^n(p)=f_n\) are nonzero and have strictly increasing degrees, so their span is infinite-dimensional. Therefore \(D\) is not locally finite, and a fortiori not locally nilpotent.

Together with the constant and linear cases, this also yields the exact first-order classification
\[
\operatorname{ad}_{a(p)q+b(p)}\text{ is locally finite}
\iff
\deg a\le1
\]
(with \(a=0\) included in the constant case), and
\[
\operatorname{ad}_{a(p)q+b(p)}\text{ is locally nilpotent}
\iff
a\in\Bbbk.
\]

## Relation to prior work

Baltazar, Lopes and Morales prove the isotropy criterion for every nonzero locally finite derivation of the first Weyl algebra and explicitly leave the unrestricted case open. Their computations include the unbounded isotropy of polynomial normal forms \(f(p)\) and the degree-one isotropy of \(pq\). Those results are used here for the constant and linear branches. The new part is the complete first-order-in-\(q\) extension beyond local finiteness, especially the finite-isotropy theorem and exact cyclic stabilizer for \(\deg a\ge2\).

The structure of \(\operatorname{Aut}(A_1)\) is classical. Dixmier and Makar-Limanov describe the automorphism group, and Makar-Limanov's leading-form argument shows that images of the Weyl generators under an automorphism have strongly constrained highest homogeneous components. These automorphism-group results are prior art and are not claimed here. The proof above uses only the filtered-domain degree argument needed for this stabilizer problem.

## Limitations

The result treats elements of \(q\)-degree at most one. It does not settle the open criterion for arbitrary \(w\in A_1\), in particular for elements genuinely involving \(q^2\) or higher powers. By the Fourier automorphism, there is an immediate symmetric statement for elements first-order in \(p\), but no claim is made for general mixed higher-order elements.

Originality is asserted only to the best of our knowledge. Targeted searches for stabilizers of first-order Weyl elements and inspection of the principal classical automorphism references did not locate the exact trichotomy above. Because the argument becomes short once the recent open problem is formulated, equivalent implicit coverage in older Weyl-algebra or polynomial-automorphism literature remains a residual risk. No independent validation is asserted.

## References

1. R. Baltazar, S. Lopes, O. Morales, *A Characterization of Local Nilpotence for Derivations of Ore Extensions*, arXiv:2609.19470v1 (2026). https://arxiv.org/abs/2609.19470v1
2. J. Dixmier, *Sur les algèbres de Weyl*, Bull. Soc. Math. France 96 (1968), 209--242. https://doi.org/10.24033/bsmf.1667
3. L. Makar-Limanov, *On automorphisms of Weyl algebra*, Bull. Soc. Math. France 112 (1984), 359--363. https://doi.org/10.24033/bsmf.2010
