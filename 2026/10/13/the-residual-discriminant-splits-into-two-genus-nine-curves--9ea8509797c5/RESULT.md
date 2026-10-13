# The residual discriminant splits into two genus-nine curves
## Finding
Let \(\mathcal B\) be the six-point blow-up of the Hirzebruch surface used in Burek's elliptic Calabi–Yau threefold, and let \(C_+\) and \(C_-\) denote the two discriminant curves carrying split fibers of type IV. Burek defines the residual discriminant \(D\) after removing the multiplicity-four contributions of \(C_+\) and \(C_-\).

Over \(\mathbf C\), the residual discriminant is exactly
\[
D=D_+\cup D_-
\]
with \(D_+\) and \(D_-\) irreducible and linearly equivalent. Their divisor classes are
\[
[D_\pm]=-6K_{\mathcal B}-2C_+-2C_-.
\]
Each component has arithmetic genus
\[
p_a(D_\pm)=41,
\]
has exactly \(32\) ordinary cusps and no other intrinsic singularities, and therefore has normalization of genus
\[
9.
\]

The two components meet transversely at exactly \(96\) points. These are precisely the \(96\) ordinary nodes of the residual discriminant found in Burek's Proposition 7.1 and Lemma 8.2. Thus every node of \(D\) is an inter-component crossing, while the \(64\) cusps split evenly as \(32\) cusps on each irreducible component.

## Assumptions and scope
All geometry is over \(\mathbf C\). We use Burek's notation
\[
A(v)=v^8+14v^4+1,\qquad
B(v)=v(v^4-1),\qquad
C(v)=v^{12}-33v^8-33v^4+1,
\]
together with
\[
a=481,\qquad b=30,\qquad c=-4879.
\]
The identity
\[
A(v)^3-C(v)^2=108B(v)^4
\]
is the source's equation (1.3).

For the residual discriminant, put
\[
q=t^4,\qquad
d=54b^4,\qquad
p=cC(v),\qquad
h=54B(v)^4,\qquad
k=aA(v).
\]
Burek's Lemma 5.5 writes its affine equation, up to a nonzero scalar, as
\[
R=(dq^2+pq+h)^2-k^3q^2.
\]

The statement refines the residual curve \(D\) itself. It does not alter the construction of the Calabi–Yau threefold, the Mordell–Weil-rank computation, or the crepant-resolution argument.

## Proof
Set
\[
\lambda_\pm=
\frac{4879\pm481\sqrt{481}}{87480000}.
\]
Direct expansion gives the factorization
\[
R=d^2F_+F_-,
\]
where
\[
F_\pm(q,v)
=
q^2-2\lambda_\pm C(v)q-108\lambda_\pm^2B(v)^4.
\]
Equivalently, with \(q=t^4\),
\[
F_\pm(t,v)
=
t^8-2\lambda_\pm C(v)t^4-108\lambda_\pm^2B(v)^4.
\]

We first prove that each factor is irreducible in \(\mathbf C(v)[t]\). Its discriminant as a quadratic in \(q\) is
\[
4\lambda_\pm^2A(v)^3.
\]
The polynomial \(A\) has simple roots, so \(A\) is not a square in \(\mathbf C(v)\). Thus the quadratic in \(q\) is irreducible.

For the remaining fourth-root extension, write
\[
H_\pm(v)=v^4\pm2i\sqrt3\,v^2+1.
\]
Then
\[
A=H_+H_-,
\qquad
C=\frac{H_+^3+H_-^3}{2},
\qquad
C\pm6i\sqrt3\,B^2=H_\pm^3.
\]
The polynomials \(H_+\) and \(H_-\) are square-free and coprime, and so are their product classes modulo squares. Let \(K=\mathbf C(v)\) and \(K_1=K(\sqrt A)\). A root of \(F_\pm(q,v)\) has the form, up to a nonzero square constant,
\[
\alpha=C+A\sqrt A.
\]
In the biquadratic extension
\[
K(\sqrt{H_+},\sqrt{H_-}),
\]
a square root of \(\alpha\) is, up to a nonzero constant,
\[
H_+\sqrt{H_+}+H_-\sqrt{H_-}.
\]
The nontrivial automorphism of this biquadratic extension over \(K_1\) changes the sign of this expression, so no square root lies in \(K_1\). Hence \(\alpha\) is not a square in \(K_1\). Since \(K_1\) contains the fourth roots of unity, \(T^4-\alpha\) is irreducible over \(K_1\). Therefore \(F_\pm(t,v)\), of degree \(8\) in \(t\), is irreducible over \(K\). Its projective closure gives an irreducible residual component.

The two factors define linearly equivalent divisors. Under Burek's transition
\[
w=v^{-1},
\qquad
t'=w^3t,
\]
each \(F_\pm\) transforms with the same factor \(w^{-24}\). At every one of the six points with \(B(v)=0\) and \(t=0\), each factor has multiplicity \(4\). Hence their strict transforms on \(\mathcal B\) are linearly equivalent. Since their sum is Burek's
\[
D=-12K_{\mathcal B}-4C_+-4C_-,
\]
each has class
\[
E=-6K_{\mathcal B}-2C_+-2C_-.
\]

Burek records
\[
K_{\mathcal B}^2=2,\qquad
C_+^2=C_-^2=-3,\qquad
K_{\mathcal B}\!\cdot C_+=K_{\mathcal B}\!\cdot C_-=1,\qquad
C_+\!\cdot C_-=0.
\]
Therefore
\[
E^2=96,\qquad K_{\mathcal B}\!\cdot E=-16,
\]
and adjunction gives
\[
p_a(E)=1+\frac{E^2+K_{\mathcal B}\!\cdot E}{2}=41.
\]

The common-zero resultant of \(F_+\) and \(F_-\), taken with respect to \(q\), is a nonzero constant times
\[
B(v)^4J(v),
\]
where
\[
J(v)=a^3B(v)^4-b^4A(v)^3
\]
is exactly Burek's polynomial from Proposition 7.1. The \(B=0\) contribution belongs to the six boundary points that are separated by the base blow-ups; Burek proves that the residual discriminant is smooth at the resulting boundary points. The polynomial \(J\) has \(24\) simple roots, none a zero of \(A\), \(B\), or \(C\). For every root \(v_0\) of \(J\), the common value is
\[
q=\frac{C(v_0)}{c},
\]
which is nonzero, and therefore has four distinct fourth roots in \(t\). This gives
\[
24\cdot4=96
\]
common interior points. Because
\[
D_+\cdot D_-=E^2=96,
\]
these exhaust the intersection and every local intersection multiplicity is one. They are therefore transverse crossings. Burek independently proves that exactly these \(96\) discriminant points are ordinary nodes.

Finally, the discriminant of each quadratic \(F_\pm(q,v)\) is
\[
4\lambda_\pm^2A(v)^3.
\]
The eight roots of \(A\) are simple and are disjoint from the zeros of \(B\). At such a root the double \(q\)-root is nonzero, so it has four distinct \(t\)-lifts. The two values \(\lambda_+\) and \(\lambda_-\) are distinct, so the cusp sets of the two factors are disjoint. Burek proves that these are ordinary cusps and that the residual discriminant has no other singularities. Hence each \(D_\pm\) has
\[
8\cdot4=32
\]
ordinary cusps and no other intrinsic singularities. Since an ordinary cusp has \(\delta=1\), the normalization genus is
\[
41-32=9.
\]

## Verification
The accompanying `verify.py` performs exact symbolic checks over the relevant algebraic number fields.

It verifies the source identity \(A^3-C^2=108B^4\), the factorization \(R=d^2F_+F_-\), the factor discriminants \(4\lambda_\pm^2A^3\), and the identities involving \(H_+\) and \(H_-\) used in the square-class argument. It checks square-freeness and coprimality of the required polynomials.

It also verifies the Hirzebruch transition of each factor, computes the exact resultant
\[
\operatorname{Res}_q(F_+,F_-)
=
\text{nonzero constant}\cdot B^4J,
\]
checks that \(J\) is square-free of degree \(24\) and is coprime to \(ABC\), and verifies that \(q=C/c\) is the common root modulo \(J\).

Finally, the exact intersection arithmetic gives \(E^2=96\), \(K_{\mathcal B}\cdot E=-16\), \(p_a(E)=41\), \(32\) cusps per component, and normalization genus \(9\). The saved verifier output ends in `VERIFY_OK`.

## Relationship to prior work
Burek's paper is the initiating source. Lemma 5.5 gives the degree-\(16\) residual discriminant polynomial and proves it square-free over \(\mathbf C(v)\). Proposition 7.1 identifies the \(96\) ordinary double points through the degree-\(24\) polynomial \(J\). Lemma 8.2 gives the aggregate class
\[
D=-12K_{\mathcal B}-4C_+-4C_-,
\]
arithmetic genus \(177\), \(96\) nodes, and \(64\) cusps, explicitly making the Euler-characteristic computation without assuming irreducibility.

The checked text does not state the factorization \(D=D_+\cup D_-\), the irreducibility and divisor class of each factor, the allocation of all nodes as crossings, the \(32+32\) cusp split, or the genus-\(9\) normalizations.

Kumar and Kuwata's earlier work constructs and analyzes the individual \(F^{(4)}\) elliptic K3 surfaces associated with products of elliptic curves, including their Mordell–Weil lattices. It does not treat this two-parameter Calabi–Yau base discriminant or the component geometry above.

Targeted searches using the source identifier together with “residual discriminant”, “components”, “genus 9”, the constants \(481\) and \(4879\), and the square-root factorization found no covering statement.

## Limitations
The factorization is over \(\mathbf C\); no claim is made here about the smallest field of definition of the two components.

The result concerns the residual \(I_1\)-discriminant curve on the blown-up base. The two separate type-IV discriminant curves \(C_+\) and \(C_-\) are not included in \(D_\pm\).

The proof uses Burek's established boundary smoothness and classification of the \(96\) nodes and \(64\) cusps. It refines their distribution among components rather than reproving the analytic singularity classifications from scratch.

## References
1. D. Burek, *An elliptic Calabi–Yau threefold of Mordell–Weil rank twelve*, arXiv:2610.01276v1, 2026.
2. A. Kumar and M. Kuwata, *Elliptic K3 surfaces associated with the product of two elliptic curves: Mordell–Weil lattices and their fields of definition*, Nagoya Mathematical Journal 228 (2017), 124–185.
