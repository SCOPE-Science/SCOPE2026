# Exact factorization-length multiplicities in the symmetric generalized-star triples

## Finding

For integers \(a\ge4\) and \(n\ge2\), define the three consecutive generalized-star numbers
\[
 A=a n(n-1)+1,\qquad B=a n(n+1)+1,\qquad C=a(n+1)(n+2)+1,
\]
and \(s=2n+1\). Suppose \(s\mid 3a+4\). The following gives **every** factorization length and **its exact multiplicity** for any integer \(M\ge0\) in the numerical semigroup \(S=\langle A,B,C\rangle\), without an eventuality threshold.

Let \(u=A/s\), \(v=C/s=u+2a\). Let \(r\) be the unique integer in \(\{0,\dots,s-1\}\) satisfying \(rB\equiv M\pmod s\), and set \(N=(M-rB)/s\). Define \(x_0\in\{0,\dots,v-1\}\) by \(ux_0\equiv N\pmod v\) and \(z_0=(N-ux_0)/v\).

If \(z_0<0\), then \(M\notin S\). Otherwise put \(J=\lfloor z_0/u\rfloor\). For \(0\le j\le J\), set
\[
 x_j=x_0+vj,\quad z_j=z_0-uj,\quad
 \ell_j=r+x_0+z_0+2aj.
\]
The set of all factorization lengths of \(M\) is precisely \(\{\ell_0,\dots,\ell_J\}\), and the number of ordered generator-count triples \((x,y,z)\in\mathbb Z_{\ge0}^3\) with \(Ax+By+Cz=M\) and \(x+y+z=\ell_j\) is exactly
\[
 \boxed{h_j=1+\min\left\{\left\lfloor\frac{x_j}{n+1}\right\rfloor,
 \left\lfloor\frac{z_j}{n}\right\rfloor\right\}.}
\]
In particular, every non-singleton length set is a **full** arithmetic progression with difference \(2a\), and the semigroup delta set is exactly \(\Delta(S)=\{2a\}\).

## Assumptions and scope

The generators are three *distinct* positive integers for \(a\ge4\), \(n\ge2\), and are primitive as a triple. Factorizations are ordered by generator type rather than the order of individual coins. \(\Delta(S)\) is the union, over \(M\in S\), of gaps between consecutive distinct lengths. The divisibility assumption defines a nonempty, infinite-in-parameter subfamily: for example \((a,n)=(7,2),(5,9),(6,5)\). No formula for the complementary parameter cases is asserted.

## Proof

**Arithmetic reduction.** Since \(s\) is odd,
\[
 4A=a(s-1)(s-3)+4\equiv3a+4\pmod s,
\]
so \(s\mid A\); similarly \(s\mid C\). The gap \(C-A=2as\) gives \(v-u=2a\). Moreover \(A\) is odd and coprime to \(a\), hence \(\gcd(A,2a)=1\), so \(\gcd(u,v)=\gcd(u,2a)=1\). Also \(B\equiv-a\pmod s\). Every common divisor of \(a\) and \(s\) divides both \(3a+4\) and \(4\), and hence is 1 (since \(s\) is odd). Thus \(\gcd(B,s)=1\). Therefore the modular inverses used in the statement exist.

**The length-preserving trade.** Direct expansion proves
\[
 (n+1)A+nC=sB. \tag{1}
\]
Each factorization \((x,y,z)\) has \(y=r+st\) with \(t\ge0\), because \(A,C\) are divisible by \(s\). Using (1), replacing its \(st\) occurrences of \(B\) yields the unique associated reduced factorization
\[
 (x+(n+1)t,\ r,\ z+nt)=(x',r,z'). \tag{2}
\]
The replacement preserves factorization length because \(n+1+n=s\). Conversely, every reduced factorization \((x',r,z')\) yields exactly one original factorization for every integer
\[
 0\le t\le\min\!\left(\left\lfloor\frac{x'}{n+1}\right\rfloor,
 \left\lfloor\frac{z'}n\right\rfloor\right),
\]
namely \((x'-(n+1)t,r+st,z'-nt)\). These inverse constructions are exhaustive and injective for each \(t\).

**Enumeration of reduced factorizations.** The equation for \((x',r,z')\) is \(ux'+vz'=N\), with nonnegative \(x',z'\). As \(\gcd(u,v)=1\), the unique solution with \(0\le x'<v\) has first coordinate \(x_0\) and second coordinate \(z_0\). Any integer solution is
\[
 (x',z')=(x_0+vj,z_0-uj),\qquad j\in\mathbb Z.
\]
Since \(0\le x_0<v\), nonnegativity of the first coordinate forces \(j\ge0\). Nonnegativity of the second then gives \(j\le J\), precisely when \(z_0\ge0\). This proves the membership criterion. Each reduced factorization has length
\[
 r+x_j+z_j=r+x_0+z_0+j(v-u)=\ell_j.
\]
Because \(v-u=2a>0\), distinct \(j\) give distinct lengths. Applying the bijection (2) gives the exact multiplicity \(h_j\), with no overlooked factorizations.

**Delta-set equality.** Every gap between distinct lengths is \(2a\), hence \(\Delta(S)\subseteq\{2a\}\). The element \(M=svu\) has two factorizations \((v,0,0)\) and \((0,0,u)\), with distinct lengths differing by \(v-u=2a\); the complete progression property therefore gives \(2a\in\Delta(S)\).

## Verification

The accompanying standalone `verify.py` independently enumerates three-generator factorizations for multiple admissible parameter choices, compares **length multiplicities** (not only length support) to the formula, checks the arithmetic identities, and tests membership including gaps. All finite checks supplement the full proof and do not substitute for it. Execute `python3 verify.py` with Python 3 standard library.

## Relationship to prior work

Yin, Mu and Komatsu studied generalized-star-number triples and their \(p\)-Frobenius invariants (2024); the present invariant is the complete length-multiplicity profile, not the Frobenius number or genus. Komatsu and collaborators subsequently studied three consecutive star numbers at the classical star coefficient (2025). General work by Garcia, O'Neill and Yih (2019) analyzes factorization length *distributions*, chiefly asymptotically; their length-preserving trade framework is consistent with relation (1), but does not provide the above closed formula for this exact parameter subfamily in the material inspected. General structure theorems say eventual length sets are almost arithmetic and do not establish the exact no-exception formula for every \(M\) here. The identity (1) and two-coin reduction are elementary, and broader unstated formulas may subsume the claim; see limitations.

## Limitations

The result covers only \(s\mid3a+4\); other parameters remain outside scope. The formula is an exact specialization of a gluing-style two-coin reduction, so its novelty lies in the explicit all-element classification and multiplicities, not a new general theory of numerical semigroup factorizations. Literature coverage is not exhaustive; an implicit equivalent in prior three-generator factorization literature remains possible. No independent audit has been performed.

## References

1. R. Yin, J. Mu, T. Komatsu, *The p-Frobenius Number for the Triple of the Generalized Star Numbers* (2024), preprint DOI:10.20944/preprints202407.2280.v1.
2. T. Komatsu et al., *On p-Frobenius Numbers for the Numerical Semigroups Generated by Three Consecutive Star Numbers* (2025), *Integers*, `https://math.colgate.edu/~integers/z106/z106.pdf`.
3. S. R. Garcia, C. O'Neill, S. Yih, *Factorization length distribution for affine semigroups I: Numerical semigroups with three generators*, *European Journal of Combinatorics* 78 (2019), 190–204, DOI:10.1016/j.ejc.2019.01.009.
4. C. Moskowitz, C. O'Neill, *The structure theorem for sets of length for numerical semigroups* (2023), arXiv:2311.05786.
