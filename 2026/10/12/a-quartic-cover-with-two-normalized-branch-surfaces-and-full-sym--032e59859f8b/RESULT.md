# A quartic cover with two normalized branch surfaces and full symmetric monodromy

## Finding

For the polynomial map of Shi–Xu–Zuo
\[
F:\mathbb A^3_{\mathbb C}\longrightarrow\mathbb A^3_{\mathbb C},\qquad
(x,y,z)\longmapsto(u,v,w)=(y,yz-x^2,z^2+yx^2+y^2z+x^3),
\]
set
\[
B_1=v^2+u^3v-u^2w,\qquad
c=\frac{3u^5}{16}-u^4+\frac{3u^2v}{16}-uv,\qquad
d=\frac{9u^4}{64}-u^3-v,
\]
and
\[
H=(w-c)^2+\frac{3u^2d}{4}(w-c)+(u^3+v)d^2.
\]
Then \(F\) is finite flat of degree \(4\). Its branch divisor is the reduced union of precisely the two distinct irreducible hypersurfaces \(V(B_1)\) and \(V(H)\). Relative to the explicit free-module basis in the proof, its trace-pairing discriminant equals
\[
\boxed{256B_1H}.
\]
Each irreducible branch component has normalization \(\mathbb A^2_{\mathbb C}\). The first component is the complex Whitney umbrella \(v^2=u^2(w-uv)\), and the generic Galois/covering monodromy group of the degree-four map is the full symmetric group \(S_4\).

## Assumptions and scope

Everything is over \(\mathbb C\). The branch divisor is in the target, and the Galois group refers to the Galois closure of the generically separable extension \(\mathbb C(x,y,z)/\mathbb C(u,v,w)\), not to a claim that this degree-four extension is itself Galois. The trace discriminant is the determinant of the trace pairing for the stated integral basis, not the discriminant of a quartic generator after inverting a parameter.

## Proof

**1. Explicit finite free structure.** Put \(t=z+ux/2\). Inside the source coordinate ring, the two defining equations are equivalent to
\[
\begin{aligned}
0&=x^2+\frac{u^2}{2}x-ut+v,\\
0&=t^2+\left(2u^2-\frac{u^3}{4}\right)t
+\left(\frac{u^4}{8}-u^3-v\right)x+\frac{u^2v}{4}-uv-w.
\end{aligned}
\]
Over \(R=\mathbb C[u,v,w]\), their graded leading monomials are \(x^2\) and \(t^2\). Because these are relatively prime, the two monic relations form a Gröbner basis over \(R\). Thus the quotient is free over \(R\), with basis \((1,x,t,xt)\), and rank \(4\). Eliminating the auxiliary generators recovers \(\mathbb C[x,y,z]\), so this quotient is the source ring of \(F\). In particular, the map is finite, flat, surjective, and generically of degree \(4\).

**2. Exact discriminant.** For the displayed basis \(b=(1,x,t,xt)\), set \(T_{ij}=\operatorname{Tr}_{R'/R}(b_ib_j)\), where \(R'=\mathbb C[x,y,z]\). Reduce products using the two monic relations, form their \(4\times4\) multiplication matrices, and take traces. An exact symbolic determinant gives
\[
\det(T)=256\big(v^2+u^3v-u^2w\big)
\left[(w-c)^2+\frac{3u^2d}{4}(w-c)+(u^3+v)d^2\right].
\]
The standalone verifier reconstructs the relations, all multiplication matrices and the determinant from scratch. Equivalently, over \(u\ne0\), \(x\) satisfies the monic quartic
\[
X^4+u^2X^3+2(v+u^3)X^2+B_1=0,
\]
whose ordinary discriminant is \(256u^4B_1H\). The extra \(u^4\) is a chart/basis factor, not an additional branch component.

**3. The two branch components and their normalizations.** Direct differentiation gives
\[
\det(dF)=x(4z+4y^2+3xy).
\]
Thus the ramification divisor in the smooth source has two smooth irreducible components
\[
R_1=\{x=0\},\qquad R_2=\{4z+4y^2+3xy=0\}.
\]
On \(R_1\), writing \(u=y\), the restriction is the finite parametrization
\[
(u,z)\longmapsto(u,uz,z^2+u^2z).
\]
It maps onto \(B_1=0\) and is birational because \(z=v/u\) generically. After changing target coordinate to \(W=w-uv\), its image equation is \(v^2=u^2W\), the Whitney umbrella. Since \(R_1\simeq\mathbb A^2\) is normal, this finite birational map is the normalization.

On \(R_2\), \(z=-u^2-3ux/4\), whence
\[
x^2+\frac{3u^2}{4}x+u^3+v=0,\qquad w=c(u,v)+d(u,v)x.
\]
Eliminating \(x\) yields \(H=0\). The first equation is irreducible over \(\mathbb C(u,v)\), because its discriminant \(9u^4/16-4(u^3+v)\) is linear in \(v\) and is not a square. As \(d(u,v)\not\equiv0\), adjoining \(w=c+dx\) gives exactly the same quadratic extension. Therefore \(H\) is irreducible, and \(R_2\to V(H)\) is generically one-to-one; it is also finite, being the restriction of \(F\). Consequently \(R_2\simeq\mathbb A^2\) is the normalization. The polynomial \(B_1\) is irreducible because it is primitive and linear in \(w\), and \(B_1,H\) are distinct. The discriminant factorization and Jacobian show there are no further branch components.

**4. Generic simple branching and full monodromy.** Both branch factors occur with multiplicity one in the trace discriminant. On the dense chart \(u\ne0\), the quartic above identifies the four sheets; at a general smooth point of either branch component it has precisely one simple double root and two simple other roots. Hence the two local branch meridians each act on the four sheets as a transposition. The source over the branch complement is a nonempty open subset of irreducible \(\mathbb A^3\), so the covering is connected and its monodromy action is transitive. Meridians about the smooth part of the hypersurface normally generate the fundamental group of its complement in simply connected \(\mathbb C^3\). Therefore the monodromy group is generated by transpositions. A transitive subgroup of \(S_4\) generated by transpositions is \(S_4\), proving the claim.

## Verification

Run `python3 verify.py` with Python 3 and SymPy. It reconstructs the free-algebra Gröbner basis, trace-pairing determinant, quartic discriminant, Jacobian factorization, both branch parametrizations, the Whitney-umbrella coordinate change, and sample fold nondegeneracy, returning `VERIFY_OK`. Irreducibility for the general function fields and the global topological monodromy are justified by the preceding proofs, not inferred from finite samples.

## Relationship to prior work

Shi–Xu–Zuo, *Zero loci of Bernstein-Sato ideals are not necessarily linear* (arXiv:2610.04408v1), introduce exactly this map in Theorem 1.2 and prove results about its Bernstein–Sato ideal. Their paper develops algebraic \(\mathscr D\)-module criteria and a weighted blow-up, not the finite-free structure, branch discriminant, normalizations, or covering monodromy calculated here. Wu, *Bernstein–Sato ideals might not be linear* (arXiv:2609.32287v1), gives different polynomial examples. The standard general theorem that transitive simply branched coverings of a simply connected ambient affine space have full symmetric monodromy is used, not claimed as new; the explicit two-component branch geometry is the substantive calculation.

## Limitations

The result makes no claim about the full set of generators of the Bernstein–Sato ideal, a full classification of the singularities of \(V(H)\), positive-characteristic analogues, compactifications, or integral arithmetic Galois groups. The global \(S_4\) statement is a complex geometric covering statement.

## References

1. Q. Shi, Y. Xu and H. Zuo, *Zero loci of Bernstein-Sato ideals are not necessarily linear*, arXiv:2610.04408v1 (first public 2026-10-03), https://arxiv.org/abs/2610.04408.
2. L. Wu, *Bernstein–Sato ideals might not be linear*, arXiv:2609.32287v1 (2026), https://arxiv.org/abs/2609.32287.
3. Standard complex topology: normal generation of the fundamental group of an affine hypersurface complement by meridians, together with the elementary transposition-graph criterion for symmetric monodromy.
