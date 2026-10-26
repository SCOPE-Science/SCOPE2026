# Weight-zero Rota–Baxter operators on the cubic truncated polynomial algebra

## Finding

Let \(k\) be any field and let \(A=k[t]/(t^3)\). The weight-zero Rota–Baxter operators \(P:A\to A\), meaning \(k\)-linear maps satisfying
\[
P(u)P(v)=P(P(u)v+uP(v))\qquad (u,v\in A),
\]
are **exactly**
\[
P(1)=at+bt^2,\qquad P(t)=ct^2,\qquad P(t^2)=0,
\qquad a(a-2c)=0.
\]
Here \(a,b,c\in k\). Every such operator satisfies \(P^3=0\), and \(P^2(1)=ac\,t^2\).

For a finite field \(k=\mathbb F_q\), the **number of distinct operators** is
\[
\#\operatorname{RB}_0(A)=
\begin{cases}q^2,&\operatorname{char}k=2,\\ q(2q-1),&\operatorname{char}k\ne2.\end{cases}
\]
For odd \(q\), exactly \(q(q-1)\) have \(P^2\ne0\) (nilpotency index three), while every weight-zero operator in characteristic two has \(P^2=0\).

The **number of isomorphism classes**, where two operators are identified when conjugate by an algebra automorphism, is
\[
\#\bigl(\operatorname{RB}_0(A)/\operatorname{Aut}_k(A)\bigr)=
\begin{cases}q+2,&\operatorname{char}k=2,\\ q+4,&\operatorname{char}k\ne2.\end{cases}
\]
The formulas apply also to nonprime finite fields.

## Assumptions and scope

The algebra \(A\) is **unital** and commutative, with basis \((1,t,t^2)\), radical \((t)\), and nonzero radical square \((t^2)\). We classify every \(k\)-linear map satisfying the weight-zero Rota–Baxter identity, not only monomial maps, endomorphisms, or maps preserving the radical by assumption. We allow all field characteristics. Nilpotency index three means \(P^3=0\) and \(P^2\ne0\).

## Proof

**1. Forced form.** Write
\[
P(t^2)=d_0+d_1t+d_2t^2.
\]
Apply the defining identity with \((u,v)=(t^2,t^2)\). Since \(t^4=0\), its right side is \(P(2d_0t^2)=2d_0P(t^2)\). Comparing the constant coefficients yields \(d_0^2=2d_0^2\), hence \(d_0=0\), even in characteristic two. Comparing the \(t^2\)-coefficients then gives \(d_1^2=0\), hence \(d_1=0\). Therefore \(P(t^2)=d_2t^2\).

Apply the identity to \((u,v)=(1,t^2)\). If \(P(1)=a_0+a_1t+a_2t^2\), the left side is \(a_0d_2t^2\); the right side is \(P((a_0+d_2)t^2)=(a_0+d_2)d_2t^2\). Thus \(d_2^2=0\) and \(d_2=0\). Consequently \(P(t^2)=0\).

Write \(P(t)=c_0+c_1t+c_2t^2\). For \((u,v)=(t,t)\), the identity becomes \(P(t)^2=P(2tP(t))=2c_0P(t)\), since \(P(t^2)=0\). Constant coefficients yield \(c_0^2=2c_0^2\), so \(c_0=0\). The coefficient of \(t^2\) yields \(c_1^2=0\), so \(c_1=0\). Hence \(P(t)=c_2t^2\).

Write again \(P(1)=a_0+a_1t+a_2t^2\). For \((u,v)=(1,1)\), the identity reads \(P(1)^2=2P(P(1))\). The constant coefficients give \(a_0^2=2a_0^2\), and therefore \(a_0=0\). The \(t^2\)-coefficients give \(a_1^2=2a_1c_2\). Set \(a=a_1\), \(b=a_2\), \(c=c_2\). This gives precisely the claimed form and equation.

**2. Sufficiency and consequences.** Conversely, define \(P\) by the displayed form with \(a(a-2c)=0\). Since the weight-zero Rota–Baxter identity is bilinear, it suffices to check the six unordered pairs of basis elements. All pairs involving \(t^2\) vanish on both sides; \((t,t)\) and \((1,t)\) also satisfy the identity immediately. The remaining pair \((1,1)\) is equivalent to \(a^2=2ac\). Thus all listed maps, and only those, qualify. Further, \(P^2(1)=ac\,t^2\), \(P^2(t)=P^2(t^2)=0\), and \(P^3=0\).

If \(\operatorname{char}k=2\), the equation is \(a^2=0\) so \(a=0\), while \(b,c\) are arbitrary, giving \(q^2\) maps. In odd characteristic, the equation factors as \(a(a-2c)=0\); the branch \(a=0\) has \(q^2\) points, and the branch \(a=2c\) has \(q^2\), overlapping in \(q\) points with \(a=c=0\). Hence there are \(q(2q-1)\) maps. Exactly the \(q(q-1)\) points in the second branch with \(c\ne0\) satisfy \(ac\ne0\).

**3. Automorphism orbits.** Every algebra automorphism has the unique form
\[
\phi_{u,v}(t)=ut+vt^2,\qquad u\in k^\times,\ v\in k.
\]
A direct calculation shows that \(\phi_{u,v}P\phi_{u,v}^{-1}\) sends the parameters to
\[
(a,b,c)\longmapsto(ua,\;u^2b+av,\;uc).
\]
If \(a=0,c\ne0\), scaling by \(u=c^{-1}\) gives \(c=1\) and the invariant \(\beta=b/c^2\in k\); over \(\mathbb F_q\) this yields **exactly \(q\) orbits**. If \(a=c=0\), the zero operator is one orbit, and the maps with \(b\ne0\) are classified by the square classes \(k^\times/(k^\times)^2\): there are **two** nonzero orbits for odd \(q\), and **one** for even \(q\). Finally, if \(a\ne0\), the constraint forces odd characteristic and \(a=2c\). Scaling normalizes \(a=1\), after which choosing \(v\) sets \(b=0\); this forms **one orbit**. Adding these disjoint cases gives \(q+4\) orbits for odd \(q\) and \(q+2\) for even \(q\), as claimed.

## Verification

The independent script `verify.py` constructs the algebra multiplication, tests the Rota–Baxter identity on every unordered pair of basis vectors, enumerates every linear operator on the three-dimensional vector space over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_4\), and compares that complete census to the classification. For \(\mathbb F_5\) it evaluates the identity on all operators in the parametrized classification and verifies the predicted orbit counts. It constructs the automorphism action independently and computes each orbit.

Observed data:
\[
\begin{array}{c|c|c|c}
q & \text{exhaustive all linear maps} & \#\text{operators} & \#\text{automorphism orbits}\\\hline
2 & \text{yes} & 4 & 4\\
3 & \text{yes} & 15 & 7\\
4 & \text{yes} & 16 & 6\\
5 & \text{candidate replay} & 45 & 9
\end{array}
\]
The checker reports `VERIFY_OK`. These finite computations are consistency checks, not an infinite-field proof.

## Relationship to prior work

Guo–Rosenkranz–Zheng (arXiv:1402.3702v1, 2014) classify weight-zero operators on semigroup algebras of semigroup orders two and three, working in characteristic zero. Their stated objects are semigroup algebras and their tables do not provide the all-field classification or finite-field conjugacy-orbit counts for the unital local algebra \(k[t]/(t^3)\).

Guo–Zheng–Rosenkranz (arXiv:1407.5306v1, 2014) study monomial and injective operators on the untruncated polynomial algebra \(k[t]\). Restriction to a quotient is not automatic and does not classify arbitrary linear operators on \(k[t]/(t^3)\).

The later paper by Farooq (arXiv:2605.15670v1, 2026) classifies weights zero and one for the **square-zero** truncation \(k[x_1,\ldots,x_m]/(x_1,\ldots,x_m)^2\) in characteristic zero. The present algebra has nonzero radical square, and the index-three and characteristic-two phenomena are not determined by its classification.

Aliyeva (2021) and Abdujabborov–Karimjanov–Kodirova (2021) classify operators on **nilpotent (nonunital)** three-dimensional associative algebras over \(\mathbb C\). Their algebras differ from the present unital local algebra; their classifications do not give finite-field operator counts or automorphism orbits here.

The comparison establishes best-knowledge distinction from these sources; it is not a proof of absolute publication priority.

## Limitations

Only weight **zero** is classified. The results do not cover higher truncations \(k[t]/(t^m)\) for \(m\ge4\), multivariable truncations, or all finite-dimensional local algebras. The orbit count assumes finite fields; over arbitrary fields, square-class groups may be infinite, while the parameter classification remains valid. The published-literature comparison is bounded, and previously unindexed equivalent work remains possible. No independent audit was performed.

## References

1. L. Guo, M. Rosenkranz, S. Zheng, *Classification of Rota-Baxter operators on semigroup algebras of order two and three*, arXiv:1402.3702v1 (first public 2014-02-15; MSC 16W99).
2. L. Guo, S. Zheng, M. Rosenkranz, *Rota-Baxter operators on the polynomial algebras, integration and averaging operators*, arXiv:1407.5306v1 (2014).
3. A. Farooq, *Rota–Baxter Operators on Truncated Polynomial Algebras*, arXiv:2605.15670v1 (2026), square-zero truncations.
4. J. Aliyeva, *Rota-Baxter Operators on 3-Dimensional Nilpotent Associative Algebras*, International Journal on Integrated Education 4(10) (2021), pp. 198–201.
5. N. G. Abdujabborov, I. Karimjanov, M. Kodirova, *Rota-type operators on 3-dimensional nilpotent associative algebras*, Communications in Mathematics 29(2) (2021), pp. 227–241, DOI:10.2478/cm-2021-0020.
