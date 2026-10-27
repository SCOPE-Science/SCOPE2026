# Three nodal Hasse divisors and exact \(5\)-rank strata in a genus-three Howe family

## Finding
Over an algebraically closed field \(k\) of characteristic \(5\), consider the marked smooth hyperelliptic genus-three family
\[
 C_{a,b}:\quad y^2=x^8+a x^6+b x^4+a x^2+1.
\]
The allowable parameter domain is
\[
 U=\{(a,b)\in\mathbb A^2_k:(a^2+b+3)(b+2a+2)(b-2a+2)\ne0\}.
\]
Put \(H_+=a^2+2b+2a\), \(H_-=a^2+2b-2a\), and \(H_0=b^2+2a^2+2\). Then the \(5\)-rank of the Jacobian is \(3-s\), and its \(a\)-number is \(s\), where \(s\) is the number of zero elements among \(H_+,H_-,H_0\). The three reduced Hasse divisors on \(U\) are smooth and pairwise transverse, meeting exactly at
\[
 (a,b)=(0,0),\quad(2,0),\quad(-2,0),
\]
with no triple intersection. Hence the possible ranks are precisely \(1,2,3\); rank \(0\) never occurs on \(U\).

For every \(n\ge1\), write \(q=5^n\) and \(\delta_n=(1+(-1)^n)/2\). The exact counts of **marked coefficient pairs** in \(U(\mathbb F_q)\) are
\[
 \begin{array}{c|c}
 \text{Jacobian }5\text{-rank}&\#\text{marked pairs}\\\hline
 1&3\\
 2&3q-9-6\delta_n\\
 3&(q-3)^2+6\delta_n.
 \end{array}
\]
In particular \(\#U(\mathbb F_q)=q^2-3q+3\). These are not counts of geometric isomorphism classes. The Newton slopes at rank \(r\) are \(0^r,(1/2)^{2(3-r)},1^r\).

## Assumptions and scope
The characteristic is exactly \(5\). The surface \(U\) parametrizes ordered, normalized coefficient pairs, not distinct isomorphism classes. All geometric statements are over \(\overline{\mathbb F}_5\); point counts hold for every \(\mathbb F_{5^n}\). No assertion is made about singular boundary curves. The \(5\)-rank is the dimension of the \(\mathbb F_5\)-rational geometric \(5\)-torsion, and the \(a\)-number is \(\dim_k\operatorname{Hom}(\alpha_5,J(C))\).

## Proof
**Smoothness.** Put \(t=x^2\) and \(P(t)=t^4+a t^3+b t^2+a t+1\). Since \(P(0)=1\), the eight branch roots in \(x\) are distinct exactly when \(P(t)\) is squarefree. With \(z=t+t^{-1}\), one has the identity
\[
 t^{-2}P(t)=z^2+az+b-2.
\]
The two-to-one map \(t\mapsto t+t^{-1}\) ramifies precisely at \(t=\pm1\), mapping them to \(z=\pm2\). Thus squarefreeness is equivalent to the discriminant \(a^2-4(b-2)\) being nonzero and neither of the two values \(\pm2\) being a root of the quadratic. Reducing modulo \(5\) gives precisely the three displayed nonvanishing factors defining \(U\). A squarefree monic octic gives a smooth genus-three hyperelliptic curve.

**Jacobian invariants.** Write \(f(x)=x^8+a x^6+b x^4+a x^2+1\). The standard differential basis is \(dx/y,x\,dx/y,x^2dx/y\). The Cartier–Manin coefficient matrix, up to entrywise inverse Frobenius, is \(M=(c_{5i-j})_{1\le i,j\le3}\), where \(c_m\) is the coefficient of \(x^m\) in \(f(x)^2\). Direct multiplication gives
\[
 M=\begin{pmatrix}
 B&0&A\\0&D&0\\A&0&B
 \end{pmatrix},\qquad
 A=2a,\quad B=a^2+2b,\quad D=b^2+2a^2+2.
\]
Because the change of basis \((1,0,1),(1,0,-1),(0,1,0)\) is defined over \(\mathbb F_5\), Frobenius semilinearity does not mix its three one-dimensional eigenspaces. Their respective Hasse scalars are \(B+A=H_+\), \(B-A=H_-\), and \(D=H_0\). An eigenspace contributes stable Frobenius rank one exactly when its scalar is nonzero; hence the geometric \(5\)-rank is \(3-s\), not merely the rank of one uniterated Hasse–Witt matrix. The \(a\)-number is \(s\) from the rank of the Cartier operator. In addition the commuting involutions \((x,y)\mapsto(-x,y)\) and \((x,y)\mapsto(1/x,y/x^4)\) yield three elliptic quotients and a degree-a-power-of-two isogeny from their product to \(J(C)\), because their common quotient has genus zero. As \(5\) is odd, the isogeny is prime-to-\(5\), and its ordinary/supersingular elliptic factors give the stated Newton slopes.

**Intersection geometry.** The reduced curves \(H_\pm=0\) are affine parabolas and \(H_0=0\) is a smooth conic (its homogenization is nonsingular in characteristic \(5\)). Pairwise equations give the following geometric intersections, with multiplicities before restricting to \(U\):
\[
 \begin{array}{c|c}
 \text{pair}&\text{intersections}\ \hline
 H_+,H_-&(0,0)\\
 H_+,H_0&(1,1)\ (\text{multiplicity }3),\ (-2,0)\ (\text{multiplicity }1)\\
 H_-,H_0&(-1,1)\ (\text{multiplicity }3),\ (2,0)\ (\text{multiplicity }1).
 \end{array}
\]
Indeed eliminating \(b\) from \(H_\pm=H_0=0\) gives, up to nonzero scalar,
\[
 (a-1)^3(a+2)\quad\text{and}\quad (a+1)^3(a-2),
\]
respectively. The points \((1,1)\) and \((-1,1)\) lie on the excluded discriminant. The three remaining points lie on \(U\); gradients are linearly independent at each, proving transversality. They are disjoint as sets of pairwise intersections, so no triple vanishing occurs. Each \(s=2\) point has rank \(1\), each smooth point on only one divisor rank \(2\), and every other point rank \(3\).

**All-extension parameter counts.** The singular-boundary complement of \(U\) comprises the parabola \(a^2+b+3=0\) and the lines \(b\pm2a+2=0\). Each contains \(q\) rational points; their only pairwise intersections are \((1,1),(-1,1),(0,-2)\), with no triple intersection. Thus \(\#U(\mathbb F_q)=q^2-3q+3\).

Each parabola \(H_\pm=0\) has \(q\) affine \(\mathbb F_q\)-points. Each meets the excluded boundary in its respective point \((\pm1,1)\) and in two points whose \(a\)-coordinates satisfy \(a^2\pm a+1=0\), with discriminant \(2\). The latter two are rational if and only if \(n\) is even. Hence each \(H_\pm\cap U\) has \(q-1-2\delta_n\) rational points. The projective conic \(b^2+2a^2+2c^2=0\) has \(q+1\) rational points; its two possible points at infinity require \(-2=3\) to be a square and exist exactly when \(n\) is even. Its affine part meets the excluded boundary only at \((\pm1,1)\). Thus \(H_0\cap U\) also has \(q-1-2\delta_n\) rational points.

There are exactly three rational pairwise intersections and no triple intersections on \(U\). The count with two zero Hasse factors is therefore \(3\); the count with exactly one is \(3(q-1-2\delta_n)-2\cdot3=3q-9-6\delta_n\). Subtracting both from \(\#U(\mathbb F_q)\) yields the rank-three count \((q-3)^2+6\delta_n\). This proves all claimed formulas.

## Verification
The accompanying standalone standard-library checker reconstructs all \(25\) coefficient specializations of the Cartier–Manin matrix over \(\mathbb F_5\), and exhaustively enumerates every marked smooth coefficient pair over \(\mathbb F_5\), \(\mathbb F_{25}\), and \(\mathbb F_{125}\). It confirms respectively the rank-distribution triples \((3,6,4)\), \((3,60,490)\), and \((3,366,14884)\), in the order ranks \(1,2,3\). The proof above, rather than these finite tests, establishes the formulas for all \(n\) and geometric transversality.

Run from a package checkout with `python3 verify_howe5.py`; no network or nonstandard packages are required.

## Relationship to prior work
Gutierrez–Sevilla–Shaska (2012) classify genus-three hyperelliptic extra-involution families, including the symmetric octic family. Shaska–Thompson (2013) parametrize the relevant two-dimensional bielliptic locus over characteristic zero. Ohashi (2021) studies hyperelliptic Howe curves in positive characteristic and their three elliptic quotients; the cited theorem concerns maximality or minimality *conditional on superspeciality*. None of those inspected arguments supplies the full characteristic-five \(5\)-rank stratification, exclusion of rank zero, exact three rank-one points, or all-extension marked counts above. Generic Hasse–Witt coefficient methods are classical; the value here lies in the complete clean stratification and its arithmetic census, not in claiming a new Cartier algorithm.

## Limitations
The result concerns normalized marked coefficient pairs, not geometric moduli-point counts; different pairs can yield isomorphic curves. Source inspections are not an exhaustive historical novelty certification. The three rank-one points are not asserted to be geometrically nonisomorphic. The theorem does not classify the Jacobians up to isomorphism and does not extend to characteristic two or singular parameter boundaries. Numerical finite-field tests alone do not certify universal claims.

## References
- J. Gutierrez, D. Sevilla, T. Shaska, *Hyperelliptic curves of genus 3 with prescribed automorphism group*, arXiv:1209.2938v1, public 2012-09-13, especially Table 1 and Sections 2–3.
- T. Shaska, F. Thompson, *Bielliptic curves of genus 3 in the hyperelliptic moduli*, arXiv:1305.4501, 2013, Section 5.2.1.
- R. Ohashi, *On the maximality of hyperelliptic Howe curves of genus 3*, arXiv:2112.11152v1, 2021, Sections 3–4.
- E. Kani, M. Rosen, *Idempotent relations and factors of Jacobians*, Math. Ann. 284 (1989), 307–327.
