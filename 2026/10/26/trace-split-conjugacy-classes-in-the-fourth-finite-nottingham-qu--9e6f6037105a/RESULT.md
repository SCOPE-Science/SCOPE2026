# Trace-split conjugacy classes in the fourth finite Nottingham quotient over even fields

## Finding

Let \(q=2^e\), where \(e\ge1\), and let \(G_q\) consist of substitutions
\[
f(t)=t+a t^2+b t^3+c t^4+d t^5\pmod{t^6},\qquad a,b,c,d\in\mathbb F_q,
\]
with multiplication given by composition modulo \(t^6\). This group has order \(q^4\). The conjugacy classes are completely classified as follows, with \(h=b+a^2\):

1. **Central stratum:** when \(a=b=0\), every pair \((c,d)\) gives its own class, of size \(1\), yielding \(q^2\) classes.
2. **First degenerate stratum:** when \(a=0\) and \(b\ne0\), the complete invariant for fixed \(b\) is \(d+c^2/b\). This gives \(q(q-1)\) classes, each of size \(q\).
3. **Second degenerate stratum:** when \(a\ne0\) and \(h=0\), the complete invariant for fixed \(a\) is \(d+ac\). This gives \(q(q-1)\) classes, each of size \(q\).
4. **Trace-split stratum:** when \(a h\ne0\), the complete invariant for fixed \((a,b)\) is
   \[
   \epsilon=\operatorname{Tr}_{\mathbb F_q/\mathbb F_2}\!\left(\frac{d+ac}{a^2(b+a^2)}\right)\in\mathbb F_2.
   \]
   Each of the two trace values gives one class of size \(q^2/2\), for a total of \(2(q-1)^2\) classes.

Consequently the class-size enumerator (coefficient = number of classes; exponent = class size) is
\[
\mathcal K_q(X)=q^2+2q(q-1)X^{q}+2(q-1)^2X^{q^2/2},
\]
where equal-size terms are combined when \(q=2\). In particular,
\[
k(G_q)=5q^2-6q+2,\qquad
\operatorname{cp}(G_q)=\frac{5q^2-6q+2}{q^4}.
\]
The corresponding three centralizer orders are \(q^4\), \(q^3\), and \(2q^2\) (the last two coincide at \(q=2\)). The even extension fields \(q\ge4\) furnish the non-prime-field range; the \(q=2\) specialization is previously covered by prime-field results.

## Assumptions and scope

The characteristic is exactly two. No assumption of algebraic closedness is made. All parameters \(e\ge1\) and all coefficients are included; the classification is of ordinary conjugacy classes under the full composition group, not conjugacy under external formal changes of coordinates. At the quotient modulo \(t^6\), the coefficients of degrees at least six have no effect. The normalized invariants use division only under the explicitly stated nonzero hypotheses.

## Proof

Put \(f(t)=t+a t^2+b t^3+c t^4+d t^5\) and \(g(t)=t+A t^2+B t^3+C t^4+D t^5\). Direct expansion of \(f\circ g\) and \(g\circ f\) modulo \(t^6\) gives the two nontrivial commutation equations
\[
aA^2+(b+a^2)A+aB=0,\qquad bA^2+a^2B=0.
\]
They are independent of \(C,D\). If \(gfg^{-1}\) has final coefficient pair \((c',d')\), its first two coefficients remain \((a,b)\), while
\[
\delta c:=c'-c=aA^2+(b+a^2)A+aB,\qquad
\delta d:=d'-d=bA^2+a^2B.
\]
These follow either by right-composition comparison or by solving \(g\circ f=f'\circ g\); no higher coefficients enter in degree at most five. The centralizer computation is equivalent to setting both increments to zero.

If \(a=b=0\), both increments vanish for all \(A,B\). For \(a=0\), \(b\ne0\), one has \(\delta c=bA\) and \(\delta d=bA^2\). The expression \(d+c^2/b\) is unchanged, and any prescribed \(c'\) is reached by exactly one \(A\); thus the invariant is complete and the orbit has size \(q\).

If \(a\ne0\), define \(h=b+a^2\). Combining the two equations yields
\[
\delta d+a\delta c=h(A^2+aA).
\]
When \(h=0\), \(d+ac\) is invariant. For any fixed \(A\) and any target \(c'\), there is a unique \(B\) making \(\delta c=c'-c\); hence every value of the invariant gives one orbit of size \(q\).

Finally suppose \(ah\ne0\). Again \(B\) independently realizes an arbitrary prescribed \(c'\), and the remaining change in \(d+ac\) ranges precisely over \(h(A^2+aA)\). With \(u=A/a\), the normalized increment is \(u^2+u\). Over every finite field of characteristic two, the additive map \(u\mapsto u^2+u\) has kernel \(\{0,1\}\), hence its image has size \(q/2\). The field trace vanishes on this image because \(\operatorname{Tr}(u^2)=\operatorname{Tr}(u)\); since the trace onto \(\mathbb F_2\) is surjective, its zero kernel also has size \(q/2\). Therefore the normalized expression has precisely two invariant trace fibers and both are single conjugacy classes, of size \(q\cdot q/2=q^2/2\).

There are \(q^2\) choices in the central stratum, \(q(q-1)\) elements in each of the two degenerate coefficient strata \((a,b)\), and \((q-1)^2\) generic coefficient pairs. Accounting for class sizes gives the displayed enumerator and total. The commuting probability identity \(\operatorname{cp}(G)=k(G)/|G|\) follows by counting ordered commuting pairs by centralizers. The noncentral centralizer orders follow from orbit-stabilizer; direct stabilizer equations give \(q^3\) and \(2q^2\) respectively. This completes the classification.

## Verification

The standalone `verify.py` implements arithmetic in \(\mathbb F_2\), \(\mathbb F_4\), \(\mathbb F_8\), and \(\mathbb F_{16}\), exhaustively groups all \(q^4\) elements by the proposed class invariants, and confirms that each invariant fiber is an actual conjugation orbit using all \(q^2\) choices of \((A,B)\). An independently expanded formal-composition routine checks the commuting equations and conjugation identity against every element pair for \(q=2,4\) and 4,000 deterministic pairs for \(q=8,16\). It prints `NOTTINGHAM_QEVEN_CONJUGACY_OK` on success.

The observed class-size multisets are \(\{1:4,2:6\}\) for \(q=2\), \(\{1:16,4:24,8:18\}\) for \(q=4\), \(\{1:64,8:112,32:98\}\) for \(q=8\), and \(\{1:256,16:480,128:450\}\) for \(q=16\). Finite exhaustive computations do not replace the general field-trace argument.

## Relationship to prior work

Pálfy (1998) classified class counts in early Nottingham quotients **over the prime field**, including the \(q=2\) case. York's earlier bound over extension fields, as described in Pálfy's introduction, only reaches quotient order at most \(q^{p+1}=q^3\) in characteristic two, while this quotient has order \(q^4\). Sangroniz's extension-field result cited there explicitly assumes odd characteristic. The new content is the exact all-even-field class partition and class-size distribution for \(q\ge4\), including the Artin–Schreier trace split. Chinburg–Symonds establish a different order-four existence result in the characteristic-two Nottingham group, not the present finite quotient census. The related Hegedűs paper describes characteristic-two subgroup structure; its full text could not be compared. A remotely indexed study of Nottingham braces treats multipermutation levels in odd characteristic, rather than conjugacy over even fields.

## Limitations

No assertion is made for odd characteristic or higher truncation degrees. The entire derivation is algebraic and finite-field-specific: the dichotomy of Artin–Schreier trace fibers need not carry unchanged to infinite fields. Priority is not established absolutely: the full text of Hegedűs (2001), further historical extension-field results, and unindexed equivalences have not been exhaustively eliminated. The proof has not undergone independent mathematical audit.

## References

- P. P. Pálfy, *The number of conjugacy classes in some quotients of the Nottingham group*, Proc. Edinburgh Math. Soc. **41** (1998), 369–384. DOI: `10.1017/S0013091500019714` (full text inspected; Cambridge online date recorded as 2009-01-20; print-day not imputed).
- P. Hegedűs, *The Nottingham Group for p=2*, J. Algebra **246** (2001), 55–69. DOI: `10.1006/jabr.2001.8948` (abstract/metadata only; full text not inspected).
- T. Chinburg and P. Symonds, *An element of order 4 in the Nottingham group at the prime 2*, arXiv:1009.5135v1 (2010), complete three-page preprint inspected.
