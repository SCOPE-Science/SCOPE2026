# The \(Q_{56}\) line-parameter field is biquadratic
## Finding
In the explicit model of the rigid 56-line quartic \(Q_{56}\), let \(p,q\) be the parameters chosen in the source:
\[
q=\frac{p-1}{p+1},\qquad p^4-p^3+2p^2+p+1=0.
\]
The field used there to define all 56 lines has the explicit structure
\[
\mathbb Q(p)=\mathbb Q(\sqrt5,\sqrt{-3}),
\]
so it is a biquadratic Galois extension of \(\mathbb Q\). Its four conjugates of \(p\) are
\[
p,\quad -\frac1p,\quad -q,\quad \frac1q.
\]
The involution \(p\mapsto-1/p\) fixes exactly the quadratic subfield \(\mathbb Q(\sqrt{-15})\), which is the field over which the source states that the quartic itself is defined.

## Assumptions and scope
Work in characteristic zero with Veniani's normalization of Section 5.2. The statement identifies the arithmetic structure of the source's field \(\mathbb Q(p)\), over which all lines are defined. It does not claim that this field is minimal for every individual line, nor does it assign a Galois permutation to each of the 56 labeled lines.

## Proof
Put
\[
f(T)=T^4-T^3+2T^2+T+1.
\]
The polynomial has no rational root. If it factored over \(\mathbb Q\) into monic quadratics, Gauss's lemma gives integer constant terms. Since the constant term is \(1\), the only possibilities are \((1,1)\) or \((-1,-1)\). The first forces the middle quadratic coefficient product to be zero and gives the wrong linear coefficient. The second would require rational roots of \(X^2+X+4\), whose discriminant is \(-15\). Thus \(f\) is irreducible and \([\mathbb Q(p):\mathbb Q]=4\).

Direct substitution gives
\[
f(-1/p)=\frac{f(p)}{p^4},
\]
\[
f\!\left(\frac{1-p}{1+p}\right)=\frac{4f(p)}{(1+p)^4},
\qquad
f\!\left(\frac{1+p}{p-1}\right)=\frac{4f(p)}{(p-1)^4}.
\]
These three Möbius transformations are distinct involutions, and the first two commute with product equal to the third. Since all four roots already lie in \(\mathbb Q(p)\), the degree-four extension is normal and
\[
\operatorname{Gal}(\mathbb Q(p)/\mathbb Q)\cong C_2\times C_2.
\]
Using \(q=(p-1)/(p+1)\), the four roots are exactly \(p,-1/p,-q,1/q\).

Now define
\[
s=2p-1-\frac2p.
\]
Reduction modulo \(f(p)\) gives \(s^2=-15\). Moreover, \(s\) is fixed by \(p\mapsto-1/p\), whereas each of the other two nontrivial Möbius involutions sends \(s\) to \(-s\). Hence the fixed field of \(p\mapsto-1/p\) is
\[
\mathbb Q(s)=\mathbb Q(\sqrt{-15}).
\]
Over this field,
\[
f(T)=\left(T^2-\frac{1+s}{2}T-1\right)
      \left(T^2-\frac{1-s}{2}T-1\right).
\]
Set \(a=(1+s)/2\). The discriminant of the first quadratic is \(a^2+4=a\). If \(u^2=a\), then \(p=(a+u)/2\) after choosing one of the two roots, so \(\mathbb Q(p)=\mathbb Q(s,u)\). Put \(v=2/u\). Since \(a(1-s)/2=4\), one has \(v^2=(1-s)/2\), and therefore
\[
(u+v)^2=5,\qquad (u-v)^2=-3,\qquad (u+v)(u-v)=s.
\]
Thus
\[
\mathbb Q(p)=\mathbb Q(\sqrt5,\sqrt{-3}).
\]
In particular its three quadratic subfields are \(\mathbb Q(\sqrt5)\), \(\mathbb Q(\sqrt{-3})\), and \(\mathbb Q(\sqrt{-15})\).

Finally, under the relative involution \(p\mapsto-1/p\), the relation for \(q\) gives \(q\mapsto-1/q\). In the displayed quartic equation of the source, the four coefficient groups are
\[
2p^2q^2,
\quad (p^4+1)(q^4+1),
\quad -2q^2(p^4+1),
\quad -2p^2(q^4+1).
\]
After \((p,q)\mapsto(-1/p,-1/q)\), all four are multiplied by the common scalar \(1/(p^4q^4)\). Hence the projective equation is fixed, giving an equation-level explanation of the descent to \(\mathbb Q(\sqrt{-15})\).

## Verification
The accompanying `verify.py` checks the polynomial identities over exact rational arithmetic, the three Möbius root transformations and their Klein-four composition law, the identity \(s^2=-15\), the factorization over \(\mathbb Q(s)\), the quadratic-subfield relations, and the common scalar by which the quartic coefficient vector transforms.

## Relationship to prior work
Veniani constructs the explicit \(Q_{56}\) equation, proves the parameter relation \(q=(p-1)/(p+1)\), obtains the quartic polynomial for \(p\), and states that the surface is defined over \(\mathbb Q(\sqrt{-15})\) while all lines are defined over \(\mathbb Q(p)\). The source does not identify \(\mathbb Q(p)\) as a named biquadratic field or give the Möbius description of its Galois group in the inspected Section 5.2. The earlier projective classification of quartics with more than 52 lines establishes the rigid configuration containing \(Q_{56}\), but the later source explicitly presents the equation of \(Q_{56}\) as one of the previously missing explicit equations.

## Limitations
The result concerns the particular field \(\mathbb Q(p)\) appearing in the explicit construction. It does not prove that every individual line has minimal field of definition \(\mathbb Q(p)\), and it does not determine the permutation representation of the Galois group on all 56 lines. Those stronger questions require the complete labeled line equations.

## References
1. D. C. Veniani, *Symmetries and equations of smooth quartic surfaces with many lines*, arXiv:1708.01219, especially Section 5.2 and Remark 5.1; Rev. Mat. Iberoam. 36 (2020), 233–256.
2. A. Degtyarev, I. Itenberg, A. S. Sertöz, *Lines on quartic surfaces*, arXiv:1601.04238; Math. Ann. 368 (2017), 753–809.
