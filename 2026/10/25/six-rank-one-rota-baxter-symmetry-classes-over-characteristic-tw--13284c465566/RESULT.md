# Six rank-one Rota–Baxter symmetry classes over characteristic-two extension fields

## Finding

Let \(k=\mathbb F_q\) be a finite field with \(q=2^e\) for an integer \(e\ge2\), and let \(E=\Lambda_k(k^2)\) be the four-dimensional exterior algebra. A weight-zero Rota–Baxter operator is a \(k\)-linear map \(R:E\to E\) satisfying
\[
R(a)R(b)=R(R(a)b+aR(b))\qquad(a,b\in E).
\]
There are exactly **six** conjugacy classes of nonzero rank-one such operators under the full unital algebra automorphism group of \(E\), uniformly across all characteristic-two extension degrees. Their sizes, in a canonical order, are
\[
q-1,\quad q^2-1,\quad (q-1)(q^2-1),\quad(q^2+q)(q-1),\quad(q^2+q)(q-1),\quad(q^2+q)(q-1)^2.
\]
In particular, the exact number of rank-one operators is
\[
\boxed{N_1(q)=q^4+2q^3-q^2-q-1.}
\]
The six classes are specified by the three intrinsic tests: whether \(\operatorname{im}R\subseteq J^2\), whether \(R(1)=0\), and whether \(R(J)=0\), where \(J\) is the Jacobson radical. Since \(R\ne0\), the last two tests cannot both be zero.

## Assumptions and scope

The base field is a finite extension \(k=\mathbb F_{2^e}\) of \(\mathbb F_2\), with \(e\ge2\); the multiplication is the standard exterior multiplication (not the Clifford or ordinary commutative polynomial multiplication). Relative to the basis \((1,x,y,z=xy)\),
\[
x^2=y^2=z^2=xz=zx=yz=zy=0,\qquad xy=z=-yx.
\]
In this characteristic, \(xy=yx\) because \(-1=1\), though the exterior square relations remain part of the definition. The radical is \(J=kx\oplus ky\oplus kz\), with \(J^2=kz\). All operators are ungraded, unrestricted linear maps; only the operator's vector-space rank is required to equal one. Equivalence means \(R\mapsto gRg^{-1}\) with \(g\in\operatorname{Aut}_{k\text{-alg}}(E)\).

## Proof

**1. Rank-one normal form.** Write a nonzero rank-one map as \(R(a)=\varphi(a)v\), where \(0\ne v\in E\) and \(0\ne\varphi\in E^*\); simultaneous replacement \((v,\varphi)\mapsto(cv,c^{-1}\varphi)\) defines the same map. The Rota–Baxter identity becomes
\[
\varphi(a)\varphi(b)v^2
=\bigl(\varphi(a)\varphi(vb)+\varphi(b)\varphi(av)\bigr)v.
\]
Choose \(a,b\) with \(\varphi(a)\varphi(b)\ne0\). Then \(v^2\in kv\). Write \(v=c1+w\), with \(w\in J\). Every \(w\in J\) squares to zero, including in characteristic two. Since \(v^2=c^2 1+2cw\), the relation \(v^2\in kv\) forces either \(c=0\) or \(w=0\). If \(w=0\), the Rota–Baxter equation would read \(1=2\) after division by a nonzero scalar, impossible in every field. Hence \(v\in J\) and \(v^2=0\).

Set \(\alpha=\varphi\circ L_v\) and \(\beta=\varphi\circ R_v\), with \(L_v(a)=va\) and \(R_v(a)=av\). The identity simplifies to
\[
\varphi(a)\alpha(b)+\beta(a)\varphi(b)=0\qquad(a,b\in E).
\]
As \(\varphi\ne0\), fixing one input with \(\varphi=1\) shows that \(\alpha=c\varphi\) and \(\beta=-c\varphi\) for some \(c\in k\). Because \(L_v^2=R_v^2=0\), applying \(L_v\) twice to \(\varphi\) gives \(0=c^2\varphi\), hence \(c=0\). Thus
\[
\boxed{R(a)=\varphi(a)v\text{ is Rota–Baxter}\iff v\in J\setminus\{0\},\ \varphi\ne0,\ \varphi(vE+Ev)=0.}
\]
In particular, \(R(z)=0\) automatically for every rank-one solution, because \(z\in vE+Ev\) in both cases below.

**2. Counting by projective image.** If \(v\in J^2\setminus\{0\}\), then \(vE+Ev=kz\), so its annihilator in \(E^*\) has dimension three. There is one projective image line and \(q^3-1\) nonzero functionals after fixing its generator. If \(v\in J\setminus J^2\), then \(vE+Ev=kv+kz\) has dimension two. There are
\[
|\mathbb P(J)(k)|-|\mathbb P(J^2)(k)|=(q^2+q+1)-1=q^2+q
\]
such projective image lines, each allowing \(q^2-1\) nonzero functionals. Therefore
\[
N_1(q)=(q^3-1)+(q^2+q)(q^2-1)=q^4+2q^3-q^2-q-1.
\]
This uses projective normalization once per image line, so no scalar multiplicities are omitted or double-counted.

**3. Algebra automorphisms.** Any unital algebra automorphism is uniquely
\[
\begin{aligned}
g(x)&=a x+c y+u z,\\
g(y)&=b x+d y+v z,\\
g(z)&=(ad-bc)z,
\end{aligned}
\quad
\begin{pmatrix}a&b\\c&d\end{pmatrix}\in\operatorname{GL}_2(k),\ \ u,v\in k.
\]
Conversely all these assignments preserve the exterior relations and are invertible. Consequently \(\operatorname{Aut}_{k\text{-alg}}(E)\) has order \(q^2(q^2-1)(q^2-q)\). It preserves \(J^2\), fixes the unit, and preserves \(J\), so the three stated tests are conjugacy invariants.

**4. Exactly six orbits.** For the socle-image case normalize \(v=z\). All allowed functionals satisfy \(\varphi(z)=0\), and therefore are specified by \((\alpha,\ell)\in k\oplus(k^2)^*\setminus\{0\}\), where \(\alpha=\varphi(1)\) and \(\ell=\varphi|_{kx\oplus ky}\). Conjugation transforms this pair by
\[
(\alpha,\ell)\longmapsto\bigl((\det M)\alpha,(\det M)\ell M^{-1}\bigr),\quad M\in\operatorname{GL}_2(k).
\]
The group is transitive separately on \((\alpha\ne0,\ell=0)\), \((\alpha=0,\ell\ne0)\), and \((\alpha\ne0,\ell\ne0)\): for fixed nonzero \(\ell\), its stabilizer realizes every nonzero determinant. Representatives, listed by their images on \((1,x,y,z)\), are
\[
(z,0,0,0),\quad (0,z,0,0),\quad (z,z,0,0).
\]
Their orbit sizes equal the sizes of these respective sets of functionals: \(q-1\), \(q^2-1\), and \((q-1)(q^2-1)\).

For a nonsocle image, transitivity of the algebra automorphism group on projective lines in \(J\setminus J^2\) lets us take \(v=x\). Allowed functionals vanish on \(x\) and \(z\) and are determined by a nonzero pair \((\alpha=\varphi(1),\beta=\varphi(y))\). The line stabilizer contains maps \(x\mapsto\lambda x\), \(y\mapsto d y\) for arbitrary \(\lambda,d\in k^\times\), which send
\[
(\alpha,\beta)\longmapsto(\lambda\alpha,(\lambda/d)\beta).
\]
There are exactly three orbits according to which entries vanish; convenient representatives are
\[
(x,0,0,0),\quad(0,0,x,0),\quad(x,0,x,0).
\]
For each of the \(q^2+q\) image lines, the numbers of allowed functionals in those three orbits are \(q-1\), \(q-1\), \((q-1)^2\). Multiplication by the number of image lines gives the last three claimed sizes. Thus the six invariant strata exhaust all nonzero rank-one weight-zero operators, and every stratum is a single orbit.

## Verification

The standalone arithmetic procedure `artifacts/verify.py` enumerates all rank-one linear endomorphisms via projectively normalized image vectors and all nonzero linear functionals for \(q=2,3\). It tests the Rota–Baxter equation on all sixteen ordered basis pairs (sufficient by bilinearity), computes the full unital algebra automorphism groups, generates the orbits by conjugation, and checks that each invariant stratum is exactly one orbit. A separately implemented \(\mathbb F_4\) arithmetic checker (`artifacts/verify_f4.py`) repeats the complete computation over the first extension field, including all \(2880\) algebra automorphisms. The first checker also tests \(\mathbb F_3\) as an out-of-scope algebraic stress test. The actual combined output is

```text
q= 2 rank1= 25 orbit_sizes= [1, 3, 3, 6, 6, 6] automorphisms= 24
q= 3 rank1= 122 orbit_sizes= [2, 8, 16, 24, 24, 48] automorphisms= 432
VERIFY_OK
q= 4 rank1= 363 orbit_sizes= [3, 15, 45, 60, 60, 180] automorphisms= 2880
VERIFY_F4_OK
```

A separate projective-image/covector enumeration also returns \(25,122,844,3030\) for prime-field sizes \(q=2,3,5,7\), agreeing with the formula. These finite checks are corroboration; the general proof is the argument above and applies equally to extension fields.

## Relationship to prior work

Shakoor and Noor-ul-Ain, *The Classification of the Rota-Baxter Operators on Four-dimensional Grassmann Algebra* (arXiv:2609.07377, first public September 7, 2026), give a full real-coefficient classification of weight-zero and nonzero-weight operators on this four-dimensional algebra. Their Theorem 4.1 is inspected in full: its statements concern real matrix families, not exact finite-field counts or conjugacy orbit sizes.

Hua and Liu, *Rota-Baxter Operators on Exterior Algebra* (2013), classify operators on the exterior algebra on two variables over an **algebraically closed field of characteristic different from two**, according to the available journal abstract; it is a particularly relevant antecedent. It may imply part of the characteristic-odd parameter classification, but does not directly provide the finite-field point counts, characteristic-two family, or six-orbit sizes asserted here. The full 2013 article was not accessible to inspect, an explicit literature limitation.

An earlier finite-field computation classifies all weight-zero operators over \(\mathbb F_2\): it reports \(80\) operators, of which \(25\) have rank one and split into six automorphism orbits with sizes \(1,3,3,6,6,6\). That covered special case is **not** claimed as original here. The present theorem concerns the previously untreated extension fields of characteristic two, \(q=2^e\) with \(e\ge2\), and computes the entire natural rank-one stratum and its conjugacy classes.

## Limitations

The classification is specifically claimed for nonzero rank-one weight-zero operators on the two-generator exterior algebra over finite fields \(\mathbb F_{2^e}\) with \(e\ge2\). It does not classify higher-rank operators, nonzero weights, higher exterior rank, or inequivalent dendriform algebras. As with any literature search, older or unindexed calculations may duplicate part of the result; the 2013 antecedent is an identified incomplete full-text comparison. The proof uses identities that also make sense in other characteristics; finite-field formulas outside the stated characteristic-two family are not asserted as novel. Exhaustive automorphism enumeration was run over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_4\).

## References

1. K. Shakoor and Noor-ul-Ain, *The Classification of the Rota-Baxter Operators on Four-dimensional Grassmann Algebra*, arXiv:2609.07377v1 (2026-09-07), updated v2 (2026-10-08). https://arxiv.org/html/2609.07377v2
2. X. Y. Hua and W. D. Liu, *Rota-Baxter Operators on Exterior Algebra*, Journal of Harbin University of Science and Technology **18** (2013), no. 4, 125–128 (in Chinese). Characteristic restriction reported in the available abstract.
3. V. Gubarev, *Rota–Baxter operators on unital algebras*, Moscow Mathematical Journal **21** (2021), no. 2, 325–364, arXiv:1805.00723; supplies a bibliographic reference to Hua–Liu and general background.
