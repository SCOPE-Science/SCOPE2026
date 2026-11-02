# Two-factor normal forms for characteristic-two anticommutator operator monoids

## Finding
Let \(k\) be any field of characteristic two, let \(V=M_2(k)\), and for \(A\in V\) let \(D_A\in\operatorname{End}_k(V)\) be the unnormalized anticommutator operator \(D_A(X)=AX+XA\). Set \(\mathcal M(k)=\langle\operatorname{id}_V,D_A:A\in V\rangle\). Every nonidentity member of \(\mathcal M(k)\) is a product of **at most two** operators \(D_A\). In an explicit basis, the two-factor operators admit a complete unique-parameter classification given below.

For every finite field \(k=\mathbb F_q\) of even order, the monoid has
\[
 |\mathcal M(\mathbb F_q)|=(q-1)q^4+2q^3+q^2-q.
\]
Its exact linear-rank distribution on the four-dimensional vector space \(V\) is
\[
\begin{array}{c|ccccc}
\operatorname{rank}&0&1&2&3&4\\\hline
\text{number}&1&2q^3-q-1&(q-1)q^4+q^2-1&0&1.
\end{array}
\]
The nonunital generated semigroup has one fewer element. In particular, for \(q=2\) the unital monoid has \(34\) elements, with ranks \(0,1,2,4\) occurring \(1,13,19,1\) times respectively. This is the characteristic-two **unnormalized** anticommutator construction; the usual half-scaled Jordan product is undefined in this characteristic.

## Assumptions and scope
No algebraic closure, perfectness, or finiteness hypothesis is needed for the normal forms. Finite cardinality is assumed only for the numerical formula. We use the ordinary composition of \(k\)-linear maps, include the identity as an empty product, and count distinct linear transformations, not distinct words or coefficient matrices. On characteristic-two matrix algebras the map \(D_A\) equals the inner Lie derivation \([A,-]\); scalar matrices give the zero operator. All ranks are vector-space dimensions over \(k\).

## Proof
Write \(H=E_{11}\), \(C=I_2\), \(e=E_{12}\), and \(f=E_{21}\), a basis of \(V\). Identify \(X=hH+tC+z_1e+z_2f\) with \((h,t,z)\), where \(z=(z_1,z_2)\in k^2\). For \(v=(v_1,v_2)\), set \(\omega(v,z)=v_1z_2+v_2z_1\). This is a nondegenerate alternating bilinear form even in characteristic two. For \(A=aH+bC+v_1e+v_2f\), a direct calculation using \([H,e]=e\), \([H,f]=f\), and \([e,f]=C\) gives
\[
D_A(h,t,z)=(0,\omega(v,z),hv+az)=:T(a,v)(h,t,z).
\]
Thus the generator depends only on the three parameters \((a,v)\), uniquely: the value on \(H\) recovers \(v\), while its action on \(e,f\) recovers \(a\).

For two generators, direct substitution gives
\[
T(a_2,v_2)T(a_1,v_1)(h,t,z)
 =(0,dh+\omega(u,z),hs+rz)=:P(r,s,u,d)(h,t,z),
\]
where \(r=a_2a_1\), \(s=a_2v_1\), \(u=a_1v_2\), and \(d=\omega(v_2,v_1)\). The quadruple \((r,s,u,d)\) uniquely determines the map: its action on \(H,e,f\) recovers the four parameters.

Precisely the following quadruples occur as twofold products:
\[
\begin{cases}
r\ne0,\quad s,u\in k^2,\quad d=\omega(u,s)/r;\\
r=0,\quad s=0\text{ or }u=0,\quad d\in k.
\end{cases}
\]
Necessity follows immediately from the factor parameters. For \(r\ne0\), take \(a_1=1\), \(a_2=r\), \(v_1=s/r\), \(v_2=u\). For \(r=0,u=0,s\ne0\), take \(a_1=0,a_2=1,v_1=s\), and choose \(v_2\) with \(\omega(v_2,s)=d\); nondegeneracy ensures a solution. The case \(r=0,s=0,u\ne0\) follows symmetrically with \(a_2=0,a_1=1,v_2=u\). Finally, if \(r=s=u=0\), take \(a_1=a_2=0\), \(v_1=(1,0)\), and \(v_2=(0,d)\). This proves both necessity and sufficiency.

For any three factors, the output of the first factor has zero \(H\)-coordinate, so a direct substitution yields the *exact word reduction*
\[
 T(a_3,v_3)T(a_2,v_2)T(a_1,v_1)
 =T(a_3a_2,a_2v_3)T(a_1,v_1).
\]
Induction reduces all words of length at least two to length two. The onefold map \(T(a,v)\) has quadruple representation \(P(a,v,v,0)\). It belongs to the twofold class if \(a\ne0\) (the first case) or \(v=0\) (the zero map). If \(a=0\) and \(v\ne0\), its two nonzero vectors \(s=u=v\) violate the second case, so it is a genuinely onefold-only map. The identity is distinct from every nonempty word: every generator kills \(C\), whereas the identity does not. Hence the claimed exhaustive disjoint normal forms hold over every characteristic-two field.

For finite \(k\) with \(|k|=q\), the first twofold case has \((q-1)q^4\) maps. The second consists of the union of the sets \(u=0\) and \(s=0\), each of size \(q^3\), with intersection size \(q\), contributing \(2q^3-q\). The onefold-only maps contribute \(q^2-1\); the identity contributes one. Adding gives the stated monoid order.

For rank: in the first case \(r\ne0\), writing \(y=hs+rz\), the identity \(d=\omega(u,s)/r\) gives output scalar \(\omega(u,y)/r\), so the image is exactly the graph of a linear functional \(k^2\to k\) and has rank two. In the second case \(r=0\), either \(u=0\) or \(s=0\), so every nonzero \(P\) has rank one; \(P(0,0,0,0)\) is the zero map. Every onefold-only \(T(0,v)\) with \(v\ne0\) has rank two, as its scalar and vector output directions are independent. The identity has rank four. These give all rank multiplicities, completing the proof.

## Verification
The accompanying standalone Python program `verify.py` independently constructs \(D_A\) from matrix multiplication in \(M_2(\mathbb F_2)\) and \(M_2(\mathbb F_4)\), enumerates all single and twofold operators, computes their ranks by finite-field row reduction, and confirms closure under right multiplication by every generator. Results:

- \(\mathbb F_2\): \(8\) generators, \(30\) twofold maps, \(34\) monoid maps, rank counts \((1,13,19,0,1)\).
- \(\mathbb F_4\): \(64\) generators, \(892\) twofold maps, \(908\) monoid maps, rank counts \((1,123,783,0,1)\).

Both enumerations returned `VERIFY_OK`. These finite checks corroborate but do not replace the algebraic proof for arbitrary characteristic-two fields.

## Relationship to prior work
Gogić, Kazalicki, and Tomašević proved that for \(\operatorname{char}k\ne2\), the semigroup generated by ordinary normalized Jordan multiplications on \(M_n(k)\) is the entire linear endomorphism semigroup (Theorem 1.1 of arXiv:2604.17664v1). Their Introduction explicitly observes that in characteristic two the unnormalized Jordan symmetrization becomes a commutator, annihilates scalar matrices, and is trace-valued; the full-semigroup theorem therefore fails. That source does **not** give the exact characteristic-two \(2\times2\) monoid order, ranks, or word-length-two normal form obtained here. The distinction is mathematical, not just terminology: the normalized product cannot be defined when \(2=0\). Prior work on local and \(2\)-local inner derivations of Lie rings concerns rigidity of derivations, rather than enumeration of products of inner-derivation operators.

## Limitations
The exact enumeration is only for \(2\times2\) matrices over finite characteristic-two fields. The structural two-factor theorem applies to any characteristic-two field but not to larger matrices. Nothing is asserted for Jordan algebra structures defined through quadratic operators in characteristic two, which are different objects. A historically equivalent result may be hidden under literature about adjoint representations or transformation monoids; the originality comparison is not an absolute priority certificate. The review is not an independent mathematical audit.

## References
1. I. Gogić, M. Kazalicki, M. Tomašević, *The Jordan multiplication semigroup of matrix algebras is the full endomorphism semigroup*, arXiv:2604.17664v1, first posted 2026-04-19, especially §1, Theorem 1.1, and the characteristic-two remark. https://arxiv.org/html/2604.17664v1
2. Sh. Ayupov, F. Arzikulov, S. Umrzaqov, *Local and 2-local derivations on Lie matrix rings over commutative involutive rings*, arXiv:2204.03234v1 (scope comparison only). https://arxiv.org/abs/2204.03234
