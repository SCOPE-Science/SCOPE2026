# Exact periodic-point counts for higher unit-torus permutation lifts

## Finding

Every higher unit-torus permutation lift of a \(q\)-linearized permutation admits an explicit formula for the number of fixed points of **each iterate**, in terms of scalar eigenspaces of the underlying linearized map and one cyclic-group greatest common divisor. These counts determine its complete cycle decomposition by Möbius inversion, including nonlinear sparse binomials and trinomials. When the lift exponent is one, every nonzero cycle of the linearized permutation is replicated by a known common factor.

More precisely, use the notation in the next section. For each positive integer \(m\), put
\[
 g_m=\gcd(r^m-1,S),\qquad
 d_{m,\lambda}=\dim_{\mathbb F_q}\ker(\mathcal L^m-\lambda I)\quad(\lambda\in\mathbb F_q^\times).
\]
The exact fixed-point formula is
\[
 \boxed{\#\operatorname{Fix}(F^m)=1+\frac{g_m}{q-1}
 \sum_{\substack{\lambda\in\mathbb F_q^\times\\\lambda^{S/g_m}=1}}
 \bigl(q^{d_{m,\lambda}}-1\bigr).}
\]
Consequently, the number of cycles of exact length \(\ell\ge 1\) is
\[
 c_\ell(F)=\frac1\ell\sum_{d\mid\ell}\mu(\ell/d)\,\#\operatorname{Fix}(F^d).
\]
These formulas require no enumeration of the \(q^{ns}\) elements of the extension field.

## Assumptions and scope

Let \(q\) be a prime power, \(n\ge2\), and \(s\ge1\) with \(\gcd(s,M)=1\), where
\[
 L=\mathbb F_{q^n},\quad K=\mathbb F_{q^{ns}},\quad
 M=\frac{q^n-1}{q-1},\quad N=q^{ns}-1,\quad S=N/M.
\]
Choose \(h\in\mathbb Z\) satisfying \(hs\equiv1\pmod M\), and let \(T\equiv hS\pmod N\). Put \(e_i=(q^i-1)/(q-1)\) for \(0\le i<n\). Let
\[
 \mathcal L(Z)=\sum_{i=0}^{n-1}a_i Z^{q^i},\qquad a_i\in L,
\]
be any \(q\)-linearized permutation of \(L\). Let \(r\ge1\) satisfy \(\gcd(r,N)=1\) and \(r\equiv1\pmod{q^n-1}\). Define the sparse lift on \(K\) by
\[
 F(X)=X^r\sum_{i=0}^{n-1}a_iX^{e_iT},\qquad F(0)=0.
\]
Here negative representatives for \(T\) are replaced by their nonnegative residues modulo \(N\); the formula specifies the induced map on \(K\). This is the family of the higher unit-torus lifting construction of Li (2026). The present claim is its periodic-point classification, not its known permutation or inverse construction.

## Proof

**1. Two multiplicative factors.** Since \(S=(q-1)\sum_{j=0}^{s-1}q^{nj}\), we have \(S\equiv s(q-1)\pmod{q^n-1}\). Thus \(T=hS\equiv q-1\pmod{q^n-1}\). Let
\[
 H=\{u\in K^\times:u^T=1\}.
\]
Because \(N=MS\) and \(\gcd(h,M)=1\), the group \(H\) is cyclic of order \(\gcd(T,N)=S\). On \(L^\times\), the equality \(z^T=z^{q-1}\) holds. Consequently
\[
 H\cap L^\times=\mathbb F_q^\times.
\]
The product of subgroups has cardinality \(S(q^n-1)/(q-1)=N\), hence \(K^\times=HL^\times\). Every nonzero \(x\in K\) has exactly \(q-1\) representations \(x=uz\), with \(u\in H\), \(z\in L^\times\).

**2. Exact dynamics on the factorization.** For \(u\in H\), \(z\in L^\times\), and every \(i\), the definition gives \((uz)^{e_iT}=z^{e_iT}=z^{q^i-1}\). The condition on \(r\) gives \(z^r=z\), and hence
\[
 F(uz)=u^r\sum_{i=0}^{n-1}a_i z^{q^i}=u^r\mathcal L(z).
\]
Since \(u^r\in H\), \(\mathcal L(z)\in L^\times\), and \(\mathcal L\) is a permutation, induction yields for every \(m\ge1\):
\[
 F^m(uz)=u^{r^m}\mathcal L^m(z).
\]
The factorization is well-defined despite its \(q-1\)-fold redundancy because \(r\equiv1\pmod{q-1}\) and \(\mathcal L\) is \(\mathbb F_q\)-linear.

**3. Fixed-point count.** The equality \(F^m(uz)=uz\) is equivalent to
\[
 u^{r^m-1}=z/\mathcal L^m(z)=\lambda^{-1}\in H\cap L^\times=\mathbb F_q^\times,
\]
where necessarily \(\mathcal L^m(z)=\lambda z\). For each \(\lambda\in\mathbb F_q^\times\), the nonzero solutions \(z\in L\) comprise exactly \(q^{d_{m,\lambda}}-1\) vectors. Since \(H\) is cyclic of order \(S\), the power equation in \(u\) has \(g_m\) solutions exactly when \(\lambda^{S/g_m}=1\), and no solutions otherwise. Dividing the resulting count of pairs \((u,z)\) by their exact representation multiplicity \(q-1\), and including \(x=0\), proves the displayed fixed-point formula.

**4. Complete cycles.** In any finite permutation, \(\#\operatorname{Fix}(F^m)=\sum_{\ell\mid m}\ell c_\ell(F)\); the stated Möbius inversion is exact and uniquely determines every cycle multiplicity. In particular, zero is always one fixed point.

**5. Replication and parity for \(r=1\).** Put \(t=N/(q^n-1)=S/(q-1)\). In this case \(F(uz)=u\mathcal L(z)\), so the \(t\) distinct cosets \(uL^\times\) of \(L^\times\) in \(K^\times\) are invariant, each with dynamics conjugate to \(\mathcal L\) restricted to \(L^\times\). Therefore
\[
 c_1(F)=1+t(c_1(\mathcal L)-1),\qquad
 c_\ell(F)=t\,c_\ell(\mathcal L)\quad(\ell>1).
\]
The permutation order and sign consequently satisfy \(\operatorname{ord}(F)=\operatorname{ord}(\mathcal L)\) and \(\operatorname{sgn}(F)=\operatorname{sgn}(\mathcal L)^t\). No parity claim is made for general \(r\) beyond what follows from the cycle formula.

## Verification

The self-contained Python script `cycle_lift_verify.py` constructs three finite fields using polynomials whose irreducibility is independently tested by exact trial division. It computes all permutation cycles of the lifted polynomial directly, then checks the fixed-point expression for every iterate up to twice the largest cycle length. The seven checks include nontrivial exponents \(r\ne1\), characteristics two and three, and subfield dimensions two and three.

- Over \(\mathbb F_{64}\), \(q=2,n=3,s=2,r=8\), the complete cycle inventory is \(2\) fixed points, \(4\) cycles of length \(2\), \(2\) of length \(3\), and \(8\) of length \(6\).
- Over \(\mathbb F_{256}\), \(q=4,n=2,s=2,r=16\), the cycle inventory is \(1\) fixed point, \(1\) cycle of length \(3\), and \(42\) cycles of length \(6\).
- Over \(\mathbb F_{729}\), \(q=3,n=2,s=3,r=9\), the inventory is \(1\) fixed point, \(1\) cycle of length \(8\), and \(30\) cycles of length \(24\).

The checks return `CERTIFICATE_OK` and `ODD_CERTIFICATE_OK`. Finite tests corroborate the proof; they do not establish its universal quantifiers.

## Relationship to prior work

Li's 2026 construction establishes that these sparse lifts are permutations and supplies sparse inverse formulas and certain involution criteria. It does not give the complete fixed-point profile of every iterate. Bian–Chen–Zheng (2026) determine cycles and parity of the *linearized* permutations, not the lifted generally nonlinear maps. Bors–Wang (2021), especially Section 6.2, provide a general wreath-product method for computing cycle types of generalized cyclotomic permutations. Their framework applies broadly, and the present result is a special arithmetic refinement: it produces a direct all-iterate fixed-point formula using scalar eigenspace dimensions and one cyclic greatest common divisor for this newly specified lift family. Accordingly, no assertion is made that cycle computations for general cyclotomic maps were previously unknown.

## Limitations

The formula is restricted to the stated lifting family, including the congruence condition on \(r\); it does not classify arbitrary sparse permutation polynomials. Efficient computation of the scalar eigenspace dimensions may require linear-algebra work on the base field, and full cycle inventories may require evaluations at divisors of the permutation order. This is a proved, self-reviewed mathematical statement, not an independently audited or publication-certified result. A possible implicit specialization of older general cyclotomic cycle algorithms cannot be entirely excluded.

## References

1. Yi Li, *Sparse Lifts of q-Linearized Permutation Polynomials with Explicit Inverses*, arXiv:2610.16619v1 (first posted 2026-10-12), Sections 2–5. https://arxiv.org/abs/2610.16619
2. Huajun Bian, Shaoshi Chen, Dabin Zheng, *Cycle structures and parities of linearized permutation polynomials*, arXiv:2610.11574v1 (2026), full text. https://arxiv.org/abs/2610.11574
3. Alexander Bors and Qiang Wang, *Generalized cyclotomic mappings: Switching between polynomial, cyclotomic, and wreath product form*, arXiv:2103.00664v1 (2021), especially Sections 3 and 6.2. https://arxiv.org/abs/2103.00664
