# Exact cubic Möbius autocorrelation cancellation when the cube map is bijective

## Finding
For every odd prime power \(q\) with \(3\nmid(q-1)\) and every \(h\in\mathbb F_q^\times\),
\[
\sum_{\substack{f\in\mathbb F_q[T]\\ f\text{ monic},\ \deg f=3}}
\mu(f)\mu(f+h)=0.
\]
The equality is *exact*, at finite field size, rather than an asymptotic cancellation estimate. It applies both to fields with \(q\equiv2\pmod3\) and to finite fields of characteristic three. The restriction on the size is substantive: over \(\mathbb F_7\), the same sum can be nonzero for nonzero shifts.

## Assumptions and scope
The polynomial Möbius function is zero on nonsquarefree polynomials and equals \((-1)^r\) on products of \(r\) distinct monic irreducibles. The quadratic character \(\chi\) on \(\mathbb F_q\) is extended by \(\chi(0)=0\). The shift \(h\) is a nonzero *constant*. All monic cubic polynomials, including those with repeated roots, enter the sum. The field order \(q\) is odd, so the classical polynomial discriminant and Pellet identity apply. There is no restriction on the extension degree of the finite field.

## Proof
For every monic cubic \(f\) over an odd finite field, Pellet's identity gives \(\mu(f)=-\chi(\operatorname{disc}f)\). Hence the summand is \(\chi(\Delta(f)\Delta(f+h))\), with the vanishing at repeated-root cubics handled automatically.

**Case 1: \(\operatorname{char}\mathbb F_q\ne3\).** Write \(f(T)=T^3+aT^2+bT+d\) and translate \(Y=T+a/3\). There are unique \(A,B\in\mathbb F_q\) with \(f(T)=Y^3+AY+B\), and the change of variables from \((b,d)\) to \((A,B)\), for fixed \(a\), is bijective. The discriminant is \(\Delta=-4A^3-27B^2\), while replacing \(f\) by \(f+h\) replaces \(B\) by \(B+h\). Thus the desired sum is
\[
q\sum_{A,B\in\mathbb F_q}
\chi\bigl((-4A^3-27B^2)(-4A^3-27(B+h)^2)\bigr).
\]
Now \(3\nmid(q-1)\) makes the cube map a bijection on \(\mathbb F_q\). We may replace \(-4A^3\) with a freely ranging variable \(U\). For any \(u,v\in\mathbb F_q\), the elementary quadratic-character identity is
\[
\sum_{U\in\mathbb F_q}\chi((U-u)(U-v))=
\begin{cases}q-1,&u=v,\\-1,&u\ne v.\end{cases}
\]
Indeed the equal case is the sum of \(\chi((U-u)^2)\); for distinct roots, translate and rescale to count solutions to \(Y^2=Z(Z-1)\), obtaining \(q-1\) solutions, hence character sum \(-1\). Since \(27B^2=27(B+h)^2\) holds exactly when \(B=-h/2\) (as \(h\ne0\) and the characteristic is odd), exactly one of the \(q\) inner character sums is \(q-1\), and the other \(q-1\) sums equal \(-1\). Their sum is zero.

**Case 2: \(\operatorname{char}\mathbb F_q=3\).** The general cubic discriminant specializes to
\[
\Delta(T^3+aT^2+bT+d)=a^2b^2-b^3-a^3d.
\]
When \(a\ne0\), as \(d\) varies the first discriminant runs bijectively through \(\mathbb F_q\), and the shifted discriminant differs by the nonzero constant \(-a^3h\). The preceding two-root character identity therefore makes the sum over \(d\) equal \(-1\) for each \((a,b)\) with \(a\ne0\). All these terms contribute \(-q(q-1)\). When \(a=0\), both discriminants equal \(-b^3\), independent of \(d\), so their character product is one if \(b\ne0\) and zero if \(b=0\). These terms contribute \(q(q-1)\). The two contributions cancel exactly. This also proves the result for every odd extension field of characteristic three. \(\square\)

## Verification
The self-contained file `verify_mobius.py` computes arithmetic in ten concrete finite fields, detects squarefreeness and Möbius signs using polynomial roots and derivatives independently of the discriminant proof, and sums \(\mu(f)\mu(f+h)\) over all monic cubics and all nonzero constants \(h\). Running `python3 verify_mobius.py` returned `VERIFY_OK fields 10 shift_cases 130`. In particular, all tested orders \(3,5,9,11,17,23,27\), which obey the hypotheses, gave zero for every tested shift. In the excluded orders \(7,13,25\), the verifier produced nonzero autocorrelations, confirming that no unrestricted all-odd-field cancellation is being asserted. The finite checks corroborate rather than prove the universal assertion.

## Relationship to prior work
Carmon and Rudnick prove a function-field analogue of Chowla's conjecture, giving an asymptotic bound on polynomial Möbius correlations over growing finite fields for fixed polynomial degree; their 2012 preprint explicitly includes constant shifts. This theorem addresses the same two-factor correlation in the cubic case but determines an exact zero in a natural infinite family of field orders. Keating and Rudnick study related averages and correlations of polynomial Möbius functions, primarily in asymptotic regimes. The stated earlier theorems do not by themselves imply this finite-field identity. Characteristic-three cancellation is treated separately because cubic depression is unavailable there. No claim of priority beyond the comparisons made here is implied.

## Limitations
The theorem does not cover even characteristic, cubic shifts other than nonzero constants, or fields with \(q\equiv1\pmod3\). It does not classify the nonzero correlation values in excluded fields or extend the exact vanishing to higher polynomial degree. Further historical literature may contain equivalent special cases; independent mathematical validation has not been performed.

## References
1. D. Carmon and Z. Rudnick, *The autocorrelation of the Möbius function and Chowla's conjecture for the rational function field*, arXiv:1205.1599 (first posted 2012-05-08), https://arxiv.org/abs/1205.1599; DOI: 10.1093/qmath/has047.
2. J. P. Keating and Z. Rudnick, *Squarefree polynomials and Möbius values in short intervals and arithmetic progressions*, arXiv:1504.03444 (first posted 2015-04-14), https://arxiv.org/abs/1504.03444.
