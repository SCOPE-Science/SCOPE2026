# Arithmetic forms and exact rational-point spectra of ordinary Kloosterman Artin–Schreier curves

## Finding

Let \(p\ge 5\) be prime, \(c\in\mathbb F_p^\times\), and \(C_c\) the smooth projective model of
\[
y^p-y=x+\frac{c}{x}.
\]
For an arbitrary nonsquare \(d\in\mathbb F_p^\times\), exactly \(p+3\) mutually nonisomorphic \(\mathbb F_p\)-forms of \(C_c\) occur. They have representatives, for \(a=0,1,\ldots,(p-1)/2\),
\[
A_a:\quad Y^p-Y=X+\frac{c}{X}+a,\qquad
B_a:\quad dW^2=(Y^p-Y-a)^2-4c,
\]
and two additional representatives
\[
R:\quad Y^p+Y=X+\frac{c}{dX},\qquad
S:\quad dW^2=(Y^p+Y)^2-\frac{4c}{d}.
\]
All equations designate their smooth projective normalizations, not just the displayed affine loci. Write \(\chi\) for the quadratic character on \(\mathbb F_p\), with \(\chi(0)=0\), and \(\Delta_a=a^2-4c\). Then
\[
\#A_a(\mathbb F_p)=2+p(1+\chi(\Delta_a)),\quad
\#B_a(\mathbb F_p)=p(1-\chi(\Delta_a)),\quad
\#R(\mathbb F_p)=\#S(\mathbb F_p)=p+1.
\]
Put \(u=\chi(c)\), \(v=\chi(-c)\). The number of representatives \(a\) for which \(\chi(\Delta_a)\) equals \(+1,0,-1\), respectively, is
\[
N_+=\frac{p-1-u+v}{4},\qquad N_0=\frac{1+u}{2},\qquad N_-=\frac{p+1-u-v}{4}.
\]
Thus the point-count multiset has \(N_+\) instances each of \(0\) and \(2p+2\), \(N_0\) each of \(p\) and \(p+2\), \(N_-\) each of \(2\) and \(2p\), plus two instances of \(p+1\). In particular \(N_+>0\) for all \(p\ge5\), hence every \(C_c\) has a pointless \(\mathbb F_p\)-form.

## Assumptions and scope

Every statement is over the prime field \(\mathbb F_p\) in odd characteristic \(p\ge5\), with \(c\ne0\). A form is a smooth projective, geometrically connected curve over \(\mathbb F_p\) becoming isomorphic to \(C_c\) over \(\overline{\mathbb F}_p\). Count forms up to \(\mathbb F_p\)-isomorphism, not marked Artin–Schreier coverings. Each form has genus \(p-1\) and is geometrically ordinary. No claim is made for \(p=3\), extensions \(\mathbb F_{p^r}\), or simultaneous classification as \(c\) varies.

## Proof

**1. The complete Galois-twist classification.** Proposition 8.2 of Tafazolian [1] proves the full geometric group
\[
G=\operatorname{Aut}_{\overline{\mathbb F}_p}(C_c)=\langle\iota\rangle\times\langle\tau,\rho\rangle\cong C_2\times D_{2p},
\]
where \(\tau(x,y)=(x,y+1)\), \(\rho(x,y)=(-x,-y)\), and \(\iota(x,y)=(c/x,y)\). They obey \(\tau^p=\rho^2=\iota^2=1\), \(\rho\tau\rho=\tau^{-1}\), and \(\iota\) is central. These are *all* defined over \(\mathbb F_p\); thus arithmetic Frobenius acts trivially on \(G\). Continuous nonabelian cohomology for a constant finite group gives
\[
H^1(\mathbb F_p,G)=\{\text{conjugacy classes in }G\}.
\]
The conjugacy classes are \(\iota^\epsilon\tau^a\) for \(\epsilon\in\{0,1\}\) and \(a=0,1,\ldots,(p-1)/2\), together with \(\iota^\epsilon\rho\) for \(\epsilon\in\{0,1\}\). This gives \(2(p+1)/2+2=p+3\) classes and exhausts the forms.

**2. Explicit descent.** The equation for \(A_a\) becomes \(C_c\) after adjoining \(\alpha\) with \(\alpha^p-\alpha=a\) and putting \(y=Y-\alpha\); its Frobenius cocycle is \(\tau^{-a}\), with \(a\) indexing classes modulo sign. On \(A_a\), let \(U=Y^p-Y-a\) and \(Z=2X-U\). Since \(U=X+c/X\), direct multiplication gives \(Z^2=U^2-4c\). The central involution \(\iota\) acts by \(Z\mapsto-Z\). Therefore the quadratic twist \(dW^2=U^2-4c\) represents \(\iota\tau^{-a}\).

Choose \(\delta\) with \(\delta^2=d\), so \(\delta^p=-\delta\). Over \(\mathbb F_{p^2}\) the substitution \(x=-\delta X\), \(y=\delta Y\) identifies \(R\) with \(C_c\). Frobenius sends these chosen coordinates to \((-x,-y)\), hence the cocycle is \(\rho\). Taking the central quadratic twist through \(Z=2X-(Y^p+Y)\) gives the last displayed equation \(S\), whose class is \(\iota\rho\). Because \(c\ne0\), the hyperelliptic right sides have degree \(2p\) and simple roots; their smooth models have genus \(p-1\). This proves both existence and distinctness of all displayed forms.

**3. Point counts, including points at infinity.** The degree-\(p\) map \(A_a\to\mathbb P^1_X\) is totally ramified at \(X=0,\infty\), giving two \(\mathbb F_p\)-points there. For \(X\in\mathbb F_p^\times\), the relation \(Y^p-Y=0\) gives \(p\) solutions precisely if \(X^2+aX+c=0\); there are \(1+\chi(\Delta_a)\) such nonzero roots. This yields the asserted \(A_a\) count. On \(B_a\), the even-degree hyperelliptic equation has nonsquare leading coefficient \(1/d\), so neither point above infinity is rational. At each \(Y\in\mathbb F_p\), its equation becomes \(dW^2=\Delta_a\), producing \(1-\chi(\Delta_a)\) solutions and the claimed count.

For \(R\), the map to the \(X\)-line has one totally ramified rational point over each of \(0,\infty\); for each nonzero \(X\in\mathbb F_p\), the equation \(Y^p+Y=2Y=X+c/(dX)\) has exactly one rational solution. Hence \(\#R=p+1\). On \(S\), neither point at infinity is rational, and the affine count is
\[
\sum_{Y\in\mathbb F_p}\Bigl(1-\chi\bigl((2Y)^2-4c/d\bigr)\Bigr)=p+1,
\]
because \(\sum_{t\in\mathbb F_p}\chi(t^2-b)=-1\) whenever \(b\ne0\). The last identity follows by counting \((t,z)\) with \(z^2=t^2-b\): writing \((t-z)(t+z)=b\) gives exactly \(p-1\) pairs, whereas the same count is \(p+\sum_t\chi(t^2-b)\).

**4. Discriminant frequencies and pointless forms.** Since \(4c\ne0\), the same character identity gives \(\sum_{a\in\mathbb F_p}\chi(a^2-4c)=-1\). The value at \(a=0\) is \(v=\chi(-c)\). The nonzero representatives come in opposite-sign pairs, and there are \(1+u\) total zero discriminants. Consequently \(N_0=(1+u)/2\), \(N_+-N_-=(v-1)/2\), and \(N_++N_-=(p-u)/2\); solving gives the three formulas. Finally choose any \(t\in\mathbb F_p^\times\) with \(t^2\ne c\), possible since \(p\ge5\), and put \(a=-(t+c/t)\). Then \(a^2-4c=(t-c/t)^2\ne0\) is a square. Its representative modulo sign lies among the chosen indices, proving \(N_+>0\), and its form \(B_a\) has no rational point.

## Verification

The included executable, `verify_twist_counts.py`, uses only Python's standard library. Run `python3 verify_twist_counts.py`; it exhaustively checks every \(c\in\mathbb F_p^\times\) for each prime \(5\le p\le37\), each rotation representative, all four affine point-count models, and all discriminant-frequency identities. The expected final line is `VERIFY_OK`. This is a finite consistency test; the all-prime theorem rests on the proof above and Proposition 8.2 of [1].

## Relationship to prior work

Tafazolian [1, Proposition 8.2] proves the full geometric automorphism group, hyperelliptic presentation, and geometric parameter-equivalence criterion. It does not provide the \(\mathbb F_p\)-form classification, the four explicit arithmetic descent families, or their complete rational-point spectrum. Ho–Pries [2] study mass formulas of Artin–Schreier covers with *marked* order-\(p\) action, rather than the complete unmarked forms of a fixed Kloosterman curve. The classical work of van der Geer–van der Vlugt [3] concerns Kloosterman sums and Jacobian \(p\)-torsion; its bibliographic description is relevant, but full text was not accessible for a decisive whole-document comparison. The theorem uses standard nonabelian descent and character sums but combines them to classify and count every form in this natural geometric isomorphism class.

## Limitations

The classification is over the prime field only and excludes characteristic three, where [1] identifies an exceptional automorphism group. Isomorphism classes of forms are counted, not families of marked covers nor a moduli count across different geometric parameters. The infinite theorem is independently argued symbolically, while the script checks finitely many primes. An unindexed or inaccessible older twist classification, particularly one implicit in [3], remains a novelty risk. No independent audit has been performed.

## References

[1] Saeed Tafazolian, *Sharp bounds and gap phenomena for large \(p\)-subgroups of automorphism groups of curves*, arXiv:2610.05539v1 (first posted 4 October 2026), Proposition 8.2, https://arxiv.org/abs/2610.05539.

[2] Anne M. Ho and Rachel Pries, *A Mass Formula For Artin–Schreier Curves Over Finite Fields*, arXiv:2203.10187v1 (2022), Sections 1–3, 5, https://arxiv.org/abs/2203.10187.

[3] Gerard van der Geer and Marcel van der Vlugt, *Kloosterman sums and the \(p\)-torsion of certain Jacobians*, Mathematische Annalen 290 (1991), DOI:10.1007/BF01459260 (full text not inspected).
