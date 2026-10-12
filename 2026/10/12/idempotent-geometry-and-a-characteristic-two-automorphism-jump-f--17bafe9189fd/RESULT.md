# Idempotent geometry and a characteristic-two automorphism jump for the four-element dihedral quandle algebra

## Finding

Let \(K\) be any field and let \(A_K=K[R_4]\) be the four-dimensional, nonunital, nonassociative algebra with distinguished basis \(a_0,a_1,a_2,a_3\) and bilinear product
\[
a_i a_j=a_{2j-i\ (\mathrm{mod}\ 4)}.
\]
Write \(x=c_0a_0+c_1a_1+c_2a_2+c_3a_3\), \(E=c_0+c_2\), and \(O=c_1+c_3\). Its idempotents and its complete group of \(K\)-linear algebra automorphisms undergo simultaneous characteristic-dependent transitions:

1. If \(\operatorname{char} K\ne2\), the idempotent set is the origin together with three affine lines
\[
\begin{aligned}
L_e&=\{c_0a_0+c_2a_2:c_0+c_2=1\},\\
L_o&=\{c_1a_1+c_3a_3:c_1+c_3=1\},\\
L_m&=\{\tfrac{t}{2}(a_0+a_2)+\tfrac{1-t}{2}(a_1+a_3):t\in K\}.
\end{aligned}
\]
The third line meets each of the first two in one point; the first two are disjoint. Furthermore,
\[
\operatorname{Aut}_K(A_K)\cong(K^\times\times K^\times)\rtimes C_2,
\]
with the nonidentity element of \(C_2\) interchanging the factors.

2. If \(\operatorname{char} K=2\), the idempotent set is the origin together with two disjoint affine planes
\[
P_e=\{x:E=1,\ O=0\},\qquad P_o=\{x:E=0,\ O=1\}.
\]
Moreover,
\[
\operatorname{Aut}_K(A_K)\cong (K^4,+)\rtimes C_2,
\]
where the involution acts on \(K^4=\operatorname{Hom}_K(K^2,K^2)\) by simultaneous interchange of its source and target coordinate axes. The automorphism group acts transitively on all nonzero idempotents.

Consequently, if \(K=\mathbb F_q\), the numbers of nonzero idempotents and automorphisms are respectively
\[
\begin{array}{c|cc}
&\#\{x\ne0:x^2=x\}&|\operatorname{Aut}_K(A_K)|\\ \hline
q\text{ odd}&3q-2&2(q-1)^2\\
q\text{ even}&2q^2&2q^4
\end{array}.
\]
For example, over \(\mathbb F_2\) there are eight nonzero idempotents and thirty-two automorphisms, whereas over \(\mathbb F_3\) there are seven nonzero idempotents and eight automorphisms.

## Assumptions and scope

All isomorphisms are of abstract groups of \(K\)-linear algebra automorphisms, not assertions about automorphism group schemes or extensions to nonfields. There are no finiteness or algebraic-closedness assumptions on \(K\). For finite-field counts, \(q\) is any prime power of the stated parity. Multiplication is that of the dihedral quandle algebra; it is not assumed associative.

## Proof

**1. A characteristic-free normal form.** Set
\[
p=a_0,\quad q_0=a_1,\quad u=a_0-a_2,\quad v=a_1-a_3.
\]
The vectors \(p,q_0,u,v\) form a basis over every field. The full multiplication is determined by
\[
\begin{array}{c|cccc}
& p&q_0&u&v\\\hline
p&p&p-u&0&0\\
q_0&q_0-v&q_0&0&0\\
u&u&-u&0&0\\
v&-v&v&0&0
\end{array}.
\]
It follows that \(J=\operatorname{span}(u,v)\) is the intrinsic right annihilator \(\{z:A_Kz=0\}\): the right-multiplication action on the span of \(p,q_0\) has trivial common kernel (evaluate at \(p\) and \(q_0\) in the displayed table). The quotient \(L=A_K/J\) is the two-dimensional left-zero algebra
\[
xy=\varepsilon(y)x,\qquad \varepsilon(\alpha\bar p+\beta\bar q_0)=\alpha+\beta.
\]
An automorphism therefore preserves \(J\), and its induced automorphism \(B\) of \(L\) preserves \(\varepsilon\).

**2. Idempotents.** The multiplication rule immediately gives
\[
x^2=(Ec_0+Oc_2)a_0+(Oc_1+Ec_3)a_1+(Ec_2+Oc_0)a_2+(Oc_3+Ec_1)a_3.
\]
Since the augmentation of a product is the product of augmentations, \(x^2=x\) implies \((E+O)^2=E+O\), so the augmentation is zero or one. If it is zero, the coefficient sum in each parity class of \(x^2\) is zero, hence \(E=O=0\) and then \(x=x^2=0\). If it is one, put \(E=t\), \(O=1-t\). The remaining equations reduce exactly to
\[
(1-t)(c_0-c_2)=0,\qquad t(c_1-c_3)=0.
\]
For \(\operatorname{char}K\ne2\), if \(t\notin\{0,1\}\) the coefficients within each parity class coincide, giving \(L_m\); the endpoints yield \(L_e\) and \(L_o\). For characteristic two, \(c_0-c_2=E=t\) and \(c_1-c_3=O=1-t\), so the equations force \(t(1-t)=0\), hence precisely the two stated planes. All constructions are reversible.

**3. Automorphisms in characteristic other than two.** The vectors
\[
b=p-\tfrac12u=\tfrac12(a_0+a_2),\quad c=q_0-\tfrac12v=\tfrac12(a_1+a_3)
\]
span an algebra complement to \(J\) satisfying \(xy=\varepsilon(y)x\). On \(J\), right multiplication by \(\alpha b+\beta c\) has two distinct characters \(\chi_u=\alpha-\beta\) and \(\chi_v=\beta-\alpha\). Write an automorphism as \(F(x+z)=Bx+t(x)+Sz\) with \(x\) in that complement, \(z\in J\). Multiplicativity with two complement inputs gives \(t(x)\,By=\varepsilon(y)t(x)\); because neither \(\chi_u\) nor \(\chi_v\) equals augmentation, \(t=0\). Multiplicativity with one \(J\) input now means \(S\) intertwines the two right characters under \(B\). Since they are distinct and \(S\) invertible, \(B\) either fixes the ordered pair or swaps it. The functionals \(\varepsilon\) and \(\chi_u\) form a basis of \(L^*\), so \(B\) must be the identity or the swap of \(b,c\). Accordingly, \(S\) scales \(u,v\) independently or swaps them while scaling. Every such map preserves the full displayed multiplication table and is invertible. This establishes \((K^\times)^2\rtimes C_2\).

**4. Automorphisms in characteristic two.** Use the complement \(\operatorname{span}(p,q_0)\). The right action of \(L\) on \(J\) is now scalar multiplication by augmentation. Its multiplication defect is the \(J\)-valued bilinear map with
\[
f(p,p)=f(q_0,q_0)=0,\qquad f(p,q_0)=u,\quad f(q_0,p)=v,
\]
where we identify \(L\) with its complement. Any automorphism has block form \(F(x+z)=Bx+t(x)+Sz\), where \(\varepsilon B=\varepsilon\), \(t:L\to J\) is linear and \(S\in\operatorname{GL}(J)\). The multiplicativity equations are exactly
\[
S f(x,y)=f(Bx,By);
\]
all terms involving \(t\) cancel because \(J\) is the right annihilator and its right action is by augmentation. If \(Bp=\alpha p+\beta q_0\), then \(\alpha+\beta=1\) and \(f(Bp,Bp)=\alpha\beta(u+v)=0\). Since \(u+v\ne0\) and \(K\) is a field, \(\alpha\beta=0\), implying \(Bp\) is \(p\) or \(q_0\). Invertibility and the same argument for \(Bq_0\) force \(B\) to be the identity or swap. Then the equations force \(S\) to be the same identity or swap on \(u,v\). Conversely **every** linear \(t:L\to J\) yields an automorphism, giving a normal additive subgroup \(\operatorname{Hom}_K(L,J)\cong K^4\) and a two-element complement. Conjugation by the swap interchanges source and target coordinates. Finally, varying \(t(p)\) sweeps \(P_e\), varying \(t(q_0)\) sweeps \(P_o\), and the swap interchanges the planes: the action on nonzero idempotents is transitive.

## Verification

The standalone, standard-library-only `checker.py` directly enumerates all four-component vectors and all invertible multiplicative maps for the prime fields \(\mathbb F_2,\mathbb F_3,\mathbb F_5\). It verifies exactly the nonzero-idempotent and automorphism counts \((8,32),(7,8),(13,32)\). In \(\mathbb F_4=\mathbb F_2[t]/(t^2+t+1)\), it enumerates all \(256\) algebra elements and verifies all \(33\) idempotents (including zero), as well as all \(512\) distinct algebra automorphisms **constructed by the theorem**; this last enumeration does not independently exhaust all invertible linear maps over \(\mathbb F_4\). Run `python checker.py` and require `VERIFY_OK`. The arbitrary-field classification is proved above algebraically; finite tests alone are not a proof of it.

## Relationship to prior work

Bardakov–Passi–Singh (arXiv:2001.06843, Proposition 4.4 and Theorem 6.4) completely describe the **integral** idempotents and integral automorphism group of \(\mathbb Z[R_4]\). Their integral idempotents are the two parity-class families, and their group \((C_2\times C_2)\rtimes C_2\) agrees with the integral-unit specialization of the odd-characteristic normal form, but does **not** establish the finite-field symmetry jump or the two-plane characteristic-two locus. Elhamdadi–Nunez–Singh–Swain (arXiv:2204.11288, Theorem 4.5 and Corollaries 4.6–4.8) classify idempotents under covering hypotheses that are not satisfied by the nontrivial idempotents of the two-point trivial-quandle quotient \(R_4\to R_2\), and their even-dihedral family in Corollary 4.8 has odd half-order. Sangare–Ta (arXiv:2608.01550, Theorems 4.13 and 4.15 and Problem 4.14) determine odd-half-order automorphism groups, but for even half-order (including \(R_4\)) establish only a characteristic-not-two embedding, not these exact groups. Bardakov–Elhamdadi (arXiv:2601.07057, Proposition 4.5) give integral claims about \(R_4\) and cite the book Corollary 13.42 concerning additional idempotents; this is not treated as a novelty claim for integral idempotents.

## Limitations

This theorem concerns algebra automorphisms and idempotents over fields only. It does not determine scheme-theoretic automorphism groups or idempotents over general coefficient rings. The original classification of integral idempotents is prior work. The book preprint arXiv:2506.23175, specifically Corollary 13.42 cited in later work, could not be inspected in full and might overlap part of the field-idempotent description; the genuinely distinguished group-theoretic claim is the explicit characteristic-dependent **full automorphism group** and resulting geometric orbit behavior. Exhaustive computations cover only the stated fields, with no claim of independent certification or universal computational proof.

## References

1. V. G. Bardakov, I. B. S. Passi and M. Singh, *Zero-divisors and idempotents in quandle rings*, arXiv:2001.06843 (first public version 2020-01-19), Osaka J. Math. 59 (2022), 611–637; Proposition 4.4 and Theorem 6.4.
2. M. Elhamdadi, B. Nunez, M. Singh and D. Swain, *Idempotents, free products and quandle coverings*, arXiv:2204.11288; Theorem 4.5 and Corollaries 4.6–4.8.
3. B. Sangare and L. Ta, *Idempotents, automorphism groups, and commutator widths of quandle algebras*, arXiv:2608.01550; Theorems 4.13–4.15, Problem 4.14.
4. V. Bardakov and M. Elhamdadi, *Idempotents and powers of ideals in quandle rings*, arXiv:2601.07057; Proposition 4.5 and its reference to Corollary 13.42 of arXiv:2506.23175.
5. V. Bardakov, M. Elhamdadi and M. Singh, *Yang–Baxter Equation and Related Algebraic Structures*, arXiv:2506.23175, Section 13 (full-text comparison remained unavailable).
