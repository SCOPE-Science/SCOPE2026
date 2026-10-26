# Square-zero endomorphisms of unequal cyclic prime-power pairs with first exponent at most two

## Finding

For a prime \(p\) and integers \(1\leq a<b\), put
\[
G_{a,b}(p)=C_{p^a}\oplus C_{p^b},\qquad
Q_{a,b}(p)=\#\{T\in\operatorname{End}(G_{a,b}(p)):T^2=0\}.
\]
The following is an exact count for both of the first two possible shorter cyclic exponents, at every prime and every larger exponent:
\[
\boxed{Q_{1,b}(p)=
\begin{cases}(2p-1)p^{b/2},&b\text{ even},\\
p^{(b+3)/2},&b\text{ odd},\end{cases}\quad b\geq2.}
\]
\[
\boxed{Q_{2,b}(p)=
\begin{cases}(2p^2-1)p^{(b+2)/2},&b\text{ even},\\
(3p-2)p^{(b+3)/2},&b\text{ odd},\end{cases}\quad b\geq3.}
\]
Thus for either \(a\in\{1,2\}\), and every \(b>a\), the exact two-step stabilization law is
\[
Q_{a,b+2}(p)=pQ_{a,b}(p).
\]
The zero map is counted; the number of nonzero square-zero endomorphisms is \(Q_{a,b}(p)-1\). No formula for a shorter exponent \(a\geq3\) is asserted.

## Assumptions and scope

All groups are additive finite abelian groups. The symbol \(C_{p^j}\) denotes a cyclic group of order \(p^j\). The endomorphism square \(T^2\) means composition; it does **not** mean an entrywise square or an involution equation. The prime \(p\) can equal two. No restriction is placed on the size of \(b\), except \(b>a\). The invariant counts individual endomorphisms, not their conjugacy classes, images, or isomorphism types.

Write \(h=b-a\). Every endomorphism has a *unique* coordinate representation
\[
T=\begin{pmatrix}u&v\\p^h w&z\end{pmatrix},\qquad
u,v,w\in\mathbb Z/p^a\mathbb Z,\quad
z\in\mathbb Z/p^b\mathbb Z.
\]
In the displayed matrix, products in the first row are interpreted modulo \(p^a\) and products in the second modulo \(p^b\). The equations \(T^2=0\) are equivalent to the four congruences
\[
\begin{aligned}
\text{(i)}&:\quad u^2+p^h vw\equiv0\pmod{p^a},\\
\text{(ii)}&:\quad v(u+z)\equiv0\pmod{p^a},\\
\text{(iii)}&:\quad w(u+z)\equiv0\pmod{p^a},\\
\text{(iv)}&:\quad z^2+p^h vw\equiv0\pmod{p^b}.
\end{aligned}
\]
The displayed congruences, with these moduli, are also sufficient, so no invertibility assumption is present.

## Proof

**1. The short exponent one.** Suppose \(a=1\). Since \(h\geq1\), the first equation gives \(u=0\) in \(\mathbb F_p\). Put \(t=vw\) in \(\mathbb F_p\). There are \(2p-1\) ordered pairs \((v,w)\) with \(t=0\). For all of these, the last equation is \(z^2=0\) modulo \(p^b\), admitting \(p^{\lfloor b/2\rfloor}\) choices. Every such \(z\) is divisible by \(p\), making both off-diagonal equations automatic.

If \(t\ne0\), the last congruence forces \(v_p(z^2)=b-1\), where \(v_p\) denotes the integer \(p\)-adic valuation. This is impossible for even \(b\). For odd \(b=2k+1\), we must have \(v_p(z)=k\), giving \((p-1)p^k\) possibilities for \(z\). Each such \(z\) specifies a unique nonzero residue \(t\) through \(t\equiv-z^2/p^{2k}\pmod p\), and every prescribed nonzero \(t\) has exactly \(p-1\) factorizations \(t=vw\) in \(\mathbb F_p\). Here \(k\geq1\), so again \(z\equiv0\pmod p\). The additional count is \((p-1)^2p^k\). The total for odd \(b\) is
\[
(2p-1)p^k+(p-1)^2p^k=p^{k+2},
\]
which gives the stated first boxed formula.

**2. A product-fiber lemma modulo \(p^2\).** In \(R=\mathbb Z/p^2\mathbb Z\), the number of ordered pairs \((v,w)\in R^2\) with product equal to a prescribed \(t\in R\) is
\[
F(t)=\begin{cases}
p(3p-2),&t=0,\\
2p(p-1),&v_p(t)=1,\\
p(p-1),&t\text{ a unit}.
\end{cases}
\]
For a unit \(t\), either coordinate may be chosen as a unit and the other is determined, giving \(p(p-1)\) choices. For a nonzero \(t\) divisible by \(p\), exactly one coordinate is a unit and the other is in \(pR\), giving two such contributions. For zero product, partition according to \(v=0\), \(v\) a nonzero multiple of \(p\), or \(v\) a unit; this gives respectively \(p^2\), \(p(p-1)\), and \(p(p-1)\) pairs. This proves the lemma.

**3. The short exponent two, with \(b\geq5\).** Now \(a=2\) and \(h=b-2\geq3\). Reducing the first congruence modulo \(p^2\) gives \(u=p\alpha\) for unique \(\alpha\in\mathbb F_p\). The last congruence forces \(z\equiv0\pmod{p^2}\), since \(z^2\equiv0\pmod{p^3}\). Hence the two off-diagonal congruences become
\[
\alpha v\equiv\alpha w\equiv0\pmod p.
\]
When \(\alpha\ne0\), both \(v,w\) are divisible by \(p\), so \(t=vw=0\) in \(R\). When \(\alpha=0\), all \(v,w\) are permitted and their product is distributed according to the lemma. Write \(k=\lfloor b/2\rfloor\). The \(t=0\) contribution, combining the two possible \(\alpha\) cases, is
\[
\bigl((p-1)p^2+p(3p-2)\bigr)p^k
=p^{k+1}(p^2+2p-2).
\]
If \(b=2k\) is even, the only additional possible products are units \(t\); then \(v_p(z)=k-1\). There are \((p-1)p^k\) such \(z\), each prescribing a unit \(t\), with \(p(p-1)\) factorizations. The additional count is \(p^{k+1}(p-1)^2\), so
\[
Q_{2,2k}(p)=p^{k+1}\bigl(p^2+2p-2+(p-1)^2\bigr)
=(2p^2-1)p^{k+1}.
\]
If \(b=2k+1\) is odd, instead \(t\) must have valuation exactly one, forcing \(v_p(z)=k\). There are \((p-1)p^k\) possible \(z\), each prescribing such a \(t\) with \(2p(p-1)\) factorizations. The additional count is \(2p^{k+1}(p-1)^2\), hence
\[
Q_{2,2k+1}(p)=p^{k+1}\bigl(p^2+2p-2+2(p-1)^2\bigr)
=(3p-2)p^{k+2}.
\]
The valuation alternatives exhaust all possible \(t\): an odd square valuation cannot match an even one. The off-diagonal congruences force \(\alpha=0\) whenever \(t\ne0\), as already included.

**4. Exceptional boundaries \(b=3,4\).** These cannot be inferred by assuming \(z\equiv0\pmod{p^2}\), so they are checked separately. In both cases \(u=p\alpha\). For \(b=3\), \(h=1\) and the first equation restricts \(t=vw\) to multiples of \(p\). If \(t=0\) in \(R\), then \(z\equiv0\pmod{p^2}\), giving \(p\) choices of \(z\), and \(p(3p-2)+(p-1)p^2\) choices of \((\alpha,v,w)\). If \(v_p(t)=1\), then \(z=p s\) with \(s\) a unit modulo \(p\), and \(t\) is determined by \(s\); each \(z\) admits \(2p(p-1)\) factor pairs, and at least one of \(v,w\) is a unit, forcing \(\alpha\equiv-s\pmod p\). There are \(p(p-1)\) such \(z\). Thus
\[
Q_{2,3}(p)=p\bigl(p(3p-2)+(p-1)p^2\bigr)+2p^2(p-1)^2=(3p-2)p^3.
\]
For \(b=4\), \(h=2\). If \(z\equiv0\pmod{p^2}\), the final equation implies \(t=0\), contributing \(p^2\bigl(p(3p-2)+(p-1)p^2\bigr)\). Otherwise \(z=p s\) with \(s\) a unit, the last equation prescribes a unit \(t\), hence both \(v,w\) are units and the middle equations uniquely determine \(\alpha\equiv-s\pmod p\). There are \((p-1)p^2\) such \(z\) and \(p(p-1)\) factor pairs for each. Therefore
\[
Q_{2,4}(p)=p^2\bigl(p(3p-2)+(p-1)p^2\bigr)+p^3(p-1)^2=(2p^2-1)p^3.
\]
These agree with the general even/odd formulas. Every case has now been proved. The two-step recurrence follows immediately from the four closed expressions. \(\square\)

## Verification

The standalone Python file `verify.py` enumerates all allowed endomorphism coordinates independently and tests the four congruences directly, comparing the resulting count with the theorem. It checks \(37\) finite cases at primes \(2,3,5,7\) and directly checks the three product-fiber sizes modulo \(p^2\) for all four primes. Run `python3 verify.py` in an ordinary Python 3 environment. Its expected terminal line begins with `SQUARE_ZERO_MIXED_P_GROUP_OK 37 exhaustive_cases`. These finite checks do not substitute for the preceding proof for all primes and exponents.

## Relationship to prior work

Hillar and Rhea, *Automorphisms of finite Abelian groups* (arXiv:math/0605185v1, May 8, 2006), Section 3, Theorem 3.3 and Lemma 3.4, describe finite abelian group endomorphisms through divisibility-constrained integer matrices; this foundational parametrization supplies the setup. Section 4 counts the invertible maps, whereas the present invariant counts noninvertible square-zero maps. Breaz and collaborators, *Nil-clean matrix rings* (arXiv:1310.0416v1), address nil-clean structure and related endomorphism-ring properties; those properties do not give these individual square-zero multiplicities. The study *Dynamics of Endomorphism of Finite Abelian Groups* analyzes orbit dynamics rather than this arithmetic census. Related fixed-point counts for automorphisms likewise do not imply these formulas because a nontrivial finite group cannot have an invertible square-zero endomorphism.

## Limitations

No classification or count is asserted for \(a\geq3\), for endomorphisms with higher nilpotence index, or for individual conjugacy orbits. The general literature might contain a more inclusive enumeration; no absolute priority guarantee is claimed. In particular, an accessible abstract of a more recent study of special endomorphisms did not permit full-text comparison, and only the subset of square-zero maps with equal image and kernel is directly related to that paper's stated object.

## References

1. Christopher J. Hillar and Darren L. Rhea, *Automorphisms of finite Abelian groups*, arXiv:math/0605185v1 (2006-05-08), https://arxiv.org/abs/math/0605185.
2. *Nil-clean matrix rings*, arXiv:1310.0416v1 (2013-10-01), https://arxiv.org/abs/1310.0416.
3. Zhao Jinxing and Nan Jizhu, *Dynamics of Endomorphism of Finite Abelian Groups* (2017), https://doi.org/10.1155/2017/6295430, supplementary dynamical comparison.
4. A. Sarwary, *Special endomorphisms of finitely generated Abelian groups*, Chebyshevskii Sb. 26:3 (2025), 247–256, https://doi.org/10.22405/2226-8383-2025-26-3-247-256; abstract-level supplementary comparison; full text not inspected.
