# Linear-component geometry of square-zero derivations on truncated polynomial algebras in characteristic two

## Finding
For every field \(k\) of characteristic \(2\) and integer \(N\ge2\), let \(A_N=k[t]/(t^N)\). The scheme \(X_N\) parametrizes \(k\)-derivations \(D:A_N\to A_N\) satisfying \(D^2=0\). Put
\[
m=\lfloor N/2\rfloor,\qquad c=\lfloor N/4\rfloor+1.
\]
The reduced scheme \((X_N)_{\mathrm{red}}\) is a union of **exactly \(c\) distinct, explicitly described linear affine spaces of dimension \(m\)** over \(k\). Ordered by increasing initial vanishing order, each new component meets the union of earlier components exactly in a codimension-one linear subspace of that new component, namely its intersection with the immediately preceding component. Consequently, for every finite field \(\mathbb F_q\) of characteristic \(2\),
\[
\#X_N(\mathbb F_q)=c q^m-(c-1)q^{m-1}.
\]
The original scheme \(X_N\), before reduction, is **nonreduced for every \(N\ge2\)**. At its zero point the Zariski tangent dimension is \(N\) if \(N\) is even and \(N-1\) if \(N\) is odd; these exceed the dimension \(m\) of its reduced support.

## Assumptions and scope
Here \(k\) is any field of characteristic \(2\). Every derivation is determined by \(f=D(t)=\sum_{i=0}^{N-1} f_i t^i\); for even \(N\), any \(f\in A_N\) is permitted, and for odd \(N\), the defining relation forces \(f_0=0\). These coefficients serve as affine coordinates, with the linear relation \(f_0=0\) imposed when necessary. Let \(C_j\) denote the linear spaces below; an empty set of equations is understood to impose no condition.

**Even \(N\).** For each integer \(0\le j\le\lfloor N/4\rfloor\), define \(C_j\) by
\[
 f_i=0\quad(0\le i<2j),\qquad
 f_i=0\quad(2j+1\le i\le N-2j-1,\ i\text{ odd}).
\]
The components, in order, are \(C_0,C_1,\ldots,C_{\lfloor N/4\rfloor}\).

**Odd \(N\).** Put \(h=\lfloor(N-1)/4\rfloor\). For each integer \(1\le j\le h\), define \(C_j\) by
\[
 f_i=0\quad(0\le i<2j),\qquad
 f_i=0\quad(2j+1\le i\le N-2j,\ i\text{ odd}).
\]
In addition define \(C_*\) by \(f_i=0\) for \(0\le i\le\lfloor N/2\rfloor\). The components, in order, are \(C_1,\ldots,C_h,C_*\). For \(N=3\), this consists of the single component \(C_*\).

## Proof
**1. Derivations and the restricted-square equation.** The relation \(t^N=0\) gives \(0=D(t^N)=N t^{N-1}f\). In characteristic \(2\), this places no restriction on \(f\) when \(N\) is even and says \(f_0=0\) when \(N\) is odd. Conversely these restrictions suffice to define the unique derivation \(D_f(g)=f g'\) on \(A_N\). Because the characteristic is \(2\), \(D_f^2\) is again a derivation, and
\[
D_f^2(t)=f f'\pmod{t^N}.
\]
Thus \(D_f^2=0\) holds exactly when \(f f'=0\) in \(A_N\).

**2. The valuation dichotomy.** If \(f\ne0\), write \(f=t^s u\) with \(u(0)\ne0\). If \(s\) is odd, the leading term of \(f'\) is \(u(0)t^{s-1}\), and hence \(f f'=0\) exactly when \(2s-1\ge N\). If \(s\) is even, \(f'=t^s u'\) and
\[
 f f'=t^{2s}u u'.
\]
For \(2s\ge N\) the condition is automatic. Otherwise \(u\) is invertible and \(u'\equiv0\pmod{t^{N-2s}}\). Since characteristic two kills even-degree derivatives, this last requirement means precisely that the coefficients of \(f\) at odd degrees
\[
s+1,\ s+3,\ldots,\ N-s
\]
vanish, omitting indices outside \(0,\ldots,N-1\). The leading order \(s\) is understood to have an unconstrained nonzero coefficient.

**3. Exhaustive component decomposition.** For even \(N\), any allowable even valuation \(s=2j\) with \(4j<N\) gives an element of \(C_j\). When \(4j\ge N\), or when \(s\) is odd and \(2s-1\ge N\), the resulting high-order vector belongs to the final \(C_{\lfloor N/4\rfloor}\): if \(N\) is divisible by four its first \(N/2\) coefficients vanish, while for \(N\equiv2\pmod4\) the final component imposes vanishing below \(N/2-1\) and of the \(N/2\)-th coefficient. All of these conditions are satisfied by the allowed high-order vectors.

For odd \(N\), the relation \(f_0=0\) and the odd-valuation inequality exclude all small odd orders. Every allowable even order \(s=2j\) with \(4j<N\) lies in \(C_j\). Every remaining permissible order is at least \(\lfloor N/2\rfloor+1\) and hence lies in \(C_*\). The zero vector lies in all components. In the reverse direction, the defining coordinate equations of each listed \(C_j\), and the high-order condition of \(C_*\), make \(f f'=0\) by step 2. Thus the listed union is **exactly** the square-zero locus over every extension field of \(k\), and therefore describes its underlying reduced affine variety.

**4. Components, intersections and point count.** The number of free coefficient coordinates in each even-\(N\) component is \(N/2\); the count in each odd-\(N\) component is \((N-1)/2\), including the final \(C_*\). Thus every component is a linear \(m\)-space. Consecutive components are distinct: the next component sets the preceding component's first potentially nonzero even coefficient to zero, while releasing its highest constrained odd coefficient. Their intersection therefore has dimension exactly \(m-1\). For nonconsecutive indices \(i<j-1\), the coefficient restrictions give
\[
 C_i\cap C_j\ \subseteq\ C_{j-1}\cap C_j,
\]
where the final \(C_*\), in the odd case, is treated as the last component. Indeed, among the conditions from \(C_{j-1}\) not already imposed by \(C_j\), the only new restriction is the highest odd coefficient removed at the previous step; every earlier component also forces that coefficient to zero. Consequently, the intersection of a new component with **all** earlier components is its hyperplane intersection with its immediate predecessor. All components are distinct and have the same dimension, so they are precisely the irreducible components of the reduced locus.

Over \(\mathbb F_q\), the first component contributes \(q^m\) points, and each of the remaining \(c-1\) contributes \(q^m-q^{m-1}\) previously uncounted points. This proves
\[
\#X_N(\mathbb F_q)=q^m+(c-1)(q^m-q^{m-1})
=c q^m-(c-1)q^{m-1}.
\]
In particular, the count agrees for the paired truncation lengths \(2m\) and \(2m+1\).

**5. Nonreduced scheme and tangent space.** The actual parameter scheme is defined by the coefficients of the quadratic polynomial \(f f'\), together with \(f_0=0\) when \(N\) is odd. The coefficient of \(t\) in \(f f'\) is exactly \(f_1^2\) for every \(N\ge2\). Thus \(f_1^2=0\) in the universal coordinate ring. Yet \(f_1\ne0\) there because, after the optional linear equation \(f_0=0\), the defining ideal is generated in degree two and cannot contain the nonzero degree-one coordinate \(f_1\). This proves nonreducedness without asserting a full primary decomposition of the nonreduced ideal. All remaining defining equations have zero differential at the origin, giving tangent dimension \(N\) in the even case and \(N-1\) in the odd case.

## Verification
The independent enumeration script `check.py` constructs the finite fields of sizes \(2\), \(4\), and \(8\) explicitly, enumerates **every** coefficient vector in the listed test ranges, multiplies \(f f'\) directly modulo \(t^N\), and separately tests component membership and the chain-intersection restriction. It verifies every \(N\in[2,12]\) over \(\mathbb F_2\), every \(N\in[2,8]\) over \(\mathbb F_4\), and every \(N\in[2,5]\) over \(\mathbb F_8\): 22 complete finite-field configurations. The final marker is `SQUARE_ZERO_TRUNCATED_DERIVATION_COMPONENT_CENSUS_OK 22`. This is experimental corroboration of the separate all-fields proof above, not a proof by enumeration.

## Relationship to prior work
The established restricted Witt-algebra framework identifies \(p\)-fold derivation composition with the restricted power operation. Evans and Fuchs (2001) treat the ordinary one-generator truncation of degree \(p\), not the arbitrary truncation lengths or component geometry here. Hoffmann and Kowalski (2012, 2015) establish Hasse–Schmidt integration theory and the connection between truncated group scheme actions and derivations; those results do not furnish a finite-field census or a component decomposition for the characteristic-two truncation family. Premet (2014) studies regular derivations and nilpotent-cone geometry for multivariable truncations at exponent \(p>2\), under algebraic-closedness assumptions, not this characteristic-two restricted-square stratum. The novelty assessed here is **the full reducible linear-component arrangement and exact finite-field point count over every truncation length**, together with the explicit nonreduced scheme boundary, not the general correspondence between square-zero derivations and infinitesimal group actions. Publication-priority uncertainty persists for any specialized historical treatment not located by the searches.

## Limitations
The result concerns the square-zero stratum in the derivation algebra of the single-variable truncated polynomial algebra **only in characteristic two**. It does not classify derivations whose higher restricted powers vanish, the complete nonreduced scheme primary decomposition, automorphism-conjugacy orbits of the components, or multi-variable fat points. The component description is for the reduced locus; the extra nilpotent coordinate in the actual scheme is explicitly retained, not overlooked. Independent mathematical validation has not been performed.

## References
- T. J. Evans and D. Fuchs, *On the restricted Lie algebra structure for the Witt Lie algebra in finite characteristic*, arXiv:math/0111271, public 2001-11-27, https://arxiv.org/abs/math/0111271 .
- D. Hoffmann and P. Kowalski, *Integrating Hasse–Schmidt derivations*, arXiv:1212.5788, public 2012-12-23, https://arxiv.org/abs/1212.5788 .
- A. Premet, *Regular derivations of truncated polynomial rings*, arXiv:1405.2426, public 2014-05-10, https://arxiv.org/abs/1405.2426 .
- D. Hoffmann and P. Kowalski, *A note on integrating group scheme actions*, arXiv:1501.00906, public 2015-01-05, https://arxiv.org/abs/1501.00906 .
