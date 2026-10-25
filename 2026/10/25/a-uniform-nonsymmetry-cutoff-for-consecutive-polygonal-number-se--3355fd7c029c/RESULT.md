# A uniform nonsymmetry cutoff for consecutive polygonal-number semigroups

## Finding
For integers \(m\ge3\) and \(n\ge2\), put
\[
P_m(j)=\frac{j((m-2)j-m+4)}2,\qquad S_{m,n}=\langle P_m(n),P_m(n+1),P_m(n+2)\rangle.
\]
Every triangular case \(S_{3,n}\) is symmetric, hence complete intersection and cyclotomic. For every \(m\ge4\), the explicit universal implication
\[
\boxed{n>12m(3m-8)\ \Longrightarrow\ S_{m,n}\text{ is nonsymmetric, non-complete-intersection, and noncyclotomic}}
\]
holds and its three displayed generators are minimal. Consequently, for any fixed \(m\ge4\), all symmetric starting indices are in the finite interval \(2\le n\le12m(3m-8)\). This is a uniform bound over arbitrary polygon side count, not an exact classification of the finitely many indices remaining below the bound.

For triangular numbers, writing \(n=2k\) or \(n=2k+1\) with \(k\ge1\), the respective Frobenius numbers are
\[
F(S_{3,2k})=(2k+1)(k^2-k-1)+2k(k+1)(2k+3),
\]
\[
F(S_{3,2k+1})=(2k+3)(k^2+k-1)+(2k+2)(k+1)(2k+1).
\]
Both have genus \(g=(F+1)/2\).

## Assumptions and scope
The additive semigroup \(\langle a,b,c\rangle\) comprises nonnegative integer linear combinations. It is a numerical semigroup when the three generators have gcd one. It is *symmetric* when, for its Frobenius number \(F\), each integer \(z\) has precisely one of \(z,F-z\) in the semigroup, equivalently \(2g=F+1\). We work with ordinary (not centered) polygonal numbers. The inequality on \(n\) is strict.

For a minimal three-generator numerical semigroup the standard three-generator gluing criterion states that symmetry forces a pair \(p,q\) with \(d=\gcd(p,q)>1\) and the remaining generator \(r\) in \(\langle p/d,q/d\rangle\). This necessity follows from the classification in [1, Section 5.1, Example 6] and [2, Section 1.1, Lemma 1]. In embedding dimension at most three, symmetry, complete intersection, and cyclotomicity are equivalent [1, Lemma 7].

## Proof
Set \(t=m-2\), and write
\[
a=P_m(n),\quad b=P_m(n+1),\quad c=P_m(n+2),\quad u=b-a=tn+1,\quad e=c-a=2tn+t+2.
\]
Because \(e=2u+t\) and \(\gcd(u,t)=1\), we have \(\gcd(u,e)=1\) and \(\gcd(a,b,c)=1\) (any common divisor divides both differences). Thus each object is a numerical semigroup.

Suppose now \(t\ge2\) and put \(M=(t+2)(3t-2)=m(3m-8)\). Direct polynomial identities yield
\[
2ta-(t-1)=u(tn-t+1),\qquad 8ta-M=e(2tn-3t+2).
\]
Since \(b=a+u\), the first identity implies \(\gcd(a,b)\mid(t-1)\). The same identity after replacing \(n\) by \(n+1\) gives \(\gcd(b,c)\mid(t-1)\). The second gives \(\gcd(a,c)\mid M\). Hence every pair gcd \(d\) is at most \(M\), uniformly in \(n\).

For \(n\ge2\), \(t\ge2\), elementary inequalities give
\[
a=\frac{n(t(n-1)+2)}2\ge\frac{tn^2}{4},\qquad e=2tn+t+2\le3tn.
\]
Consequently, if \(n>12M\), then \(e/a\le12/n<1/M\), and \(e> M\). In particular \(c/a<1+1/M<2\). Since \(a<b<c<2a\), all three generators are minimal.

Assume toward a contradiction that such a semigroup is symmetric. The three-generator gluing criterion provides a pair \(p,q\), pair gcd \(d\in[2,M]\), remaining generator \(r\), and nonnegative integers \(x,y\) such that
\[
dr=xp+yq.
\]
Put \(s=x+y\). All generators lie in \([a,c]\), so
\[
\frac{da}{c}\le s\le\frac{dc}{a}.
\]
The strict estimate \(c/a<1+1/M\), together with \(d\le M\), forces \(d-1<s<d+1\). Since \(s\) is an integer, \(s=d\). Therefore \(r\) is a weighted average of the other two generators. The smallest and largest generators cannot be such an average, so \(r=b\), \(p=a\), \(q=c\). Subtracting \(da\) yields
\[
d(b-a)=y(c-a),\quad\text{i.e.}\quad du=ye.
\]
But \(\gcd(u,e)=1\), so \(e\mid d\), contradicting \(e>M\ge d\). This proves nonsymmetry; [1, Lemma 7] gives the two stronger exclusions.

For the triangular boundary \(t=1\), write \(n=2k\) with \(k\ge1\). Then the generators are \(k(2k+1)\), \((k+1)(2k+1)\), \((k+1)(2k+3)\). The first pair has gcd \(d=2k+1\), the third belongs to \(\langle k,k+1\rangle\), and \(\gcd(d,(k+1)(2k+3))=1\). Thus this is a two-generator gluing and is symmetric. For \(n=2k+1\), the generators are \((k+1)(2k+1)\), \((k+1)(2k+3)\), \((k+2)(2k+3)\). The last pair has gcd \(2k+3\), and the first belongs to \(\langle k+1,k+2\rangle\), again with coprimality. The standard gluing Frobenius identity \(F(d\langle v,w\rangle+r\mathbb N_0)=d(vw-v-w)+(d-1)r\) gives the displayed formulas and symmetry gives genus \((F+1)/2\).

## Verification
The standalone file `verify.py` evaluates polygonal formulas, difference identities, pair-gcd bounds, and strict cutoff inequalities for fifteen polygon side counts and 930 sampled pairs. A separate Apéry-set shortest-path calculation checks triangular Frobenius formulas and symmetry for 53 consecutive starting indices, and independently checks 160 nontriangular instances. The verification executable prints `VERIFY_OK`. These tests are corroboration; the infinite, two-parameter assertion rests on the exact proof above.

## Relationship to prior work
The 2002 OEIS sequence A069758 tabulates Frobenius numbers for triples of successive hexagonal numbers [3], a fixed six-sided slice. Fel [2] classifies symmetry and Frobenius behavior for the powers \((n-1)^k,n^k,(n+1)^k\) with exponents two through four, including the square-number slice but not the full polygonal side-number parameter. Ciolan, García-Sánchez, and Moree [1] provide the general three-generator gluing and cyclotomic equivalence underpinning the proof. Known fixed pentagonal and hexagonal symmetry classifications also concern particular side counts; they do not furnish the displayed *uniform* quadratic bound for every side count. The contribution is the two-parameter finite-exception theorem and its triangular/nontriangular contrast, not a claim that any of these fixed-slice classifications is new.

## Limitations
The cutoff \(12m(3m-8)\) is an explicit sufficient bound; optimality is not asserted. No classification is supplied inside this cutoff for general \(m\). Published general gluing criteria may make portions of the proof routine, and an unlocated broader theorem for quadratic-polynomial triples could imply the uniform cutoff; an independent literature priority assessment remains necessary. The finding has undergone only a self-review, not an independent audit.

## References
[1] E.-A. Ciolan, P. A. García-Sánchez, P. Moree, *Cyclotomic Numerical Semigroups*, arXiv:1409.5614, initial public preprint September 2014, especially Sections 3 and 5.

[2] L. G. Fel, *Numerical semigroups generated by squares, cubes and quartics of three consecutive integers*, arXiv:1608.08693, August 31, 2016, especially Section 1.

[3] V. A. Sapko, OEIS A069758, *Frobenius number of the numerical semigroup generated by three consecutive hexagonal numbers*, entered April 8, 2002.

[4] T. Komatsu, *Numerical semigroups generated by three consecutive triangular numbers*, arXiv:2206.13054, June 2022 (related triangular setting).
