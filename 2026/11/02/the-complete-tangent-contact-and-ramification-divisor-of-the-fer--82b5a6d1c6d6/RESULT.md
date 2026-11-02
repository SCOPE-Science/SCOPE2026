# The complete tangent-contact and ramification divisor of the Fermat norm curve

## Finding

Let \(q=p^h\ge 2\), let \(k=\overline{\mathbb F}_p\), put \(d=q^2+q+1\), and consider the smooth Fermat plane curve
\[
C_q:\quad X^d+Y^d+Z^d=0\subset\mathbb P^2_k.
\]
For \(P\in C_q(k)\), write \(j(P)=I_P(C_q,T_PC_q)\), the intersection multiplicity of the curve with its tangent line. Then the **complete tangent-contact classification** is
\[
j(P)=\begin{cases}
d,&P\in C_q(\mathbb F_{q^3})\text{ and }XYZ(P)=0,\\
q+1,&P\in C_q(\mathbb F_{q^3})\text{ and }XYZ(P)\ne0,\\
q,&P\notin C_q(\mathbb F_{q^3}).
\end{cases}
\]
Here \(\mathbb F_{q^3}\subset k\) is the unique subfield of order \(q^3\), and the condition of rationality is projective. Thus the points of contact order greater than the **generic** order \(q\) are precisely the \(\mathbb F_{q^3}\)-points of \(C_q\). We call these \(q\)-flexes, distinguishing this usage from the classical contact-at-least-three definition.

There are exactly \(3d\) coordinate-boundary \(q\)-flexes of contact order \(d\) and \((q-2)d^2\) interior \(q\)-flexes of contact order \(q+1\). In particular,
\[
\# C_q(\mathbb F_{q^3})=(q-2)d^2+3d.
\]
For the complete hyperplane series \(\lvert\mathcal O_{C_q}(1)\rvert\), whose generic order sequence is \((0,1,q)\), the ramification divisor is exactly
\[
R=\sum_{\substack{P\in C_q(\mathbb F_{q^3})\\XYZ(P)\ne0}}[P]
+(d-q)\sum_{\substack{P\in C_q(\mathbb F_{q^3})\\XYZ(P)=0}}[P].
\]
The formula specifies **scheme-theoretic multiplicities** in the Wronskian ramification divisor, not merely its support. When \(q=2\), only the \(3d=21\) maximal-contact points occur; the other type starts at \(q=3\).

## Assumptions and scope

The field is algebraically closed of characteristic \(p\), with \(q=p^h\) for arbitrary integer \(h\ge1\). No restrictions on parity are imposed. Since \(d\equiv1\pmod p\), all three partial derivatives of the defining polynomial vanish simultaneously only at the excluded origin of affine three-space, so \(C_q\) is a smooth geometrically integral curve of genus \(g=(d-1)(d-2)/2\). All point counts are geometric points rational over the indicated finite field, not isomorphism classes. The theorem concerns tangent contacts to this specific plane embedding, not canonical Weierstrass points or all other plane curves of degree \(d\).

## Proof

**1. Tangent expansion and its first possible nonzero term.** Set \(F=\sum_i X_i^d\), and write a point of the cone over \(C_q\) as \(a=(a_0,a_1,a_2)\). For a non-radial tangent direction \(e=(e_0,e_1,e_2)\), the tangent condition is
\[
\sum_i a_i^{d-1}e_i=0.
\]
The factorization
\[
(a_i+te_i)^d=(a_i+te_i)(a_i^q+t^qe_i^q)(a_i^{q^2}+t^{q^2}e_i^{q^2})
\]
shows that the only possible powers of \(t\) in \(F(a+te)\) are \(0,1,q,q+1,q^2,q^2+1,q^2+q,d\). The constant and linear terms vanish on the curve and its tangent. The degree-\(q\) term is
\[
B_q(a,e)=\sum_i a_i^{q^2+1}e_i^q.
\]
Because the radial tangent direction also annihilates \(B_q\) (the evaluation equals \(F(a)=0\)), this coefficient is well defined on the one-dimensional projective tangent direction. Consequently, every contact has order at least \(q\).

**2. Exact vanishing criterion.** Suppose first that all \(a_i\ne0\). Put \(A_i=a_i^d\) and write \(e_i=a_i u_i\). Then \(\sum_i A_i=0\), the tangent condition is \(\sum_i A_i u_i=0\), and
\[
B_q(a,e)=\sum_i A_i u_i^q.
\]
The last expression vanishes on the tangent plane precisely when the coefficient rows \((A_i)\) and \((A_i^q)\) are proportional: take the \(q\)-th power of the tangent equation and compare the two linear forms in the variables \(u_i^q\). This is equivalent to \(A_i/A_j\in\mathbb F_q\) for all indices. Since \(d(q-1)=q^3-1\), that condition is in turn equivalent to \((a_i/a_j)^{q^3-1}=1\) for all indices, i.e. \(P=[a_0:a_1:a_2]\in\mathbb P^2(\mathbb F_{q^3})\).

If one coordinate is zero, say \(a_2=0\), then \((a_1/a_0)^d=-1\). The same identity \(d(q-1)=q^3-1\) implies \((a_1/a_0)^{q^3-1}=1\), so such a point is automatically \(\mathbb F_{q^3}\)-rational. Its tangent line is \(X_1=(a_1/a_0)X_0\), whose restriction of \(F\) is \(X_2^d\); hence its contact multiplicity is exactly \(d\). This also directly verifies \(B_q=0\) at coordinate-boundary points. Thus outside \(C_q(\mathbb F_{q^3})\) the contact order is exactly \(q\), and the boundary points have contact \(d\).

**3. Interior rational contacts have order exactly \(q+1\).** If \(P\in C_q(\mathbb F_{q^3})\) has three nonzero coordinates, choose its representative in \(\mathbb F_{q^3}^3\). Then \(A_i=a_i^d=N_{\mathbb F_{q^3}/\mathbb F_q}(a_i)\in\mathbb F_q^\times\), and \(A_0+A_1+A_2=0\). Replacing the tangent direction by a radial translate, we may set \(u_0=0\), \(u_1=1\) and \(u_2=-A_1/A_2\). The coefficient of \(t^{q+1}\) is
\[
B_{q+1}=\sum_i a_i^{q^2}e_i^{q+1}=\sum_i A_i u_i^{q+1}
=A_1+A_2\left(-\frac{A_1}{A_2}\right)^{q+1}
=-\frac{A_0A_1}{A_2}\ne0.
\]
Here \(u_2^q=u_2\) because \(u_2\in\mathbb F_q\), so \(u_2^{q+1}=u_2^2\), in both odd and even characteristic. Thus \(j(P)=q+1\). All possible point types have now been exhausted.

**4. Exact counts via the norm map.** On \(\mathbb F_{q^3}^\times\), the map \(x\mapsto x^d\) is the norm to \(\mathbb F_q^\times\), and each value has exactly \(d\) preimages. On any one coordinate line the Fermat equation becomes \(r^d=-1\), giving \(d\) points; the three lines do not meet on \(C_q\), giving \(3d\) boundary points. For an interior point normalize the last coordinate to 1. The two nonzero norms must add to \(-1\). There are exactly \(q-2\) ordered nonzero pairs of elements of \(\mathbb F_q\) with this sum, and each pair lifts in \(d^2\) ways. Hence the interior count is \((q-2)d^2\).

**5. Ramification multiplicities.** The generic contact order is \(q\), since the geometrically infinite smooth curve has only finitely many \(\mathbb F_{q^3}\)-points. The generic order sequence of the hyperplane linear series is therefore \((0,1,q)\). At a point choose adapted local sections \(1,t,f(t)\) of \(\mathcal O_{C_q}(1)\), where \(t\) is a uniformizer from a transverse line and \(f\) is the tangent-line section with initial term \(c t^{j(P)}\), \(c\ne0\). The Hasse–Wronskian determinant for orders \((0,1,q)\) is \(D^{(q)}f\), up to a unit. For \(j(P)=q,q+1,d\), the binomial coefficient \(\binom{j(P)}q\) is 1 modulo \(p\): this follows respectively from the base-\(q\) expansions \(q\), \(q+1\), and \(1+q+q^2\). Thus the local Wronskian valuation is exactly \(j(P)-q\). This proves the displayed ramification divisor, including multiplicities.

As a consistency check, its degree is
\[
(q-2)d^2+3d(d-q)=(q+1)d^2-3qd
=(q+1)(2g-2)+3d,
\]
exactly the global ramification-divisor degree for a rank-two linear series with generic orders \((0,1,q)\).

## Verification

The included standalone Python program `verify_contacts.py` implements finite-field polynomial quotient arithmetic, verifies field inverses, enumerates every curve point and a nonradial tangent direction, independently expands all eight possible Taylor coefficients, and checks the exact contact order. It passed the following exhaustive cases:

| Ambient field | \(q\) | Contact-order histogram |
| --- | ---: | --- |
| \(\mathbb F_8\) | 2 | 21 points of order 7 |
| \(\mathbb F_{27}\) | 3 | 169 of order 4; 39 of order 13 |
| \(\mathbb F_{64}\) | 4 | 882 of order 5; 63 of order 21 |
| \(\mathbb F_{125}\) | 5 | 2883 of order 6; 93 of order 31 |
| \(\mathbb F_{64}\) | 2 | 98 nonflexes of order 2; 21 points of order 7 |

The final test is particularly relevant because the ambient field strictly contains \(\mathbb F_{q^3}\), so it also checks the predicted nonflex stratum. Running `python verify_contacts.py` produces `FERMAT_NORM_FLEX_EXHAUSTIVE_CONTACTS_OK`. These finite checks corroborate but do not establish the infinite family; the proof above does.

## Relationship to prior work

Komeda's 2020 study introduces the degree-\(q^2+q+1\) family and computes the dual curve's singularities for its Fermat member. Its flex count and ordinary-contact analysis apply to a *general* member of that large linear system, whereas its specific Fermat theorem addresses the dual's nodes and higher singularities. The complete \(\mathbb F_{q^3}\)-rational support, the three contact orders, the two rational-fibre counts, and the ramification-divisor multiplicities are not stated in the inspected theorems or proofs. The result is therefore a special-member complement, not a replacement for the dual-curve classification.

Arakelian and Borges analyze Frobenius nonclassicality of Fermat curves relative to *plane cubics* and rational-point counts under different order conditions. The theorem here concerns the hyperplane linear series and geometric contact at **all** points. Standard Stöhr–Voloch order-sequence and ramification methods supply the formal language and the global degree formula; they do not by themselves give this special member's exact local support without the norm and tangent calculations. Earlier rational-point results for Fermat curves of exponent \(q-1\) treat a different curve family.

## Limitations

The claim is a self-contained calculation for one infinite family and one natural linear series. It does not classify higher-degree osculating series or moduli of all degree-\(d\) curves. Counts are over \(\mathbb F_{q^3}\), not arbitrary finite extensions. Historical priority is subject to possible unindexed special-case computations, particularly in the literature on nonclassical Fermat curves and positive-characteristic Weierstrass points. No independent external validation has been performed.

## References

1. Kosuke Komeda, *Singularities of the dual curve of a certain plane curve in positive characteristic*, arXiv:2002.10691, first posted 2020-02-25. In particular §§1, 4, 5 and Theorems 1–2. https://arxiv.org/abs/2002.10691
2. Nazar Arakelian and Herivelto Borges, *Frobenius nonclassicality of Fermat curves with respect to cubics*, arXiv:1502.05953, first posted 2015-02-20, especially Theorem 1.1 and §2. https://arxiv.org/abs/1502.05953
3. K.-O. Stöhr and J. F. Voloch, *Weierstrass points and curves over finite fields*, Proc. London Math. Soc. (3) 52 (1986), 1–19. General order-sequence and Hasse–Wronskian formalism.
4. José Felipe Voloch and Michael E. Zieve, *Rational points on some Fermat curves and surfaces over finite fields*, arXiv:1310.1772, 2013 (different exponent family). https://arxiv.org/abs/1310.1772
