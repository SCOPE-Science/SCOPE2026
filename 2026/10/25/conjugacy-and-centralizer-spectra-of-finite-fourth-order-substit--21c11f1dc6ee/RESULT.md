# Conjugacy and centralizer spectra of finite fourth-order substitution groups

## Finding
Let \(K=\mathbb F_q\), where \(q=p^e\) and \(p\ge5\). Consider the coefficient-field-fixing substitution automorphism group
\[
G=\operatorname{Aut}_K(K[t]/(t^5))
 =\{t\mapsto at+bt^2+ct^3+dt^4:a\in K^\times,\ b,c,d\in K\}.
\]
Write \(h=q-1\) and \(s=\gcd(3,h)\), so \(s\in\{1,3\}\). The multiplier \(a\) is invariant under conjugacy. The following is the **complete** conjugacy-class size spectrum, grouped by multiplier:

| Multiplier \(a\) | Number of classes | Size of each class |
| --- | ---: | ---: |
| \(1\) | \(1\) | \(1\) |
| \(1\) | \(s\) | \(h/s\) |
| \(1\) | \(q\) | \(qh\) |
| \(1\) | \(2\) | \(qh/2\) |
| \(-1\) | \(1\) | \(q^2\) |
| \(-1\) | \(2\) | \(q^2h/2\) |
| each primitive cube root \(a\ne1\) | \(1\) | \(q^2\) |
| each primitive cube root \(a\ne1\) | \(3\) | \(q^2h/3\) |
| every other \(a\ne1\) | \(1\) | \(q^3\) |

A primitive cube root exists precisely when \(3\mid h\); there are \(s-1\) of them. The row for generic multipliers excludes \(1\), \(-1\), and all primitive cube roots. All class sizes above are positive integers, including when \(s=1\). In particular,
\[
\boxed{k(G)=2q+4s},\qquad |G|=q^3(q-1),
\]
and the exact ordered commuting-pair count and commuting probability are
\[
\boxed{|\{(g_1,g_2)\in G^2:g_1g_2=g_2g_1\}|=(2q+4s)q^3(q-1)},
\]
\[
\boxed{\Pr(g_1g_2=g_2g_1)=\frac{2q+4s}{q^3(q-1)}}.
\]
Equivalently, \(k(G)=2q+4\) when \(q\equiv2\pmod3\), and \(k(G)=2q+12\) when \(q\equiv1\pmod3\), for all prime powers of characteristic at least five.

## Assumptions and scope
All automorphisms fix \(K\) pointwise; field-semilinear automorphisms are not included. Group multiplication is substitution/composition truncated modulo \(t^5\). The theorem applies to every finite extension \(\mathbb F_{p^e}\) with \(p\ge5\). It does not assert the same formulas in characteristics two or three. Class sizes are sizes of conjugacy classes in the **full** group \(G\), not classes in the unipotent subgroup alone, and the probability uses a uniform ordered pair of elements of \(G\).

## Proof
**1. Heisenberg-by-torus model.** Let \(U\) be the normal subgroup of substitutions of multiplier one. The split homomorphism sending a substitution to its nonzero coefficient of \(t\) gives \(G=U\rtimes K^\times\), with splitting \(t\mapsto at\). Work in the three-dimensional Lie algebra of truncated derivations
\[
D_{x,y,z}=(xt^2+yt^3+zt^4)\frac{d}{dt},\qquad x,y,z\in K.
\]
Because the truncation is modulo \(t^5\) and \(p\ge5\), the finite exponential \(\exp D=1+D+D^2/2+D^3/6\) is defined and gives a bijection from this Lie algebra to \(U\). In particular its value on the generator is
\[
\exp(D_{x,y,z})(t)=t+xt^2+(y+x^2)t^3+
\left(z+\frac52xy+x^3\right)t^4.
\]
The only nonzero bracket between the displayed basis derivations is
\[
[t^2\partial_t,t^3\partial_t]=t^4\partial_t.
\]
The Baker--Campbell--Hausdorff formula therefore terminates, showing that under exponential coordinates \(U\) has multiplication
\[
(x,y,z)(x',y',z')=
(x+x',y+y',z+z'+(xy'-yx')/2).
\]
This is the three-dimensional Heisenberg group over \(K\). Conjugating the Lie coordinates by \(t\mapsto at\) multiplies \(x,y,z\) by \(a,a^2,a^3\) respectively.

**2. Multiplier one.** Heisenberg conjugation sends \((x,y,z)\) to \((x,y,z+uy-vx)\) for a suitable conjugator \((u,v,w)\), while torus conjugation sends \((x,y,z)\) to \((ax,a^2y,a^3z)\).
If \((x,y)=(0,0)\), the identity \(z=0\) is central in \(G\); the nonzero centers split into \(s\) cube-power cosets, each a class of size \(h/s\). If \(x\ne0\), Heisenberg conjugation kills \(z\) and torus scaling normalizes \(x\) to \(1\), leaving the invariant \(y/x^2\in K\). Thus there are \(q\) classes, each of size \(qh\). If \(x=0\) and \(y\ne0\), Heisenberg conjugation again kills \(z\), and torus scaling identifies nonzero \(y\)'s modulo squares. Since \(q\) is odd, there are two classes, each of size \(qh/2\). These cases exhaust \(U\), and the displayed size-count products total \(q^3\) elements.

**3. Nonidentity multiplier.** Fix \(a\ne1\). Conjugation of the coset \(Ua\) by the Heisenberg subgroup eliminates its first coordinate uniquely, because \(1-a\ne0\). If in addition \(a^2\ne1\), it eliminates the second coordinate; if \(a^3\ne1\), it also eliminates the central coordinate. This is the standard successive central-series elimination: at each step the coordinate changes by a nonzero scalar multiple \(1-a^i\), plus already determined lower-weight terms, and hence has exactly one required solution. When all three factors are nonzero, the coset is a single class of size \(q^3\).

If \(a=-1\), the only resonant weight is \(2\). The first and third coordinates can be eliminated, leaving one parameter \(y\in K\). A conjugation preserving those two zero coordinates cannot alter \(y\); the residual torus scales it by squares. Thus \(y=0\) gives one class of size \(q^2\), and nonzero \(y\) gives two classes of size \(q^2h/2\). The sizes total \(q^3\), exactly the whole multiplier coset.

If \(a\) has order three, the only resonant weight is \(3\). The first two coordinates can be eliminated, leaving one central parameter \(z\in K\), invariant under the residual unipotent conjugations. The torus acts on it by cubes. Thus \(z=0\) produces one class of size \(q^2\), and the nonzero cube classes produce three classes, each of size \(q^2h/3\). These again exhaust that multiplier coset. The case \(a=-1\) and primitive cube root cases are disjoint in characteristic at least five.

**4. Sum and commuting pairs.** The multiplier-one coset contributes \(q+s+3\) classes; \(a=-1\) contributes three; each of the \(s-1\) primitive cube roots contributes \(1+s\) classes; and \(h-s-1\) remaining multipliers each contribute one. Hence
\[
k(G)=q+s+3+3+(s-1)(s+1)+h-s-1=2q+3+s^2=2q+4s,
\]
since \(s\in\{1,3\}\). The number of ordered commuting pairs in a finite group equals its order times its number of conjugacy classes: summing \(|C_G(g)|\) over all elements gives one copy of \(|G|\) for each conjugacy class. The two final formulas follow.

## Verification
A standalone exhaustive checker in `verify.py` enumerates every substitution \((a,b,c,d)\) over the prime fields \(\mathbb F_5\) and \(\mathbb F_7\). It composes truncated polynomials directly, counts centralizers directly, and compares the resulting class-size multisets **separately for each multiplier** with the theorem. It also checks the ordered commuting-pair count and total class count.

Its output was:
```
q=5: |G|=500; commuting ordered pairs=7000; classes=14; multiplier-resolved class sizes verified
q=7: |G|=2058; commuting ordered pairs=53508; classes=26; multiplier-resolved class sizes verified
ALL_FOUR_JET_CHECKS_PASSED
```
These are exhaustive finite checks only for two prime fields; the proof, rather than the checker, establishes the extension-field and all-characteristic-at-least-five quantifiers. Reproduce with `python verify.py` using only a standard Python installation.

## Relationship to prior work
The classical Nottingham group is the subgroup of formal substitutions with multiplier one. Pálfy (1998) analyzes conjugacy counts for **quotients of that unipotent group**, not the larger group of all invertible fourth-order jets. Byszewski--Cornelissen--Tijsma (2020 preprint, 2022 journal) study torsion and automata for the infinite Nottingham group, mainly in characteristic two, not the present odd-characteristic finite-jet class-size table. Gorshkov's 2022 work treats general restrictions on finite-group conjugacy class sizes and motivates obtaining explicit full spectra, but does not classify substitution groups of truncated polynomial rings. Classical formal normal forms inform the method; the use of those techniques is not presented as new. The result here is the explicit **entire full-group** multiplier-resolved finite-field spectrum and cube-root arithmetic jump, not the unipotent class count alone.

## Limitations
No historical uniqueness is asserted. The exact group could appear in earlier work under “extended Nottingham group”, “jet group”, or “triangular solvable algebraic group” terminology, and some inaccessible material could entail these formulas. The literature comparison specifically distinguishes full torus extension from unipotent Nottingham quotients but cannot exclude every unpublished or differently phrased classification. Characteristics two and three are outside scope, as are higher truncations and field-semilinear automorphisms.

## References
1. I. Gorshkov, *Structure of finite groups with restrictions on the set of conjugacy classes sizes*, arXiv:2206.09547v1, first publicly posted 2022-06-20. Primary MSC 20D60.
2. J. Byszewski, G. Cornelissen, D. Tijsma, *Automata and finite order elements in the Nottingham group*, arXiv:2008.04971v1 (2020-08-11), *Journal of Algebra* 602 (2022), 484–554.
3. P. P. Pálfy, *The number of conjugacy classes in some quotients of the Nottingham group*, *Proc. Edinburgh Math. Soc.* 41 (1998), 369–384, DOI:10.1017/S0013091500019714.
