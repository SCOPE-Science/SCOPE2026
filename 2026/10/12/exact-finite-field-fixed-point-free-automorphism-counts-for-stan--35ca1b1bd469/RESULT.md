# Exact finite-field fixed-point-free automorphism counts for standard filiform Lie algebras
## Finding
Let \(L_n(\mathbb F_q)\), with \(n\ge 4\), be the standard filiform Lie algebra on a basis \(e_1,\ldots,e_n\) with
\[
[e_1,e_i]=e_{i+1}\qquad(2\le i\le n-1),
\]
and every other bracket between basis vectors equal to zero. The automorphism group has exact order
\[
|\operatorname{Aut}(L_n(\mathbb F_q))|=q^{2n-3}(q-1)^2.
\]
More sharply, the number of fixed-point-free automorphisms is
\[
N_{q,n}=q^{2n-3}\sum_{\substack{d\mid(q-1)\\d>1}}\varphi(d)\bigl(q-1-\min(d,n-1)\bigr).
\]
Consequently, \(L_n(\mathbb F_q)\) admits a fixed-point-free automorphism if and only if either \(q>n\), or \(q\le n\) and \(q-1\) is composite. For \(n=4\),
\[
N_{q,4}=
\begin{cases}
q^5(q-2)(q-4),&q\text{ even},\\
q^5(q-3)^2,&q\text{ odd}.
\end{cases}
\]
Thus the four-dimensional standard filiform algebra has no fixed-point-free automorphism exactly over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_4\).

## Assumptions and scope
The field is an arbitrary finite field \(\mathbb F_q\); no restriction on characteristic is used. The dimension satisfies \(n\ge4\). “Fixed-point-free” means that \(\phi(x)=x\) implies \(x=0\), equivalently \(\det(\phi-I)\ne0\).

The recent complex-field source proves that the standard filiform algebra admits fixed-point-free automorphisms and records diagonal semisimple automorphisms with eigenvalues of the form \(s,t,st,s^2t,\ldots\). The present statement is a finite-field enumeration: it determines the full number of automorphisms, the exact fixed-point-free fiber, and the field-size/dimension existence boundary.

## Proof
Write
\[
\phi(e_1)=a e_1+u_2e_2+\cdots+u_ne_n,\qquad
\phi(e_2)=c e_1+b e_2+v_3e_3+\cdots+v_ne_n.
\]
Because \(\phi(e_3)=[\phi(e_1),\phi(e_2)]\), its coefficient of \(e_3\) is \(ab-u_2c\). Invertibility forces this coefficient to be nonzero. Since \([e_2,e_3]=0\) and \(n\ge4\), the coefficient of \(e_4\) in \([\phi(e_2),\phi(e_3)]\) is \(c(ab-u_2c)\); hence \(c=0\). Therefore \(a,b\ne0\).

Now \(\phi(e_2)\) has no \(e_1\)-component, and all brackets among \(e_2,\ldots,e_n\) vanish. Recursively,
\[
\phi(e_{j+1})=[\phi(e_1),\phi(e_j)]\qquad(2\le j\le n-1),
\]
so the matrix of \(\phi\) is lower triangular with diagonal
\[
a,\ b,\ ab,\ a^2b,\ldots,a^{n-2}b.
\]
Conversely, arbitrary choices of \(a,b\in\mathbb F_q^\times\), arbitrary \(u_2,\ldots,u_n\), and arbitrary \(v_3,\ldots,v_n\) produce an automorphism via the same recursion. There are \((n-1)+(n-2)=2n-3\) free additive parameters, proving
\[
|\operatorname{Aut}(L_n(\mathbb F_q))|=q^{2n-3}(q-1)^2.
\]

Because the matrix is triangular, \(\phi\) is fixed-point-free exactly when
\[
a\ne1,\qquad a^jb\ne1\quad(0\le j\le n-2).
\]
Fix \(a\ne1\) of multiplicative order \(d\mid(q-1)\). The forbidden values of \(b\) are
\[
1,a^{-1},\ldots,a^{-(n-2)},
\]
whose number is \(\min(d,n-1)\). Hence this \(a\) permits exactly \(q-1-\min(d,n-1)\) values of \(b\). Since the cyclic group \(\mathbb F_q^\times\) has \(\varphi(d)\) elements of order \(d\), summing over \(d>1\) gives the formula for \(N_{q,n}\).

Every summand is nonnegative. If \(q>n\), then \(n-1<q-1\), so at least one summand is positive. If \(q\le n\), then \(n-1\ge q-1\), and a summand is positive exactly when there is a divisor \(d\) with \(1<d<q-1\), i.e. exactly when \(q-1\) is composite. For \(n=4\), the only collision among \(1,a^{-1},a^{-2}\) with \(a\ne1\) occurs at \(a=-1\) in odd characteristic, giving the displayed parity formulas.

## Verification
The included `verify.py` independently checks the divisor-sum formula against direct scalar-pair enumeration for prime fields \(\mathbb F_p\) with \(p\in\{2,3,5,7,11\}\) and dimensions \(n\in\{4,5,6,8\}\). It also exhausts all \(2^{16}\) linear maps on \(L_4(\mathbb F_2)\), recovers exactly \(32\) automorphisms, and confirms that none is fixed-point-free. The finite-field theorem itself is symbolic and does not depend on these finite checks.

Representative computed values include \(N_{5,4}=12500\), \(N_{7,4}=268912\), and \(N_{8,8}=0\). The last value illustrates the dimension-sensitive obstruction when \(q-1\) is prime and \(n\ge q\).

## Relationship to prior work
Burde and Dekimpe define fixed-point-free automorphisms, classify the complex Lie algebras of dimension at most four admitting them, and show that the complex algebra \(\mathfrak n_4\) with \([e_1,e_2]=e_3\), \([e_1,e_3]=e_4\) admits fixed-point-free automorphisms of every finite order at least four. Their proof records semisimple automorphisms with diagonal \(s,t,st,s^2t\). They also define the standard graded filiform family \(L_n\) by \([e_1,e_i]=e_{i+1}\).

Those statements concern existence over \(\mathbb C\) and do not enumerate the full finite-field automorphism group, count the fixed-point-free locus, or give the arithmetic existence criterion above. Targeted searches for “standard filiform Lie algebra fixed-point-free automorphism finite field exact count”, “\(L_4(q)\) filiform Lie algebra automorphism fixed point free”, and equivalent automorphism-count formulations found no prior statement of the divisor-sum formula or the field-size/dimension boundary. A published exact count for the three-dimensional Heisenberg algebra is not stronger: in dimension three the two generators may mix by an arbitrary \(\operatorname{GL}_2\)-matrix, whereas for \(n\ge4\) the relation \([e_2,e_3]=0\) forces the first-coordinate coefficient of \(\phi(e_2)\) to vanish, producing a different automorphism group and count.

## Limitations
The theorem treats the standard filiform family \(L_n\), not arbitrary filiform Lie algebras. It counts linear automorphisms over finite fields and does not classify their conjugacy classes or orders. The literature search cannot exclude an equivalent formula hidden under a different notation for maximal-class Lie algebras; this remains the principal originality risk.

## References
1. D. Burde and K. Dekimpe, “Fixed-point-free automorphisms of solvable Lie algebras,” arXiv:2604.27916v1, first submitted 2026-04-30. Primary MSC 17B30, 17B08.
