# A modular central extension changes the commuting-pair census of truncated polynomial derivations

## Finding
Let \(p\ge3\) be an odd prime, and \(q=p^a\) with \(a\ge1\). Put \(k=\mathbb F_q\), \(R=k[x]/(x^{p+2})\), and \(L=\operatorname{Der}_k(R)\). Every \(D\in L\) is represented uniquely by \(f(x)\partial_x\), where \(f\in xR\). For \(D\ne0\), let \(j=\operatorname{ord}_x(f)\), so \(1\le j\le p+1\). The following is the complete distribution of element-centralizer dimensions:

\[
\dim_k C_L(D)=
\begin{cases}
2,&j=1,\\
j,&2\le j\le(p+1)/2,\\
j-1,&(p+3)/2\le j\le p,\\
p+1,&j=p+1.
\end{cases}
\]
For \(D=0\), the centralizer dimension is \(p+1\). Exactly \((q-1)q^{p+1-j}\) nonzero elements have order \(j\). Hence the number of ordered commuting pairs is
\[
C(L)=\#\{(D,E)\in L^2:[D,E]=0\}
=q^{p+3}+\frac{p-1}{2}(q^2-1)q^p.
\]
In particular, the commuting probability is
\[
\operatorname{cp}(L)=q^{1-p}+\frac{p-1}{2}(q^{-p}-q^{-p-2}).
\]
The center is \(Z(L)=k x^{p+1}\partial_x\). The natural quotient
\[
0\longrightarrow kx^{p+1}\partial_x\longrightarrow L
\longrightarrow L'=\operatorname{Der}_k(k[x]/(x^{p+1}))\longrightarrow0
\]
is central and **does not split**. The quotient has
\[
C(L')=\frac{p+1}{2}q^{p+1}-\frac{p-1}{2}q^{p-1}.
\]
Thus \(C(L)/(q^2 C(L'))\longrightarrow 2/(p+1)\) as \(q\to\infty\) with \(p\) fixed. A split stabilization by a one-dimensional central summand would instead have \(q^2 C(L')\) commuting pairs.

## Assumptions and scope
All fields are finite of odd prime characteristic \(p\); no assumption that \(q=p\) is made. The first formula concerns the Lie algebra of **all** \(k\)-linear derivations of the unital commutative ring \(R\), with the usual derivation commutator. The definition uses representatives of polynomials of degree at most \(p+1\). The centralizer is the linear subspace of Lie elements commuting with the specified element. Ordered pairs, including pairs with zero entries, are counted. The asymptotic is for fixed prime \(p\) and powers \(q=p^a\) tending to infinity. No scheme-theoretic claims are made.

## Proof
**Derivation presentation and bracket.** A derivation is determined by \(f=D(x)\). Differentiating \(x^{p+2}=0\) gives \((p+2)x^{p+1} f=2x^{p+1}f=0\); since \(p\) is odd, the constant coefficient of \(f\) vanishes. Conversely any \(f\in xR\) defines a derivation \(D=f\partial_x\). Therefore \(L\) has basis \(e_i=x^i\partial_x\) for \(1\le i\le p+1\), and
\[
[e_i,e_j]=\begin{cases}
(j-i)e_{i+j-1},&i+j-1\le p+1,\\
0,&i+j-1>p+1,
\end{cases}
\]
with integer coefficients reduced modulo \(p\).

**Triangular centralizer computation.** Fix nonzero \(f=a_jx^j+\cdots\) with \(a_j\ne0\). Write \(g=\sum_{s=1}^{p+1}b_sx^s\). The centralizer condition \(fg'-gf'=0\pmod{x^{p+2}}\) gives equations, for each \(s\) with \(1\le s\le p-j+2\), whose leading unknown is \((s-j)a_j b_s\), plus terms involving only earlier coefficients \(b_t\), \(t<s\). Thus the equations are triangular. For \(2\le j\le p\), the coefficient \(s-j\) cannot vanish modulo \(p\) for any admissible \(s\ne j\). Consequently every \(b_s\) up to \(p-j+2\) is uniquely constrained, except the free position \(s=j\) when \(2j\le p+2\); at that exceptional position the equation is automatically satisfied because all earlier \(b_s\), \(s<j\), are zero. The \(j-1\) coefficients with \(s>p-j+2\) are free. This gives \(j\) free coefficients for \(2\le j\le(p+1)/2\), and \(j-1\) for \((p+3)/2\le j\le p\).

For \(j=1\), the diagonal term vanishes at \(s=1\) and also at \(s=p+1\), since \(p=0\) in \(k\); every intermediate \(b_s\) is uniquely determined. The final resonant equation imposes no additional condition: \(g=cf+u x^{p+1}\) is a solution for all \(c,u\in k\), because \(x^{p+1}\partial_x\) is central, and every intermediate coefficient is forced to equal the corresponding coefficient of \(cf\). These two free parameters give dimension \(2\). For \(j=p+1\), the bracket with every basis element is zero: with \(e_1\) the coefficient is \(p=0\), and with \(e_s\), \(s\ge2\), the basis index exceeds the truncation bound. This proves the centralizer formula, including all boundary positions.

**Counting.** The elements of exact order \(j\) are specified by a nonzero coefficient of \(x^j\) and arbitrary coefficients in degrees \(j+1,\dots,p+1\); hence they number \((q-1)q^{p+1-j}\). An element of centralizer dimension \(d\) commutes with precisely \(q^d\) elements. Adding the contributions of zero and all orders yields
\[
\begin{aligned}
C(L)&=q^{p+1}+(q-1)q^{p+2}
 +(q-1)\sum_{j=2}^{(p+1)/2}q^{p+1}
 +(q-1)\sum_{j=(p+3)/2}^{p}q^{p}+(q-1)q^{p+1}\\
&=q^{p+3}+\frac{p-1}{2}(q^2-1)q^p.
\end{aligned}
\]
The displayed summation has the first term for \(D=0\), the next for order one, the two middle sums, and the last for the nonzero central line. The simplification is ordinary integer arithmetic, not arithmetic modulo \(p\).

**Center and nonsplitting.** The centralizer description proves that all nonzero central elements have order \(p+1\), so \(Z(L)=ke_{p+1}\). Modulo this line, the brackets agree with the corresponding derivation algebra at truncation exponent \(p+1\). In the quotient the classes of \(e_2\) and \(e_p\) commute because their bracket is supported in degree \(p+1\). But in \(L\) the bracket of any lifts is \([e_2,e_p]=(p-2)e_{p+1}\ne0\); adding central elements to lifts does not change their bracket. Therefore no Lie-algebra section exists, and the central extension is nonsplit.

**Comparison with the quotient.** In \(L'\), the same triangular calculation uses the highest basis index \(p\), giving centralizer dimension \(1\) for order one, dimension \(j\) for \(2\le j\le (p+1)/2\), and dimension \(j-1\) for \((p+3)/2\le j\le p\). There are \((q-1)q^{p-j}\) elements of order \(j\). Summing \(q^{\dim C_{L'}(D)}\) gives
\[C(L')=\frac{p+1}{2}q^{p+1}-\frac{p-1}{2}q^{p-1}.\]
A central direct product with one one-dimensional abelian Lie algebra would multiply the number of commuting ordered pairs by \(q^2\). The quotient comparison and the limit now follow directly.

## Verification
The standalone program `verify.py` constructs the original bracket in the natural derivation basis and uses finite-field Gaussian elimination to calculate \(\ker\operatorname{ad}_D\) without invoking the triangular proof. It exhaustively verifies all derivations for \((p,q)=(3,3),(3,9),(5,5)\), with an explicit irreducible quadratic model of \(\mathbb F_9\), and checks \(600\) reproducible samples for \((p,q)=(7,7)\). It also independently evaluates every ordered pair over \(\mathbb F_3\). The recorded program output is in `verification_output.txt`.

Observed counts of commuting ordered pairs are \(945\) over \(\mathbb F_3\), \(589761\) over \(\mathbb F_9\), and \(540625\) over \(\mathbb F_5\). These agree with the formulas. The larger characteristic-seven check is sampled, not exhaustive; none of the finite computations is used as a proof for all \(p\).

## Relationship to prior work
The characteristic-\(p\) Witt algebra \(\operatorname{Der}(k[x]/(x^p))\) and its orbit and centralizer structure are classical. Mygind, *Orbit Closures in the Witt Algebra and its Dual Space* (2012), studies automorphism orbits of the simple Witt algebra. Yao and Chang, *Nilpotent commuting varieties of the Witt algebra* (2013), give the centralizers of elements of the simple Witt algebra explicitly in Lemma 2.3 and study nilpotent commuting loci. In particular, the order-\(p\) Witt centralizer classification is NOT new here. Premet, *Regular derivations of truncated polynomial rings* (2014), treats multivariate truncated algebras with all truncation exponents equal to \(p\), and regularity in their simple derivation algebras. None of these statements directly gives the non-split central extension at exponent \(p+2\) or its complete rational finite-field census. This is a best-knowledge comparison, not a proof of historical uniqueness.

## Limitations
The result is restricted to odd prime characteristic, one polynomial variable, and the consecutive truncation exponents \(p+1\) and \(p+2\). It does not assert a classification for arbitrary truncation exponents or multivariate rings, nor a geometric decomposition or scheme structure for the commuting variety. Independent mathematical validation and full historical-priority verification have not been performed. A more general theorem about centralizers in truncated Witt-type Lie algebras could subsume the result.

## References
1. M. Mygind, *Orbit Closures in the Witt Algebra and its Dual Space*, first posted 2012-12-04, https://arxiv.org/abs/1212.0740; full text https://arxiv.org/pdf/1212.0740.
2. Y.-F. Yao and H. Chang, *Nilpotent commuting varieties of the Witt algebra*, first posted 2013-01-23, https://arxiv.org/abs/1301.5667; full text https://arxiv.org/pdf/1301.5667, particularly Lemma 2.3.
3. A. Premet, *Regular derivations of truncated polynomial rings*, first posted 2014-05-10, https://arxiv.org/abs/1405.2426; full text https://arxiv.org/pdf/1405.2426.
